# NI DOCUMENT BUNDLE: diadem

<!--NI_BUNDLE_CHUNK bundle=diadem start=1 end=250 -->
<!--NI_TOPIC bundle=diadem path=comonl/dcsudscommunicationmodeset.htm language=enus -->
## TOPIC 00001: Command: DCSUDSCommunicationModeSet

- bundle_id: `diadem`
- source_path: `comonl/dcsudscommunicationmodeset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcsudscommunicationmodeset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSUDSCommunicationModeSet

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSUDSCommunicationModeSet

Switches the transmission and the reception of normal messages (mostly CAN messages) on or off.

Call DCSUDSCommunicationModeSet(DCSDiagRef, DCSCommunicationMask, DCSCommunicationType)

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |
| DCSCommunicationMask | Specifies the data to be transferred. Longinteger variable Access: Read only The variable can have the following values: ValueMeaning 00Rx on, Tx on 01Rx on, Tx off 02Rx off, Tx on 03Rx off, Tx off |
| Longinteger variable |  |
| Access: Read only |  |
| Value | Meaning |
| 00 | Rx on, Tx on |
| 01 | Rx on, Tx off |
| 02 | Rx off, Tx on |
| 03 | Rx off, Tx off |
| DCSCommunicationType | Specifies the application level to be changed. Longinteger variable Access: Read only The variable can have the following values: ValueMeaning 01Application02Network management You can change several levels at the same time. |
| Longinteger variable |  |
| Access: Read only |  |
| Value | Meaning |
| 01 | Application |
| 02 | Network management |

<!--NI_TOPIC bundle=diadem path=comonl/dcsudsioportmodeset.htm language=enus -->
## TOPIC 00002: Command: DCSUDSIOPortModeSet

- bundle_id: `diadem`
- source_path: `comonl/dcsudsioportmodeset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcsudsioportmodeset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSUDSIOPortModeSet

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSUDSIOPortModeSet

Specifies the behavior of the I/O port of the engine control unit (ECU).

ReturnValue

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |
| DCSID | Specifies the routine ID. Longinteger variable Access: Read only |
| Longinteger variable |  |
| Access: Read only |  |
| DCSUDSIOControlMode | Specifies the I/O control type. The application determines the settings. Longinteger variable Access: Read only The variable can have the following values: ValueMeaning 0Returns the control to the engine control unit 1Sets the default value 2Freezes the current status 3Short-term adjustment |
| Longinteger variable |  |
| Access: Read only |  |
| Value | Meaning |
| 0 | Returns the control to the engine control unit |
| 1 | Sets the default value |
| 2 | Freezes the current status |
| 3 | Short-term adjustment |
| DCSData | Specifies the user-defined date for a service. Variant variable |
| Variant variable |  |

#### Return Parameters

| ReturnValue | Receives the user-defined date for a service. The return value is a DCSData type. Variant variable |
| --- | --- |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/dcsudsmemoryread.htm language=enus -->
## TOPIC 00003: Command: DCSUDSMemoryRead

- bundle_id: `diadem`
- source_path: `comonl/dcsudsmemoryread.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcsudsmemoryread.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSUDSMemoryRead

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSUDSMemoryRead

Reads data from the ECU memory.

ReturnValue

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |
| DCSMemoryAddress | Specifies the memory address of the data. Floating-point number variable Access: Read only |
| Floating-point number variable |  |
| Access: Read only |  |
| DCSMemorySize | Specifies the memory size of the data block. Floating-point number variable Access: Read only |
| Floating-point number variable |  |
| Access: Read only |  |

#### Return Parameters

| ReturnValue | Receives the user-defined date for a service. The return value is a DCSData type. Variant variable |
| --- | --- |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/dcsudsmemorywrite.htm language=enus -->
## TOPIC 00004: Command: DCSUDSMemoryWrite

- bundle_id: `diadem`
- source_path: `comonl/dcsudsmemorywrite.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcsudsmemorywrite.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSUDSMemoryWrite

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSUDSMemoryWrite

Writes data into the ECU memory.

Call DCSUDSMemoryWrite(DCSDiagRef, DCSMemoryAddress, DCSData)

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |
| DCSMemoryAddress | Specifies the memory address of the data. Floating-point number variable Access: Read only |
| Floating-point number variable |  |
| Access: Read only |  |
| DCSData | Specifies the user-defined date for a service. Variant variable |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/dcsudsroutineexecute.htm language=enus -->
## TOPIC 00005: Command: DCSUDSRoutineExecute

- bundle_id: `diadem`
- source_path: `comonl/dcsudsroutineexecute.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcsudsroutineexecute.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSUDSRoutineExecute

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSUDSRoutineExecute

Executes a routine on the engine control unit (ECU).

ReturnValue

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |
| DCSID | Specifies the routine ID. Longinteger variable Access: Read only |
| Longinteger variable |  |
| Access: Read only |  |
| DCSUDSExecuteMode | Specifies the execution mode of the service. Longinteger variable Access: Read only The variable can have the following values: ValueMeaning 01Starts the routine 02Stops the routing 03Requests the routine results >3Application specific |
| Longinteger variable |  |
| Access: Read only |  |
| Value | Meaning |
| 01 | Starts the routine |
| 02 | Stops the routing |
| 03 | Requests the routine results |
| >3 | Application specific |
| DCSData | Specifies the user-defined date for a service. Variant variable |
| Variant variable |  |

#### Return Parameters

| ReturnValue | Receives the user-defined date for a service. The return value is a DCSData type. Variant variable |
| --- | --- |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/dcsudssecurityaccessseedget.htm language=enus -->
## TOPIC 00006: Command: DCSUDSSecurityAccessSeedGet

- bundle_id: `diadem`
- source_path: `comonl/dcsudssecurityaccessseedget.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcsudssecurityaccessseedget.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSUDSSecurityAccessSeedGet

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSUDSSecurityAccessSeedGet

Requests in a security prompt a random number (seed) from the engine control unit (ECU) in order to generate a key code (key).

ReturnValue

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |
| DCSAccessMode | Specifies which security level to release on the engine control unit (ECU). Longinteger variable Access: Read only |
| Longinteger variable |  |
| Access: Read only |  |

#### Return Parameters

| ReturnValue | Receives the user-defined date for a service. The return value is a DCSData type. Variant variable |
| --- | --- |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/dcsudstesterpresentserviceexecute.htm language=enus -->
## TOPIC 00007: Command: DCSUDSTesterPresentServiceExecute

- bundle_id: `diadem`
- source_path: `comonl/dcsudstesterpresentserviceexecute.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcsudstesterpresentserviceexecute.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSUDSTesterPresentServiceExecute

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSUDSTesterPresentServiceExecute

Executes a Tester Present Service to keep the engine control unit (ECU) in the diagnostic mode.

Call DCSUDSTesterPresentServiceExecute(DCSDiagRef, DCSResponseRequired)

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |
| DCSResponseRequired | Specifies whether a service requires a response. Boolean Variable Access: Read only |
| Boolean Variable |  |
| Access: Read only |  |

<!--NI_TOPIC bundle=diadem path=comonl/dcsvwtpconnect.htm language=enus -->
## TOPIC 00008: Command: DCSVWTPConnect

- bundle_id: `diadem`
- source_path: `comonl/dcsvwtpconnect.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcsvwtpconnect.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSVWTPConnect

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSVWTPConnect

Creates a connection to the engine control unit (ECU) over the VW TP 2.0 transmission protocol.

Call DCSVWTPConnect(DCSDiagRef, DCSVWTPChannelID, DCSVWTPApplicationType)

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |
| DCSVWTPChannelID | Specifies to which CAN message identifier the engine control unit (ECU) answers. Floating-point number variable Access: Read only |
| Floating-point number variable |  |
| Access: Read only |  |
| DCSVWTPApplicationType | Specifies which communication type to use. Longinteger variable Access: Read only The variable can have the following values: ValueMeaning 1Diagnosis applications (KWP2000)<>1Manufacturer-specific |
| Longinteger variable |  |
| Access: Read only |  |
| Value | Meaning |
| 1 | Diagnosis applications (KWP2000) |
| <>1 | Manufacturer-specific |

<!--NI_TOPIC bundle=diadem path=comonl/dcsvwtpdisconnect.htm language=enus -->
## TOPIC 00009: Command: DCSVWTPDisconnect

- bundle_id: `diadem`
- source_path: `comonl/dcsvwtpdisconnect.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcsvwtpdisconnect.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSVWTPDisconnect

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSVWTPDisconnect

Disconnects the VW TP 2.0 transmission protocol and the engine control unit (ECU).

Call DCSVWTPDisconnect(DCSDiagRef)

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |

<!--NI_TOPIC bundle=diadem path=comonl/dcswwhconvertdtcstoj2012.htm language=enus -->
## TOPIC 00010: Command: DCSWWHConvertDTCsToJ2012

- bundle_id: `diadem`
- source_path: `comonl/dcswwhconvertdtcstoj2012.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcswwhconvertdtcstoj2012.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSWWHConvertDTCsToJ2012

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSWWHConvertDTCsToJ2012

Converts a list with diagnostic trouble codes (DTCs) into the J2012 DTC format.

ReturnValue

#### Input Parameters

| DCSDTCList | Specifies the list with the diagnostic trouble codes. Variant variable |
| --- | --- |
| Variant variable |  |

#### Return Parameters

| ReturnValue | Receives the list of DTCs in the J2012 format. Type DCSWWHDTCJ2012List return value. Variant variable |
| --- | --- |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/dcswwhdidrequest.htm language=enus -->
## TOPIC 00011: Command: DCSWWHDIDRequest

- bundle_id: `diadem`
- source_path: `comonl/dcswwhdidrequest.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcswwhdidrequest.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSWWHDIDRequest

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSWWHDIDRequest

Reads a data set from the ECU.

ReturnValue

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |
| DCSWWHDataIdentifier | Specifies the data identifier of the data to be read. The SAE J1979DA standard determines the values. Longinteger variable Access: Read only |
| Longinteger variable |  |
| Access: Read only |  |
| DCSReturnDataAsString | Specifies whether DIAdem returns the result of an ADCS function as a string. Boolean variable Access: Read only |
| Boolean variable |  |
| Access: Read only |  |

#### Return Parameters

| ReturnValue | Receives the user-defined date for a service. The return value is a DCSData type. Variant variable |
| --- | --- |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/dcswwhdtcextendeddatarecordrequest.htm language=enus -->
## TOPIC 00012: Command: DCSWWHDTCExtendedDataRecordRequest

- bundle_id: `diadem`
- source_path: `comonl/dcswwhdtcextendeddatarecordrequest.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcswwhdtcextendeddatarecordrequest.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSWWHDTCExtendedDataRecordRequest

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSWWHDTCExtendedDataRecordRequest

Reads the selected diagnostic trouble codes (DTCs).

ReturnValue

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |
| DCSData | Specifies the user-defined date for a service. Variant variable |
| Variant variable |  |

#### Return Parameters

| ReturnValue | Receives the user-defined date for a service. The return value is a DCSData type. Variant variable |
| --- | --- |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/dcswwhemissiondtcsclear.htm language=enus -->
## TOPIC 00013: Command: DCSWWHEmissionDTCsClear

- bundle_id: `diadem`
- source_path: `comonl/dcswwhemissiondtcsclear.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcswwhemissiondtcsclear.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSWWHEmissionDTCsClear

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSWWHEmissionDTCsClear

Deletes the selected diagnostic trouble codes (DTCs).

Call DCSWWHEmissionDTCsClear(DCSDiagRef)

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |

<!--NI_TOPIC bundle=diadem path=comonl/dcswwhemissiondtcsrequest.htm language=enus -->
## TOPIC 00014: Command: DCSWWHEmissionDTCsRequest

- bundle_id: `diadem`
- source_path: `comonl/dcswwhemissiondtcsrequest.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcswwhemissiondtcsrequest.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSWWHEmissionDTCsRequest

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSWWHEmissionDTCsRequest

Reads the selected diagnostic trouble codes (DTCs).

ReturnValue

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |
| DCSSeverityMask | Specifies the information on the severity of diagnostic trouble codes (TDC) to be read. Longinteger variable Access: Read only |
| Longinteger variable |  |
| Access: Read only |  |
| DCSStatusMask | Specifies the status of the diagnostic trouble codes (TDC) to be read. Longinteger variable Access: Read only |
| Longinteger variable |  |
| Access: Read only |  |
| DCSDTCDescriptor | Specifies the structure of a diagnostic trouble code. Variant variable Use the DCSDTCDescriptorInit command to initialize the data structure. |
| Variant variable |  |

#### Return Parameters

| ReturnValue | Receives the list with the diagnostic trouble codes. The return value is a DCSDTCList type. Variant variable |
| --- | --- |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/dcswwhfreezeddatarequest.htm language=enus -->
## TOPIC 00015: Command: DCSWWHFreezedDataRequest

- bundle_id: `diadem`
- source_path: `comonl/dcswwhfreezeddatarequest.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcswwhfreezeddatarequest.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSWWHFreezedDataRequest

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSWWHFreezedDataRequest

Reads the selected diagnostic trouble codes (DTCs).

ReturnValue

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |
| DCSWWHMaskRecord | Specifies the DTC mask data set. Variant variable |
| Variant variable |  |
| DCSWWHRecordNumber | Specifies the data set number of the snap shot. Longinteger variable Access: Read only |
| Longinteger variable |  |
| Access: Read only |  |

#### Return Parameters

| ReturnValue | Receives the user-defined date for a service. The return value is a DCSData type. Variant variable |
| --- | --- |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/dcswwhridrequest.htm language=enus -->
## TOPIC 00016: Command: DCSWWHRIDRequest

- bundle_id: `diadem`
- source_path: `comonl/dcswwhridrequest.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcswwhridrequest.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSWWHRIDRequest

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSWWHRIDRequest

Reads a data set from the ECU.

ReturnValue

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |
| DCSWWHRIDMode | Specifies the working mode for the service. Longinteger variable Access: Read only |
| Longinteger variable |  |
| Access: Read only |  |
| DCSWWHRoutineID | Specifies the user-defined identifier of the routine to be started. Longinteger variable Access: Read only |
| Longinteger variable |  |
| Access: Read only |  |

#### Return Parameters

| ReturnValue | Receives the user-defined date for a service. The return value is a DCSData type. Variant variable |
| --- | --- |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/dcswwhsupporteddidsrequest.htm language=enus -->
## TOPIC 00017: Command: DCSWWHSupportedDIDsRequest

- bundle_id: `diadem`
- source_path: `comonl/dcswwhsupporteddidsrequest.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/dcswwhsupporteddidsrequest.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: DCSWWHSupportedDIDsRequest

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: DCSWWHSupportedDIDsRequest

Executes the WWH-OBD ReadDataByIdentifier service in order to get a list of the supported DIDs.

ReturnValue

#### Input Parameters

| DCSDiagRef | Specifies the diagnostic handle in a vehicle. Longinteger variable Access: Read only |
| --- | --- |
| Longinteger variable |  |
| Access: Read only |  |
| DCSWWHDID | Specifies the Diagnostic Data Identifier for this service. Longinteger variable Access: Read only |
| Longinteger variable |  |
| Access: Read only |  |

#### Return Parameters

| ReturnValue | Receives a list of valid DIDs. Type DCSWWHDIDList return value. Variant variable |
| --- | --- |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/ecuconnect.htm language=enus -->
## TOPIC 00018: Command: ECUConnect

- bundle_id: `diadem`
- source_path: `comonl/ecuconnect.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/ecuconnect.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: ECUConnect

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: ECUConnect

Establishes communication to the selected ECU through CCP or XCP. After a successful ECU connect you can create a measurement task or read/write a characteristic.

Call ECUConnect(ECUDeviceHandle)

#### Input Parameters

| ECUDeviceHandle | Specifies the handle for the ECU. Longinteger variable -21474836487 <= ECUDeviceHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| -21474836487 <= ECUDeviceHandle <= 2147483647 |  |

<!--NI_TOPIC bundle=diadem path=comonl/ecudatabaseclose.htm language=enus -->
## TOPIC 00019: Command: ECUDatabaseClose

- bundle_id: `diadem`
- source_path: `comonl/ecudatabaseclose.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/ecudatabaseclose.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: ECUDatabaseClose

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: ECUDatabaseClose

Closes a specified A2L database.

ReturnValue

#### Input Parameters

| ECUDatabasehandle | Specifies the handle for an A2L database. Longinteger variable -21474836487 <= ECUDatabaseHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| -21474836487 <= ECUDatabaseHandle <= 2147483647 |  |

#### Return Parameters

| ReturnValue | Receives the handle for the database task. The return value is a ECUDatabasehandle type. Longinteger variable -21474836487 <= ECUDatabaseHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| -21474836487 <= ECUDatabaseHandle <= 2147483647 |  |

<!--NI_TOPIC bundle=diadem path=comonl/ecudatabaseopen.htm language=enus -->
## TOPIC 00020: Command: ECUDatabaseOpen

- bundle_id: `diadem`
- source_path: `comonl/ecudatabaseopen.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/ecudatabaseopen.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: ECUDatabaseOpen

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: ECUDatabaseOpen

Opens a specified A2L database.

ReturnValue

#### Input Parameters

| ECUDatabase | Specifies the path to an A2L database file which contains the description of the ECU. The file must use an A2L filename extension. String variable |
| --- | --- |
| String variable |  |

#### Return Parameters

| ReturnValue | Receives the handle for the database task. The return value is a ECUDatabasehandle type. Longinteger variable -21474836487 <= ECUDatabaseHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| -21474836487 <= ECUDatabaseHandle <= 2147483647 |  |

<!--NI_TOPIC bundle=diadem path=comonl/ecudisconnect.htm language=enus -->
## TOPIC 00021: Command: ECUDisconnect

- bundle_id: `diadem`
- source_path: `comonl/ecudisconnect.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/ecudisconnect.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: ECUDisconnect

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: ECUDisconnect

Disconnects the CCP communication or XCP communication from the selected ECU.

Call ECUDisconnect(ECUDeviceHandle)

#### Input Parameters

| ECUDeviceHandle | Specifies the handle for the ECU. Longinteger variable -21474836487 <= ECUDeviceHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| -21474836487 <= ECUDeviceHandle <= 2147483647 |  |

<!--NI_TOPIC bundle=diadem path=comonl/ecudownload.htm language=enus -->
## TOPIC 00022: Command: ECUDownload

- bundle_id: `diadem`
- source_path: `comonl/ecudownload.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/ecudownload.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: ECUDownload

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: ECUDownload

Downloads data to an ECU.

Call ECUDownload(ECUDeviceHandle, ECUTargetAddress, ECUTargetExtension, ECUData)

#### Input Parameters

| ECUDeviceHandle | Specifies the handle for the ECU. Longinteger variable -21474836487 <= ECUDeviceHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| -21474836487 <= ECUDeviceHandle <= 2147483647 |  |
| ECUTargetAddress | Specifies the address part of the destination address. Floating-point number variable 0 <= ECUTargetAddress <= 4294967295 |
| Floating-point number variable |  |
| 0 <= ECUTargetAddress <= 4294967295 |  |
| ECUTargetExtension | Contains the extension part of the destination address. Byte variable |
| Byte variable |  |
| ECUData | Contains the data which the ECU read or received. Variant variable |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/ecumemoryclear.htm language=enus -->
## TOPIC 00023: Command: ECUMemoryClear

- bundle_id: `diadem`
- source_path: `comonl/ecumemoryclear.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/ecumemoryclear.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: ECUMemoryClear

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: ECUMemoryClear

Clears the contents of the specified ECU memory.

Call ECUMemoryClear(ECUDeviceHandle, ECUTargetAddress, ECUTargetExtension, ECUBlockSize)

#### Input Parameters

| ECUDeviceHandle | Specifies the handle for the ECU. Longinteger variable -21474836487 <= ECUDeviceHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| -21474836487 <= ECUDeviceHandle <= 2147483647 |  |
| ECUTargetAddress | Specifies the address part of the destination address. Floating-point number variable 0 <= ECUTargetAddress <= 4294967295 |
| Floating-point number variable |  |
| 0 <= ECUTargetAddress <= 4294967295 |  |
| ECUTargetExtension | Contains the extension part of the destination address. Byte variable |
| Byte variable |  |
| ECUBlockSize | Specifies the block size in bytes. Floating-point number variable 0 <= ECUBlockSize <= 4294967295 |
| Floating-point number variable |  |
| 0 <= ECUBlockSize <= 4294967295 |  |

<!--NI_TOPIC bundle=diadem path=comonl/ecunamelistget.htm language=enus -->
## TOPIC 00024: Command: ECUNameListGet

- bundle_id: `diadem`
- source_path: `comonl/ecunamelistget.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/ecunamelistget.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: ECUNameListGet

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: ECUNameListGet

Calls a list with the names of all ECUs, Measurements, Characteristics, Events, Characteristic pages, or Groups from a specified A2L database.

ReturnValue

#### Input Parameters

| ECUHandle | Specifies the handle you use to access the ECU. Longinteger variable -21474836487 <= ECUHandle <= 2147483647 |  |
| --- | --- | --- |
| Longinteger variable |  |  |
| -21474836487 <= ECUHandle <= 2147483647 |  |  |
| ECUNameSelector | Specifies the type to be returned. Longinteger variable 0 <= ECUNameSelector <= 20 The variable can accept the following values: 0eECUNamesECUsAll ECUs defined in the A2L file 1eECUNamesMeasurementsAll measurements defined in the A2L file 2eECUNamesCharacteristicsAll characteristics defined in the A2L file 3eECUNamesEventChannelsAll event channels defined in the A2L file 4eECUNamesDefinedPagesAll memory pages defined in the A2L file 5eECUNamesGroupsAll groups defined in the A2L file 6eECUNamesSubGroupsAll subgroups defined in the ECUName group 7eECUNamesGroupMeasurementsAll measurements defined in the ECUName group 8eECUNamesGroupCharacteristicsAll characteristics defined in the ECUName group |  |
| Longinteger variable |  |  |
| 0 <= ECUNameSelector <= 20 |  |  |
| 0 | eECUNamesECUs | All ECUs defined in the A2L file |
| 1 | eECUNamesMeasurements | All measurements defined in the A2L file |
| 2 | eECUNamesCharacteristics | All characteristics defined in the A2L file |
| 3 | eECUNamesEventChannels | All event channels defined in the A2L file |
| 4 | eECUNamesDefinedPages | All memory pages defined in the A2L file |
| 5 | eECUNamesGroups | All groups defined in the A2L file |
| 6 | eECUNamesSubGroups | All subgroups defined in the ECUName group |
| 7 | eECUNamesGroupMeasurements | All measurements defined in the ECUName group |
| 8 | eECUNamesGroupCharacteristics | All characteristics defined in the ECUName group |
| ECUName | Specifies the name for accessing an element in an A2L database file. This name is, for example, the name of an ECU, a Characteristic, or a Measurement. String variable |  |
| String variable |  |  |

#### Return Parameters

| ReturnValue | Contains a list of names separated by commas from the specified type. The return value is a ECUNameList type. Variant variable |
| --- | --- |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/ecuprogram.htm language=enus -->
## TOPIC 00025: Command: ECUProgram

- bundle_id: `diadem`
- source_path: `comonl/ecuprogram.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/ecuprogram.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: ECUProgram

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: ECUProgram

Programs a memory block on the ECU.

Call ECUProgram(ECUDeviceHandle, ECUTargetAddress, ECUTargetExtension, ECUData)

#### Input Parameters

| ECUDeviceHandle | Specifies the handle for the ECU. Longinteger variable -21474836487 <= ECUDeviceHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| -21474836487 <= ECUDeviceHandle <= 2147483647 |  |
| ECUTargetAddress | Specifies the address part of the destination address. Floating-point number variable 0 <= ECUTargetAddress <= 4294967295 |
| Floating-point number variable |  |
| 0 <= ECUTargetAddress <= 4294967295 |  |
| ECUTargetExtension | Contains the extension part of the destination address. Byte variable |
| Byte variable |  |
| ECUData | Contains the data which the ECU read or received. Variant variable |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/ecuprogramreset.htm language=enus -->
## TOPIC 00026: Command: ECUProgramReset

- bundle_id: `diadem`
- source_path: `comonl/ecuprogramreset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/ecuprogramreset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: ECUProgramReset

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: ECUProgramReset

Identifies the end of programming on the ECU.

Call ECUProgramReset(ECUDeviceHandle)

#### Input Parameters

| ECUDeviceHandle | Specifies the handle for the ECU. Longinteger variable -21474836487 <= ECUDeviceHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| -21474836487 <= ECUDeviceHandle <= 2147483647 |  |

<!--NI_TOPIC bundle=diadem path=comonl/ecuprogramstart.htm language=enus -->
## TOPIC 00027: Command: ECUProgramStart

- bundle_id: `diadem`
- source_path: `comonl/ecuprogramstart.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/ecuprogramstart.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: ECUProgramStart

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: ECUProgramStart

Identifies the start of programming on the ECU.

Call ECUProgramStart(ECUDeviceHandle)

#### Input Parameters

| ECUDeviceHandle | Specifies the handle for the ECU. Longinteger variable -21474836487 <= ECUDeviceHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| -21474836487 <= ECUDeviceHandle <= 2147483647 |  |

<!--NI_TOPIC bundle=diadem path=comonl/ecuxcpcalibpageset.htm language=enus -->
## TOPIC 00028: Command: ECUXCPCalibPageSet

- bundle_id: `diadem`
- source_path: `comonl/ecuxcpcalibpageset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/ecuxcpcalibpageset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: ECUXCPCalibPageSet

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: ECUXCPCalibPageSet

Sets a calibration page.

Call ECUXCPCalibPageSet(ECUDeviceHandle, ECUMode, ECUSegment, ECUPage)

#### Input Parameters

| ECUDeviceHandle | Specifies the handle for the ECU. Longinteger variable -21474836487 <= ECUDeviceHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| -21474836487 <= ECUDeviceHandle <= 2147483647 |  |
| ECUMode | Specifies a bit mask which describes the mode. Byte variable |
| Byte variable |  |
| ECUSegment | Specifies the logical number of the data segment. Byte variable |
| Byte variable |  |
| ECUPage | Specifies the logical page number. Byte variable |
| Byte variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/ecuxcpidget.htm language=enus -->
## TOPIC 00029: Command: ECUXCPIdGet

- bundle_id: `diadem`
- source_path: `comonl/ecuxcpidget.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/ecuxcpidget.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: ECUXCPIdGet

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: ECUXCPIdGet

Retrieves the session configuration or the slave device identification.

ReturnValue

#### Input Parameters

| ECUDeviceHandle | Specifies the handle for the ECU. Longinteger variable -21474836487 <= ECUDeviceHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| -21474836487 <= ECUDeviceHandle <= 2147483647 |  |
| ECUXCPIdSelector | Specifies the type of requested identification. Byte variable 0 <= ECUXCPIDSelector <= 4 |
| Byte variable |  |
| 0 <= ECUXCPIDSelector <= 4 |  |

#### Return Parameters

| ReturnValue | Receives the requested ID string. The return value is a ECUXCPId type. Variant variable |
| --- | --- |
| Variant variable |  |

<!--NI_TOPIC bundle=diadem path=comonl/opcclearserver.htm language=enus -->
## TOPIC 00030: Command: OPCClearServer

- bundle_id: `diadem`
- source_path: `comonl/opcclearserver.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/opcclearserver.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: OPCClearServer

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: OPCClearServer

Deletes all OPC items and OPC groups on an OPC server.

Call OPCClearServer(OPCSrvHandle)

#### Input Parameters

| OPCSrvHandle | Specifies the handle for the connection to the OPC server. Longinteger variable 0 <= OPCSrvHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| 0 <= OPCSrvHandle <= 2147483647 |  |

#### Return Parameters

| OPCErrorCode | Receives the status of the OPC command. Longinteger variable 0 <= OPCErrorCode <= 2147483647 The OPCErrorCode variable returns the number or the OPC code of the respective message: No. OPC code Description 0 eOPCAuto_Ok DIAdem executed the command without errors. 1 eOPCAuto_GeneralError A global error has occurred. 2 eOPCAuto_BlockMapEntryNotFound DIAdem cannot find entry for the signal and device specification in the driver blockmap. 3 eOPCAuto_UnidentifiedBlocktype The block type is not valid because no DAC input block or DAC output block open. 4 eOPCAuto_OPCBlockNotOpen No DAC block opened with the DACObjOpen command. 5 eOPCAuto_InvalidSignalIndex The signal index is not valid. Values from 1 to 255 are valid. 6 eOPCAuto_InvalidLogReset The value for the time of the logfile reset is not valid. 7 eOPCAuto_InvalidReportVerbosity The value for the type and extent of information to be recorded is not valid. 8 eOPCAuto_ProgIDNotInLocalRegistry DIAdem cannot find the transferred ProgID in the local registration. 9 eOPCAuto_ServerNotConnected The OPC server is not connected. 10 eOPCAuto_DataConversionFail Data could not be converted. 11 eOPCAuto_InvalidErrorAction The value provided for the error reaction is invalid. 12 eOPCAuto_InvalidDACSigListLen The length of the DAC signal list specified in the block is invalid. 13 eOPCAuto_InvalidServerName The name of the OPC server is invalid. 14 eOPCAuto_NotImplemented The function is not implemented. 15 eOPCAuto_RemoteConnectWithoutClassID Transfer the ClassID to the OPCSrvConnect command to access a remote server without local registration. You only can reference OPC servers on remote computers with the ProgID if the ProgID or the server are registered locally. 16 eOPCAuto_ArrayAccesNotAllowed The function cannot access arrays. 17 eOPCAuto_NoMoreHandles No more OPC objects possible in the script area. 18 eOPCAuto_InvalidServerHandle The server handle is invalid. 19 eOPCAuto_InvalidGroupHandle The group handle is invalid. 20 eOPCAuto_InvalidItemHandle The item handle is invalid. 21 eOPCAuto_ConnectTimeout Timeout occurred while connecting to OPC server. The server cannot be accessed or one of the Proxy-DLLs such as opcproxy.dll and opccomn_ps.dll, is not registered. 22 eOPCAuto_CallTimeout A timeout occurred while a function on an OPC server was being called. 23 eOPCAuto_NoIOPCServer No IOPCServer interface at OPC server. 24 eOPCAuto_NoIOPCItemMgt No IOPCItemMgt interface at OPC server. 25 eOPCAuto_NoIOPCSyncIO No IOPCSyncIO interface at OPC server. 26 eOPCAuto_NoIOPCGroupStateMgt No IOPCGroupStateMgt interface at OPC server. 27 eOPCAuto_InvalidItemNo The number of items is invalid or an OPC group contains more items than acceptable. |  |
| --- | --- | --- |
| Longinteger variable |  |  |
| 0 <= OPCErrorCode <= 2147483647 |  |  |
| No. | OPC code | Description |
| 0 | eOPCAuto_Ok | DIAdem executed the command without errors. |
| 1 | eOPCAuto_GeneralError | A global error has occurred. |
| 2 | eOPCAuto_BlockMapEntryNotFound | DIAdem cannot find entry for the signal and device specification in the driver blockmap. |
| 3 | eOPCAuto_UnidentifiedBlocktype | The block type is not valid because no DAC input block or DAC output block open. |
| 4 | eOPCAuto_OPCBlockNotOpen | No DAC block opened with the DACObjOpen command. |
| 5 | eOPCAuto_InvalidSignalIndex | The signal index is not valid. Values from 1 to 255 are valid. |
| 6 | eOPCAuto_InvalidLogReset | The value for the time of the logfile reset is not valid. |
| 7 | eOPCAuto_InvalidReportVerbosity | The value for the type and extent of information to be recorded is not valid. |
| 8 | eOPCAuto_ProgIDNotInLocalRegistry | DIAdem cannot find the transferred ProgID in the local registration. |
| 9 | eOPCAuto_ServerNotConnected | The OPC server is not connected. |
| 10 | eOPCAuto_DataConversionFail | Data could not be converted. |
| 11 | eOPCAuto_InvalidErrorAction | The value provided for the error reaction is invalid. |
| 12 | eOPCAuto_InvalidDACSigListLen | The length of the DAC signal list specified in the block is invalid. |
| 13 | eOPCAuto_InvalidServerName | The name of the OPC server is invalid. |
| 14 | eOPCAuto_NotImplemented | The function is not implemented. |
| 15 | eOPCAuto_RemoteConnectWithoutClassID | Transfer the ClassID to the OPCSrvConnect command to access a remote server without local registration. You only can reference OPC servers on remote computers with the ProgID if the ProgID or the server are registered locally. |
| 16 | eOPCAuto_ArrayAccesNotAllowed | The function cannot access arrays. |
| 17 | eOPCAuto_NoMoreHandles | No more OPC objects possible in the script area. |
| 18 | eOPCAuto_InvalidServerHandle | The server handle is invalid. |
| 19 | eOPCAuto_InvalidGroupHandle | The group handle is invalid. |
| 20 | eOPCAuto_InvalidItemHandle | The item handle is invalid. |
| 21 | eOPCAuto_ConnectTimeout | Timeout occurred while connecting to OPC server. The server cannot be accessed or one of the Proxy-DLLs such as opcproxy.dll and opccomn_ps.dll, is not registered. |
| 22 | eOPCAuto_CallTimeout | A timeout occurred while a function on an OPC server was being called. |
| 23 | eOPCAuto_NoIOPCServer | No IOPCServer interface at OPC server. |
| 24 | eOPCAuto_NoIOPCItemMgt | No IOPCItemMgt interface at OPC server. |
| 25 | eOPCAuto_NoIOPCSyncIO | No IOPCSyncIO interface at OPC server. |
| 26 | eOPCAuto_NoIOPCGroupStateMgt | No IOPCGroupStateMgt interface at OPC server. |
| 27 | eOPCAuto_InvalidItemNo | The number of items is invalid or an OPC group contains more items than acceptable. |

#### Related Topics

[Command: OPCAddGroup](../comonl/opcaddgroup.htm) | [Command: OPCAddItems](../comonl/opcadditems.htm) | [Command: OPCClear](../comonl/opcclear.htm) | [Command: OPCClearGroup](../comonl/opccleargroup.htm) | [Command: OPCClearItemDef](../comonl/opcclearitemdef.htm) | [Command: OPCConnect](../comonl/opcconnect.htm) | [Command: OPCDISConnect](../comonl/opcdisconnect.htm) | [Command: OPCGetDouble](../comonl/opcgetdouble.htm) | [Command: OPCGetInt](../comonl/opcgetint.htm) | [Command: OPCGetString](../comonl/opcgetstring.htm) | [Command: OPCReadSync](../comonl/opcreadsync.htm) | [Command: OPCRemoveGroup](../comonl/opcremovegroup.htm) | [Command: OPCRemoveItems](../comonl/opcremoveitems.htm) | [Command: OPCResetLogFile](../comonl/opcresetlogfile.htm) | [Command: OPCSetActiveStat](../comonl/opcsetactivestat.htm) | [Command: OPCSetCallTo](../comonl/opcsetcallto.htm) | [Command: OPCSetConnectTo](../comonl/opcsetconnectto.htm) | [Command: OPCSetDouble](../comonl/opcsetdouble.htm) | [Command: OPCSetInt](../comonl/opcsetint.htm) | [Command: OPCSetString](../comonl/opcsetstring.htm) | [Command: OPCValidateItems](../comonl/opcvalidateitems.htm) | [Command: OPCWriteSync](../comonl/opcwritesync.htm)

<!--NI_TOPIC bundle=diadem path=comonl/opcconnect.htm language=enus -->
## TOPIC 00031: Command: OPCConnect

- bundle_id: `diadem`
- source_path: `comonl/opcconnect.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/opcconnect.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: OPCConnect

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: OPCConnect

Connects an OPC server.

Call OPCConnect(OPCSrvName, OPCConnectTO)

#### Input Parameters

| OPCSrvName | Specifies the name of an OPC server. String variable Maximum 80 characters You can specify server names as follows: <ClassID> <ProgID> <Computername>\\<ClassID> <Computername>\\<ProgID> The ClassID identifies, globally unique, the COM object that is to be started, such as the OPC server. MS Windows always uses the ClassID when it starts OPC servers. The ProgID is the name of the OPC server, in text. MS Windows determines the associated ClassID from the registration of the OPC server with the operating system. The installation program writes the ClassID of the OPC server into the registration. However, if the OPC server is installed on a different computer, the registration of the local computer does not contain a ClassID for this OPC server. In this case you use the computer name and the ProgID. |
| --- | --- |
| String variable |  |
| Maximum 80 characters |  |
| OPCConnectTO | Specifies the time in milliseconds after which DIAdem disconnects a link to an OPC server. Longinteger variable 1 <= OPCConnectTo <= 600000 The default value is 15000 milliseconds. |
| Longinteger variable |  |
| 1 <= OPCConnectTo <= 600000 |  |

#### Return Parameters

| OPCErrorCode | Receives the status of the OPC command. Longinteger variable 0 <= OPCErrorCode <= 2147483647 The OPCErrorCode variable returns the number or the OPC code of the respective message: No. OPC code Description 0 eOPCAuto_Ok DIAdem executed the command without errors. 1 eOPCAuto_GeneralError A global error has occurred. 2 eOPCAuto_BlockMapEntryNotFound DIAdem cannot find entry for the signal and device specification in the driver blockmap. 3 eOPCAuto_UnidentifiedBlocktype The block type is not valid because no DAC input block or DAC output block open. 4 eOPCAuto_OPCBlockNotOpen No DAC block opened with the DACObjOpen command. 5 eOPCAuto_InvalidSignalIndex The signal index is not valid. Values from 1 to 255 are valid. 6 eOPCAuto_InvalidLogReset The value for the time of the logfile reset is not valid. 7 eOPCAuto_InvalidReportVerbosity The value for the type and extent of information to be recorded is not valid. 8 eOPCAuto_ProgIDNotInLocalRegistry DIAdem cannot find the transferred ProgID in the local registration. 9 eOPCAuto_ServerNotConnected The OPC server is not connected. 10 eOPCAuto_DataConversionFail Data could not be converted. 11 eOPCAuto_InvalidErrorAction The value provided for the error reaction is invalid. 12 eOPCAuto_InvalidDACSigListLen The length of the DAC signal list specified in the block is invalid. 13 eOPCAuto_InvalidServerName The name of the OPC server is invalid. 14 eOPCAuto_NotImplemented The function is not implemented. 15 eOPCAuto_RemoteConnectWithoutClassID Transfer the ClassID to the OPCSrvConnect command to access a remote server without local registration. You only can reference OPC servers on remote computers with the ProgID if the ProgID or the server are registered locally. 16 eOPCAuto_ArrayAccesNotAllowed The function cannot access arrays. 17 eOPCAuto_NoMoreHandles No more OPC objects possible in the script area. 18 eOPCAuto_InvalidServerHandle The server handle is invalid. 19 eOPCAuto_InvalidGroupHandle The group handle is invalid. 20 eOPCAuto_InvalidItemHandle The item handle is invalid. 21 eOPCAuto_ConnectTimeout Timeout occurred while connecting to OPC server. The server cannot be accessed or one of the Proxy-DLLs such as opcproxy.dll and opccomn_ps.dll, is not registered. 22 eOPCAuto_CallTimeout A timeout occurred while a function on an OPC server was being called. 23 eOPCAuto_NoIOPCServer No IOPCServer interface at OPC server. 24 eOPCAuto_NoIOPCItemMgt No IOPCItemMgt interface at OPC server. 25 eOPCAuto_NoIOPCSyncIO No IOPCSyncIO interface at OPC server. 26 eOPCAuto_NoIOPCGroupStateMgt No IOPCGroupStateMgt interface at OPC server. 27 eOPCAuto_InvalidItemNo The number of items is invalid or an OPC group contains more items than acceptable. |  |
| --- | --- | --- |
| Longinteger variable |  |  |
| 0 <= OPCErrorCode <= 2147483647 |  |  |
| No. | OPC code | Description |
| 0 | eOPCAuto_Ok | DIAdem executed the command without errors. |
| 1 | eOPCAuto_GeneralError | A global error has occurred. |
| 2 | eOPCAuto_BlockMapEntryNotFound | DIAdem cannot find entry for the signal and device specification in the driver blockmap. |
| 3 | eOPCAuto_UnidentifiedBlocktype | The block type is not valid because no DAC input block or DAC output block open. |
| 4 | eOPCAuto_OPCBlockNotOpen | No DAC block opened with the DACObjOpen command. |
| 5 | eOPCAuto_InvalidSignalIndex | The signal index is not valid. Values from 1 to 255 are valid. |
| 6 | eOPCAuto_InvalidLogReset | The value for the time of the logfile reset is not valid. |
| 7 | eOPCAuto_InvalidReportVerbosity | The value for the type and extent of information to be recorded is not valid. |
| 8 | eOPCAuto_ProgIDNotInLocalRegistry | DIAdem cannot find the transferred ProgID in the local registration. |
| 9 | eOPCAuto_ServerNotConnected | The OPC server is not connected. |
| 10 | eOPCAuto_DataConversionFail | Data could not be converted. |
| 11 | eOPCAuto_InvalidErrorAction | The value provided for the error reaction is invalid. |
| 12 | eOPCAuto_InvalidDACSigListLen | The length of the DAC signal list specified in the block is invalid. |
| 13 | eOPCAuto_InvalidServerName | The name of the OPC server is invalid. |
| 14 | eOPCAuto_NotImplemented | The function is not implemented. |
| 15 | eOPCAuto_RemoteConnectWithoutClassID | Transfer the ClassID to the OPCSrvConnect command to access a remote server without local registration. You only can reference OPC servers on remote computers with the ProgID if the ProgID or the server are registered locally. |
| 16 | eOPCAuto_ArrayAccesNotAllowed | The function cannot access arrays. |
| 17 | eOPCAuto_NoMoreHandles | No more OPC objects possible in the script area. |
| 18 | eOPCAuto_InvalidServerHandle | The server handle is invalid. |
| 19 | eOPCAuto_InvalidGroupHandle | The group handle is invalid. |
| 20 | eOPCAuto_InvalidItemHandle | The item handle is invalid. |
| 21 | eOPCAuto_ConnectTimeout | Timeout occurred while connecting to OPC server. The server cannot be accessed or one of the Proxy-DLLs such as opcproxy.dll and opccomn_ps.dll, is not registered. |
| 22 | eOPCAuto_CallTimeout | A timeout occurred while a function on an OPC server was being called. |
| 23 | eOPCAuto_NoIOPCServer | No IOPCServer interface at OPC server. |
| 24 | eOPCAuto_NoIOPCItemMgt | No IOPCItemMgt interface at OPC server. |
| 25 | eOPCAuto_NoIOPCSyncIO | No IOPCSyncIO interface at OPC server. |
| 26 | eOPCAuto_NoIOPCGroupStateMgt | No IOPCGroupStateMgt interface at OPC server. |
| 27 | eOPCAuto_InvalidItemNo | The number of items is invalid or an OPC group contains more items than acceptable. |
| OPCHResult | Receives the return value of the OPC command. Longinteger variable -2147483648 <= OPCHResult <= 2147483647 The OPCHResult variable can contain the following values: Value Meaning 0 The command was executed successfully. 1 The command was only partially executed successfully. The aOPCItemError variable contains information. Other Command could not execute. |  |
| Longinteger variable |  |  |
| -2147483648 <= OPCHResult <= 2147483647 |  |  |
| Value | Meaning |  |
| 0 | The command was executed successfully. |  |
| 1 | The command was only partially executed successfully. The aOPCItemError variable contains information. |  |
| Other | Command could not execute. |  |
| OPCSrvHandle | Receives the handle for the connection to the OPC server. Longinteger variable 0 <= OPCSrvHandle <= 2147483647 |  |
| Longinteger variable |  |  |
| 0 <= OPCSrvHandle <= 2147483647 |  |  |

#### Example

The following example connects the computer to the OPC server National Instruments.OPCDemo and interrupts the connection if no message is received after ten seconds.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call OPCConnect("National Instruments.OPCDemo.1",10000)
```

[Copy script](javascript:void(0);)

```text
OPCConnect("National Instruments.OPCDemo.1",10000) 
```

#### Related Topics

[Command: OPCAddGroup](../comonl/opcaddgroup.htm) | [Command: OPCAddItems](../comonl/opcadditems.htm) | [Command: OPCClear](../comonl/opcclear.htm) | [Command: OPCClearGroup](../comonl/opccleargroup.htm) | [Command: OPCClearItemDef](../comonl/opcclearitemdef.htm) | [Command: OPCClearServer](../comonl/opcclearserver.htm) | [Command: OPCDISConnect](../comonl/opcdisconnect.htm) | [Command: OPCGetDouble](../comonl/opcgetdouble.htm) | [Command: OPCGetInt](../comonl/opcgetint.htm) | [Command: OPCGetString](../comonl/opcgetstring.htm) | [Command: OPCReadSync](../comonl/opcreadsync.htm) | [Command: OPCRemoveGroup](../comonl/opcremovegroup.htm) | [Command: OPCRemoveItems](../comonl/opcremoveitems.htm) | [Command: OPCResetLogFile](../comonl/opcresetlogfile.htm) | [Command: OPCSetActiveStat](../comonl/opcsetactivestat.htm) | [Command: OPCSetCallTo](../comonl/opcsetcallto.htm) | [Command: OPCSetConnectTo](../comonl/opcsetconnectto.htm) | [Command: OPCSetDouble](../comonl/opcsetdouble.htm) | [Command: OPCSetInt](../comonl/opcsetint.htm) | [Command: OPCSetString](../comonl/opcsetstring.htm) | [Command: OPCValidateItems](../comonl/opcvalidateitems.htm) | [Command: OPCWriteSync](../comonl/opcwritesync.htm)

<!--NI_TOPIC bundle=diadem path=comonl/opcdisconnect.htm language=enus -->
## TOPIC 00032: Command: OPCDISConnect

- bundle_id: `diadem`
- source_path: `comonl/opcdisconnect.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/opcdisconnect.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: OPCDISConnect

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: OPCDISConnect

Disconnects an OPC server.

Call OPCDISConnect(OPCSrvHandle)

#### Input Parameters

| OPCSrvHandle | Specifies the handle for the connection to the OPC server. Longinteger variable 0 <= OPCSrvHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| 0 <= OPCSrvHandle <= 2147483647 |  |

#### Return Parameters

| OPCErrorCode | Receives the status of the OPC command. Longinteger variable 0 <= OPCErrorCode <= 2147483647 The OPCErrorCode variable returns the number or the OPC code of the respective message: No. OPC code Description 0 eOPCAuto_Ok DIAdem executed the command without errors. 1 eOPCAuto_GeneralError A global error has occurred. 2 eOPCAuto_BlockMapEntryNotFound DIAdem cannot find entry for the signal and device specification in the driver blockmap. 3 eOPCAuto_UnidentifiedBlocktype The block type is not valid because no DAC input block or DAC output block open. 4 eOPCAuto_OPCBlockNotOpen No DAC block opened with the DACObjOpen command. 5 eOPCAuto_InvalidSignalIndex The signal index is not valid. Values from 1 to 255 are valid. 6 eOPCAuto_InvalidLogReset The value for the time of the logfile reset is not valid. 7 eOPCAuto_InvalidReportVerbosity The value for the type and extent of information to be recorded is not valid. 8 eOPCAuto_ProgIDNotInLocalRegistry DIAdem cannot find the transferred ProgID in the local registration. 9 eOPCAuto_ServerNotConnected The OPC server is not connected. 10 eOPCAuto_DataConversionFail Data could not be converted. 11 eOPCAuto_InvalidErrorAction The value provided for the error reaction is invalid. 12 eOPCAuto_InvalidDACSigListLen The length of the DAC signal list specified in the block is invalid. 13 eOPCAuto_InvalidServerName The name of the OPC server is invalid. 14 eOPCAuto_NotImplemented The function is not implemented. 15 eOPCAuto_RemoteConnectWithoutClassID Transfer the ClassID to the OPCSrvConnect command to access a remote server without local registration. You only can reference OPC servers on remote computers with the ProgID if the ProgID or the server are registered locally. 16 eOPCAuto_ArrayAccesNotAllowed The function cannot access arrays. 17 eOPCAuto_NoMoreHandles No more OPC objects possible in the script area. 18 eOPCAuto_InvalidServerHandle The server handle is invalid. 19 eOPCAuto_InvalidGroupHandle The group handle is invalid. 20 eOPCAuto_InvalidItemHandle The item handle is invalid. 21 eOPCAuto_ConnectTimeout Timeout occurred while connecting to OPC server. The server cannot be accessed or one of the Proxy-DLLs such as opcproxy.dll and opccomn_ps.dll, is not registered. 22 eOPCAuto_CallTimeout A timeout occurred while a function on an OPC server was being called. 23 eOPCAuto_NoIOPCServer No IOPCServer interface at OPC server. 24 eOPCAuto_NoIOPCItemMgt No IOPCItemMgt interface at OPC server. 25 eOPCAuto_NoIOPCSyncIO No IOPCSyncIO interface at OPC server. 26 eOPCAuto_NoIOPCGroupStateMgt No IOPCGroupStateMgt interface at OPC server. 27 eOPCAuto_InvalidItemNo The number of items is invalid or an OPC group contains more items than acceptable. |  |
| --- | --- | --- |
| Longinteger variable |  |  |
| 0 <= OPCErrorCode <= 2147483647 |  |  |
| No. | OPC code | Description |
| 0 | eOPCAuto_Ok | DIAdem executed the command without errors. |
| 1 | eOPCAuto_GeneralError | A global error has occurred. |
| 2 | eOPCAuto_BlockMapEntryNotFound | DIAdem cannot find entry for the signal and device specification in the driver blockmap. |
| 3 | eOPCAuto_UnidentifiedBlocktype | The block type is not valid because no DAC input block or DAC output block open. |
| 4 | eOPCAuto_OPCBlockNotOpen | No DAC block opened with the DACObjOpen command. |
| 5 | eOPCAuto_InvalidSignalIndex | The signal index is not valid. Values from 1 to 255 are valid. |
| 6 | eOPCAuto_InvalidLogReset | The value for the time of the logfile reset is not valid. |
| 7 | eOPCAuto_InvalidReportVerbosity | The value for the type and extent of information to be recorded is not valid. |
| 8 | eOPCAuto_ProgIDNotInLocalRegistry | DIAdem cannot find the transferred ProgID in the local registration. |
| 9 | eOPCAuto_ServerNotConnected | The OPC server is not connected. |
| 10 | eOPCAuto_DataConversionFail | Data could not be converted. |
| 11 | eOPCAuto_InvalidErrorAction | The value provided for the error reaction is invalid. |
| 12 | eOPCAuto_InvalidDACSigListLen | The length of the DAC signal list specified in the block is invalid. |
| 13 | eOPCAuto_InvalidServerName | The name of the OPC server is invalid. |
| 14 | eOPCAuto_NotImplemented | The function is not implemented. |
| 15 | eOPCAuto_RemoteConnectWithoutClassID | Transfer the ClassID to the OPCSrvConnect command to access a remote server without local registration. You only can reference OPC servers on remote computers with the ProgID if the ProgID or the server are registered locally. |
| 16 | eOPCAuto_ArrayAccesNotAllowed | The function cannot access arrays. |
| 17 | eOPCAuto_NoMoreHandles | No more OPC objects possible in the script area. |
| 18 | eOPCAuto_InvalidServerHandle | The server handle is invalid. |
| 19 | eOPCAuto_InvalidGroupHandle | The group handle is invalid. |
| 20 | eOPCAuto_InvalidItemHandle | The item handle is invalid. |
| 21 | eOPCAuto_ConnectTimeout | Timeout occurred while connecting to OPC server. The server cannot be accessed or one of the Proxy-DLLs such as opcproxy.dll and opccomn_ps.dll, is not registered. |
| 22 | eOPCAuto_CallTimeout | A timeout occurred while a function on an OPC server was being called. |
| 23 | eOPCAuto_NoIOPCServer | No IOPCServer interface at OPC server. |
| 24 | eOPCAuto_NoIOPCItemMgt | No IOPCItemMgt interface at OPC server. |
| 25 | eOPCAuto_NoIOPCSyncIO | No IOPCSyncIO interface at OPC server. |
| 26 | eOPCAuto_NoIOPCGroupStateMgt | No IOPCGroupStateMgt interface at OPC server. |
| 27 | eOPCAuto_InvalidItemNo | The number of items is invalid or an OPC group contains more items than acceptable. |

#### Related Topics

[Command: OPCAddGroup](../comonl/opcaddgroup.htm) | [Command: OPCAddItems](../comonl/opcadditems.htm) | [Command: OPCClear](../comonl/opcclear.htm) | [Command: OPCClearGroup](../comonl/opccleargroup.htm) | [Command: OPCClearItemDef](../comonl/opcclearitemdef.htm) | [Command: OPCClearServer](../comonl/opcclearserver.htm) | [Command: OPCConnect](../comonl/opcconnect.htm) | [Command: OPCGetDouble](../comonl/opcgetdouble.htm) | [Command: OPCGetInt](../comonl/opcgetint.htm) | [Command: OPCGetString](../comonl/opcgetstring.htm) | [Command: OPCReadSync](../comonl/opcreadsync.htm) | [Command: OPCRemoveGroup](../comonl/opcremovegroup.htm) | [Command: OPCRemoveItems](../comonl/opcremoveitems.htm) | [Command: OPCResetLogFile](../comonl/opcresetlogfile.htm) | [Command: OPCSetActiveStat](../comonl/opcsetactivestat.htm) | [Command: OPCSetCallTo](../comonl/opcsetcallto.htm) | [Command: OPCSetConnectTo](../comonl/opcsetconnectto.htm) | [Command: OPCSetDouble](../comonl/opcsetdouble.htm) | [Command: OPCSetInt](../comonl/opcsetint.htm) | [Command: OPCSetString](../comonl/opcsetstring.htm) | [Command: OPCValidateItems](../comonl/opcvalidateitems.htm) | [Command: OPCWriteSync](../comonl/opcwritesync.htm)

<!--NI_TOPIC bundle=diadem path=comonl/opcgetautovalid.htm language=enus -->
## TOPIC 00033: Command: OPCGetAutoValid

- bundle_id: `diadem`
- source_path: `comonl/opcgetautovalid.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/opcgetautovalid.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: OPCGetAutoValid

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: OPCGetAutoValid

Determines how DIAdem validates OPC items.

Call OPCGetAutoValid()

#### Input Parameters

| None |
| --- |

#### Return Parameters

| OPCAutoValid | Specifies whether DIAdem runs a request before validating OPC items. Longinteger variable 0 <= OPCAutoValid <= 1 The OPCAutoValid variable can contain the following values: ValueMeaning 0A request occurs before validation.1The validation runs directly and without a confirmation prompt. |
| --- | --- |
| Longinteger variable |  |
| 0 <= OPCAutoValid <= 1 |  |
| Value | Meaning |
| 0 | A request occurs before validation. |
| 1 | The validation runs directly and without a confirmation prompt. |

#### Related Topics

[Command: OPCGetBlockParam](../comonl/opcgetblockparam.htm) | [Command: OPCGetConnMode](../comonl/opcgetconnmode.htm) | [Command: OPCGetLogFile](../comonl/opcgetlogfile.htm) | [Command: OPCGetSigParam](../comonl/opcgetsigparam.htm) | [Command: OPCLogGetVerb](../comonl/opcloggetverb.htm) | [Command: OPCLogSetVerb](../comonl/opclogsetverb.htm) | [Command: OPCSetActiveFlag](../comonl/opcsetactiveflag.htm) | [Command: OPCSetArrAccess](../comonl/opcsetarraccess.htm) | [Command: OPCSetAutoValid](../comonl/opcsetautovalid.htm) | [Command: OPCSetChkAS](../comonl/opcsetchkas.htm) | [Command: OPCSetConnMode](../comonl/opcsetconnmode.htm) | [Command: OPCSetDeadBand](../comonl/opcsetdeadband.htm) | [Command: OPCSetDeviceRead](../comonl/opcsetdeviceread.htm) | [Command: OPCSetErrAction](../comonl/opcseterraction.htm) | [Command: OPCSetItemID](../comonl/opcsetitemid.htm) | [Command: OPCSetLogFile](../comonl/opcsetlogfile.htm) | [Command: OPCSetMode](../comonl/opcsetmode.htm) | [Command: OPCSetServer](../comonl/opcsetserver.htm) | [Command: OPCSetSigName](../comonl/opcsetsigname.htm) | [Command: OPCSetToSync](../comonl/opcsettosync.htm) | [Command: OPCSetUpdRate](../comonl/opcsetupdrate.htm) | [Command: OPCSetWaitValid](../comonl/opcsetwaitvalid.htm) | [Command: OPCSyncListLen](../comonl/opcsynclistlen.htm)

<!--NI_TOPIC bundle=diadem path=comonl/opclogsetverb.htm language=enus -->
## TOPIC 00034: Command: OPCLogSetVerb

- bundle_id: `diadem`
- source_path: `comonl/opclogsetverb.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/opclogsetverb.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: OPCLogSetVerb

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: OPCLogSetVerb

Specifies the settings of the logfile for OPC communication.

Call OPCLogSetVerb(OPCLogCategory, OPCLogEnableCat)

#### Input Parameters

| OPCLogCategory | Specifies which categories DIAdem records in an OPC logfile. Longinteger variable 0 <= OPCLogCategory <= 3 The OPCLogCategory variable can contain the following values: Value Meaning 0DIAdem records error messages.1DIAdem records warning messages.2DIAdem records general information.3DIAdem records information about the measurement preparation. |
| --- | --- |
| Longinteger variable |  |
| 0 <= OPCLogCategory <= 3 |  |
| Value | Meaning |
| 0 | DIAdem records error messages. |
| 1 | DIAdem records warning messages. |
| 2 | DIAdem records general information. |
| 3 | DIAdem records information about the measurement preparation. |
| OPCLogEnableCat | Specifies whether DIAdem records the categories listed in the OPCLogCategory variables. Longinteger variable 0 <= OPCLogEnableCat <= 1 The OPCLogEnableCat variable can contain the following values: Value Meaning 0DIAdem does not record the category in the OPC logfile.1DIAdem records the category in the OPC logfile. |
| Longinteger variable |  |
| 0 <= OPCLogEnableCat <= 1 |  |
| Value | Meaning |
| 0 | DIAdem does not record the category in the OPC logfile. |
| 1 | DIAdem records the category in the OPC logfile. |

#### Example

The following example records all the messages for the measurement preparations, until the measurement starts.

```text
Call OPCLogSetVerb(3,1)
Call SchemeLoad("OPCExample")
Call SchemeMeasStart()
Call OPCLogSetVerb(3,1)
```

#### Related Topics

[Command: OPCGetAutoValid](../comonl/opcgetautovalid.htm) | [Command: OPCGetBlockParam](../comonl/opcgetblockparam.htm) | [Command: OPCGetConnMode](../comonl/opcgetconnmode.htm) | [Command: OPCGetLogFile](../comonl/opcgetlogfile.htm) | [Command: OPCGetSigParam](../comonl/opcgetsigparam.htm) | [Command: OPCLogGetVerb](../comonl/opcloggetverb.htm) | [Command: OPCSetActiveFlag](../comonl/opcsetactiveflag.htm) | [Command: OPCSetArrAccess](../comonl/opcsetarraccess.htm) | [Command: OPCSetAutoValid](../comonl/opcsetautovalid.htm) | [Command: OPCSetChkAS](../comonl/opcsetchkas.htm) | [Command: OPCSetConnMode](../comonl/opcsetconnmode.htm) | [Command: OPCSetDeadBand](../comonl/opcsetdeadband.htm) | [Command: OPCSetDeviceRead](../comonl/opcsetdeviceread.htm) | [Command: OPCSetErrAction](../comonl/opcseterraction.htm) | [Command: OPCSetItemID](../comonl/opcsetitemid.htm) | [Command: OPCSetLogFile](../comonl/opcsetlogfile.htm) | [Command: OPCSetMode](../comonl/opcsetmode.htm) | [Command: OPCSetServer](../comonl/opcsetserver.htm) | [Command: OPCSetSigName](../comonl/opcsetsigname.htm) | [Command: OPCSetToSync](../comonl/opcsettosync.htm) | [Command: OPCSetUpdRate](../comonl/opcsetupdrate.htm) | [Command: OPCSetWaitValid](../comonl/opcsetwaitvalid.htm) | [Command: OPCSyncListLen](../comonl/opcsynclistlen.htm)

<!--NI_TOPIC bundle=diadem path=comonl/opcsetactivestat.htm language=enus -->
## TOPIC 00035: Command: OPCSetActiveStat

- bundle_id: `diadem`
- source_path: `comonl/opcsetactivestat.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/opcsetactivestat.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: OPCSetActiveStat

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: OPCSetActiveStat

Enables or disables OPC items of an OPC group.

Call OPCSetActiveStat(OPCGrpHandle, OPCItemNo, OPCItemActive)

#### Input Parameters

| OPCGrpHandle | Specifies the handle of an OPC group. Longinteger variable 0 <= OPCGrpHandle <= 2147483647 |
| --- | --- |
| Longinteger variable |  |
| 0 <= OPCGrpHandle <= 2147483647 |  |
| OPCItemNo | Specifies the number of items of an OPC group that are to be processed. Longinteger variable 0 <= OPCItemNo <= 2147483647 |
| Longinteger variable |  |
| 0 <= OPCItemNo <= 2147483647 |  |
| OPCItemActive | Specifies the status of an OPC item. Longinteger variable 0 <= OPCItemActive <= 1 The OPCItemActive variable can contain the following values: Value Meaning 0The OPC item is not active.1The OPC item is active. |
| Longinteger variable |  |
| 0 <= OPCItemActive <= 1 |  |
| Value | Meaning |
| 0 | The OPC item is not active. |
| 1 | The OPC item is active. |

#### Global Parameters

| aOPCItemHandle | Specifies the handles of various OPC items. Longinteger variablei = 1 ... 1024 The OPCItemNo variable limits the field length. |
| --- | --- |
| Longinteger variablei = 1 ... 1024 |  |

#### Return Parameters

| OPCErrorCode | Receives the status of the OPC command. Longinteger variable 0 <= OPCErrorCode <= 2147483647 The OPCErrorCode variable returns the number or the OPC code of the respective message: No. OPC code Description 0 eOPCAuto_Ok DIAdem executed the command without errors. 1 eOPCAuto_GeneralError A global error has occurred. 2 eOPCAuto_BlockMapEntryNotFound DIAdem cannot find entry for the signal and device specification in the driver blockmap. 3 eOPCAuto_UnidentifiedBlocktype The block type is not valid because no DAC input block or DAC output block open. 4 eOPCAuto_OPCBlockNotOpen No DAC block opened with the DACObjOpen command. 5 eOPCAuto_InvalidSignalIndex The signal index is not valid. Values from 1 to 255 are valid. 6 eOPCAuto_InvalidLogReset The value for the time of the logfile reset is not valid. 7 eOPCAuto_InvalidReportVerbosity The value for the type and extent of information to be recorded is not valid. 8 eOPCAuto_ProgIDNotInLocalRegistry DIAdem cannot find the transferred ProgID in the local registration. 9 eOPCAuto_ServerNotConnected The OPC server is not connected. 10 eOPCAuto_DataConversionFail Data could not be converted. 11 eOPCAuto_InvalidErrorAction The value provided for the error reaction is invalid. 12 eOPCAuto_InvalidDACSigListLen The length of the DAC signal list specified in the block is invalid. 13 eOPCAuto_InvalidServerName The name of the OPC server is invalid. 14 eOPCAuto_NotImplemented The function is not implemented. 15 eOPCAuto_RemoteConnectWithoutClassID Transfer the ClassID to the OPCSrvConnect command to access a remote server without local registration. You only can reference OPC servers on remote computers with the ProgID if the ProgID or the server are registered locally. 16 eOPCAuto_ArrayAccesNotAllowed The function cannot access arrays. 17 eOPCAuto_NoMoreHandles No more OPC objects possible in the script area. 18 eOPCAuto_InvalidServerHandle The server handle is invalid. 19 eOPCAuto_InvalidGroupHandle The group handle is invalid. 20 eOPCAuto_InvalidItemHandle The item handle is invalid. 21 eOPCAuto_ConnectTimeout Timeout occurred while connecting to OPC server. The server cannot be accessed or one of the Proxy-DLLs such as opcproxy.dll and opccomn_ps.dll, is not registered. 22 eOPCAuto_CallTimeout A timeout occurred while a function on an OPC server was being called. 23 eOPCAuto_NoIOPCServer No IOPCServer interface at OPC server. 24 eOPCAuto_NoIOPCItemMgt No IOPCItemMgt interface at OPC server. 25 eOPCAuto_NoIOPCSyncIO No IOPCSyncIO interface at OPC server. 26 eOPCAuto_NoIOPCGroupStateMgt No IOPCGroupStateMgt interface at OPC server. 27 eOPCAuto_InvalidItemNo The number of items is invalid or an OPC group contains more items than acceptable. |  |
| --- | --- | --- |
| Longinteger variable |  |  |
| 0 <= OPCErrorCode <= 2147483647 |  |  |
| No. | OPC code | Description |
| 0 | eOPCAuto_Ok | DIAdem executed the command without errors. |
| 1 | eOPCAuto_GeneralError | A global error has occurred. |
| 2 | eOPCAuto_BlockMapEntryNotFound | DIAdem cannot find entry for the signal and device specification in the driver blockmap. |
| 3 | eOPCAuto_UnidentifiedBlocktype | The block type is not valid because no DAC input block or DAC output block open. |
| 4 | eOPCAuto_OPCBlockNotOpen | No DAC block opened with the DACObjOpen command. |
| 5 | eOPCAuto_InvalidSignalIndex | The signal index is not valid. Values from 1 to 255 are valid. |
| 6 | eOPCAuto_InvalidLogReset | The value for the time of the logfile reset is not valid. |
| 7 | eOPCAuto_InvalidReportVerbosity | The value for the type and extent of information to be recorded is not valid. |
| 8 | eOPCAuto_ProgIDNotInLocalRegistry | DIAdem cannot find the transferred ProgID in the local registration. |
| 9 | eOPCAuto_ServerNotConnected | The OPC server is not connected. |
| 10 | eOPCAuto_DataConversionFail | Data could not be converted. |
| 11 | eOPCAuto_InvalidErrorAction | The value provided for the error reaction is invalid. |
| 12 | eOPCAuto_InvalidDACSigListLen | The length of the DAC signal list specified in the block is invalid. |
| 13 | eOPCAuto_InvalidServerName | The name of the OPC server is invalid. |
| 14 | eOPCAuto_NotImplemented | The function is not implemented. |
| 15 | eOPCAuto_RemoteConnectWithoutClassID | Transfer the ClassID to the OPCSrvConnect command to access a remote server without local registration. You only can reference OPC servers on remote computers with the ProgID if the ProgID or the server are registered locally. |
| 16 | eOPCAuto_ArrayAccesNotAllowed | The function cannot access arrays. |
| 17 | eOPCAuto_NoMoreHandles | No more OPC objects possible in the script area. |
| 18 | eOPCAuto_InvalidServerHandle | The server handle is invalid. |
| 19 | eOPCAuto_InvalidGroupHandle | The group handle is invalid. |
| 20 | eOPCAuto_InvalidItemHandle | The item handle is invalid. |
| 21 | eOPCAuto_ConnectTimeout | Timeout occurred while connecting to OPC server. The server cannot be accessed or one of the Proxy-DLLs such as opcproxy.dll and opccomn_ps.dll, is not registered. |
| 22 | eOPCAuto_CallTimeout | A timeout occurred while a function on an OPC server was being called. |
| 23 | eOPCAuto_NoIOPCServer | No IOPCServer interface at OPC server. |
| 24 | eOPCAuto_NoIOPCItemMgt | No IOPCItemMgt interface at OPC server. |
| 25 | eOPCAuto_NoIOPCSyncIO | No IOPCSyncIO interface at OPC server. |
| 26 | eOPCAuto_NoIOPCGroupStateMgt | No IOPCGroupStateMgt interface at OPC server. |
| 27 | eOPCAuto_InvalidItemNo | The number of items is invalid or an OPC group contains more items than acceptable. |
| OPCHResult | Receives the return value of the OPC command. Longinteger variable The OPCHResult variable can contain the following values: Value Meaning 0 The command was executed successfully. 1 The command was only partially executed successfully. The aOPCItemError variable contains information. |  |
| Longinteger variable |  |  |
| Value | Meaning |  |
| 0 | The command was executed successfully. |  |
| 1 | The command was only partially executed successfully. The aOPCItemError variable contains information. |  |
| aOPCItemError | Receives the status of operations with various OPC items. Longinteger variablei = 1 ... 1024 Specify the field length with the OPCItemNo variable.The aOPCItemError variable can contain the following values: Value Meaning 0Command executed successfully.OtherCommand could not execute. The OPCErrorCode variable contains a list of error codes. |  |
| Longinteger variablei = 1 ... 1024 |  |  |
| Value | Meaning |  |
| 0 | Command executed successfully. |  |
| Other | Command could not execute. The OPCErrorCode variable contains a list of error codes. |  |

#### Related Topics

[Command: OPCAddGroup](../comonl/opcaddgroup.htm) | [Command: OPCAddItems](../comonl/opcadditems.htm) | [Command: OPCClear](../comonl/opcclear.htm) | [Command: OPCClearGroup](../comonl/opccleargroup.htm) | [Command: OPCClearItemDef](../comonl/opcclearitemdef.htm) | [Command: OPCClearServer](../comonl/opcclearserver.htm) | [Command: OPCConnect](../comonl/opcconnect.htm) | [Command: OPCDISConnect](../comonl/opcdisconnect.htm) | [Command: OPCGetDouble](../comonl/opcgetdouble.htm) | [Command: OPCGetInt](../comonl/opcgetint.htm) | [Command: OPCGetString](../comonl/opcgetstring.htm) | [Command: OPCReadSync](../comonl/opcreadsync.htm) | [Command: OPCRemoveGroup](../comonl/opcremovegroup.htm) | [Command: OPCRemoveItems](../comonl/opcremoveitems.htm) | [Command: OPCResetLogFile](../comonl/opcresetlogfile.htm) | [Command: OPCSetCallTo](../comonl/opcsetcallto.htm) | [Command: OPCSetConnectTo](../comonl/opcsetconnectto.htm) | [Command: OPCSetDouble](../comonl/opcsetdouble.htm) | [Command: OPCSetInt](../comonl/opcsetint.htm) | [Command: OPCSetString](../comonl/opcsetstring.htm) | [Command: OPCValidateItems](../comonl/opcvalidateitems.htm) | [Command: OPCWriteSync](../comonl/opcwritesync.htm)

<!--NI_TOPIC bundle=diadem path=comonl/opcsetarraccess.htm language=enus -->
## TOPIC 00036: Command: OPCSetArrAccess

- bundle_id: `diadem`
- source_path: `comonl/opcsetarraccess.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/opcsetarraccess.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: OPCSetArrAccess

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: OPCSetArrAccess

Enables array indexing for the signals of an OPC block.

Call OPCSetArrAccess(OPCSigIndex, OPCArrayEnable, OPCArrayIndex)

#### Input Parameters

| OPCSigIndex | Specifies the index of a signal in an OPC block. Longinteger variable 0 <= OPCSigIndex <= 2147483647 The index starts with 1. |
| --- | --- |
| Longinteger variable |  |
| 0 <= OPCSigIndex <= 2147483647 |  |
| OPCArrayEnable | Specifies whether array indexing is executed for a signal in an OPC block. Longinteger variable 0 <= OPCArrayEnable <= 1 The OPCArrayEnable variable can contain the following values: Value Meaning 0No array indexing for signal.1Array indexing for signal. |
| Longinteger variable |  |
| 0 <= OPCArrayEnable <= 1 |  |
| Value | Meaning |
| 0 | No array indexing for signal. |
| 1 | Array indexing for signal. |
| OPCArrayIndex | Specifies the index of the read value when the OPC server returns an array for the OPC item. Longinteger variable 0 <= OPCArrayIndex <= 2147483647 The array length limits the value range. |
| Longinteger variable |  |
| 0 <= OPCArrayIndex <= 2147483647 |  |

|  | Note You must use the following object hierarchy to execute this command: Call DACObjOpen(BlockName) Call OPCSetArrAccess(SignalIndex,1,ArrayIndex)Call DACObjClose(BlockName) You need the DAC block name to open the DAC block, to execute the command, and to close the DAC block. Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Related Topics

[Command: OPCGetAutoValid](../comonl/opcgetautovalid.htm) | [Command: OPCGetBlockParam](../comonl/opcgetblockparam.htm) | [Command: OPCGetConnMode](../comonl/opcgetconnmode.htm) | [Command: OPCGetLogFile](../comonl/opcgetlogfile.htm) | [Command: OPCGetSigParam](../comonl/opcgetsigparam.htm) | [Command: OPCLogGetVerb](../comonl/opcloggetverb.htm) | [Command: OPCLogSetVerb](../comonl/opclogsetverb.htm) | [Command: OPCSetActiveFlag](../comonl/opcsetactiveflag.htm) | [Command: OPCSetAutoValid](../comonl/opcsetautovalid.htm) | [Command: OPCSetChkAS](../comonl/opcsetchkas.htm) | [Command: OPCSetConnMode](../comonl/opcsetconnmode.htm) | [Command: OPCSetDeadBand](../comonl/opcsetdeadband.htm) | [Command: OPCSetDeviceRead](../comonl/opcsetdeviceread.htm) | [Command: OPCSetErrAction](../comonl/opcseterraction.htm) | [Command: OPCSetItemID](../comonl/opcsetitemid.htm) | [Command: OPCSetLogFile](../comonl/opcsetlogfile.htm) | [Command: OPCSetMode](../comonl/opcsetmode.htm) | [Command: OPCSetServer](../comonl/opcsetserver.htm) | [Command: OPCSetSigName](../comonl/opcsetsigname.htm) | [Command: OPCSetToSync](../comonl/opcsettosync.htm) | [Command: OPCSetUpdRate](../comonl/opcsetupdrate.htm) | [Command: OPCSetWaitValid](../comonl/opcsetwaitvalid.htm) | [Command: OPCSyncListLen](../comonl/opcsynclistlen.htm)

<!--NI_TOPIC bundle=diadem path=comonl/opcsetchkas.htm language=enus -->
## TOPIC 00037: Command: OPCSetChkAS

- bundle_id: `diadem`
- source_path: `comonl/opcsetchkas.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/comonl/opcsetchkas.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Command: OPCSetChkAS

[[IMAGE alt='image' src='image/arrowdown.gif']](#nowhere)[Display all](javascript:expandall();) [[IMAGE alt='image' src='image/arrowright.gif']](#nowhere)[Hide all](javascript:closeall();)

Command: OPCSetChkAS

Checks asynchronous connections of an OPC block to the OPC server.

Call OPCSetChkAS(OPCChkAs, OPCChkAsIntrv)

#### Input Parameters

| OPCChkAs | Specifies whether DIAdem checks asynchronous connections to OPC servers during the measurement. Longinteger variable 0 <= OPCChkAs <= 1 The OPCChkAs variable can contain the following values: Value Meaning 0DIAdem does not check asynchronous connections.1DIAdem checks asynchronous connections. |
| --- | --- |
| Longinteger variable |  |
| 0 <= OPCChkAs <= 1 |  |
| Value | Meaning |
| 0 | DIAdem does not check asynchronous connections. |
| 1 | DIAdem checks asynchronous connections. |
| OPCChkAsIntrv | Specifies the number of clock cycles after which DIAdem checks asynchronous connections to OPC servers again. Longinteger variable 1 <= OPCChkAsIntrV <= 2147483647 |
| Longinteger variable |  |
| 1 <= OPCChkAsIntrV <= 2147483647 |  |

|  | Note The OPCSetChkAs command can only check the connection to the OPC server if you have set asynchronous mode for the OPC block. |
| --- | --- |

|  | Note You must use the following object hierarchy to execute this command: Call DACObjOpen(BlockName) Call OPCSetChkAs(1,Interval)Call DACObjClose(BlockName) You need the DAC block name to open the DAC block, to execute the command, and to close the DAC block. Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Related Topics

[Command: OPCGetAutoValid](../comonl/opcgetautovalid.htm) | [Command: OPCGetBlockParam](../comonl/opcgetblockparam.htm) | [Command: OPCGetConnMode](../comonl/opcgetconnmode.htm) | [Command: OPCGetLogFile](../comonl/opcgetlogfile.htm) | [Command: OPCGetSigParam](../comonl/opcgetsigparam.htm) | [Command: OPCLogGetVerb](../comonl/opcloggetverb.htm) | [Command: OPCLogSetVerb](../comonl/opclogsetverb.htm) | [Command: OPCSetActiveFlag](../comonl/opcsetactiveflag.htm) | [Command: OPCSetArrAccess](../comonl/opcsetarraccess.htm) | [Command: OPCSetAutoValid](../comonl/opcsetautovalid.htm) | [Command: OPCSetConnMode](../comonl/opcsetconnmode.htm) | [Command: OPCSetDeadBand](../comonl/opcsetdeadband.htm) | [Command: OPCSetDeviceRead](../comonl/opcsetdeviceread.htm) | [Command: OPCSetErrAction](../comonl/opcseterraction.htm) | [Command: OPCSetItemID](../comonl/opcsetitemid.htm) | [Command: OPCSetLogFile](../comonl/opcsetlogfile.htm) | [Command: OPCSetMode](../comonl/opcsetmode.htm) | [Command: OPCSetServer](../comonl/opcsetserver.htm) | [Command: OPCSetSigName](../comonl/opcsetsigname.htm) | [Command: OPCSetToSync](../comonl/opcsettosync.htm) | [Command: OPCSetUpdRate](../comonl/opcsetupdrate.htm) | [Command: OPCSetWaitValid](../comonl/opcsetwaitvalid.htm) | [Command: OPCSyncListLen](../comonl/opcsynclistlen.htm)

<!--NI_TOPIC bundle=diadem path=concepts/diadem_5_03.html language=dede -->
## TOPIC 00038: Bearbeiten von Layouts

- bundle_id: `diadem`
- source_path: `concepts/diadem_5_03.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/dede/concepts/diadem_5_03.html
- source_language: `dede`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Reports erstellen](../concepts/diadem_5_01.html) > Bearbeiten von Layouts

### Bearbeiten von Layouts

In der Layoutdatei mit der Dateinamenserweiterung .tdr speichern Sie die Beschreibung aller Arbeitsblätter eines Reports. Die Layoutdatei enthält die Beschreibung aller Objekte, wie Achsensysteme, Tabellen oder Texte, und die Verknüpfungen zu den Daten. Sie können Datenzuordnungen in den Dialogen der Achsensysteme und Tabellen ändern oder löschen.

DIAdem weist im Report die Datenkanäle standardmäßig über den Kanalnamen und den Gruppenindex zu. Diese eindeutige Zuordnung ist sinnvoll, wenn die Kanäle in den auszuwertenden Datendateien immer denselben Kanalnamen besitzen und in derselben Kanalgruppe stehen. Wenn die Kanalgruppe nicht immer an derselben Position in den Datendateien steht, aber die Gruppe immer denselben Namen hat, kann die Kanalzuordnung auch aus dem Gruppennamen und dem Kanalnamen bestehen. Ein Report kann auch Kanalbezüge enthalten, die sich aus dem Gruppennamen oder Gruppenindex und dem Kanalindex zusammensetzen. Den namensorientierten Kanalbezug legen Sie unter **Einstellungen»DIAdem-Einstellungen»Allgemeines** fest.

Wenn Sie die Kurvenexpansion in den Layout-Parametern aktivieren, stellt DIAdem mit einem Eintrag in der Kurvendefinition nicht nur die Kurve des ersten passenden Kanalpaars in einer Kanalgruppe, sondern die Kurven aller Kanalpaare mit gleichen Kanalnamen in allen Kanalgruppen dar. Nachdem Sie die Kanalzuordnung für ein Achsensystem definiert haben, sucht DIAdem im Datenportal den ersten Kanal mit dem vorgegebenen x-Kanalnamen, beispielsweise Time. Wenn DIAdem den x-Kanal gefunden hat, sucht DIAdem nach dem zugehörigen y-Kanal Speed in derselben Kanalgruppe. Im Expansionsmodus sucht DIAdem nach weiteren Kanalpaaren Time und Speed in den anderen Kanalgruppen, bis das Ende des Datenportals erreicht ist. Über **Einstellungen»Layout einrichten»Layout-Parameter»Darstellung»Kurvenexpansion** können Sie die Attribute zur Darstellung jeder Kurve festlegen.

#### Verwandte Themen

[Einfügen von Report-Objekten](../concepts/diadem_5_04.html) | [Gestalten von Arbeitsblättern](../concepts/diadem_5_02.html) | [Reports erstellen](../concepts/diadem_5_01.html)

<!--NI_TOPIC bundle=diadem path=concepts/diadem_5_043.html language=dede -->
## TOPIC 00039: 3D-Achsensysteme

- bundle_id: `diadem`
- source_path: `concepts/diadem_5_043.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/dede/concepts/diadem_5_043.html
- source_language: `dede`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Reports erstellen](../concepts/diadem_5_01.html) > [Einfügen von Report-Objekten](../concepts/diadem_5_04.html) > 3D-Achsensysteme

### 3D-Achsensysteme

Verwenden Sie 3D-Achsensysteme, um beispielsweise Kennfelder von Motorleistungen oder Wasserfalldarstellungen von Ordnungsanalysen darzustellen.

Um die Darstellung zu ändern, doppelklicken Sie auf das Achsensystem. Klicken Sie in die Spalte **Art**, um eine Darstellungsart, wie Fläche, Isolinien, Balken, Spikes, Schwärzungsmatrix, Vektor- oder Symboldarstellung, auszuwählen. Um die Darstellung zu bearbeiten, klicken Sie auf die Schaltfläche mit den drei Punkten und bestimmen die Kurvenparameter. Verwenden Sie die Darstellungsart **Koordinate**, um auffällige Punkte wie Plateaus oder Spitzen zu markieren und mit einem Kommentar zu versehen. Bei der Projektion auf eine Ebene können Sie Koordinaten wie im 2D-Achsensystem interaktiv über das Kontextmenü setzen.

Die folgende Abbildung zeigt eine Kombination mehrerer Darstellungsarten für eine Spirale in einem 3D-Achsensystem. Für die Darstellung der Spirale als Raumkurve wählen Sie drei Kanäle im Dialog des 3D-Achsensystems aus. Die Pfeile an der Spirale sind Vektoren, die für jeden Punkt der Spirale die Kraft anzeigen. In der xy- und der xz-Ebene sehen Sie Projektionen der Spirale. Sie können für jede Darstellungsebene die Skalierung, Beschriftung und Gitterdarstellung festlegen. Wie beim 2D-Achsensystem können Sie die Achsen abhängig von der Position, an der Sie den Mauszeiger auf der Achsenbeschriftung bewegen, interaktiv mit dem Mausrad skalieren.

[IMAGE alt='image' src='image/report_spiral.png']

*Vektordarstellung einer Spirale mit Projektionen auf die Ebenen*

Sie können 3D-Achsensysteme im Arbeitsblatt drehen und verschieben und auch die einzelnen Koordinatenebenen verschieben. Um die Ansicht auf ein 3D-Achsensystem zu ändern, klicken Sie auf das 3D-Achsensystem und drehen das Achsensystem. Um ein 3D-Achsensystem zu verschieben, klicken Sie außerhalb des Achsensystems, aber innerhalb des Markierungsrahmens. Wenn der Mauszeiger keine ineinandergreifenden Kreispfeile zeigt, können Sie das Achsensystem verschieben. Um eine Ebene nach außen zu verschieben, klicken Sie auf den Rand der Ebene. Sobald die Ebene einen blauen Markierungsrahmen zeigt, verschieben Sie die Ebene nach außen.

Für Wasserfall-, Balken- und 2D-Matrixdarstellungen benötigt DIAdem die Daten in Matrixstruktur. Im Dialog des 3D-Achsensystems wählen Sie für diese Darstellungen einen x-Kanal, einen y-Kanal und so viele z-Kanäle, wie der y-Kanal Werte enthält. Für Raumkurven benötigt DIAdem die Daten in Tripelstruktur, für die Sie drei Kanäle auswählen. Flächen-, Spike-, Symbol- und Kennfelddarstellungen können Daten sowohl in Tripelstruktur als auch in Matrixstruktur darstellen. Mit den Funktionen zur 3D-Analyse von DIAdem-ANALYSIS können Sie Kanäle zu einer zusammenhängenden Matrix aufbereiten oder in Wertetripel konvertieren.

#### Verwandte Themen

[2D-Achsensysteme](../concepts/diadem_5_041.html) | [2D-Tabellen](../concepts/diadem_5_044.html) | [3D-Tabellen](../concepts/diadem_5_045.html) | [Einfügen von Report-Objekten](../concepts/diadem_5_04.html) | [Grafiken, Linien und vordefinierte Objekte](../concepts/diadem_5_047.html) | [Polarachsensysteme](../concepts/diadem_5_042.html) | [Texte, Kommentare und Formeln](../concepts/diadem_5_046.html)

<!--NI_TOPIC bundle=diadem path=concepts/diadem_5_044.html language=dede -->
## TOPIC 00040: 2D-Tabellen

- bundle_id: `diadem`
- source_path: `concepts/diadem_5_044.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/dede/concepts/diadem_5_044.html
- source_language: `dede`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Reports erstellen](../concepts/diadem_5_01.html) > [Einfügen von Report-Objekten](../concepts/diadem_5_04.html) > 2D-Tabellen

### 2D-Tabellen

Verwenden Sie 2D-Tabellen, um numerische Kanäle, Waveform-Kanäle, Zeit- und Textkanäle aufzulisten. Mit Drag&Drop ziehen Sie Kanäle aus dem Datenportal in die Tabelle. Mit einem Doppelklick auf die Tabelle öffnen Sie die Tabellendefinition, in der Sie die Reihenfolge der Spalten ändern, die Darstellungsparameter bestimmen und die Überschriften eingeben. Für lange Kanäle können Sie den ersten Datenwert, den letzten Datenwert und die Schrittweite der darzustellenden Werte vorgeben. Um die Spaltenbreiten oder die Höhe der Überschriften zu ändern, verschieben Sie die entsprechenden Trennlinien. Um die Schriftattribute zu ändern, markieren Sie die Spalteneinträge oder Überschriften und wählen beispielsweise die Schriftart in der Formatleiste aus. Für die Darstellung können Sie die Daten spaltenweise auf- oder absteigend sortieren und wie im 2D-Achsensystem mit dem Einheitenkatalog eine andere Einheit berechnen, beispielsweise Temperaturkanäle von Grad Celsius in Grad Fahrenheit.

[IMAGE alt='image' src='image/report_tablepage.png'] Lange Kanäle können Sie vollständig lesbar darstellen, wenn Sie für die Tabellenlänge die Einstellung **Automatisch wachsend** auf der Registerkarte **Skalierung** des Tabellendialogs wählen. Damit definieren Sie eine mehrseitige Tabelle, die die Inhalte der Kanäle fortlaufend auf mehreren Seiten auflistet. Mit den Funktionen der **Tabellennavigation** in der Befehlsleiste von DIAdem-REPORT blättern Sie durch die Seiten der Tabelle.

In 2D-Tabellen können Sie auch Einzel- und Vektorvariablen darstellen. Wählen Sie auf der Registerkarte **Tabellenspalten** als Datenart **Variable** und geben Sie den Namen der Variablen ein. Wenn Sie die Einzelvariable CurrDate eingeben, erscheint das aktuelle Datum in der obersten Tabellenzeile. Wenn Sie die Vektorvariable CD eingeben, zeigt DIAdem in der Tabellenspalte die Einheiten aller im Datenportal vorhandenen Kanäle.

Verwenden Sie Textlisten in 2D-Tabellen, um beliebige Texte und Ausdrücke unabhängig von Kanälen in Tabellen darzustellen. Wählen Sie auf der Registerkarte **Tabellenspalten** die Datenart **Textliste**. Erstellen Sie auf der Registerkarte **Spalteneigenschaften»Textliste** so viele Zeilen, wie Sie zur Eingabe Ihres Textes benötigen. Klicken Sie auf die Schaltfläche mit den drei Punkten, um Variablen und Ausdrücke einzufügen. Vor und hinter jeder Variablen müssen doppelte @-Zeichen stehen. DIAdem speichert die Textlisten mit dem Reportlayout ab.

#### Verwandte Themen

[2D-Achsensysteme](../concepts/diadem_5_041.html) | [3D-Achsensysteme](../concepts/diadem_5_043.html) | [3D-Tabellen](../concepts/diadem_5_045.html) | [Einfügen von Report-Objekten](../concepts/diadem_5_04.html) | [Grafiken, Linien und vordefinierte Objekte](../concepts/diadem_5_047.html) | [Polarachsensysteme](../concepts/diadem_5_042.html) | [Texte, Kommentare und Formeln](../concepts/diadem_5_046.html)

<!--NI_TOPIC bundle=diadem path=concepts/diadem_5_045.html language=dede -->
## TOPIC 00041: 3D-Tabellen

- bundle_id: `diadem`
- source_path: `concepts/diadem_5_045.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/dede/concepts/diadem_5_045.html
- source_language: `dede`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Reports erstellen](../concepts/diadem_5_01.html) > [Einfügen von Report-Objekten](../concepts/diadem_5_04.html) > 3D-Tabellen

### 3D-Tabellen

Verwenden Sie 3D-Tabellen, um die Matrixstruktur von 3D-Daten numerisch darzustellen. Im Dialog der 3D-Tabelle geben Sie den x-, den y- und den ersten z-Kanal der Matrixstruktur ein. Die folgende Abbildung zeigt, wie eine 3D-Tabelle jedem xy-Wertepaar den zugehörigen z-Wert zuordnet.

[IMAGE alt='image' src='image/report_3dtable.png']

*3D-Tabellen ordnen jedem xy-Wertepaar den zugehörigen z-Wert zu*

Die 3D-Tabelle kann die gesamte Matrixstruktur oder einen Ausschnitt abbilden. Für x-, y- und z-Werte bestimmen Sie die Darstellungsparameter, wie Zeichensatz und Darstellungsformat. Um 3D-Daten in Tripelstruktur darzustellen, listen Sie die drei Kanäle in einer 2D-Tabelle auf, wobei jede Spalte einen Kanal und jede Zeile ein Wertetripel enthält.

#### Verwandte Themen

[2D-Achsensysteme](../concepts/diadem_5_041.html) | [2D-Tabellen](../concepts/diadem_5_044.html) | [3D-Achsensysteme](../concepts/diadem_5_043.html) | [Einfügen von Report-Objekten](../concepts/diadem_5_04.html) | [Grafiken, Linien und vordefinierte Objekte](../concepts/diadem_5_047.html) | [Polarachsensysteme](../concepts/diadem_5_042.html) | [Texte, Kommentare und Formeln](../concepts/diadem_5_046.html)

<!--NI_TOPIC bundle=diadem path=concepts/diadem_5_046.html language=dede -->
## TOPIC 00042: Texte, Kommentare und Formeln

- bundle_id: `diadem`
- source_path: `concepts/diadem_5_046.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/dede/concepts/diadem_5_046.html
- source_language: `dede`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Reports erstellen](../concepts/diadem_5_01.html) > [Einfügen von Report-Objekten](../concepts/diadem_5_04.html) > Texte, Kommentare und Formeln

### Texte, Kommentare und Formeln

Zum Erstellen von Texten können Sie Texte, Textobjekte oder Kommentare verwenden. Mit dem Text erstellen Sie einheitlich formatierte Texte wie Überschriften, mit dem Textobjekt mehrzeilige Texte mit unterschiedlichen Formatierungen und mit Kommentaren platzieren Sie Beschriftungen an markanten Punkten im Arbeitsblatt. Verwenden Sie Formelgrafiken, um eine mathematische Berechnungsvorschriften in den Report einzufügen.

Alle Texte können Sonderzeichen, Formelausdrücke und DIAdem-Variablen enthalten, die DIAdem mit dem Report aktualisiert. Um beispielsweise die aktuelle Zeit anzuzeigen, fügen Sie @@CurrTime@@ in einen Text ein. DIAdem erkennt an den @@-Zeichen, dass CurrTime eine Variable ist. Neben den Programm- und Hilfsvariablen können Sie auch Anwendervariablen verwenden. Weitere Informationen zu Variablen finden Sie im Abschnitt [Verwenden von Variablen](../concepts/diadem_6_032.html).

#### Verwandte Themen

[2D-Achsensysteme](../concepts/diadem_5_041.html) | [2D-Tabellen](../concepts/diadem_5_044.html) | [3D-Achsensysteme](../concepts/diadem_5_043.html) | [3D-Tabellen](../concepts/diadem_5_045.html) | [Einfügen von Report-Objekten](../concepts/diadem_5_04.html) | [Grafiken, Linien und vordefinierte Objekte](../concepts/diadem_5_047.html) | [Polarachsensysteme](../concepts/diadem_5_042.html)

<!--NI_TOPIC bundle=diadem path=concepts/diadem_5_0463.html language=dede -->
## TOPIC 00043: Kommentare

- bundle_id: `diadem`
- source_path: `concepts/diadem_5_0463.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/dede/concepts/diadem_5_0463.html
- source_language: `dede`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Reports erstellen](../concepts/diadem_5_01.html) > [Einfügen von Report-Objekten](../concepts/diadem_5_04.html) > [Texte, Kommentare und Formeln](../concepts/diadem_5_046.html) > Kommentare

### Kommentare

Verwenden Sie Kommentare, um auf markante Punkte im Arbeitsblatt hinzuweisen. Um einen Kommentar zu erstellen, wählen Sie **Texte»Kommentar**. Ziehen Sie mit der Maus an der Stelle des Arbeitsblatts einen Rahmen auf, auf die der Kommentar zeigen soll. DIAdem erstellt einen Pfeil mit einem Textrahmen. Doppelklicken Sie auf den Textrahmen und geben Sie den Text ein. Wie für das Textobjekt geben Sie die Schriftgröße fest vor. Verwenden Sie die Formatleiste von DIAdem-REPORT, um Kommentare zu formatieren.

Wenn Sie das Pfeilende verankern, bewegt sich die Pfeilspitze beim Verschieben des Kommentars nicht. Um den Pfeil neu zu positionieren, klicken Sie auf den Pfeil und bewegen das Quadrat an der Pfeilspitze.

Wenn Sie den Pfeil markieren und löschen, erhalten Sie einen Kommentarrahmen. Ein Kommentarrahmen behält, anders als ein Text, seine Größe unabhängig von der eingegebenen Textmenge. Überschreitet die Textmenge die Rahmengröße, bricht DIAdem den Text um und zeigt nur so viel vom Text an, wie in den Rahmen passt.

#### Verwandte Themen

[Formelgrafiken](../concepts/diadem_5_0464.html) | [Texte, Kommentare und Formeln](../concepts/diadem_5_046.html) | [Texte](../concepts/diadem_5_0461.html) | [Textobjekte](../concepts/diadem_5_0462.html)

<!--NI_TOPIC bundle=diadem path=concepts/diadem_5_0464.html language=dede -->
## TOPIC 00044: Formelgrafiken

- bundle_id: `diadem`
- source_path: `concepts/diadem_5_0464.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/dede/concepts/diadem_5_0464.html
- source_language: `dede`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Reports erstellen](../concepts/diadem_5_01.html) > [Einfügen von Report-Objekten](../concepts/diadem_5_04.html) > [Texte, Kommentare und Formeln](../concepts/diadem_5_046.html) > Formelgrafiken

### Formelgrafiken

Verwenden Sie Formelgrafiken, um eine mathematische Formel in ein Arbeitsblatt einzufügen. Um eine Formelgrafik zu erstellen, wählen Sie **Texte»Formelgrafik** und ziehen an der Stelle des Arbeitsblatts einen Rahmen auf, wo Sie die Formel platzieren wollen. Doppelklicken Sie auf die Formelgrafik und schreiben Sie die Formel in das Eingabefeld auf der Registerkarte **Text**. Sie können die Formel wie im Taschenrechner eingeben, beispielsweise die Berechnung einer Quadratwurzel als y=SQR(x^3). Die Vorschau zeigt die mathematische Darstellung der Formel, wie sie im Arbeitsblatt erscheinen wird. Komplexere Formeln und Ausdrücke geben Sie in der Mathematical Markup Language (MathML) ein, in der DIAdem Formeln in der Reportdatei ablegt. Wie einen Kommentar können Sie die Formelgrafik mit einen Rahmen und einem Pfeil versehen. Die Größe des Rahmens bestimmt die Größe der Formeldarstellung.

#### Verwandte Themen

[Kommentare](../concepts/diadem_5_0463.html) | [Texte, Kommentare und Formeln](../concepts/diadem_5_046.html) | [Texte](../concepts/diadem_5_0461.html) | [Textobjekte](../concepts/diadem_5_0462.html)

<!--NI_TOPIC bundle=diadem path=concepts/diadem_6_022.html language=dede -->
## TOPIC 00045: Scripte testen und speichern

- bundle_id: `diadem`
- source_path: `concepts/diadem_6_022.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/dede/concepts/diadem_6_022.html
- source_language: `dede`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Arbeitsabläufe automatisieren](../concepts/diadem_6_01.html) > [Arbeiten mit Scripten](../concepts/diadem_6_02.html) > Scripte testen und speichern

### Scripte testen und speichern

Um das im Script-Editor sichtbare Script zu testen, klicken Sie auf **Script ausführen** in der Befehlsleiste von DIAdem-SCRIPT. Auf diese Weise können Sie überprüfen, ob das Script fehlerfrei arbeitet und die Arbeitsschritte wie erwartet durchführt.

Wenn DIAdem das Script nicht fehlerfrei abarbeitet, verwenden Sie den Script-Debugger, um Fehler im Script zu finden. Sobald ein Fehler auftritt, setzt der Debugger einen grünen Marker vor die fehlerhafte Script-Zeile. Der aufgetretene Fehler erscheint auf der Registerkarte **Logdatei** im Überwachungsbereich unterhalb des Scripts. Um nur die aktuellen Fehlermeldungen auf dieser Registerkarte zu sehen, wählen Sie zuvor im Kontextmenü **Logdatei-Ansicht löschen**. Um Variablen zu überwachen, übernehmen Sie die Variable mit Drag&Drop aus dem Script in das Überwachungsfenster des Informationsbereichs. Wenn Sie im Script Haltepunkte setzen, zeigt DIAdem den Inhalt der Variablen an.

|  | Hinweis Aus lizenzrechtlichen Gründen wird der Debugger nicht mit DIAdem installiert. Weitere Informationen zur Installation des Debuggers finden Sie auf der Seite Microsoft Debugger der DIAdem-Hilfe. |
| --- | --- |

[IMAGE alt='image' src='image/script_scriptf1.png'] Speichern Sie das Script, um es später zu verwenden. Um mehrere im Script-Editor geöffnete Scripte zu speichern, rechtsklicken Sie auf die Registerleiste und wählen im Kontextmenü **Alle Dateien speichern**. Um ein gespeichertes Script auszuführen, ohne es in den Script-Editor zu laden, klicken Sie auf **Datei ausführen**. Wenn Sie ein Script häufig aufrufen, weisen Sie es einer Schaltfläche der Funktionsgruppen **DIAdem-Scripte** zu. Diese Funktionsgruppe ist in allen DIAdem-Modulen verfügbar, sodass Sie diese Scripte in jedem Modul aufrufen können.

|  | Hinweis Darüber hinaus können Sie Scripte im Aufruf von DIAdem angeben, um Abläufe direkt beim Start von DIAdem automatisch zu starten. Weitere Informationen zum automatischen Start von Scripten finden Sie im Abschnitt Programmstart mit Parametern. |
| --- | --- |

Sie können alle Dateien, die Sie für ein Projekt benötigen, als Arbeitsbereich speichern. Laden Sie dazu alle Dateien wie die verschiedenen Scripte, Variablendefinitionsdateien und Listendateien des Projekts und erstellen Sie einen Arbeitsbereich über **Datei»Arbeitsbereich speichern unter**. Arbeitsbereiche speichert DIAdem mit der Dateinamenserweiterung .wsp. Um alle Projektdateien automatisch zu laden, laden Sie einen Arbeitsbereich über **Datei»Arbeitsbereich öffnen** oder geben einen Arbeitsbereich in **Einstellungen»DIAdem-Einstellungen»SCRIPT** als Startdatei an.

Sie können Scripte und [Anwenderdialoge](../concepts/diadem_6_042.html) verschlüsseln, um Scripte auf anderen Rechnern einzusetzen, ohne dass die Bediener das Script oder den Anwenderdialog verändern können. Um Scripte und Anwenderdialoge zu verschlüsseln, wählen Sie **Script»VBS-Script/SUD-Datei verschlüsseln** und laden das entsprechende Script oder die Dialogdatei. DIAdem speichert verschlüsselte Scripte mit der Dateinamenserweiterung .vbc und verschlüsselte Anwenderdialoge mit der Dateinamenserweiterung .suc.

DIAdem speichert Scripte standardmäßig im Unicode-Format. Unicode-Zeichen schließen auch chinesische, japanische und arabische Zeichen ein. Um ein Script stattdessen im ANSI-Format zu speichern, wählen Sie **Datei»Kodierung ändern**.

#### Verwandte Themen

[Arbeiten mit Scripten](../concepts/diadem_6_02.html) | [Scripte bearbeiten](../concepts/diadem_6_021.html)

<!--NI_TOPIC bundle=diadem path=concepts/diadem_6_042c.html language=enus -->
## TOPIC 00046: Saving and Testing User Dialog Boxes

- bundle_id: `diadem`
- source_path: `concepts/diadem_6_042c.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/concepts/diadem_6_042c.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Automating Sequences](../concepts/diadem_6.01.html) > [Creating User Interfaces](../concepts/diadem_6.04.html) > [Creating User Dialog Boxes](../concepts/diadem_6.042.html) > Saving and Testing User Dialog Boxes

Saving and Testing User Dialog Boxes

To check the appearance of the dialog box, select **View»Preview**. To test the dialog box functions, select **View»Test in DIAdem**. This function checks the variable definitions and the event definitions of each control.

After designing and testing a dialog box, you save the user dialog box in a dialog box file with the filename extension .sud. In a dialog box file, you can save several dialog boxes, so that all the dialog boxes of a project are in the same SUD file. To add a dialog box to a dialog box file, select **Dialog Box»New**. To copy and to delete dialog boxes, select **Dialog Box»Dialog Box Overview**.

You can save parts of the user dialog box in the catalog window in the dialog editor. Select **View»Catalog** to open the catalog. Select the dialog box controls that you want to save and select **Copy** from the context menu. Then click the catalog window and select **Paste** from the context menu to copy the selected controls from the clipboard to the catalog. You save the properties and events together with the controls. You can save catalogs in a CAT file, create new catalogs, and load catalogs.

#### Related Topics

[Controlling User Dialog Boxes](../concepts/diadem_6_042b.html) | [Creating User Dialog Boxes](../concepts/diadem_6.042.html) | [Defining User Dialog Boxes](../concepts/diadem_6_042a.html)

<!--NI_TOPIC bundle=diadem path=contextmenu/objects/contextmenu_objects_imenupoints.htm language=enus -->
## TOPIC 00047: Collection: MenuPoints

- bundle_id: `diadem`
- source_path: `contextmenu/objects/contextmenu_objects_imenupoints.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/contextmenu/objects/contextmenu_objects_imenupoints.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Context Menu Object](../objects/contextmenu_objects_contextmenu.htm) > [Objects](../objects/contextmenu_objects_overview.htm) > Collection: MenuPoints

Collection: MenuPoints

Collection of context menu items.

In a script you can access the context menus of the [File Browser](../../dlgnavigator/dlgnavigator/navi_search_tree_window.htm), [Data Browser](../../dlgnavigator/dlgnavigator/navi_datastore_tree.htm), [Search Results List of a DataFinder](../../dlgnavigator/dlgnavigator/navi_search_resultlist_window.htm), [Search Result List of a Data Store](../../dlgnavigator/dlgnavigator/navi_datastore_resultlist_window.htm), a [Tree](../../sudref/objects/sud_objects_totreenodeint.htm) in user dialog boxes, an [Extended Table](../../sudref/objects/sud_objects_tovirtgridctrl.htm) in user dialog boxes and the channel preview, as well as the context menus of DIAdem VIEW.

Read and write access.

|  | Note To test the following example script, you must first save the script and register the script as a user command in the dialog box that opens when you select Settings»Extensions»User Commands. |
| --- | --- |

The following example executes the MyNavigatorOnShowingContextMenu user command when you open the context menu in DIAdem NAVIGATOR and the MyViewOnShowingContextMenu user command when you open the context menu in DIAdem VIEW. These user commands add a new entry to the existing context menus when you open the context menu in the browser, the search results list, the axis system, or the channel table. 
When you click one of the defined context menu items, the example executes the MyNavigatorOnContextMenuPointSelected user command or the MyViewOnContextMenuPointSelected user command and displays the selected item in a message.

[Copy script](javascript:void(0);)

```text
' --- For DIAdem-NAVIGATOR ------------------------------------------
Call AddUserCommandToEvent("Navigator.Events.OnShowingContextMenu","MyNavigatorOnShowingContextMenu")
Call AddUserCommandToEvent("Navigator.Events.OnContextMenuPointSelected","MyNavigatorOnContextMenuPointSelected")

Sub MyNavigatorOnShowingContextMenu(ParentObj, MenuPoints)
  If (ParentObj.IsKindOf("Browser")) Then
    Call MenuPoints.Add("My Browser Menu Point", 1)
  End If
  If (ParentObj.IsKindOf("ResultsList")) Then
    Call MenuPoints.Add("My ResultsList Menu Point", 2)
  End If
End Sub

Sub MyNavigatorOnContextMenuPointSelected(ParentObj, MenuPoint)
  Select Case MenuPoint.ID
    Case 1    Call MsgBoxDisp("DIAdem-NAVIGATOR: MyMenuPoint1 selected")
    Case 2    Call MsgBoxDisp("DIAdem-NAVIGATOR: MyMenuPoint2 selected")
  End Select
End Sub


' --- For DIAdem-VIEW -----------------------------------------------
Call AddUserCommandToEvent("View.Events.OnShowingContextMenu","MyViewOnShowingContextMenu")
Call AddUserCommandToEvent("View.Events.OnContextMenuPointSelected","MyViewOnContextMenuPointSelected")

Sub MyViewOnShowingContextMenu(Area, MenuPoints)
  If (Area.DisplayObjType = "CurveChart2D") Then
    Call MenuPoints.Add("My CurveChart Menu Point", 1)
  End If
  If (Area.DisplayObjType = "ChannelTable") Then
    Call MenuPoints.Add("My ChannelTable Menu Point", 2)
  End If
End Sub

Sub MyViewOnContextMenuPointSelected(Area, MenuPoint)
  Select Case MenuPoint.ID
    Case 1    Call MsgBoxDisp("DIAdem-VIEW: MyMenuPoint1 selected")
    Case 2    Call MsgBoxDisp("DIAdem-VIEW: MyMenuPoint2 selected")
  End Select
End Sub
```

The following example shows the functionality of a context menu in an extended table. If you right-click a cell, the example creates a context menu and displays the selected entry of the context menu.

[Copy script](javascript:void(0);)

```text
Sub XTable1_EventContextMenuPointSelected(ByRef This, Row, Col, MenuPoint)
    Call MsgBox("Row: " & Row & "; Column: " & Col & VBCrLf & "Menu entry: " & MenuPoint.Text)
End Sub

Sub XTable1_EventContextMenuShowing(ByRef This, Row, Col, MenuPoints) 
  Call MenuPoints.Add("Menu 1",1)
  Call MenuPoints.Add("Menu 2",2)
End Sub
```

The following example creates a tree in a user dialog box. If you right-click a node, the example creates a context menu and displays the selected entry of the context menu.

[Copy script](javascript:void(0);)

```text
Sub Tree1_EventInitialize(ByRef This)
  Call CreateDefaultTree(This)
End Sub

Sub Tree1_EventContextMenuShowing(ByRef This, ByRef Node, MenuPoints)
  Call MenuPoints.Add("Menu 1",1)
  Call MenuPoints.Add("Menu 2",2)
End Sub

Sub Tree1_EventContextMenuPointSelected(ByRef This, ByRef Node, MenuPoint)
    Call MsgBox("Selected Node: " & Node.Text & VBCrLf & "Menu entry: " & MenuPoint.Text)
End Sub

Sub CreateDefaultTree(ByRef This)
  Dim oRoot, oMainNode
  Set oRoot = This.Nodes.Add("Tools")
  oRoot.Key = "tools"
  oRoot.Expanded = true
  Set oMainNode = oRoot.Nodes.Add("Electric Tools")
  oMainNode.Key = "electric"
  oMainNode.Nodes.Add("Drill").Key = "drill"
  oMainNode.Nodes.Add("Saw").Key = "saw"
  Set oMainNode = oRoot.Nodes.Add("Hand Tools")
  oMainNode.Key = "handtool"
  oMainNode.Nodes.Add("Hammer").Key = "hammer"
  oMainNode.Nodes.Add("Screwdriver").Key = "screwdriver"
  oMainNode.Nodes.Add("Tongs").Key = "tongs"
End Sub
```

#### Properties

[Count](../properties/contextmenu_property_count_imenupoints.htm)

#### Methods

[Add](../methods/contextmenu_method_add_imenupoints.htm) | [IsIDUsed](../methods/contextmenu_method_isidused_imenupoints.htm) | [Item](../methods/contextmenu_method_item_imenupoints.htm) | [Remove](../methods/contextmenu_method_remove_imenupoints.htm) | [RemoveAll](../methods/contextmenu_method_removeall_imenupoints.htm)

#### See Also

[Objects Overview](../objects/contextmenu_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=contextmenu/objects/contextmenu_objects_overview.htm language=enus -->
## TOPIC 00048: Objects

- bundle_id: `diadem`
- source_path: `contextmenu/objects/contextmenu_objects_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/contextmenu/objects/contextmenu_objects_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Context Menu Object](../objects/contextmenu_objects_contextmenu.htm) > Objects

Objects

If an event occurs, you can call a [user command](../../genshell/genshell/genshell_user_commands.htm) in order to react to the event. A possible event is when you call a context menu (OnShowingContextMenu) or when you select a context menu item (OnContextMenuPointSelected) in DIAdem NAVIGATOR or DIAdem VIEW.

In a script you can access the context menus of the [File Browser](../../dlgnavigator/dlgnavigator/navi_search_tree_window.htm), [Data Browser](../../dlgnavigator/dlgnavigator/navi_datastore_tree.htm), [Search Results List of a DataFinder](../../dlgnavigator/dlgnavigator/navi_search_resultlist_window.htm), [Search Result List of a Data Store](../../dlgnavigator/dlgnavigator/navi_datastore_resultlist_window.htm), a [Tree](../../sudref/objects/sud_objects_totreenodeint.htm) in user dialog boxes, an [Extended Table](../../sudref/objects/sud_objects_tovirtgridctrl.htm) in user dialog boxes and the channel preview, as well as the context menus of DIAdem VIEW.

A context menu consists of several context menu items and the context menu object consists of a collection of single objects that you can create, delete, and modify with a script. You can access the single objects and the collection. Use the [Set statement](../../vbs/general/vbs_set.htm) to assign objects to a variable and to make it easier to access these objects. You use the Add methods to create new objects. You use the Remove methods to remove existing objects. You use properties to change objects.

The following section shows the structure of the context menu objects and how you can click to the objects:

[MenuPoints](../objects/contextmenu_objects_imenupoints.htm) 
  [IMAGE alt='image' src='../image/lastnode.gif'] [MenuPoint](../objects/contextmenu_objects_imenupoint.htm) 
       [IMAGE alt='image' src='../image/lastnode.gif'] [MenuPoints](../objects/contextmenu_objects_imenupoints.htm)

<!--NI_TOPIC bundle=diadem path=contextmenu/properties/contextmenu_property_check_imenupoint.htm language=enus -->
## TOPIC 00049: Property: Check for MenuPoint

- bundle_id: `diadem`
- source_path: `contextmenu/properties/contextmenu_property_check_imenupoint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/contextmenu/properties/contextmenu_property_check_imenupoint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Context Menu Object](../objects/contextmenu_objects_contextmenu.htm) > [Properties](../properties/contextmenu_property_overview.htm) > Property: Check for MenuPoint

Property: Check for MenuPoint

Specifies whether a context menu item is active. DIAdem identifies the enabled items with a tick in front of the item.

```text
Object.Check
```

| Object | MenuPointObject with this property |
| --- | --- |
| Object.Check | LongInteger with read and write access |

|  | Note To test the following example script, you must first save the script and register the script as a user command in the dialog box that opens when you select Settings»Extensions»User Commands. |
| --- | --- |

The following example adds the item MyMenuPoint1 to the context menu and enables this item:

[Copy script](javascript:void(0);)

```text
'--- For DIAdem-NAVIGATOR ------------------------------------------
Call AddUserCommandToEvent("Navigator.Events.OnShowingContextMenu","MyNavigatorOnShowingContextMenu")

Sub MyNavigatorOnShowingContextMenu(ParentObj, MenuPoints)
  MenuPoints.Add("MyMenuPoint1", 1).Check = TRUE
End Sub


'--- For DIAdem-VIEW ------------------------------------------
Call AddUserCommandToEvent("View.Events.OnShowingContextMenu","MyViewOnShowingContextMenu")

Sub MyViewOnShowingContextMenu(Area, MenuPoints)
  MenuPoints.Add("MyMenuPoint1", 1).Check = TRUE
End Sub
```

#### See Also

[Objects Overview](../objects/contextmenu_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=contextmenu/properties/contextmenu_property_count_imenupoints.htm language=enus -->
## TOPIC 00050: Property: Count for MenuPoints

- bundle_id: `diadem`
- source_path: `contextmenu/properties/contextmenu_property_count_imenupoints.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/contextmenu/properties/contextmenu_property_count_imenupoints.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Context Menu Object](../objects/contextmenu_objects_contextmenu.htm) > [Properties](../properties/contextmenu_property_overview.htm) > Property: Count for MenuPoints

Property: Count for MenuPoints

Specifies the number of entries in the context menu.

```text
Object.Count
```

| Object | MenuPointsObject with this property |
| --- | --- |
| Object.Count | LongInteger with read access |

|  | Note To test the following example script, you must first save the script and register the script as a user command in the dialog box that opens when you select Settings»Extensions»User Commands. |
| --- | --- |

The following example disables all entries in the context menu.

[Copy script](javascript:void(0);)

```text
'--- For DIAdem-NAVIGATOR ------------------------------------------
Call AddUserCommandToEvent("Navigator.Events.OnShowingContextMenu","MyNavigatorOnShowingContextMenu")

Sub MyNavigatorOnShowingContextMenu(ParentObj, MenuPoints)
Dim oMenuPoint, Index
  For Index = 1 To MenuPoints.Count
    Set oMenuPoint = MenuPoints.Item(Index)
    oMenuPoint.Enable(FALSE)
  Next
End Sub


'--- For DIAdem-VIEW ------------------------------------------
Call AddUserCommandToEvent("View.Events.OnShowingContextMenu","MyViewOnShowingContextMenu")

Sub MyViewOnShowingContextMenu(Area, MenuPoints)
Dim oMenuPoint, Index
  For Index = 1 To MenuPoints.Count
    Set oMenuPoint = MenuPoints.Item(Index)
    oMenuPoint.Enable(FALSE)
  Next
End Sub
```

#### See Also

[Objects Overview](../objects/contextmenu_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=contextmenu/properties/contextmenu_property_enable_imenupoint.htm language=enus -->
## TOPIC 00051: Property: Enable for MenuPoint

- bundle_id: `diadem`
- source_path: `contextmenu/properties/contextmenu_property_enable_imenupoint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/contextmenu/properties/contextmenu_property_enable_imenupoint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Context Menu Object](../objects/contextmenu_objects_contextmenu.htm) > [Properties](../properties/contextmenu_property_overview.htm) > Property: Enable for MenuPoint

Property: Enable for MenuPoint

Specifies whether DIAdem disables a context menu item.

```text
Object.Enable
```

| Object | MenuPointObject with this property |
| --- | --- |
| Object.Enable | LongInteger with read and write access |

|  | Note To test the following example script, you must first save the script and register the script as a user command in the dialog box that opens when you select Settings»Extensions»User Commands. |
| --- | --- |

The following example disables all entries in the context menu.

[Copy script](javascript:void(0);)

```text
'--- For DIAdem-NAVIGATOR ------------------------------------------
Call AddUserCommandToEvent("Navigator.Events.OnShowingContextMenu","MyNavigatorOnShowingContextMenu")

Sub MyNavigatorOnShowingContextMenu(ParentObj, MenuPoints)
  Dim MenuPoint
  For Each MenuPoint in MenuPoints
    MenuPoint.Enable(FALSE)
  Next
End Sub


'--- For DIAdem-VIEW ------------------------------------------
Call AddUserCommandToEvent("View.Events.OnShowingContextMenu","MyViewOnShowingContextMenu")

Sub MyViewOnShowingContextMenu(Area, MenuPoints)
  Dim MenuPoint
  For Each MenuPoint in MenuPoints
    MenuPoint.Enable(FALSE)
  Next
End Sub
```

#### See Also

[Objects Overview](../objects/contextmenu_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=contextmenu/properties/contextmenu_property_id_imenupoint.htm language=enus -->
## TOPIC 00052: Property: ID for MenuPoint

- bundle_id: `diadem`
- source_path: `contextmenu/properties/contextmenu_property_id_imenupoint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/contextmenu/properties/contextmenu_property_id_imenupoint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Context Menu Object](../objects/contextmenu_objects_contextmenu.htm) > [Properties](../properties/contextmenu_property_overview.htm) > Property: ID for MenuPoint

Property: ID for MenuPoint

Specifies the ID of a context menu item. Use the ID to determine which action DIAdem executes in the OnContextMenuPointSelected event.

```text
Object.ID
```

| Object | MenuPointObject with this property |
| --- | --- |
| Object.ID | LongInteger with read and write access |

|  | Note Assign only values less than 22000 to an ID. |
| --- | --- |

|  | Note To test the following example script, you must first save the script and register it as a user command in the dialog box that opens when you select Settings»Extensions»User Commands. |
| --- | --- |

The following example deletes all the items from the context menu. The example adds three new items to the context menu and then deletes the item MyMenuPoint3. If you click a context menu item, a message displays:

[Copy script](javascript:void(0);)

```text
'--- For DIAdem-NAVIGATOR ------------------------------------------
Call AddUserCommandToEvent("Navigator.Events.OnShowingContextMenu", "MyOnShowingContextMenu")
Call AddUserCommandToEvent("Navigator.Events.OnContextMenuPointSelected","MyOnContextMenuPointSelected")

Sub MyNavigatorOnShowingContextMenu(ParentObj, MenuPoints)
  Call MenuPoints.RemoveAll
  Call MenuPoints.Add("MyMenuPoint1", 1)
  Call MenuPoints.Add("MyMenuPoint2", 2)
  Call MenuPoints.Add("MyMenuPoint3", 3)
  Call MenuPoints.Remove(3)
End Sub

Sub MyNavigatorOnContextMenuPointSelected(ParentObj, MenuPoint)
  Select Case MenuPoint.ID
    Case 1    Call MsgBoxDisp("DIAdem-NAVIGATOR: MyMenuPoint1 selected")
    Case 2    Call MsgBoxDisp("DIAdem-NAVIGATOR: MyMenuPoint2 selected")
  End Select
End Sub


'--- For DIAdem-VIEW ------------------------------------------
Call AddUserCommandToEvent("View.Events.OnShowingContextMenu", "MyViewOnShowingContextMenu")
Call AddUserCommandToEvent("View.Events.OnContextMenuPointSelected","MyViewOnContextMenuPointSelected")

Sub MyViewOnShowingContextMenu(Area, MenuPoints)
  Call MenuPoints.RemoveAll
  Call MenuPoints.Add("MyMenuPoint1", 1)
  Call MenuPoints.Add("MyMenuPoint2", 2)
  Call MenuPoints.Add("MyMenuPoint3", 3)
  Call MenuPoints.Remove(3)
End Sub

Sub MyViewOnContextMenuPointSelected(Area, MenuPoint)
  Select Case MenuPoint.ID
    Case 1    Call MsgBoxDisp("DIAdem-VIEW: MyMenuPoint1 selected")
    Case 2    Call MsgBoxDisp("DIAdem-VIEW: MyMenuPoint2 selected")
  End Select
End Sub
```

[Objects Overview](../objects/contextmenu_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=contextmenu/properties/contextmenu_property_menupoints_imenupoint.htm language=enus -->
## TOPIC 00053: Property: MenuPoints for MenuPoint

- bundle_id: `diadem`
- source_path: `contextmenu/properties/contextmenu_property_menupoints_imenupoint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/contextmenu/properties/contextmenu_property_menupoints_imenupoint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Context Menu Object](../objects/contextmenu_objects_contextmenu.htm) > [Properties](../properties/contextmenu_property_overview.htm) > Property: MenuPoints for MenuPoint

Property: MenuPoints for MenuPoint

Returns the items of a submenu.

```text
Set oMenuPoints = Object.MenuPoints
```

| Object | MenuPointObject with this property |
| --- | --- |
| oMenuPoints | MenuPointsReturned object |

|  | Note To test the following example script, you must first save the script and register the script as a user command in the dialog box that opens when you select Settings»Extensions»User Commands. |
| --- | --- |

The following example creates an item with several sub-items in the context menu:

[Copy script](javascript:void(0);)

```text
'--- For DIAdem-NAVIGATOR ------------------------------------------
Call AddUserCommandToEvent("Navigator.Events.OnShowingContextMenu","MyNavigatorOnShowingContextMenu")

Sub MyNavigatorOnShowingContextMenu(ParentObj, MenuPoints)
Dim MyMenuPoint
  Call MenuPoints.RemoveAll()
  Call MenuPoints.Add("MenuPoint1", 1)
  Set MyMenuPoint = MenuPoints.Add("SubMenu", 2)
  Call MyMenuPoint.MenuPoints.Add("SubMenuPoint1", 3)
  Call MyMenuPoint.MenuPoints.Add("SubMenuPoint2", 4)
End Sub


'--- For DIAdem-VIEW ------------------------------------------
Call AddUserCommandToEvent("View.Events.OnShowingContextMenu","MyViewOnShowingContextMenu")

Sub MyViewOnShowingContextMenu(Area, MenuPoints)
Dim MyMenuPoint
  Call MenuPoints.RemoveAll()
  Call MenuPoints.Add("MenuPoint1", 1)
  Set MyMenuPoint = MenuPoints.Add("SubMenu", 2)
  Call MyMenuPoint.MenuPoints.Add("SubMenuPoint1", 3)
  Call MyMenuPoint.MenuPoints.Add("SubMenuPoint2", 4)
End Sub
```

#### See Also

[Objects Overview](../objects/contextmenu_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=contextmenu/properties/contextmenu_property_overview.htm language=enus -->
## TOPIC 00054: Properties

- bundle_id: `diadem`
- source_path: `contextmenu/properties/contextmenu_property_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/contextmenu/properties/contextmenu_property_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Context Menu Object](../objects/contextmenu_objects_contextmenu.htm) > Properties

Properties

Properties determine the appearance and the behavior of objects or generate new objects. These new objects can have properties and methods.

The subordinate topics contained in the tree on the contents tab of the Help describe all properties of the context menu object.

<!--NI_TOPIC bundle=diadem path=crash/chest_tti.html language=enus -->
## TOPIC 00055: TTI(d)

- bundle_id: `diadem`
- source_path: `crash/chest_tti.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/crash/chest_tti.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Crash Analysis Criteria](../crash/crash_intro.html) > [Chest Criteria](../crash/chest_criteria.html) > TTI(d)

TTI(d)

TTI(d) is the abbreviation for Thoracic Trauma Index (Thorax Trauma Index).

#### Description

The thorax trauma index is an injury criterion for the thorax in the case of a side impact. The TTI(d) is the mean of the lateral maximum acceleration of the abdominal spine (12th spinal segment) and the higher of the two values for the maximum acceleration of the upper (4th) and lower (8th) Rib.

#### Mathematical Calculation

The TTI value is calculated with the following formula:

[IMAGE alt='image' src='image/f_tti_1.gif']

[IMAGE alt='image' src='image/f_tti_2.gif']

| with | A(upr.rib) | Maximum acceleration of the upper rib; [g] |
| --- | --- | --- |
|  | A(lwr.rib) | Maximum acceleration of the lower rib; [g] |
|  | A(max.rib) | Maximum of A(upr.rib) and A(lwr.rib); [g] |
|  | A(lwr.spine) | Maximum acceleration of the lower spine; [g] |

#### Determining Input Values

Preprocessing the acceleration data of the single sensors (see also [CFC Filter](../crash/misc_cfc.html):

1. Filtering with CFC180
2. Reduction of the sampling rate to 1600 Hz
3. Removal of bias
4. Filtering with FIR100
5. Transferring the reduced sampling rate to the original sampling rate (oversampling, only SAE)

Due to the sign regulations in SAE J1733, the acceleration values have to be positive absolute maximum values. If test data with negative absolute maximum values are to be evaluated, the measurement data must first be inverted.

The calculation must use the original measurement data, not selected data sections, otherwise the digital filters may have differing transient responses.

#### ISO TS 13499 Code

The ISO code describes the input channels for the TTI(d) as follows:

? ? RIBS ?? UP ?? AC Y C : Upper Ribs Acceleration Y, CFC 180

? ? RIBS ?? LO ?? AC Y C : Lower Ribs Acceleration Y, CFC 180

? ? SPIN 12 ?? SI AC Y C : Spinal Acceleration Y, CFC 180

? ? SPIN 12 ?? E1 AC Y C : Spinal Acceleration Y, CFC 180

#### Relevant Laws and Regulations

- FMVSS 214, S5.1
- FMVSS 214, S6.13.5
- SAE J1727, 6.13

[IMAGE alt='image' src='image/crashkreis.gif'] 
 
 
Based on the Crash Analysis, Criteria Description of the Measured Data Processing Vehicle Safety Workgroup

<!--NI_TOPIC bundle=diadem path=crash/crash_intro.html language=enus -->
## TOPIC 00056: Crash Analysis Criteria

- bundle_id: `diadem`
- source_path: `crash/crash_intro.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/crash/crash_intro.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Crash Analysis Criteria

Crash Analysis Criteria

[IMAGE alt='image' src='image/crashkreis.gif']The following section contains descriptions of the crash analysis criteria of the workgroup measurement data processing vehicle safety, algorithm workgroup. The order in which the crash analysis criteria are described follows the structure of the human body.

The description of the criteria contains the name, the mathematical calculation, the input unit, the coding in compliance with ISO TS 13499, and a list of rules and regulations of the algorithm.

|  | Note All descriptions are subject to a SAE J1733 conform signal polarity (Sign convention). |
| --- | --- |

#### Explanations to ISO TS 13499

The ISO TS 13499 describes a simple exchange format for multi-medial data from vehicle safety tests.

The ISO TS 13499 describes the data storage structure and the coding of measurement channels and their attributes in the channel description.

In the current version you can encode the measurement channels as well as the criteria values described in this documentation.

##### Documents

The following table lists the meaning and source of the various single documents that the ISO TS 13499 contains.

| Document/Version | Contents | Source | Price |
| --- | --- | --- | --- |
| ISO TS 13499 | Main document | www.iso.org | With costs |
| RED*A | Examples and hints | http://standards.iso.org/iso | Free of charge |
| RED B | Channel codes |  |  |
| RED C | Figures |  |  |
| RED D | NHTSA compatibility |  |  |
| RED E | Calculated channels |  |  |

<sup>*</sup>RED - Related Electronic Document

##### Codes

The above document REDB describes the channel codes used in this documentation. You can download the channel codes as a data base free of charge from standards.iso.org.

The following figure shows the main menu of the ISO TS 13499 data base in the internet.

[IMAGE alt='image' src='image/isots13499.gif']

[Head Criteria](../crash/head_criteria.html) | [Neck Criteria](../crash/neck_criteria.html) | [Chest Criteria](../crash/chest_criteria.html) | [Abdominal Criteria](../crash/abdomen_criteria.html) | [Further Crash Criteria](../crash/misc_criteria.html)

<!--NI_TOPIC bundle=diadem path=crash/head_criteria.html language=enus -->
## TOPIC 00057: Description of the Head Criteria

- bundle_id: `diadem`
- source_path: `crash/head_criteria.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/crash/head_criteria.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Crash Analysis Criteria](../crash/crash_intro.html) > Description of the Head Criteria

Description of the Head Criteria

The following head criteria are described in the Crash Analysis Criteria:

- [HIC](../crash/head_hic.html) — Head Injury Criterion
- HAC — Head Acceptability Criterion
- [HIC(d)](../crash/head_hic_d.html) — Performance Criterion
- [HPC](../crash/head_hpc.html) — Head Performance Criterion
- [HCD](../crash/head_hcd.html) — Head Contact Duration
- [BRIC](../crash/head_bric.html) — Rotational Brain Injury Criterion

Head Criteria | [Neck Criteria](../crash/neck_criteria.html) | [Chest Criteria](../crash/chest_criteria.html) | [Abdominal Criteria](../crash/abdomen_criteria.html) | [Further Crash Criteria](../crash/misc_criteria.html)

<!--NI_TOPIC bundle=diadem path=crash/head_hcd.html language=enus -->
## TOPIC 00058: HCD

- bundle_id: `diadem`
- source_path: `crash/head_hcd.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/crash/head_hcd.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Crash Analysis Criteria](../crash/crash_intro.html) > [Head Criteria](../crash/head_criteria.html) > HCD

HCD

HCD is the abbreviation for Head Contact Duration.

#### Description

The HCD value is the standardized maximum integral value of the head acceleration during head contact intervals. The contact intervals are determined using the resultant contact force (calculated from neck force of the upper neck transducer, head acceleration and head mass).

#### Mathematical Calculation

To determine the contact interval, the resultant contact force *F* must be calculated first.

[IMAGE alt='image' src='image/f_hcd.gif']

| with | m | Mass of the head |
| --- | --- | --- |
|  | ai | Head acceleration in the i direction |
|  | Fi | Upper neck force in the i direction |

Contact intervals are all the intervals in which a lower threshold value (threshold level = 200 N) is constantly exceeded and a lower search level (search level = 500 N) is exceeded at least once as the following figure shows.

[IMAGE alt='image' src='image/hcd_contact.gif']

The *HIC<sub>j</sub>* value is calculated for every contact interval Kj.

[IMAGE alt='image' src='image/f_hcd_kj.gif']

[IMAGE alt='image' src='image/f_hcd_hicj.gif']

| with | tjbeg | Start point for contact interval Kj |
| --- | --- | --- |
|  | tjend | End time for contact interval Kj |

The HCD value is then the maximum HIC value of all the contact intervals.

[IMAGE alt='image' src='image/f_hcd_maxhicj.gif']

#### Determining Input Values

The measured values of the head acceleration (ax, ay, az) and the neck force (Fx, Fy, Fz) are filtered in accordance with [CFC 1000](../crash/misc_cfc.html).

#### ISO TS 13499 Code

The ISO code describes the input channels for the HCD as follows:

? ? HEAD 00 ?? ?? AC X A : Head Acceleration X, CFC 1000

? ? HEAD 00 ?? ?? AC Y A : Head Acceleration Y, CFC 1000

? ? HEAD 00 ?? ?? AC Z A : Head Acceleration Z, CFC 1000

? ? NECK UP ?? ?? FO X A : Upper Neck Force X, CFC 1000

? ? NECK UP ?? ?? FO Y A : Upper Neck Force Y, CFC 1000

? ? NECK UP ?? ?? FO Z A : Upper Neck Force Z, CFC 1000

#### Relevant Laws and Regulations

- SAE J2052, 3.3
- SAE J2052, 5
- ISO/TC22/SC12/WG3 N 282 (Issued 1990-03-16)
- TRANS/SC1/WP29/GRSP/R.48/Rev.1, page 19, Annex 4, Appendix 1

[IMAGE alt='image' src='image/crashkreis.gif'] 
 
 
Based on the Crash Analysis, Criteria Description of the Measured Data Processing Vehicle Safety Workgroup

<!--NI_TOPIC bundle=diadem path=crash/head_hic.html language=enus -->
## TOPIC 00059: HIC

- bundle_id: `diadem`
- source_path: `crash/head_hic.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/crash/head_hic.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Crash Analysis Criteria](../crash/crash_intro.html) > [Head Criteria](../crash/head_criteria.html) > HIC

HIC

HIC is the abbreviation for Head Injury Criterion.

#### Description

The HIC value is the standardized maximum integral value of the head acceleration. The length of the corresponding time interval is:

- HIC: unlimited
- HIC36 : maximum 36 ms
- HIC15: maximum 15 ms

#### Mathematical Calculation

The HIC value is calculated with the following formula:

[IMAGE alt='image' src='image/f_hic.gif']

[IMAGE alt='image' src='image/f_res.gif']

with the resultant acceleration a of the center of gravity of the head in units of acceleration of gravity (1 g =9,81 m/s²). Tests in compliance with TRIAS assume (1 g = 9,80 m/s²) for the acceleration of gravity (1 g = 9,80 m/s²). t<sub>1</sub> and t<sub>2</sub> are the moments during an impact for which the HIC value is the maximum value. Measured times are to be specified in seconds.

#### Determining Input Values

The measurement values of the head acceleration (a<sub>x</sub>, a<sub>y</sub>, a<sub>z</sub>) are filtered according to [CFC 1000](../crash/misc_cfc.html).

To define the input values in accordance with ECE-R 80, the measured values for head acceleration (a<sub>x</sub>, a<sub>y</sub>, a<sub>z</sub>) are filtered in accordance with CFC 600.

#### ISO TS 13499 Code

The ISO code describes the input channels for the HIC as follows:

? ? HEAD 00 00 ?? AC X A : Head Acceleration X, CFC 1000

? ? HEAD 00 00 ?? AC Y A : Head Acceleration Y, CFC 1000

? ? HEAD 00 00 ?? AC Z A : Head Acceleration Z, CFC 1000

? ? HEAD 00 00 ?? AC X B : Head Acceleration X, CFC 600, (ECE R80)

? ? HEAD 00 00 ?? AC Y B : Head Acceleration Y, CFC 600, (ECE R80)

? ? HEAD 00 00 ?? AC Z B : Head Acceleration Z, CFC 600, (ECE R80)

#### Relevant Laws and Regulations

- FMVSS 208, S6.2
- SAE J2052, 3.2
- SAE J1727,6.1
- ISO/TC22/SC12/WG3 N 282 Issued 1990-03-16
- ADR69/00, 5.3.1
- ECE–R 80, Annex 4, 1
- ECE–R 22, 7.3.2.5
- EuroNCAP, Front Impact, 10, 10.1
- EuroNCAP, Side Impact, 10, 10.1
- EuroNCAP, Pole Side Impact, 10, 10.1
- EuroNCAP, Assessment Protocol , 5
- EuroNCAP, Pedestrian Testing Protocol, 10.2
- TRIAS 47, Frontal Impact, 2-6
- TRIAS 63, Pedestrian Impact, 2.4
- ISO-MME, Red E (Calculated Value Codes and Channels)

[IMAGE alt='image' src='image/crashkreis.gif'] 
 
 
Based on the Crash Analysis, Criteria Description of the Measured Data Processing Vehicle Safety Workgroup

<!--NI_TOPIC bundle=diadem path=crash/misc_criteria.html language=enus -->
## TOPIC 00060: Description of Additional Criteria

- bundle_id: `diadem`
- source_path: `crash/misc_criteria.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/crash/misc_criteria.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Crash Analysis Criteria](../crash/crash_intro.html) > Description of Additional Criteria

Description of Additional Criteria

The following further criteria are described in the Crash Analysis Criteria:

- [Xms](../crash/misc_xms.html) — Generalization of the 3ms value
- [Xg](../crash/misc_xg.html) — Time range for an acceleration greater than *x<sub>g</sub>*
- [Acomp](../crash/misc_acomp.html) — Average Acceleration During Compression Phase
- [Pulse Test](../crash/misc_pulsetest.html) — Deceleration corridor for Trolley
- [ASI](../crash/misc_asi.html) — Acceleration Severity Index
- [THIV](../crash/misc_thiv.html) — Theoretical Head Impact Velocity
- Gillis-Index — Characteristic value for the assessment of the vehicle safety during a frontal crash.
- NCAP — New Car Assessment Program
- EuroNCAP — European New Car Assessment Program
- [SI](../crash/misc_si.html) — Severity Index
- Integration — Integration procedures used
- Differentiation — Differentiation procedures used
- Energy
- [CFC Filter](../crash/misc_cfc.html) — Channel Frequency Class
- [FIR100 Filter](../crash/misc_fir.html) — Finite Impulse Response

[Head Criteria](../crash/head_criteria.html) | [Neck Criteria](../crash/neck_criteria.html) | [Chest Criteria](../crash/chest_criteria.html) | [Abdominal Criteria](../crash/abdomen_criteria.html) | Further Crash Criteria

<!--NI_TOPIC bundle=diadem path=crash/misc_fir.html language=enus -->
## TOPIC 00061: FIR 100 filters

- bundle_id: `diadem`
- source_path: `crash/misc_fir.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/crash/misc_fir.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Crash Analysis Criteria](../crash/crash_intro.html) > [More Crash Criteria](../crash/misc_criteria.html) > FIR 100 filters

FIR 100 filters

FIR is the abbreviation for Finite Impulse Response

#### Description

FIR filters are digital filters.

#### Mathematical Calculation

Filter characteristics in accordance with FMVSS 214, S6.13.5.4

- Passband frequency: 100 Hz
- Stopband frequency: 189 Hz
- Stopband gain: –50 dB
- Passband ripple: 0,0225 dB

NHTSA algorithm for FIR 100:

- CFC 180 phaseless
- Subsampling to 1600 Hz
- Removal of bias
- FIR filters in accordance with filter characteristic FMVSS 214
- Oversampling back to the original sample rate

#### Determining Input Values

—

#### Relevant Laws and Regulations

- FMVSS 214, S6.13.5.4
- SAE J1727, 6.13

[IMAGE alt='image' src='image/crashkreis.gif'] 
 
 
Based on the Crash Analysis, Criteria Description of the Measured Data Processing Vehicle Safety Workgroup

<!--NI_TOPIC bundle=diadem path=crash/misc_pulsetest.html language=enus -->
## TOPIC 00062: Pulse Test

- bundle_id: `diadem`
- source_path: `crash/misc_pulsetest.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/crash/misc_pulsetest.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Crash Analysis Criteria](../crash/crash_intro.html) > [More Crash Criteria](../crash/misc_criteria.html) > Pulse Test

Pulse Test

The pulse test checks the deceleration corridor for sled tests (Deceleration Corridor for Trolley).

#### Description

In sled tests, you check whether the measured acceleration is within a specific corridor, as shown in the following figures.

- Corridor for ECE–R 44; Annex 7; Appendix 1 
 [IMAGE alt='image' src='image/pulse_ecer44_1.gif']
- Corridor for ECE–R 44; Annex 7; Appendix 2 
 [IMAGE alt='image' src='image/pulse_ecer44_2.gif']
- Corridor for ECE R16 
 [IMAGE alt='image' src='image/pulse_ecer16.gif'] 
 Description of the delay curve or the acceleration curve of the test sled over time in accordance with ECE R 16, Appendix 8 [IMAGE alt='image' src='image/pulse_ecer16_8.gif']
- Corridor for ECE R17; 6.3.1 
 [IMAGE alt='image' src='image/pulse_ecer17.gif']
- Corridor for ECE R80; Annex 4; Figure 1 
 [IMAGE alt='image' src='image/pulse_ecer80.gif']
- Corridor for FMVSS 206; Figure 5 
 [IMAGE alt='image' src='image/pulse_fmvss206.gif']
- Corridor for FMVSS 208; S13.1; Figure 6 
 [IMAGE alt='image' src='image/pulse_fmvss208.gif']
- Acceleration Impulse of Test Sled in Accordance with EN 1789 and DIN 75302, Figure 4 
 [IMAGE alt='image' src='image/pulse_en1789.gif']
- Acceleration impulse in accordance with EN 1789: 1999, Figure 7 
 [IMAGE alt='image' src='image/pulse_en1789_2010.gif']
- Acceleration/Delay requirements for the (48 0 +2 ) km/h delta V Impact Text in accordance with ISO 7176-19:2001(E) 
 [IMAGE alt='image' src='image/pulse_iso7176.gif']
- Low Severity Pulse Corridors in accordance with EuroNCAP, Appendix IV, Figure 17 
 [IMAGE alt='image' src='image/pulse_lowseverity.gif']
- Medium Severity Pulse Corridors in accordance with EuroNCAP, Appendix IV, Figure 18 
 [IMAGE alt='image' src='image/pulse_mediumseverity.gif']
- High Severity Pulse Corridors in accordance with EuroNCAP, Appendix IV, Figure 19 
 [IMAGE alt='image' src='image/pulse_highseverity.gif']

#### Mathematical Calculation

The test must determine whether straight lines between two points exceed the specified range and whether the points are within the given range. As the following figure shows points and their connection lines must be within the corridor.

[IMAGE alt='image' src='image/pulse_calculation.gif']

|  | Note In accordance with DIN 75302 the measurement curve (1) can be moved (2) so that the test can be passed. |
| --- | --- |

#### Determining Input Values

The measurement values of the acceleration are filtered in accordance with [CFC 60](../crash/misc_cfc.html).

#### Relevant Laws and Regulations

- ECE–R 11; 3.5.1
- ECE–R 16; Annex 8
- ECE R17
- ECE–R 44; Annex 7
- ECE–R 80; Annex 4; Figure 1
- EN 1789
- DIN 75302
- FMVSS 208; S13.1
- FMVSS 213
- EuroNCAP Whiplash
- SAE AS 8049, Appendix A
- ISO 7862, Annex A – Annex C

[IMAGE alt='image' src='image/crashkreis.gif'] 
 
 
Based on the Crash Analysis, Criteria Description of the Measured Data Processing Vehicle Safety Workgroup

<!--NI_TOPIC bundle=diadem path=crash/misc_si.html language=enus -->
## TOPIC 00063: SI

- bundle_id: `diadem`
- source_path: `crash/misc_si.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/crash/misc_si.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Crash Analysis Criteria](../crash/crash_intro.html) > [More Crash Criteria](../crash/misc_criteria.html) > SI

SI

#### Description

The SI value assesses the danger of a chest injury (obsolete, similar to HIC {head injury}). This procedure is based on the Wayne-State Curve of Human Tolerance of the human head.

#### Mathematical Calculation

The incremental SI value is calculated with the following formula:

[IMAGE alt='image' src='image/f_si_1.gif']

| with | j | j=1,2, ... T |
| --- | --- | --- |
|  | T | Length of the data set |
|  | N | Values per ms |
|  | A | i-th value of acceleration signal |

The cumulative SI value is calculated with the following formulas:

[IMAGE alt='image' src='image/f_si_2.gif']

[IMAGE alt='image' src='image/f_si_3.gif']

with *j* = 2,3, ... T

#### Determining Input Values

—

#### ISO TS 13499 Code

The ISO code describes the input channels for the SI as follows:

? ? CHST ?? ?? ?? AC X : Chest Acceleration X

#### Relevant Laws and Regulations

- SAE J885

[IMAGE alt='image' src='image/crashkreis.gif'] 
 
 
Based on the Crash Analysis, Criteria Description of the Measured Data Processing Vehicle Safety Workgroup

<!--NI_TOPIC bundle=diadem path=crash/misc_xms.html language=enus -->
## TOPIC 00064: Xms

- bundle_id: `diadem`
- source_path: `crash/misc_xms.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/crash/misc_xms.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Crash Analysis Criteria](../crash/crash_intro.html) > [More Crash Criteria](../crash/misc_criteria.html) > Xms

Xms

Xms is a generalization of the 3ms value.

#### Description

The xms value is the highest amplitude in a measured signal that lasts x milliseconds. The Xms value is specified either as a single peak (SAE), or multiple peaks (ECE-R94, FMVSS). In the cumulative calculation, separate periods of the measurement signal are added, until x milliseconds are reached.

#### Mathematical Calculation

The xms value can be calculated with one peak, as shown in the first and second figure, or with several peaks, as shown in the third figure.

[IMAGE alt='image' src='image/xms_1.gif']

The special case shown in the second figure might have a total time of >x milliseconds.

[IMAGE alt='image' src='image/xms_2.gif']

Since the SAE must have a time span of **at least** x ms, the total time (4.5ms) has to be specified, as shown in the third figure 4.5 ms.

[IMAGE alt='image' src='image/xms_3.gif']

If the sampling rates are constant, the calculation of the accumulated xms value shown in the third figure can be based on the following algorithm:

1. Acceleration values in descending order
2. Acceleration value (sorted) after x ms is the required xms value.

During calculations in accordance with ECE R94, the rebound movement of the head is not included.

#### Determining Input Values

The measured values must be filtered in accordance with the stipulated filter classes.

#### ISO TS 13499 Code

The ISO code describes the input channels for the Xms as follows:

? ? ???? ?? ?? ?? AC ? ? : Acceleration

#### Relevant Laws and Regulations

- Directive 96/79/EG, Annex 2, 3.2.1.1
- ECE R94, Annex 3, 5.2.1
- ECE R94, Annex 4, 1.3
- ECE–R 80, Annex 4, 2.1
- ECE–R 44, 7.1.4.2.1
- ECE–R 44, 7.1.4.2.2
- ECE–R 12, 5.3
- ECE–R 17, 5.1.3.1
- ECE R94, Annex 6, 2
- FMVSS 208 (May 2000), S15.3.3
- FMVSS 208 (May 2000), S19.4.3
- FMVSS 208 (May 2000), S21.5.3
- FMVSS 208 (May 2000), S23.5.3
- SAE J1727, 5.3
- SAE J1727, 6.11
- ADR69/00, 5.3.2
- NHTSA 49 CFR 571[Docket No. 92-28; Notice8],[RIN No. 2127-AG07]; S5.1 (b)
- NHTSA 49 CFR 571,572,589[Docket No. 92-28; Notice7],[RIN No. 2127-AB85]; S5.1 (b)
- EURO NCAP, Front Impact, 10, 10.1
- EURO NCAP, Side Impact, 10, 10.1
- EURO NCAP, Pole Side Impact, 10, 10.1
- EURO NCAP, Assessment Protocol , 5
- Formula One Technical Regulation, 16.2

[IMAGE alt='image' src='image/crashkreis.gif'] 
 
 
Based on the Crash Analysis, Criteria Description of the Measured Data Processing Vehicle Safety Workgroup

<!--NI_TOPIC bundle=diadem path=crash/neck_criteria.html language=enus -->
## TOPIC 00065: Description of the Neck Criteria

- bundle_id: `diadem`
- source_path: `crash/neck_criteria.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/crash/neck_criteria.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Crash Analysis Criteria](../crash/crash_intro.html) > Description of the Neck Criteria

Description of the Neck Criteria

The following neck criteria for a frontal impact and a rear impact are described in the Crash Analysis Criteria:

**Front Impact:**

- MOC — Total Moment about Occipital condyle
- MTO — Total Moment (Lower Neck)
- [Time at level](../crash/neck_timeatlevel.html)
- [NIC (front impact ECE)](../crash/neck_nic_ece.html) — Neck Injury Criterion
- NIC (front impact EuroNCAP) — Neck Injury Criterion
- NIC (front impact FMVSS) — Neck Injury Criterion
- NIC (IIHS) — Neck Injury Criterion
- [Nij](../crash/neck_nij.html) — Normalized Neck Injury Criterion

**Rear Impact:**

- T1max (rear impact EuroNCAP) — Spine Injury Criterion
- [NIC (rear impact)](../crash/neck_nic_rear.html) — Neck Injury Criterion
- NIC (rear impact EuroNCAP) — Neck Injury Criterion
- Nkm — Neck Criterion rear impact
- LNL — Lower Neck Load Index

[Head Criteria](../crash/head_criteria.html) | Neck Criteria | [Chest Criteria](../crash/chest_criteria.html) | [Abdominal Criteria](../crash/abdomen_criteria.html) | [Further Crash Criteria](../crash/misc_criteria.html)

<!--NI_TOPIC bundle=diadem path=crash/neck_nic_ece.html language=enus -->
## TOPIC 00066: NIC (Front Impact ECE)

- bundle_id: `diadem`
- source_path: `crash/neck_nic_ece.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/crash/neck_nic_ece.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Crash Analysis Criteria](../crash/crash_intro.html) > [Neck Criteria](../crash/neck_criteria.html) > NIC (Front Impact ECE)

NIC (Front Impact ECE)

NIC is the abbreviation for Neck Injury Criterion.

#### Description

The criteria for neck injuries on the hybrid III 50% dummy are determined by the axial compression force, the axial tensile force, and the shearing forces at the transition from head to neck, expressed in kN, and the duration of these forces in ms. The following figure shows these forces.

[IMAGE alt='image' src='image/nic_ece.gif']

#### Mathematical Calculation

For all the above-mentioned signals, the continuous [Time at Level](../crash/neck_timeatlevel.html) is calculated and compared to the limit values.

#### Determining Input Values

The measurement values of the axial force F<sub>z</sub> and the side shear force F<sub>x</sub> are filtered according to [CFC 1000](../crash/misc_cfc.html).

#### ISO TS 13499 Code

The ISO code describes the input channels for the NIC (front impact ECE) as follows:

? ? NECK UP 00 ?? FO X A : (+)pos. Upper Neck Force X, CFC 1000

? ? NECK UP 00 ?? FO Z A : Upper Neck Force Z, CFC 1000

#### Relevant Laws and Regulations

- Directive 96/79/EG, Annex II, 3.2.1.2
- Directive 96/79/EG, Annex II, Appendix 2, 2
- ECE–R 94, 5.2.1.2
- ECE R94, Annex 4, 2
- SAE J1733

[IMAGE alt='image' src='image/crashkreis.gif'] 
 
 
Based on the Crash Analysis, Criteria Description of the Measured Data Processing Vehicle Safety Workgroup

<!--NI_TOPIC bundle=diadem path=crash/neck_nic_rear.html language=enus -->
## TOPIC 00067: NIC (rear impact)

- bundle_id: `diadem`
- source_path: `crash/neck_nic_rear.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/crash/neck_nic_rear.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Crash Analysis Criteria](../crash/crash_intro.html) > [Neck Criteria](../crash/neck_criteria.html) > NIC (rear impact)

NIC (rear impact)

NIC is the abbreviation for Neck Injury Criterion.

#### Description

The criterion for the neck injury with a rear impact is expressed by the relative acceleration between the upper and lower neck acceleration, in m/s², and the relative velocity, in m/s.

#### Mathematical Calculation

The NIC value (without dimensions) is calculated with the following formula:

[IMAGE alt='image' src='image/f_nic.gif']

with:

[IMAGE alt='image' src='image/f_nica.gif']

[IMAGE alt='image' src='image/f_nicv.gif']

| and | axT1 | Acceleration in X direction of the first thorax spine in [m/s2] |
| --- | --- | --- |
|  | axHead | Acceleration in x-direction measured at the height of the c.o.g. of the head [m/s2] |

#### Determining Input Values

The measurement values of the accelerations are filtered in accordance with [CFC 180](../crash/misc_cfc.html). The NIC<sub>max</sub> value specifies and documents the maximum value of the NIC within an interval of 150 ms after the start of the sled acceleration. If the head changes the direction of the relative movement at a time point within the 150 ms interval after contact with the head rest, this time point limits the NIC interval for determining the NIC <sub>max</sub> value.

|  | Note The result of the NIC calculation is a value without dimensions. |
| --- | --- |

#### ISO TS 13499 Code

The ISO code describes the input channels for the NIC (rear impact) as follows:

? ? HEAD 00 00 ?? AC X C : Head Acceleration X, CFC 180

? ? SPIN 01 00 ?? AC X C : Spine Acceleration X, CFC 180

#### Relevant Laws and Regulations

This injury criterion is in the research phase.

##### Publications:

- A SLED TESTS PROCEDURE PROPOSAL TO EVALUATE THE RISK OF NECK INJURY IN LOW SPEED REAR IMPACTS USING A NEW NECK INJURY CRITERION (NIC); Paper no. 98-S7-O-07; Ola Boström, Yngve Håland, Rikard Frediksson, Autoliv Research Sweden, Mats Y Svensoson Hugo Mellander, Chalmers University of Technology Sweden; 16 th ESV Conference; June 1-4, 1998 Windsor Canada
- EVALUATION OF THE APPLACABILITY OF THE NECK INJURY CRITERION (NIC) IN REAR END IMPACTS ON THE BASIS OF HUMAN SUBJECT TESTS; A.Eichberger, H. Steffan, B.Geigl, M.Svensson, O. Boström, P.E. Leinzinger, M.Darok; IRCOBI Conference – Göteborg, September 1998
- Proposal for the ISO/TC22N2071, ISO/TC22/SC10 (Collision Test Procedures): TEST PROCEDURE FOR THE EVALUATION OF THE INJURY RISK TO THE CERVICAL SPINE IN A LOW SPEED REAR END IMPACT; M. Muser, H. Zellmer, F. Walz, W. Hell, K. Langwieder, K. Steiner, H. Steffan; Rear end impact test procedure, working draft 5, 05/2001
- SAE J1727, 6.8

[IMAGE alt='image' src='image/crashkreis.gif'] 
 
 
Based on the Crash Analysis, Criteria Description of the Measured Data Processing Vehicle Safety Workgroup

<!--NI_TOPIC bundle=diadem path=crash/neck_timeatlevel.html language=enus -->
## TOPIC 00068: Time at level

- bundle_id: `diadem`
- source_path: `crash/neck_timeatlevel.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/crash/neck_timeatlevel.html
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Crash Analysis Criteria](../crash/crash_intro.html) > [Neck Criteria](../crash/neck_criteria.html) > Time at level

Time at level

Time-Dependent Loading Criteria

#### Description

The Time at Level describes the maximum time interval for which the measurement value of a signal has exceeded a specific lower threshold. The value is determined either from the continuous time interval (continuous calculation) or from the sum of all time intervals (cumulative calculation).

#### Mathematical Calculation

##### Continuous Calculation (SAE)

To determine the relationship between the measured value of the signal (for example the force) and its corresponding time-at-level, the time-related ”load criterion curve” is determined, as the following figure shows.

[IMAGE alt='image' src='image/timeatlevel.gif']

1. The threshold values are plotted on the ordinate, the times-at-level are plotted on the abscissa.
2. The maximum measured value and the time-at-level zero are assigned to the highest threshold value.
3. In a matrix with two columns and 101 rows, all the threshold values are stored in the first column, starting with the maximum value. All the threshold values in this column are equal to the preceding ones minus the quotient, which is the maximum value divided by 100. Zero is assigned to the threshold value of the first row.
4. The largest continuous time interval in which the threshold value is exceeded by the measurement signal is determined for every threshold value in the first column. Use linear interpolation to determine the time interval, round it to the nearest millisecond, and enter it in the second column.
5. Every line in this matrix describes a value pair (point) that consists of the threshold value and the time at level – the ”load criterion curve” – which are plotted in a coordinate system (criterion graph) and thus compared to the injury assessment boundary. Times at level are only used if they are less than 60 ms.
6. To compare the ”load criterion curve” to the injury assessment boundary, the ratio between the load criterion value and the injury assessment boundary value is determined for each value pair and multiplied by 100. The highest value is the ”injury assessment reference” value which is entered in the coordinate system.

##### Cumulative Calculation (EuroNCAP)

If the sampling rates are constant, the accumulated values can be calculated with the following algorithm:

1. Values in descending order
2. Value (sorted) after x ms is the y-value.

#### Determining Input Values

—

#### Relevant Laws and Regulations

- SAE J1727, 6.10
- EuroNCAP, Front Impact, 10.2.2

[IMAGE alt='image' src='image/crashkreis.gif'] 
 
 
Based on the Crash Analysis, Criteria Description of the Measured Data Processing Vehicle Safety Workgroup

<!--NI_TOPIC bundle=diadem path=dacconcepts/dac2_02.html language=dede -->
## TOPIC 00069: Messhardware einrichten

- bundle_id: `diadem`
- source_path: `dacconcepts/dac2_02.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/dede/dacconcepts/dac2_02.html
- source_language: `dede`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Messhardware einrichten und über Schnittstellen kommunizieren](../dacconcepts/dac2_01.html) > Messhardware einrichten

### Messhardware einrichten

Nachdem Sie ein Messgerät beispielsweise über USB angeschlossen haben, fordert das Betriebssystem Sie auf, den Treiber des Hardware-Herstellers zu installieren. Anschließend melden Sie den zugehörigen DIAdem-Treiber, der mit dem Hardware-Treiber kommuniziert, in DIAdem-DAC an. Dann können Sie die Funktionsgruppen von DIAdem-DAC mit den benötigten Treiberfunktionen konfigurieren.

#### Verwandte Themen

[Messhardware einrichten und über Schnittstellen kommunizieren](../dacconcepts/dac2_01.html) | [Über Schnittstellen kommunizieren](../dacconcepts/dac2_03.html)

<!--NI_TOPIC bundle=diadem path=dacconcepts/dac2_021.html language=dede -->
## TOPIC 00070: Hardware-Treiber installieren

- bundle_id: `diadem`
- source_path: `dacconcepts/dac2_021.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/dede/dacconcepts/dac2_021.html
- source_language: `dede`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Messhardware einrichten und über Schnittstellen kommunizieren](../dacconcepts/dac2_01.html) > [Messhardware einrichten](../dacconcepts/dac2_02.html) > Hardware-Treiber installieren

### Hardware-Treiber installieren

Hardware-Hersteller liefern mit der Hardware Treiberbibliotheken aus, die Sie zusätzlich zu DIAdem installieren müssen. Um Hardware von NI zu verwenden, installieren Sie die Treiberbibliothek NI-DAQmx mit dem Measurement & Automation Explorer (kurz NI MAX), in dem Sie die Geräte- und Kanalparameter der Hardware konfigurieren. Rufen Sie NI MAX über das Windows-Startmenü auf. In einer Baumansicht listet NI MAX die installierte Hard- und Software von NI auf. Doppelklicken Sie auf **Geräte und Schnittstellen**, um die installierten Erfassungskarten und angeschlossenen Messgeräte anzuzeigen. Wenn Sie einen Eintrag auswählen, zeigt NI MAX die Eigenschaften der Hardware an. Um die Hardware zu prüfen, klicken Sie auf **Selbsttest**. Um die Funktionen der Karte zu testen, klicken Sie auf **Testpanels**.

Um mit DIAdem auf Hardware von NI zugreifen zu können, richten Sie in NI MAX für alle benötigten Ein- und Ausgänge Kanäle ein. In DIAdem greifen Sie auf diese Kanäle über die in NI MAX vorgegebenen Kanalnamen zu. Um einen globalen NI-DAQmx-Kanal zu erstellen, rechtsklicken Sie in der Baumansicht auf **Datenumgebung** und wählen im Kontextmenü **Neu**. Wählen Sie **Globaler virtueller NI-DAQmx-Kanal**. Der Kanal-Assistent führt Sie durch die Konfiguration und bestimmt die Art der Messung und die Anschlussklemme. Wie in der folgenden Abbildung listet NI MAX alle virtuellen Kanäle im Zweig **Datenumgebung** der Baumansicht auf. Auf der Registerkarte **Kalibrierung** können Sie mit Hilfe eines Assistenten eine 2-Punktkalibrierung definieren. Um Daten in Echtzeit zu erfassen, sollten Sie die Skalierung der Messwerte nicht in NI MAX sondern in DIAdem durchführen.

[IMAGE alt='image' src='image/hardware_channel.png']

*Testen eines NI-DAQmx-Kanals im Measurement & Automation Explorer (NI MAX)*

#### Verwandte Themen

[DIAdem-Treiber konfigurieren](../dacconcepts/dac2_022.html) | [Messhardware einrichten](../dacconcepts/dac2_02.html)

<!--NI_TOPIC bundle=diadem path=dacconcepts/dac2_022.html language=dede -->
## TOPIC 00071: DIAdem-Treiber konfigurieren

- bundle_id: `diadem`
- source_path: `dacconcepts/dac2_022.html`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/dede/dacconcepts/dac2_022.html
- source_language: `dede`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Messhardware einrichten und über Schnittstellen kommunizieren](../dacconcepts/dac2_01.html) > [Messhardware einrichten](../dacconcepts/dac2_02.html) > DIAdem-Treiber konfigurieren

### DIAdem-Treiber konfigurieren

Der DIAdem-Treiber verbindet die Treiberbibliothek des Herstellers mit DIAdem-DAC. DIAdem-Treiber liegen in Form von DLLs (Dynamic Link Library) vor, die Sie über **Einstellungen»Erweiterungen»GPI-Erweiterungen** in DIAdem anmelden. Klicken Sie auf die Registerkarte **Standard-Erweiterungen**, um zu überprüfen, ob die für Ihre Hardware erforderliche DLL bereits in DIAdem angemeldet ist. Klicken Sie auf die Registerkarte **Anwender-Erweiterungen**, um eine zusätzliche DLL zu laden. Den DIAdem-Treiber erhalten Sie wie die Treiberbibliothek vom Hardware-Hersteller.

Die für die Kommunikation zwischen der Treiberbibliothek NI-DAQmx und DIAdem erforderliche DLL GfSNIDAQ.dll ist standardmäßig angemeldet, sodass Sie den zugehörigen Treiberblock bereits in den Treibereingängen und Treiberausgängen finden. Um die in NI MAX definierten Kanäle für die Erfassung zu nutzen, klicken Sie in der Funktionsgruppe **Treibereingänge** auf **NI-DAQmx-Treiber**. Öffnen Sie den Blockdialog mit einem Doppelklick, um die gewünschten Kanäle auszuwählen.

[IMAGE alt='image' src='image/hardware_nidaq.png']

*Verwenden von NI-DAQmx-Kanäle in DIAdem*

Anders als beim NI-DAQmx-Treiber müssen Sie nach der Anmeldung von DIAdem-Treibern, die nicht von NI sind, in DIAdem-DAC über **Einstellungen»Einzelwertverarbeitung»Treiber-Funktionsgruppen** festlegen, welche Funktionen diese Treiber zur Erfassung und Ausgabe anbieten. In diesen Einstellungen können Sie DIAdem-Treiber, Signaleingänge, Signalausgänge sowie Verarbeitungsfunktionen, die der Treiber auch auf der Messhardware durchführen kann, hinzufügen, entfernen und konfigurieren. Achten Sie beim Bearbeiten der Einstellungen darauf, dass Geräteparameter wie Basisadresse oder Eingangsspannungsbereich mit den Einstellungen der Messhardware übereinstimmen.

In der Regel erfolgt die Vergabe von Systemressourcen wie Basisadressen, IRQs oder DMA-Kanälen per Plug&Play. Das Betriebssystem sorgt unter Berücksichtigung bereits installierter Hardware für die einwandfreie Einbindung der neuen Hardware. Falls Sie die für die Hardware erforderlichen Systemressourcen manuell festlegen, achten Sie darauf, dass keine andere Applikation diese Ressourcen verwendet.

|  | Hinweis Auf installierte Hardware können Sie normalerweise mit unterschiedlichen Applikationen, wie DIAdem und LabVIEW, wechselweise aber nicht gleichzeitig zugreifen. Für Hardware von NI wird ein solcher Konflikt auf Treiberebene erkannt und als Fehler gemeldet. |
| --- | --- |

In den Funktionsgruppen **Treibereingänge**, **Treiberausgänge** und **Verarbeitung** zeigt DIAdem die konfigurierten Treiberfunktionen. Alle konfigurieren Treiberfunktionen speichert DIAdem in der Desktop-Datei.

Wenn Sie nachträglich die Voreinstellungen der Treiberblöcke in den Funktionsgruppen verändern, bleiben die Einstellungen der Treiberblöcke im Schaltplan unverändert. Die Einstellungen der in einem Schaltplan enthaltenen Treiberblöcke speichert DIAdem im Schaltplan. Wenn Sie eine andere Hardware einsetzen, können Sie die im Schaltplan enthaltenen Treiberblöcke durch die Treibereingänge und Treiberausgänge der neuen Hardware ersetzen. Dazu lassen Sie die Treiberblöcke der neuen Hardware mit Drag&Drop auf die zu ersetzenden Blöcke im Schaltplan fallen. DIAdem übernimmt die Einstellungen der bisherigen Blöcke soweit wie möglich in die neuen Blöcke.

#### Verwandte Themen

[Hardware-Treiber installieren](../dacconcepts/dac2_021.html) | [Messhardware einrichten](../dacconcepts/dac2_02.html)

<!--NI_TOPIC bundle=diadem path=dataplugin/examples/example_add1_da.htm language=enus -->
## TOPIC 00072: Additional Example 1b: Reading in an Unspecified Number of Channels

- bundle_id: `diadem`
- source_path: `dataplugin/examples/example_add1_da.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/examples/example_add1_da.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Examples](../examples/examples.htm) > Additional Example 1b: Reading in an Unspecified Number of Channels

Additional Example 1b: Reading in an Unspecified Number of Channels

The following example shows a DataPlugin for reading in the text files [DataPlugin_AdditionalEx1_1.aex1](../examples/examples_load.htm) and [DataPlugin_AdditionalEx1_2.aex1](../examples/examples_load.htm). The DataPlugin script file is located at [DataPlugin_AdditionalEx1b.vbs](../examples/examples_load.htm)

#### Data Format Description

These two text files contain metadata and channel data. The metadata includes the channel name and the channel unit. The channel names are in the first line of the file to be read in and the associated units are in the second line. The channel data follows:

The names, units, and data are separated by a tabulator. The specified numbers use a point as the decimal symbol. The empty rows in the file and the leading and trailing blanks are irrelevant. The end of the line is indicated by Carriage Return and Line Feed.

The [DataPlugin_AdditionalEx1_1.aex1](../examples/examples_load.htm) file contains specifications for 2 channels and the [DataPlugin_AdditionalEx1_2.aex1](../examples/examples_load.htm) file specifications for 3 channels.

#### Special Features of the DataPlugin

- Line feed: CrLf
- Separators: <Tab>
- Ignoring spaces and empty rows
- Using the Split function to read in the channel names and the channel units. You do not need to know the number of channels to be read in before.
- Using DirectAccess channels to read in channel data

[Copy script](javascript:void(0);)

```text
Option Explicit
Sub ReadStore(oFile)
  ' Set string formatter
  oFile.Formatter.LineFeeds        = vbCrLf
  oFile.Formatter.TrimCharacters   = " "
  oFile.Formatter.IgnoreEmptyLines = True
  oFile.Formatter.Delimiters       = vbTab
  oFile.Formatter.DecimalPoint     = "."

  ' Read channel header
  Dim saChannelName : saChannelName = Split(oFile.GetNextLine, vbTab)
  Dim saChannelUnit : saChannelUnit = Split(oFile.GetNextLine, vbTab)

  ' Create channel group object and set property
  Dim oChannelGroup : Set oChannelGroup = Root.ChannelGroups.Add(oFile.Info.FileName)

  ' Get object for block stored data  
  Dim oBlock : Set oBlock = oFile.GetStringBlock() 

  ' Import all other channels with fast access
  Dim iLoop : iLoop = 0
  Dim oChn, oElem

  For each oElem in saChannelName
    ' Create channel in string block (file)
    Set oChn = oBlock.Channels.Add(oElem, eR64)
    Call oChn.Properties.Add("Unit_String", saChannelUnit(iLoop))
    
    ' Add defined channel to DIAdem channel group
    Call oChannelGroup.Channels.AddDirectAccessChannel(oChn)
    iLoop = iLoop + 1
  Next
End Sub
```

#### DataPlugin Description

The DataPlugin first specifies the general format of the file through the File object. The DataPlugin uses the VBS constant vbCrLf as the word-wrap and ignores empty rows and spaces which are not within the text. The VBS constant vbTab separates single values. A point is the decimal symbol.

Then the DataPlugin reads in the descriptions of the channels. The first line of the file contains the names of the channels and the second line the corresponding units. The DataPlugin uses the Split function to check the read in data for the vbTab separator and stores the substrings in a one-dimensional, zero-based array. The number of arrays specifies the number of channels that the file contains.

Then the DataPlugin generates a new channel group whose name corresponds to the name of the file to be read in.

The DataPlugin transfers the other file contents into a StringBlock. If DirectAccess channels are associated with a StringBlock, the order of the values in a row determine which value belongs to which channel. The first value of the row belongs to the first channel, the second value of the row belongs to the second channel and so on. The value limits are specified by the Delimiter property, which in this case is vbTab.

The channel data is imported in a loop structure. The number of loops is specified by the size of the array which contains the channel names. Within the loop, the DataPlugin generates a new DirectAccess channel with the title that was previously read in and the associated unit. Because channels always belong to one channel group, the DataPlugin assigns the channels to the new channel group.

<!--NI_TOPIC bundle=diadem path=dataplugin/examples/example_add2.htm language=enus -->
## TOPIC 00073: Additional Example 2: Splitting Metadata

- bundle_id: `diadem`
- source_path: `dataplugin/examples/example_add2.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/examples/example_add2.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Examples](../examples/examples.htm) > Additional Example 2: Splitting Metadata

Additional Example 2: Splitting Metadata

The following example shows a DataPlugin for reading in the text file [DataPlugin_AdditionalEx2.aex2](../examples/examples_load.htm). The DataPlugin script file is located at [DataPlugin_AdditionalEx2.vbs](../examples/examples_load.htm)

#### Data Format Description

This text file contains metadata and channel data. The metadata includes a comment and the channel names and channel units. The first line of the file to be read in contains the comment. The second line contains an identifier, a name, and a unit for each channel. The unit is enclosed in angle brackets and is part of the channel name. The identifier and the channel name are separated by a colon as the diagram shows: Identifier1: Name1[Unit1], Identifier2: Name2[Unit2].

The channel data follows: The channel names and the channel data are separated by commas. The specified numbers use a point as the decimal symbol. The numbers do not have a thousand separator. Leading and trailing blanks are irrelevant. The end of the line is indicated by Carriage Return and Line Feed.

#### Special Features of the DataPlugin

- Line feed: CrLf
- Ignoring spaces
- Separators: Comma
- Decimal symbol: Point
- Reading in the comment and saving the comment in the group properties
- Using the Split function to read in the identifier and the channel name. You do not need to know the number of channels to be read in before.
- Extracting the channel unit, which is part of the channel name
- Using DirectAccess channels to read in channel data

[Copy script](javascript:void(0);)

```text
Option Explicit
Sub ReadStore(oFile)
  ' Set string formatter
  oFile.Formatter.LineFeeds        = vbCrLf
  oFile.Formatter.TrimCharacters   = " "
  oFile.Formatter.Delimiters       = ","
  oFile.Formatter.DecimalPoint     = "."
  oFile.Formatter.ThousandSeparator = ""

  ' Create channel group object and set property
  Dim oChannelGroup : Set oChannelGroup = Root.ChannelGroups.Add(oFile.Info.FileName)
  Dim sComment : sComment = oFile.GetNextLine
  Call oChannelGroup.Properties.Add("Input_File", sComment)

  ' Read channel header
  Dim saChnNameUnit : saChnNameUnit = Split(oFile.GetNextLine, ",")

  ' Get object for block stored data  
  Dim oBlock : Set oBlock = oFile.GetStringBlock() 

 ' Import all other channels with fast access
  Dim oChn, oElem, sName, sUnit

  For each oElem in saChnNameUnit
    ' Extract the channel unit, which is part of the channel name
    Call GetChnName(oElem, sName, sUnit)

    ' Create channel in string block (file)
    Set oChn = oBlock.Channels.Add(sName, eR64)
    Call oChn.Properties.Add("Unit_String", sUnit)
    
   ' Add defined channel to DIAdem channel group
    Call oChannelGroup.Channels.AddDirectAccessChannel(oChn)
  Next
End Sub
'-----------------------------------
Sub GetChnName(sNameUnit, sName, sUnit)
  'sNameUnit contains e.g. C1 (1A1): Time[s]
  sNameUnit = Trim(Mid(sNameUnit, InStr(sNameUnit, ":") + 1, len(sNameUnit)))

  If InStr(sNameUnit, "[") > 0 Then
    sName = Left(sNameUnit, InStr(sNameUnit, "[") - 1)
    sUnit = Mid(sNameUnit, InStr(sNameUnit, "[")+1, InStr(sNameUnit, "]") - InStr(sNameUnit, "[")-1)
  Else
    sName = sNameUnit
  End If
End Sub
```

#### DataPlugin Description

The DataPlugin first specifies the general format of the file through the File object. The DataPlugin uses the VBS constant vbCrLf as the word-wrap and ignores spaces which are not within the text. The comma separates single values. A point is the decimal symbol.

The DataPlugin then generates a new channel group whose name corresponds to the name of the file to be read in. The DataPlugin uses the GetNextLine function to read in the comment contained in the first line and saves the group property Input_File.

The second line contains an identifier, a name, and a unit for each channel. The unit is part of the channel name. A colon separates the identifier and the channel name. The DataPlugin reads in this data, uses the Split function to check the data for the colon delimiter, and stores the substrings in a one-dimensional, zero-based array. The number of arrays specifies the number of channels that the file contains.

The DataPlugin transfers the other file contents into a StringBlock. If DirectAccess channels are associated with a StringBlock, the order of the values in a row determine which value belongs to which channel. The first value of the row belongs to the first channel, the second value of the row belongs to the second channel and so on. The value limits are specified by the Delimiter property, which in this case is the colon.

The channel data is imported in a loop structure. The number of loops is specified by the size of the array which contains the channel names. Within the loop, the DataPlugin generates a new DirectAccess channel with the name that was previously read in and the associated unit. Because channels always belong to one channel group, the DataPlugin assigns the channels to the new channel group.

The channel unit is extracted from the channel name in the GetChnName procedure. This procedure receives the transfer parameter which contains the array with the identifiers and the channel names. In the first step, the procedure separates the identifier and the channel names. The identifier is irrelevant for reading in the data. In a further step, the procedure checks whether the channel name contains a unit. If this is the case, the unit is in angle brackets. The procedure returns the channel name and the channel unit in the transfer parameters sName and sUnit.

<!--NI_TOPIC bundle=diadem path=dataplugin/examples/example_add3.htm language=enus -->
## TOPIC 00074: Additional Example 3: Reading in Data from Different Files

- bundle_id: `diadem`
- source_path: `dataplugin/examples/example_add3.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/examples/example_add3.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Examples](../examples/examples.htm) > Additional Example 3: Reading in Data from Different Files

Additional Example 3: Reading in Data from Different Files

The following example shows a DataPlugin for reading in the text file [DataPlugin_AdditionalEx3.aex3](../examples/examples_load.htm) and the table calculation file [DataPlugin_AdditionalEx3.xls](../examples/examples_load.htm). The DataPlugin script file is located at [DataPlugin_AdditionalEx3.vbs](../examples/examples_load.htm)

#### Data Format Description

This text file contains metadata and channel data. The metadata consists of a number of group properties and a text row containing the name of the channels to be read in. When DIAdem saves the group properties, a row contains the name of a property and, separated by the equals sign, the value of this property.

Then the channel data follows: a date/time channel and a number of numeric channels. The settings in the text file are separated by a tabulator. The specified numbers use a point as the decimal symbol. The end of the line is indicated by Carriage Return and Line Feed.

The table calculation file with the same name contains a table which specifies the channel names and the channel units assigned to these names.

#### Special Features of the DataPlugin

- Line feed: CrLf
- Separators: <Tab>
- Decimal symbol: Point
- Reading in the table calculation file
- Using the Split function to determine the group property and its value
- Using DirectAccess channels to read in channel data

[Copy script](javascript:void(0);)

```text
Option Explicit 

Sub ReadStore(oFile) 
  ' Set string formatter
  oFile.Formatter.LineFeeds    = vbCrLf
  oFile.Formatter.Delimiters   = vbTab
  oFile.Formatter.DecimalPoint = "."
  oFile.Formatter.TimeFormat   = "DD/MM/YYYY hh:mm"
  
  Dim sExcelFileName, oExcelFile, saSignalUnits
  sExcelFileName = oFile.Info.Drive  & oFile.Info.Directory & oFile.Info.FileName & ".xlsx"
  Set oExcelFile = OpenSpreadsheet(sExcelFileName)
  Call ReadExcelFile(oExcelFile, saSignalUnits) ' Read in the units and the associated names

  ' Create channel group object and set property
  Dim oChannelGroup : Set oChannelGroup = Root.Channelgroups.Add(oFile.Info.FileName)

  Dim bHeaderEmpty, sCurrLine, saHDProperty
  bHeaderEmpty = False
  Do
    ' Read first line
    sCurrLine = oFile.GetNextLine
    If InStr(sCurrLine, "=") > 0 Then
      saHDProperty = Split(sCurrLine, "=")
      Call oChannelGroup.Properties.Add(Trim(saHDProperty(0)), Trim(saHDProperty(1)))
    Else
      bHeaderEmpty = True
    End If
  Loop Until bHeaderEmpty

  ' Read channel header
  Dim saChnName  : saChnName = Split(sCurrLine, vbTab)
  Dim saChnDim() : ReDim saChnDim(uBound(saChnName))
  Call GetChnDim(saChnName, saChnDim, saSignalUnits)
 
  ' Get object for block stored data  
  Dim oBlock : Set oBlock = oFile.GetStringBlock() 
  oBlock.Position = oFile.Position
  
  ' Import all other channels with fast access
  Dim iLoop, elem, oChn
  iLoop = 0
  Set oChn = oBlock.Channels.Add(saChnName(iLoop), eTime)
  ' Add defined channel to DIAdem channel group
  Call oChannelGroup.Channels.AddDirectAccessChannel(oChn)

  For iLoop = 1 to uBound(saChnName)
    ' Create channel in string block (file)
    Set oChn = oBlock.Channels.Add(saChnName(iLoop), eR64)
    If saChnName(iLoop) <> "-" Then
      Call oChn.Properties.Add("Unit_String", saChnDim(iLoop))
      ' Add defined channel to DIAdem channel group
      Call oChannelGroup.Channels.AddDirectAccessChannel(oChn)
    End If
  Next
End Sub
'----------------------------------------------------------------------------
Sub GetChnDim(saChnName, saChnDim, saSignalUnits)
  Dim iLoop, iPos, i, j
  
  For iLoop = 0 to uBound(saChnName)-1
    saChnName(iLoop) = Trim(saChnName(iLoop))
    saChnDim(iLoop) = ""
    
    If uCase(Left(saChnName(iLoop),2)) = "AI" Then
      saChnName(iLoop) = "-"               ' ignored
    Else
      If InStr(saChnName(iLoop), "(") Then ' Unit
        iPos = InStr(saChnName(iLoop), "(")
        saChnDim(iLoop) = Trim(Mid(saChnName(iLoop), iPos+1, InStr(saChnName(iLoop), ")")-iPos-1))
        saChnName(iLoop) = Mid(saChnName(iLoop), 1, iPos-1)
      Else
        If (InStr(saChnName(iLoop), "/") > 0) and not (uCase(saChnName(iLoop)) = "DATE/TIME" ) Then ' delete before / and behind
          iPos = InStr(saChnName(iLoop), "/")
          If Mid(saChnName(iLoop), iPos-1, 1) <> " " Then
            iPos = InStrRev(Trim(saChnName(iLoop)), " ")
          End If
          saChnName(iLoop) = Trim(Left(saChnName(iLoop), iPos-1))
        End If
        ' Search unit
        For i = 0 To uBound(saSignalUnits,2)   'oSheet.MaxPosition.Column
          For j = 1 To uBound(saSignalUnits,1) 'oSheet.MaxPosition.Row
            If (uCase(saChnName(iLoop)) = saSignalUnits(j,i)) or (saSignalUnits(j,i)<>"") and Instr(uCase(saChnName(iLoop)), saSignalUnits(j,i)) Then
              saChnDim(iLoop) = saSignalUnits(0,i)
              Exit For  
            End If  
          Next
        Next
      End If
    End If
  Next
End Sub

'----------------------------------------------------------------------------
Sub ReadExcelFile(oExcelFile, saSignalUnits)
  Dim oSheet : Set oSheet = oExcelFile.Sheets(1)
  Redim saSignalUnits(oSheet.MaxPosition.Row-2, oSheet.MaxPosition.Column-2) ' Ignore empty line or first column, zero-based array
  
  Dim i, j, sText
  For i = 2 To oSheet.MaxPosition.Column
    sText = oSheet.GetCellValue(1,i)
    saSignalUnits(0,i-2) = Trim(sText) ' Units

    For j = 3 To oSheet.MaxPosition.Row
      sText = oSheet.GetCellValue(j,i)
      If not IsNull(sText) Then
        saSignalUnits(j-2,i-2) = uCase(Trim(sText)) ' Signal names which have this unit
      End If  
    Next
  Next
End Sub
```

#### DataPlugin Description

The DataPlugin first specifies the general format of the file through the File object. The DataPlugin uses the VBS constant vbCrLf as the linefeed character. The VBS constant vbTab separates single values. A point is the decimal symbol.

The the DataPlugin uses the OpenSpreadSheet function to open the spreadsheet file with the same name and transfers the contents of this file with the ReadExcelFileprocedure to the two-dimensional array saSignalUnits.

The DataPlugin generates a new channel group whose name corresponds to the name of the file to be read in. Then the DataPlugin reads in the metadata line by line. The DataPlugin uses the Split function to check the metadata containing the group properties for the equals sign. The DataPlugin interprets the information in front of the equals sign as group property name and the information behind the equals sign as the value.

The DataPlugin uses the Split function to check the next line, which contains the channel names, for the vbTab separator and stores the substrings in a one-dimensional, zero-based array. The number of arrays specifies the number of channels that the file contains.

The GetChnDim procedure checks the read in channel names and, if they are valid, determines the associated channel unit using the saSignalUnits array. If the name of a channel is not valid, the DataPlugin marks this channel with the "-" unit.

The DataPlugin transfers the other file contents into a StringBlock. If DirectAccess channels are associated with a StringBlock, the order of the values in a row determine which value belongs to which channel. The first value of the row belongs to the first channel, the second value of the row belongs to the second channel and so on. The value limits are specified by the Delimiter property, which in this case is vbTab.

The channel data is imported in a loop structure. The number of loops is specified by the size of the array which contains the channel names. Within the loop, the DataPlugin checks the channel unit and, if it is valid, generates a new DirectAccess channel with the respective name and the associated unit. Because channels always belong to one channel group, the DataPlugin assigns the channels to the new channel group.

<!--NI_TOPIC bundle=diadem path=dataplugin/examples/example_add4.htm language=enus -->
## TOPIC 00075: Additional Example 4: Merging Date and Time Channels

- bundle_id: `diadem`
- source_path: `dataplugin/examples/example_add4.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/examples/example_add4.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Examples](../examples/examples.htm) > Additional Example 4: Merging Date and Time Channels

Additional Example 4: Merging Date and Time Channels

The following example shows a DataPlugin for reading in the text file [DataPlugin_AdditionalEx4.aex4](../examples/examples_load.htm). The DataPlugin script file is located at [DataPlugin_AdditionalEx4.vbs](../examples/examples_load.htm)

#### Data Format Description

The text file contains only channel data: one channel with date and time data and two numeric channels. The tilde character separates the channel data. A point is the decimal symbol for the specified numbers. The numbers do not have a thousand separator. Leading and trailing blanks are irrelevant. The end of the row is indicated by Carriage Return and Line Feed.

#### Special Features of the DataPlugin

- Line feed: CrLf
- Ignoring spaces
- Separators: Tilde
- Decimal symbol: Point
- Reading in channel data. The date and time information is stored together in one channel.
- Using DirectAccess channels to read in channel data

[Copy script](javascript:void(0);)

```text
Option Explicit
Sub ReadStore(oFile)
  ' Set string formatter
  oFile.Formatter.LineFeeds         = vbCrLf
  oFile.Formatter.TrimCharacters    = " "
  oFile.Formatter.Delimiters        = "~"
  oFile.Formatter.DecimalPoint      = "."
  oFile.Formatter.ThousandSeparator = ""


 ' Create channel group object
  Dim oChannelGroup : Set oChannelGroup = Root.ChannelGroups.Add(oFile.Info.FileName)


  ' Declaration for channel and add properties
  Dim oChn : Set oChn = oChannelGroup.Channels.Add("Time", eTime)

  ' Import the time channel with offset 2000 for year
  ' needs to be value by value because offset must be calculated
  Dim iLoop : iLoop = 1
  Dim oTime : Set oTime = CreateTime(2014,6,17,10,20,30,40,45,50)
  Dim sTemp
  Do While not oFile.Position = oFile.Size
    sTemp = Trim(oFile.GetNextStringValue(eString))
    sTemp = sTemp & " " & Trim(oFile.GetNextStringValue(eString))
    Call CreateDate(sTemp, oTime)    
    oChn.Values(iLoop) = oTime.VariantDate
    oFile.SkipLine
    iLoop = iLoop + 1
  Loop
  
  ' Jump back to begin
  oFile.Position = 1

  ' Get object for block stored data  
  Dim oBlock: Set oBlock = oFile.GetStringBlock() 

  ' This channel must be ignored for the channel group 
  Set oChn = oBlock.Channels.Add("Dummy1", eString)  
  Set oChn = oBlock.Channels.Add("Dummy2", eString)  

  ' Import all other channels with fast access
  Set oChn = oBlock.Channels.Add("Channel_1", eR64)  
  Call oChannelGroup.Channels.AddDirectAccessChannel(oChn)

  Set oChn = oBlock.Channels.Add("Channel_2", eR64)  
  Call oChannelGroup.Channels.AddDirectAccessChannel(oChn)
End Sub

'-----------------------------------
' Creates the date channel with the offset for year 2000
Sub CreateDate(sTxt, oReturnedDate)
Dim iY, iM, iD, iH, iMin, iSec

  iD   = CInt(Left(sTxt, 2))
  iM   = GetMonthNo(Mid(sTxt, 4, 3))
  iY   = CInt(Mid(sTxt, 8, 2))
  iH   = CInt(Mid(sTxt, 11, 2))
  iMin = CInt(Mid(sTxt, 14, 2))
  iSec = CInt(Mid(sTxt, 17, 2))
  Set oReturnedDate = CreateTime(2000 + iY, iM, iD, iH, iMin, iSec, 0, 0, 0)
End Sub

'-----------------------------------
' Creates month as number
Function GetMonthNo(sInput)
  Select Case UCase(sInput)
    Case "JAN" GetMonthNo = 1
    Case "FEB" GetMonthNo = 2
    Case "MAR" GetMonthNo = 3
    Case "APR" GetMonthNo = 4
    Case "MAY" GetMonthNo = 5
    Case "JUN" GetMonthNo = 6
    Case "JUL" GetMonthNo = 7
    Case "AUG" GetMonthNo = 8
    Case "SEP" GetMonthNo = 9
    Case "OCT" GetMonthNo = 10
    Case "NOV" GetMonthNo = 11
    Case "DEC" GetMonthNo = 12
    Case Else
      GetMonthNo = 0
  End Select
End Function
```

#### DataPlugin Description

The DataPlugin first specifies the general format of the file through the File object. The DataPlugin uses the VBS constant vbCrLf as the word-wrap and ignores spaces which are not within the text. The tilde character separates single values. A point is the decimal symbol.

The DataPlugin then creates a new channel group, whose name is the same as that of the file to be read in and also a new channel named Time.

The date and time data is imported in a loop structure. The While loop runs over all the lines of the text file and uses the GetNextStringValue function to read in the respective date value and time value. The DataPlugin connects the read in values, executes an offset correction, and saves the new value in the Time channel.

In the next step, the DataPlugin positions the file pointer at the beginning and transfers the entire file contents to the StringBlock. If DirectAccess channels are associated with a StringBlock, the order of the values in a row determine which value belongs to which channel. The first value of the row belongs to the first channel, the second value of the row belongs to the second channel and so on. The limits of the value are specified by the Delimiter property, which in this case is the tilde. The DataPlugin uses wildcards for the two channels within the StringBlock because the date and time information is already read in. The DataPlugin creates a new DirectAccess channel for the remaining channels and assigns these channels to the new channel group.

The CreateDate function defines the offset correction and the GetMonthNo function converts the name of the month into a numeric value.

<!--NI_TOPIC bundle=diadem path=dataplugin/examples/example_add5.htm language=enus -->
## TOPIC 00076: Additional Example 5: Using Processed Channels

- bundle_id: `diadem`
- source_path: `dataplugin/examples/example_add5.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/examples/example_add5.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Examples](../examples/examples.htm) > Additional Example 5: Using Processed Channels

Additional Example 5: Using Processed Channels

The following example shows a DataPlugin for reading in the text file [DataPlugin_AdditionalEx5.aex5](../examples/examples_load.htm). The DataPlugin script file is located at [DataPlugin_AdditionalEx5.vbs](../examples/examples_load.htm)

#### Data Format Description

This text file contains metadata and channel data. The metadata has three lines. The first line contains an identifier, the second line contains the channel names, and the third line contains the associated channel units.

Then the channel data follows: a date/time channel and a number of numeric channels. The settings in the text file are separated by a tabulator. The specified numbers use a point as the decimal symbol. The end of the line is indicated by Carriage Return and Line Feed. Any empty rows are irrelevant.

#### Special Features of the DataPlugin

- Line feed: CrLf
- Ignoring spaces
- Separators: <Tab>
- Checking file contents for a specific keyword
- Reading in channel data. The date and time information is stored together in one channel.
- Using a Processed Channel

[Copy script](javascript:void(0);)

```text
Option Explicit 
Sub ReadStore(oFile)
  oFile.Formatter.LineFeeds        = vbCrLf
  oFile.Formatter.IgnoreEmptyLines = True  
  oFile.Formatter.Delimiters       = vbTab
  oFile.Formatter.DecimalPoint     = "."
  oFile.Formatter.TimeFormat       = "DD/MM/YYYY hh:mm:ss"

  ' Check whether selected file is known
  Dim sCurrLine : sCurrLine = uCase(oFile.GetNextLine)
  If not (InStr(sCurrLine, "XYZ") > 0) Then Call RaiseError("Not a known file.")

  Dim oChnGroup : Set oChnGroup = Root.ChannelGroups.Add(oFile.Info.FileName)
  Call oChnGroup.Properties.Add("description", Replace(sCurrLine, vbTab, ""))

  ' Read all channel names
  Dim saChnName : saChnName = Split(oFile.GetNextLine, vbTab)

  ' Read all channel units
  Dim saChnUnit : saChnUnit = Split(oFile.GetNextLine, vbTab)

  ' Create a file accessor
   Dim oBlock: Set oBlock = oFile.GetStringBlock()

  ' Create dummy channels because of data time
  Dim oChnD : Set oChnD = oBlock.Channels.Add("Date", eTime)
  Dim oChnT : Set oChnT = oBlock.Channels.Add("Time", eTime)
  Dim oPChn : Set oPChn = oChnGroup.Channels.AddProcessedChannel("DataTime", eTime, eAddProcessor)
  Call oPChn.Channels.Add(oChnD)
  Call oPChn.Channels.Add(oChnT)

  Dim iLoop, oChn
  For iLoop = 2 to UBound(saChnName)
    Set oChn = oBlock.Channels.Add(saChnName(iLoop), eR64)
    If saChnUnit(iLoop) <> "?" Then
      oChn.Properties.Item("unit_string").Value = saChnUnit(iLoop)
    End If
    'Provide the data to USI
    Call oChnGroup.Channels.AddDirectAccessChannel(oChn)
  Next
End Sub
```

#### DataPlugin Description

The DataPlugin first specifies the general format of the file through the File object. The DataPlugin uses the VBS constant vbCrLf as the word-wrap and ignores spaces which are not within the text. The VBS constant vbTab separates single values. A point is the decimal symbol.

The DataPlugin uses the GetNextLine function to read in the first line of the text file and checks whether the line contains the keyword XYZ. If this is not the case, the DataPlugin cancels the loading process with an error message. Then the DataPlugin generates a new channel group whose name corresponds to the name of the file to be read in. The DataPlugin saves the contents of the first read in line as a short description in the channel group.

The second line contains the name for every channel and the third line contains the channel unit. The DataPlugin reads in this data, uses the Split function to check the data for the separator vbTab, and stores the substrings in a one-dimensional, zero-based array. The number of arrays specifies the number of channels that the file contains.

The DataPlugin transfers the remaining file contents into a StringBlock. A Processed channel, which combines the values of the date channel and the values of the time channel in one channel, imports the date and time data.

If DirectAccess channels are associated with a StringBlock, the order of the values in a row determine which value belongs to which channel. The first value of the row belongs to the first channel, the second value of the row belongs to the second channel and so on. The value limits are specified by the Delimiter property, which in this case is vbTab. As the date and time data is already read in, the DataPlugin only creates new DirectAccess channels for the remaining channels and assigns these channels to the new channel group.

<!--NI_TOPIC bundle=diadem path=dataplugin/examples/example_add6.htm language=enus -->
## TOPIC 00077: Additional Example 6: Reading in Data Saved Blockwise

- bundle_id: `diadem`
- source_path: `dataplugin/examples/example_add6.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/examples/example_add6.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Examples](../examples/examples.htm) > Additional Example 6: Reading in Data Saved Blockwise

Additional Example 6: Reading in Data Saved Blockwise

The following example shows a DataPlugin for reading in the text file [DataPlugin_AdditionalEx6.aex6](../examples/examples_load.htm). The DataPlugin script file is located at [DataPlugin_AdditionalEx6.vbs](../examples/examples_load.htm)

#### Data Format Description

This text file contains several blocks with metadata and channel data. The metadata comprises three comment lines that start with a slash and which contain information on the test. The first line contains the name of the author and the time of the test. The second line contains an identifier. The second line contains the name and unit for each channel. The unit is enclosed in angle brackets and is part of the channel name. The channel names are separated by semicolons.

Then the associated channel data follows. The data is separated by a tabulator. The specified numbers use a point as the decimal symbol. Line feed shows the end of the row. Any empty rows are irrelevant.

#### Special Features of the DataPlugin

- Line feed: Lf
- Ignoring spaces
- Separators: <Tab>
- Reading in metadata and channel data alternately
- Extracting the channel unit, which is part of the channel name
- Using DirectAccess channels to read in channel data

[Copy script](javascript:void(0);)

```text
Option Explicit 
Sub ReadStore(oFile) 
  ' Set string formatter
  oFile.Formatter.LineFeeds        = vbLF
  oFile.Formatter.Delimiters       = vbTab
  oFile.Formatter.IgnoreEmptyLines = True

  Dim sStr, iCount, aPBBegin(), iLines, aLines(), sGrpName(), sChnIdent()
  Dim sPName(), sPValue(), sChnN(), sChnU()
  Dim sChnName, sChnUnit, sChn, iLoop, iBegin, saChnNameUnit, oElem

  iCount = 0
  While (oFile.Position <> oFile.Size)
    sStr = oFile.GetNextLine()

    If (InStr(sStr, "/") > 0 ) Then
      ReDim Preserve aPBBegin(iCount), sGrpName(iCount), sChnIdent(iCount)
      ReDim Preserve sPName(iCount), sPValue(iCount)
      ReDim Preserve sChnN(iCount), sChnU(iCount)
      
      '--- Header line 1
      iBegin = InStr(sStr, ":")+1 
      sGrpName(iCount) = Mid(sStr, iBegin, InStr(sStr, ";")-iBegin) 'Name

      iBegin = InStr(iBegin, sStr, ":")+1
      sChnIdent(iCount) = Mid(sStr, iBegin) 'Ident
  
      '--- Header line 2
      sStr = oFile.GetNextLine()

      iBegin = InStr(sStr, " ")+1
      sPName(iCount) = Mid(sStr, iBegin, InStr(sStr, ":")-iBegin) 'Property

      iBegin = InStr(iBegin, sStr, ":")+1
      sPValue(iCount) = Mid(sStr, iBegin) 'Value

      '--- Header line 3      
      sStr = oFile.GetNextLine()

      sStr = Mid(sStr, InStr(sStr, " ")+1)
      saChnNameUnit = Split(sStr, ";")
      For each oElem in saChnNameUnit
        iBegin = InStr(oElem, "[")
        sChnN(iCount) = sChnN(iCount) & Mid(oElem, 1, iBegin-1) & ";"
        sChnU(iCount) = sChnU(iCount) & Mid(oElem, iBegin+1, InStr(oElem, "]")-(iBegin + 1)) & ";"
      Next
     
      aPBBegin(iCount) = oFile.Position
      iCount = iCount + 1
      ReDim Preserve aLines(iCount)
      iLines = 0
    Else
      iLines = iLines + 1
      aLines(iCount-1) = iLines
    End If
  Wend

  ' Import all channels with fast access
  iCount = 0
  Dim oBlock, oGrp, oChn
  For each oElem in aPBBegin
    Set oGrp = Root.Channelgroups.Add(sGrpName(iCount))
    oGrp.Properties.Item("Description").Value = sChnIdent(iCount)
    Call oGrp.Properties.Add(sPName(iCount),sPValue(iCount))

    oFile.Position = aPBBegin(iCount)

    Set oBlock = oFile.GetStringBlock()
    oBlock.BlockLength = aLines(iCount)
    
    sChnName = Split(sChnN(iCount), ";")
    sChnUnit = Split(sChnU(iCount), ";")
    For iLoop = 0 To uBound(sChnName)-1
      Set oChn = oBlock.Channels.Add(sChnName(iLoop), eR64)
      oChn.Properties.Item("unit_string").Value = sChnUnit(iLoop)
      Call oGrp.Channels.AddDirectAccessChannel(oChn)
    Next
    iCount = iCount + 1
  Next
End Sub
```

#### DataPlugin Description

The DataPlugin first specifies the general format of the file through the File object. The DataPlugin uses the VBS constant vbLf as the linefeed character and ignores empty rows. The VBS constant vbTab separates the channel values.

In the first step the DataPlugin reads in every row of the text file. If the DataPlugin recognizes comment lines, it analyses them. The DataPlugin interprets the first comment line as the name of the author and the time of test and uses this information as the name and description of a channel group. The DataPlugin interprets the identifier, which is in the second comment line, as the name and the value for a channel group property. The third line contains the name and the unit of the subsequent channels. The DataPlugin uses the Split function to extract the channel units from the channel names. The DataPlugin marks the position of the channels to be read in within the text file where the associated data is.

The DataPlugin saves the read in and analyzed data in one-dimensional, zero-based arrays. The number of array elements specifies the number of channel groups to be read in.

In the second step, the DataPlugin edits all elements of the arrays, generates a new channel group with the respective properties, and positions the pointer of the text file on the associated channel data.

The DataPlugin transfers the remaining file contents to a StringBlock for reading in the channel data. If DirectAccess channels are associated with a StringBlock, the order of the values in a row determine which value belongs to which channel. The first value of the row belongs to the first channel, the second value of the row belongs to the second channel and so on. The value limits are specified by the Delimiter property, which in this case is vbTab.

The DataPlugin uses a loop structure to import the channel data. The number of loops is specified by the size of the array which contains the channel names. Within the loop, the DataPlugin generates a new DirectAccess channel with the name that was previously read in and the associated unit. Because channels always belong to one channel group, the DataPlugin assigns the channels to the new channel group.

<!--NI_TOPIC bundle=diadem path=dataplugin/examples/example_add7.htm language=enus -->
## TOPIC 00078: Additional Example 7: Using Waveform Channels

- bundle_id: `diadem`
- source_path: `dataplugin/examples/example_add7.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/examples/example_add7.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Examples](../examples/examples.htm) > Additional Example 7: Using Waveform Channels

Additional Example 7: Using Waveform Channels

The following example shows a DataPlugin for reading in the text file [DataPlugin_AdditionalEx7.aex7](../examples/examples_load.htm). The DataPlugin script file is located at [DataPlugin_AdditionalEx7.vbs](../examples/examples_load.htm)

#### Data Format Description

This text file contains metadata and channel data. The metadata corresponds with a number of channel properties or group properties. When this information is saved, a row contains the name of a property in quotation marks and, separated by a semicolon, the value of this property.

Then the channel data follows: a date/time channel and a numeric channel. All channel data in the text file is separated by a semicolon. The specified numbers use a comma as the decimal symbol and E as the exponential sign. The end of the line is indicated by Carriage Return and Line Feed. Any empty rows are irrelevant.

#### Special Features of the DataPlugin

- Line feed: CrLf
- Separators: Semicolon
- Decimal symbol: Comma
- Exponential character: E
- Ignoring quotation marks and spaces
- Checking file contents for specific keywords
- Reading in the channel data which is stored in combination with a waveform channel
- Defining waveform channel properties

[Copy script](javascript:void(0);)

```text
Option Explicit 
Sub ReadStore(oFile) 
  ' Set string formatter
  oFile.Formatter.LineFeeds         = vbCrLf
  oFile.Formatter.Delimiters        = ";"
  oFile.Formatter.DecimalPoint      = ","
  oFile.Formatter.ThousandSeparator = ""
  oFile.Formatter.ExponentSeparator = "E"
  oFile.Formatter.TrimCharacters    = " """
  
  ' Create channel group object and set property
  Dim oChannelGroup : Set oChannelGroup = Root.ChannelGroups.Add(oFile.Info.FileName)

  Dim PropName, PropValue, iProp, ChnName
  Dim saPropName(13), saPropValue(13)  
  PropName  = oFile.GetNextStringValue(eString)
  PropValue = oFile.GetNextStringValue(eString)
  Call oFile.SkipLine()
  iProp = 0
  Do While PropName <> ""
    Select Case PropName
      Case "Title"           ChnName = PropValue
      Case "Date", "Time"    Call oChannelGroup.Properties.Add(PropName, PropValue)
      Case Else              saPropName(iProp)  = PropName 
                             saPropValue(iProp) = PropValue
                             iProp = iProp + 1
    End Select
    PropName  = oFile.GetNextStringValue(eString)
    PropValue = oFile.GetNextStringValue(eString)
    Call oFile.SkipLine()
  Loop 
 
  ' Get object for block stored data  
  Dim oBlock : Set oBlock = oFile.GetStringBlock() 
  
  ' Import first channels with fast access
  ' First read dummy then read Y channel as waveform
  Dim oChn
  Set oChn = oBlock.Channels.Add("Dummy", eR64)
  Set oChn = oBlock.Channels.Add(ChnName, eR64)
  
  ' Add properties
  Dim oFormatter : Set oFormatter = oFile.Formatter
  Dim iLoop
  For iLoop = 0 to iProp-1
    Select Case saPropName(iLoop)
      Case "X scale"       Call oChn.Properties.Add("wf_increment", oFormatter.ParseString(saPropValue(iLoop),eR64))
      Case "X at 0%"       Call oChn.Properties.Add("wf_start_offset", oFormatter.ParseString(saPropValue(iLoop),eR64))
      Case "X samples"     Call oChn.Properties.Add("wf_samples", oFormatter.ParseString(saPropValue(iLoop),eI32))
      Case "X unit"        Call oChn.Properties.Add("wf_xunit_string", saPropValue(iLoop))
      Case "X label"       Call oChn.Properties.Add("wf_xname", saPropValue(iLoop))
      Case Else            Call oChn.Properties.Add(saPropName(iLoop),saPropValue(iLoop))
    End Select
  Next
  ' Create wave form channel  
  Call oChn.Properties.Add("wf_time_pref", "relative")
  
  ' Add defined channel to DIAdem channel group
  Call oChannelGroup.Channels.AddDirectAccessChannel(oChn)
End Sub
```

#### DataPlugin Description

The DataPlugin first specifies the general format of the file through the File object. The DataPlugin uses the VBS constant vbCrLf as the linefeed character. The semicolon separates single values, the comma is the decimal symbol, and E is the exponential character. The DataPlugin ignores quotation marks and leading and trailing blanks.

The DataPlugin generates a new channel group whose name corresponds to the name of the file to be read in. Then the DataPlugin reads in the metadata rowwise and checks the data for certain keywords. The DataPlugin saves the information in two arrays: one array with the names of the properties and one array with the associated values.

The DataPlugin transfers the remaining file contents into a StringBlock. If DirectAccess channels are associated with a StringBlock, the order of the values in a row determine which value belongs to which channel. The first value of the row belongs to the first channel, the second value of the row belongs to the second channel and so on. The limits of the value are specified by the Delimiter property, which in this case is the semicolon. The DataPlugin ignores the data of the first channel and saves the data of the second channel in a waveform channel. In order to generate a waveform channel, the DataPlugin checks the array with the previously read properties for certain keywords and transfers the associated values to the required waveform properties. The DataPlugin specifies the other properties as custom properties of the waveform channel.

<!--NI_TOPIC bundle=diadem path=dataplugin/examples/examples.htm language=enus -->
## TOPIC 00079: Examples

- bundle_id: `diadem`
- source_path: `dataplugin/examples/examples.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/examples/examples.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > Examples

Examples

The following examples show you how to create DataPlugins for loading or registering your own file formats in the DIAdem Data Portal.

A DataPlugin is based on a VBScript that reads data from files and provides the data for DIAdem. To create a DataPlugin, you must be familiar with the file structure. Therefore, you need a detailed description of the data format before you can program the DataPlugin. When you have this information, you can select **Settings»Extensions»DataPlugins** in DIAdem NAVIGATOR or in DIAdem SCRIPT, to create a DataPlugin. You then program the associated script in a script editor you select, for example, in the Microsoft Script Editor (version 10 or later) from the Microsoft Development Environment (Version 7.0 or later).

|  | Note For programming you also can use the script editor integrated in DIAdem. However, you can no longer use the debugger features. When programming your DataPlugins, do not use any DIAdem commands. |
| --- | --- |

Example 1: [Reading in a Text File with Meta Information](../examples/example.1.htm)

This example shows you how to

- create a DataPlugin and use the DataPlugin in the DataFinder.
- provide information about the text file.
- read in text.
- create properties and assign values to the properties.
- generate channels with automatically calculated values.

Example 2: [Reading in an ASCII File with Meta Information and Channel Data](../examples/example.2.htm)

This example shows you how to

- use a StringBlock to read in text channels.
- provide information about formatting a time channel.
- display a message when an error occurs.

Example 3: [Reading in a Binary File with Four Channels](../examples/example.3.htm)

This example shows you how to

- read in binary channel values.
- create a channel group.
- create a channel.
- export the DataPlugin.

Example 4: [Reading in a Text File and Handling Errors](../examples/example.4.htm)

This example shows you how to

- read in a time channel.
- read in and edit single values.
- display error messages.
- process invalid values.

Example 5: [Reading in Data from an Excel File](../examples/example.5.htm)

This example shows you how to

- read in general information on the workbook.
- use a CellBlock to read in data of a worksheet.

Additional examples

Example 1a: [Reading in an Unspecified Number of Channels (Value by Value)](../examples/example_add1_vpv.htm)

Example 1b: [Reading in an Unspecified Number of Channels (DirectAccess Channels)](../examples/example_add1_da.htm)

Example 2: [Splitting up Meta Information](../examples/example_add2.htm)

Example 3: [Reading in Data from Different Files](../examples/example_add3.htm)

Example 4: [Merging Date and Time Channels](../examples/example_add4.htm)

Example 5: [Using Processed Channels](../examples/example_add5.htm)

Example 6: [Reading in Data Saved Blockwise](../examples/example_add6.htm)

Example 7: [Using Waveform Channels](../examples/example_add7.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_opendocument_idataplugin.htm language=enus -->
## TOPIC 00080: Method: OpenDocument for DataPlugin

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_opendocument_idataplugin.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_opendocument_idataplugin.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: OpenDocument for DataPlugin

Method: OpenDocument for DataPlugin

Returns an object which provides methods and properties for reading or editing the metadata of a document.

```text
Set oDocument = Object.OpenDocument(FileName, DocumentType)
```

| Object | DataPluginObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the filename of the document. |  |
| DocumentType | VariantSpecifies the file types of the document. 0eDocumentTypeAuto The file type is specified automatically from the filename extension 1eDocumentTypeXMP XMPfile (for example *.pdf; *.jpg; *.jpeg; *.png; *.tif; *.tiff) 2eDocumentTypeWord XML based Word file (for example *.docx; *.docm; *.dotx; *.dotm) 3eDocumentTypeExcel XML based Excel file (for example *.xlsx; *.xltm; *.xltx; *.xltm) 4eDocumentTypePowerPoint XML based PowerPoint file (for example *.pptx; *.pptm; *.potx; *.potm) |  |
| 0 | eDocumentTypeAuto | The file type is specified automatically from the filename extension |
| 1 | eDocumentTypeXMP | XMPfile (for example *.pdf; *.jpg; *.jpeg; *.png; *.tif; *.tiff) |
| 2 | eDocumentTypeWord | XML based Word file (for example *.docx; *.docm; *.dotx; *.dotm) |
| 3 | eDocumentTypeExcel | XML based Excel file (for example *.xlsx; *.xltm; *.xltx; *.xltm) |
| 4 | eDocumentTypePowerPoint | XML based PowerPoint file (for example *.pptx; *.pptm; *.potx; *.potm) |
| oDocument | Document <DataPlugin>Returned object |  |

The following example opens a PDF file:

[Copy script](javascript:void(0);)

```text
Dim oMyDocument
Set oMyDocument = OpenDocument("c:\test.pdf", eDocumentTypeAuto)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_openfile_idataplugin.htm language=enus -->
## TOPIC 00081: Method: OpenFile for DataPlugin

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_openfile_idataplugin.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_openfile_idataplugin.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: OpenFile for DataPlugin

Method: OpenFile for DataPlugin

Opens a file.

```text
Set oFile = Object.OpenFile(FileName)
```

| Object | DataPluginObject with this method |
| --- | --- |
| FileName | StringSpecifies the name of the file to be opened, including the folder and the filename extension. |
| oFile | FileReturned object |

The following example opens a file:

[Copy script](javascript:void(0);)

```text
Dim oMyFile : Set oMyFile = OpenFile("c:\test.txt")
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_openspreadsheet_idataplugin.htm language=enus -->
## TOPIC 00082: Method: OpenSpreadsheet for DataPlugin

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_openspreadsheet_idataplugin.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_openspreadsheet_idataplugin.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: OpenSpreadsheet for DataPlugin

Method: OpenSpreadsheet for DataPlugin

Uses a specified DataPlugin to open an Excel file. To create this DataPlugin use the file reader Only filename in the **Configure DataPlugin** dialog box.

The DataPlugin cannot access Excel files that are password protected.

```text
Set oWorkbook = Object.OpenSpreadsheet(FileName, [SpreadsheetType])
```

| Object | DataPluginObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the name of the Excel file to be saved with the filename extension and the path. |  |
| [SpreadsheetType] | Specifies the Excel file type.If you do not specify this parameter, DIAdem uses the filename extension to specify the Excel file type.Enumeration with the following selection terms: 1eXlsExcel file created with Excel 2003 or an earlier version. 2eXlsxExcel file created with Excel 2007 or Excel 2010. 3eOdsExcel file created with OpenOffice. 4eCsv Excel file created in the CSV format (Character Separated Values). |  |
| 1 | eXls | Excel file created with Excel 2003 or an earlier version. |
| 2 | eXlsx | Excel file created with Excel 2007 or Excel 2010. |
| 3 | eOds | Excel file created with OpenOffice. |
| 4 | eCsv | Excel file created in the CSV format (Character Separated Values). |
| oWorkbook | WorkbookReturned object |  |

The following example opens an Excel file and saves the author of the workbook as a root property:

[Copy script](javascript:void(0);)

```text
Sub ReadStore(File)
  Dim oExcelFile
  Set oExcelFile = OpenSpreadsheet("C:\ExcelExample.xls")
  Call Root.Properties.Add("Author",oExcelFile.WorkbookInfo.Author)
End Sub
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_openstore_idataplugin.htm language=enus -->
## TOPIC 00083: Method: OpenStore for DataPlugin

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_openstore_idataplugin.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_openstore_idataplugin.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: OpenStore for DataPlugin

Method: OpenStore for DataPlugin

Uses a specified DataPlugin to open a data store.

```text
Set oStore = Object.OpenStore(PluginParameter, Plugin, [ConfigFile])
```

| Object | DataPluginObject with this method |
| --- | --- |
| PluginParameter | StringSpecifies the name of a data file with the filename extension and the path. |
| Plugin | StringSpecifies the name of the DataPlugin that opens the data store. |
| [ConfigFile] | StringSpecifies the configuration file with the extension .stp, which contains the search path to be used. |
| oStore | StoreReturned object |

The following example opens a data store:

[Copy script](javascript:void(0);)

```text
Dim oMyStore
Set oMyStore = OpenStore("C:\Program Files\..\Demo.atf","ATFX")
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_store.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_overview.htm language=enus -->
## TOPIC 00084: Methods

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > Methods

Methods

Use methods to execute actions. For example, you can use a method to add a new element to a collection. Many methods return an object that contains the new element in the collection.

The subordinate topics contained in the tree on the contents tab of the Help describe all the methods of the script interface for DataPlugins.

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_remove_ibinarydirectaccesschannels.htm language=enus -->
## TOPIC 00085: Method: Remove for BinaryDirectAccessChannels

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_remove_ibinarydirectaccesschannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_remove_ibinarydirectaccesschannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: Remove for BinaryDirectAccessChannels

Method: Remove for BinaryDirectAccessChannels

Deletes one element from the BinaryDirectAccessChannels collection.

```text
Object.Remove(DAChnNameOrIndex)
```

| Object | BinaryDirectAccessChannelsObject with this method |
| --- | --- |
| DAChnNameOrIndex | VariantSpecifies the name or the index of the channel that is to be deleted. |

The following example deletes the MyChannel channel:

[Copy script](javascript:void(0);)

```text
Call oBlock.Channels.Remove("MyChannel")
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_remove_ichannelgroups.htm language=enus -->
## TOPIC 00086: Method: Remove for ChannelGroups <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_remove_ichannelgroups.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_remove_ichannelgroups.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: Remove for ChannelGroups <DataPlugin>

Method: Remove for ChannelGroups <DataPlugin>

Deletes one element from the ChannelGroups collection.

```text
Object.Remove(GrpNameOrIndex)
```

| Object | ChannelGroups <DataPlugin>Object with this method |
| --- | --- |
| GrpNameOrIndex | VariantSpecifies the name or the index of the channel group that is to be deleted. |

The following example deletes the MyChnGroup channel group:

[Copy script](javascript:void(0);)

```text
Call Root.ChannelGroups.Remove("MyChnGroup")
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_remove_ichannels.htm language=enus -->
## TOPIC 00087: Method: Remove for Channels <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_remove_ichannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_remove_ichannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: Remove for Channels <DataPlugin>

Method: Remove for Channels <DataPlugin>

Deletes one element from the Channels collection.

```text
Object.Remove(ChnNameorIndex)
```

| Object | Channels <DataPlugin>Object with this method |
| --- | --- |
| ChnNameorIndex | VariantSpecifies the name or the index of the channel that is to be deleted. |

The following example deletes the MyChannel channel from the first channel group:

[Copy script](javascript:void(0);)

```text
Call Root.ChannelGroups(1).Channels.Remove("MyChannel")
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_remove_ichannelstoprocess.htm language=enus -->
## TOPIC 00088: Method: Remove for ChannelsToProcess

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_remove_ichannelstoprocess.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_remove_ichannelstoprocess.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: Remove for ChannelsToProcess

Method: Remove for ChannelsToProcess

Deletes one element from the ChannelsToProcess collection.

```text
Object.Remove(iIndex)
```

| Object | ChannelsToProcessObject with this method |
| --- | --- |
| iIndex | LongIntegerSpecifies the index of the channel that is to be deleted. |

The following example deletes the second channel from the ChannelsToProcess collection:

[Copy script](javascript:void(0);)

```text
Call ProcessedChn.Channels.Remove(2)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_remove_iexceldachannels.htm language=enus -->
## TOPIC 00089: Method: Remove for DirectCellChannels

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_remove_iexceldachannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_remove_iexceldachannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: Remove for DirectCellChannels

Method: Remove for DirectCellChannels

Deletes one element from the DirectCellChannels collection.

```text
Object.Remove(DAChnNameOrIndex)
```

| Object | DirectCellChannelsObject with this method |
| --- | --- |
| DAChnNameOrIndex | VariantSpecifies the name or the index of the channel that is to be deleted. |

The following example deletes the MyChannel channel:

[Copy script](javascript:void(0);)

```text
Call oCellBlock.Channels.Remove("MyChannel")
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_remove_iusielements.htm language=enus -->
## TOPIC 00090: Method: Remove for Elements <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_remove_iusielements.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_remove_iusielements.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: Remove for Elements <DataPlugin>

Method: Remove for Elements <DataPlugin>

Deletes one element from the Elements collection.

```text
Object.Remove(iIndex)
```

| Object | Elements <DataPlugin>Object with this method |
| --- | --- |
| iIndex | LongIntegerSpecifies the index of the element that is to be deleted. |

The following example deletes the first element from the Elements selection list:

[Copy script](javascript:void(0);)

```text
Call StoreElements.Remove(1)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_store.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_removeall_iexceldachannels.htm language=enus -->
## TOPIC 00091: Method: RemoveAll for DirectCellChannels

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_removeall_iexceldachannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_removeall_iexceldachannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: RemoveAll for DirectCellChannels

Method: RemoveAll for DirectCellChannels

Deletes all elements from the DirectCellChannels collection.

```text
Object.RemoveAll
```

| Object | DirectCellChannelsObject with this method |
| --- | --- |

The following example deletes all channels:

[Copy script](javascript:void(0);)

```text
Call oCellBlock.Channels.RemoveAll
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_removeall_iusielements.htm language=enus -->
## TOPIC 00092: Method: RemoveAll for Elements <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_removeall_iusielements.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_removeall_iusielements.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: RemoveAll for Elements <DataPlugin>

Method: RemoveAll for Elements <DataPlugin>

Deletes all elements from the Elements collection.

```text
Object.RemoveAll
```

| Object | Elements <DataPlugin>Object with this method |
| --- | --- |

The following example deletes all elements:

[Copy script](javascript:void(0);)

```text
Call StoreElements.RemoveAll
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_store.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_skipline_imeasurementfileio.htm language=enus -->
## TOPIC 00093: Method: SkipLine for File

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_skipline_imeasurementfileio.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_skipline_imeasurementfileio.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: SkipLine for File

Method: SkipLine for File

Skips one line in the file.

```text
bSkipLine = Object.SkipLine
```

| Object | FileObject with this method |
| --- | --- |
| bSkipLine | BooleanThe value is TRUE if the method was successful.The value is FALSE when the end of the file is reached. |

The following example reads the following lines from a file.

[Copy script](javascript:void(0);)

```text
XAxis¶
¶
1.000.000; 2.000; 301¶
```

These lines contain the name and the generation parameters of an implicit channel. The example skips the empty line that separates the information. The example then generates a channel group that contains an implicit channel.

[Copy script](javascript:void(0);)

```text
File.Formatter.LineFeeds = vbNewLine
File.Formatter.Delimiters = ";"
File.Formatter.ThousandSeparator = "."
Dim ChannelName: ChannelName = File.GetNextStringValue(eString)
Call File.SkipLine()
Dim StartValue : StartValue  = File.GetNextStringValue(eI32)
Dim Increment  : Increment   = File.GetNextStringValue(eI32)
Dim ChannelSize: ChannelSize = File.GetNextStringValue(eI32)
Dim oMyGrp : Set oMyGrp = Root.ChannelGroups.Add("MyChannelGroup") 
Call oMyGrp.Channels.AddImplicitChannel(ChannelName, StartValue, Increment, ChannelSize, eI32)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_swap_ibinarydirectaccesschannels.htm language=enus -->
## TOPIC 00094: Method: Swap for BinaryDirectAccessChannels

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_swap_ibinarydirectaccesschannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_swap_ibinarydirectaccesschannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: Swap for BinaryDirectAccessChannels

Method: Swap for BinaryDirectAccessChannels

Moves a [DirectAccess](../objects/dataplugin_objects_idirectaccesschannel.htm) channel to a specific position.

```text
Object.Swap(Index1, Index2)
```

| Object | BinaryDirectAccessChannelsObject with this method |
| --- | --- |
| Index1 | LongIntegerSpecifies the position of the channel. |
| Index2 | LongIntegerSpecifies the new position of the channel. |

The following example shows how you interchange the positions of the channels YShift and XShift:

[Copy script](javascript:void(0);)

```text
Call oBlock.Channels.Swap(oBlock.Channels.Item("YShift").Index, oBlock.Channels.Item("XShift").Index)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_swap_idirectaccesschannels.htm language=enus -->
## TOPIC 00095: Method: Swap for DirectAccessChannels

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_swap_idirectaccesschannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_swap_idirectaccesschannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: Swap for DirectAccessChannels

Method: Swap for DirectAccessChannels

Moves an DirectAccess channel to a specific position.

```text
Object.Swap(Index1, Index2)
```

| Object | DirectAccessChannelsObject with this method |
| --- | --- |
| Index1 | LongIntegerSpecifies the position of the DirectAccess channel. |
| Index2 | LongIntegerSpecifies the position of the DirectAccess channel. |

The following example shows how you interchange the positions of the channels YShift and XShift:

[Copy script](javascript:void(0);)

```text
Call oBlock.Channels.Swap(oBlock.Channels.Item("YShift").Index, oBlock.Channels.Item("XShift").Index)
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/methods/dataplugin_method_swap_iexceldachannels.htm language=enus -->
## TOPIC 00096: Method: Swap for DirectCellChannels

- bundle_id: `diadem`
- source_path: `dataplugin/methods/dataplugin_method_swap_iexceldachannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/methods/dataplugin_method_swap_iexceldachannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Methods](../methods/dataplugin_method_overview.htm) > Method: Swap for DirectCellChannels

Method: Swap for DirectCellChannels

Moves an DirectAccess channel to a specific position.

```text
Object.Swap(DAChnIndex1, DAChnIndex2)
```

| Object | DirectCellChannelsObject with this method |
| --- | --- |
| DAChnIndex1 | LongIntegerSpecifies the position of the DirectAccess channel. |
| DAChnIndex2 | LongIntegerSpecifies the position of the DirectAccess channel. |

The following example shows how you interchange the positions of the channels YShift and XShift:

[Copy script](javascript:void(0);)

```text
Call oCellBlock.Channels.Swap(oCellBlock.Channels("YShift").Index, oCellBlock.Channels("XShift").Index)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_iabstractchannel.htm language=enus -->
## TOPIC 00097: Object: AbstractChannel

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_iabstractchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_iabstractchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Channels](../objects/dataplugin_objects_ichannels.htm) | [ChannelsToProcess](../objects/dataplugin_objects_ichannelstoprocess.htm)) > Object: AbstractChannel

Object: AbstractChannel

The AbstractChannel object provides the channel values and the associated properties. The AbstractChannel object corresponds with a [Channel](../objects/dataplugin_objects_ichannel.htm), a [DirectAccessChannel](../objects/dataplugin_objects_idirectaccesschannel.htm) or an [ImplicitChannel](../objects/dataplugin_objects_iimplicitchannel.htm).

The following example creates the Offset channel property if the third channel in the FirstChnGroup channel group is an implicit channel:

[Copy script](javascript:void(0);)

```text
Dim oMyChn
For Each oMyChn in Root.ChannelGroups(1).Channels
  If (oMyChn.IsKindOf(eNormal)) Then
    Call oMyChn.Properties.Add("DataType", oMyChn.DataType)
  End If
Next
```

#### Properties

[DataType](../properties/dataplugin_property_datatype_iabstractchannel.htm) | [Name](../properties/dataplugin_property_name_iabstractchannel.htm) | [Properties](../properties/dataplugin_property_properties_iabstractchannel.htm)

#### Methods

[IsKindOf](../methods/dataplugin_method_iskindof_iabstractchannel.htm)

#### Returned From

[Channels <DataPlugin>](../objects/dataplugin_objects_ichannels.htm).[Item](../methods/dataplugin_method_item_ichannels.htm) | [ChannelsToProcess](../objects/dataplugin_objects_ichannelstoprocess.htm).[Add](../methods/dataplugin_method_add_ichannelstoprocess.htm) | [ChannelsToProcess](../objects/dataplugin_objects_ichannelstoprocess.htm).[Item](../methods/dataplugin_method_item_ichannelstoprocess.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_iabstractchannelformatter.htm language=enus -->
## TOPIC 00098: Object: AbstractChannelFormatter

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_iabstractchannelformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_iabstractchannelformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([AbstractDirectAccessChannels](../objects/dataplugin_objects_iabstractdirectaccesschannels.htm) | [BinaryDirectAccessChannels](../objects/dataplugin_objects_ibinarydirectaccesschannels.htm) | [Channels](../objects/dataplugin_objects_ichannels.htm) | [ChannelsToProcess](../objects/dataplugin_objects_ichannelstoprocess.htm) | [DirectAccessChannels](../objects/dataplugin_objects_idirectaccesschannels.htm) | [DirectCellChannels](../objects/dataplugin_objects_iexceldachannels.htm)) > [DirectAccessChannel](../objects/dataplugin_objects_idirectaccesschannel.htm) > Object: AbstractChannelFormatter

Object: AbstractChannelFormatter

The AbstractChannelFormatter object contains information about how the values of a channel are represented in the file.

Depending on whether the channel belongs to a [BinaryBlock](../objects/dataplugin_objects_ibinaryblock.htm), [StringBlock](../objects/dataplugin_objects_istringblock.htm), [FixedWidthBlock](../objects/dataplugin_objects_ifixedwidthblock.htm), or [CellBlock](../objects/dataplugin_objects_icellblock.htm) the AbstractChannelFormatter is a [BinaryChannelFormatter](../objects/dataplugin_objects_ibinarychannelformatter.htm), [StringChannelFormatter](../objects/dataplugin_objects_istringchannelformatter.htm), [FixedWidthChannelFormatter](../objects/dataplugin_objects_ifixedwidthchannelformatter.htm), or [CellChannelFormatter](../objects/dataplugin_objects_icellchannelformatter.htm) object.

The following example checks to which block type each channel belongs and creates the channel property BlockType:

[Copy script](javascript:void(0);)

```text
Dim oMyChn
For Each oMyChn in oBlock.Channels
  If oMyChn.Formatter.IsKindOf(eStringBlock) Then
    Call oMyChn.Properties.Add("BlockType", "StringBlock")
  ElseIf oMyChn.Formatter.IsKindOf(eBinaryBlock) Then
    Call oMyChn.Properties.Add("BlockType", "BinaryBlock")
  ElseIf oMyChn.Formatter.IsKindOf(eFixedWidthBlock) Then
    Call oMyChn.Properties.Add("BlockType", "FixedWidthBlock")
  ElseIf oMyChn.Formatter.IsKindOf(eCellBlock) Then
    Call oMyChn.Properties.Add("BlockType", "CellBlock")
  End If
Next
```

#### Methods

[IsKindOf](../methods/dataplugin_method_iskindof_iabstractchannelformatter.htm)

#### Returned From

[DirectAccessChannel](../objects/dataplugin_objects_idirectaccesschannel.htm).[Formatter](../properties/dataplugin_property_formatter_idirectaccesschannel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_iabstractdirectaccesschannels.htm language=enus -->
## TOPIC 00099: Collection: AbstractDirectAccessChannels

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_iabstractdirectaccesschannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_iabstractdirectaccesschannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([BinaryBlock](../objects/dataplugin_objects_ibinaryblock.htm) | [Collections](../objects/dataplugin_objects_collections.htm) | [FixedWidthBlock](../objects/dataplugin_objects_ifixedwidthblock.htm) | [StringBlock](../objects/dataplugin_objects_istringblock.htm)) > Collection: AbstractDirectAccessChannels

Collection: AbstractDirectAccessChannels

The AbstractDirectAccessChannels collection corresponds to a [DirectAccessChannels](../objects/dataplugin_objects_idirectaccesschannels.htm) or a [BinaryDirectAccessChannels](../objects/dataplugin_objects_ibinarydirectaccesschannels.htm) collection.

#### Properties

[Count](../properties/dataplugin_property_count_iabstractdirectaccesschannels.htm)

#### Methods

[Item](../methods/dataplugin_method_item_iabstractdirectaccesschannels.htm) | [Remove](../methods/dataplugin_method_remove_iabstractdirectaccesschannels.htm) | [RemoveAll](../methods/dataplugin_method_removeall_iabstractdirectaccesschannels.htm) | [Swap](../methods/dataplugin_method_swap_iabstractdirectaccesschannels.htm)

#### Returned From

[BinaryBlock](../objects/dataplugin_objects_ibinaryblock.htm).[Channels](../properties/dataplugin_property_channels_ibinaryblock.htm) | [FixedWidthBlock](../objects/dataplugin_objects_ifixedwidthblock.htm).[Channels](../properties/dataplugin_property_channels_ifixedwidthblock.htm) | [StringBlock](../objects/dataplugin_objects_istringblock.htm).[Channels](../properties/dataplugin_property_channels_istringblock.htm)

#### Procedures

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_iautoremove.htm language=enus -->
## TOPIC 00100: Object: AutoRemove

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_iautoremove.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_iautoremove.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([General](../examples/general.htm) | [Objects](../objects/dataplugin_objects.htm)) > [DataPlugin](../objects/dataplugin_objects_idataplugin.htm) > Object: AutoRemove

Object: AutoRemove

The AutoRemove object offers support when working with ZIP archives. The methods allow you to unzip ZIP archives to a temporary folder and automatically delete the files in this folder.

Note that a ZIP archive contains exactly one measurement data file. The DataFinder indexes a ZIP file only once, like any other measurement data file. Addressing within the ZIP archive is not possible.

The following example creates a temporary folder and unzips the ZIP archive FileName in this folder. Then the example imports the data of the first file with the load method described in the ATFX DataPlugin:

[Copy script](javascript:void(0);)

```text
Sub ReadStore(FileName)
  Dim TempFolder
  TempFolder = AutoRemove.CreateFolder()

  Dim FileList
  FileList = Unzip(FileName, TempFolder)

  Call Root.ImportStore(TempFolder & FileList(0), "ATFX")
End Sub
```

#### Methods

[AddExisting](../methods/dataplugin_method_addexisting_iautoremove.htm) | [CreateFolder](../methods/dataplugin_method_createfolder_iautoremove.htm)

#### Returned From

[DataPlugin](../objects/dataplugin_objects_idataplugin.htm).[AutoRemove](../properties/dataplugin_property_autoremove_idataplugin.htm)

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_ibinaryblock.htm language=enus -->
## TOPIC 00101: Object: BinaryBlock

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_ibinaryblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_ibinaryblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([BinaryChannelFormatter](../objects/dataplugin_objects_ibinarychannelformatter.htm) | [File](../objects/dataplugin_objects_imeasurementfileio.htm)) > Object: BinaryBlock

Object: BinaryBlock

Use the BinaryBlock object to access channel data from a binary file.

A BinaryBlock can contain one or more DirectAccess channels. The channel values are organized columnwise in this block. The number of bytes in each column depends on the channel type. For example, if a block contains three channels with 32-bit integer values, the first four bytes are the first value of the first channel, the second four bytes are the first value of the second channel, and the third group of four bytes are the first value of the third channel. The fourth group of four bytes are the second value of the first channel, and so on.

You read the contents of a binary file as follows: 
- position the file pointer at the section to be read, 
- use the File.GetBinaryBlock method and assign the return value to a variable, 
- add a DirectAccess channel to the BinaryBlock for each channel to be read, 
- read the separate values from the channel or assign the entire DirectAccess channel to a channel group.

If you do not want to read all the channels, create DirectAccess channels for the channels you want, and use the BlockWidth property to adjust the block width. The block width is usually the sum of the single channel widths.

|  | Note The file pointer of the binary file does not move when a BinaryBlock is read. |
| --- | --- |

The following example reads a binary file that contains four channels with 32-bit integer values:

[Copy script](javascript:void(0);)

```text
Dim oBlock : Set oBlock = File.GetBinaryBlock()
Dim oChn1 : Set oChn1 = oBlock.Channels.Add("Channel1", eI32)
Dim oChn2 : Set oChn2 = oBlock.Channels.Add("Channel2", eI32)
Dim oChn3 : Set oChn3 = oBlock.Channels.Add("Channel3", eI32)
Dim oChn4 : Set oChn4 = oBlock.Channels.Add("Channel4", eI32)
```

#### Properties

[BlockLength](../properties/dataplugin_property_blocklength_ibinaryblock.htm) | [BlockWidth](../properties/dataplugin_property_blockwidth_ibinaryblock.htm) | [Channels](../properties/dataplugin_property_channels_ibinaryblock.htm) | [Position](../properties/dataplugin_property_position_ibinaryblock.htm)

#### Methods

[IsKindOf](../methods/dataplugin_method_iskindof_ibinaryblock.htm)

#### Returned From

[BinaryChannelFormatter](../objects/dataplugin_objects_ibinarychannelformatter.htm).[Block](../properties/dataplugin_property_block_ibinarychannelformatter.htm) | [File](../objects/dataplugin_objects_imeasurementfileio.htm).[GetBinaryBlock](../methods/dataplugin_method_getbinaryblock_imeasurementfileio.htm)

#### See Also

[File Object Overview](../objects/idataplugin_objects_overview_file.htm) | [Workbook Object Overview](../objects/idataplugin_objects_overview_excel.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_ibinarychannelformatter.htm language=enus -->
## TOPIC 00102: Object: BinaryChannelFormatter

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_ibinarychannelformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_ibinarychannelformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([AbstractDirectAccessChannels](../objects/dataplugin_objects_iabstractdirectaccesschannels.htm) | [BinaryDirectAccessChannels](../objects/dataplugin_objects_ibinarydirectaccesschannels.htm) | [Channels](../objects/dataplugin_objects_ichannels.htm) | [ChannelsToProcess](../objects/dataplugin_objects_ichannelstoprocess.htm) | [DirectAccessChannels](../objects/dataplugin_objects_idirectaccesschannels.htm) | [DirectCellChannels](../objects/dataplugin_objects_iexceldachannels.htm)) > [DirectAccessChannel](../objects/dataplugin_objects_idirectaccesschannel.htm) > Object: BinaryChannelFormatter

Object: BinaryChannelFormatter

The BinaryChannelFormatter object contains information about how the values of a channel are represented in the binary file.

The following example checks each channel whether this channel has a BinaryBlock and creates the channel property DataType:

[Copy script](javascript:void(0);)

```text
Dim oMyChn
For Each oMyChn in oBlock.Channels
  If (oMyChn.Formatter.IsKindOf(eBinaryBlock)) Then
    Call oMyChn.Properties.Add("DataType", oMyChn.Formatter.DataType)
  End If
Next
```

#### Properties

[BitMask](../properties/dataplugin_property_bitmask_ibinarychannelformatter.htm) | [Block](../properties/dataplugin_property_block_ibinarychannelformatter.htm) | [ByteOrder](../properties/dataplugin_property_byteorder_ibinarychannelformatter.htm) | [DataType](../properties/dataplugin_property_datatype_ibinarychannelformatter.htm)

#### Methods

[IsKindOf](../methods/dataplugin_method_iskindof_ibinarychannelformatter.htm)

#### See Also

[File Object Overview](../objects/idataplugin_objects_overview_file.htm) | [Workbook Object Overview](../objects/idataplugin_objects_overview_excel.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_ibinarydirectaccesschannels.htm language=enus -->
## TOPIC 00103: Collection: BinaryDirectAccessChannels

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_ibinarydirectaccesschannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_ibinarydirectaccesschannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([BinaryBlock](../objects/dataplugin_objects_ibinaryblock.htm) | [Collections](../objects/dataplugin_objects_collections.htm) | [FixedWidthBlock](../objects/dataplugin_objects_ifixedwidthblock.htm) | [StringBlock](../objects/dataplugin_objects_istringblock.htm)) > Collection: BinaryDirectAccessChannels

Collection: BinaryDirectAccessChannels

Collection of all [DirectAccess](../objects/dataplugin_objects_idirectaccesschannel.htm) channels. You can use the BinaryDirectAccessChannels collection to delete or to add DirectAccess channels.

The following example reads out a binary file which contains two channels. The channel data is in blocks. A block is structured in a way that the first three values belong to the first channel and the fourth value belongs to the second channel. The example then generates a channel group and binds the two channels.

[Copy script](javascript:void(0);)

```text
Dim oBlock : Set oBlock = File.GetBinaryBlock()
Dim oChn1  : Set oChn1 = oBlock.Channels.Add("Channel1", eI32, 3)
Dim oChn2  : Set oChn2 = oBlock.Channels.Add("Channel2", eI32, 1)
Dim oMyGrp : Set oMyGrp = Root.ChannelGroups.Add("MyChannelGroup")
Call oMyGrp.Channels.AddDirectAccessChannel(oChn1)
Call oMyGrp.Channels.AddDirectAccessChannel(oChn2)
```

#### Properties

[Count](../properties/dataplugin_property_count_ibinarydirectaccesschannels.htm)

#### Methods

[Add](../methods/dataplugin_method_add_ibinarydirectaccesschannels.htm) | [Item](../methods/dataplugin_method_item_ibinarydirectaccesschannels.htm) | [Remove](../methods/dataplugin_method_remove_ibinarydirectaccesschannels.htm) | [RemoveAll](../methods/dataplugin_method_removeall_ibinarydirectaccesschannels.htm) | [Swap](../methods/dataplugin_method_swap_ibinarydirectaccesschannels.htm)

#### Returned From

[BinaryBlock](../objects/dataplugin_objects_ibinaryblock.htm).[Channels](../properties/dataplugin_property_channels_ibinaryblock.htm) | [FixedWidthBlock](../objects/dataplugin_objects_ifixedwidthblock.htm).[Channels](../properties/dataplugin_property_channels_ifixedwidthblock.htm) | [StringBlock](../objects/dataplugin_objects_istringblock.htm).[Channels](../properties/dataplugin_property_channels_istringblock.htm)

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_idataplugin.htm language=enus -->
## TOPIC 00104: Object: DataPlugin

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_idataplugin.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_idataplugin.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([General](../examples/general.htm) | [Objects](../objects/dataplugin_objects.htm)) > Object: DataPlugin

Object: DataPlugin

The DataPlugin object is available as a global object. Therefore, all the properties and methods of the object are available at all points in the script.

The following example generates the DateTime Root property and assigns the time value 17.06.2004 10:00:00 to the Root property.

[Copy script](javascript:void(0);)

```text
Call Root.Properties.Add("DateTime",CreateTime(2004,6,17,10,0,0))
```

#### Properties

[AutoRemove](../properties/dataplugin_property_autoremove_idataplugin.htm) | [CurrentScriptName](../properties/dataplugin_property_currentscriptname_idataplugin.htm) | [CurrentScriptPath](../properties/dataplugin_property_currentscriptpath_idataplugin.htm) | [Root](../properties/dataplugin_property_root_idataplugin.htm)

#### Methods

[CreateJsonParser](../methods/dataplugin_method_createjsonparser_idataplugin.htm) | [CreateTime](../methods/dataplugin_method_createtime_idataplugin.htm) | [DBM](../methods/dataplugin_method_dbm_idataplugin.htm) | [OpenDocument](../methods/dataplugin_method_opendocument_idataplugin.htm) | [OpenFile](../methods/dataplugin_method_openfile_idataplugin.htm) | [OpenSpreadsheet](../methods/dataplugin_method_openspreadsheet_idataplugin.htm) | [OpenStore](../methods/dataplugin_method_openstore_idataplugin.htm) | [RaiseError](../methods/dataplugin_method_raiseerror_idataplugin.htm) | [Unzip](../methods/dataplugin_method_unzip_idataplugin.htm)

#### See Also

[Root Object Overview](../objects/idataplugin_objects_overview.htm) | [File Object Overview](../objects/idataplugin_objects_overview_file.htm) | [Store Object Overview](../objects/idataplugin_objects_overview_store.htm) | [Workbook Object Overview](../objects/idataplugin_objects_overview_excel.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_idirectaccesschannel.htm language=enus -->
## TOPIC 00105: Object: DirectAccessChannel

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_idirectaccesschannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_idirectaccesschannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([AbstractDirectAccessChannels](../objects/dataplugin_objects_iabstractdirectaccesschannels.htm) | [BinaryDirectAccessChannels](../objects/dataplugin_objects_ibinarydirectaccesschannels.htm) | [Channels](../objects/dataplugin_objects_ichannels.htm) | [ChannelsToProcess](../objects/dataplugin_objects_ichannelstoprocess.htm) | [DirectAccessChannels](../objects/dataplugin_objects_idirectaccesschannels.htm) | [DirectCellChannels](../objects/dataplugin_objects_iexceldachannels.htm)) > Object: DirectAccessChannel

Object: DirectAccessChannel

The DirectAccessChannel object provides access to a DirectAccess channel and the associated properties.

The following example creates a new channel group with a DirectAccess channel. When the channel values are read, each value is first multiplied by the factor 2, and then the offset 5 is added.

[Copy script](javascript:void(0);)

```text
Dim oBlock: Set oBlock = File.GetBinaryBlock()
Dim oChn  : Set oChn   = oBlock.Channels.Add("MyChannel",eI32)
Dim oMyGrp: Set oMyGrp = Root.ChannelGroups.Add("MyChannelGroup") 
Dim oMyChn: Set oMyChn = oMyGrp.Channels.AddDirectAccessChannel(oChn)
oMyChn.Factor = 2
oMyChn.Offset = 5
```

The following example reads in the values of the worksheet columnwise from the second row of the first column and saves the values in channels of the first channel group:

[Copy script](javascript:void(0);)

```text
Dim oCurrSheet: Set oCurrSheet = Workbook.Sheets(1)
Dim oCellBlock: Set oCellBlock = oCurrSheet.GetCellBlock(2,1)

Dim i, Name, oNewChannel
For i = 1 to oCurrSheet.MaxPosition.Column
  Name = oCurrSheet.GetCellValue(1,i)
  Set oNewChannel = oCellBlock.Channels.Add(Name) 
  Call Root.ChannelGroups(1).Channels.AddDirectAccessChannel(oNewChannel)
Next
```

#### Properties

[DataType](../properties/dataplugin_property_datatype_idirectaccesschannel.htm) | [Factor](../properties/dataplugin_property_factor_idirectaccesschannel.htm) | [Formatter](../properties/dataplugin_property_formatter_idirectaccesschannel.htm) | [Index](../properties/dataplugin_property_index_idirectaccesschannel.htm) | [Name](../properties/dataplugin_property_name_idirectaccesschannel.htm) | [Offset](../properties/dataplugin_property_offset_idirectaccesschannel.htm) | [Properties](../properties/dataplugin_property_properties_idirectaccesschannel.htm) | [Size](../properties/dataplugin_property_size_idirectaccesschannel.htm) | [Values](../properties/dataplugin_property_values_idirectaccesschannel.htm)

#### Methods

[AddCharacteristics](../methods/dataplugin_method_addcharacteristics_idirectaccesschannel.htm) | [AddWaveformProperties](../methods/dataplugin_method_addwaveformproperties_idirectaccesschannel.htm) | [IsKindOf](../methods/dataplugin_method_iskindof_idirectaccesschannel.htm)

#### Returned From

[AbstractDirectAccessChannels](../objects/dataplugin_objects_iabstractdirectaccesschannels.htm).[Item](../methods/dataplugin_method_item_iabstractdirectaccesschannels.htm) | [BinaryDirectAccessChannels](../objects/dataplugin_objects_ibinarydirectaccesschannels.htm).[Add](../methods/dataplugin_method_add_ibinarydirectaccesschannels.htm) | [BinaryDirectAccessChannels](../objects/dataplugin_objects_ibinarydirectaccesschannels.htm).[Item](../methods/dataplugin_method_item_ibinarydirectaccesschannels.htm) | [Channels <DataPlugin>](../objects/dataplugin_objects_ichannels.htm).[AddDirectAccessChannel](../methods/dataplugin_method_adddirectaccesschannel_ichannels.htm) | [Channels <DataPlugin>](../objects/dataplugin_objects_ichannels.htm).[Item](../methods/dataplugin_method_item_ichannels.htm) | [ChannelsToProcess](../objects/dataplugin_objects_ichannelstoprocess.htm).[Add](../methods/dataplugin_method_add_ichannelstoprocess.htm) | [ChannelsToProcess](../objects/dataplugin_objects_ichannelstoprocess.htm).[Item](../methods/dataplugin_method_item_ichannelstoprocess.htm) | [DirectAccessChannels](../objects/dataplugin_objects_idirectaccesschannels.htm).[Add](../methods/dataplugin_method_add_idirectaccesschannels.htm) | [DirectAccessChannels](../objects/dataplugin_objects_idirectaccesschannels.htm).[Item](../methods/dataplugin_method_item_idirectaccesschannels.htm) | [DirectCellChannels](../objects/dataplugin_objects_iexceldachannels.htm).[Add](../methods/dataplugin_method_add_iexceldachannels.htm) | [DirectCellChannels](../objects/dataplugin_objects_iexceldachannels.htm).[Item](../methods/dataplugin_method_item_iexceldachannels.htm)

#### See Also

[Root Object Overview](../objects/idataplugin_objects_overview.htm) | [File Object Overview](../objects/idataplugin_objects_overview_file.htm) | [Workbook Object Overview](../objects/idataplugin_objects_overview_excel.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_idirectaccesschannels.htm language=enus -->
## TOPIC 00106: Collection: DirectAccessChannels

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_idirectaccesschannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_idirectaccesschannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([BinaryBlock](../objects/dataplugin_objects_ibinaryblock.htm) | [Collections](../objects/dataplugin_objects_collections.htm) | [FixedWidthBlock](../objects/dataplugin_objects_ifixedwidthblock.htm) | [StringBlock](../objects/dataplugin_objects_istringblock.htm)) > Collection: DirectAccessChannels

Collection: DirectAccessChannels

Collection of all [DirectAccess](../objects/dataplugin_objects_idirectaccesschannel.htm) channels. You can use the DirectAccessChannels collection to delete or to add DirectAccess channels.

The following example reads a text file that contains one time channel and one real channel. The example then generates a channel group and binds the two channels.

[Copy script](javascript:void(0);)

```text
Dim oBlock : Set oBlock = File.GetStringBlock()
Dim oChn1  : Set oChn1 = oBlock.Channels.Add("Time", eTime)
Dim oChn2  : Set oChn2 = oBlock.Channels.Add("YShift", eR64)
Dim oMyGrp : Set oMyGrp = Root.ChannelGroups.Add("MyChannelGroup")
Call oMyGrp.Channels.AddDirectAccessChannel(oChn1)
Call oMyGrp.Channels.AddDirectAccessChannel(oChn2)
```

#### Properties

[Count](../properties/dataplugin_property_count_idirectaccesschannels.htm)

#### Methods

[Add](../methods/dataplugin_method_add_idirectaccesschannels.htm) | [Item](../methods/dataplugin_method_item_idirectaccesschannels.htm) | [Remove](../methods/dataplugin_method_remove_idirectaccesschannels.htm) | [RemoveAll](../methods/dataplugin_method_removeall_idirectaccesschannels.htm) | [Swap](../methods/dataplugin_method_swap_idirectaccesschannels.htm)

#### See Also

[File Object Overview](../objects/idataplugin_objects_overview_file.htm) | [Store Object Overview](../objects/idataplugin_objects_overview_store.htm) | [Workbook Object Overview](../objects/idataplugin_objects_overview_excel.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_idocumentnamespaces.htm language=enus -->
## TOPIC 00107: Collection: DocumentNamespaces <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_idocumentnamespaces.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_idocumentnamespaces.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Collections](../objects/dataplugin_objects_collections.htm) | [Document](../objects/dataplugin_objects_idocumentroot.htm)) > Collection: DocumentNamespaces <DataPlugin>

Collection: DocumentNamespaces <DataPlugin>

Collection of name spaces in a document. Use namespaces to group XML elements in a document.

The following example transfers all meta properties of a document's namespaces into the data set properties:

[Copy script](javascript:void(0);)

```text
Dim oMyNameSpace,oMyProperty
For each oMyNameSpace in Document.Namespaces
  For each oMyProperty in oMyNameSpace.Properties
    Call Root.Properties.Add(oMyProperty.Name, oMyProperty.Value)
  Next
Next
```

#### Properties

[Count](../properties/dataplugin_property_count_idocumentnamespaces.htm)

#### Methods

[Exists](../methods/dataplugin_method_exists_idocumentnamespaces.htm) | [Item](../methods/dataplugin_method_item_idocumentnamespaces.htm)

#### Returned From

[Document <DataPlugin>](../objects/dataplugin_objects_idocumentroot.htm).[Namespaces](../properties/dataplugin_property_namespaces_idocumentroot.htm)

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_documents.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_iexcelsheets.htm language=enus -->
## TOPIC 00108: Collection: Sheets

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_iexcelsheets.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_iexcelsheets.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Collections](../objects/dataplugin_objects_collections.htm) | [Workbook](../objects/dataplugin_objects_iexcelfileio.htm)) > Collection: Sheets

Collection: Sheets

Collection of all [Worksheets](../objects/dataplugin_objects_iexcelsheet.htm). Use the sheets collection to access individual worksheets of the open work folder.

The following example generates a new channel group which has the name of the first worksheet:

[Copy script](javascript:void(0);)

```text
Dim oCurrSheet
Set oCurrSheet = Workbook.Sheets.Item(1)
Call Root.ChannelGroups.Add(oCurrSheet.Name)
```

#### Properties

[Count](../properties/dataplugin_property_count_iexcelsheets.htm)

#### Methods

[Exists](../methods/dataplugin_method_exists_iexcelsheets.htm) | [Item](../methods/dataplugin_method_item_iexcelsheets.htm)

#### Returned From

[Workbook](../objects/dataplugin_objects_iexcelfileio.htm).[Sheets](../properties/dataplugin_property_sheets_iexcelfileio.htm)

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_ifileinfo.htm language=enus -->
## TOPIC 00109: Object: Info

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_ifileinfo.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_ifileinfo.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([File](../objects/dataplugin_objects_imeasurementfileio.htm) | [Store](../objects/dataplugin_objects_iusisimplifiedstore.htm) | [Workbook](../objects/dataplugin_objects_iexcelfileio.htm)) > Object: Info

Object: Info

The Info object contains information about the file that the DataPlugin is currently processing.

The following examples save the name of the edited file as a root property:

[Copy script](javascript:void(0);)

```text
Call Root.Properties.Add("File name", File.Info.FileName)
```

[Copy script](javascript:void(0);)

```text
Call Root.Properties.Add("File name", FromStore.FileInfo.FileName)
```

[Copy script](javascript:void(0);)

```text
Call Root.Properties.Add("File name", Workbook.FileInfo.FileName)
```

#### Properties

[Directory](../properties/dataplugin_property_directory_ifileinfo.htm) | [Drive](../properties/dataplugin_property_drive_ifileinfo.htm) | [Extension](../properties/dataplugin_property_extension_ifileinfo.htm) | [FileName](../properties/dataplugin_property_filename_ifileinfo.htm) | [FullPath](../properties/dataplugin_property_fullpath_ifileinfo.htm)

#### Returned From

[File](../objects/dataplugin_objects_imeasurementfileio.htm).[Info](../properties/dataplugin_property_info_imeasurementfileio.htm) | [Store](../objects/dataplugin_objects_iusisimplifiedstore.htm).[FileInfo](../properties/dataplugin_property_fileinfo_iusisimplifiedstore.htm) | [Workbook](../objects/dataplugin_objects_iexcelfileio.htm).[FileInfo](../properties/dataplugin_property_fileinfo_iexcelfileio.htm)

#### See Also

[File Object Overview](../objects/idataplugin_objects_overview_file.htm) | [Store Object Overview](../objects/idataplugin_objects_overview_store.htm) | [Workbook Object Overview](../objects/idataplugin_objects_overview_excel.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_ifixedwidthblock.htm language=enus -->
## TOPIC 00110: Object: FixedWidthBlock

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_ifixedwidthblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_ifixedwidthblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([File](../objects/dataplugin_objects_imeasurementfileio.htm) | [FixedWidthChannelFormatter](../objects/dataplugin_objects_ifixedwidthchannelformatter.htm)) > Object: FixedWidthBlock

Object: FixedWidthBlock

Use the FixedWidthBlock object to access channel data in a text file.

The data in this text file is not separated by a specific separator. The data is separated at a specific number of characters, which you specify in the [CharacterCount](../properties/dataplugin_property_charactercount_ifixedwidthchannelformatter.htm) property.

|  | Note The file pointer of the text file does not move when a FixedWidthBlock is read out. |
| --- | --- |

The following example reads the values of a channel from a text file. Four characters of a text line correspond to one channel value. Each text line contains two channel values:

[Copy script](javascript:void(0);)

```text
Dim oBlock: Set oBlock = File.GetFixedWidthBlock
Dim oChannelGroup: Set oChannelGroup = Root.ChannelGroups.Add("Channelgroup")

Dim oChn1 : Set oChn1  = oBlock.Channels.Add("Channel1", eI32)
oChn1.Formatter.CharacterCount = 4
oChn1.Formatter.SampleWidth = 2

Call oChannelGroup.Channels.AddDirectAccessChannel(oChn1)

oBlock.Position = File.Position
```

#### Properties

[BlockLength](../properties/dataplugin_property_blocklength_ifixedwidthblock.htm) | [Channels](../properties/dataplugin_property_channels_ifixedwidthblock.htm) | [Position](../properties/dataplugin_property_position_ifixedwidthblock.htm)

#### Methods

[IsKindOf](../methods/dataplugin_method_iskindof_ifixedwidthblock.htm)

#### Returned From

[File](../objects/dataplugin_objects_imeasurementfileio.htm).[GetFixedWidthBlock](../methods/dataplugin_method_getfixedwidthblock_imeasurementfileio.htm) | [FixedWidthChannelFormatter](../objects/dataplugin_objects_ifixedwidthchannelformatter.htm).[Block](../properties/dataplugin_property_block_ifixedwidthchannelformatter.htm)

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_ifixedwidthchannelformatter.htm language=enus -->
## TOPIC 00111: Object: FixedWidthChannelFormatter

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_ifixedwidthchannelformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_ifixedwidthchannelformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([AbstractDirectAccessChannels](../objects/dataplugin_objects_iabstractdirectaccesschannels.htm) | [BinaryDirectAccessChannels](../objects/dataplugin_objects_ibinarydirectaccesschannels.htm) | [Channels](../objects/dataplugin_objects_ichannels.htm) | [ChannelsToProcess](../objects/dataplugin_objects_ichannelstoprocess.htm) | [DirectAccessChannels](../objects/dataplugin_objects_idirectaccesschannels.htm) | [DirectCellChannels](../objects/dataplugin_objects_iexceldachannels.htm)) > [DirectAccessChannel](../objects/dataplugin_objects_idirectaccesschannel.htm) > Object: FixedWidthChannelFormatter

Object: FixedWidthChannelFormatter

The FixedWidthChannelFormatter object contains information about how the values of a channel are represented in the text file.

The following example shows the settings required for reading the lines listed below:

[Copy script](javascript:void(0);)

```text
0127+098
0000-876
-128+654
```

The text file contains the values from two channels. The FixedWidthChannelFormatter object specifies that four characters in a text line correspond to one channel value:

[Copy script](javascript:void(0);)

```text
Dim oBlock: Set oBlock = File.GetFixedWidthBlock
Dim oChannelGroup: Set oChannelGroup = Root.ChannelGroups.Add("Channelgroup")
          
Dim oChn1  : Set oChn1  = oBlock.Channels.Add("Channel1", eI32)
oChn1.Formatter.CharacterCount = 4
oChn1.Formatter.SampleWidth = 1
Call oChannelGroup.Channels.AddDirectAccessChannel(oChn1)

Dim oChn2  : Set oChn2  = oBlock.Channels.Add("Channel2", eI32)
oChn2.Formatter.CharacterCount = 4
oChn2.Formatter.SampleWidth = 1

Call oChannelGroup.Channels.AddDirectAccessChannel(oChn2)
oBlock.Position = File.Position
```

#### Properties

[Block](../properties/dataplugin_property_block_ifixedwidthchannelformatter.htm) | [CharacterCount](../properties/dataplugin_property_charactercount_ifixedwidthchannelformatter.htm) | [DataType](../properties/dataplugin_property_datatype_ifixedwidthchannelformatter.htm) | [SampleWidth](../properties/dataplugin_property_samplewidth_ifixedwidthchannelformatter.htm)

#### Methods

[IsKindOf](../methods/dataplugin_method_iskindof_iabstractchannelformatter.htm)

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_iformatter.htm language=enus -->
## TOPIC 00112: Object: Formatter

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_iformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_iformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([General](../examples/general.htm) | [Objects](../objects/dataplugin_objects.htm)) > [DataPlugin](../objects/dataplugin_objects_idataplugin.htm) > [File](../objects/dataplugin_objects_imeasurementfileio.htm) > Object: Formatter

Object: Formatter

The Formatter object contains information about the format of the file that the DataPlugin is currently processing.

The following example sets the Formatter object properties that are required for reading the following values:

[Copy script](javascript:void(0);)

```text
28.06.2004 16:28:20; 0,001234¶
28.06.2004 16:28:21; 0,002398¶
28.06.2004 16:28:22; 0,001296¶
28.06.2004 16:28:23; 0,001628¶
28.06.2004 16:28:24; 0,001683¶

File.Formatter.TrimCharacters = " "
File.Formatter.LineFeeds  = vbNewLine
File.Formatter.TimeFormat = "DD.MM.YYYY hh:mm:ss"
File.Formatter.Delimiters = ";"
File.Formatter.DecimalPoint = ","
Dim ValueTime, Value
While (File.Position <> File.Size)
  Set ValueTime = File.GetNextStringValue(eTime)
  Value = File.GetNextStringValue(eR64)
  Call File.SkipLine()
Wend
```

#### Properties

[ByteOrder](../properties/dataplugin_property_byteorder_iformatter.htm) | [CharacterFormat](../properties/dataplugin_property_characterformat_iformatter.htm) | [CommentSign](../properties/dataplugin_property_commentsign_iformatter.htm) | [DecimalPoint](../properties/dataplugin_property_decimalpoint_iformatter.htm) | [Delimiters](../properties/dataplugin_property_delimiters_iformatter.htm) | [ExponentSeparator](../properties/dataplugin_property_exponentseparator_iformatter.htm) | [IgnoreEmptyLines](../properties/dataplugin_property_ignoreemptylines_iformatter.htm) | [LineFeeds](../properties/dataplugin_property_linefeeds_iformatter.htm) | [NoValueSign](../properties/dataplugin_property_novaluesign_iformatter.htm) | [StringSign](../properties/dataplugin_property_stringsign_iformatter.htm) | [ThousandSeparator](../properties/dataplugin_property_thousandseparator_iformatter.htm) | [TimeFormat](../properties/dataplugin_property_timeformat_iformatter.htm) | [TrimCharacters](../properties/dataplugin_property_trimcharacters_iformatter.htm)

#### Methods

[ParseString](../methods/dataplugin_method_parsestring_iformatter.htm)

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_iimplicitchannel.htm language=enus -->
## TOPIC 00113: Object: ImplicitChannel

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_iimplicitchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_iimplicitchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Channels](../objects/dataplugin_objects_ichannels.htm) | [ChannelsToProcess](../objects/dataplugin_objects_ichannelstoprocess.htm)) > Object: ImplicitChannel

Object: ImplicitChannel

The ImplicitChannel object provides an implicit channel and the associated properties.

The following example reads in the generation instruction of an implicit channel and then generates this channel within the channel group MyChnGroup:

[Copy script](javascript:void(0);)

```text
Dim ChannelName: ChannelName = File.GetNextStringValue(eString)
Dim StartValue : StartValue  = File.GetNextStringValue(eString)
Dim Increment  : Increment   = File.GetNextStringValue(eString)
Dim ChannelSize: ChannelSize = File.GetNextStringValue(eString)
Dim ChannelGroup : Set ChannelGroup = Root.ChannelGroupsAdd("MyChnGroup")
Call ChannelGroup.Channels.AddImplicitChannel(ChannelName, StartValue, Increment, ChannelSize, eI32)
```

#### Properties

[ChannelGroup](../properties/dataplugin_property_channelgroup_iimplicitchannel.htm) | [DataType](../properties/dataplugin_property_datatype_iimplicitchannel.htm) | [Increment](../properties/dataplugin_property_increment_iimplicitchannel.htm) | [Name](../properties/dataplugin_property_name_iimplicitchannel.htm) | [Properties](../properties/dataplugin_property_properties_iimplicitchannel.htm) | [Size](../properties/dataplugin_property_size_iimplicitchannel.htm) | [StartValue](../properties/dataplugin_property_startvalue_iimplicitchannel.htm) | [Values](../properties/dataplugin_property_values_iimplicitchannel.htm)

#### Methods

[AddWaveformProperties](../methods/dataplugin_method_addwaveformproperties_iimplicitchannel.htm) | [IsKindOf](../methods/dataplugin_method_iskindof_iimplicitchannel.htm)

#### Returned From

[Channels <DataPlugin>](../objects/dataplugin_objects_ichannels.htm).[AddImplicitChannel](../methods/dataplugin_method_addimplicitchannel_ichannels.htm) | [Channels <DataPlugin>](../objects/dataplugin_objects_ichannels.htm).[Item](../methods/dataplugin_method_item_ichannels.htm) | [ChannelsToProcess](../objects/dataplugin_objects_ichannelstoprocess.htm).[Add](../methods/dataplugin_method_add_ichannelstoprocess.htm) | [ChannelsToProcess](../objects/dataplugin_objects_ichannelstoprocess.htm).[Item](../methods/dataplugin_method_item_ichannelstoprocess.htm)

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_iroot.htm language=enus -->
## TOPIC 00114: Object: Root <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_iroot.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_iroot.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([ChannelGroup](../objects/dataplugin_objects_ichannelgroup.htm) | [DataPlugin](../objects/dataplugin_objects_idataplugin.htm)) > Object: Root <DataPlugin>

Object: Root <DataPlugin>

The Root object provides the list of all channel groups and all properties of the data set.

The following example first deletes all channel groups and then creates the MyChannelGroup channel group:

[Copy script](javascript:void(0);)

```text
Call Root.ChannelGroups.RemoveAll
Call Root.ChannelGroups.Add("MyChannelGroup")
```

#### Properties

[ChannelGroups](../properties/dataplugin_property_channelgroups_iroot.htm) | [Name](../properties/dataplugin_property_name_iroot.htm) | [Properties](../properties/dataplugin_property_properties_iroot.htm)

#### Methods

[ImportStore](../methods/dataplugin_method_importstore_iroot.htm)

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_istringblock.htm language=enus -->
## TOPIC 00115: Object: StringBlock

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_istringblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_istringblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([File](../objects/dataplugin_objects_imeasurementfileio.htm) | [StringChannelFormatter](../objects/dataplugin_objects_istringchannelformatter.htm)) > Object: StringBlock

Object: StringBlock

The StringBlock object facilitates access to text, single values, and channel data in a text file.

If DirectAccess channels are associated with a StringBlock, the order of the values in a line determine which value belongs to which channel. The first value in the line belongs to the first channel, the second value in the line belongs to the second channel, and so on. The [Delimiters](../properties/dataplugin_property_delimiters_iformatter.htm) property in the text file specifies the value limits. [LineFeeds](../properties/dataplugin_property_linefeeds_iformatter.htm) specifies the end of the line.

|  | Note The file pointer of the text file does not move when a StringBlock is read. |
| --- | --- |

The following example reads a text file that consists of one time channel and one real channel. The example then generates a channel group and inserts the two channels:

[Copy script](javascript:void(0);)

```text
Dim oBlock : Set oBlock = File.GetStringBlock()
Dim oChn1  : Set oChn1 = oBlock.Channels.Add("Time", eTime)
Dim oChn2  : Set oChn2 = oBlock.Channels.Add("YShift", eR64)
Dim oMyGrp : Set oMyGrp = Root.ChannelGroups.Add("MyChannelGroup")
Call oMyGrp.Channels.AddDirectAccessChannel(oChn1)
Call oMyGrp.Channels.AddDirectAccessChannel(oChn2)
```

#### Properties

[BlockLength](../properties/dataplugin_property_blocklength_istringblock.htm) | [Channels](../properties/dataplugin_property_channels_istringblock.htm) | [Position](../properties/dataplugin_property_position_istringblock.htm)

#### Methods

[IsKindOf](../methods/dataplugin_method_iskindof_istringblock.htm)

#### Returned From

[File](../objects/dataplugin_objects_imeasurementfileio.htm).[GetStringBlock](../methods/dataplugin_method_getstringblock_imeasurementfileio.htm) | [StringChannelFormatter](../objects/dataplugin_objects_istringchannelformatter.htm).[Block](../properties/dataplugin_property_block_istringchannelformatter.htm)

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/dataplugin_objects_istringchannelformatter.htm language=enus -->
## TOPIC 00116: Object: StringChannelFormatter

- bundle_id: `diadem`
- source_path: `dataplugin/objects/dataplugin_objects_istringchannelformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/dataplugin_objects_istringchannelformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([AbstractDirectAccessChannels](../objects/dataplugin_objects_iabstractdirectaccesschannels.htm) | [BinaryDirectAccessChannels](../objects/dataplugin_objects_ibinarydirectaccesschannels.htm) | [Channels](../objects/dataplugin_objects_ichannels.htm) | [ChannelsToProcess](../objects/dataplugin_objects_ichannelstoprocess.htm) | [DirectAccessChannels](../objects/dataplugin_objects_idirectaccesschannels.htm) | [DirectCellChannels](../objects/dataplugin_objects_iexceldachannels.htm)) > [DirectAccessChannel](../objects/dataplugin_objects_idirectaccesschannel.htm) > Object: StringChannelFormatter

Object: StringChannelFormatter

The StringChannelFormatter object contains information about how the values of a channel are represented in the text file.

The [Formatter](../objects/dataplugin_objects_iformatter.htm) object contains information for formatting the file which is currently being processed by the DataPlugin. This information includes details on the used [decimal sign](../properties/dataplugin_property_decimalpoint_iformatter.htm), [NoValue sign](../properties/dataplugin_property_novaluesign_iformatter.htm), [thousand separator](../properties/dataplugin_property_thousandseparator_iformatter.htm), and [date/time format](../properties/dataplugin_property_timeformat_iformatter.htm). These formatting details are universally true, which means that the DataPlugin uses them for reading in all channels from the text file. If a channel deviates from these formatting instructions, you can use the StringChannelFormatter object to specify an individual format for this channel.

The following example checks each channel whether this channel has a StringBlock and creates the channel property DataType:

[Copy script](javascript:void(0);)

```text
Dim oMyChn
For Each oMyChn in oBlock.Channels
  If (oMyChn.Formatter.IsKindOf(eStringBlock)) Then
    Call oMyChn.Properties.Add("DataType", oMyChn.Formatter.DataType)
  End If
Next
```

#### Properties

[Block](../properties/dataplugin_property_block_istringchannelformatter.htm) | [DataType](../properties/dataplugin_property_datatype_istringchannelformatter.htm) | [DecimalPoint](../properties/dataplugin_property_decimalpoint_istringchannelformatter.htm) | [NoValueSign](../properties/dataplugin_property_novaluesign_istringchannelformatter.htm) | [ThousandSeparator](../properties/dataplugin_property_thousandseparator_istringchannelformatter.htm) | [TimeFormat](../properties/dataplugin_property_timeformat_istringchannelformatter.htm)

#### Methods

[IsKindOf](../methods/dataplugin_method_iskindof_istringchannelformatter.htm)

#### See Also

[File Object Overview](../objects/idataplugin_objects_overview_file.htm) | [Workbook Object Overview](../objects/idataplugin_objects_overview_excel.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/idataplugin_objects_overview_documents.htm language=enus -->
## TOPIC 00117: Document <DataPlugin>-Object: Overview

- bundle_id: `diadem`
- source_path: `dataplugin/objects/idataplugin_objects_overview_documents.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/idataplugin_objects_overview_documents.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [General](../examples/general.htm) > Document <DataPlugin>-Object: Overview

[[IMAGE alt='image' src='ms-its:diadem.chm::/plus.png']Display all](#nowhere)  [[IMAGE alt='image' src='ms-its:diadem.chm::/minus2.png']Hide all](#nowhere)

Document <DataPlugin>-Object: Overview

The DataPlugin consists of objects and subobjects that you create, delete, and modify with a script. You receive the Document <DataPlugin> object if you select the file reader Document File Reader when you create a new DataPlugin. The ReadStore procedure receives the Document <DataPlugin> object through the Document parameter and thus a reference to the document to be loaded. A document might be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file.

The structure of the Document <DataPlugin> object is shown in the following:

- Document <DataPlugin>
  - DocumentNamespaces 
 <DataPlugin>
    - DocumentNamespace 
 <DataPlugin>
      - DocumentProperties 
 <DataPlugin>
        - DocumentProperty 
 <DataPlugin>
  - DocumentProperties 
 <DataPlugin>
    - DocumentProperty 
 <DataPlugin>

For an overview of the global methods and properties of the DataPlugin, click [here](../objects/dataplugin_objects_idataplugin.htm).

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/idataplugin_objects_overview_excel.htm language=enus -->
## TOPIC 00118: Workbook Object: Overview

- bundle_id: `diadem`
- source_path: `dataplugin/objects/idataplugin_objects_overview_excel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/idataplugin_objects_overview_excel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [General](../examples/general.htm) > Workbook Object: Overview

[[IMAGE alt='image' src='ms-its:diadem.chm::/plus.png']Display all](#nowhere)  [[IMAGE alt='image' src='ms-its:diadem.chm::/minus2.png']Hide all](#nowhere)

Workbook Object: Overview

The DataPlugin consists of objects and subobjects that you create, delete, and modify with a script. You receive the Workbook object if you select the file reader Spreadsheet Reader when you create a new DataPlugin. The file reader Spreadsheet reader can access Excel files which were created with OpenOffice, Excel 2007, Excel 2003, or an earlier version and which are not password protected. The ReadStore procedure receives the workbook object with a reference to the file to be loaded via the Workbook parameter. When loading data from an XLSM file, DIAdem does not execute the macros contained in this file.

To search for data in or to load data from a spreadsheet, Microsoft.NET Framework 4.0 must be installed on your computer. DIAdem installs Microsoft.NET Framework 4.0 by default.

The Workbook object structure is shown in the following:

- Workbook
  - CellFormatter
  - Info
  - Sheets
    - Sheet
      - CellBlock
        - CellPosition
        - DirectCellChannels
          - DirectAccessChannel
            - AbstractChannelFormatter
            - BinaryChannelFormatter
              - BinaryBlock
                - AbstractDirectAccessChannels
                  - DirectAccessChannel
                - BinaryDirectAccessChannels
                  - DirectAccessChannel
                - DirectAccessChannels
                  - DirectAccessChannel
            - CellChannelFormatter
              - CellBlock
            - FixedWidthChannelFormatter
              - FixedWidthBlock
                - AbstractDirectAccessChannels
                  - DirectAccessChannel
                - BinaryDirectAccessChannels
                  - DirectAccessChannel
                - DirectAccessChannels
                  - DirectAccessChannel
            - Properties <DataPlugin>
              - Property <DataPlugin>
            - StringChannelFormatter
              - StringBlock
                - AbstractDirectAccessChannels
                  - DirectAccessChannel
                - BinaryDirectAccessChannels
                  - DirectAccessChannel
                - DirectAccessChannels
                  - DirectAccessChannel
      - CellPosition
  - WorkbookInfo

For an overview of the global methods and properties of the DataPlugin, click [here](../objects/dataplugin_objects_idataplugin.htm).

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/idataplugin_objects_overview_file.htm language=enus -->
## TOPIC 00119: File Object: Overview

- bundle_id: `diadem`
- source_path: `dataplugin/objects/idataplugin_objects_overview_file.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/idataplugin_objects_overview_file.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [General](../examples/general.htm) > File Object: Overview

[[IMAGE alt='image' src='ms-its:diadem.chm::/plus.png']Display all](#nowhere)  [[IMAGE alt='image' src='ms-its:diadem.chm::/minus2.png']Hide all](#nowhere)

File Object: Overview

The DataPlugin consists of objects and subobjects that you create, delete, and modify with a script. You receive the File object if you select the ASCII Binary file reader when you create a new DataPlugin. The ReadStore procedure receives the File object with a reference to the file to load, via the File parameter.

The File object structure is shown in the following:

- File
  - BinaryBlock
    - AbstractDirectAccessChannels
      - DirectAccessChannel
        - AbstractChannelFormatter
        - BinaryChannelFormatter
          - BinaryBlock
        - CellChannelFormatter
          - CellBlock
            - CellPosition
            - DirectCellChannels
              - DirectAccessChannel
        - FixedWidthChannelFormatter
          - FixedWidthBlock
            - AbstractDirectAccessChannels
            - BinaryDirectAccessChannels
              - DirectAccessChannel
            - DirectAccessChannels
              - DirectAccessChannel
        - Properties <DataPlugin>
          - Property <DataPlugin>
        - StringChannelFormatter
          - StringBlock
            - AbstractDirectAccessChannels
            - BinaryDirectAccessChannels
              - DirectAccessChannel
            - DirectAccessChannels
              - DirectAccessChannel
    - BinaryDirectAccessChannels
      - DirectAccessChannel
        - AbstractChannelFormatter
        - BinaryChannelFormatter
          - BinaryBlock
        - CellChannelFormatter
          - CellBlock
            - CellPosition
            - DirectCellChannels
              - DirectAccessChannel
        - FixedWidthChannelFormatter
          - FixedWidthBlock
            - AbstractDirectAccessChannels
              - DirectAccessChannel
            - BinaryDirectAccessChannels
            - DirectAccessChannels
              - DirectAccessChannel
        - Properties <DataPlugin>
          - Property <DataPlugin>
        - StringChannelFormatter
          - StringBlock
            - AbstractDirectAccessChannels
              - DirectAccessChannel
            - BinaryDirectAccessChannels
            - DirectAccessChannels
              - DirectAccessChannel
    - DirectAccessChannels
      - DirectAccessChannel
        - AbstractChannelFormatter
        - BinaryChannelFormatter
          - BinaryBlock
        - CellChannelFormatter
          - CellBlock
            - CellPosition
            - DirectCellChannels
              - DirectAccessChannel
        - FixedWidthChannelFormatter
          - FixedWidthBlock
            - AbstractDirectAccessChannels
              - DirectAccessChannel
            - BinaryDirectAccessChannels
              - DirectAccessChannel
            - DirectAccessChannels
        - Properties <DataPlugin>
          - Property <DataPlugin>
        - StringChannelFormatter
          - StringBlock
            - AbstractDirectAccessChannels
              - DirectAccessChannel
            - BinaryDirectAccessChannels
              - DirectAccessChannel
            - DirectAccessChannels
  - FixedWidthBlock
    - AbstractDirectAccessChannels
      - DirectAccessChannel
        - AbstractChannelFormatter
        - BinaryChannelFormatter
          - BinaryBlock
            - AbstractDirectAccessChannels
            - BinaryDirectAccessChannels
              - DirectAccessChannel
            - DirectAccessChannels
              - DirectAccessChannel
        - CellChannelFormatter
          - CellBlock
            - CellPosition
            - DirectCellChannels
              - DirectAccessChannel
        - FixedWidthChannelFormatter
          - FixedWidthBlock
        - Properties <DataPlugin>
          - Property <DataPlugin>
        - StringChannelFormatter
          - StringBlock
            - AbstractDirectAccessChannels
            - BinaryDirectAccessChannels
              - DirectAccessChannel
            - DirectAccessChannels
              - DirectAccessChannel
    - BinaryDirectAccessChannels
      - DirectAccessChannel
        - AbstractChannelFormatter
        - BinaryChannelFormatter
          - BinaryBlock
            - AbstractDirectAccessChannels
              - DirectAccessChannel
            - BinaryDirectAccessChannels
            - DirectAccessChannels
              - DirectAccessChannel
        - CellChannelFormatter
          - CellBlock
            - CellPosition
            - DirectCellChannels
              - DirectAccessChannel
        - FixedWidthChannelFormatter
          - FixedWidthBlock
        - Properties <DataPlugin>
          - Property <DataPlugin>
        - StringChannelFormatter
          - StringBlock
            - AbstractDirectAccessChannels
              - DirectAccessChannel
            - BinaryDirectAccessChannels
            - DirectAccessChannels
              - DirectAccessChannel
    - DirectAccessChannels
      - DirectAccessChannel
        - AbstractChannelFormatter
        - BinaryChannelFormatter
          - BinaryBlock
            - AbstractDirectAccessChannels
              - DirectAccessChannel
            - BinaryDirectAccessChannels
              - DirectAccessChannel
            - DirectAccessChannels
        - CellChannelFormatter
          - CellBlock
            - CellPosition
            - DirectCellChannels
              - DirectAccessChannel
        - FixedWidthChannelFormatter
          - FixedWidthBlock
        - Properties <DataPlugin>
          - Property <DataPlugin>
        - StringChannelFormatter
          - StringBlock
            - AbstractDirectAccessChannels
              - DirectAccessChannel
            - BinaryDirectAccessChannels
              - DirectAccessChannel
            - DirectAccessChannels
  - Formatter
  - Info
  - StringBlock
    - AbstractDirectAccessChannels
      - DirectAccessChannel
        - AbstractChannelFormatter
        - BinaryChannelFormatter
          - BinaryBlock
            - AbstractDirectAccessChannels
            - BinaryDirectAccessChannels
              - DirectAccessChannel
            - DirectAccessChannels
              - DirectAccessChannel
        - CellChannelFormatter
          - CellBlock
            - CellPosition
            - DirectCellChannels
              - DirectAccessChannel
        - FixedWidthChannelFormatter
          - FixedWidthBlock
            - AbstractDirectAccessChannels
            - BinaryDirectAccessChannels
              - DirectAccessChannel
            - DirectAccessChannels
              - DirectAccessChannel
        - Properties <DataPlugin>
          - Property <DataPlugin>
        - StringChannelFormatter
          - StringBlock
    - BinaryDirectAccessChannels
      - DirectAccessChannel
        - AbstractChannelFormatter
        - BinaryChannelFormatter
          - BinaryBlock
            - AbstractDirectAccessChannels
              - DirectAccessChannel
            - BinaryDirectAccessChannels
            - DirectAccessChannels
              - DirectAccessChannel
        - CellChannelFormatter
          - CellBlock
            - CellPosition
            - DirectCellChannels
              - DirectAccessChannel
        - FixedWidthChannelFormatter
          - FixedWidthBlock
            - AbstractDirectAccessChannels
              - DirectAccessChannel
            - BinaryDirectAccessChannels
            - DirectAccessChannels
              - DirectAccessChannel
        - Properties <DataPlugin>
          - Property <DataPlugin>
        - StringChannelFormatter
          - StringBlock
    - DirectAccessChannels
      - DirectAccessChannel
        - AbstractChannelFormatter
        - BinaryChannelFormatter
          - BinaryBlock
            - AbstractDirectAccessChannels
              - DirectAccessChannel
            - BinaryDirectAccessChannels
              - DirectAccessChannel
            - DirectAccessChannels
        - CellChannelFormatter
          - CellBlock
            - CellPosition
            - DirectCellChannels
              - DirectAccessChannel
        - FixedWidthChannelFormatter
          - FixedWidthBlock
            - AbstractDirectAccessChannels
              - DirectAccessChannel
            - BinaryDirectAccessChannels
              - DirectAccessChannel
            - DirectAccessChannels
        - Properties <DataPlugin>
          - Property <DataPlugin>
        - StringChannelFormatter
          - StringBlock

For an overview of the global methods and properties of the DataPlugin, click [here](../objects/dataplugin_objects_idataplugin.htm).

<!--NI_TOPIC bundle=diadem path=dataplugin/objects/idataplugin_objects_overview_store.htm language=enus -->
## TOPIC 00120: Store Object: Overview

- bundle_id: `diadem`
- source_path: `dataplugin/objects/idataplugin_objects_overview_store.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/objects/idataplugin_objects_overview_store.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [General](../examples/general.htm) > Store Object: Overview

[[IMAGE alt='image' src='ms-its:diadem.chm::/plus.png']Display all](#nowhere)  [[IMAGE alt='image' src='ms-its:diadem.chm::/minus2.png']Hide all](#nowhere)

Store Object: Overview

The DataPlugin consists of objects and subobjects that you create, delete, and modify with a script. You receive the Store object if you select a DataPlugin file reader when you create a new DataPlugin. The ReadStore procedure receives the Store object with a reference to the data store to be loaded, via the FromStore parameter.

The Store object structure is shown in the following:

- Store
  - Elements <DataPlugin>
    - Element <DataPlugin>
      - Elements <DataPlugin>
      - Properties <DataPlugin>
        - Property <DataPlugin>
  - Info

For an overview of the global methods and properties of the DataPlugin, click [here](../objects/dataplugin_objects_idataplugin.htm).

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_properties_overview.htm language=enus -->
## TOPIC 00121: Properties

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_properties_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_properties_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > Properties

Properties

Properties determine the behavior of objects or return objects. These objects can have their own properties and methods.

The subordinate topics contained in the tree on the contents tab of the Help describe all the properties of the script interface of DataPlugins.

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_bitmask_ibinarychannelformatter.htm language=enus -->
## TOPIC 00122: Property: BitMask for BinaryChannelFormatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_bitmask_ibinarychannelformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_bitmask_ibinarychannelformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: BitMask for BinaryChannelFormatter

Property: BitMask for BinaryChannelFormatter

Specifies the bit mask that masks the value DIAdem reads in.

You can use bit masking to hide single bits when values are read in. The data is masked with an AND operation:

New value = old value AND bit mask

The bit masking is executed before values are calibrated by [Factor](../properties/dataplugin_property_factor_idirectaccesschannel.htm) and [Offset](../properties/dataplugin_property_offset_idirectaccesschannel.htm).

```text
Object.BitMask
```

| Object | BinaryChannelFormatterObject with this property |
| --- | --- |
| Object.BitMask | String with read and write access |

|  | Note The bit mask is ignored when R32 values and R64 values are read. |
| --- | --- |

|  | Note You can specify the value of the bit mask as a decimal, hexadecimal, or octal. 1234 is a decimal value, 0x134 is a hexadecimal value, and 01234 is an octal value. |
| --- | --- |

The following example shows how to mask the fifth bit when channel values are read. You set the bit mask to 2<sup>5-1</sup> = 16. If the fifth bit is set as a value, the result is 16, otherwise it is zero. However, if you want the channel to only contain the values 0 (bit not set) and 1 (bit set), scale the channel with the factor <sup>1</sup>/<sub>16</sub>= 0.0625.

[Copy script](javascript:void(0);)

```text
Dim oBlock : Set oBlock = File.GetBinaryBlock()
Dim oChn : Set oChn = oBlock.Channels.Add("MyChannel", eI32)
oChn.Formatter.Bitmask = 16
oChn.Factor = 0.0625
Dim oMyGrp: Set oMyGrp = Root.ChannelGroups.Add("MyChannelGroup")
oMyGrp.Channels.AddDirectAccessChannel(oChn)
```

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_block_ibinarychannelformatter.htm language=enus -->
## TOPIC 00123: Property: Block for BinaryChannelFormatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_block_ibinarychannelformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_block_ibinarychannelformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Block for BinaryChannelFormatter

Property: Block for BinaryChannelFormatter

Contains the parent object for a BinaryChannelFormatter object.

```text
Set oBinaryBlock = Object.Block
```

| Object | BinaryChannelFormatterObject with this property |
| --- | --- |
| oBinaryBlock | BinaryBlockReturned object |

If the channel belongs to a BinaryBlock, the following example interprets the first byte as the higher-order byte when reading in the channel values:

[Copy script](javascript:void(0);)

```text
If oMyChn.Formatter.Block.IsKindOf(eBinaryBlock) Then
  oMyChn.Formatter.ByteOrder = eBigEndian
End If
```

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_block_icellchannelformatter.htm language=enus -->
## TOPIC 00124: Property: Block for CellChannelFormatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_block_icellchannelformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_block_icellchannelformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Block for CellChannelFormatter

Property: Block for CellChannelFormatter

Contains the parent object for a CellChannelFormatter object.

```text
Set oCellBlock = Object.Block
```

| Object | CellChannelFormatterObject with this property |
| --- | --- |
| oCellBlock | CellBlockReturned object |

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_block_ifixedwidthchannelformatter.htm language=enus -->
## TOPIC 00125: Property: Block for FixedWidthChannelFormatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_block_ifixedwidthchannelformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_block_ifixedwidthchannelformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Block for FixedWidthChannelFormatter

Property: Block for FixedWidthChannelFormatter

Contains the parent object for a FixedWidthChannelFormatter object.

```text
Set oFixedWidthBlock = Object.Block
```

| Object | FixedWidthChannelFormatterObject with this property |
| --- | --- |
| oFixedWidthBlock | FixedWidthBlockReturned object |

If the channel is associated with a FixedWidthBlock type, the following example changes the number of characters read from the text file per channel value:

[Copy script](javascript:void(0);)

```text
If oMyChn.Formatter.Block.IsKindOf(eFixedWidthBlock) Then
  oMyChn.Formatter.CharacterCount = 4
End If
```

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_block_istringchannelformatter.htm language=enus -->
## TOPIC 00126: Property: Block for StringChannelFormatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_block_istringchannelformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_block_istringchannelformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Block for StringChannelFormatter

Property: Block for StringChannelFormatter

Contains the parent object for a StringChannelFormatter object.

```text
Set oStringBlock = Object.Block
```

| Object | StringChannelFormatterObject with this property |
| --- | --- |
| oStringBlock | StringBlockReturned object |

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_blocklength_ibinaryblock.htm language=enus -->
## TOPIC 00127: Property: BlockLength for BinaryBlock

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_blocklength_ibinaryblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_blocklength_ibinaryblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: BlockLength for BinaryBlock

Property: BlockLength for BinaryBlock

Specifies the number of values that a channel in the BinaryBlock contains.

If the number is -1, the block extends to the end of the file.

```text
Object.BlockLength
```

| Object | BinaryBlockObject with this property |
| --- | --- |
| Object.BlockLength | LongInteger with read and write access |

The following example checks the block type and sets the block length according to this block type:

[Copy script](javascript:void(0);)

```text
If oBlock.IsKindOf(eBinaryBlock) Then
  oBlock.BlockLength = -1
Else
  oBlock.BlockLength = 20  
End If
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_blocklength_icellblock.htm language=enus -->
## TOPIC 00128: Property: BlockLength for CellBlock

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_blocklength_icellblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_blocklength_icellblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: BlockLength for CellBlock

Property: BlockLength for CellBlock

Specifies the number of values that a channel in the CellBlock contains.

If the number is -1, the block extends to the end of the file.

```text
Object.BlockLength
```

| Object | CellBlockObject with this property |
| --- | --- |
| Object.BlockLength | LongInteger with read and write access |

The following example reads in the values of the worksheet columnwise and saves the values in channels from the first channel group: The example reads in only five values per channel.

[Copy script](javascript:void(0);)

```text
Dim oCurrSheet
Set oCurrSheet = Workbook.Sheets(1)
Dim oCellBlock
Set oCellBlock = oCurrSheet.GetCellBlock(2,1)
oCellBlock.BlockLength = 5

Dim i, Name, oNewChannel
For i = 1 to oCurrSheet.MaxPosition.Column
  Name = oCurrSheet.GetCellValue(1,i)
  Set oNewChannel = oCellBlock.Channels.Add(Name) 
  Call Root.ChannelGroups(1).Channels.AddDirectAccessChannel(oNewChannel)
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_blocklength_ifixedwidthblock.htm language=enus -->
## TOPIC 00129: Property: BlockLength for FixedWidthBlock

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_blocklength_ifixedwidthblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_blocklength_ifixedwidthblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: BlockLength for FixedWidthBlock

Property: BlockLength for FixedWidthBlock

Specifies the number of values that a channel in the FixedWidthBlock contains.

If the number is -1, the block extends to the end of the file.

```text
Object.BlockLength
```

| Object | FixedWidthBlockObject with this property |
| --- | --- |
| Object.BlockLength | LongInteger with read and write access |

|  | Note If the property SampleWidth is not equal to 1 in a FixedWidthBlock, the BlockLength contains the number of lines in a text file. |
| --- | --- |

The following example reads a group name and the length of a FixedWidthBlock from a text file. Then the example creates this channel group with the property BlockLength and the channel MyChannel. The example skips the lines specified by the BlockLength before reading in the channel values:

[Copy script](javascript:void(0);)

```text
Dim oBlock : Set oBlock = File.GetFixedWidthBlock
Dim GroupName : GroupName = File.GetNextStringValue(eString)
oBlock.BlockLength = File.GetNextStringValue(eI32)
       
Set oChannelGroup = Root.ChannelGroups.Add(GroupName)
Call oChannelGroup.Properties.Add("BlockLength", oBlock.BlockLength)
  
Dim oChannel : Set oChannel = Block.Channels.Add("MyChannel", eI16)
oChannel.Formatter.CharacterCount = 4
oChannel.Formatter.SampleWidth = 4
Call oChannelGroup.Channels.AddDirectAccessChannel(Channel)
              
Call File.SkipLines(oBlock.BlockLength+1)
oBlock.Position = File.Position
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_blocklength_istringblock.htm language=enus -->
## TOPIC 00130: Property: BlockLength for StringBlock

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_blocklength_istringblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_blocklength_istringblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: BlockLength for StringBlock

Property: BlockLength for StringBlock

Specifies the number of values that a channel in the StringBlock contains.

If the number is -1, the block extends to the end of the file.

```text
Object.BlockLength
```

| Object | StringBlockObject with this property |
| --- | --- |
| Object.BlockLength | LongInteger with read and write access |

The following example checks the block type and sets the block length according to this block type:

[Copy script](javascript:void(0);)

```text
If oBlock.IsKindOf(eBinaryBlock) Then
  oBlock.BlockLength = -1
ElseIf oBlock.IsKindOf(eStringBlock) Then
  oBlock.BlockLength = 20
End If
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_blockwidth_ibinaryblock.htm language=enus -->
## TOPIC 00131: Property: BlockWidth for BinaryBlock

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_blockwidth_ibinaryblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_blockwidth_ibinaryblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: BlockWidth for BinaryBlock

Property: BlockWidth for BinaryBlock

Specifies the number of bytes between two consecutive values of a block channel.

If the value is -1, the interval between the values is automatically calculated in relation to the channels in this block.

```text
Object.BlockWidth
```

| Object | BinaryBlockObject with this property |
| --- | --- |
| Object.BlockWidth | LongInteger with read and write access |

The following example reads a BinaryBlock from a file that contains four 32-bit integer channels. The block width is 16 which means that the example only uses the values of the first channel and skips the other channel values:

[Copy script](javascript:void(0);)

```text
Dim oBlock : Set oBlock = File.GetBinaryBlock()
Dim oChannel1 : Set oChannel1 = oBlock.Channels.Add("Channel1", eI32)
oBlock.BlockWidth = 16
Dim oChannelGroup : Set oChannelGroup = Root.ChannelGroups.Add("MyChannelGroup")
Call oChannelGroup.Channels.AddDirectAccessChannel(oChannel1)
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_byteorder_ibinarychannelformatter.htm language=enus -->
## TOPIC 00132: Property: ByteOrder for BinaryChannelFormatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_byteorder_ibinarychannelformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_byteorder_ibinarychannelformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: ByteOrder for BinaryChannelFormatter

Property: ByteOrder for BinaryChannelFormatter

Specifies the byte order for a channel in the file if the data type consists of several bytes.

```text
Object.ByteOrder
```

| Object | BinaryChannelFormatterObject with this property |  |
| --- | --- | --- |
| Object.ByteOrder | Receives the sequence of bytes in the file.Enumeration with read and write access and the following selection terms: 1eLittleEndian The first byte is the higher-value byte. 2eBigEndian The last byte is the higher-value byte. |  |
| 1 | eLittleEndian | The first byte is the higher-value byte. |
| 2 | eBigEndian | The last byte is the higher-value byte. |

The following example interprets the first byte as the higher-value byte when the values of the MyChannel are read.

[Copy script](javascript:void(0);)

```text
Dim oBinBlock : Set oBinBlock = File.GetBinaryBlock()
Dim oChn : Set oChn = oBinBlock.Channels.Add("MyChannel",eI16)
oChn.Factor = 5
oChn.Offset = 50
oChn.Formatter.ByteOrder = eBigEndian
Dim oMyGrp: Set oMyGrp = Root.ChannelGroups.Add("MyChannelGroup")
Call oMyGrp.Channels.AddDirectAccessChannel(oChn)
```

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_byteorder_iformatter.htm language=enus -->
## TOPIC 00133: Property: ByteOrder for Formatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_byteorder_iformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_byteorder_iformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: ByteOrder for Formatter

Property: ByteOrder for Formatter

Specifies the byte order in the file if the data type consists of several bytes.

```text
Object.ByteOrder
```

| Object | FormatterObject with this property |  |
| --- | --- | --- |
| Object.ByteOrder | Receives the sequence of bytes in the file.Enumeration with read and write access and the following selection terms: 1eLittleEndian The first byte is the higher-value byte. 2eBigEndian The last byte is the higher-value byte. |  |
| 1 | eLittleEndian | The first byte is the higher-value byte. |
| 2 | eBigEndian | The last byte is the higher-value byte. |

If the byte order is BigEndian, the last byte is the byte with the highest value. If the byte order is LittleEndian, the opposite applies. In the former case, the number 255 is FF 00 in hexadecimal, and in the latter case, it is 00 FF.

The following example interprets the first byte as the higher-value byte when the channel values are read.

[Copy script](javascript:void(0);)

```text
File.Formatter.ByteOrder = eBigEndian
Dim oBlock : Set oBlock = File.GetBinaryBlock()
Dim oChn1  : Set oChn1  = oBlock.Channels.Add("MyChannel1", eI32)
Dim oChn2  : Set oChn2  = oBlock.Channels.Add("MyChannel2", eI32)
Dim oMyGrp : Set oMyGrp = Root.ChannelGroups.Add("MyChannelGroup")
oMyGrp.Channels.AddDirectAccessChannel(oChn1)
oMyGrp.Channels.AddDirectAccessChannel(oChn2)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_channelgroup_ichannel.htm language=enus -->
## TOPIC 00134: Property: ChannelGroup for Channel <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_channelgroup_ichannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_channelgroup_ichannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: ChannelGroup for Channel <DataPlugin>

Property: ChannelGroup for Channel <DataPlugin>

Specifies the channel group to which a channel is assigned.

```text
Set oChannelGroup = Object.ChannelGroup
```

| Object | Channel <DataPlugin>Object with this property |
| --- | --- |
| oChannelGroup | ChannelGroup <DataPlugin>Returned object |

The following example displays the name of the channel group that contains the Temp channel:

[Copy script](javascript:void(0);)

```text
Dim i, oMyChn
For i = 1 to Root.ChannelGroups.Count
  For Each oMyChn in Root.ChannelGroups(i).Channels
    If oMyChn.Name = "Temp" Then
      Call MsgBoxDisp(oMyChn.ChannelGroup.Name)
    End If
  Next
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_channelgroup_iimplicitchannel.htm language=enus -->
## TOPIC 00135: Property: ChannelGroup for ImplicitChannel

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_channelgroup_iimplicitchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_channelgroup_iimplicitchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: ChannelGroup for ImplicitChannel

Property: ChannelGroup for ImplicitChannel

Specifies the channel group to which the implicit channel is assigned.

```text
Set oChannelGroup = Object.ChannelGroup
```

| Object | ImplicitChannelObject with this property |
| --- | --- |
| oChannelGroup | ChannelGroup <DataPlugin>Returned object |

The following example displays the name of the channel group that contains the Temp channel:

[Copy script](javascript:void(0);)

```text
Dim i, oMyChn
For i = 1 to Root.ChannelGroups.Count
  For Each oMyChn in Root.ChannelGroups(i).Channels
    If oMyChn.Name = "Temp" Then
      Call MsgBoxDisp(oMyChn.ChannelGroup.Name)
    End If
  Next
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_channelgroups_iroot.htm language=enus -->
## TOPIC 00136: Property: ChannelGroups for Root <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_channelgroups_iroot.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_channelgroups_iroot.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: ChannelGroups for Root <DataPlugin>

Property: ChannelGroups for Root <DataPlugin>

Contains the ChannelGroups collection associated with a Root object.

ChannelGroups object with read access.

```text
Set oChannelGroups = Object.ChannelGroups
```

| Object | Root <DataPlugin>Object with this property |
| --- | --- |
| oChannelGroups | ChannelGroups <DataPlugin>Returned object |

The following example searches in all channel groups for the Test_Status property and changes the value of this property:

[Copy script](javascript:void(0);)

```text
Dim i, j, oMyProp
For j = 1 to Root.ChannelGroups.Count
  Set oMyProp = Root.ChannelGroups(j).Properties
  For i = 1 to oMyProp.Count
    If oMyProp(i).Name = "Test_Status" Then
      oMyProp(i).Value = "failed"
    End If
  Next
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_channels_ibinaryblock.htm language=enus -->
## TOPIC 00137: Property: Channels for BinaryBlock

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_channels_ibinaryblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_channels_ibinaryblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Channels for BinaryBlock

Property: Channels for BinaryBlock

Contains the DirectAccessChannels collection associated with a BinaryBlock object.

```text
Set oAbstractDirectAccessChannels = Object.Channels
```

| Object | BinaryBlockObject with this property |
| --- | --- |
| oAbstractDirectAccessChannels | AbstractDirectAccessChannelsReturned object |

The following example creates the channel property Offset for each DirectAccess channel:

[Copy script](javascript:void(0);)

```text
Dim oBlock : Set oBlock = File.GetBinaryBlock()
'further instructions
Dim i
For i = 1 to oBlock.Channels.Count
  Call oBlock.Channels(i).Properties.Add("Offset",3)
Next
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_channels_icellblock.htm language=enus -->
## TOPIC 00138: Property: Channels for CellBlock

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_channels_icellblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_channels_icellblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Channels for CellBlock

Property: Channels for CellBlock

Contains the DirectAccessChannels collection associated with a CellBlock object.

```text
Set oDirectCellChannels = Object.Channels
```

| Object | CellBlockObject with this property |
| --- | --- |
| oDirectCellChannels | DirectCellChannelsReturned object |

The following example reads in the values of the worksheet columnwise from the second row of the first column and saves the values in channels of the first channel group:

[Copy script](javascript:void(0);)

```text
Dim oCurrSheet
Set oCurrSheet = Workbook.Sheets(1)
Dim oCellBlock
Set oCellBlock = oCurrSheet.GetCellBlock(2,1)

Dim i, Name, oNewChannel
For i = 1 to oCurrSheet.MaxPosition.Column
  Name = oCurrSheet.GetCellValue(1,i)
  Set oNewChannel = oCellBlock.Channels.Add(Name) 
  Call Root.ChannelGroups(1).Channels.AddDirectAccessChannel(oNewChannel)
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_channels_ichannelgroup.htm language=enus -->
## TOPIC 00139: Property: Channels for ChannelGroup <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_channels_ichannelgroup.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_channels_ichannelgroup.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Channels for ChannelGroup <DataPlugin>

Property: Channels for ChannelGroup <DataPlugin>

Contains the Channels collection associated with a ChannelGroup object.

Channels object with read access.

```text
Set oChannels = Object.Channels
```

| Object | ChannelGroup <DataPlugin>Object with this property |
| --- | --- |
| oChannels | Channels <DataPlugin>Returned object |

The following example creates the channel property Sensor_Type for each channel from the QT_34-5_Lower channel group:

[Copy script](javascript:void(0);)

```text
Dim oMyChn
For Each oMyChn in Root.ChannelGroups("QT_34-51_Lower").Channels
  Call oMyChn.Properties.Add("Sensor_Type","TC-N")
Next
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_channels_ifixedwidthblock.htm language=enus -->
## TOPIC 00140: Property: Channels for FixedWidthBlock

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_channels_ifixedwidthblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_channels_ifixedwidthblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Channels for FixedWidthBlock

Property: Channels for FixedWidthBlock

Contains the DirectAccessChannels collection associated with a FixedWidthBlock object.

```text
Set oAbstractDirectAccessChannels = Object.Channels
```

| Object | FixedWidthBlockObject with this property |
| --- | --- |
| oAbstractDirectAccessChannels | AbstractDirectAccessChannelsReturned object |

The following example creates the channel property Offset for each DirectAccess channel:

[Copy script](javascript:void(0);)

```text
Dim oBlock : Set oBlock = File.GetFixedWidthBlock
'further instructions
Dim i
For i = 1 to oBlock.Channels.Count
  Call oBlock.Channels(i).Properties.Add("Offset",3)
Next
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_channels_iprocessedchannel.htm language=enus -->
## TOPIC 00141: Property: Channels for ProcessedChannel

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_channels_iprocessedchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_channels_iprocessedchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Channels for ProcessedChannel

Property: Channels for ProcessedChannel

Contains the ChannelsToProcess collection associated with a ProcessedChannel object.

ProcessedChannel object with read access.

```text
Set oChannelsToProcess = Object.Channels
```

| Object | ProcessedChannelObject with this property |
| --- | --- |
| oChannelsToProcess | ChannelsToProcessReturned object |

The following example generates a new channel MyChannel in the Measurements channel group. The channel contains the values, which are added rowwise, of the 64-bit Real type DirectAccess channels from the Measurements channel group.

[Copy script](javascript:void(0);)

```text
Dim ChannelGroup: Set ChannelGroup = Root.ChannelGroups.Add("Measurements")
Dim ProcessedChn: Set ProcessedChn = ChannelGroup.Channels.AddProcessedChannel("MyChannel",eR64,eAddProcessor)
Dim Channel
For Each Channel in ChannelGroup.Channels
  If Channel.IsKindOf(eDirectAccess) and (Channel.DataType = eR64) Then
    Call ProcessedChn.Channels.Add(Channel)
  End If
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_channels_istringblock.htm language=enus -->
## TOPIC 00142: Property: Channels for StringBlock

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_channels_istringblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_channels_istringblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Channels for StringBlock

Property: Channels for StringBlock

Contains the DirectAccessChannels collection associated with a StringBlock object.

```text
Set oAbstractDirectAccessChannels = Object.Channels
```

| Object | StringBlockObject with this property |
| --- | --- |
| oAbstractDirectAccessChannels | AbstractDirectAccessChannelsReturned object |

The following example creates the channel property Offset for each DirectAccess channel:

[Copy script](javascript:void(0);)

```text
Dim oBlock : Set oBlock = File.GetStringBlock
'further instructions
Dim i
For i = 1 to oBlock.Channels.Count
  Call oBlock.Channels(i).Properties.Add("Offset",3)
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_charactercount_ifixedwidthchannelformatter.htm language=enus -->
## TOPIC 00143: Property: CharacterCount for FixedWidthChannelFormatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_charactercount_ifixedwidthchannelformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_charactercount_ifixedwidthchannelformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: CharacterCount for FixedWidthChannelFormatter

Property: CharacterCount for FixedWidthChannelFormatter

Specifies the number of characters that are read from the text file per channel value. The default value for this property is 10.

```text
Object.CharacterCount
```

| Object | FixedWidthChannelFormatterObject with this property |
| --- | --- |
| Object.CharacterCount | LongInteger with read and write access |

The following example shows the settings required for reading the lines listed below:

[Copy script](javascript:void(0);)

```text
0127+098
0000-876
-128+654
```

The CharacterCount property specifies that four characters are interpreted as one channel value:

[Copy script](javascript:void(0);)

```text
Dim oBlock: Set oBlock = File.GetFixedWidthBlock
Dim oChannelGroup: Set oChannelGroup = Root.ChannelGroups.Add("Channelgroup")
          
Dim oChn1  : Set oChn1  = oBlock.Channels.Add("Channel1", eI32)
oChn1.Formatter.CharacterCount = 4
oChn1.Formatter.SampleWidth = 2
Call oChannelGroup.Channels.AddDirectAccessChannel(oChn1)

Dim oChn2  : Set oChn2  = oBlock.Channels.Add("Channel2", eI32)
oChn2.Formatter.CharacterCount = 4
oChn2.Formatter.SampleWidth = 2
Call oChannelGroup.Channels.AddDirectAccessChannel(oChn2)

oBlock.Position = File.Position
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_characterformat_iformatter.htm language=enus -->
## TOPIC 00144: Property: CharacterFormat for Formatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_characterformat_iformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_characterformat_iformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: CharacterFormat for Formatter

Property: CharacterFormat for Formatter

Specifies the coding for interpreting the strings in the file.

```text
Object.CharacterFormat
```

| Object | FormatterObject with this property |  |
| --- | --- | --- |
| Object.CharacterFormat | Enumeration with read and write access and the following selection terms: 0eUTF16 16-bit characters that allow Asian characters, for example. 1eANSI Extended ASCII character set (8-bit). 3eSJIS Shift-JIS character set for the Japanese language. 4eUTF8 8-bit character set commonly used for encoding English texts. |  |
| 0 | eUTF16 | 16-bit characters that allow Asian characters, for example. |
| 1 | eANSI | Extended ASCII character set (8-bit). |
| 3 | eSJIS | Shift-JIS character set for the Japanese language. |
| 4 | eUTF8 | 8-bit character set commonly used for encoding English texts. |

|  | Note If you do not specify the coding, it is specified automatically. The first two bytes in the file are checked. If the first two bytes contain 0xFEFF, this indicates UTF16 coding. |
| --- | --- |

The following example reads a text channel. The text is UTF16-coded:

[Copy script](javascript:void(0);)

```text
File.Formatter.TrimCharacters = " "
File.Formatter.LineFeeds = vbNewLine
File.Formatter.Delimiters = ";"
File.Formatter.CharacterFormat = eUTF16
Dim oBlock: Set oBlock = File.GetStringBlock()
Dim oChn  : Set oChn = oBlock.Channels.Add("Texts", eString)
Dim oMyGrp: Set oMyGrp = Root.ChannelGroups.Add("MyChannelGroup")
Call oMyGrp.Channels.AddDirectAccessChannel(Channel)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_children_iusielement.htm language=enus -->
## TOPIC 00145: Property: Children for Element <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_children_iusielement.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_children_iusielement.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Children for Element <DataPlugin>

Property: Children for Element <DataPlugin>

Contains the StoreElements collection associated with an Element object.

StoreElements object with read access.

```text
Set oElements = Object.Children
```

| Object | Element <DataPlugin>Object with this property |
| --- | --- |
| oElements | Elements <DataPlugin>Returned object |

The following example transfers the information in the FromStore object about channel groups and about channels, into the structure of the TDM data model:

[Copy script](javascript:void(0);)

```text
Sub ReadStore(FromStore) 
  Call FindAndCreateGroups(FromStore.Children) 
End Sub 

Sub FindAndCreateGroups(StoreElements) 
  Dim StoreElement 
  Dim TDMGroup 
  For Each StoreElement in StoreElements 
    If StoreElement.IsKindOf(eStoreChannelGroup) Then 
      Set TDMGroup = Root.ChannelGroups.Add(StoreElement.Name) 
      Call TDMGroup.Properties.AddProperties(StoreElement.Properties) 
      Call CreateChannels(StoreElement, TDMGroup) 
    Else 
      Call FindAndCreateGroups(StoreElement.Children) 
    End If 
  Next 
End Sub 

Sub CreateChannels(StoreGroup, TDMGroup) 
  Dim StoreChannel 
  For Each StoreChannel In StoreGroup.Channels 
    Call TDMGroup.Channels.AddStoreChannel(StoreChannel) 
  Next 
End Sub
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_store.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_children_iusisimplifiedstore.htm language=enus -->
## TOPIC 00146: Property: Children for Store

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_children_iusisimplifiedstore.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_children_iusisimplifiedstore.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Children for Store

Property: Children for Store

Contains the StoreElements collection associated with a Store object.

StoreElements object with read access.

```text
Set oElements = Object.Children
```

| Object | StoreObject with this property |
| --- | --- |
| oElements | Elements <DataPlugin>Returned object |

The following example transfers the information about channel groups in the FromStore object, into the TDM data model structure:

[Copy script](javascript:void(0);)

```text
Sub ReadStore(FromStore) 
  Call FindAndCreateGroups(FromStore.Children) 
End Sub 

Sub FindAndCreateGroups(StoreElements) 
  Dim StoreElement 
  Dim TDMGroup 
  For Each StoreElement in StoreElements 
    If StoreElement.IsKindOf(eStoreChannelGroup) Then 
      Set TDMGroup = Root.ChannelGroups.Add(StoreElement.Name) 
      Call TDMGroup.Properties.AddProperties(StoreElement.Properties) 
    Else 
      Call FindAndCreateGroups(StoreElement.Children) 
    End If 
  Next 
End Sub 
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_store.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_column_iexcelposition.htm language=enus -->
## TOPIC 00147: Property: Column for CellPosition

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_column_iexcelposition.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_column_iexcelposition.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Column for CellPosition

Property: Column for CellPosition

Specifies the column number of a cell in a worksheet.

```text
Object.Column
```

| Object | CellPositionObject with this property |
| --- | --- |
| Object.Column | LongInteger with read access |

The following example reads in the values of the first worksheet columnwise from the first row of the first column and saves the values in channels of the first channel group:

[Copy script](javascript:void(0);)

```text
Dim oCurrSheet
Set oCurrSheet = Workbook.Sheets(1)
Dim oCellBlock
Set oCellBlock = oCurrSheet.GetCellBlock(1,1)

Dim i, oNewChannel
For i = 1 to oCurrSheet.MaxPosition.Column
  Set oNewChannel = oCellBlock.Channels.Add("ExcelRow_"&i) 
  Call Root.ChannelGroups(1).Channels.AddDirectAccessChannel(oNewChannel)
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_commentsign_iformatter.htm language=enus -->
## TOPIC 00148: Property: CommentSign for Formatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_commentsign_iformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_commentsign_iformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: CommentSign for Formatter

Property: CommentSign for Formatter

Specifies the characters that mark comment lines in the file. These characters must be at the start of the line.

Comment lines are skipped when the file is read.

```text
Object.CommentSign
```

| Object | FormatterObject with this property |
| --- | --- |
| Object.CommentSign | String with read and write access |

|  | Note When the file is read in, the characters are case sensitive. For example, if you enter the identifier REM, a line marked Rem is not skipped when being read. |
| --- | --- |

The following example shows the settings required for reading the lines listed below:

[Copy script](javascript:void(0);)

```text
 MyMeasurementData¶
rem generation specification for implicit channel¶
XAxis; 1.000.000; 2.000; 301¶
```

The CommentSign property specifies the characters that identify comment lines.

[Copy script](javascript:void(0);)

```text
File.Formatter.TrimCharacters = " "
File.Formatter.LineFeeds  = vbNewLine
File.Formatter.Delimiters = ";"
File.Formatter.CommentSign= "rem"
Dim MeasName    : MeasName    = File.GetNextStringValue(eString()
Call File.SkipLine()
Dim ChannelName : ChannelName = File.GetNextStringValue(eString)
Dim StartValue  : StartValue  = File.GetNextStringValue(eI32)
Dim Increment   : Increment   = File.GetNextStringValue(eI32)
Dim ChannelSize : ChannelSize = File.GetNextStringValue(eI32)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_count_idocumentreadproperties.htm language=enus -->
## TOPIC 00149: Property: Count for DocumentProperties <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_count_idocumentreadproperties.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_count_idocumentreadproperties.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Count for DocumentProperties <DataPlugin>

Property: Count for DocumentProperties <DataPlugin>

Returns the number of meta properties of a document. A document might be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file.

```text
Object.Count
```

| Object | DocumentProperties <DataPlugin>Object with this property |
| --- | --- |
| Object.Count | LongInteger with read access |

The following example transfers the names and values of a document's meta properties into the data set properties:

[Copy script](javascript:void(0);)

```text
Dim oMyProperties, i
Set oMyProperties = Document.Properties
For i = 1 to oMyProperties.Count 
  Call Root.Properties.Add(oMyProperties(i).Name, oMyProperties(i).Value)
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_documents.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_count_iexceldachannels.htm language=enus -->
## TOPIC 00150: Property: Count for DirectCellChannels

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_count_iexceldachannels.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_count_iexceldachannels.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Count for DirectCellChannels

Property: Count for DirectCellChannels

Returns the number of elements in a DirectCellChannels collection.

```text
Object.Count
```

| Object | DirectCellChannelsObject with this property |
| --- | --- |
| Object.Count | LongInteger with read access |

The following example creates two channels for a CellBlock and inserts these DirectAccess channels into the MyChannelGroup channel group:

[Copy script](javascript:void(0);)

```text
Dim oCellBlock   : Set oCellBlock = Workbook.Sheets(1).GetCellBlock(1,1)
Call oCellBlock.Channels.Add("Channel1",eI32)
Call oCellBlock.Channels.Add("Channel2",eI32)
Dim ChannelGroup : Set ChannelGroup = Root.ChannelGroups.Add("MyChannelGroup")
Dim i
For i = 1 to oCellBlock.Channels.Count
 Call ChannelGroup.Channels.AddDirectAccessChannel(oCellBlock.Channels.Item(i))
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_currentscriptpath_idataplugin.htm language=enus -->
## TOPIC 00151: Property: CurrentScriptPath for DataPlugin

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_currentscriptpath_idataplugin.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_currentscriptpath_idataplugin.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: CurrentScriptPath for DataPlugin

Property: CurrentScriptPath for DataPlugin

Specifies the path of the script file which belongs to the currently executed DataPlugin.

```text
Object.CurrentScriptPath
```

| Object | DataPluginObject with this property |
| --- | --- |
| Object.CurrentScriptPath | String with read access |

The following example saves the path of the executed DataPlugin as a root property:

[Copy script](javascript:void(0);)

```text
Call Root.Properties.Add("ScriptPath",CurrentScriptPath)
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_custom_idocumentproperty.htm language=enus -->
## TOPIC 00152: Property: Custom for DocumentProperty <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_custom_idocumentproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_custom_idocumentproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Custom for DocumentProperty <DataPlugin>

Property: Custom for DocumentProperty <DataPlugin>

Specifies whether a meta property of a document is a custom property. Custom properties are user-defined meta properties of a document. A document can be an Office file in XML format, a PDF, JPEG, PNG, or TIFF file.

```text
Object.Custom
```

| Object | DocumentProperty <DataPlugin>Object with this property |
| --- | --- |
| Object.Custom | Boolean value with read access |

The following example transfers the names and values of all custom properties of a document into the data set properties:

[Copy script](javascript:void(0);)

```text
Dim oMyProp
For each oMyProp in Document.Properties
  If oMypPop.Custom Then
    Call Root.Properties.Add("Custom_"&oMyProp.Name, oMyProp.Value)
  End If
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_documents.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_datatype_ibinarychannelformatter.htm language=enus -->
## TOPIC 00153: Property: DataType for BinaryChannelFormatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_datatype_ibinarychannelformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_datatype_ibinarychannelformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: DataType for BinaryChannelFormatter

Property: DataType for BinaryChannelFormatter

Specifies the data type of a DirectAccess channel that is associated with a BinaryBlock.

```text
Object.DataType
```

| Object | BinaryChannelFormatterObject with this property |  |
| --- | --- | --- |
| Object.DataType | Returns the data type.Enumeration with read access and the following selection terms: 0 eNoType Not defined 1 eI8 8-bit integer values 2 eI16 16-bit integer values 3 eI32 32-bit integer values 4 eI64 64-bit integer values 5 eByte Byte 6 eU16 16-bit unsigned integer 7 eU32 32-bit unsigned integer 8 eU64 64-bit unsigned integer 9 eR32 32-bit real values 10 eR64 64-bit real values 23 eString Text 24 eEnum Enumeration 30 eTime Time values |  |
| 0 | eNoType | Not defined |
| 1 | eI8 | 8-bit integer values |
| 2 | eI16 | 16-bit integer values |
| 3 | eI32 | 32-bit integer values |
| 4 | eI64 | 64-bit integer values |
| 5 | eByte | Byte |
| 6 | eU16 | 16-bit unsigned integer |
| 7 | eU32 | 32-bit unsigned integer |
| 8 | eU64 | 64-bit unsigned integer |
| 9 | eR32 | 32-bit real values |
| 10 | eR64 | 64-bit real values |
| 23 | eString | Text |
| 24 | eEnum | Enumeration |
| 30 | eTime | Time values |

The following example creates a new channel property that contains the data type of the channel for all DirectAccess channels:

[Copy script](javascript:void(0);)

```text
Dim oMyChn
For Each oMyChn in oBlock.Channels
  If oMyChn.Formatter.IsKindOf(eStringBlock) Then
    Call oMyChn.Properties.Add("StringBlock", oMyChn.Formatter.DataType)
  ElseIf oMyChn.Formatter.IsKindOf(eBinaryBlock) Then
    Call oMyChn.Properties.Add("BinaryBlock", oMyChn.Formatter.DataType)
  ElseIf oMyChn.Formatter.IsKindOf(eFixedWidthBlock) Then
    Call oMyChn.Properties.Add("FixedWidthBlock", oMyChn.Formatter.DataType)
  ElseIf oMyChn.Formatter.IsKindOf(eCellBlock) Then
    Call oMyChn.Properties.Add("CellBlock", oMyChn.Formatter.DataType)
  End If
Next
```

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_datatype_ifixedwidthchannelformatter.htm language=enus -->
## TOPIC 00154: Property: DataType for FixedWidthChannelFormatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_datatype_ifixedwidthchannelformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_datatype_ifixedwidthchannelformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: DataType for FixedWidthChannelFormatter

Property: DataType for FixedWidthChannelFormatter

Specifies the data type of a DirectAccess channel that is associated with a FixedWidthBlock.

```text
Object.DataType
```

| Object | FixedWidthChannelFormatterObject with this property |  |
| --- | --- | --- |
| Object.DataType | Returns the data type.Enumeration with read access and the following selection terms: 0 eNoType Not defined 1 eI8 8-bit integer values 2 eI16 16-bit integer values 3 eI32 32-bit integer values 4 eI64 64-bit integer values 5 eByte Byte 6 eU16 16-bit unsigned integer 7 eU32 32-bit unsigned integer 8 eU64 64-bit unsigned integer 9 eR32 32-bit real values 10 eR64 64-bit real values 23 eString Text 24 eEnum Enumeration 30 eTime Time values |  |
| 0 | eNoType | Not defined |
| 1 | eI8 | 8-bit integer values |
| 2 | eI16 | 16-bit integer values |
| 3 | eI32 | 32-bit integer values |
| 4 | eI64 | 64-bit integer values |
| 5 | eByte | Byte |
| 6 | eU16 | 16-bit unsigned integer |
| 7 | eU32 | 32-bit unsigned integer |
| 8 | eU64 | 64-bit unsigned integer |
| 9 | eR32 | 32-bit real values |
| 10 | eR64 | 64-bit real values |
| 23 | eString | Text |
| 24 | eEnum | Enumeration |
| 30 | eTime | Time values |

The following example creates a new channel property that contains the data type of the channel for all DirectAccess channels:

[Copy script](javascript:void(0);)

```text
Dim oMyChn
For Each oMyChn in oBlock.Channels
  If oMyChn.Formatter.IsKindOf(eStringBlock) Then
    Call oMyChn.Properties.Add("StringBlock", oMyChn.Formatter.DataType)
  ElseIf oMyChn.Formatter.IsKindOf(eBinaryBlock) Then
    Call oMyChn.Properties.Add("BinaryBlock", oMyChn.Formatter.DataType)
  ElseIf oMyChn.Formatter.IsKindOf(eFixedWidthBlock) Then
    Call oMyChn.Properties.Add("FixedWidthBlock", oMyChn.Formatter.DataType)
  ElseIf oMyChn.Formatter.IsKindOf(eCellBlock) Then
    Call oMyChn.Properties.Add("CellBlock", oMyChn.Formatter.DataType)
  End If
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_datatype_iimplicitchannel.htm language=enus -->
## TOPIC 00155: Property: DataType for ImplicitChannel

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_datatype_iimplicitchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_datatype_iimplicitchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: DataType for ImplicitChannel

Property: DataType for ImplicitChannel

Specifies the data type of an implicit channel.

```text
Object.DataType
```

| Object | ImplicitChannelObject with this property |  |
| --- | --- | --- |
| Object.DataType | Returns the data type.Enumeration with read access and the following selection terms: 0 eNoType Not defined 2 eI16 16-bit integer values 3 eI32 32-bit integer values 4 eI64 64-bit integer values 5 eByte Byte 6 eU16 16-bit unsigned integer 7 eU32 32-bit unsigned integer 9 eR32 32-bit real values 10 eR64 64-bit real values 23 eString Text 24 eEnum Enumeration 30 eTime Time values |  |
| 0 | eNoType | Not defined |
| 2 | eI16 | 16-bit integer values |
| 3 | eI32 | 32-bit integer values |
| 4 | eI64 | 64-bit integer values |
| 5 | eByte | Byte |
| 6 | eU16 | 16-bit unsigned integer |
| 7 | eU32 | 32-bit unsigned integer |
| 9 | eR32 | 32-bit real values |
| 10 | eR64 | 64-bit real values |
| 23 | eString | Text |
| 24 | eEnum | Enumeration |
| 30 | eTime | Time values |

The following example creates the channel property DataType for all implicit channels of the first channel group.

[Copy script](javascript:void(0);)

```text
Dim oMyChn
For Each oMyChn in Root.ChannelGroups(1).Channels
  If (oMyChn.IsKindOf(eImplicit)) Then
    Call oMyChn.Properties.Add("DataType", oMyChn.DataType)
  End If
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_datatype_iprocessedchannel.htm language=enus -->
## TOPIC 00156: Property: DataType for ProcessedChannel

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_datatype_iprocessedchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_datatype_iprocessedchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: DataType for ProcessedChannel

Property: DataType for ProcessedChannel

Returns the data type of a channel.

```text
Object.DataType
```

| Object | ProcessedChannelObject with this property |  |
| --- | --- | --- |
| Object.DataType | Returns the data type.Enumeration with read access and the following selection terms: 0 eNoType Not defined 2 eI16 16-bit integer values 3 eI32 32-bit integer values 4 eI64 64-bit integer values 5 eByte Byte 6 eU16 16-bit unsigned integer 7 eU32 32-bit unsigned integer 9 eR32 32-bit real values 10 eR64 64-bit real values 23 eString Text 24 eEnum Enumeration 30 eTime Time values |  |
| 0 | eNoType | Not defined |
| 2 | eI16 | 16-bit integer values |
| 3 | eI32 | 32-bit integer values |
| 4 | eI64 | 64-bit integer values |
| 5 | eByte | Byte |
| 6 | eU16 | 16-bit unsigned integer |
| 7 | eU32 | 32-bit unsigned integer |
| 9 | eR32 | 32-bit real values |
| 10 | eR64 | 64-bit real values |
| 23 | eString | Text |
| 24 | eEnum | Enumeration |
| 30 | eTime | Time values |

The following example generates a new MyChannel channel in the Measurements channel group. The new channel contains the values added rowwise of the second, third, and fourth channels of the Measurements channel group. The example generates for this channel the channel property MyDataType.

[Copy script](javascript:void(0);)

```text
Dim oChannelGroup, oProcessedChn, i
Set oChannelGroup = Root.ChannelGroups("Measurements")
Set oProcessedChn = oChannelGroups.Channels.AddProcessedChannel("MyChannel",eR64,eAddProcessor)
Call oProcessedChn.Properties.Add("MyDataType", oProcessedChn.DataType)
For i = 2 to 4
  Call oProcessedChn.Channels.Add(oChannelGroup.Channels(i))
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_default_iproperty.htm language=enus -->
## TOPIC 00157: Property: Default for Property <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_default_iproperty.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_default_iproperty.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Default for Property <DataPlugin>

Property: Default for Property <DataPlugin>

Specifies whether a property is a [base property](../objects/dataplugin_default_properties.htm).

```text
Object.Default
```

| Object | Property <DataPlugin>Object with this property |
| --- | --- |
| Object.Default | LongInteger with read accessThe value is TRUE if the property is a base property. |

The following example checks all properties of the Root object and deletes the value of this property if it is not a base property:

[Copy script](javascript:void(0);)

```text
Dim oMyProp
For Each oMyProp in Root.Properties
  If not oMyProp.Default Then
    oMyProp.Value = ""
  End If
Next
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_delimiters_iformatter.htm language=enus -->
## TOPIC 00158: Property: Delimiters for Formatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_delimiters_iformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_delimiters_iformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Delimiters for Formatter

Property: Delimiters for Formatter

Specifies the characters that separate values or text in the file.

```text
Object.Delimiters
```

| Object | FormatterObject with this property |
| --- | --- |
| Object.Delimiters | String with read and write access |

|  | Note The specified characters are not a string; they are a list of single characters. |
| --- | --- |

The following example shows the settings required for reading the lines listed below:

[Copy script](javascript:void(0);)

```text
 XAxis; 1.000.000; 2.000; 301¶
```

The Delimiters property interprets a semicolon as a delimiter between two values.

[Copy script](javascript:void(0);)

```text
File.Formatter.TrimCharacters = " "
File.Formatter.LineFeeds = vbNewLine
File.Formatter.Delimiters = ";"
File.Formatter.ThousandSeparator = "."
Dim ChannelName : ChannelName = File.GetNextStringValue(eString)
Dim StartValue  : StartValue  = File.GetNextStringValue(eI32)
Dim Increment   : Increment   = File.GetNextStringValue(eI32)
Dim ChannelSize : ChannelSize = File.GetNextStringValue(eI32)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_exponentseparator_iformatter.htm language=enus -->
## TOPIC 00159: Property: ExponentSeparator for Formatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_exponentseparator_iformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_exponentseparator_iformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: ExponentSeparator for Formatter

Property: ExponentSeparator for Formatter

Specifies the exponential character used in the file.

```text
Object.ExponentSeparator
```

| Object | FormatterObject with this property |
| --- | --- |
| Object.ExponentSeparator | String with read and write access |

The following example shows the settings required for reading the lines listed below:

[Copy script](javascript:void(0);)

```text
 15.12.1998 12:00:00; 2.84529E-04¶
15.01.1999 12:00:00; 1.05914E-04¶
14.02.1999 12:00:00; 2.84483E-04¶
16.03.1999 12:00:00; 4.72043E-04¶
16.04.1999 12:00:00; 5.47222E-04¶
16.05.1999 12:00:00; 0.00010¶
16.06.1999 12:00:00; 0.00012¶
16.07.1999 12:00:00; 0.00015¶
```

The ExponentSeparator property defines an E as the exponential character:

[Copy script](javascript:void(0);)

```text
File.Formatter.TrimCharacters = " "
File.Formatter.LineFeeds  = vbNewLine
File.Formatter.Delimiters = ";"
File.Formatter.Timeformat = "DD.MM.YYYY hh:mm:ss"
File.Formatter.DecimalPoint = "."
File.Formatter.ExponentSeparator = "E"

Dim oGrp  : Set oGrp = Root.ChannelGroups.Add("Measurements")
Dim oBlock: Set oBlock = File.GetStringBlock()
Dim oChn  : Set oChn = oBlock.Channels.Add("Time", eTime)
oGrp.Channels.AddDirectAccessChannel(oChn)
Set oChn = oBlock.Channels.Add("YShift", eR64)
oGrp.Channels.AddDirectAccessChannel(oChn)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_extension_ifileinfo.htm language=enus -->
## TOPIC 00160: Property: Extension for Info

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_extension_ifileinfo.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_extension_ifileinfo.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Extension for Info

Property: Extension for Info

Returns the filename extension of the processed file.

```text
Object.Extension
```

| Object | InfoObject with this property |
| --- | --- |
| Object.Extension | String with read access |

The following example saves the filename extension of the edited file as a root property:

[Copy script](javascript:void(0);)

```text
Call Root.Properties.Add("File extension", File.Info.Extension)
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_factor_ichannel.htm language=enus -->
## TOPIC 00161: Property: Factor for Channel <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_factor_ichannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_factor_ichannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Factor for Channel <DataPlugin>

Property: Factor for Channel <DataPlugin>

Specifies the factor that the read value is multiplied by.

This property, used with the [Offset](../properties/dataplugin_property_offset_ichannel.htm) property, can be used to calibrate values as they are read in. The formula for conversion is as follows:

Value = Factor*File value + Offset.

```text
Object.Factor
```

| Object | Channel <DataPlugin>Object with this property |
| --- | --- |
| Object.Factor | Double with read and write access |

|  | Note The properties Factor and Offset are ignored when text channels and time channels are read. For all other channel types, the conversion formula returns a Real result. |
| --- | --- |

The following example creates a new channel group with one channel. When the channel values are read, each value is first multiplied by the factor 2, and then the offset 5 is added.

[Copy script](javascript:void(0);)

```text
Dim oMyGrp : Set oMyGrp = Root.ChannelGroups.Add("MyChannelGroup")
Dim oMyChn : Set oMyChn = oMyGrp.Channels.Add("MyChannelNum",eR32)
oMyChn.Factor = 2
oMyChn.Offset = 5
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_factor_idirectaccesschannel.htm language=enus -->
## TOPIC 00162: Property: Factor for DirectAccessChannel

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_factor_idirectaccesschannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_factor_idirectaccesschannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Factor for DirectAccessChannel

Property: Factor for DirectAccessChannel

Specifies the factor that the read value is multiplied by.

This property, used with the [Offset](../properties/dataplugin_property_offset_idirectaccesschannel.htm) property, can be used to calibrate values as they are read in. The formula for conversion is as follows:

Value = Factor*File value + Offset.

```text
Object.Factor
```

| Object | DirectAccessChannelObject with this property |
| --- | --- |
| Object.Factor | Double with read and write access |

|  | Note The properties Factor and Offset are ignored when text channels and time channels are read. For all other channel types, the conversion formula returns a Real result. |
| --- | --- |

The following example creates a new channel group with a DirectAccess channel. When the channel values are read, each value is first multiplied by the factor 2, and then the offset 5 is added.

[Copy script](javascript:void(0);)

```text
Dim oBlock: Set oBlock = File.GetBinaryBlock()
Dim oChn  : Set oChn   = oBlock.Channels.Add("MyChannel",eI32)
Dim oMyGrp: Set oMyGrp = Root.ChannelGroups.Add("MyChannelGroup") 
Dim oMyChn: Set oMyChn = oMyGrp.Channels.AddDirectAccessChannel(oChn)
oMyChn.Factor = 2
oMyChn.Offset = 5
```

#### See Also

[Root Object Overview](../objects/idataplugin_objects_overview.htm) | [File Object Overview](../objects/idataplugin_objects_overview_file.htm) | [Workbook Object Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_factor_iprocessedchannel.htm language=enus -->
## TOPIC 00163: Property: Factor for ProcessedChannel

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_factor_iprocessedchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_factor_iprocessedchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Factor for ProcessedChannel

Property: Factor for ProcessedChannel

Specifies the factor that the read value is multiplied by.

This property, used with the [Offset](../properties/dataplugin_property_offset_iprocessedchannel.htm) property, can be used to calibrate values as they are read in. The formula for conversion is as follows:

Value = Factor*File value + Offset.

```text
Object.Factor
```

| Object | ProcessedChannelObject with this property |
| --- | --- |
| Object.Factor | Double with read and write access |

|  | Note The properties Factor and Offset are ignored when text channels and time channels are read. For all other channel types, the conversion formula returns a Real result. |
| --- | --- |

The following example generates a new MyChannel channel in the Measurements channel group. The new channel contains the values added rowwise of the second, third, and fourth channels of the Measurements channel group. Each value of the MyChannel channel is also multiplied by the factor 2 and then the offset 5 is added.

[Copy script](javascript:void(0);)

```text
Dim oChannelGroup, oProcessedChn, i
Set oChannelGroup = Root.ChannelGroups("Measurements")
Set oProcessedChn = oChannelGroups.Channels.AddProcessedChannel("MyChannel",eR64,eAddProcessor)
oProcessedChn.Factor = 2
oProcessedChn.Offset = 5
For i = 2 to 4
  Call oProcessedChn.Channels.Add(oChannelGroup.Channels(i))
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_fileinfo_iexcelfileio.htm language=enus -->
## TOPIC 00164: Property: FileInfo for Workbook

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_fileinfo_iexcelfileio.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_fileinfo_iexcelfileio.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: FileInfo for Workbook

Property: FileInfo for Workbook

Returns the FileInfo object that contains information about the workbook that the DataPlugin is currently processing.

```text
Set oInfo = Object.FileInfo
```

| Object | WorkbookObject with this property |
| --- | --- |
| oInfo | InfoReturned object |

The following example saves the name of the edited file as a root property:

[Copy script](javascript:void(0);)

```text
Call Root.Properties.Add("Filename", Workbook.FileInfo.FileName)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_fileinfo_iusisimplifiedstore.htm language=enus -->
## TOPIC 00165: Property: FileInfo for Store

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_fileinfo_iusisimplifiedstore.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_fileinfo_iusisimplifiedstore.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: FileInfo for Store

Property: FileInfo for Store

Returns the FileInfo object that contains information about the file that the DataPlugin is currently processing.

```text
Set oInfo = Object.FileInfo
```

| Object | StoreObject with this property |
| --- | --- |
| oInfo | InfoReturned object |

The following example saves the name of the edited file as a root property:

[Copy script](javascript:void(0);)

```text
Call Root.Properties.Add("Filename", FromStore.FileInfo.FileName)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_store.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_filepath_idocumentroot.htm language=enus -->
## TOPIC 00166: Property: FilePath for Document <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_filepath_idocumentroot.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_filepath_idocumentroot.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: FilePath for Document <DataPlugin>

Property: FilePath for Document <DataPlugin>

Returns the absolute path of a document. A document might be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file.

```text
Object.FilePath
```

| Object | Document <DataPlugin>Object with this property |
| --- | --- |
| Object.FilePath | String with read access |

The following example creates the data set property DocumentFilePath and assigns the absolute path of the document to this property:

[Copy script](javascript:void(0);)

```text
Call Root.Properties.Add("DocumentFilePath",Document.FilePath)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_documents.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_filetype_idocumentroot.htm language=enus -->
## TOPIC 00167: Property: FileType for Document <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_filetype_idocumentroot.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_filetype_idocumentroot.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: FileType for Document <DataPlugin>

Property: FileType for Document <DataPlugin>

Returns the data type of a document. A document may be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file, which uses XMP.

```text
Object.FileType
```

| Object | Document <DataPlugin>Object with this property |  |
| --- | --- | --- |
| Object.FileType | Enumeration with read access and the following selection terms: 1eDocumentTypeXMP XMP file (for example *.pdf; *.jpg; *.jpeg; *.png; *.tif; *.tiff) 2eDocumentTypeWord XML based Word file (for example *.docx; *.docm; *.dotx; *.dotm) 3eDocumentTypeExcel XML based Excel file (for example *.xlsx; *.xltm; *.xltx; *.xltm) 4eDocumentTypePowerPoint XML based PowerPoint file (for example *.pptx; *.pptm; *.potx; *.potm) |  |
| 1 | eDocumentTypeXMP | XMP file (for example *.pdf; *.jpg; *.jpeg; *.png; *.tif; *.tiff) |
| 2 | eDocumentTypeWord | XML based Word file (for example *.docx; *.docm; *.dotx; *.dotm) |
| 3 | eDocumentTypeExcel | XML based Excel file (for example *.xlsx; *.xltm; *.xltx; *.xltm) |
| 4 | eDocumentTypePowerPoint | XML based PowerPoint file (for example *.pptx; *.pptm; *.potx; *.potm) |

The following example creates the data set property DocumentFileType and assigns the data type of the document to this property:

[Copy script](javascript:void(0);)

```text
Call Root.Properties.Add("DocumentFileType",Document.FileType)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_documents.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_formatter_idirectaccesschannel.htm language=enus -->
## TOPIC 00168: Property: Formatter for DirectAccessChannel

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_formatter_idirectaccesschannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_formatter_idirectaccesschannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Formatter for DirectAccessChannel

Property: Formatter for DirectAccessChannel

Contains information about how the values of a DirectAccess channel are represented.

```text
Set oAbstractChannelFormatter = Object.Formatter
```

| Object | DirectAccessChannelObject with this property |
| --- | --- |
| oAbstractChannelFormatter | AbstractChannelFormatterReturned object |

The following example interprets the first byte as the higher-value byte when the values of the MyChannel are read.

[Copy script](javascript:void(0);)

```text
Dim oBinBlock : Set oBinBlock = File.GetBinaryBlock()
Dim oChn : Set oChn = oBinBlock.Channels.Add("MyChannel",eI16)
oChn.Formatter.ByteOrder = eBigEndian
Dim oMyGrp: Set oMyGrp = Root.ChannelGroups.Add("MyChannelGroup")
Call oMyGrp.Channels.AddDirectAccessChannel(oChn)
```

#### See Also

[Root Object Overview](../objects/idataplugin_objects_overview.htm) | [File Object Overview](../objects/idataplugin_objects_overview_file.htm) | [Workbook Object Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_formatter_imeasurementfileio.htm language=enus -->
## TOPIC 00169: Property: Formatter for File

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_formatter_imeasurementfileio.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_formatter_imeasurementfileio.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Formatter for File

Property: Formatter for File

Returns the Formatter object that contains information about the format of the file that the DataPlugin is currently processing.

```text
Set oFormatter = Object.Formatter
```

| Object | FileObject with this property |
| --- | --- |
| oFormatter | FormatterReturned object |

The following example sets the Formatter object properties that are required for reading the following values:

[Copy script](javascript:void(0);)

```text
28.06.2004 16:28:20; 0,001234¶
28.06.2004 16:28:21; 0,002398¶
28.06.2004 16:28:22; 0,001296¶
28.06.2004 16:28:23; 0,001628¶
28.06.2004 16:28:24; 0,001683¶

File.Formatter.TrimCharacters = " "
File.Formatter.LineFeeds  = vbNewLine
File.Formatter.TimeFormat = "DD.MM.YYYY hh:mm:ss"
File.Formatter.Delimiters = ";"
File.Formatter.DecimalPoint = ","
Dim ValueTime, Value
While (File.Position <> File.Size)
  Set ValueTime = File.GetNextStringValue(eTime)
  Value = File.GetNextStringValue(eR64)
  Call File.SkipLine()
Wend
```

#### See Also

[Object overview](../objects/idataplugin_objects_overview_file.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_fullpath_ifileinfo.htm language=enus -->
## TOPIC 00170: Property: FullPath for Info

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_fullpath_ifileinfo.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_fullpath_ifileinfo.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: FullPath for Info

Property: FullPath for Info

Returns the name of the processed file, including the filename extension, and the path.

```text
Object.FullPath
```

| Object | InfoObject with this property |
| --- | --- |
| Object.FullPath | String with read access |

The following example saves the name of the edited file as a root property:

[Copy script](javascript:void(0);)

```text
Call Root.Properties.Add("Full path", File.Info.FullPath)
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_hour_iusitimedisp.htm language=enus -->
## TOPIC 00171: Property: Hour for UsiTimeDisp

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_hour_iusitimedisp.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_hour_iusitimedisp.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Hour for UsiTimeDisp

Property: Hour for UsiTimeDisp

Specifies the hours.

```text
Object.Hour
```

| Object | UsiTimeDispObject with this property |
| --- | --- |
| Object.Hour | Integer with read and write access |

The following example generates an object with the time value 17.06.2004 10:20:30 and saves the current hours as a root property:

[Copy script](javascript:void(0);)

```text
Dim oMyTime: Set oMyTime = CreateTime(2004,6,17,10,20,30,0,0,0)
Call Root.Properties.Add("Hour", oMyTime.Hour)
```

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_ignoreemptylines_iformatter.htm language=enus -->
## TOPIC 00172: Property: IgnoreEmptyLines for Formatter

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_ignoreemptylines_iformatter.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_ignoreemptylines_iformatter.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: IgnoreEmptyLines for Formatter

Property: IgnoreEmptyLines for Formatter

Specifies whether the empty lines in the file are ignored.

If the value of the property is FALSE, empty lines are interpreted as NULL when channel values are read.

```text
Object.IgnoreEmptyLines
```

| Object | FormatterObject with this property |
| --- | --- |
| Object.IgnoreEmptyLines | Boolean with read and write access |

The following example shows the settings required for reading the lines listed below:

[Copy script](javascript:void(0);)

```text
 MyMeasurementData¶
¶
XAxis; 1.000.000; 2.000; 301¶
```

The IgnoreEmptyLines property ignores the empty line.

[Copy script](javascript:void(0);)

```text
File.Formatter.TrimCharacters = " "
File.Formatter.LineFeeds = vbNewLine
File.Formatter.Delimiters = ";"
File.Formatter.IgnoreEmptyLines = TRUE
Dim MeasName    : MeasName    = File.GetNextStringValue(eString)
Call File.SkipLine()
Dim ChannelName : ChannelName = File.GetNextStringValue(eString)
Dim StartValue  : StartValue  = File.GetNextStringValue(eI32)
Dim Increment   : Increment   = File.GetNextStringValue(eI32)
Dim ChannelSize : ChannelSize = File.GetNextStringValue(eI32)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_file.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_increment_iimplicitchannel.htm language=enus -->
## TOPIC 00173: Property: Increment for ImplicitChannel

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_increment_iimplicitchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_increment_iimplicitchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Increment for ImplicitChannel

Property: Increment for ImplicitChannel

Specifies the step width for generating the data of an implicit channel.

```text
Object.Increment
```

| Object | ImplicitChannelObject with this property |
| --- | --- |
| Object.Increment | Variant with read and write access |

The following example reads in the generation instruction of an implicit channel and then generates this channel within the channel group MyChnGroup:

[Copy script](javascript:void(0);)

```text
Dim ChannelName: ChannelName = File.GetNextStringValue(eString)
Dim StartValue : StartValue  = File.GetNextStringValue(eString)
Dim Increment  : Increment   = File.GetNextStringValue(eString)
Dim ChannelSize: ChannelSize = File.GetNextStringValue(eString)
Dim ChannelGroup : Set ChannelGroup = Root.ChannelGroupsAdd("MyChnGroup")
Call ChannelGroup.Channels.AddImplicitChannel(ChannelName, StartValue, Increment, ChannelSize, eI32)
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_index_idirectaccesschannel.htm language=enus -->
## TOPIC 00174: Property: Index for DirectAccessChannel

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_index_idirectaccesschannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_index_idirectaccesschannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Index for DirectAccessChannel

Property: Index for DirectAccessChannel

Specifies the position of the DirectAccess channel in the block.

```text
Object.Index
```

| Object | DirectAccessChannelObject with this property |
| --- | --- |
| Object.Index | LongInteger with read access |

|  | Note Use the Channels.Swap method to change the position of a DirectAccessChannel in the block. |
| --- | --- |

#### See Also

[Root Object Overview](../objects/idataplugin_objects_overview.htm) | [File Object Overview](../objects/idataplugin_objects_overview_file.htm) | [Workbook Object Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_index_iexcelsheet.htm language=enus -->
## TOPIC 00175: Property: Index for Sheet

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_index_iexcelsheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_index_iexcelsheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Index for Sheet

Property: Index for Sheet

Specifies the position of the worksheet in the workbook.

```text
Object.Index
```

| Object | SheetObject with this property |
| --- | --- |
| Object.Index | LongInteger with read access |

The following example generates for each worksheet a new channel group. The channel group receives the name of the worksheet and a property which retains the position of the worksheet in the workbook.

[Copy script](javascript:void(0);)

```text
Dim i, oCurrSheet, oNewGroup
For i = 1 to Workbook.Sheets.Count
  Set oCurrSheet = Workbook.Sheets(i)
  Set oNewGroup = Root.ChannelGroups.Add(oCurrSheet.Name)
  Call NewGroup.Properties.Add("Description", "Sheet"&oCurrSheet.Index)
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_maxposition_iexcelsheet.htm language=enus -->
## TOPIC 00176: Property: MaxPosition for Sheet

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_maxposition_iexcelsheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_maxposition_iexcelsheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: MaxPosition for Sheet

Property: MaxPosition for Sheet

Specifies within the worksheet the position of the cell that contains the last value.

```text
Set oCellPosition = Object.MaxPosition
```

| Object | SheetObject with this property |
| --- | --- |
| oCellPosition | CellPositionReturned object |

The following example reads in the values of the worksheet columnwise from the second row and saves the values in channels of the first channel group:

[Copy script](javascript:void(0);)

```text
Dim oCurrSheet
Set oCurrSheet = Workbook.Sheets(1)
Dim oCellBlock
Set oCellBlock = oCurrSheet.GetCellBlock(2,1)

Dim i, Name, oNewChannel
For i = 1 to oCurrSheet.MaxPosition.Column
  Name = oCurrSheet.GetCellValue(1,i)
  Set oNewChannel = oCellBlock.Channels.Add(Name) 
  Call Root.ChannelGroups(1).Channels.AddDirectAccessChannel(oNewChannel)
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_microsecond_iusitimedisp.htm language=enus -->
## TOPIC 00177: Property: Microsecond for UsiTimeDisp

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_microsecond_iusitimedisp.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_microsecond_iusitimedisp.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Microsecond for UsiTimeDisp

Property: Microsecond for UsiTimeDisp

Specifies the microseconds.

```text
Object.Microsecond
```

| Object | UsiTimeDispObject with this property |
| --- | --- |
| Object.Microsecond | Integer with read and write access |

The following example creates an object with the time value 17.06.2004 10:20:30. The number of microseconds is 40. The example then saves the current microseconds as a root property:

[Copy script](javascript:void(0);)

```text
Dim oMyTime: Set oMyTime = CreateTime(2004,6,17,10,20,30,0,40,0)
Call Root.Properties.Add("Microsecond", oMyTime.Microsecond)
```

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_millisecond_iusitimedisp.htm language=enus -->
## TOPIC 00178: Property: Millisecond for UsiTimeDisp

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_millisecond_iusitimedisp.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_millisecond_iusitimedisp.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Millisecond for UsiTimeDisp

Property: Millisecond for UsiTimeDisp

Specifies the milliseconds.

```text
Object.Millisecond
```

| Object | UsiTimeDispObject with this property |
| --- | --- |
| Object.Millisecond | Integer with read and write access |

The following example creates an object with the time value 17.06.2004 10:20:30. The number of milliseconds is 50. The example then saves the current microseconds as a root property:

[Copy script](javascript:void(0);)

```text
Dim oMyTime: Set oMyTime = CreateTime(2004,6,17,10,20,30,50,0,0)
Call Root.Properties.Add("Microsecond", oMyTime.Microsecond)
```

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_minposition_iexcelsheet.htm language=enus -->
## TOPIC 00179: Property: MinPosition for Sheet

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_minposition_iexcelsheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_minposition_iexcelsheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: MinPosition for Sheet

Property: MinPosition for Sheet

Specifies within the worksheet the position of the cell that contains the first value.

```text
Set oCellPosition = Object.MinPosition
```

| Object | SheetObject with this property |
| --- | --- |
| oCellPosition | CellPositionReturned object |

The following example reads in the values of the worksheet columnwise and saves the values in channels from the first channel group:

[Copy script](javascript:void(0);)

```text
Dim oCurrSheet
Set oCurrSheet = Workbook.Sheets(1)
Dim oCellBlock
Set oCellBlock = oCurrSheet.GetCellBlock(oCurrSheet.MinPositiom.Row+1,oCurrSheet.MinPosition.Column)

Dim i, Name, oNewChannel
For i = oCurrSheet.MinPosition.Column to oCurrSheet.MaxPosition.Column
  Name = oCurrSheet.GetCellValue(oCurrSheet.MinPositiom.Row,i)
  Set oNewChannel = oCellBlock.Channels.Add(Name) 
  Call Root.ChannelGroups(1).Channels.AddDirectAccessChannel(oNewChannel)
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_minute_iusitimedisp.htm language=enus -->
## TOPIC 00180: Property: Minute for UsiTimeDisp

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_minute_iusitimedisp.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_minute_iusitimedisp.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Minute for UsiTimeDisp

Property: Minute for UsiTimeDisp

Specifies the minutes.

```text
Object.Minute
```

| Object | UsiTimeDispObject with this property |
| --- | --- |
| Object.Minute | Integer with read and write access |

The following example generates an object with the time value 17.06.2004 10:20:30 and saves the current minutes as a root property:

[Copy script](javascript:void(0);)

```text
Dim oMyTime: Set oMyTime = CreateTime(2004,6,17,10,20,30,0,0,0)
Call Root.Properties.Add("Minute", oMyTime.Minute)
```

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_month_iusitimedisp.htm language=enus -->
## TOPIC 00181: Property: Month for UsiTimeDisp

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_month_iusitimedisp.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_month_iusitimedisp.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Month for UsiTimeDisp

Property: Month for UsiTimeDisp

Specifies the month.

```text
Object.Month
```

| Object | UsiTimeDispObject with this property |
| --- | --- |
| Object.Month | Integer with read and write access |

The following example generates an object with the time value 17.06.2004 10:20:30 and saves the current month as a root property:

[Copy script](javascript:void(0);)

```text
Dim oMyTime: Set oMyTime = CreateTime(2004,6,17,10,20,30,0,0,0)
Call Root.Properties.Add("Month", oMyTime.Month)
```

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_name_iabstractchannel.htm language=enus -->
## TOPIC 00182: Property: Name for AbstractChannel

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_name_iabstractchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_name_iabstractchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Name for AbstractChannel

Property: Name for AbstractChannel

Specifies a channel name.

```text
Object.Name
```

| Object | AbstractChannelObject with this property |
| --- | --- |
| Object.Name | String with read and write access |

The following example searches for the Temp channel in all channels groups and creates the Sensor_Type channel property for this channel:

[Copy script](javascript:void(0);)

```text
Dim i, oMyChn
For i = 1 to Root.ChannelGroups.Count
  For Each oMyChn in Root.ChannelGroups(i).Channels
    If oMyChn.Name = "Temp" Then
      Call oMyChn.Properties.Add("Sensor_Type","TC-J")
    End If
  Next
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_name_ichannel.htm language=enus -->
## TOPIC 00183: Property: Name for Channel <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_name_ichannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_name_ichannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Name for Channel <DataPlugin>

Property: Name for Channel <DataPlugin>

Receives the name of a Channel object.

```text
Object.Name
```

| Object | Channel <DataPlugin>Object with this property |
| --- | --- |
| Object.Name | String with read and write access |

The following example searches for the Temp channel in all channels groups and creates the Sensor_Type channel property for this channel:

[Copy script](javascript:void(0);)

```text
Dim i, oMyChn
For i = 1 to Root.ChannelGroups.Count
  For Each oMyChn in Root.ChannelGroups(i).Channels
    If oMyChn.Name = "Temp" Then
      Call oMyChn.Properties.Add("Sensor_Type","TC-J")
    End If
  Next
Next
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_name_ichannelgroup.htm language=enus -->
## TOPIC 00184: Property: Name for ChannelGroup <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_name_ichannelgroup.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_name_ichannelgroup.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Name for ChannelGroup <DataPlugin>

Property: Name for ChannelGroup <DataPlugin>

Receives the name of a ChannelGroup object.

```text
Object.Name
```

| Object | ChannelGroup <DataPlugin>Object with this property |
| --- | --- |
| Object.Name | String with read and write access |

The following example searches for the channel group TQT_33-5_Upper and creates for this channel group the group property Test_Status:

[Copy script](javascript:void(0);)

```text
Dim oMyGrp
For Each oMyGrp in Root.ChannelGroups
  If oMyGrp.Name = "QT_33-5_Upper" Then
    Call oMyGrp.Properties.Add("Test_Status","Pass")
  End If
Next
```

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_name_idirectaccesschannel.htm language=enus -->
## TOPIC 00185: Property: Name for DirectAccessChannel

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_name_idirectaccesschannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_name_idirectaccesschannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Name for DirectAccessChannel

Property: Name for DirectAccessChannel

Specifies the name of a DirectAccessChannel object.

```text
Object.Name
```

| Object | DirectAccessChannelObject with this property |
| --- | --- |
| Object.Name | String with read and write accessYou only have read/write access until you insert the channel into a channel group. When you insert the channel, the channel name becomes the unique identifier and cannot be changed. |

#### See Also

[Root Object Overview](../objects/idataplugin_objects_overview.htm) | [File Object Overview](../objects/idataplugin_objects_overview_file.htm) | [Workbook Object Overview](../objects/idataplugin_objects_overview_excel.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_name_idocumentnamespace.htm language=enus -->
## TOPIC 00186: Property: Name for DocumentNamespace <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_name_idocumentnamespace.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_name_idocumentnamespace.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Name for DocumentNamespace <DataPlugin>

Property: Name for DocumentNamespace <DataPlugin>

Returns the name of a namespace in a document. Use namespaces to group XML elements in a document.

```text
Object.Name
```

| Object | DocumentNamespace <DataPlugin>Object with this property |
| --- | --- |
| Object.Name | String with read access |

The following example creates for each namespace of a document a data set property with the same name and assigns the number of properties in a namespace to this data set property:

[Copy script](javascript:void(0);)

```text
Dim oMyNamespace, oMyProp
For each oMyNamespace in Document.Namespaces
  Call Root.Properties.Add(oMyNamespace.Name, oMyNamespace.Properties.Count)
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_documents.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_properties_idocumentroot.htm language=enus -->
## TOPIC 00187: Property: Properties for Document <DataPlugin>

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_properties_idocumentroot.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_properties_idocumentroot.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Properties for Document <DataPlugin>

Property: Properties for Document <DataPlugin>

Returns all meta properties of a document. A document might be an Office file in XML format or a PDF, JPEG, PNG, or TIFF file.

```text
Set oDocumentProperties = Object.Properties
```

| Object | Document <DataPlugin>Object with this property |
| --- | --- |
| oDocumentProperties | DocumentProperties <DataPlugin>Returned object |

The following example transfers the names and values of a document's meta properties into the data set properties:

[Copy script](javascript:void(0);)

```text
Dim oMyProperty
For each oMyProperty in Document.Properties
  Call Root.Properties.Add(oMyProperty.Name, oMyProperty.Value)
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview_documents.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_properties_iimplicitchannel.htm language=enus -->
## TOPIC 00188: Property: Properties for ImplicitChannel

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_properties_iimplicitchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_properties_iimplicitchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Properties for ImplicitChannel

Property: Properties for ImplicitChannel

Contains the Properties collection associated with an implicit channel.

```text
Set oProperties = Object.Properties
```

| Object | ImplicitChannelObject with this property |
| --- | --- |
| oProperties | Properties <DataPlugin>Returned object |

The following example checks all channel properties of an implicit channel from the first channel group. The example creates the channel property Sensor_Type if this property does not exist.

[Copy script](javascript:void(0);)

```text
Dim oMyChn, oMyProp, bFound
For Each oMyChn in Root.ChannelGroups(1).Channels
  If oMyChn.IsKindOf(eImplicit) Then
    For Each oMyProp in oMyChn.Properties
      If oMyProp.Name = "Sensor_Type" Then
        bFound = TRUE
      End If
    Next
    If not bFound Then
      Call oMyChn.Properties.Add("Sensor_type","TC-N")
    End If
  End If
Next
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=dataplugin/properties/dataplugin_property_properties_iprocessedchannel.htm language=enus -->
## TOPIC 00189: Property: Properties for ProcessedChannel

- bundle_id: `diadem`
- source_path: `dataplugin/properties/dataplugin_property_properties_iprocessedchannel.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dataplugin/properties/dataplugin_property_properties_iprocessedchannel.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DataPlugin](../scriptdataplugin_overview.htm) > [Properties](../properties/dataplugin_properties_overview.htm) > Property: Properties for ProcessedChannel

Property: Properties for ProcessedChannel

Contains the Properties collection associated with a ProcessedChannel object.

```text
Set oProperties = Object.Properties
```

| Object | ProcessedChannelObject with this property |
| --- | --- |
| oProperties | Properties <DataPlugin>Returned object |

The following example generates a new MyChannel channel that contains the values, which are added rowwise, of the Real type DirectAccess channels. The example creates the channel property Sensor_Type if this property does not exist.

[Copy script](javascript:void(0);)

```text
Dim ChannelGroup: Set ChannelGroup = Root.ChannelGroups.Add("MyChannelGroup")
Dim ProcessedChn: Set ProcessedChn = ChannelGroup.Channels.AddProcessedChannel("MyChannel",eR64,eAddProcessor)
Dim Channel
For Each Channel in ChannelGroup.Channels
  If Channel.IsKindOf(eDirectAccess) and (Channel.DataType = eR64) Then
    Call ProcessedChn.Channels.Add(Channel)
  End If
Next

If not ProcessedChn.Properties.Exists("Sensor_type") Then
  Call ProcessedChn.Properties.Add("Sensor_type","TC-N")
End If
```

#### See Also

[Objects Overview](../objects/idataplugin_objects_overview.htm)

#### Examples

[Checking DataPlugins for Timeout](../../exploff/examples/dataplugintimeout.htm)

<!--NI_TOPIC bundle=diadem path=diamisc/methods/mqtt_method_disconnect_mqtt.htm language=enus -->
## TOPIC 00190: Method: Disconnect for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/methods/mqtt_method_disconnect_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/methods/mqtt_method_disconnect_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Disconnect for MQTT

Method: Disconnect for MQTT

Disconnects an existing connection to a MQTT broker. There is no further communication between DIAdem and the MQTT broker.

```text
Object.Disconnect
```

| Object | MQTTObject with this method |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=diamisc/methods/mqtt_method_readbinary_mqtt.htm language=enus -->
## TOPIC 00191: Method: ReadBinary for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/methods/mqtt_method_readbinary_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/methods/mqtt_method_readbinary_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: ReadBinary for MQTT

Method: ReadBinary for MQTT

Reads binary data of a topic from the MQTT broker. Before DIAdem can read data from a topic, you must subscribe to the topic using the [Subscribe](../methods/mqtt_method_subscribe_mqtt.htm) method. Use the [ReadString](../methods/mqtt_method_readstring_mqtt.htm) method to read ASCII strings.

```text
vReadBinary = Object.ReadBinary(Topic)
```

| Object | MQTTObject with this method |
| --- | --- |
| Topic | StringSpecifies the MQTT topic. |
| vReadBinary | VariantReceives the vector with the received data. |

<!--NI_TOPIC bundle=diadem path=diamisc/methods/mqtt_method_readstring_mqtt.htm language=enus -->
## TOPIC 00192: Method: ReadString for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/methods/mqtt_method_readstring_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/methods/mqtt_method_readstring_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: ReadString for MQTT

Method: ReadString for MQTT

Reads a null-terminated ASCII string of a topic from the MQTT broker. Before DIAdem can read data from a topic, you must subscribe to the topic using the [Subscribe](../methods/mqtt_method_subscribe_mqtt.htm) method. Use the [ReadBinary](../methods/mqtt_method_readbinary_mqtt.htm) method to read binary data.

```text
vReadString = Object.ReadString(Topic)
```

| Object | MQTTObject with this method |
| --- | --- |
| Topic | StringSpecifies the MQTT topic. |
| vReadString | VariantReceives the received data. |

<!--NI_TOPIC bundle=diadem path=diamisc/methods/mqtt_method_subscribe_mqtt.htm language=enus -->
## TOPIC 00193: Method: Subscribe for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/methods/mqtt_method_subscribe_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/methods/mqtt_method_subscribe_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Subscribe for MQTT

Method: Subscribe for MQTT

Subscribes to the receipt of data of a topic from the MQTT broker. A subscription is necessary in order to receive the data of a topic with the methods [ReadString](../methods/mqtt_method_readstring_mqtt.htm) or [ReadBinary](../methods/mqtt_method_readbinary_mqtt.htm).

```text
bSubscribe = Object.Subscribe(Topic)
```

| Object | MQTTObject with this method |
| --- | --- |
| Topic | StringSpecifies the MQTT topic. |
| bSubscribe | BooleanReceives the information whether the subscription was successful (TRUE) or not (FALSE). |

<!--NI_TOPIC bundle=diadem path=diamisc/methods/mqtt_method_unsubscribe_mqtt.htm language=enus -->
## TOPIC 00194: Method: Unsubscribe for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/methods/mqtt_method_unsubscribe_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/methods/mqtt_method_unsubscribe_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Unsubscribe for MQTT

Method: Unsubscribe for MQTT

Cancels the receipt of data of a topic from the MQTT broker.

```text
Object.Unsubscribe(Topic)
```

| Object | MQTTObject with this method |
| --- | --- |
| Topic | StringSpecifies the MQTT topic. |

<!--NI_TOPIC bundle=diadem path=diamisc/methods/mqtt_method_writebinary_mqtt.htm language=enus -->
## TOPIC 00195: Method: WriteBinary for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/methods/mqtt_method_writebinary_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/methods/mqtt_method_writebinary_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: WriteBinary for MQTT

Method: WriteBinary for MQTT

Sends binary data to the MQTT broker. Use the [WriteString](../methods/mqtt_method_writestring_mqtt.htm) method to send ASCII strings.

```text
Object.WriteBinary(Topic, Data)
```

| Object | MQTTObject with this method |
| --- | --- |
| Topic | StringSpecifies the MQTT topic. |
| Data | VariantSpecifies the vector with the data to be sent. |

<!--NI_TOPIC bundle=diadem path=diamisc/methods/mqtt_method_writestring_mqtt.htm language=enus -->
## TOPIC 00196: Method: WriteString for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/methods/mqtt_method_writestring_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/methods/mqtt_method_writestring_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: WriteString for MQTT

Method: WriteString for MQTT

Sends an ASCII string to the MQTT broker. Use the method [WriteBinary](../methods/mqtt_method_writebinary_mqtt.htm) to send binary data or to send strings containing characters with an ASCII value greater than 127.

```text
Object.WriteString(Topic, Data)
```

| Object | MQTTObject with this method |
| --- | --- |
| Topic | StringSpecifies the MQTT topic. |
| Data | StringSpecifies the ASCII string. |

<!--NI_TOPIC bundle=diadem path=diamisc/mqtt_overview.htm language=enus -->
## TOPIC 00197: MQTT

- bundle_id: `diadem`
- source_path: `diamisc/mqtt_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/mqtt_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

MQTT

MQTT

The subordinate topics in the tree of the help describe the object-oriented script interface of the **M**essage **Q**ueue **T**elemetry **T**ransport protocol. The MQTT protocol is an open message protocol for machine-to-machine (M2M) communication for the transmission of telemetry data between devices. Use the [CreateMQTT](../comoff/createmqtt.htm) command to create the [MQTT](../diamisc/objects/mqtt_objects_mqtt.htm) object.

The topics provide information about all objects, methods, properties, and examples that demonstrate how to use the interface.

<!--NI_TOPIC bundle=diadem path=diamisc/objects/mqtt_objects_mqtt.htm language=enus -->
## TOPIC 00198: Object: MQTT

- bundle_id: `diadem`
- source_path: `diamisc/objects/mqtt_objects_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/objects/mqtt_objects_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[MQTT](../mqtt_overview.htm) > Object: MQTT

Object: MQTT

The MQTT object provides the **M**essage **Q**ueue **T**elemetry **T**ransport Protocol in DIAdem. The MQTT protocol is an open message protocol for machine-to-machine (M2M) communication for the transmission of telemetry data between devices. The communication of the individual devices between each other occurs over the MQTT broker. The MQTT broker is not an element of DIAdem.

The MQTT communication is based on the topic principle. A topic of a sensor, for example, can look as follows: "BuildingA/Floor5/Room5A12/Temperature". The MQTT broker is familiar with the topics and permits the communication between DIAdem and various topics.

Use the command [CreateMQTT](../../comoff/createmqtt.htm) to create the MQTT object.

The following example shows a script file for the script driver that you can use to read data of a topic from an MQTT broker:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim MQTT

Sub SFD_ReadChannel(ChannelNumberP, ParamP, DataP, ErrorP)
  Dim sTemp
  Set MQTT  = CreateMQTT(DeviceParam1V)
  sTemp = MQTT.ReadString(ParamP)
  
  If isEmpty(sTemp) Then
    DataP = NoValue
  Else
    If sTemp <> "" Then
      DataP = CDbl(sTemp)
    Else
      DataP = NoValue
    End If
  End If
End Sub

Sub SFD_InitInChannel(ChannelNumberP, ParamP, ErrorP)
  Call MQTT.Subscribe(ParamP)
End Sub

Sub SFD_Init(DeviceParam1V, DeviceParam2V, ErrorP)
  Set MQTT  = CreateMQTT(DeviceParam1V)
  Call MQTT.Connect
End Sub
```

[Copy script](javascript:void(0);)

```text
def SFD_ReadChannel(ChannelNumberP, ParamP, DataP, ErrorP): 
    MQTT  = dd.CreateMQTT(DeviceParam1V) 
    sTemp = MQTT.ReadString(ParamP) 
    if len(sTemp) == 0 : 
        DataP = dd.NoValue 
    else: 
        if sTemp != "" : 
            DataP = float(sTemp) 
        else: 
            DataP = dd.NoValue 
def SFD_InitInChannel(ChannelNumberP, ParamP, ErrorP): 
    MQTT.Subscribe(ParamP) 
def SFD_Init(DeviceParam1V, DeviceParam2V, ErrorP): 
    MQTT  = dd.CreateMQTT(DeviceParam1V) 
    MQTT.Connect 
```

The following example shows a script file for the script driver that you use to write data to a topic using a MQTT broker:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim MQTT

Sub SFD_WriteChannel(ChannelNumberP, ParamP, DataP, ErrorP)
  Call MQTT.WriteString(ParamP, DataP)
End Sub

Sub SFD_Init(DeviceParam1V, DeviceParam2V, ErrorP)
  Set MQTT  = CreateMQTT(DeviceParam1V)
  MQTT.Connect
End Sub
```

[Copy script](javascript:void(0);)

```text
def SFD_WriteChannel(ChannelNumberP, ParamP, DataP, ErrorP): 
    MQTT.WriteString(ParamP, DataP) 
def SFD_Init(DeviceParam1V, DeviceParam2V, ErrorP): 
    MQTT  = dd.CreateMQTT(DeviceParam1V) 
    MQTT.Connect 
```

#### Properties

[CACertificate](../properties/mqtt_property_cacertificate_mqtt.htm) | [Certificate](../properties/mqtt_property_certificate_mqtt.htm) | [ConnectTimeout](../properties/mqtt_property_connecttimeout_mqtt.htm) | [KeyFile](../properties/mqtt_property_keyfile_mqtt.htm) | [Password](../properties/mqtt_property_password_mqtt.htm) | [Port](../properties/mqtt_property_port_mqtt.htm) | [TLSPassword](../properties/mqtt_property_tlspassword_mqtt.htm) | [UseAuthentication](../properties/mqtt_property_useauthentication_mqtt.htm) | [UserName](../properties/mqtt_property_username_mqtt.htm) | [UseTLS](../properties/mqtt_property_usetls_mqtt.htm)

#### Methods

[Connect](../methods/mqtt_method_connect_mqtt.htm) | [Disconnect](../methods/mqtt_method_disconnect_mqtt.htm) | [ReadBinary](../methods/mqtt_method_readbinary_mqtt.htm) | [ReadString](../methods/mqtt_method_readstring_mqtt.htm) | [Subscribe](../methods/mqtt_method_subscribe_mqtt.htm) | [Unsubscribe](../methods/mqtt_method_unsubscribe_mqtt.htm) | [WriteBinary](../methods/mqtt_method_writebinary_mqtt.htm) | [WriteString](../methods/mqtt_method_writestring_mqtt.htm)

<!--NI_TOPIC bundle=diadem path=diamisc/properties/mqtt_property_connecttimeout_mqtt.htm language=enus -->
## TOPIC 00199: Property: ConnectTimeout for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/properties/mqtt_property_connecttimeout_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/properties/mqtt_property_connecttimeout_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: ConnectTimeout for MQTT

Property: ConnectTimeout for MQTT

Specifies in seconds the time that elapses before DIAdem cancels an communication attempt with the MQTT broker. If you do not specify this property, DIAdem cancels the communication attempt after 5 seconds.

```text
Object.ConnectTimeout
```

| Object | MQTTObject with this property |
| --- | --- |
| Object.ConnectTimeout | LongInteger with read and write accessSpecifies in seconds the time that elapses before DIAdem cancels an communication attempt with the MQTT broker. |

<!--NI_TOPIC bundle=diadem path=diamisc/properties/mqtt_property_keyfile_mqtt.htm language=enus -->
## TOPIC 00200: Property: KeyFile for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/properties/mqtt_property_keyfile_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/properties/mqtt_property_keyfile_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: KeyFile for MQTT

Property: KeyFile for MQTT

Specifies the path to the private key file that DIAdem uses for encrypted communication with an MQTT broker. If in an encrypted data transfer the [CACertificate](../properties/mqtt_property_cacertificate_mqtt.htm), [Certificate](../properties/mqtt_property_certificate_mqtt.htm), and [KeyFile](../properties/mqtt_property_keyfile_mqtt.htm) properties are not set to valid values, DIAdem displays a dialog box where you can add these properties when you connect with the [Connect](../methods/mqtt_method_connect_mqtt.htm) method.

```text
Object.KeyFile
```

| Object | MQTTObject with this property |
| --- | --- |
| Object.KeyFile | String with read and write accessSpecifies the path to the key file. |

<!--NI_TOPIC bundle=diadem path=diamisc/properties/mqtt_property_password_mqtt.htm language=enus -->
## TOPIC 00201: Property: Password for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/properties/mqtt_property_password_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/properties/mqtt_property_password_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: Password for MQTT

Property: Password for MQTT

Specifies the password with which the user logs on to the MQTT broker. Whether a user name and password are required depends on the MQTT server.

```text
Object.Password
```

| Object | MQTTObject with this property |
| --- | --- |
| Object.Password | String with read and write accessSpecifies the password. |

<!--NI_TOPIC bundle=diadem path=diamisc/properties/mqtt_property_port_mqtt.htm language=enus -->
## TOPIC 00202: Property: Port for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/properties/mqtt_property_port_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/properties/mqtt_property_port_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: Port for MQTT

Property: Port for MQTT

Specifies the TCP port DIAdem uses for communication with the MQTT Broker. DIAdem only evaluates this property if you do not specify a port in the IP address when creating the MQTT object. The default value of this property is -1. By default, DIAdem uses port 1883 for unencrypted communication and port 8883 for encrypted communication.

```text
Object.Port
```

| Object | MQTTObject with this property |
| --- | --- |
| Object.Port | LongInteger with read and write accessSpecifies the TCP port DIAdem uses for communication with the MQTT Broker. |

<!--NI_TOPIC bundle=diadem path=diamisc/properties/mqtt_property_tlspassword_mqtt.htm language=enus -->
## TOPIC 00203: Property: TLSPassword for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/properties/mqtt_property_tlspassword_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/properties/mqtt_property_tlspassword_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: TLSPassword for MQTT

Property: TLSPassword for MQTT

Specifies the password of the private key of the MQTT client. If the private key of the MQTT client is protected with a password, you must specify the password so that the client can decrypt the messages from the MQTT Broker.

```text
Object.TLSPassword
```

| Object | MQTTObject with this property |
| --- | --- |
| Object.TLSPassword | String with read and write accessSpecifies the password of the private key. |

<!--NI_TOPIC bundle=diadem path=diamisc/properties/mqtt_property_useauthentication_mqtt.htm language=enus -->
## TOPIC 00204: Property: UseAuthentication for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/properties/mqtt_property_useauthentication_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/properties/mqtt_property_useauthentication_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: UseAuthentication for MQTT

Property: UseAuthentication for MQTT

Determines whether the user logs on to the MQTT-Broker anonymously or with user name and password. If the property has the value True, you must specify the [UserName](../properties/mqtt_property_username_mqtt.htm) and [Password](../properties/mqtt_property_password_mqtt.htm) properties. If any of these properties are missing during the connection setup to the MQTT Broker, DIAdem displays a data entry dialog box before DIAdem connects to the MQTT Broker.

```text
Object.UseAuthentication
```

| Object | MQTTObject with this property |
| --- | --- |
| Object.UseAuthentication | Boolean with read and write accessReceives the information whether the user logs on with user name and password (TRUE) or anonymously (FALSE). |

<!--NI_TOPIC bundle=diadem path=diamisc/properties/mqtt_property_username_mqtt.htm language=enus -->
## TOPIC 00205: Property: UserName for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/properties/mqtt_property_username_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/properties/mqtt_property_username_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: UserName for MQTT

Property: UserName for MQTT

Specifies the name with which the user logs on to the MQTT broker. Whether a user name and password are required depends on the MQTT server.

```text
Object.UserName
```

| Object | MQTTObject with this property |
| --- | --- |
| Object.UserName | String with read and write accessSpecifies the user name. |

<!--NI_TOPIC bundle=diadem path=diamisc/properties/mqtt_property_usetls_mqtt.htm language=enus -->
## TOPIC 00206: Property: UseTLS for MQTT

- bundle_id: `diadem`
- source_path: `diamisc/properties/mqtt_property_usetls_mqtt.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamisc/properties/mqtt_property_usetls_mqtt.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: UseTLS for MQTT

Property: UseTLS for MQTT

Specifies whether DIAdem exchanges encrypted data with the MQTT-Broker. If in an encrypted data transfer the [CACertificate](../properties/mqtt_property_cacertificate_mqtt.htm), [Certificate](../properties/mqtt_property_certificate_mqtt.htm), and [KeyFile](../properties/mqtt_property_keyfile_mqtt.htm) properties are not set to valid values, DIAdem displays a dialog box where you can add these properties when you connect with the [Connect](../methods/mqtt_method_connect_mqtt.htm) method.

```text
Object.UseTLS
```

| Object | MQTTObject with this property |
| --- | --- |
| Object.UseTLS | Boolean with read and write accessReceives the information whether the data transfer was successful (TRUE) or not (FALSE). |

<!--NI_TOPIC bundle=diadem path=diamiscobjects/methods/excelworkbook_method_item_iexcelworksheets.htm language=enus -->
## TOPIC 00207: Method: Item for Worksheets

- bundle_id: `diadem`
- source_path: `diamiscobjects/methods/excelworkbook_method_item_iexcelworksheets.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamiscobjects/methods/excelworkbook_method_item_iexcelworksheets.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Item for Worksheets

Method: Item for Worksheets

Returns a cell of an Excel workbook. You can always omit the Item method because it is the standard element of the collection.

```text
Set oWorksheet = Object.Item(NameOrIndex)
```

| Object | WorksheetsObject with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or index of the worksheet. |
| oWorksheet | WorksheetReturned object |

The following example creates an Excel workbook and outputs the name of the first worksheet. Refer to the help pages [Worksheets](../objects/excelworkbook_objects_iexcelworksheets.htm) and [Worksheet](../objects/excelworkbook_objects_iexcelworksheet.htm) for detailed examples:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyWorkbook, oMySheet 
Set oMyWorkbook = CreateExcelWorkbook() 
Set oMySheet = oMyWorkbook.Worksheets.Item(1)
Call MsgBox(oMySheet.Name)
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets.Item(1) 
print(oMySheet.Name) 
```

#### See Also

[Objects Overview](../objects/iexcelworkbook_objects_overview.htm)

#### Examples

[Creating an Excel File](../../exploff/examples/expl_excel.htm)

<!--NI_TOPIC bundle=diadem path=diamiscobjects/methods/excelworkbook_method_remove_iexcelworksheets.htm language=enus -->
## TOPIC 00208: Method: Remove for Worksheets

- bundle_id: `diadem`
- source_path: `diamiscobjects/methods/excelworkbook_method_remove_iexcelworksheets.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamiscobjects/methods/excelworkbook_method_remove_iexcelworksheets.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: Remove for Worksheets

Method: Remove for Worksheets

Deletes a worksheet in an Excel workbook.

```text
Object.Remove(NameOrIndex)
```

| Object | WorksheetsObject with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or index of the worksheet. |

The following example creates an Excel workbook, checks whether the Data worksheet exists, and deletes it. Refer to the help page [Worksheets](../objects/excelworkbook_objects_iexcelworksheets.htm) for detailed examples:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyWorkbook, oMyWorkSheet
Set oMyWorkbook = CreateExcelWorkbook()
If oMyWorkbook.Worksheets.Exists("Data") Then
  Call  oMyWorkbook.Worksheets.Remove("Data")
End If
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
if oMyWorkbook.Worksheets.Exists("Data") : 
     oMyWorkbook.Worksheets.Remove("Data") 
```

#### See Also

[Objects Overview](../objects/iexcelworkbook_objects_overview.htm)

#### Examples

[Creating an Excel File](../../exploff/examples/expl_excel.htm)

<!--NI_TOPIC bundle=diadem path=diamiscobjects/methods/excelworkbook_method_removeall_iexcelworksheets.htm language=enus -->
## TOPIC 00209: Method: RemoveAll for Worksheets

- bundle_id: `diadem`
- source_path: `diamiscobjects/methods/excelworkbook_method_removeall_iexcelworksheets.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamiscobjects/methods/excelworkbook_method_removeall_iexcelworksheets.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: RemoveAll for Worksheets

Method: RemoveAll for Worksheets

Deletes all worksheets of an Excel workbook.

```text
Object.RemoveAll
```

| Object | WorksheetsObject with this method |
| --- | --- |

The following example creates an Excel workbook, deletes all the worksheets, and creates a new worksheet named Data. Refer to the help page [Worksheets](../objects/excelworkbook_objects_iexcelworksheets.htm) for detailed examples:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyWorkbook, oMyWorkSheet
Set oMyWorkbook = CreateExcelWorkbook()
Call  oMyWorkbook.Worksheets.RemoveAll
Set oMyWorkSheet = oMyWorkbook.Worksheets.Add("Data")
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
 oMyWorkbook.Worksheets.RemoveAll() 
oMyWorkSheet = oMyWorkbook.Worksheets.Add("Data") 
```

#### See Also

[Objects Overview](../objects/iexcelworkbook_objects_overview.htm)

#### Examples

[Creating an Excel File](../../exploff/examples/expl_excel.htm)

<!--NI_TOPIC bundle=diadem path=diamiscobjects/methods/excelworkbook_method_saveas_iexcelworkbook.htm language=enus -->
## TOPIC 00210: Method: SaveAs for Workbook

- bundle_id: `diadem`
- source_path: `diamiscobjects/methods/excelworkbook_method_saveas_iexcelworkbook.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamiscobjects/methods/excelworkbook_method_saveas_iexcelworkbook.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Methods > Method: SaveAs for Workbook

Method: SaveAs for Workbook

Saves an Excel workbook.

```text
bSaveAs = Object.SaveAs(Filename)
```

| Object | WorkbookObject with this method |
| --- | --- |
| Filename | StringSpecifies the path and the name of the Excel file. You must enter the filename extension. |
| bSaveAs | BooleanSpecifies whether saving was successful (TRUE) or not (FALSE). |

The following example creates an Excel workbook, fills the first cell in the first worksheet with the value 3.14, and saves the Excel workbook in a new XLSX file. Refer to the help page [Workbook](../objects/excelworkbook_objects_iexcelworkbook.htm) for detailed examples:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyWorkbook, oMySheet 
Set oMyWorkbook = CreateExcelWorkbook() 
Set oMySheet = oMyWorkbook.Worksheets(1) 
oMySheet.Cells(1, 1).Value = 3.14
Call oMyWorkbook.SaveAs(DataWritePath & "Test.xlsx")
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets(1) 
oMySheet.Cells(1, 1).Value = 3.14 
oMyWorkbook.SaveAs(dd.DataWritePath + "Test.xlsx") 
```

#### See Also

[Objects Overview](../objects/iexcelworkbook_objects_overview.htm)

#### Examples

[Creating an Excel File](../../exploff/examples/expl_excel.htm)

<!--NI_TOPIC bundle=diadem path=diamiscobjects/objects/excelworkbook_objects_iexcelcell.htm language=enus -->
## TOPIC 00211: Object: Cell

- bundle_id: `diadem`
- source_path: `diamiscobjects/objects/excelworkbook_objects_iexcelcell.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamiscobjects/objects/excelworkbook_objects_iexcelcell.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Excel](../excel_overview.htm) > [Objects](../objects/iexcelworkbook_objects_overview.htm) > [Workbook](../objects/excelworkbook_objects_iexcelworkbook.htm) > [Worksheets](../objects/excelworkbook_objects_iexcelworksheets.htm) > [Worksheet](../objects/excelworkbook_objects_iexcelworksheet.htm) > Object: Cell

Object: Cell

The Cell object corresponds to a cell in an Excel worksheet.

The following example creates an Excel workbook, fills the first cell with the value 3.14, and outputs this value.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyWorkbook, oMySheet, oMyCell
Set oMyWorkbook = CreateExcelWorkbook() 
Set oMySheet = oMyWorkbook.Worksheets(1) 
Set oMyCell = oMySheet.Cells(1, 1)
oMyCell.Value = 3.14
Call MsgBox(oMyCell.Value)
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets(1) 
oMyCell = oMySheet.Cells(1, 1) 
oMyCell.Value = 3.14 
print(oMyCell.Value) 
```

The following example creates an Excel workbook, fills the first worksheet with random values, and highlights the cells containing the value 47 with a red background:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim iCount, jCount, oMyWorkbook, oMySheet, oMyCell, oMyNextCell
Set oMyWorkbook = CreateExcelWorkbook()
Set oMySheet = oMyWorkbook.Worksheets(1)
For iCount = 1 to 1000
  For jCount = 1 to 20
    Set oMyCell = oMySheet.Cells(iCount, jCount)
    oMyCell.Value = Round(Random(100))
  Next
Next
Set oMyNextCell = oMySheet.Find(47, eExcelSearchEquals)
Do While Not(oMyNextCell Is Nothing)
  oMyNextCell.Interior.Color = RGB(255, 0, 0)
  Set oMyNextCell = oMySheet.Find(47, eExcelSearchEquals, oMyNextCell.Row,  oMyNextCell.Column)
Loop
Call oMyWorkbook.SaveAs(DataWritePath & "Test.xlsx")
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets(1) 
for iCount in range( 1, 1000 + 1): 
    for jCount in range( 1, 20 + 1): 
        oMyCell = oMySheet.Cells(iCount, jCount) 
        oMyCell.Value = Round(dd.Random(100)) 
oMyNextCell = oMySheet.Find(47, dd.eExcelSearchEquals) 
while Do : 
    oMyNextCell.Interior.Color = dd.RGB(255, 0, 0) 
    oMyNextCell = oMySheet.Find(47, dd.eExcelSearchEquals, oMyNextCell.Row,  oMyNextCell.Column) 
oMyWorkbook.SaveAs(dd.DataWritePath + "Test.xlsx") 
```

#### Properties

[Column](../properties/excelworkbook_property_column_iexcelcell.htm) | [ColumnWidth](../properties/excelworkbook_property_columnwidth_iexcelcell.htm) | [Font](../properties/excelworkbook_property_font_iexcelcell.htm) | [HorizontalAlignment](../properties/excelworkbook_property_horizontalalignment_iexcelcell.htm) | [Interior](../properties/excelworkbook_property_interior_iexcelcell.htm) | [Row](../properties/excelworkbook_property_row_iexcelcell.htm) | [RowHeight](../properties/excelworkbook_property_rowheight_iexcelcell.htm) | [Value](../properties/excelworkbook_property_value_iexcelcell.htm) | [VerticalAlignment](../properties/excelworkbook_property_verticalalignment_iexcelcell.htm)

#### Returned From

[Worksheet](../objects/excelworkbook_objects_iexcelworksheet.htm).[Cells](../methods/excelworkbook_method_cells_iexcelworksheet.htm) | [Worksheet](../objects/excelworkbook_objects_iexcelworksheet.htm).[Find](../methods/excelworkbook_method_find_iexcelworksheet.htm)

#### See Also

[Objects Overview](../objects/iexcelworkbook_objects_overview.htm)

#### Examples

[Creating an Excel File](../../exploff/examples/expl_excel.htm)

<!--NI_TOPIC bundle=diadem path=diamiscobjects/objects/excelworkbook_objects_iexcelfont.htm language=enus -->
## TOPIC 00212: Object: Font

- bundle_id: `diadem`
- source_path: `diamiscobjects/objects/excelworkbook_objects_iexcelfont.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamiscobjects/objects/excelworkbook_objects_iexcelfont.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Excel](../excel_overview.htm) > [Objects](../objects/iexcelworkbook_objects_overview.htm) > [Workbook](../objects/excelworkbook_objects_iexcelworkbook.htm) > [Worksheets](../objects/excelworkbook_objects_iexcelworksheets.htm) > [Worksheet](../objects/excelworkbook_objects_iexcelworksheet.htm) > [Cell](../objects/excelworkbook_objects_iexcelcell.htm) > Object: Font

Object: Font

The Font object corresponds to the font of a cell in an Excel worksheet.

The following example creates an Excel workbook, sets the first cell to 3.14, sets the font color of this cell to blue, and saves the Excel workbook in a new XLSX file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyWorkbook, oMySheet, oMyCell
Set oMyWorkbook = CreateExcelWorkbook() 
Set oMySheet = oMyWorkbook.Worksheets(1) 
Set oMyCell = oMySheet.Cells(1, 1)
oMyCell.Value = 3.14
oMyCell.Font.Color = RGB(0, 0, 255)
Call oMyWorkbook.SaveAs(DataWritePath & "Test.xlsx")
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets(1) 
oMyCell = oMySheet.Cells(1, 1) 
oMyCell.Value = 3.14 
oMyCell.Font.Color = dd.RGB(0, 0, 255) 
oMyWorkbook.SaveAs(dd.DataWritePath + "Test.xlsx") 
```

The following example creates an Excel workbook, fills the first workbook with random values, searches for the value 47 in the worksheet, marks the found cells with a larger red font, and saves this Excel workbook in a new XLSX file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim iCount, jCount, oMyWorkbook, oMySheet, oMyCell, oMyNextCell
Set oMyWorkbook = CreateExcelWorkbook()
Set oMySheet = oMyWorkbook.Worksheets(1)
For iCount = 1 to 1000
  For jCount = 1 to 20
    Set oMyCell = oMySheet.Cells(iCount, jCount)
    oMyCell.Value = Round(Random(100))
  Next
Next
Set oMyNextCell = oMySheet.Find(47, eExcelSearchEquals)
Do While Not(oMyNextCell Is Nothing)
  oMyNextCell.Font.Color = RGB(255, 0, 0)
  oMyNextCell.Font.Size = 15
  Set oMyNextCell = oMySheet.Find(47, eExcelSearchEquals, oMyNextCell.Row,  oMyNextCell.Column)
Loop
Call oMyWorkbook.SaveAs(DataWritePath & "Test.xlsx")
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets(1) 
for iCount in range( 1, 1000 + 1): 
    for jCount in range( 1, 20 + 1): 
        oMyCell = oMySheet.Cells(iCount, jCount) 
        oMyCell.Value = Round(dd.Random(100)) 
oMyNextCell = oMySheet.Find(47, dd.eExcelSearchEquals) 
while Do : 
    oMyNextCell.Font.Color = dd.RGB(255, 0, 0) 
    oMyNextCell.Font.Size = 15 
    oMyNextCell = oMySheet.Find(47, dd.eExcelSearchEquals, oMyNextCell.Row,  oMyNextCell.Column) 
oMyWorkbook.SaveAs(dd.DataWritePath + "Test.xlsx") 
```

#### Properties

[Bold](../properties/excelworkbook_property_bold_iexcelfont.htm) | [Color](../properties/excelworkbook_property_color_iexcelfont.htm) | [Italic](../properties/excelworkbook_property_italic_iexcelfont.htm) | [Size](../properties/excelworkbook_property_size_iexcelfont.htm) | [Underline](../properties/excelworkbook_property_underline_iexcelfont.htm)

#### Returned From

[Cell](../objects/excelworkbook_objects_iexcelcell.htm).[Font](../properties/excelworkbook_property_font_iexcelcell.htm)

#### See Also

[Objects Overview](../objects/iexcelworkbook_objects_overview.htm)

#### Examples

[Creating an Excel File](../../exploff/examples/expl_excel.htm)

<!--NI_TOPIC bundle=diadem path=diamiscobjects/objects/excelworkbook_objects_iexcelinterior.htm language=enus -->
## TOPIC 00213: Object: Interior

- bundle_id: `diadem`
- source_path: `diamiscobjects/objects/excelworkbook_objects_iexcelinterior.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamiscobjects/objects/excelworkbook_objects_iexcelinterior.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Excel](../excel_overview.htm) > [Objects](../objects/iexcelworkbook_objects_overview.htm) > [Workbook](../objects/excelworkbook_objects_iexcelworkbook.htm) > [Worksheets](../objects/excelworkbook_objects_iexcelworksheets.htm) > [Worksheet](../objects/excelworkbook_objects_iexcelworksheet.htm) > [Cell](../objects/excelworkbook_objects_iexcelcell.htm) > Object: Interior

Object: Interior

The Interior object corresponds to the interior of a cell in an Excel worksheet.

The following example creates an Excel workbook and changes the background of the first cell.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyWorkbook, oMySheet, oMyCell
Set oMyWorkbook = CreateExcelWorkbook() 
Set oMySheet = oMyWorkbook.Worksheets(1) 
Set oMyCell = oMySheet.Cells(1, 1)
oMyCell.Interior.Color = RGB(0, 255, 0)
Call oMyWorkbook.SaveAs(DataWritePath & "Test.xlsx")
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets(1) 
oMyCell = oMySheet.Cells(1, 1) 
oMyCell.Interior.Color = dd.RGB(0, 255, 0) 
oMyWorkbook.SaveAs(dd.DataWritePath + "Test.xlsx") 
```

The following example creates an Excel workbook, fills the first worksheet with random values, and highlights the cells containing the value 47 with a red background:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim iRow, jCol, oMyWorkbook, oMySheet, oMyCell
Set oMyWorkbook = CreateExcelWorkbook()
Set oMySheet = oMyWorkbook.Worksheets(1)
For iRow = 1 to 1000
  For jCol = 1 to 20
    Set oMyCell = oMySheet.Cells(iRow, jCol)
    oMyCell.Value = Round(Random(100))
    If oMyCell.Value = 47 Then oMyCell.Interior.Color = RGB(255, 0, 0)
  Next
Next
Call oMyWorkbook.SaveAs(DataWritePath & "Test.xlsx")
Call LogFileWrite(DataWritePath & "Test.xlsx")
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets(1) 
for iRow in range( 1, 1000 + 1): 
    for jCol in range( 1, 20 + 1): 
        oMyCell = oMySheet.Cells(iRow, jCol) 
        oMyCell.Value = Round(dd.Random(100)) 
        if oMyCell.Value == 47 : oMyCell.Interior.Color = dd.RGB(255, 0, 0) 
    oMyWorkbook.SaveAs(dd.DataWritePath + "Test.xlsx") 
    dd.LogFileWrite(dd.DataWritePath + "Test.xlsx") 
```

#### Properties

[Color](../properties/excelworkbook_property_color_iexcelinterior.htm)

#### Returned From

[Cell](../objects/excelworkbook_objects_iexcelcell.htm).[Interior](../properties/excelworkbook_property_interior_iexcelcell.htm)

#### See Also

[Objects Overview](../objects/iexcelworkbook_objects_overview.htm)

#### Examples

[Creating an Excel File](../../exploff/examples/expl_excel.htm)

<!--NI_TOPIC bundle=diadem path=diamiscobjects/objects/excelworkbook_objects_iexcelworkbook.htm language=enus -->
## TOPIC 00214: Object: Workbook

- bundle_id: `diadem`
- source_path: `diamiscobjects/objects/excelworkbook_objects_iexcelworkbook.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamiscobjects/objects/excelworkbook_objects_iexcelworkbook.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Excel](../excel_overview.htm) > [Objects](../objects/iexcelworkbook_objects_overview.htm) > Object: Workbook

Object: Workbook

The Workbook object corresponds to an Excel workbook.

The following example creates an Excel workbook and fills a cell with the value 3.14:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyWorkbook, oMySheet 
Set oMyWorkbook = CreateExcelWorkbook() 
Set oMySheet = oMyWorkbook.Worksheets(1) 
oMySheet.Cells(1, 1).Value = 3.14
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets(1) 
oMySheet.Cells(1, 1).Value = 3.14 
```

The following example creates an Excel workbook, fills the first worksheet with random values, and highlights the cells containing the value 47 with a red background:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim iRow, jCol, oMyWorkbook, oMySheet, oMyCell
Set oMyWorkbook = CreateExcelWorkbook()
Set oMySheet = oMyWorkbook.Worksheets(1)
For iRow = 1 to 1000
  For jCol = 1 to 20
    Set oMyCell = oMySheet.Cells(iRow, jCol)
    oMyCell.Value = Round(Random(100))
    IF oMyCell.Value = 47 THEN oMyCell.Interior.Color = RGB(255, 0, 0)
  Next
Next
Call oMyWorkbook.SaveAs(DataWritePath & "Test.xlsx")
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets(1) 
for iRow in range( 1, 1000 + 1): 
    for jCol in range( 1, 20 + 1): 
        oMyCell = oMySheet.Cells(iRow, jCol) 
        oMyCell.Value = Round(dd.Random(100)) 
        if oMyCell.Value == 47 : oMyCell.Interior.Color = dd.RGB(255, 0, 0) 
    oMyWorkbook.SaveAs(dd.DataWritePath + "Test.xlsx") 
```

#### Properties

[Worksheets](../properties/excelworkbook_property_worksheets_iexcelworkbook.htm)

#### Methods

[SaveAs](../methods/excelworkbook_method_saveas_iexcelworkbook.htm)

#### See Also

[Objects Overview](../objects/iexcelworkbook_objects_overview.htm)

#### Examples

[Creating an Excel File](../../exploff/examples/expl_excel.htm)

<!--NI_TOPIC bundle=diadem path=diamiscobjects/objects/excelworkbook_objects_iexcelworksheet.htm language=enus -->
## TOPIC 00215: Object: Worksheet

- bundle_id: `diadem`
- source_path: `diamiscobjects/objects/excelworkbook_objects_iexcelworksheet.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamiscobjects/objects/excelworkbook_objects_iexcelworksheet.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Excel](../excel_overview.htm) > [Objects](../objects/iexcelworkbook_objects_overview.htm) > [Workbook](../objects/excelworkbook_objects_iexcelworkbook.htm) > [Worksheets](../objects/excelworkbook_objects_iexcelworksheets.htm) > Object: Worksheet

Object: Worksheet

The Worksheet object corresponds to an Excel worksheet.

The following example creates an Excel workbook and outputs the name of the first worksheet:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyWorkbook, oMySheet
Set oMyWorkbook = CreateExcelWorkbook()
Set oMySheet = oMyWorkbook.Worksheets(1)
Call MsgBox(oMySheet.Name)
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets(1) 
print(oMySheet.Name) 
```

The following example creates an Excel workbook, fills the first worksheet with random values, and saves this Excel workbook in a new XLSX file. If the value is 47, the example highlights this cell with a red background.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim iRow, jCol, oMyWorkbook, oMySheet, oMyCell
Set oMyWorkbook = CreateExcelWorkbook()
Set oMySheet = oMyWorkbook.Worksheets(1)
For iRow = 1 to 1000
  For jCol = 1 to 20
    Set oMyCell = oMySheet.Cells(iRow, jCol)
    oMyCell.Value = Round(Random(100))
    If oMyCell.Value = 47 Then oMyCell.Interior.Color = RGB(255, 0, 0)
  Next
Next
Call oMyWorkbook.SaveAs(DataWritePath & "Test.xlsx")
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets(1) 
for iRow in range( 1, 1000 + 1): 
    for jCol in range( 1, 20 + 1): 
        oMyCell = oMySheet.Cells(iRow, jCol) 
        oMyCell.Value = Round(dd.Random(100)) 
        if oMyCell.Value == 47 : oMyCell.Interior.Color = dd.RGB(255, 0, 0) 
    oMyWorkbook.SaveAs(dd.DataWritePath + "Test.xlsx") 
```

#### Properties

[Name](../properties/excelworkbook_property_name_iexcelworksheet.htm)

#### Methods

[Cells](../methods/excelworkbook_method_cells_iexcelworksheet.htm) | [Find](../methods/excelworkbook_method_find_iexcelworksheet.htm)

#### Returned From

[Worksheets](../objects/excelworkbook_objects_iexcelworksheets.htm).[Add](../methods/excelworkbook_method_add_iexcelworksheets.htm) | [Worksheets](../objects/excelworkbook_objects_iexcelworksheets.htm).[Item](../methods/excelworkbook_method_item_iexcelworksheets.htm)

#### See Also

[Objects Overview](../objects/iexcelworkbook_objects_overview.htm)

#### Examples

[Creating an Excel File](../../exploff/examples/expl_excel.htm)

<!--NI_TOPIC bundle=diadem path=diamiscobjects/objects/excelworkbook_objects_iexcelworksheets.htm language=enus -->
## TOPIC 00216: Collection: Worksheets

- bundle_id: `diadem`
- source_path: `diamiscobjects/objects/excelworkbook_objects_iexcelworksheets.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamiscobjects/objects/excelworkbook_objects_iexcelworksheets.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Excel](../excel_overview.htm) > [Objects](../objects/iexcelworkbook_objects_overview.htm) > [Workbook](../objects/excelworkbook_objects_iexcelworkbook.htm) > Collection: Worksheets

Collection: Worksheets

Collection of Excel worksheets.

The following example creates an Excel workbook and returns the number of worksheets.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyWorkbook, oMyWorksheets
Set oMyWorkbook = CreateExcelWorkbook()
Set oMyWorksheets = oMyWorkbook.Worksheets
Call MsgBox(oMyWorksheets.Count)
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMyWorksheets = oMyWorkbook.Worksheets 
print(oMyWorksheets.Count) 
```

The following example creates an Excel workbook, fills the first worksheet with random values, and highlights the cells containing the value 47 with a red background:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim iRow, jCol, oMyWorkbook, oMySheet, oMyCell
Set oMyWorkbook = CreateExcelWorkbook()
Set oMySheet = oMyWorkbook.Worksheets(1)
For iRow = 1 to 1000
  For jCol = 1 to 20
    Set oMyCell = oMySheet.Cells(iRow, jCol)
    oMyCell.Value = Round(Random(100))
    If oMyCell.Value = 47 Then oMyCell.Interior.Color = RGB(255, 0, 0)
  Next
Next
Call oMyWorkbook.SaveAs(DataWritePath & "Test.xlsx")
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets(1) 
for iRow in range( 1, 1000 + 1): 
    for jCol in range( 1, 20 + 1): 
        oMyCell = oMySheet.Cells(iRow, jCol) 
        oMyCell.Value = Round(dd.Random(100)) 
        if oMyCell.Value == 47 : oMyCell.Interior.Color = dd.RGB(255, 0, 0) 
    oMyWorkbook.SaveAs(dd.DataWritePath + "Test.xlsx") 
```

#### Properties

[Count](../properties/excelworkbook_property_count_iexcelworksheets.htm)

#### Methods

[Add](../methods/excelworkbook_method_add_iexcelworksheets.htm) | [Exists](../methods/excelworkbook_method_exists_iexcelworksheets.htm) | [Item](../methods/excelworkbook_method_item_iexcelworksheets.htm) | [Remove](../methods/excelworkbook_method_remove_iexcelworksheets.htm) | [RemoveAll](../methods/excelworkbook_method_removeall_iexcelworksheets.htm)

#### Returned From

[Workbook](../objects/excelworkbook_objects_iexcelworkbook.htm).[Worksheets](../properties/excelworkbook_property_worksheets_iexcelworkbook.htm)

#### See Also

[Objects Overview](../objects/iexcelworkbook_objects_overview.htm)

#### Examples

[Creating an Excel File](../../exploff/examples/expl_excel.htm)

<!--NI_TOPIC bundle=diadem path=diamiscobjects/properties/excelworkbook_property_interior_iexcelcell.htm language=enus -->
## TOPIC 00217: Property: Interior for Cell

- bundle_id: `diadem`
- source_path: `diamiscobjects/properties/excelworkbook_property_interior_iexcelcell.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamiscobjects/properties/excelworkbook_property_interior_iexcelcell.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: Interior for Cell

Property: Interior for Cell

Returns the interior of a cell in an Excel worksheet.

```text
Set oInterior = Object.Interior
```

| Object | CellObject with this property |
| --- | --- |
| oInterior | InteriorReturned object |

The following example creates an Excel workbook, changes the background color of the first cell to green, and saves the Excel workbook in a new XLSX file. Refer to the help pages [Cell](../objects/excelworkbook_objects_iexcelcell.htm) and [Interior](../objects/excelworkbook_objects_iexcelinterior.htm) for detailed examples:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyWorkbook, oMySheet, oMyCell
Set oMyWorkbook = CreateExcelWorkbook() 
Set oMySheet = oMyWorkbook.Worksheets(1) 
Set oMyCell = oMySheet.Cells(1, 1)
oMyCell.Interior.Color = RGB(0, 255, 0)
Call oMyWorkbook.SaveAs(DataWritePath & "Test.xlsx")
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets(1) 
oMyCell = oMySheet.Cells(1, 1) 
oMyCell.Interior.Color = dd.RGB(0, 255, 0) 
oMyWorkbook.SaveAs(dd.DataWritePath + "Test.xlsx") 
```

#### See Also

[Objects Overview](../objects/iexcelworkbook_objects_overview.htm)

#### Examples

[Creating an Excel File](../../exploff/examples/expl_excel.htm)

<!--NI_TOPIC bundle=diadem path=diamiscobjects/properties/excelworkbook_property_italic_iexcelfont.htm language=enus -->
## TOPIC 00218: Property: Italic for Font

- bundle_id: `diadem`
- source_path: `diamiscobjects/properties/excelworkbook_property_italic_iexcelfont.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/diamiscobjects/properties/excelworkbook_property_italic_iexcelfont.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Properties > Property: Italic for Font

Property: Italic for Font

Specifies whether DIAdem formats the text of a cell in an Excel worksheet in Italic type.

```text
Object.Italic
```

| Object | FontObject with this property |
| --- | --- |
| Object.Italic | Boolean with read and write accessSpecifies whether DIAdem displays a text in italic type (TRUE) or not (FALSE). |

The following example creates an Excel workbook, sets the value of the first cell to 3.14, sets the font attributes to italics, and saves the Excel workbook in a new XLSX file. Refer to the help page [Font](../objects/excelworkbook_objects_iexcelfont.htm) for detailed examples:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyWorkbook, oMySheet, oMyCell
Set oMyWorkbook = CreateExcelWorkbook() 
Set oMySheet = oMyWorkbook.Worksheets(1) 
Set oMyCell = oMySheet.Cells(1, 1)
oMyCell.Value = 3.14
oMyCell.Font.Italic = TRUE
Call oMyWorkbook.SaveAs(DataWritePath & "Test.xlsx")
```

[Copy script](javascript:void(0);)

```text
oMyWorkbook = dd.CreateExcelWorkbook() 
oMySheet = oMyWorkbook.Worksheets(1) 
oMyCell = oMySheet.Cells(1, 1) 
oMyCell.Value = 3.14 
oMyCell.Font.Italic = True 
oMyWorkbook.SaveAs(dd.DataWritePath + "Test.xlsx") 
```

#### See Also

[Objects Overview](../objects/iexcelworkbook_objects_overview.htm)

#### Examples

[Creating an Excel File](../../exploff/examples/expl_excel.htm)

<!--NI_TOPIC bundle=diadem path=dlgcalculator/dlgcalculator/dlgcalculation_buttons.htm language=enus -->
## TOPIC 00219: Calculator Buttons

- bundle_id: `diadem`
- source_path: `dlgcalculator/dlgcalculator/dlgcalculation_buttons.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgcalculator/dlgcalculator/dlgcalculation_buttons.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculator](../dlgcalculator/dlgcalculation_dialog.htm) > Calculator Buttons

Calculator Buttons

Use the buttons of the Calculator to insert numeric values and functions in the formula input of the calculator. You can also use the keyboard to make your entries. When you enter the formulas with the buttons, DIAdem adds the selected functions at the current cursor position. If you select an area of the formula entry, DIAdem inserts this area between the opening and closing parentheses of the selected function. If the function does not use parentheses, DIAdem inserts the function behind the selected text.

| Button | Meaning |
| --- | --- |
|  | Use the ch() button to insert a channel assignment. |
|  | Use the e button to enter the Eularian number. Depending on the formula syntax, DIAdem decides whether to use the Eulerian number or the scientific numeric display.Use the Pi button to enter the mathematical constant Pi. |
|  | Use the x^y button to calculate the power of two numbers.Use the x² button to calculate the square of a number.Use the Root button to calculate the square root of a number.Use the 1/x button to calculate the reciprocal of a number. |
|  | Use the buttons ( and ) to enclose operations in parentheses. |
|  | Use the buttons <, >, <=, >=, =, and <> for comparisons. |
|  | Use the MC (Memory clear) button to delete the contents of the intermediate memory.Use the MR (Memory recall) button to enter the contents of the intermediate memory into the text box.Use the M+ (Memory +) button to add the result of the current calculation to the contents of the buffer.Use the M- (Memory -) button to subtract the result of the current calculation from the contents of the buffer. |
|  | Use the C button to delete the contents of the Formula/Result input fields.Use the CE button to undo the last entry. |
|  | Use the buttons /, *, -, and + to insert basic mathematical operators. |
|  | Use the Period button to specify it as the decimal symbol. |
|  | Use the Calculate button to Request Variable Contents and Calculation Results in the Calculator. |

#### Procedures

[Assigning a Value to a Variable in the Calculator](../../procmaths/procmaths/mathsproc_singlevariables.htm) | [Executing Channel Calculations in the Calculator](../../procmaths/procmaths/mathsproc_channelcalculations.htm) | [Repeating Calculations Automatically](../../procmaths/procmaths/mathsproc_auto.htm) | [Requesting Variable Contents and Calculation Results on the Calculator](../../procmaths/procmaths/mathsproc_request.htm) | [Running Comparisons on the Calculator](../../procmaths/procmaths/mathsproc_compop.htm) | [Using NoValues to Eliminate Outliers](../../procmaths/procmaths/mathsproc_novalue_limit.htm) | [Working with Text in the Calculator](../../procmaths/procmaths/mathsproc_text.htm)

<!--NI_TOPIC bundle=diadem path=dlgcalculator/dlgcalculator/dlgcalculation_dialog.htm language=enus -->
## TOPIC 00220: Calculator

- bundle_id: `diadem`
- source_path: `dlgcalculator/dlgcalculator/dlgcalculation_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgcalculator/dlgcalculator/dlgcalculation_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Calculator

Calculator

Use this dialog box to enter and calculate a formula. In the formula, you connect data channels according to their function, request values from variables, and assign values to variables. You can also execute numeric operations, Boolean operations, and text operations.

The calculator dialog box is non-modal, which means that the dialog box can remain open while you work in DIAdem. You can display the Calculator with reduced or extended functions, or minimize it to the title bar. The current setting and the position remain when the Calculator or DIAdem are restarted.

#### Settings

|  | Reduced Functions | Switches the Calculator to basic mode. |
| --- | --- | --- |
|  | Extended Functions | Switches the Calculator to extended mode. In the extended mode an additional control panel with 30 function buttons opens. |
|  | Formula Transfer to Calculation Manager | Converts the formula in a calculation in the calculation manager. DIAdem then starts the calculation manager so that you can process the new calculation.You can only convert A = B + C type equations. During conversion, the Calculation Manager interprets the right part of the equation as inputs and the left part as outputs. If the names used in the Calculator do not correspond to the Name Conventions for Calculations, the Calculation Manager marks these names with the prefix Error_. You must correct the formula and the names so that the Calculation Manager can execute the calculation. |
|  | Prepare for SCRIPT and Copy to Clipboard | Processes the formula for a script and then copies the formula to the clipboard. |
|  | Configure Function Buttons | Opens the dialog box where you assign operators to the function buttons which you label and specify tooltips for. |
|  | Undo | Undoes the last work step. You can undo a maximum of 20 work steps. |
|  | Restore | Restores the last work step that was undone. |
|  | Formula Stack | Opens the dialog box in which DIAdem displays the formula used last. |
|  | Formula | Entry field for your formula in the Formula Syntax in the Calculator.If you drag and drop a channel from the Data Portal into the formula input, you can add a channel assignment.When you drag and drop a property from the Data Portal, you add the contents of this property. Click and press the <Shift>-key in order to insert a reference to the object-oriented script interface. |
|  | Result | Displays the formula expression and the result of a calculation. You cannot edit the contents of this field. |
|  | Single value | Displays the calculated single value. |
|  | Memory contents | Displays the contents of the memory. To do so, calculate the current calculation result with the memory keys. |

|  | Note Refer to Calculator Buttons for details on how to use the Calculator buttons. |
| --- | --- |

|  | Note To execute a calculation in quantity-based mode, click the Calculate Quantity-Based button on the DIAdem ANALYSIS toolbar or assign the value TRUE to the CalcQuantityBased variable. When executing quantity-based calculations, DIAdem checks whether the program can also execute calculations on physical quantities in the same calculation. If DIAdem cannot execute the calculation because the physical quantities are unsuitable, the program displays an error message. Refer to the Help page Calculating Quantity-Based and Non-Quantity-Based in DIAdem for the conditions and rules for quantity-based calculations. In addition to the rules for quantity-based calculations the following rules apply for the calculator and for the Calculate command: Use the CalculateResultUnit variable to determine the result unit. User commands, variables, and constants do not contain a unit. Use the VU function to assign a unit. If you calculate with time channels, DIAdem converts the time channels into seconds, uses the unit s, and ignores the unit that was assigned to the time channel. DIAdem uses unit one when calculating text channels. |
| --- | --- |

|  | Note Use the ValEqual command instead of the equals sign when you want to check whether two real numbers are equal. DIAdem uses only the significant digits of a number in the ValEqual command. |
| --- | --- |

#### Procedures

[Assigning a Value to a Variable in the Calculator](../../procmaths/procmaths/mathsproc_singlevariables.htm) | [Executing Channel Calculations in the Calculator](../../procmaths/procmaths/mathsproc_channelcalculations.htm) | [Repeating Calculations Automatically](../../procmaths/procmaths/mathsproc_auto.htm) | [Requesting Variable Contents and Calculation Results on the Calculator](../../procmaths/procmaths/mathsproc_request.htm) | [Running Comparisons on the Calculator](../../procmaths/procmaths/mathsproc_compop.htm) | [Using NoValues to Eliminate Outliers](../../procmaths/procmaths/mathsproc_novalue_limit.htm) | [Working with Text in the Calculator](../../procmaths/procmaths/mathsproc_text.htm)

<!--NI_TOPIC bundle=diadem path=dlgcalculator/dlgcalculator/dlgcalculation_formel_dialog.htm language=enus -->
## TOPIC 00221: Configure Function Buttons

- bundle_id: `diadem`
- source_path: `dlgcalculator/dlgcalculator/dlgcalculation_formel_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgcalculator/dlgcalculator/dlgcalculation_formel_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Calculator](../dlgcalculator/dlgcalculation_dialog.htm) > Configure Function Buttons

Configure Function Buttons

Use this dialog box to specify which operations are available on the 30 function buttons of the Calculator in the extended mode. You can assign numeric, Boolean, and text operations to these buttons.

DIAdem manages the assignment of the function buttons in a file with the filename extension .tfc. This file, which has the same name as the desktop file, is in the desktop folder. When the calculator is called, DIAdem reads in the individual configuration file. If the file does not exist, DIAdem uses the standard configuration. If you use **Apply** to exit the dialog box, DIAdem saves the configuration. If a configuration file already exists, DIAdem overwrites it without a prompt.

#### Settings

| Title | Specifies the function button labels, which can have up to 5 characters. |
| --- | --- |
| Operation | Specifies which numeric, Boolean, or text operation is transferred into the Formula entry field of the calculator when the function button is pressed. |
| Tooltip | Specifies the tooltip of the function button. |

#### Procedures

[Assigning a Value to a Variable in the Calculator](../../procmaths/procmaths/mathsproc_singlevariables.htm) | [Executing Channel Calculations in the Calculator](../../procmaths/procmaths/mathsproc_channelcalculations.htm) | [Repeating Calculations Automatically](../../procmaths/procmaths/mathsproc_auto.htm) | [Requesting Variable Contents and Calculation Results on the Calculator](../../procmaths/procmaths/mathsproc_request.htm) | [Running Comparisons on the Calculator](../../procmaths/procmaths/mathsproc_compop.htm) | [Using NoValues to Eliminate Outliers](../../procmaths/procmaths/mathsproc_novalue_limit.htm) | [Working with Text in the Calculator](../../procmaths/procmaths/mathsproc_text.htm)

<!--NI_TOPIC bundle=diadem path=dlgcanconverter/dlgcanconverter/dlgcanconv_editbusdbconf_dialog.htm language=enus -->
## TOPIC 00222: Edit Bus in Configuration

- bundle_id: `diadem`
- source_path: `dlgcanconverter/dlgcanconverter/dlgcanconv_editbusdbconf_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgcanconverter/dlgcanconverter/dlgcanconv_editbusdbconf_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../dlgcanconverter/canconverter_overview.htm) > [Bus Log Converter](../dlgcanconverter/dlgcanconv_main_dialog.htm) > [Edit Bus-Database Configuration](../dlgcanconverter/dlgcanconv_busdbconf_dialog.htm) > Edit Bus in Configuration

Edit Bus in Configuration

Use this dialog box to edit the link between database files and a bus.

#### Settings

|  | Bus type | Specifies the type of the bus to be edited. |
| --- | --- | --- |
|  | Bus number | Specifies the number of the bus to be edited. |
|  | Bus name | Specifies the name of the bus to be edited. To configure a specified XNET channel in TDMS logfiles, use the name of the XNET channel as bus name. |
|  | Add Database File | Opens the dialog box where you assign the appropriate database file to the selected bus.DIAdem supports the Vector CAN database format (*.dbc), the NI database format for NI-CAN (*.ncd), the Fibex database format (*.xml), the LIN file format (*.ldf), and AUTOSAR database files (*.arxml). AUTOSAR database file DIAdem supports CAN and CAN-FD formats but no LIN and FLEXRAY formats. |
|  | Remove Database File | Removes the database file that is selected in the overview. |
|  | Move Database File Up | Moves the selected database file one line up in the overview. You also can select and move several consecutively listed files. |
|  | Move Database File Down | Moves the selected database file one line down in the overview. You also can select and move several consecutively listed files. |
|  | No. | Specifies the serial number of the database file. |
|  | IdMode | Specifies whether the database file is a standard file or a file with a special mode. |
|  | Cluster | Shows the cluster taken from the Fibex database file. If this line does not contain clusters, DIAdem uses all clusters contained in the database file. Click this field to open the Dialog box for cluster selection. |
|  | Database File | Displays the name of the database file. |

<!--NI_TOPIC bundle=diadem path=dlgcanconverter/dlgcanconverter/dlgcanconv_example_script.htm language=enus -->
## TOPIC 00223: Converting Logfiles with a Script

- bundle_id: `diadem`
- source_path: `dlgcanconverter/dlgcanconverter/dlgcanconv_example_script.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgcanconverter/dlgcanconverter/dlgcanconv_example_script.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../dlgcanconverter/canconverter_overview.htm) > Converting Logfiles with a Script

Converting Logfiles with a Script

The following script converts all available logfiles within a folder into the TDM format using the specified filename extension. Each of the result data files contains the same name as the logfile which is to be converted.

Before you start the script, select, for example, the paths, logfile format, the logfile filename extension, or the bus database configuration under Settings. To get an overview of your settings, press <Ctrl-Shift-C> in the dialog box and then use <Ctrl-V> to insert the clipboard contents into an empty script .

Refer to [Bus Log Converter Interface](../../icanconverter/canconverterapi_overview.htm) for further information on creating a script.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Option Explicit  
Dim aFoundFiles       'Array of logfiles
Dim iCount            'Counter for existing logfiles
Dim sLogFileFolder    'Logfile folder
Dim sDbcFileFolder    'Dbc file folder
Dim sResultFileFolder 'Result file folder (tdm)
Dim sLogFileExt       'Logfile extension
Dim sLogFileName      'Currently converted logfile

'Settings
Call BusLogToTDM.Clear()
BusLogToTDM.BusDbConfig.Name = "CAN converter configuration"
BusLogToTDM.BusDbConfig.Description = "Convert logfiles of one folder"
BusLogToTDM.ResultSettings.TimeFilter.Active = False
BusLogToTDM.ResultSettings.BusFilter.Active = False
BusLogToTDM.ResultSettings.SequenceChannel = True
BusLogToTDM.ResultSettings.EnumSubstitution = True

sLogFileFolder = "C:\MyLogFiles\"
sDbcFileFolder = "C:\MyDbcFiles\"
sResultFileFolder = "C:\MyTdmFiles\"
sLogFileExt = "*.ncl"
BusLogToTDM.LogSettings.FileType = eLogFileTypeNI
Call BusLogToTDM.BusDbConfig.Buses.Add("CANBus", 1)
Call BusLogToTDM.BusDbConfig.Buses("CANBus").DbFiles.Add(sDbcFileFolder & "CANExample.dbc")
' End of settings

'Convert files 
aFoundFiles = DirListGet(sLogFileFolder, sLogFileExt, "filename", "FullFilenames")
If IsArray(aFoundFiles) Then
  For iCount = Lbound(aFoundFiles) to Ubound(aFoundFiles)
    Call BusLogToTDM.LogSettings.LogFiles.RemoveAll
    Call BusLogToTDM.LogSettings.LogFiles.Add(aFoundFiles(iCount))
    sLogFileName = FileNameSplit(aFoundFiles(iCount),"N")
    BusLogToTDM.ResultSettings.ResultFile = sResultFileFolder & sLogFileName & ".tdm"
    Call BusLogToTDM.Convert()
  Next
End If
```

[Copy script](javascript:void(0);)

```text
 #Array of logfiles
 #Counter for existing logfiles
 #Logfile folder
 #Dbc file folder
 #Result file folder (tdm)
 #Logfile extension
 #Currently converted logfile
#Settings
dd.BusLogToTDM.Clear() 
BusLogToTDM.BusDbConfig.Name = "CAN converter configuration" 
BusLogToTDM.BusDbConfig.Description = "Convert logfiles of one folder" 
BusLogToTDM.ResultSettings.TimeFilter.Active = False 
BusLogToTDM.ResultSettings.BusFilter.Active = False 
BusLogToTDM.ResultSettings.SequenceChannel = True 
BusLogToTDM.ResultSettings.EnumSubstitution = True 
sLogFileFolder = "C:\\MyLogFiles\" 
sDbcFileFolder = "C:\\MyDbcFiles\" 
sResultFileFolder = "C:\\MyTdmFiles\" 
sLogFileExt = "*.ncl" 
BusLogToTDM.LogSettings.FileType = dd.eLogFileTypeNI 
dd.BusLogToTDM.BusDbConfig.Buses.Add("CANBus", 1) 
dd.BusLogToTDM.BusDbConfig.Buses("CANBus").DbFiles.Add(sDbcFileFolder + "CANExample.dbc") 
# End of settings
#Convert files 
aFoundFiles = dd.DirListGet(sLogFileFolder, sLogFileExt, "filename", "FullFilenames") 
if IsArray(aFoundFiles) : 
    for iCount in range( 0, len(aFoundFiles) + 1): 
        dd.BusLogToTDM.LogSettings.LogFiles.RemoveAll() 
        dd.BusLogToTDM.LogSettings.LogFiles.Add(aFoundFiles(iCount)) 
        sLogFileName = dd.FileNameSplit(aFoundFiles(iCount),"N") 
        dd.BusLogToTDM.ResultSettings.ResultFile = sResultFileFolder + sLogFileName + ".tdm" 
        dd.BusLogToTDM.Convert() 
```

<!--NI_TOPIC bundle=diadem path=dlgcanconverter/dlgcanconverter/dlgcanconv_gin_select_dialog.htm language=enus -->
## TOPIC 00224: Multiple Selection for GIN Logfiles

- bundle_id: `diadem`
- source_path: `dlgcanconverter/dlgcanconverter/dlgcanconv_gin_select_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgcanconverter/dlgcanconverter/dlgcanconv_gin_select_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../dlgcanconverter/canconverter_overview.htm) > [Bus Log Converter](../dlgcanconverter/dlgcanconv_main_dialog.htm) > Multiple Selection for GIN Logfiles

Multiple Selection for GIN Logfiles

Use this dialog box to select several GIN logfiles which the Bus Log Converter converts into a TDM file. DIAdem lists all selected logfiles in the Bus Log Converter.

#### Settings

|  | Add Logfiles to Configuration | Opens the dialog box where you select or create a GIN logfile. |
| --- | --- | --- |
|  | Remove Logfile | Removes the selected GIN logfiles from the configuration. |
|  | Move Logfile Up | Moves the selected logfile one line up in the overview. You also can select and move several consecutively listed files. |
|  | Move Logfile Down | Moves the selected logfiles one line down in the overview. You also can select and move several consecutively listed files. |
|  | No. | Specifies the number of the logfile in the overview. |
|  | Logfile | Displays the name of the logfile. |

<!--NI_TOPIC bundle=diadem path=dlgcanconverter/dlgcanconverter/dlgcanconv_main_dialog.htm language=enus -->
## TOPIC 00225: Bus Log Converter

- bundle_id: `diadem`
- source_path: `dlgcanconverter/dlgcanconverter/dlgcanconv_main_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgcanconverter/dlgcanconverter/dlgcanconv_main_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../dlgcanconverter/canconverter_overview.htm) > Bus Log Converter

Bus Log Converter

Use this dialog box to configure and to execute the conversion of Bus logfiles to the TDM format. Determine the logfile with the file type and the bus configuration and specify the target file.

On the [Conversion of Logfiles with a Script](../dlgcanconverter/dlgcanconv_example_script.htm) page you will find a script that enables you to convert all logfiles from a folder into the TDM format. Press <Ctrl-Shift-C> to also record the current settings of the dialog box that is open, in the recording mode. If the recording mode is not enabled, press <Ctrl-Shift-C> to copy the settings of the open dialog box to the clipboard.

#### Settings

|  | File type | Specifies the type of logfile that the Bus Log Converter converts into the TDM format. |
| --- | --- | --- |
|  | Logfile | Shows the name and the path of the logfile to be converted.If you select several logfiles in GIN format, this field shows the name of the files. |
|  | Select logfile | Opens the dialog box where you select a logfile of the format selected under File type.If you select the GIN file type, the dialog box Multiple Selection for GIN Logfiles opens. In this dialog box you can select several logfiles in GIN format. |
|  | File size | Displays the file size of the loaded logfile. |
|  | Name | Displays the name of the bus-database configuration.Specifies the name of the bus-database configuration in the Edit Bus-Database Configuration dialog box. |
|  | Edit | Opens the dialog box Edit Bus-Database Configuration where you link the buses from a logfile to the associated database files. |
|  | Bus filter | Specifies that the Bus Log Converter uses specific buses for the conversion. |
|  | Bus name | Specifies the name of a bus. Use the checkboxes to specify whether the converter includes this bus in the conversion. |
|  | Replace signal text | Specifies whether the Bus Log Converter ignores assignments in the file to be converted and replaces them by NoValues in the TDM file. |
|  | Create sequence channel | Specifies that the Bus Log Converter creates an additional channel, which records the sequence of the telegrams, for each group. |
|  | Time filter | Specifies that the Bus Log Converter converts only telegrams from a specified time range. |
|  | From | Specifies the beginning of the time domain. |
|  | To | Specifies the end of the time domain. |
|  | Ignore first frames | Specifies that the Bus Log Converter ignores the first frames when converting. |
|  | Number | Specifies the number of frames at the beginning, which the Bus Log Converter ignores when converting. |
|  | Load | Opens the dialog box where you load the Bus Log Converter settings. |
|  | Save As | Opens the dialog box where you load the Bus Log Converter settings into a TCC file. |
|  | Reset | Rejects all settings and uses the standard settings of the Bus Log Converter. |
|  | TDM file | Displays the name and path of the TDM file into which the Bus Log Converter saves the converted logfile. |
|  | Select TDM File | Opens the dialog box where you select or create a TDM logfile. |
|  | Delete data in the Data Portal and load TDM file. | Specifies that DIAdem deletes the internal data and loads the TDM file into the Data Portal after the conversion. |
|  | Load TDM file | Specifies that DIAdem loads the TDM file after the conversion and adds it to the data store in the Data Portal. |
|  | Create TDM file only | Specifies that DIAdem converts the logfile and creates the TDM file without loading the file into the Data Portal. |
|  | Close | Closes the Bus Log Converter without a conversion. |
|  | Convert | Converts the loaded logfile into the TDM format. |

#### Script Call

Call [BusLogToTDM](../../icanconverter/objects/canconverter_objects_icanconverter.htm).[ShowConvertDlg()](../../icanconverter/methods/canconverter_method_showconvertdlg_icanconverter.htm)

Call [BusLogToTDM](../../icanconverter/objects/canconverter_objects_icanconverter.htm).[Convert()](../../icanconverter/methods/canconverter_method_convert_icanconverter.htm)

<!--NI_TOPIC bundle=diadem path=dlgcanconverter/dlgcanconverter/dlgcanconv_xnet_select_dialog.htm language=enus -->
## TOPIC 00226: Select Clusters

- bundle_id: `diadem`
- source_path: `dlgcanconverter/dlgcanconverter/dlgcanconv_xnet_select_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgcanconverter/dlgcanconverter/dlgcanconv_xnet_select_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Bus Log Converter](../dlgcanconverter/canconverter_overview.htm) > [Bus Log Converter](../dlgcanconverter/dlgcanconv_main_dialog.htm) > [Edit Bus-Database Configuration](../dlgcanconverter/dlgcanconv_busdbconf_dialog.htm) > Select Clusters

Select Clusters

Use this dialog box to add clusters contained in the loaded Fibex database file to a bus. If the database file contains several clusters, you can select several.

#### Settings

| Fibex database | Displays the name and path of the database file. |
| --- | --- |
| Cluster | Lists all clusters that a database file contains. Select one or more clusters to add them to the new bus. If you do not select any clusters, DIAdem uses all clusters. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_dlgspackagevalues_overview.htm language=enus -->
## TOPIC 00227: Packet Processing Dialog Boxes

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_dlgspackagevalues_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_dlgspackagevalues_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem DAC](../dlgdacsv/dac_dlgs_overview.htm) > Packet Processing Dialog Boxes

Packet Processing Dialog Boxes

The subordinate topics contained in the tree on the contents tab of the Help describe the dialog boxes from the packet processing function groups of the DIAdem DAC packet processing.

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg/hb_frequbew.htm language=enus -->
## TOPIC 00228: Frequency Weighting

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg/hb_frequbew.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg/hb_frequbew.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > [Packet Blocks in the Complete Collection](../dac_packet_dlg_handling/dlgdigblnew_dialog.htm) > Frequency Weighting

Frequency Weighting

Use this packet block to evaluate time-related and frequency-related data, for example, the results of a FFT or third analysis, with a group of digital filters according to DIN IEC 651, and to output this data as an evaluated, time-related signal. The frequency weighting can differentiate between power spectrum, amplitude spectrum, and spectrum in dB as well as between third analysis, octave analysis, and linear frequency distribution. DIAdem must measure the input signal with a sampling rate greater than 24400 Hz.

Over the input signal at the control input S, you can change the evaluation during a measurement, for example, with a slider. For the value 0 at the signal input S, the packet block uses the **Linear frequency weighting**, for the value 1 the **A weighting**, for the value 2 the **B weighting**, and for the value 3 the **C weighting**.

The acoustic noise sensitivity of the human ear does not correspond to a linear frequency response. The higher and lower frequencies of an acoustic signal are muted for the human ear whereas the middle frequencies are perceived as slightly higher. The frequency weightings A,B, and C take this effect into account.

#### Settings

| Linear frequency weighting | Specifies that DIAdem outputs the input signal without an evaluation. |
| --- | --- |
| A weighting | Specifies that DIAdem evaluates and outputs the input signal with the A characteristic. The A weighting uses a volume of approximately 20-40 dB. |
| B weighting | Specifies that DIAdem evaluates and outputs the input signal with the B characteristic. The B weighting uses a volume of approximately 50-70 dB. |
| C weighting | Specifies that DIAdem evaluates and outputs the input signal with the C characteristic. The C weighting uses a volume of approximately 80-90 dB. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg/hb_pegelber.htm language=enus -->
## TOPIC 00229: Level Calculation

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg/hb_pegelber.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg/hb_pegelber.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > [Packet Blocks in the Complete Collection](../dac_packet_dlg_handling/dlgdigblnew_dialog.htm) > Level Calculation

Level Calculation

Use this packet block to calculate characteristic values for describing surrounding noise from a time-related acoustic signal. DIAdem must acquire the input signal with a sampling rate of over 24400 Hz to apply a [Frequency weighting](../dac_packet_dlg/hb_frequbew.htm) to the input signal.

You can control the level calculation during run time with the signal at the control input S:

| Control input S | Function | Description |
| --- | --- | --- |
| 1 | Reset Maximum | Resets the maximum and minimum value |
| 2 | Reset | Resets the level calculation |
| 4 | Pause | Stops the level calculation |

You can combine possible values of the control signal. The value 5, for example, causes a pause and a reset maximum. Use the bit switch to control the level calculation manually.

#### Settings

| RMS | Calculates the floating root mean square (RMS). |
| --- | --- |
| Peak value (peak) | Calculates the peak value. |
| Time analysis | Specifies the time constant for calculating the floating root mean square. |
| Clock period | Specifies a fixed period of time in which DIAdem acquires the maximum level of the clock. |
| Fade out time [s] | Specifies the time in seconds that DIAdem deletes from the calculations when the button is pressed. |
| Output frequency [Hz] | Specifies how fast DIAdem outputs the results. |

#### Structure of the Output Data Packets

For each input signal the data block outputs 18-channel data packets that contain all the calculated characteristic values. Characteristic values that are not calculated, for example, the continuous noise pressure level when **Peak** is set, receive the value 0. If the incoming data packets have multiple channels, the packet block outputs 18 channels for each further input signal. The packet block outputs the calculated characteristic values in the following order:

| Channel | Characteristics | Description |
| --- | --- | --- |
| 1st channel | Display value of the noise pressure level | Contains the calculated noise pressure level. If you select the settings RMS and the time analysis Impulse, DIAdem adds an inertia constant to the display in compliance with DIN IEC 651. The constant causes the displayed value to immediately follow the high level values, but to drop by a maximum of 2.9 dB/s, regardless of how fast the calculated level actually drops. |
| 2nd channel | Elapsed time since the start of the measurement or the last Reset All | Contains the time since the start of the measurement or the last reset all. If you use the pause button and the setting Fade out time, the elapsed time is not the actual measurement period. |
| 3rd channel | Real measurement time since the start of the measurement or the last Reset All | Contains the real measurement period. |
| 4th channel | Measurement period since the last Reset Maximum or the last Reset All | Contains the real measurement duration since the last maximum. In a RMS calculation the maximum value and the minimum value can be reset regardless of other values. |
| 5th channel | Current noise pressure level | Contains the peak level that occurs in a instantaneous value calculation.Contains the total of the current level and the previous level values weighted with the time constants Tc (S,F,I), in a RMS calculation. |
| 6th Channel | Maximum noise pressure level |  |
| 7th channel | Minimum noise pressure level |  |
| 8th channel | Impulse or continuous noise pressure level | Contains the mean noise pressure level which is the continuous noise pressure level when the time analysis settings are Slow and Fast, in RMS calculations. If you select the Impulse time analysis, the averaging result is called an impulse noise level because the changes occur very fast. |
| 9th channel | Noise exposure level | Contains the mean value standardized to a second, in an RMS calculation. The noise exposure level evaluates the phenomenon that low but persistent noises are almost as unpleasant as short loud noises. |
| 10th channel | Clock maximum level | Contains the maximum noise pressure level in a limited period of 1, 3 or 5 seconds to highlight the maximum strain in a certain time interval. |
| 11th channel | Averaged clock maximum level | Contains the average of the measured clock maximum level to receive a value for persistent noise strain. This value can provide limit values for acceptable strain. |
| 12th channel | Percentile level for 1 % | Contains the level value that 1% of the measurement values exceed.You can classify all the levels to characterize the properties of a noise emission. You can see whether a signal is uniform or whether the strain consists of short intense noise levels, whereas otherwise the levels are low. |
| 13th channel | Percentile level for 5% | Contains the level value that 5% of the measurement values exceed. |
| 14th channel | Percentile level for 10% | Contains the level value that 10% of the measurement values exceed. |
| 15th channel | Percentile level for 50% | Contains the level value that 50% of the measurement values exceed. |
| 16th channel | Percentile level for 90% | Contains the level value that 90% of the measurement values exceed. |
| 17th channel | Percentile level for 95% | Contains the level value that 95% of the measurement values exceed. |
| 18th channel | Percentile level for 99% | Contains the level value that 99% of the measurement values exceed. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg/hb_trigsuch.htm language=enus -->
## TOPIC 00230: Trigger Finder

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg/hb_trigsuch.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg/hb_trigsuch.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > [Packet Blocks in the Complete Collection](../dac_packet_dlg_handling/dlgdigblnew_dialog.htm) > Trigger Finder

Trigger Finder

Use this packet block to monitor one data channel in multi-channel data packets and to output a control signal. The **Trigger finder** packet block outputs incoming data packets unchanged at the signal output A and outputs a control signal of the same length at the signal output Ts. The control signal contains the value 0 for TTL low and 5 for TTL high.

The **Trigger finder** packet block outputs a control signal when the monitored data channel has fulfilled the first condition. To output the next control signal the second condition must be fulfilled. You can use a retrigger, for example, to alleviate slight fluctuations in the signal.

#### Settings

| Selected channel | Specifies the number of the channel to monitor, in multi-channel data packets. |
| --- | --- |
| Type | Specifies which condition triggers a control signal. If you select a Slope or Window, the packet block returns a control signal (TTL high), as soon as the condition is true. If you select Region, the packet block returns a control signal (TTL high), as long as the monitored data signal is in the trigger region. |
| Slope: Limit | Specifies the type of triggering slope condition. |
| Threshold | Specifies the limit value of the slope. |
| Window: Threshold | Specifies the type of window condition to trigger. |
| Upper limit | Specifies the top window limit. |
| Lower limit | Specifies the bottom window limit. |
| Range: Threshold | Specifies whether the trigger event occurs inside or outside the region. |
| Upper limit | Specifies the top limit of the region. |
| Lower limit | Specifies the bottom limit of the region. |
| Automatic/Condition | Specifies whether the event retrigger is automatic or whether you define a condition for a retrigger. You can define a retrigger for a slope condition and a window condition. |
| Retrigger type | Specifies which condition triggers a retrigger. |
| Slope: Limit | Specifies the type of triggering slope condition. |
| Threshold | Specifies the limit value of the slope. |
| Window: Threshold | Specifies the type of window condition to trigger. |
| Top | Specifies the top window limit. |
| Bottom | Specifies the bottom window limit. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg/hb_tstueck.htm language=enus -->
## TOPIC 00231: Copy

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg/hb_tstueck.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg/hb_tstueck.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > [Packet Blocks in the Complete Collection](../dac_packet_dlg_handling/dlgdigblnew_dialog.htm) > Copy

Copy

Use this packet block to output data packets from an input signal to several packet buses simultaneously.

|  | Note To distribute data packets parallel to further packet blocks, you also can connect packet blocks on parallel packet buses. DIAdem implements a hidden copy block for each branch. Only use a Copy packet block to distribute an input signal on several packet blocks simultaneously. The Copy packet block can distribute data packets to multiple packet buses faster than branches. |
| --- | --- |

#### Settings

| Number of output channels | Specifies the number of signal outputs. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg/hb_verteilen.htm language=enus -->
## TOPIC 00232: Separate

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg/hb_verteilen.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg/hb_verteilen.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > [Packet Blocks in the Complete Collection](../dac_packet_dlg_handling/dlgdigblnew_dialog.htm) > Separate

Separate

Use this packet block to output channels from multi-channel data packets as single-channel data packets. The output signals are in the same order as the channels in the data packet. All the output data packets are the same size and have the same unit.

If the incoming data packets contain fewer channels than specified signal outputs, DIAdem does not output values to the surplus signal outputs. You do not need to connect every signal output to a packet bus, because DIAdem rejects the data packets of the open outputs without displaying an error message.

#### Settings

| Number of channels to be separated | Specifies the number of signal outputs. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm language=enus -->
## TOPIC 00233: Display and I/O

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Display and I/O

Display and I/O

The subordinate topics contained in the tree on the contents tab of the Help describe the dialog boxes in which you configure the display and I/O blocks.

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_disp_io/hb_datei.htm language=enus -->
## TOPIC 00234: File I/O

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_disp_io/hb_datei.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_disp_io/hb_datei.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Display and I/O](../dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm) > File I/O

File I/O

Use this packet block to read data from a file or to write measurement values into a file.

To read data from a file specify the filename and the path. You only need to connect a data bus to the signal output. With the repetition settings you specify how many values DIAdem reads and outputs repeatedly. Use the repetitions to evaluate the same values, for example, for a comparative operation.

To write data into a file you must connect a packet bus to the signal input. If you also connect a packet bus to the signal output, the packet block forwards the data to the block diagram at the same time.

#### Settings

| Filename | Specifies the name and path of the data file to be read or written. |
| --- | --- |
| Search | Opens the dialog box where you select the read data file or create a write data file. |
|  |  |
| Without repetition | Specifies that DIAdem reads the data once and outputs the data to the block diagram. |
| Repetition at packet end | Specifies that DIAdem reads the first data packet repeatedly and outputs it to the block diagram.If you entered a block size of, for example, 1000 values under Settings»Packet Processing»Default System Clock, DIAdem reads exactly 1000 values from the file and outputs these values as a data packet to the block diagram. At the first value DIAdem starts reading the same 1000 values from the file again. |
| Repetition at the file end | Specifies that DIAdem reads the file any number of times and outputs the values to the block diagram. |
|  |  |
| Only channel | Specifies that DIAdem reads only one data channel from a multi-channel file. |
| Number | Specifies the number of the data channel to be read. |
|  |  |
| Default | Specifies that DIAdem uses the packet size set in Settings»Packet Processing»Default System Clock. |
| Packet size | Specifies the packet size of the data packets to be read. |
|  |  |
| File format | Specifies the write File format. |
| Append (do not overwrite) | Specifies that DIAdem appends the write data if the data file exists, in each measurement. |
| Warning if file exists | Specifies that DIAdem overwrites existing data files in each measurement. If you answer the overwrite prompt with no, DIAdem only stops the packet processing. |
| Decimal comma (no point) | Specifies that DIAdem uses a comma as the decimal symbol when writing the file format Packet-ASCII. If you do not select this setting, DIAdem uses a decimal point. |
| Increment the file extension | Specifies that DIAdem sets a running index at the end of the filename or in place of the filename extension when DIAdem has written the specified number of data packets into a file.If you select the file format DIAdem, DIAdem uses the running index for the last three characters of the filename, for example, TESTD001.DAT and TESTD001.R32. The filename extensions remain unchanged. If you select a different file format, DIAdem writes the index instead of the filename extension. If you enter the filename TEST.DAT, for example, DIAdem saves the first data packets in the TEST.001 file. |
| After packets | Defines the maximum number of data packets in a file. |
| Max. count of files | Specifies the maximum number of files to create. When DIAdem reaches the maximum number of files, DIAdem overwrites the file created first. Use this setting to create a ring buffer. |
|  |  |
| Calculate X from offset and clock rate | Specifies that DIAdem calculates the time channel to be written, from the start time and the sampling rate. Use this setting to write data into a file quickly. |
| Store additional time channel | Specifies that DIAdem writes the date and time of acquisition into a time channel. DIAdem saves the absolute time in seconds that have elapsed since 01.01.1900. Use this setting to write data from slow measurements into a file. |
| Store additional x-channel | Specifies that DIAdem writes the measurement time in seconds, into a time channel. Use this measurement for measurements that acquire measurement values irregularly. |
|  |  |
| Data information | Opens the dialog box that displays file information of earlier DigiS files. |

|  |
| --- |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_disp_io/hb_datei_dateiformat.htm language=enus -->
## TOPIC 00235: File Formats of the Packet Block File I/O

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_disp_io/hb_datei_dateiformat.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_disp_io/hb_datei_dateiformat.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Display and I/O](../dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm) > [File I/O](../dac_packet_dlg_disp_io/hb_datei.htm) > File Formats of the Packet Block File I/O

File Formats of the Packet Block File I/O

The [File I/O](../dac_packet_dlg_disp_io/hb_datei.htm) packet block can write the following file formats:

| DIAdem | DIAdem writes the data in DIAdem DAT format. This format saves the descriptive information in a header file with the name extension dat and the measurement values in a separate file. DIAdem writes the measurement values blockwise in the REAL32 file format or in the INT16 file format.The File I/O packet block only can read data files in the DIAdem DAT format if the values are available blockwise. DIAdem interprets the first data channel of a file as a time channel. The File I/O packet block reads only implicit time channels and generates an implicit time channel when writing from the number as well as the minimum and maximum value of an explicit time channel. |
| --- | --- |
| Packet ASCII | DIAdem writes the data in ASCII format and saves the measurement values as text. Header data such as the step width of the time channel, are at the beginning of the file. |
| Packet binary (IEEE 32-bit real) | DIAdem writes the packet-binary format a lot faster than the ASCII format. A header is at the start of the file followed by the measurement values as 4-Byte real numbers in IEEE standard. |
| Packet binary (high-speed) | DIAdem writes the measurement values as integer values directly into the file. |
| DFS binary (IEEE 32-bit real) | DIAdem does not write data in multiple channels but sequentially stores the channel values: 1st value of the 1st channel, 1st value of the 2nd channel, 1st value of the 3rd channel, 2nd value of the 1st channel, and so on. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_disp_io/hb_generator.htm language=enus -->
## TOPIC 00236: Function Generator

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_disp_io/hb_generator.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_disp_io/hb_generator.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Display and I/O](../dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm) > Function Generator

Function Generator

Use this packet block to generate signals. When the measurement starts the time axis and the phase start at zero.

The function generator has the signal inputs FM and En. Use the signal input FM to apply a frequency modulation to the generated signal. Use the signal input n to control the output of the generated signal with a control signal. As long as the control input n receives TTL high, the function generator outputs the generated data packets.

#### Settings

| Waveform | Specifies the signal form. |
| --- | --- |
| Frequency | Specifies the frequency of a sine signal, a square signal, triangle signal, and an impulse signal. Enter a frequency value that is considerably lower than the Sampling rate. |
| Amplitude | Specifies the amplitude of the signal. |
| Unit | Specifies the unit of the amplitude. |
| Phase | Specifies the phase of a sine signal, a square signal, triangle signal, and an impulse signal. |
| Default clock | Specifies that the function generator uses the sampling rate and block size that are set when you select Settings»Packet Processing»Default System Clock to generate data packets. |
| Sampling rate | Specifies the sampling rate of the signal if you do not select Default clock. |
| Packet size | Specifies the packet size of the data packets if you do not select Default clock. |
| Generate data packets in real time | Specifies whether DIAdem generates data packets as fast as possible or with the specified clock rate and packet size. |
| Logarithmical frequency modulation | Specifies a logarithmic frequency modulation of the generated signal. Because the slope is 1 volt/octave, a voltage of one volt at the signal input FM produces a frequency duplication at the signal output. |
| Signal frequency in Hertz | Specifies that DIAdem reads the signal frequency in hertz from the data packets at the signal input FM. |

#### Examples

[Creating Data Sections](../../explonl/explonl/explonl_dac_av36.htm) | [Generating Signals (1)](../../explonl/explonl/explonl_dac_av22.htm) | [Generating Signals (2)](../../explonl/explonl/explonl_dac_ab4.htm) | [Linear Scaling and Two-Point Scaling](../../explonl/explonl/explonl_dac_av12.htm) | [Relay](../../explonl/explonl/explonl_dac_av34.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_disp_io/hb_read_matrix.htm language=enus -->
## TOPIC 00237: DATA Reader

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_disp_io/hb_read_matrix.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_disp_io/hb_read_matrix.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Display and I/O](../dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm) > DATA Reader

DATA Reader

Use this packet block to read several data channels from the Data Portal and to output the read in data packets to the block diagram.

Use the settings **Repeat first packet** or **Repeat at end of channel** to create a continuous flow of data packets. The amount of created data packets depends on how many data packets the following packet blocks can process. Refer to [Data Flow in Packet Processing](../../gendacpp/dac_packet_general/hal_zeitverhalten.htm) for more information.

#### Settings

| Repeat first packet | Specifies that DIAdem reads the first data packet of each data channel any number of times and outputs it to the block diagram. |
| --- | --- |
| Repeat at end of channel | Specifies that DIAdem reads each data channel repeatedly and outputs it to the block diagram. |
| Stop at end of channel | Specifies that DIAdem reads each data channel once and outputs it to the block diagram. |
| Stop after first packet | Specifies that DIAdem reads values for a data packet and outputs the values to the block diagram. |
| Packet size | Specifies how many values DIAdem reads from each data channel. |
| Default | Specifies that DIAdem uses the sampling rate set in Settings»Packet Processing»Default System Clock to create the x-channel. |
| Manual input | Specifies that DIAdem uses a user-defined sampling rate to create the x-channel. |
| X rate (no units) | Specifies the sampling rate for generating the x-channel. |
| Y-Channels | Displays the data channels available in the Data Portal. You can select single data channels or groups of channels that do not have to be connected. |
| Enabled | Enables the channels selected in the overview. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_disp_io/hb_tcp_ip_client.htm language=enus -->
## TOPIC 00238: Network Client

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_disp_io/hb_tcp_ip_client.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_disp_io/hb_tcp_ip_client.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Display and I/O](../dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm) > Network Client

Network Client

Use this packet block to receive data packets from a net client, in a network. The packet blocks **Network Server** and **Network Client** use the TCP/IP logfile.

Net clients register at the net server via the network in order to request data. The net server reads data packets from a running measurement in order to offer these data packets to a net client.

#### Settings

| Port number | Specifies the port number of the net client. DIAdem uses the entered port number with a offset of 1025. The entry 5 means an internal port number of 1030. If other programs or DIAdem server blocks already use this port number, DIAdem does not transfer any data. |
| --- | --- |
| Host name or address | Specifies the IP address of the computer. |
| Logfile | Specifies that DIAdem records the data transfer. The logfile contains information, such as the initialization or the network protocol used. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_disp_io/hb_tcp_ip_server.htm language=enus -->
## TOPIC 00239: Network Server

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_disp_io/hb_tcp_ip_server.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_disp_io/hb_tcp_ip_server.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Display and I/O](../dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm) > Network Server

Network Server

Use this packet block to send data packets to a net client, in a network. The packet blocks **Network Server** and **Network Client** use the TCP/IP logfile.

The net server reads data packets from a running measurement and offers these data packets to a net client. Net clients on other computers can register with the net server via the network and request data.

#### Settings

| Port number | Specifies the port number of the net server. DIAdem uses the entered port number with a offset of 1025. The entry 5 means an internal port number of 1030. If other programs or DIAdem server blocks already use this port number, DIAdem does not transfer any data. |
| --- | --- |
| Host name or address | Specifies the IP address of the computer. |
| Non-blocking | Specifies that, when the transfer rate is slow, DIAdem rejects data packets in order to send the current data packet. This setting does not send the complete data to the net client. However it avoids blocking the transfer. |
| Blocking | Specifies that, when the transfer rate is slow, DIAdem transfers the complete data packets. This setting can lead to a data jam which might block or even abort the measurement. |
| Logfile | Specifies that DIAdem records the data transfer. The logfile contains information, such as the initialization or the network protocol used. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_disp_io/hb_write_matrix.htm language=enus -->
## TOPIC 00240: DATA Writer

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_disp_io/hb_write_matrix.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_disp_io/hb_write_matrix.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Display and I/O](../dac_packet_dlg_disp_io/dac_dlgspacketvalues_disp_io_overview.htm) > DATA Writer

DATA Writer

Use this packet block to write data packets into the Data Portal and to output the data packets to the block diagram. DIAdem creates the new data channels in the default group of the Data Portal.

#### Settings

| Continuous | Specifies that DIAdem writes data packets into the Data Portal until the available storage space is full. |
| --- | --- |
| N packages | Specifies that DIAdem writes a specified number of data packets into the Data Portal. |
| A number of packages | Specifies the number of data packets. |
| Writes n values | Specifies that DIAdem writes a specified number of values into the Data Portal. |
| N values | Specifies the number of values. |
| Write only the last package | Specifies that DIAdem writes only the data packet acquired last into the Data Portal. If you use this setting, DIAdem does not forward data packets to the signal output. |
| Do not search new channels | Specifies that DIAdem writes all data into the first data channel. |
| At the end of the channel | Specifies that DIAdem creates a new data channel as soon as a data channel is full. |
| After each package | Specifies that DIAdem writes each data packet into a separate data channel. |
| 1 x-channel | Specifies that DIAdem creates an x-channel. |
| No x-channel | Specifies that DIAdem does not create an x-channel. |
| Always new channels | Specifies that DIAdem creates an x-channel to each y-channel. |

|  | Note If you use the settings A number of packages and A number of values, DIAdem does not abort the measurement when the specified number is reached. |
| --- | --- |

#### Examples

Use the setting **Write only last package** to write the result of a classification into the Data Portal while the block diagram displays online the interim results.

Use the settings **Automatic channel search after each package** and **1 x channel** for saving FFT results in order to save the results in separate data blocks with a joint x data channel. The x-values are identical for each FFT result.

Use the settings **A number of values** and **No new channels** to save a greater number of measurement values in a data channel.

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm language=enus -->
## TOPIC 00241: Signal Processing

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Signal Processing

Signal Processing

The subordinate topics contained in the tree on the contents tab of the Help describe the configuration dialog boxes for signal processing blocks.

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/dlgdigblnew_dialog.htm language=enus -->
## TOPIC 00242: Complete Selection/Packet Processing Selection

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/dlgdigblnew_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/dlgdigblnew_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Complete Selection/Packet Processing Selection

Complete Selection/Packet Processing Selection

Use this dialog box to insert packet blocks that are not available in the packet processing function groups, into a block diagram. Select a packet driver and then a packet block. Click **Select** to configure the selected packet block and to insert the block into the block diagram. Click **Close** to finish the selection.

#### Settings

| Packet driver | Specifies a packet processing function library. |
| --- | --- |
| Block type | Specifies a packet block from the selected function library. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/dlgpacketclock_dialog.htm language=enus -->
## TOPIC 00243: Clock

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/dlgpacketclock_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/dlgpacketclock_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Clock

Clock

Use this packet block to change the packet call clock or to display the packet processing status.

To change the rate of the packet call in the block diagram connect the packet block **PacketClock** to the single point block **System clock** via a system bus. Enter the sampling rate at which DIAdem calls the packet blocks, in the system clock block. To change the packet call clock in relation to the event you also can connect a control block to the control input of the system clock block.

To display the status of the packet processing connect the packet block **PacketClock** to the control instrument **Digits** in single point processing. As long as the packet blocks are running the digit gauge displays a 1. As soon as, for example, the [Stop block](../dac_packet_dlg_handling/hb_stop.htm) stops the packet processing, the digits gauge displays a 0 because the measurement continues.

#### Settings

| Name | Specifies the unique block name in the block diagram. |
| --- | --- |

|  | NoteYou specify the packet call clock in the Settings»Packet Processing»Default System Clock dialog box. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/dlgpacketexport_dialog.htm language=enus -->
## TOPIC 00244: Pack: Parameters

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/dlgpacketexport_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/dlgpacketexport_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Pack: Parameters

Pack: Parameters

Use this packet block to connect packet blocks to single point blocks. The **Pack** packet block combines values from one data bus in single point processing and outputs the data packets to a packet bus.

If you connect a system clock block from single point processing at the top block edge of the clock input, the clock rate of the system clock determines the output rate of the data packets. If you do not connect a system clock block, DIAdem uses the single point clock specified in **Settings»Single Point Processing»Default System Clock**.

#### Settings

|  | Name | Specifies the unique block name in the block diagram. |
| --- | --- | --- |
|  | Packet size | Specifies the Packet size of the data packets. |
|  | Extend List | Adds a signal to the end of the list. |
|  | Reduce List | Deletes the signal at the end of the list. |
|  | List Length | Opens the dialog box where you specify the number of possible signals at one block. |
|  | Signal Name | Contains the name of the connected signal. You specify the signal names in the connected signal block. Use the Connect Signals dialog box to specify which signals DIAdem displays. |
|  | Terminal No.. | Specifies the number of the terminal on the measurement hardware used. |
|  | Enabled | Specifies whether a signal is active. |
|  | Terminal Name | Specifies the terminal name. Use the Connect Signals dialog box to connect signals to terminals. |

#### Further Settings

Parameters | [Inputs»Data](../../dlgvis/dlgvis/dlgvisdatainps_dialog.htm) | [Inputs»System](../../dlgvis/dlgvis/dlgvissysinp_dialog.htm) | [Outputs»Data](../../dlgvis/dlgvis/dlgvisdataoutp_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/dlgpacketimport_dialog.htm language=enus -->
## TOPIC 00245: Unpack: Parameters

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/dlgpacketimport_dialog.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/dlgpacketimport_dialog.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Unpack: Parameters

Unpack: Parameters

Use this packet block to connect single point blocks to packet blocks. The **Unpack** packet block divides the data packets of a packet bus into single values and outputs the values to a data bus in single point processing.

If you connect a system clock block from single point processing at the top block edge of the clock input, the single points are output at the rate specified for the system clock. If you do not connect a system clock block, DIAdem uses the packet processing [Packet call clock](../../dlgdacsv/dac_dlg_menu/dlgpacketcycle_dialog.htm).

#### Settings

|  | Name | Specifies the unique block name in the block diagram. |
| --- | --- | --- |
|  | Repeat last value | Specifies that DIAdem outputs the last value until a new data packet arrives. |
|  | Transfer NoValue | Specifies that DIAdem outputs NoValues until a new data packet arrives. |
|  | Transfer no values | Specifies that DIAdem does not output any values until a new data packet arrives. |
|  | Extend List | Adds a signal to the end of the list. |
|  | Reduce List | Deletes the signal at the end of the list. |
|  | List Length | Opens the dialog box where you specify the number of possible signals at one block. |
|  | New Names | Assigns the current block name to existing signals. |
|  | Signal Name | Contains the name of the connected signal. You specify the signal names in the connected signal block. Use the Connect Signals dialog box to specify which signals DIAdem displays. |
|  | Terminal No.. | Specifies the number of the terminal on the measurement hardware used. |
|  | Enabled | Specifies whether DIAdem outputs the signal. |

#### Further Settings

Parameters | [Inputs»Data](../../dlgvis/dlgvis/dlgvisdatainp_dialog.htm) | [Inputs»System](../../dlgvis/dlgvis/dlgvissysinp_dialog.htm) | [Outputs»Data](../../dlgvis/dlgvis/dlgvisdataoutps_dialog.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/hb_2_punkt_skalierung.htm language=enus -->
## TOPIC 00246: 2-Point Scaling

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/hb_2_punkt_skalierung.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/hb_2_punkt_skalierung.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > 2-Point Scaling

2-Point Scaling

Use this packet block for linear data scaling. To define the straight line, assign the scaled values to measurement values. The expected value range of the input signal simplifies the automatic scaling for the subsequent visualization blocks.

#### Settings

| Measurement values: 1. Value | Specifies the measurement value for the first linear point. |
| --- | --- |
| Measurement values: 2. Value | Specifies the measurement value for the second linear point. |
| Scaled value: 1. Value | Specifies the scaled value for the first linear point. |
| Scaled value: 2. Value | Specifies the scaled value for the second linear point. |
| Unit | Specifies the unit of the physical value to be output. |
| Y-Max | Specifies the expected top limit for the value range of the input signal. |
| Y-Min | Specifies the expected bottom limit for the value range of the input signal. |

#### Examples

[Free Linearization](../../explonl/explonl/explonl_dac_av13.htm) | [Linear Scaling and Two-Point Scaling](../../explonl/explonl/explonl_dac_av12.htm) | [Monitoring a Dynamic Set Point Range](../../explonl/explonl/explonl_dac_av30.htm) | [Thermo Linearization](../../explonl/explonl/explonl_dac_av14.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/hb_extract.htm language=enus -->
## TOPIC 00247: Channel Manager

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/hb_extract.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/hb_extract.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Channel Manager

Channel Manager

Use this packet block to extract channels from multi-channel data packets. The channel manager forwards the extracted channels at the data output A to the block diagram. The data output E forwards the input signal unchanged. To extract further channels from the input signal you can connect another channel manager to the data output E.

#### Settings

| Fixed channel list | Specifies that you enter the channel numbers of the channels to be output. |
| --- | --- |
| Channels from control input | Specifies that DIAdem reads the channel numbers from the data packets incoming at control input S. |
| Channel numbers | Specifies the output channels in a channel list. For example, specify the channel list as 1-6,17. The example corresponds to channels 1 to 6 and channel 17. |

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/hb_geraden_skal.htm language=enus -->
## TOPIC 00248: Linear Scaling

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/hb_geraden_skal.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/hb_geraden_skal.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Linear Scaling

Linear Scaling

Use this packet block to scale data with a linear equation. The linear equation has the following formula:

Physical value = Factor * Measured value + Offset

The expected value range of the input signal simplifies the automatic scaling for the subsequent visualization blocks.

#### Settings

| Factor | Specifies the factor of the linear equation. |
| --- | --- |
| Offset | Specifies the offset of the linear equation. |
| Unit | Specifies the unit of the physical value to be output. |
| Y-Max | Specifies the expected top limit for the value range of the input signal. |
| Y-Min | Specifies the expected bottom limit for the value range of the input signal. |

#### Examples

[Free Linearization](../../explonl/explonl/explonl_dac_av13.htm) | [Linear Scaling and Two-Point Scaling](../../explonl/explonl/explonl_dac_av12.htm) | [Monitoring a Dynamic Set Point Range](../../explonl/explonl/explonl_dac_av30.htm) | [Thermo Linearization](../../explonl/explonl/explonl_dac_av14.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/hb_mehrpunkt_skal.htm language=enus -->
## TOPIC 00249: Multiple Point Scaling

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/hb_mehrpunkt_skal.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/hb_mehrpunkt_skal.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Multiple Point Scaling

Multiple Point Scaling

Use this packet block to scale data with a nonlinear calibration curve. The packet block at data input K receives the calibration curve. Further calibration curves can arrive during a measurement to change the calibration dynamically. The expected value range of the input signal simplifies the automatic scaling for the subsequent visualization blocks.

#### Settings

| Unit | Specifies the unit of the physical value to be output. |
| --- | --- |
| Y-Max | Specifies the expected top limit for the value range of the input signal. |
| Y-Min | Specifies the expected bottom limit for the value range of the input signal. |
| Dynamic calibration points | Specifies that new calibration curves arrive at data input K during a measurement. If you do not select this setting, DIAdem uses the first calibration curve for the complete measurement. |

#### Examples

[Free Linearization](../../explonl/explonl/explonl_dac_av13.htm) | [Linear Scaling and Two-Point Scaling](../../explonl/explonl/explonl_dac_av12.htm) | [Monitoring a Dynamic Set Point Range](../../explonl/explonl/explonl_dac_av30.htm) | [Thermo Linearization](../../explonl/explonl/explonl_dac_av14.htm)

<!--NI_TOPIC bundle=diadem path=dlgdacpp/dac_packet_dlg_handling/hb_relais.htm language=enus -->
## TOPIC 00250: Relay Switch

- bundle_id: `diadem`
- source_path: `dlgdacpp/dac_packet_dlg_handling/hb_relais.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/dlgdacpp/dac_packet_dlg_handling/hb_relais.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Signal Processing](../dac_packet_dlg_handling/dac_dlgspacketvalues_signalprocessing_overview.htm) > Relay Switch

Relay Switch

Use this packet block to enable the output of data packets or to switch between two data outputs. The signal at control input S controls the relay switch.

#### Settings

| Switch on/off | Specifies that the relay switch works as an On/Off switch. |
| --- | --- |
| Switch output | Specifies that the relay switch works as a Toggle switch. If you select this setting, DIAdem creates two data outputs A1 and A2. |
| Logic level at control input | Specifies that a control signal at the control input S controls the forwarding or the distributing of data packets to the data outputs. As long as the control input S receives a control signal (TTL high), the On/Off switch outputs the incoming data packets to the data output A and the Toggle switch outputs the data packets to the second data output A2. If the control input S does not receive a control signal, the On/Off switch rejects the incoming data packets and the Toggle switch outputs the incoming data packets to the first data output A1. |
| Data packet at control input | Specifies that a data signal at the control input S controls the forwarding or the distributing of data packets to the data outputs. As long as the control input S receives data packets, the On/Off switch outputs the incoming data packets to the data output A and the Toggle switch outputs the data packets to the second data output A2. If the control input S does not receive data packets, the On/Off switch rejects the incoming data packets and the Toggle switch outputs the incoming data packets to the first data output A1. |
| Interactive answer of user | Specifies that the user must confirm every output data packet.This setting holds up the following functions and can cause buffer overflows and timeouts. Use a Push button or switch at control input S to output data blocks manually. |
| Asynchronous | Specifies that the sampling rate and the packet size of the data signal and of the control signal can be different. |

#### Examples

[Relay](../../explonl/explonl/explonl_dac_av34.htm)
