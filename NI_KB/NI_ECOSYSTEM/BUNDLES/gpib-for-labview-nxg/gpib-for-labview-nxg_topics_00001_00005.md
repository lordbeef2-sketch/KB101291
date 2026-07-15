# NI DOCUMENT BUNDLE: gpib-for-labview-nxg

<!--NI_BUNDLE_CHUNK bundle=gpib-for-labview-nxg start=1 end=5 -->
<!--NI_TOPIC bundle=gpib-for-labview-nxg path=advanced-gpib-initialization-and-misc-functions-and-visa-functions.html language=enus -->
## TOPIC 00001: Advanced GPIB Initialization and Misc Functions and VISA Functions

- bundle_id: `gpib-for-labview-nxg`
- source_path: `advanced-gpib-initialization-and-misc-functions-and-visa-functions.html`
- source_url: https://docs-be.ni.com/bundle/gpib-for-labview-nxg/raw/resource/enus/advanced-gpib-initialization-and-misc-functions-and-visa-functions.html
- document_id: `gpib-for-labview-nxg`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table maps advanced GPIB Initialization and Misc functions to the equivalent VISA functions. Advanced GPIB Initialization and Misc Functions and VISA Functions GPIB Action GPIB Function VISA Action VISA Function LabVIEW LabVIEW NXG Inputs Outputs LabVIEW NXG Inputs Outputs GPIB Initial

Advanced GPIB Initialization and Misc Functions and VISA Functions

The following table maps advanced GPIB Initialization and Misc functions to the equivalent VISA functions.

| GPIB Action | GPIB Function | VISA Action | VISA Function |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LabVIEW | LabVIEW NXG | Inputs | Outputs | LabVIEW NXG | Inputs | Outputs |  |  |
| GPIB Initialization: Require readdressing |  |  | require readdressing address string |  | VISA Property |  | session in (Instrument) Readdress To get or set property—Instrument properties»GPIB Settings»Readdressing | session out |
| GPIB Initialization: Assert REN with IFC |  |  | assert REN when IFC address string |  | VISA Send Remote Local Command |  | session in (GPIB Board Interface) mode: Assert REN Deassert REN | session out |
| GPIB Initialization: System Controller |  |  | system controller address string |  | VISA Property |  | session in (GPIB Board Interface) SysCntrl State To get or set property—GPIB Board Interface»GPIB Settings»System Controller State | session out |
| GPIB Initialization: IST bit sense (Individual Status bit) |  |  | address string IST bit sense |  | VISA action does not support Parallel Poll calls |  |  |  |
| GPIB Initialization: Disallow DMA |  |  | address string disallow DMA |  | VISA Property |  | session in (GPIB Board Interface, Instrument) Allow DMA To get or set property— GPIB Board Interface»General Settings»Allow DMA Transfers Instrument»General Settings»Allow DMA Transfers | session out |
| GPIB Misc: command to Become Active Controller |  |  | command string: "cac [0/1]" | output string status | VISA GPIB Control ATN |  | session in (GPIB Board Interface) mode: Assert ATN Assert ATN Immediately | session out |
| GPIB Misc: command to Send IEEE 488 commands |  |  | command string: "cmd [string]" (refer to the IEEE 488 Command Messages table for possible command strings) | output string status | VISA GPIB Send Command |  | session in (GPIB Board Interface) command (refer to the IEEE 488 Command Messages table for possible command strings) | session out return count |
| GPIB Misc: command to set DMA or programmed I/O mode |  |  | command string: "dma [0/1]" | output string status | VISA Property |  | session in (GPIB Board Interface, Instrument) Allow DMA To get or set property— GPIB Board Interface»General Settings»Allow DMA Transfers Instrument»General Settings»Allow DMA Transfers | session out |
| GPIB Misc: command to go from active controller to standby |  |  | command string: "gts [0/1]" | output string status | VISA GPIB Control ATN |  | session in (GPIB Board Interface) mode: Deassert ATN Deassert ATN with Handshake | session out |
| GPIB Misc: command to set Individual Status Bit |  |  | command string: "ist [0/1]" | output string status | VISA action does not support Parallel Poll calls |  |  |  |
| GPIB Misc: command for Local lockout |  |  | command string: "llo" | output string status | VISA Send Remote Local Command |  | session in (GPIB Board Interface) mode: Local Lockout (Addressed Devices) | session out |
| GPIB Misc: command to place controller in Local State |  |  | command string: "loc" | output string status | VISA action does not support this call |  |  |  |
| GPIB Misc: command to go to Local for an instrument |  |  | command string: "loc [address]" | output string status | VISA Send Remote Local Command |  | session in (Instrument) mode: Local Local without Lockout | session out |
| GPIB Misc: command to take controller offline |  |  | command string: "off" | output string status | VISA Close |  | session in (GPIB Board Interface) |  |
| GPIB Misc: command to take device offline |  |  | command string: "off [address]" | output string status | VISA Close |  | session in (Instrument) |  |
| GPIB Misc: command to pass control |  |  | command string: "pct [address]" | output string status | VISA GPIB Pass Control |  | session in (GPIB Board Interface) primary address secondary address | session out |
| GPIB Misc: command for parallel poll configure (enable and disable) |  |  | command string: "ppc [byte]" | output string status | VISA action does not support Parallel Poll calls |  |  |  |
| GPIB Misc: command for parallel poll configure |  |  | command string: "ppc [byte address]" | output string status | VISA action does not support Parallel Poll calls |  |  |  |
| GPIB Misc: command for parallel poll unconfigure |  |  | command string: "ppu" | output string status | VISA action does not support Parallel Poll calls |  |  |  |
| GPIB Misc: command to conduct parallel poll |  |  | command string: "rpp" | output string status | VISA action does not support Parallel Poll calls |  |  |  |
| GPIB Misc: command to release or request system control |  |  | command string: "rsc [0/1]" | output string status | VISA Property |  | session in (GPIB Board Interface) SysCntrl State To get or set property—GPIB Board Interface»GPIB Settings»System Controller State | session out |
| GPIB Misc: command to request service and/or set the serial poll status byte |  |  | command string: "rsv [byte]" | output string status | VISA Property |  | session in (GPIB Board Interface) Device STB To get or set property—GPIB Board Interface»Message Based Settings»Device Status Byte | session out |
| GPIB Misc: command to send interface clear |  |  | command string: "sic" | output string status | VISA GPIB Send Interface Clear |  | session in (GPIB Board Interface) | session out |
| GPIB Misc: command to assert or unassert remote enable |  |  | command string: "sre [0/1]" | output string status | VISA Send Remote Local Command |  | session in (GPIB Board Interface) mode: Assert REN Deassert REN | session out |

Parent topic:

GPIB-to-VISA Migration

<!--NI_TOPIC bundle=gpib-for-labview-nxg path=gpib-4882-functions-and-visa-functions-table.html language=enus -->
## TOPIC 00002: GPIB 488.2 Functions and VISA Functions

- bundle_id: `gpib-for-labview-nxg`
- source_path: `gpib-4882-functions-and-visa-functions-table.html`
- source_url: https://docs-be.ni.com/bundle/gpib-for-labview-nxg/raw/resource/enus/gpib-4882-functions-and-visa-functions-table.html
- document_id: `gpib-for-labview-nxg`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table maps GPIB 488.2 functions to the equivalent VISA Functions. GPIB 488.2 Functions and VISA Functions GPIB Action GPIB Function VISA Action VISA Function LabVIEW LabVIEW NXG Inputs Outputs LabVIEW NXG Inputs Outputs AllSpoll bus address list serial poll byte list status byte count

GPIB 488.2 Functions and VISA Functions

The following table maps GPIB 488.2 functions to the equivalent VISA Functions.

| GPIB Action | GPIB Function | VISA Action | VISA Function |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LabVIEW | LabVIEW NXG | Inputs | Outputs | LabVIEW NXG | Inputs | Outputs |  |  |
| AllSpoll |  |  | bus address list | serial poll byte list status byte count | VISA Read STB1 |  | session in (Instrument) | session out status byte |
| DevClear |  |  | bus address | status | VISA Clear |  | session in (Instrument) | session out |
| DevClearList |  |  | bus address list | status | VISA Clear1 |  | session in (Instrument) | session out |
| EnableLocal |  |  | bus address list | status | VISA GPIB Send Command (refer to the IEEE 488 Command Messages table for the command strings) |  | session in (GPIB Board Interface) command: example— MTA0, UNListen, MLA1, MLA2, MLA3, GTL Description—Make GPIB Board Interface 0 to be the Talker, issue UNListen, make three Listeners at Address 1, 2, and 3, then issue Go To Local | session out return count |
| EnableRemote |  |  | bus address list | status | VISA GPIB Send Command (refer to the IEEE 488 Command Messages table for the command strings) |  | session in (GPIB Board Interface) command: example— MTA0, UNListen, MLA1, MLA2, MLA3 Description—Make GPIB Board Interface 0 to be the Talker, issue UNListen, then make three Listeners at Address 1, 2, and 3 | session out |
| FindLstn |  |  | bus address list limit | listener address list status number of listeners | VISA Find Resource |  | expression: example— To scan for all the Instruments connected to the GPIB Interface Board 0, use a regular expression "GPIB0::?*INSTR"; alternatively, set up an array of addresses and loop through them return aliases if available | found resources |
| FindRQS |  |  | bus address list | requester status byte status requester index | VISA Read STB1 |  | session in (Instrument) | session out status byte |
| MakeAddr |  |  | primary address secondary address | packed address | Use the primary and secondary addresses with the session in |  | Session in: format to use—GPIB[board]::primary address[::secondary address][::INSTR] Optional string segments are shown in square brackets ([ ]) |  |
| PassControl |  |  | bus address | status | VISA GPIB Pass Control |  | session in (GPIB Board Interface) primary address secondary address | session out |
| PPoll |  |  | bus | parallel poll byte status | VISA action does not support Parallel Poll calls |  |  |  |
| PPollConfig |  |  | bus address dataline sense | status | VISA action does not support Parallel Poll calls |  |  |  |
| PPollUnconfig |  |  | bus address list | status | VISA action does not support Parallel Poll calls |  |  |  |
| RcvRespMsg |  |  | bus mode count | data string status byte count | VISA Read (use VISA GPIB Send Command first—refer to ReceiveSetup) |  | session in (GPIB Board Interface) byte count | session out read buffer |
| ReadStatus |  |  | bus address | serial poll response | VISA Read STB |  | session in (Instrument) | session out status byte |
| Receive |  |  | bus address mode count | data string status byte count | VISA Read |  | session in (GPIB Board Interface, Instrument) byte count | session out read buffer |
| ReceiveSetup |  |  | bus address | status | VISA GPIB Send Command (refer to the IEEE 488 Command Messages table for the command strings) |  | session in (GPIB Board Interface) command: example— UNListen, MLA0, MTA3 Description—Issue UNListen, make GPIB Board Interface 0 to be the Listener, then make Instrument at Address 3 to be the Talker | session out |
| ResetSys |  |  | bus address list | status | VISA GPIB Send Command (refer to the IEEE 488 Command Messages table for the command strings) |  | session in (GPIB Board Interface) command: example— DCL, MTA0, UNListen, MLA1, MLA2, MLA3 Description—Issue Device Clear, make GPIB Board Interface 0 to be the Talker, issue UNListen, then make three Listeners at Address 1, 2, and 3 | session out |
| VISA Write |  | session in (GPIB Board Interface, Instrument) write buffer: "*RST\\n" | session out return count |  |  |  |  |  |
| Send |  |  | bus address mode data string | status byte count | VISA Write |  | session in (GPIB Board Interface, Instrument) write buffer | session out return count |
| SendCmds |  |  | bus command string (refer to the IEEE 488 Command Messages table for the command strings) | status byte count | VISA GPIB Send Command |  | session in (GPIB Board Interface) command (refer to the IEEE 488 Command Messages table for the command strings) | session out return count |
| SendDataBytes |  |  | bus mode data string | status byte count | VISA Write (use VISA GPIB Send Command first—refer to SendSetup) |  | session in (GPIB Board Interface) write buffer | session out return count |
| SendIFC |  |  | bus | status | VISA GPIB Send Interface Clear |  | session in (GPIB Board Interface) | session out |
| SendList |  |  | bus address list mode data string | status byte count | VISA Write1 |  | session in (GPIB Board Interface, Instrument) write buffer | session out return count |
| SendLLO |  |  | bus | status | VISA Send Remote Local Command |  | session in (GPIB Board Interface) mode: Local Lockout (Addressed Devices) Local Local without Lockout | session out |
| SendSetup |  |  | bus address list | status | VISA GPIB Send Command (refer to the IEEE 488 Command Messages table for the command strings) |  | session in (GPIB Board Interface) command: example— MTA0, UNListen, MLA3 Description—Make GPIB Board Interface 0 to be the Talker, issue UNListen, then make Instrument at Address 3 to be the Listener | session out |
| SetRWLS |  |  | bus address list | status | VISA GPIB Send Command (refer to the IEEE 488 Command Messages table for the command strings) |  | session in (GPIB Board Interface) command: example— MTA0, UNListen, MLA1, MLA2, MLA3, LLO Description—Make GPIB Board Interface 0 to be the Talker, issue UNListen, make 3 Listeners at Address 1, 2, and 3, then issue Local Lockout | session out |
| SetTimeOut |  |  | new timeout | previous timeout | VISA Property |  | session in (GPIB Board Interface, Instrument) Timeout To get or set property— GPIB Board Interface»General Settings»Timeout Value Instrument»General Settings»Timeout Value | session out |
| TestSRQ |  |  | bus | SRQ status | VISA Property |  | session in (GPIB Board Interface) SRQ State To get property— GPIB Board Interface»GPIB Settings»Line SRQ State | session out |
| TestSys |  |  | bus address list | result list status failed devices | VISA Write1 |  | session in (GPIB Board Interface, Instrument) write buffer: "TST?\\n" | session out return count |
| VISA Read1 |  | session in (GPIB Board Interface, Instrument) byte count | session out read buffer |  |  |  |  |  |
| Trigger |  |  | bus address | status | VISA Software Trigger |  | session in (GPIB Board Interface, Instrument) | session out |
| TriggerList |  |  | bus address list | status | VISA Software Trigger1 |  | session in (GPIB Board Interface, Instrument) | session out |
| WaitSRQ |  |  | bus | SRQ status | VISA Wait on Event |  | wait timeout session in (GPIB Board Interface, Instrument) event type in: Service Request | session out event type out event out |
| 1For GPIB functions that take an address list, to set up the equivalent functionality in VISA, set up an array of addresses and use a loop to cycle through the VISA function. |  |  |  |  |  |  |  |  |

Parent topic:

GPIB-to-VISA Migration

<!--NI_TOPIC bundle=gpib-for-labview-nxg path=gpib-and-visa-functions-table.html language=enus -->
## TOPIC 00003: GPIB and VISA Functions

- bundle_id: `gpib-for-labview-nxg`
- source_path: `gpib-and-visa-functions-table.html`
- source_url: https://docs-be.ni.com/bundle/gpib-for-labview-nxg/raw/resource/enus/gpib-and-visa-functions-table.html
- document_id: `gpib-for-labview-nxg`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table maps GPIB functions to the equivalent VISA functions. GPIB and VISA Functions GPIB Action GPIB Function VISA Action VISA Function LabVIEW LabVIEW NXG Inputs Outputs LabVIEW NXG Inputs Outputs GPIB Clear address string status VISA Clear session in (Instrument) session out GPIB Rea

GPIB and VISA Functions

The following table maps GPIB functions to the equivalent VISA functions.

| GPIB Action | GPIB Function | VISA Action | VISA Function |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LabVIEW | LabVIEW NXG | Inputs | Outputs | LabVIEW NXG | Inputs | Outputs |  |  |
| GPIB Clear |  |  | address string | status | VISA Clear |  | session in (Instrument) | session out |
| GPIB Read Note: Both Synchronous and Asynchronous I/O modes are supported. |  |  | timeout ms address string byte count mode | data status | VISA Read Note: Only Asynchronous I/O mode is supported. |  | session in (GPIB Board Interface; Instrument) byte count | session out read buffer |
| GPIB Serial Poll |  |  | address string | serial poll byte status | VISA Read STB |  | session in (Instrument) | session out status byte |
| GPIB Status: ERR (Error Detected) TIMO (Timeout) END (EOI or EOS Detected) SRQI (SRQ Detected while CIC) CMPL (Operation Completed) LOK (Lockout State) REM (Remote State) CIC (Controller-In-Charge) ATN (Attention Asserted) TACS (Talker Active) LACS (Listener Active) DTAS (Device Trigger State) DCAS (Device Clear state) |  |  | address string | status GPIB error byte count | VISA Property Note: Only a subset of status bits can be obtained: SRQ State (SRQ Detected) while CIC) REN State (Remote State) Is CIC (Controller-In-Charge) ATN State (Attention Asserted) Address State (Talker Active or Listener Active) |  | session in (GPIB Board Interface) To get property—GPIB Board Interface»GPIB Settings» Line SRQ State Line REN State Is Controller In Charge Line ATN State Addressed State | session out State error out—use this to detect errors such as VI_ERROR_TMO (Timeout) |
| GPIB Trigger |  |  | address string | status | VISA Software Trigger |  | session in (GPIB Board Interface, Instrument) | session out |
| GPIB Wait: Device Clear State Device Trigger State Listener Active Talker Active Controller-In-Charge SRQ Detected while CIC |  |  | timeout ms address string wait state vector | status | VISA Wait on Event: Clear Trigger GPIB Listen GPIB Talk GPIB CIC Service Request |  | wait timeout session in (GPIB Board Interface) event type in | session out event type out event out |
| GPIB Wait: Attention Asserted Remote State Lockout State EOI or EOS Detected |  |  | timeout ms address string wait state vector | status | VISA action does not support these events For the Attention Asserted and Remote State events, you can use a Loop to check the VISA Property of ATN State and REN State: To get property— GPIB Board Interface»GPIB Settings»Line ATN State GPIB Board Interface»GPIB Settings»Line REN State Instrument»GPIB Settings»Line REN State |  |  |  |
| GPIB Wait for RQS |  |  | address string timeout ms | poll response byte | VISA Wait on Event: Service Request… |  | wait timeout session in (Instrument) event type in | session out event type out event out |
| Followed by VISA Read STB |  | session in (Instrument) | session out status byte |  |  |  |  |  |
| GPIB Write Note: Both Synchronous and Asynchronous I/O modes are supported. |  |  | timeout ms address string data mode | status | VISA Write Note: Only Asynchronous I/O mode is supported. |  | session in (GPIB Board Interface, Instrument) write buffer | session out return count |

Parent topic:

GPIB-to-VISA Migration

<!--NI_TOPIC bundle=gpib-for-labview-nxg path=gpib-to-visa.html language=enus -->
## TOPIC 00004: GPIB-to-VISA Migration

- bundle_id: `gpib-for-labview-nxg`
- source_path: `gpib-to-visa.html`
- source_url: https://docs-be.ni.com/bundle/gpib-for-labview-nxg/raw/resource/enus/gpib-to-visa.html
- document_id: `gpib-for-labview-nxg`
- page_type: `leaf`
- content_type: `reference`
- source_description: LabVIEW GPIB functions are deprecated in LabVIEW NXG. When you create new applications, use VISA functions equivalent to the deprecated GPIB functions. LabVIEW VISA is extensible and supports other hardware interfaces in addition to GPIB. If you are programming multiple devices that communicate over

GPIB-to-VISA Migration

LabVIEW GPIB functions are deprecated in LabVIEW NXG. When you create new applications, use VISA functions equivalent to the deprecated GPIB functions. LabVIEW VISA is extensible and supports other hardware interfaces in addition to GPIB. If you are programming multiple devices that communicate over more than one bus type, it is easier and more efficient to use VISA for your entire system.

Known Compatibility Issue Between GPIB and VISA Functions in LabVIEW NXG

Arbitration was built into LabVIEW to ensure VISA and GPIB functions that access instruments using the same GPIB Board Interface were synchronized. There is no arbitration in LabVIEW NXG, which may result in unexpected behavior including race conditions and intermittent errors. To prevent these problems, National Instruments recommends switching the deprecated GPIB functions to the equivalent VISA functions. This document assists you with the conversion. Refer to 
 *Converting GPIB Functions to VISA Functions in LabVIEW NXG* for more information.

If you need to make minor modifications using GPIB functions and do not want to convert your application to VISA, contact National Instruments [technical support](http://www.ni.com/en-us/support.html).

Converting GPIB Functions to VISA Functions in LabVIEW NXG

As a resource to help you convert an existing GPIB application to VISA in LabVIEW NXG, the following tables list each LabVIEW GPIB function along with the equivalent VISA function, where applicable.

- The *GPIB and VISA Functions* table maps GPIB functions to the equivalent VISA functions.
- The *Advanced GPIB Initialization and Misc Functions and VISA Functions* table maps advanced GPIB Initialization and Misc functions to the equivalent VISA functions.
- The *GPIB 488.2 Functions and VISA Functions* table maps GPIB 488.2 functions to the equivalent VISA functions.
- The *IEEE 488 Command Messages* table lists IEEE 488 command messages that are command bytes, which you can use to configure the GPIB state.

377077B-01

<!--NI_TOPIC bundle=gpib-for-labview-nxg path=ieee-488-command-messages.html language=enus -->
## TOPIC 00005: IEEE 488 Command Messages

- bundle_id: `gpib-for-labview-nxg`
- source_path: `ieee-488-command-messages.html`
- source_url: https://docs-be.ni.com/bundle/gpib-for-labview-nxg/raw/resource/enus/ieee-488-command-messages.html
- document_id: `gpib-for-labview-nxg`
- page_type: `leaf`
- content_type: `reference`
- source_description: The IEEE 488 Command Messages table lists IEEE 488 command messages that are command bytes, which you can use to configure the GPIB state. For more information about the messages table, refer to the ANSI/IEEE Standard 488.1-1987, IEEE Standard Digital Interface for Programmable Instrumentation, and

IEEE 488 Command Messages

The 
 *IEEE 488 Command Messages* table lists IEEE 488 command messages that are command bytes, which you can use to configure the GPIB state.

For more information about the messages table, refer to the ANSI/IEEE Standard 488.1-1987, 
 *IEEE Standard Digital Interface for Programmable Instrumentation*, and ANSI/IEEE Standard 488.1-2003, 
 *IEEE Standard for Higher Performance Protocol for the Standard Digital Interface for Programmable Instrumentation*.

Refer to the 
 *Multiline Interface Message Definitions* table below the 
 *IEEE 488 Command Messages* table for the message definitions.

| Hex | Decimal | ASCII | Message |
| --- | --- | --- | --- |
| 00 | 0 | NUL | — |
| 01 | 1 | SOH | GTL |
| 02 | 2 | STX | — |
| 03 | 3 | ETX | — |
| 04 | 4 | EOT | SDC |
| 05 | 5 | ENQ | PPC |
| 06 | 6 | ACK | — |
| 07 | 7 | BEL | — |
| 08 | 8 | BS | GET |
| 09 | 9 | HT | TCT |
| 0A | 10 | LF | — |
| 0B | 11 | VT | — |
| 0C | 12 | FF | — |
| 0D | 13 | CR | — |
| 0E | 14 | SO | — |
| 0F | 15 | SI | — |
| 10 | 16 | DLE | — |
| 11 | 17 | DC1 | LLO |
| 12 | 18 | DC2 | — |
| 13 | 19 | DC3 | — |
| 14 | 20 | DC4 | DCL |
| 15 | 21 | NAK | PPU |
| 16 | 22 | SYN | — |
| 17 | 23 | ETB | — |
| 18 | 24 | CAN | SPE |
| 19 | 25 | EM | SPD |
| 1A | 26 | SUB | — |
| 1B | 27 | ESC | — |
| 1C | 28 | FS | — |
| 1D | 29 | GS | — |
| 1E | 30 | RS | — |
| 1F | 31 | US | CFE |
| 20 | 32 | SP | MLA0 |
| 21 | 33 | ! | MLA1 |
| 22 | 34 | " | MLA2 |
| 23 | 35 | # | MLA3 |
| 24 | 36 | $ | MLA4 |
| 25 | 37 | % | MLA5 |
| 26 | 38 | & | MLA6 |
| 27 | 39 | ' | MLA7 |
| 28 | 40 | ( | MLA8 |
| 29 | 41 | ) | MLA9 |
| 2A | 42 | * | MLA10 |
| 2B | 43 | + | MLA11 |
| 2C | 44 | , | MLA12 |
| 2D | 45 | - | MLA13 |
| 2E | 46 | . | MLA14 |
| 2F | 47 | / | MLA15 |
| 30 | 48 | 0 | MLA16 |
| 31 | 49 | 1 | MLA17 |
| 32 | 50 | 2 | MLA18 |
| 33 | 51 | 3 | MLA19 |
| 34 | 52 | 4 | MLA20 |
| 35 | 53 | 5 | MLA21 |
| 36 | 54 | 6 | MLA22 |
| 37 | 55 | 7 | MLA23 |
| 38 | 56 | 8 | MLA24 |
| 39 | 57 | 9 | MLA25 |
| 3A | 58 | : | MLA26 |
| 3B | 59 | ; | MLA27 |
| 3C | 60 | < | MLA28 |
| 3D | 61 | = | MLA29 |
| 3E | 62 | > | MLA30 |
| 3F | 63 | ? | UNL |
| 40 | 64 | @ | MTA0 |
| 41 | 65 | A | MTA1 |
| 42 | 66 | B | MTA2 |
| 43 | 67 | C | MTA3 |
| 44 | 68 | D | MTA4 |
| 45 | 69 | E | MTA5 |
| 46 | 70 | F | MTA6 |
| 47 | 71 | G | MTA7 |
| 48 | 72 | H | MTA8 |
| 49 | 73 | I | MTA9 |
| 4A | 74 | J | MTA10 |
| 4B | 75 | K | MTA11 |
| 4C | 76 | L | MTA12 |
| 4D | 77 | M | MTA13 |
| 4E | 78 | N | MTA14 |
| 4F | 79 | O | MTA15 |
| 50 | 80 | P | MTA16 |
| 51 | 81 | Q | MTA17 |
| 52 | 82 | R | MTA18 |
| 53 | 83 | S | MTA19 |
| 54 | 84 | T | MTA20 |
| 55 | 85 | U | MTA21 |
| 56 | 86 | V | MTA22 |
| 57 | 87 | W | MTA23 |
| 58 | 88 | X | MTA24 |
| 59 | 89 | Y | MTA25 |
| 5A | 90 | Z | MTA26 |
| 5B | 91 | [ | MTA27 |
| 5C | 92 | \\ | MTA28 |
| 5D | 93 | ] | MTA29 |
| 5E | 94 | ^ | MTA30 |
| 5F | 95 | – | UNT |
| 60 | 96 | ` | MSA0, PPE |
| 61 | 97 | a | MSA1, PPE, CFG1 |
| 62 | 98 | b | MSA2, PPE, CFG2 |
| 63 | 99 | c | MSA3, PPE, CFG3 |
| 64 | 100 | d | MSA4, PPE, CFG4 |
| 65 | 101 | e | MSA5, PPE, CFG5 |
| 66 | 102 | f | MSA6, PPE, CFG6 |
| 67 | 103 | g | MSA7, PPE, CFG7 |
| 68 | 104 | h | MSA8, PPE, CFG8 |
| 69 | 105 | i | MSA9, PPE, CFG9 |
| 6A | 106 | j | MSA10, PPE, CFG10 |
| 6B | 107 | k | MSA11, PPE, CFG11 |
| 6C | 108 | l | MSA12, PPE, CFG12 |
| 6D | 109 | m | MSA13, PPE, CFG13 |
| 6E | 110 | n | MSA14, PPE, CFG14 |
| 6F | 111 | o | MSA15, PPE, CFG15 |
| 70 | 112 | p | MSA16, PPD |
| 71 | 113 | q | MSA17, PPD |
| 72 | 114 | r | MSA18, PPD |
| 73 | 115 | s | MSA19, PPD |
| 74 | 116 | t | MSA20, PPD |
| 75 | 117 | u | MSA21, PPD |
| 76 | 118 | v | MSA22, PPD |
| 77 | 119 | w | MSA23, PPD |
| 78 | 120 | x | MSA24, PPD |
| 79 | 121 | y | MSA25, PPD |
| 7A | 122 | z | MSA26, PPD |
| 7B | 123 | { | MSA27, PPD |
| 7C | 124 | \| | MSA28, PPD |
| 7D | 125 | } | MSA29, PPD |
| 7E | 126 | ~ | MSA30, PPD |
| 7F | 127 | DEL | — |

| Message | Definition |
| --- | --- |
| CFE | Configuration Enable (This multiline interface message is part of the IEEE 488.1-2003 specification and supports the HS488 high-speed protocol.) |
| CFG | Configure (This multiline interface message is part of the IEEE 488.1-2003 specification and supports the HS488 high-speed protocol.) |
| DCL | Device Clear |
| GET | Group Execute Trigger |
| GTL | Go To Local |
| LLO | Local Lockout |
| MLA | My Listen Address |
| MSA | My Secondary Address |
| MTA | My Talk Address |
| PPC | Parallel Poll Configure |
| PPD | Parallel Poll Disable |
| PPE | Parallel Poll Enable |
| PPU | Parallel Poll Unconfigure |
| SDC | Selected Device Clear |
| SPD | Serial Poll Disable |
| SPE | Serial Poll Enable |
| TCT | Take Control |
| UNL | Unlisten |
| UNT | Untalk |

Parent topic:

GPIB-to-VISA Migration
