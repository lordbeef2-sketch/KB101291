# NI DOCUMENT BUNDLE: ni-gpib-serial-converter

<!--NI_BUNDLE_CHUNK bundle=ni-gpib-serial-converter start=1 end=94 -->
<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/choosingbetweenmodes.html language=enus -->
## TOPIC 00001: Choosing Between Modes

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/choosingbetweenmodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/choosingbetweenmodes.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Choosing Between Modes

You can connect the GPIB-RS232/485/422 to a serial device and one or more GPIB devices. The way you use the serial device in your system setup determines the mode of operation to use.

If the serial device is the controller, use either S Mode or C Mode. If the GPIB device is the controller, use either G Mode or D Mode.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/choosingbetweensmodeandcmode.html language=enus -->
## TOPIC 00002: Choosing Between S Mode and C Mode

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/choosingbetweensmodeandcmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/choosingbetweensmodeandcmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Choosing Between S Mode and C Mode

Use S Mode when communicating with more than one GPIB device. You should also consider S Mode if you are using more advanced GPIB controller functionality beyond talker/listener functionality.

Use C Mode when communicating with a single GPIB device only using talker/listener functionality.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/clr.html language=enus -->
## TOPIC 00003: clr

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/clr.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/clr.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

clr

Clear Specified Device

#### Type

High-level bus management function

#### Syntax

**cl**r [alist]<CR>

#### Purpose

You can use clr to reset the internal or device functions of the specified GPIB devices. For example, a multimeter might require that you send it either the GPIB Device Clear or Selected Device Clear command to change its function, range, and trigger mode back to its default setting.

#### Remarks

The argument alist is a list of addresses separated by commas or spaces. addresses specify the GPIB addresses you want to clear.

If you call clr with alist, the GPIB-RS232/485/422 clears only the devices specified in alist (Selected Device Clear). If you call clr without alist, the GPIB-RS232/485/422 clears all devices (Device Clear).

If clr is the first function you call that requires GPIB Controller capability, and you have not disabled System Controller capability with rsc, the GPIB-RS232/485/422 sends Interface Clear (IFC*) to make itself CIC. It also asserts Remote Enable.

If you passed control to some other GPIB device, control must be passed back to you or you must send IFC* to make yourself CIC before making this call. Otherwise, the ECIC error is recorded.

#### See Also

GPIB Basics

Status and Error Message Information

#### Example 1

Selectively clear five devices.

```text
char  buffer [] = "clr 14+30,16+12,18,3+26,6\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 2

Issue a device clear to all devices.

```text
char  buffer [] = "clr\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/cmd.html language=enus -->
## TOPIC 00004: cmd

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/cmd.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/cmd.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

cmd

Send GPIB Commands

#### Type

Low-level bus management function

#### Syntax

**cm**d [#count]<LF> 

commands<CR>

#### Purpose

You can use cmd when the I/O and high-level bus management functions do not meet the needs of your device. cmd gives you precise control over the GPIB. For example, in applications that require command sequences not sent by other functions, you can use cmd to transmit any sequence of interface messages (commands) over the GPIB.

#### Remarks

The argument commands is a list of GPIB commands. These commands are represented by their ASCII character equivalents. For example, the GPIB Untalk (UNT) command is the ASCII character underscore (_). The GPIB commands, or interface messages, are listed in [Multiline Interface Messages](multilineinterfacemessages.html). They include device talk and listen addresses, secondary addresses, device clear and trigger messages, and other management messages.

The argument count is a numeric string preceded by a number sign (#). count specifies the number of GPIB command bytes (interface messages) to send, and can range from 1 to 4294967295. count must not include the <LF> or <CR> characters, which are used to terminate the programming message or string of GPIB command bytes.

If you call cmd without count, the GPIB-RS232/485/422 recognizes the end of the command string when it sees a <CR> or an <LF>. Consequently, count is required only if the command string contains a <CR> or <LF> character.

Do not terminate the cmd programming message with the <CR> character alone. Use either <LF> or <CR><LF> to terminate the programming message. If you use <CR> alone and the first character of the command string is <LF>, the GPIB-RS232/485/422 discards the <LF> as the second character of a <CR><LF> termination.

Do not use cmd to send programming instructions to devices. Use rd and wrt to send or receive device programming instructions and other device-dependent information. If the GPIB-RS232/485/422 is CIC but not Active Controller, it takes control and asserts ATN* before sending the command bytes. It remains Active Controller afterward.

The cmd operation terminates when:

- The GPIB-RS232/485/422 successfully transfers all commands.
- The GPIB-RS232/485/422 is not Controller-In-Charge. The ECIC error is recorded.
- The I/O time limit is exceeded. The EABO error is recorded.
- There is no device on the bus receiving the command bytes. The ENOL error is recorded.
- A serial port error occurs and is not ignored (refer to [spign](spignsmode.html) ).

After cmd terminates, the GPIB-RS232/485/422 records the number of command bytes it actually sent. If one of the errors described above occurs, the count might be less than expected.

If an error occurs and the GPIB-RS232/485/422 cannot transmit the entire command string, the GPIB-RS232/485/422 reads in and discards the remaining bytes of the command string.

#### See Also

[spign](spignsmode.html) and [Multiline Interface Messages](multilineinterfacemessages.html).

#### Example 1

Program the device at address 11 to listen and GPIB-RS232/485/422 at address 0 to talk. Then write the string ABCDE to the device at address 11.

```text
char  cmdBuffer [] = "cmd\n+@\r";
char  wrtBuffer [] = "wrt\nABCDE\r";
viWrite(instr, cmdBuffer, strlen(cmdBuffer), &retCount);
viWrite(instr, wrtBuffer, strlen(wrtBuffer), &retCount);
```

#### Example 2

Pass control to the device at GPIB address 23. 0x9 is the TCT command.

```text
char  buffer [] = "cmd #4\n_?W\x9\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/cmode.html language=enus -->
## TOPIC 00005: C Mode Overview

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/cmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/cmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

C Mode Overview

In C Mode, the GPIB-RS232/485/422 and a serial host together act as the GPIB System Controller. The following figure shows the C Mode system layout.

[IMAGE alt='image' src='cmodesystem.gif']

When you turn on the power with the GPIB-RS232/485/422 in C Mode, the GPIB-RS232/485/422 asserts IFC* for 500 µs and addresses an instrument to listen. On a GPIB system, asserting IFC* for at least 100 µs initializes the GPIB and causes the System Controller to become Controller-In-Charge (CIC). After the GPIB-RS232/485/422 becomes CIC, it addresses the PAD/SAD configured through configuration mode as a listener. The GPIB-RS232/485/422 always asserts REN* when addressing an instrument.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/conditionsthatcausesrqtobeasserted.html language=enus -->
## TOPIC 00006: Conditions that Cause SRQ to Be Asserted

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/conditionsthatcausesrqtobeasserted.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/conditionsthatcausesrqtobeasserted.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Conditions that Cause SRQ to Be Asserted

If SRQ is enabled, the GPIB-RS232/485/422 asserts the SRQ* signal on two conditions:

- When the GPIB-RS232/485/422 receives serial data that it needs to pass on to the GPIB port.
- When the GPIB input buffer becomes empty.

When the GPIB-RS232/485/422 serial input buffer is empty and the GPIB-RS232/485/422 receives a serial character to be sent along to the GPIB, the SRQ* signal is asserted. This alerts the GPIB Controller that the GPIB-RS232/485/422 has data to send to a GPIB Listener. The Controller can then address the GPIB-RS232/485/422 to talk so that the data can be read out of the GPIB-RS232/485/422 serial buffer. When the serial buffer is empty, the Controller can unaddress the GPIB-RS232/485/422 to talk and address other devices to transfer data on the bus.

SRQ* is also asserted when the GPIB input buffer becomes empty. When the GPIB-RS232/485/422 has emptied the buffer, it requests service, indicating it is ready for more data. The Controller can then readdress the GPIB-RS232/485/422 to listen and continue sending data until all data is sent.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/configurationofsmode.html language=enus -->
## TOPIC 00007: Configuration of S Mode

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/configurationofsmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/configurationofsmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Configuration of S Mode

When the GPIB-RS232/485/422 is configured to operate in S mode, it lets your serial device act as a Controller in the GPIB system, addressing one or more devices, and performing other GPIB Controller functions. For more details about S Mode operation, refer to [Programming in S Mode](programminginsmode.html).

S Mode requires the user to configure the serial settings used on the serial interface. The serial settings must exactly match the serial settings used on the host serial port. The serial settings are:

- Baud Rate —Number of bits transmitted over the serial interface per second
(300, 600, 1200, 2400, 4800, 9600, 19200, 38400, 57600, and 115200).
- Data Bits —Number of data bits that represent a serial byte.
  - 7 —Seven data bits per data byte.
  - 8 —Eight data bits per data byte.
- Parity —Parity algorithm used to detect serial errors.
  - None —No parity is used to detect serial errors.
  - Even —Data bits plus the parity bit sum to an even number.
  - Odd —Data bits plus the parity bit sum to an odd number.
- Stop Bits —Number of bits per byte used to indicate the end of the serial data byte.
  - 1 —One stop bit is used for every data byte.
  - 2 —Two stop bits are used for every data byte.
- Flow Control —Method used to ensure serial data is not lost.
  - Hardware —Hardware protocol used for flow control. For more information, refer to Hardware Handshaking .
  - XonXoff —Software implementation of the flow control protocol. For more information, refer to XON/XOFF Software Handshaking .
  - None —No flow control used.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/configurethehardware.html language=enus -->
## TOPIC 00008: Configure the Hardware

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/configurethehardware.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/configurethehardware.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Configure the Hardware

To configure the hardware, complete the following steps:

1. Set the configuration switch on the rear panel to CFG , as shown below.

 [IMAGE alt='image' src='rearpanelconfig.gif'] 

 [IMAGE alt='image' src='note.gif']
**Note** The switch is recessed to avoid unintentional toggling during operation of the GPIB-RS232/485/422. To flip the switch, a flathead screwdriver or similar tool may be required.
2. Power on the GPIB-RS232/485/RS422 using the power switch on the front of the unit. 

The PWR LED indicator should come on immediately. The RDY LED indicator blinks green after the hardware has passed its power-on self test, indicating it is ready for configuration. For more information, refer to LEDs .
3. Launch the NI GPIB-Serial Converter Wizard from Start»Programs»National Instruments»GPIB-Serial Converter .
4. Follow the onscreen instructions in the wizard.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/connectingthegpibrs232485422.html language=enus -->
## TOPIC 00009: Connecting the GPIB-RS232/485/422

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/connectingthegpibrs232485422.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/connectingthegpibrs232485422.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Connecting the GPIB-RS232/485/422

The NI GPIB-Serial Converter Wizard **Connect the GPIB-RS232/485/422** screen displays, as shown in the following figure.

[IMAGE alt='image' src='converterwizardconnect.gif']

You must now connect the GPIB-RS232/485/422 to your computer and set the GPIB-RS232/485/422 for Configuration mode.

You can connect the GPIB-RS232/485/422 via either GPIB or serial cable. If your computer has a GPIB interface, use a GPIB cable to connect your computer to your GPIB-RS232/485/422. If your computer does not have a GPIB interface, use a NULL modem serial cable to connect the GPIB-RS232/485/422 to your computer.

The GPIB-RS232/485/422 must now be set to run in Configuration mode. Follow these steps to run your GPIB-RS232/485/422 in Configuration mode:

1. Set the configuration switch on the GPIB-RS232/485/422 rear panel to CFG . Refer to Configure the Hardware for the configuration switch location.
2. Turn the power switch to OFF to turn off the GPIB-RS232/485/422. Refer to LEDs for the power switch location.
3. Turn the power switch to ON to restart the GPIB-RS232/485/422.

The GPIB-RS232/485/422 is now in Configuration mode. Click **Next** to to have the NI GPIB-Serial Converter Wizard detect serial and GPIB interfaces installed in your computer.

If at least one serial or GPIB interface is detected, proceed to [Selecting an Interface](selectinganinterface.html).

If the wizard cannot find any serial or GPIB interfaces on your computer, the **No Interfaces Detected** screen displays, as shown in the following figure.

[IMAGE alt='image' src='converterwizardnointerfaces.gif']

If the wizard appears as shown above, proceed to [No Interfaces Connected](nointerfacesconnected.html).

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/connectthehardware.html language=enus -->
## TOPIC 00010: Connect the Hardware

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/connectthehardware.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/connectthehardware.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Connect the Hardware

To connect the hardware, complete the following steps:

1. Connect either the GPIB or serial cable between the GPIB-RS232/485/422 and computer.
2. Connect the DC power plug of the DC power supply to the GPIB-RS232/485/422 hardware back panel and plug the power supply into an AC outlet.

|  | Caution Do not operate your GPIB-RS232/485/422 at any voltage other than that labelled on the unit. Doing so could damage the unit. |
| --- | --- |

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/conventions.html language=enus -->
## TOPIC 00011: Conventions

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/conventions.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/conventions.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Conventions

This help file uses the following formatting and typographical conventions:

| » | The » symbol leads you through nested menu items and dialog box options to a final action. The sequence File»Page Setup»Options directs you to pull down the File menu, select the Page Setup item, and select Options from the last dialog box. |
| --- | --- |
|  | This icon denotes a note, which alerts you to important information. |
|  | This icon denotes a caution, which advises you of precautions to take to avoid injury, data loss, or a system crash. |
| bold | Bold text denotes items that you must select or click in the software, such as menu items and dialog box options. Bold text also denotes parameter names. |
| dark red | Text in this color denotes a caution. |
| GPIB-RS232/485/422 | GPIB-RS232/485/422 refers to either the GPIB-RS232 or GPIB-RS485/RS422 box. |
| green | Underlined text in this color denotes a link to a help topic, help file, or Web address. |
| IEEE 488 and IEEE 488.2 | IEEE 488 and IEEE 488.2 refer to the ANSI/IEEE Standard 488.1-1987 IEEE 488.2 and ANSI/IEEE Standard 488.2-1992, respectively, which define the GPIB. |
| italic | Italic text denotes variables, emphasis, cross–references, or an introduction to a key concept. Italic text also denotes text that is a placeholder for a word or value that you must supply. |
| monospace | Text in this font denotes text or characters that you should enter from the keyboard, sections of code, programming examples, and syntax examples. This font is also used for the proper names of disk drives, paths, directories, programs, subprograms, subroutines, device names, functions, operations, variables, filenames, and extensions. |
| monospace bold | Bold text in this font denotes the messages and responses that the computer automatically prints to the screen. This font also emphasizes lines of code that are different from the other examples. |
| RS232 | RS232 refers to the ANSI/EIA-232-D standard. |
| RS422 | RS422 refers to the EIA-422-A standard. |
| RS485 | RS485 refers to the EIA-485 standard. |

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/copyright.html language=enus -->
## TOPIC 00012: Copyright

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/copyright.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/copyright.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Copyright

Under the copyright laws, this publication may not be reproduced or transmitted in any form, electronic or mechanical, including photocopying, recording, storing in an information retrieval system, or translating, in whole or in part, without the prior written consent of National Instruments Corporation.

National Instruments respects the intellectual property of others, and we ask our users to do the same. NI software is protected by copyright and other intellectual property laws. Where NI software may be used to reproduce software or other materials belonging to others, you may use NI software only to reproduce materials that you may reproduce in accordance with the terms of any applicable license or other legal restriction.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/datatransfersindmode.html language=enus -->
## TOPIC 00013: Data Transfers in D Mode

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/datatransfersindmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/datatransfersindmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Data Transfers in D Mode

When you are ready to send data to the GPIB-RS232/485/422 in D Mode, address the GPIB-RS232/485/422 to listen, if not already in listen-only mode. All GPIB data the GPIB-RS232/485/422 receives is buffered and passed along to the serial device. All serial data the GPIB-RS232/485/422 receives from the serial instrument is also buffered. When you are expecting to receive data from the serial device, address the GPIB-RS232/485/422 to talk, and all data received over the serial port is passed along to the GPIB port. The GPIB buffer size is 1 MB. The serial buffer size is 1 MB. The user cannot configure the sizes. This is a difference from the GPIB-232CV-A, which allowed the user to configure buffer sizes. For more information about this and other differences, refer to [Differences between the GPIB-232/485CT/CV-A and GPIB-RS232/485/422](differencesbetweentheoldgpib232485ctcvaandthenewgpibrs232485422.html).

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/deviceclear.html language=enus -->
## TOPIC 00014: Device Clear

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/deviceclear.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/deviceclear.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Device Clear

When the GPIB-RS232/485/422 receives the universal Device Clear (DCL) command, or its listen address and the Selected Device Clear (SDC) command, it clears both its status buffer and serial port receive buffer. It also resets the GPIB serial poll response byte to 0 and unasserts SRQ*.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/differencesbetweentheoldgpib232485ctcvaandthenewgpibrs232485422.html language=enus -->
## TOPIC 00015: Differences Between the GPIB-232/485CT/CV-A and GPIB-RS232/485/422

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/differencesbetweentheoldgpib232485ctcvaandthenewgpibrs232485422.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/differencesbetweentheoldgpib232485ctcvaandthenewgpibrs232485422.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Differences Between the GPIB-232/485CT/CV-A and GPIB-RS232/485/422

#### S Mode and G Mode

##### Enabling/Disabling XON/XOFF Flow Control

With the GPIB-232/485CT-A, you could enable the XON/XOFF protocol when sending data to the serial port independently from enabling the protocol when receiving data from the serial port.

The GPIB-RS232/485/422 does not allow such flexibility. It allows you to either enable the XON/XOFF protocol when sending and receiving data to/from the serial port, or disable the XON/XOFF protocol altogether. Thus, xon 0,1 and xon 1,0 are still syntactically valid, but they have the side effect of enabling the XON/XOFF protocol when the GPIB-RS232/485/422 both sends and receives serial data.

##### Function Arguments Syntax

The GPIB-RS232/485/422 enforces the following syntax rules for the function arguments: The first argument is separated from the function name with at least once space, and each additional argument is separated with at least once space or comma. The GPIB-232/485/CT/CV-A allowed no separation between function arguments.

##### id string

The id string has changed between the GPIB-232/485/CT/CV-A and GPIB-RS232/485/422.

The GPIB-232/485/CT/CV-A general id string format was as follows:

```text
GPIB-232/485CT-A Rev. B.3<CR><LF>
(c)1995 National Instruments<CR><LF>
256K bytes RAM<CR><LF>
```

The GPIB-RS232/485/422 general id string format is either of the following two formats:

```text
GPIB-RS232<CR><LF>
(c)2006 National Instruments<CR><LF>
Version 1.0.0f0<CR><LF>

GPIB-RS485 / RS422<CR><LF>
(c)2006 National Instruments<CR><LF>
Version 1.0.0f0<CR><LF>
```

#### S Mode

##### tmo Timeout Value Range

The GPIB-232/485/CT/CV-A timeout value range for both I/O and serial poll was between 0.00001 and 3600 seconds. The GPIB-RS232/485/422 accepts timeout values in the same range as valid parameter values. However, the effective timeout range allowed is between 0.0001 and 1000 seconds. Thus, any value less then 0.0001 seconds is treated as 0.0001 seconds, and any value greater then 1000 seconds is treated as 1000 seconds.

##### tmo Query Drops Trailing Zeros

When issued a tmo query, the GPIB-232/485/CT/CV-A returned values exactly as it was issued in the last tmo <ioval>, <spval> command. For example, if the tmo 10.0300 command was issued, the GPIB-232/485/CT/CV-A returned 10.0300. The GPIB-RS232/485/422 returns 10.03. Also, the GPIB-RS232/485/422 timeout default value is 10,0.1, whereas the GPIB-232/485/CT/CV-A default was 10.0,0.1.

##### echo Command Echoes Every Character

If <CR><LF> was used to terminate commands sent to the GPIB-232/485/CT/CV-A, it echoed only <CR>, but not <LF>. The GPIB-RS232/485/422 echoes both <CR> and <LF>.

##### sic

With the GPIB-232/485CT-A, you could provide a time argument to the sic command to change the amount of time the IFC line is asserted. The GPIB-RS232/485/422 ignores the time argument, but does not report an error. The GPIB-RS232/485/422 asserts IFC for at least 100 µs.

##### onl 1 and Restoring All Settings to Their Power-On Values

When the onl 1 command is issued to the GPIB-RS232/485/422, it restores all settings to their power-on values except the ones changed with the xon command. For example, if you issued the xon 1,1 command to enable XON/XOFF handshaking, followed by the onl 1 command, XON/XOFF handshaking is still enabled. The GPIB-232/485/CT/CV-A reset all settings to power-on values, including the ones changed with the xon command.

#### G Mode

##### GPIB-RS232/485/422 Device and <CR><LF>

The GPIB-RS232/485/422 does not return <CR><LF> when no response is available (that is, no query was sent and continuous status is not enabled). If you attempt to read from the GPIB-RS232/485/422, the read times out.

##### Serial Polls

The GPIB-232/485/CT/CV-A responded to serial polls on either the GPIB-232/485/CT/CV-A or serial device address. If the GPIB-232/485/CT/CV-A was asserting SRQ*, serial polling either address would make the GPIB-232/485/CT/CV-A unassert SRQ*. The GPIB-RS232/485/422 responds only to serial polls on the GPIB-RS232/485/422 address. Also, if the GPIB-RS232/485/422 is asserting SRQ*, serial polling only the GPIB-RS232/485/422 address makes the GPIB-RS232/485/422 unassert SRQ*.

##### Parallel Polls

The GPIB-RS232/485/422 does not support parallel poll functionality at this time. The GPIB-232/485/CT/CV-A implemented IEEE 488 Parallel Poll (PP) interface function subset PP1.

#### D Mode

##### Serial Buffer Size is Not Configurable

The GPIB-232CV-A had 256 KB of memory, shared between GPIB and serial buffers. The user had an option of setting the serial buffer size to be 32 bytes or 32 KB, with the GPIB buffer taking the remainder. The GPIB-RS232/485/422 has a 1 MB GPIB buffer and 1 MB serial buffer. Both buffers are significantly large to accommodate most applications, so a design decision was made to disallow the user to choose buffer sizes.

#### C Mode

##### Configuring No Address

The GPIB-232CV-A has an option to set all SW1 switches 1 through 5 on. The GPIB-RS232/485/422 does not have this option.

##### Terminating with EOI

On the GPIB-RS232/485/422, both <CR> and <LF> termination modes have the configurable option of asserting EOI (End Or Identity) on the GPIB bus on the terminating byte prior to readdressing the device as a Talker.

#### All Modes

The GPIB-RS232/485/422 now supports secondary addressing.

##### Hardware Handshaking

The CTS line default state (when not driven by a serial device on the other side) on the GPIB-232/485/CT/CV-A was pulled low. However, the CTS line default state on the GPIB-RS232/485/422 is pulled high. This means that if you enable hardware handshaking on the GPIB-RS232/485/422, and your serial cable or serial device does not support it, or if you did not properly connect RTS and CTS signals as described in [Hardware Handshaking](hardwarehandshaking.html), the GPIB-RS232/485/422 cannot send serial data to your serial device.

Do not enable hardware handshaking on the GPIB-RS232/485/422 if you suspect the conditions described above are true for your system.

Refer to [Hardware Handshaking](hardwarehandshaking.html) and the flow control topic for the mode you are using for more details about serial flow control behavior for each mode.

##### BUSY LED

On the GPIB-232/485/CT/CV-A, this LED indicates that the device is currently accepting serial data. Each serial character received toggles the **BUSY** LED status. The behavior of this LED in the GPIB-RS232/485/422 is described in [LEDs](leds.html).

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/dtevsdce.html language=enus -->
## TOPIC 00016: DTE vs. DCE

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/dtevsdce.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/dtevsdce.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

DTE vs. DCE

Data Terminal Equipment (DTE) and Data Communications Equipment
(DCE) were the terms used in the RS232 specification for the types of
equipment on either end of a serial connection. (A DCE is now called Data
Circuit-Terminating Equipment in Revision D of the RS232 specification.)
In general, DTE and DCE refer to computer equipment and modems
respectively. Because the RS232 specification mainly involved connecting
a DTE directly to a DCE and vice versa, the pinouts were defined so that
cabling was simple. That is, a cable connected a computer to a modem by
wiring pin 1 to pin 1, pin 2 to pin 2, and so on. This method is commonly
known as straight-through cabling.

The following figure shows straight-through cabling in a DTE-to-DCE interface.

[IMAGE alt='image' src='straightthroughcabling.gif']

Straight-through cabling is still the standard method to connect a modem to
your PC. However, because many applications use serial communication to
connect two or more DTEs without modems, the cabling becomes more
complicated. If two DTEs were wired together using a straight-through
cable, one transmitter would be connected to the other transmitter, and one
receiver would be connected to the other receiver. In this setup, no
transmissions could occur. Thus, these applications must use a cabling
scheme that connects the transmitter on one device to the receiver on the
other device, and vice versa. This method is known as null-modem cabling,
because it replaces the two modems that traditional RS232 applications
would require between the two DTEs. You should use a null-modem cable
to communicate from one AT serial port to another.

The following figure shows null-modem cabling in a DTE-to-DCE interface.

[IMAGE alt='image' src='nullmodemcabling.gif']

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/eossmode.html language=enus -->
## TOPIC 00017: eos

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/eossmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/eossmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

eos

Change/Disable GPIB EOS Termination Mode

#### Type

Initialization function

#### Syntax

**eos** [R[B] eoschar]<CR>

or

**eos** X[B] eoschar<CR>

or

**eos** D <CR>

#### Purpose

You can use eos at the beginning of your program if you want to use an eos mode when you transfer data to and from the GPIB. eos tells the GPIB-RS232/485/422 when to stop reading information from the GPIB. eos also enables the GPIB-RS232/485/422 to tell other devices that it is finished writing information to the GPIB. eos defines a specific character, end-of-string (EOS), to be recognized as a string terminator.

#### Remarks

The arguments R, X, B, and D specify GPIB termination methods. They enable or disable the corresponding eos mode. If a particular letter is specified, the corresponding eos mode is enabled. If it is not specified, the corresponding eos mode is disabled. By default, all eos modes are disabled. The following table lists the termination methods and corresponding letters.

| Description | Letter |
| --- | --- |
| REOS—terminate read when EOS is detected | R |
| XEOS—set EOI* with EOS on write functions | X |
| BIN—compare all 8 bits of EOS byte rather than low 7 bits (all read and write functions) | B |
| DISABLE—disable all eos modes | D |

Methods R and B determine how GPIB read operations (rd) performed by the GPIB-RS232/485/422 terminate. If method R alone is chosen, reads terminate when the low 7 bits of the byte that is read match the low 7 bits of the EOS character. If both methods R and B are chosen, a full 8-bit comparison is used.

Methods X and B together determine when GPIB write operations (wrt) performed by the GPIB-RS232/485/422 send the END message. If method X alone is chosen, the END message is sent automatically with the EOS byte when the low 7 bits of that byte match the low 7 bits of the EOS character. If methods X and B are chosen, a full 8-bit comparison is used.

eoschar is a numeric string that represents a single ASCII character. For example, decimal 10 represents the ASCII linefeed character. Refer to [Multiline Interface Messages](multilineinterfacemessages.html) for more ASCII codes.

If you call eos without an argument, the GPIB-RS232/485/422 returns the current eos settings.

If you call eos with B alone as an argument, the GPIB-RS232/485/422 records the EARG error.

|  | Note Defining an EOS byte for the GPIB-RS232/485/422 does not cause the GPIB-RS232/485/422 to insert that byte into the data string when performing GPIB writes. To send the EOS byte, you must include it in the data string that you send following the wrt programming message. |
| --- | --- |

The assignment made by this function remains in effect until you call eos again, call onl,
or turn off the GPIB-RS232/485/422.

#### See Also

[GPIB Read and Write Termination Methods (END and EOS)](gpibreadandwriteterminationmethodsendandeossmode.html).

#### Example 1

Configure the GPIB-RS232/485/422 to terminate read when <LF> is detected, compare all 8 bits, and not send EOI.

```text
char  buffer [] = "eos R,B,10\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 2

Configure the GPIB-RS232/485/422 to assert EOI* with <CR> on wrt, doing a comparison on 7 bits. There is no EOS termination on reads.

```text
char  buffer [] = "eos X,13\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 3

Get the current EOS settings.

```text
char  buffer [] = "eos\r";
char  eosSettings[10];
memset(eosSettings,0,10);
viWrite(instr, buffer, strlen(buffer), &retCount);
viRead(instr, eosSettings, 10, &retCount);
printf("EOS settings are: %s\n", eosSettings);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/gettingstartedwiththegpibrs232485422.html language=enus -->
## TOPIC 00018: Getting Started with the GPIB-RS232/485/422

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/gettingstartedwiththegpibrs232485422.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/gettingstartedwiththegpibrs232485422.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Getting Started with the GPIB-RS232/485/422

The following topics contain detailed instructions for connecting and configuring your GPIB-RS232/485/422.

[Check the Hardware Configuration](checkthehardwareconfiguration.html)

[Install the Software](installthesoftware.html)

[Connect the Hardware](connectthehardware.html)

[Configure the Hardware](configurethehardware.html)

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/glossary.html language=enus -->
## TOPIC 00019: Glossary

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/glossary.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/glossary.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Glossary

Prefixes Numbers/Symbols A C D E F G H I L M O P R S T U V

#### Prefixes

| Symbol | Prefix | Value |
| --- | --- | --- |
| p | pico | 10 -12 |
| n | nano | 10 -9 |
| µ | micro | 10 -6 |
| m | milli | 10 -3 |
| k | kilo | 10 3 |
| M | mega | 10 6 |
| G | giga | 10 9 |
| T | tera | 10 12 |

#### Numbers/Symbols

| nV | nanovolts | 10-9 volts |
| --- | --- | --- |
| µV | microvolts | 10-6 volts |
| µΩ | microohms | 10-6 ohms |
| mΩ | milliohms | 10-3 ohms |
| MΩ | megaohms | 106 ohms |
| pA | picoamps | 10-12 amperes |
| nA | nanoamps | 10-9 amperes |
| µA | microamps | 10-6 amperes |
| mA | milliamps | 10-3 amperes |

| A |  |
| --- | --- |
| A | amperes |
| AC | alternating current |
| ANSI | American National Standards Institute |
| ASCII | American Standard Code for Information Interchange |
| ATN | Attention |
| C |  |
| C | Celsius |
| CIC | Controller-In-Charge |
| CSA | Canadian Standards Association |
| CTS | Clear to Send |
| D |  |
| DCAS | Device Clear Active State |
| DCE | Data Circuit-terminating Equipment |
| DCL | Device Clear |
| DIO | digital input/output |
| DIP | dual inline package |
| DTAS | Device Trigger Active State |
| DTE | Data Terminal Equipment |
| DTR | Data Terminal Ready |
| E |  |
| EIA | Electronic Industries Association |
| EOI | end or identify |
| EOS | end of string |
| F |  |
| FCC | Federal Communications Commission |
| G |  |
| g | grams |
| GND | ground |
| GPIB | General Purpose Interface Bus |
| H |  |
| hex | hexadecimal |
| Hz | hertz |
| I |  |
| IDY | Identify |
| IEC | International Electrotechnical Commission |
| IEEE | Institute of Electrical and Electronic Engineers |
| IFC | Interface Clear |
| in. | inches |
| I/O | input/output |
| ISO | International Standards Organization |
| IST | Individual Status |
| L |  |
| LACS | Listener Active State |
| LED | light-emitting diode |
| LSI | large scale integration |
| M |  |
| MB | megabytes of memory |
| m | meters |
| O |  |
| oz | ounces |
| P |  |
| PC | personal computer |
| PPE | Parallel Poll Enable |
| R |  |
| RAM | random-access memory |
| REM | Remote |
| REN | Remote Enable |
| ROM | read-only memory |
| RQS | Request Service |
| RTS | Request to Send |
| RXD | Receive Data |
| S |  |
| s | seconds |
| SRQ | Service Request |
| SRQI | Service Request Input |
| T |  |
| TACS | Talker Active State |
| TIMO | Timeout |
| TTL | Transistor-Transistor Logic |
| TXD | Transmit Data |
| U |  |
| UL | Underwriters Laboratories |
| V |  |
| V | volts |
| VAC | volts alternating current |
| VDC | volts direct current |

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/gmodedefaultsettingsandrelatedfunctions.html language=enus -->
## TOPIC 00020: G Mode Default Settings and Related Functions

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/gmodedefaultsettingsandrelatedfunctions.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/gmodedefaultsettingsandrelatedfunctions.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

G Mode Default Settings and Related Functions

The following tables list power-on characteristics of the GPIB-RS232/485/422 and the functions you can use to change those characteristics.

##### G Mode Serial Port Characteristics

| Characteristic | Power-On Value | Related Function |
| --- | --- | --- |
| Echo bytes to serial port | no | echo |
| Enable serial port communication | yes | onl |
| Baud rate | 9600 | spset |
| Parity | none | spset |
| Data bits | 8 | spset |
| Stop bits | 1 | spset |
| Hardware handshaking | on | xon |
| Send XON/XOFF | no | xon |
| Recognize XON/XOFF | no | xon |
| Report serial errors | no | spign |

##### G Mode GPIB Characteristics

| Characteristic | Power-On Value | Related Function |
| --- | --- | --- |
| End-of-string modes | none | eos |
| Allow GPIB-RS232/485/422 to assert SRQ | no | srqen |

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/gmodefunctions.html language=enus -->
## TOPIC 00021: G Mode Functions

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/gmodefunctions.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/gmodefunctions.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

G Mode Functions

The G Mode function descriptions describe the G Mode functions you can use to program the GPIB-RS232/485/422.

For general information about using G Mode functions, refer to [Programming in G Mode](programmingingmode.html).

For more information, refer to [General Programming Steps for Communicating with the GPIB-RS232/485/422 Over GPIB.](generalprogrammingstepsforcommunicatingwiththegpibrs232485422overgpib.html)

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/gotolocalgtl.html language=enus -->
## TOPIC 00022: Go To Local (GTL)

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/gotolocalgtl.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/gotolocalgtl.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Go To Local (GTL)

This command has no effect on the GPIB-RS232/485/422.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/gpibfunctionssmode.html language=enus -->
## TOPIC 00023: GPIB Functions

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/gpibfunctionssmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/gpibfunctionssmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

GPIB Functions

The GPIB functions manage the GPIB-RS232/485/422 GPIB port. The GPIB function subgroups are listed with the most frequently used groups first. Often, the I/O and high-level bus management functions are the only ones you need.

**I/O Functions**—Read data from and write to GPIB devices.

- [rd](rd.html)
- [wrt](wrt.html)

**High-Level Bus Management Functions**—Send frequently used bus management instructions to GPIB devices.

- [clr](clr.html)
- [loc](loc.html)
- [trg](trg.html)

**GPIB Initialization Functions**—Initialize various configurations of the GPIB port.

- [caddr](caddr.html)
- [eos](eossmode.html)
- [eot](eot.html)
- [onl](onlsmode.html)
- [rsc](rsc.html)
- [tmo](tmo.html)

**Serial Poll Functions**—Conduct and respond to GPIB serial polls.

- [rsp](rsp.html)
- [rsv](rsv.html)

**Low-Level Bus Management Functions**—Give you precise control over the GPIB. Use them when the I/O and high-level bus management functions do not meet the needs of your GPIB device.

- [cac](cac.html)
- [cmd](cmd.html)
- [gts](gts.html)
- [lines](lines.html)
- [ln](ln.html)
- [pct](pct.html)
- [sic](sic.html)
- [sre](sre.html)

**Parallel Poll Functions**—Conduct and respond to GPIB parallel polls.

- [ist](ist.html)
- [ppc](ppc.html)
- [ppu](ppu.html)
- [rpp](rpp.html)

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/gpibinitializationcodeusingvisa.html language=enus -->
## TOPIC 00024: GPIB Initialization Code Using VISA

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/gpibinitializationcodeusingvisa.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/gpibinitializationcodeusingvisa.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

GPIB Initialization Code Using VISA

```text
#include "visa.h"

int main(void)
{
ViStatus   status;
ViSession  defaultRM;
ViSession  GPIB232;
ViUInt32   retCount;

/* Open Default RM */
status = viOpenDefaultRM(&defaultRM);
if (status < VI_SUCCESS) {

/* Error Initializing VISA...exiting */
return -1;
}

/* Open up handle to GPIB-RS232/485/422 at GPIB Primary Address 1 */
status = viOpen(defaultRM, "GPIB::1::INSTR", VI_NULL, VI_NULL, &GPIB232);

/* TODO: Add application specific code here */

/* Use device and eventually close it. */
viClose(GPIB232);
viClose(defaultRM);
return 0;
}
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/gpibreadandwriteterminationmethodsendandeosgmode.html language=enus -->
## TOPIC 00025: GPIB Read and Write Termination Methods (END and EOS)

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/gpibreadandwriteterminationmethodsendandeosgmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/gpibreadandwriteterminationmethodsendandeosgmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

GPIB Read and Write Termination Methods (END and EOS)

The IEEE 488 specification defines two ways that GPIB Talkers and Listeners can identify the last byte of data messages: END and EOS. The two methods permit a Talker to send data messages of any length without the Listener(s) knowing the number of transmission bytes in advance. You can use END and EOS individually or in combination, but you must configure the Listener to detect the end of a transmission.

| END message | The Talker asserts the EOI* (End or Identify) signal while the last data byte is being transmitted. The Listener stops reading when it detects a data byte accompanied by EOI*, regardless of the byte value. |
| --- | --- |
| EOS character | The Talker transmits an EOS (end-of-string) character at the end of its data string. The Listener stops receiving data when it detects the EOS character. Either a 7-bit ASCII character or a full 8-bit binary byte can be used. |

When the GPIB-RS232/485/422 receives its own talk or listen address, no EOS Modes are in effect. When talking, the GPIB-RS232/485/422 asserts EOI* with the last byte of its response. When the GPIB-RS232/485/422 receives the serial device talk address, the EOS Modes in effect are those you select using the eos function.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/gpibreadandwriteterminationmethodsendandeossmode.html language=enus -->
## TOPIC 00026: GPIB Read and Write Termination Methods (END and EOS)

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/gpibreadandwriteterminationmethodsendandeossmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/gpibreadandwriteterminationmethodsendandeossmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

GPIB Read and Write Termination Methods (END and EOS)

The IEEE 488 specification defines two ways that GPIB Talkers and Listeners can identify the last byte of data messages: END and EOS. The two methods permit a Talker to send data messages of any length without the Listener(s) knowing the number of transmission bytes in advance. You can use END and EOS individually or in combination, but you must configure the Listener to detect the end of a transmission.

| END message | The Talker asserts the EOI* (End Or Identify) signal while the last data byte is being transmitted. The Listener stops reading when it detects a data decimal octal hexadecimal byte accompanied by EOI*, regardless of the byte value. |
| --- | --- |
| EOS character | The Talker sends an EOS (end-of-string) character at the end of its data string. The Listener stops receiving data when it detects the EOS character. You can use either a 7-bit ASCII character or a full 8-bit binary byte. |

The GPIB-RS232/485/422 always terminates GPIB rd operations on the END message. You can use the eos and eot functions to change GPIB read and write termination methods.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/gpibrs232485422serialpollresponses.html language=enus -->
## TOPIC 00027: GPIB-RS232/485/422 Serial Poll Responses

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/gpibrs232485422serialpollresponses.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/gpibrs232485422serialpollresponses.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

GPIB-RS232/485/422 Serial Poll Responses

If the GPIB-RS232/485/422 is serial polled, its response byte depends on the internal data buffers' status, as follows:

- If the serial input buffer is empty, bit 1 of the status byte is set to 1.
- If the serial input buffer is not empty, bit 1 is set to 0.
- If the GPIB input buffer is empty, bit 0 of the status byte is set to 1.
- If the GPIB input buffer is not empty, bit 0 is set to 0.

In all cases, bit 6 is set to 1 if the GPIB-RS232/485/422 is requesting service; otherwise, it is set to 0.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/howmessagesareprocessedgmode.html language=enus -->
## TOPIC 00028: How Messages Are Processed

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/howmessagesareprocessedgmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/howmessagesareprocessedgmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

How Messages Are Processed

The GPIB-RS232/485/422 processes each programming message on a line-by-line basis. When the GPIB-RS232/485/422 receives a message, it buffers the message, interprets the function name and arguments, and then executes the message.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/howmessagesareprocessedsmode.html language=enus -->
## TOPIC 00029: How Messages Are Processed

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/howmessagesareprocessedsmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/howmessagesareprocessedsmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

How Messages Are Processed

The GPIB-RS232/485/422 processes a programming message on a line-by-line basis. When the GPIB-RS232/485/422 receives a message, it buffers the entire message, interprets the function name and arguments, and then executes the message. The data portions of the wrt and cmd functions are processed differently. The data immediately following a wrt and a cmd function are sent directly to the GPIB.

S Mode recognizes <CTRL-H> (hex 8) in a programming message as a backspace and erases the previous character. S Mode recognizes <CTRL-H> in a data string as a data byte and does not erase the previous character.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/interfacingtoanrs485device.html language=enus -->
## TOPIC 00030: Interfacing to an RS485 Device

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/interfacingtoanrs485device.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/interfacingtoanrs485device.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Interfacing to an RS485 Device

This topic describes the RS485 serial port on the GPIB-RS485/RS422 and
explains how to interface an RS485 device to the RS485 serial port.

The GPIB-RS485/RS422 transfers serial data using the electrical signals defined
in the EIA-485 standard. The RS485 port on the GPIB-RS485/RS422 provides
an asynchronous serial communication link to a serial peripheral device.
For more information on the EIA-485 standard, contact the following
organization:

Global Engineering Documents 

15 Inverness Way East 
 
Englewood, CO 80112 
 
(800) 854-7179 

global.ihs.com

[RS422](rs422.html)

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/issuinglocalconfigurationsinsmode.html language=enus -->
## TOPIC 00031: Issuing Local Configurations in S Mode

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/issuinglocalconfigurationsinsmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/issuinglocalconfigurationsinsmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Issuing Local Configurations in S Mode

In S Mode, the ppc and ppu functions also configure the GPIB-RS232/485/422 locally. Local configuration is indicated by sending one addr argument with the value 255. For example, to configure the GPIB-RS232/485/422 to respond on DIO line 5 when its ist bit is 0, send the following programming message to the GPIB-RS232/485/422:

ppc 255,5,0<CR>

When configuring the GPIB-RS232/485/422 itself, the ppc or ppu function does not send messages out on the GPIB. Instead, the GPIB-RS232/485/422 internally enables or disables parallel poll responses as indicated. For the ppc or ppu function to have an effect, the GPIB-RS232/485/422 must be using PP subset PP2. If the GPIB-RS232/485/422 is not configured to use PP subset PP2, it cannot allow itself to be locally configured, and returns an ECAP error. You can configure the GPIB-RS232/485/422 to use PP subset PP2 with the conf function.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/issuingremoteconfigurationsinsmode.html language=enus -->
## TOPIC 00032: Issuing Remote Configurations in S Mode

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/issuingremoteconfigurationsinsmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/issuingremoteconfigurationsinsmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Issuing Remote Configurations in S Mode

In S Mode, the ppc and ppu functions configure devices remotely for parallel polls. Remote configuration is indicated by passing the addresses of the GPIB devices to be configured in the addr arguments. For example, to configure a device at address 5 to respond on DIO line 3 when its ist bit is 1, send the following programming message to the GPIB-RS232/485/422:

ppc 5,3,1<CR>

The following figure shows the PPE message formed by the ppc programming
message given above.

| 0 | 1 | 1 | U | S | DIO lines 1 though 8 |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | 0 | 1 | 0 |  |

##### Sample PPE Message Bits

The value of this byte is hex 6A, where:

- U = 0 Enable parallel poll responses
- S = 1 When ist = 1, the device asserts DIO line 3 (which corresponds to 010 in bits 0 through 2) in response to a parallel poll.

The ppc function enables GPIB devices to respond to parallel polls, and the ppu function disables parallel poll responses. For every addr, ppr, s configuration, the ppc function sends the talk address of the GPIB-RS232/485/422, unlisten, the listen address specified by addr, Parallel Poll Configure, then the Parallel Poll Enable message (PPE). The PPE message is formed by using ppr as the DIO line and s as the S bit. For every addr argument given, the ppu function sends the talk address of the GPIB-RS232/485/422, unlisten, the listen address specified by addr, Parallel Poll Configure, then the Parallel Poll Disable (PPD) message. The PPD message disables only one GPIB device at a time from responding to parallel polls.

If the ppu function is called without an argument, it disables all GPIB devices from responding to parallel polls. It does this by sending out the Parallel Poll Unconfigure (PPU) message. This message has the same effect as using the ppu function to send PPD messages to every device on the GPIB.

For the ppc or ppu function to have an effect, the device it is configuring must be using PP subset PP1. If the device is not using PP subset PP1, it does not allow an external Controller to configure it, and will probably ignore the configuration.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/ist.html language=enus -->
## TOPIC 00033: ist

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/ist.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/ist.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

ist

Set or Clear Individual Status Bit

#### Type

Parallel poll function

#### Syntax

**is**t [bool]<CR>

#### Purpose

You can use ist when the GPIB-RS232/485/422 participates in a parallel poll conducted by another device that is Active Controller.

#### Remarks

If the argument bool is 1, the GPIB-RS232/485/422's individual status bit is set to 1. If the argument bool is 0, the GPIB-RS232/485/422's individual status bit is cleared. The power-on default is 0.

If you call ist without an argument, the GPIB-RS232/485/422 returns the value of its individual status bit.

The assignment made by ist remains in effect until you call ist again, call onl, or turn off the GPIB-RS232/485/422.

#### See Also

[ppc](ppc.html) and [Parallel Polling](parallelpolling.html).

#### Example 1

Set the ist bit to 1.

```text
char  buffer [] = "ist 1\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 2

Clear the ist bit to 0.

```text
char  buffer [] = "ist 0\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 3

Determine the ist bit state.

```text
// Get GPIB-RS232 system identification
char  buffer [] = "ist\r";
char  istState[5];
memset(istState,0,5);
viWrite(instr, buffer, strlen(buffer), &retCount);
viRead(instr, istState, 5, &retCount);
printf("ist is %s\n", istState);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/launchingthenigpibserialconverterwizard.html language=enus -->
## TOPIC 00034: Launching the NI GPIB-Serial Converter Wizard

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/launchingthenigpibserialconverterwizard.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/launchingthenigpibserialconverterwizard.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Launching the NI GPIB-Serial Converter Wizard

To run the NI GPIB-Serial Converter Wizard, go to **Start»Programs»National Instruments»GPIB-Serial Converter**.

The NI GPIB-Serial Converter Wizard welcome screen should appear, as shown in the following figure.

[IMAGE alt='image' src='converterwizardwelcome.gif']

Click **Next** to continue and proceed to [Connecting the GPIB-RS232/485/422](connectingthegpibrs232485422.html).

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/leds.html language=enus -->
## TOPIC 00035: LEDs

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/leds.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/leds.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

LEDs

The eight light-emitting diodes (LEDs) are on the front of the GPIB-RS232/485/422, as shown in the following figure.

|  | Note The figure shows only the GPIB-RS232, but the GPIB-RS485/RS422 is similar. |
| --- | --- |

[IMAGE alt='image' src='frontpanel.gif']

The LEDs show the GPIB-RS232/485/422 current status at all times. The following table describes each LED.

| LED | Indication |
| --- | --- |
| PWR | Indicates that power to the unit has been applied and the ON/OFF switch is in the ON position. |
| RDY | Indicates that the power-on self-test has passed successfully, and the unit is ready to operate. |
| TALK | Indicates that the GPIB-RS232/485/422 is addressed as a GPIB Talker. |
| LSTN | Indicates that the GPIB-RS232/485/422 is addressed as a GPIB Listener. |
| SRQ | Indicates that the GPIB signal line SRQ* is asserted. |
| ATN | Indicates that the GPIB signal line ATN* is asserted. |
| FULL | Indicates that one of the GPIB-RS232/485/422 data buffers is full. This is not an error condition, but is merely a signal that bus performance may be reduced to the speed of the slower port. |
| BUSY | Does not apply in S Mode. In G and D Modes, indicates there is currently GPIB data buffered in the GPIB-RS232/485/422 to be transferred over serial. In C Mode, indicates there is currently serial data buffered in the GPIB-RS232/485/422 to be transferred over GPIB.** |
| * Indicates that the signal is active low (negative logic or low when asserted). |  |
| ** The behavior of this LED is slightly different between the GPIB-RS232/485/422 and GPIB-232/485/CT/CV-A. For more information, refer to Differences Between the GPIB-232/485CT/CV-A and GPIB-RS232/485/422. |  |

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/lines.html language=enus -->
## TOPIC 00036: lines

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/lines.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/lines.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

lines

Return State of GPIB Control Lines

#### Type

Low-level bus management function

#### Syntax

**li**nes<CR>

#### Purpose

You can use lines to determine the state of the GPIB control lines.

#### Remarks

This command returns two numeric strings of information. The numeric strings are separated by a comma and terminated with <CR><LF>. The state of the eight GPIB control lines is returned in the first number. Each bit in this number corresponds to a GPIB control line as follows:

| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EOI* | ATN* | SRQ* | REN* | IFC* | NRFD* | NDAC* | DAV* |

The second number contains mask bits in the same order as above, indicating which lines are actually being reported, and which are indeterminable. If a particular mask bit is 1, the corresponding bit in the first number indicates the line state. If the mask bit is 0, the corresponding bit in the first number should be disregarded.

#### See Also

[GPIB Basics](gpibbasics.html).

#### Example

Determine the state of the GPIB control lines.

```text
char  buffer [] = "lines\r";
char  linesState[10];
memset(linesState,0,10);
int gpibLines = 0;
viWrite(instr, buffer, strlen(buffer), &retCount);
viRead(instr, linesState, 10, &retCount);
gpibLines = atoi(linesState);
if(gpibLines & (1 << 7))
{
   printf("EOI asserted\n");
}
if(gpibLines & (1 << 6))
{
   printf("ATN asserted\n");
}
if(gpibLines & (1 << 5))
{
   printf("SRQ asserted\n");
}
if(gpibLines & (1 << 4))
{
   printf("REN asserted\n");
}
if(gpibLines & (1 << 3))
{
   printf("IFC asserted\n");
}
if(gpibLines & (1 << 2))
{
   printf("NRFD asserted\n");
}
if(gpibLines & (1 << 1))
{
   printf("NDAC asserted\n");
}
if(gpibLines & 1)
{
   printf("DAV asserted\n");
}
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/listofgmodefunctionsbygroup.html language=enus -->
## TOPIC 00037: List of G Mode Functions by Group

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/listofgmodefunctionsbygroup.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/listofgmodefunctionsbygroup.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

List of G Mode Functions by Group

The GPIB-RS232/485/422 functions are divided into three groups: GPIB functions, serial port functions, and general-use functions. For more information about the G Mode functions, refer to [Alphabetical List of G Mode Functions](alphabeticallistofgmodefunctions.html) or [G Mode Functions](gmodefunctions.html). The following topics list programming messages sent to the GPIB-RS232/485/422 from a GPIB Talker.

[GPIB Functions](gpibfunctionsgmode.html)

[Serial Port Functions](serialportfunctionsgmode.html)

[General-Use Functions](generalusefunctionsgmode.html)

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/listofsmodefunctionsbygroup.html language=enus -->
## TOPIC 00038: List of S Mode Functions by Group

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/listofsmodefunctionsbygroup.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/listofsmodefunctionsbygroup.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

List of S Mode Functions by Group

The GPIB-RS232/485/422 S Mode functions are divided into three main groups: GPIB functions, serial port functions, and general-use functions. For more information about the S Mode functions, refer to [Alphabetical List of S Mode Functions](alphabeticallistofsmodefunctions.html) or [S Mode Functions](smodefunctions.html).

[GPIB Functions](gpibfunctionssmode.html)

[Serial Port Functions](serialportfunctionssmode.html)

[General-Use Functions](generalusefunctionssmode.html)

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/listsofgpibaddresses.html language=enus -->
## TOPIC 00039: Lists of GPIB Addresses

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/listsofgpibaddresses.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/listsofgpibaddresses.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Lists of GPIB Addresses

When a function requires a list of one or more GPIB addresses, the maximum number of addresses you can specify is 14. If you specify more than 14 addresses, the GPIB-RS232/485/422 records the EARG error. This limit exists because the IEEE 488 specification allows no more than 15 GPIB devices to coexist on any GPIB.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/ln.html language=enus -->
## TOPIC 00040: ln

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/ln.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/ln.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

ln

Check for Listening Devices

#### Type

Low-level bus management function

#### Syntax

**ln** alist<CR>

#### Purpose

You can use ln to determine whether or not there are listening devices at the specified GPIB addresses.

#### Remarks

The argument alist is a list of addresses separated by commas or spaces. There should be at least one address in the list. addresses specify the GPIB addresses of the devices you want to check.

When specifying the address parameters, a value of 255 (hex FF) can be used as a secondary address. When this special value is used, the GPIB-RS232/485/422 checks all secondary addresses for the specified primary address.

If this is the first function you call that requires GPIB Controller capability, and you have not disabled System Controller capability with rsc, the GPIB-RS232/485/422 sends Interface Clear (IFC*) to make itself CIC. It also asserts Remote Enable.

If you passed control to some other GPIB device, control must be passed back to you or you must send IFC* to make yourself CIC before making this call. Otherwise, the ECIC error is posted.

ln returns the list of addresses found to be listening on the GPIB bus. The addresses of this list are separated by commas and terminated with <CR><LF>. If none of the specified addresses were found to be listening, a <CR><LF> alone is returned.

#### Example

Look for devices at primary address 2, primary address 5 with all secondary addresses, primary address 3 secondary address 20, and primary address 7.

```text
char  buffer [] = "ln 2,5+255,3+20,7\r";
char  listenAddresses[20];
memset(listenAddresses,0,20);
viWrite(instr, buffer, strlen(buffer), &retCount);
viRead(instr, listenAddresses, 20, &retCount);
printf("Devices found at addresses: %s\n", listenAddresses);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/loc.html language=enus -->
## TOPIC 00041: loc

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/loc.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/loc.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

loc

Go to Local*

#### Type

High-level bus management function

#### Syntax

**l**oc [alist]<CR>

#### Purpose

You can use loc to put a GPIB device in local program mode. In this mode, you can program the device from its front panel. Because a device must usually be placed in remote program mode before it can be programmed from the GPIB, the GPIB-RS232/485/422 automatically puts the device in remote program mode. You then use loc to return devices to local program mode.

#### Remarks

The argument alist is a list of addresses separated by commas or spaces. Addresses specify the GPIB addresses of the devices you want to return to local mode.

If you call loc with alist, the GPIB-RS232/485/422 places the specified device(s) in local mode using the Go To Local (GTL) command.

If you call loc without alist, and the GPIB-RS232/485/422 is System Controller, the GPIB-RS232/485/422 returns all devices to local mode by unasserting REN* and asserting it again. If you call loc without alist and the GPIB-RS232/485/422 is not System Controller, the GPIB-RS232/485/422 records the ESAC error.

If this is the first function you call that requires GPIB Controller capability, and you have not disabled System Controller capability with rsc, the GPIB-RS232/485/422 sends Interface Clear (IFC*) to make itself CIC. It also asserts Remote Enable.

If you passed control to some other GPIB device, control must be passed back to you or you must send IFC* to make yourself CIC before making this call. Otherwise, the ECIC error is posted.

If only the special value of 255 (hex FF) is entered as a parameter, the GPIB-RS232/485/422 configures itself for local program mode by pulsing its internal rtl (return to local) message. The GPIB-RS232/485/422 does not require GPIB Controller capability to configure itself for local program mode.

#### See Also

[Status and Error Message Information](statusanderrormessageinformation.html).

#### Example 1

Put three devices in local mode.

```text
char  buffer [] = "loc 6+22,4+23,7\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 2

Put all devices in local mode.

```text
char  buffer [] = "loc\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 3

Put the GPIB-RS232/485/422 in local mode.

```text
char  buffer [] = "loc 255\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/locatingthegpibrs232485422.html language=enus -->
## TOPIC 00042: Locating the GPIB-RS232/485/422

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/locatingthegpibrs232485422.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/locatingthegpibrs232485422.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Locating the GPIB-RS232/485/422

The NI GPIB-Serial Converter Wizard attempts to locate the GPIB-RS232/485/422 attached to the interface chosen in the previous step. If successful, the **Select Action** screen appears, and your GPIB-RS232/485/422 serial number is displayed, as shown in the following figure.

[IMAGE alt='image' src='converterwizardselectaction.gif']

If the NI GPIB-Serial Converter Wizard displays the **Select Action** screen, proceed to [Selecting an Action](selectinganaction.html).

If there was an error locating the GPIB-RS232/485/422, the **Error Locating the GPIB-RS232/485/422** screen is displayed, as shown in the following figure.

[IMAGE alt='image' src='converterwizarderrorlocating.gif']

If the NI GPIB-Serial Converter Wizard appears as shown above, proceed to [Error Locating the GPIB-RS232/485/422](errorlocatingthegpibrs232485422.html).

If there is an incompatibility with the NI GPIB-Serial Converter Wizard and the firmware running on the GPIB-RS232/485/422, the **Incompatible Firmware Version** screen is displayed, as shown in the following figure.

[IMAGE alt='image' src='converterwizardincompatiblefirmware.gif']

If the NI GPIB-Serial Converter Wizard appears as shown above, proceed to [Incompatible Firmware Version](incompatiblefirmwareversion.html).

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/navigating.html language=enus -->
## TOPIC 00043: Navigating Help (Windows Only)

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/navigating.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/navigating.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Navigating Help (Windows Only)

To navigate this help file, use the **Contents**, **Index**, and **Search** tabs to the left of this window or use the following toolbar buttons located above the tabs:

- Hide —Hides the navigation pane from view.
- Locate —Locates the currently displayed topic in the Contents tab, allowing you to view related topics.
- Back —Displays the previously viewed topic.
- Forward —Displays the topic you viewed before clicking the Back button.
- Options —Displays a list of commands and viewing options for the help file.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/nointerfacesconnected.html language=enus -->
## TOPIC 00044: No Interfaces Connected

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/nointerfacesconnected.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/nointerfacesconnected.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

No Interfaces Connected

The NI GPIB-Serial Converter Wizard requires at least one serial port or one GPIB interface installed in the computer to configure your hardware.

If a serial port or GPIB interface is installed in your computer, ensure that the driver for your hardware is correctly installed and functioning properly. Verify that any other applications that may be using your interface have exited.

After exiting all applications, click **Back** to redetect your computer interfaces.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/noswapmode.html language=enus -->
## TOPIC 00045: No-Swap Mode

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/noswapmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/noswapmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

No-Swap Mode

In no-swap mode, the GPIB-RS232/485/422 addresses the device as a listener. The GPIB-RS232/485/422 never readdresses a GPIB device after it has initially been addressed as a Listener. This mode is useful if your device is intended only to receive data. In the example in [<CR> or <LF> Termination Mode](crorlfterminationmode.html), you could use the no-swap mode to talk to the plotter if you never needed to obtain status information from it. Because you cannot readdress in no-swap mode, the <CR> is not needed to obtain status as it was in the example in [<CR> or <LF> Termination Mode](crorlfterminationmode.html).

For details about the setup of this example, refer to [General Programming Steps for Communicating with the GPIB-RS232/485/422 Over Serial](generalprogrammingstepsforcommunicatingwiththegpibrs232485422overserial.html).

```text
//Actually performing the reads / writes here.
strcpy (stringinput,"FACTORY\n");
status = viWrite (instr, (ViBuf)stringinput, strlen(stringinput), &writeCount);
if (status < VI_SUCCESS)    
{
printf ("Error writing to the device.\n");
}
strcpy (stringinput,"LANGUAGE ENGLISH\n");
status = viWrite (instr, (ViBuf)stringinput, strlen(stringinput), &writeCount);
if (status < VI_SUCCESS)    
{
printf ("Error writing to the device.\n");
}
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/numericstringarguments.html language=enus -->
## TOPIC 00046: Numeric String Arguments

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/numericstringarguments.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/numericstringarguments.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Numeric String Arguments

Another type of argument is a numeric string. A numeric string represents an integer you can express using decimal, octal, or hexadecimal digits. To specify an octal integer, precede the numeric string with a backslash (\). To specify a hexadecimal integer, precede the numeric string with a backslash X (\X).

Each of the following numeric strings represents the decimal value 112:

- Decimal 112
- Octal \160
- Hex \x70

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/onlgmode.html language=enus -->
## TOPIC 00047: onl

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/onlgmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/onlgmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

onl

Place the GPIB-RS232/485/422 Online/Offline

#### Type

General-use function

#### Syntax

**o**nl [bool]<CR>

#### Purpose

You can use onl to disable communication between the GPIB-RS232/485/422 and serial port or reset the GPIB-RS232/485/422 characteristics to their default values.

#### Remarks

If the argument bool is 1, the GPIB-RS232/485/422 places itself online. If the argument bool is 0, it places itself offline. By default, the GPIB-RS232/485/422 powers up online.

If you call onl without an argument, the GPIB-RS232/485/422 returns its current state, which is 0 if the GPIB-RS232/485/422 is offline and 1 if the it is online.

Placing the GPIB-RS232/485/422 offline is like disconnecting its serial cable from the serial device. When placed offline, no data is sent out the GPIB-RS232/485/422 serial port, and data coming in to the GPIB-RS232/485/422 serial port is not saved until onl is called with bool = 1.

Placing the GPIB-RS232/485/422 online enables data to be sent and received over its serial port. Placing the GPIB-RS232/485/422 online also restores all its settings to their power-on default values and discards any serial and GPIB data buffered inside the GPIB-RS232/485/422.

#### See Also

[G Mode Default Settings and Related Functions](gmodedefaultsettingsandrelatedfunctions.html).

#### Example 1

```text
// Put the GPIB-RS232/485/422 online and restore its power-on settings.
char onlCommand [ ] = "onl 1\r";
viWrite (GPIB232, onlCommand, strlen(onlCommand), &retCount);
```

#### Example 2

```text
// Put the GPIB-RS232/485/422 offline. 
char onlCommand [ ] = "onl 0\r";
viWrite (GPIB232, onlCommand, strlen(onlCommand), &retCount);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/onlsmode.html language=enus -->
## TOPIC 00048: onl

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/onlsmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/onlsmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

onl

Place the GPIB-RS232/485/422 Online/Offline

#### Type

Initialization function

#### Syntax

**o**nl [bool]<CR>

#### Purpose

You can use onl to disable communications between the GPIB-RS232/485/422 and the GPIB, or to reinitialize the GPIB-RS232/485/422 characteristics to their default values.

#### Remarks

If the argument bool is 1, the GPIB-RS232/485/422 places itself online. If the argument bool is 0, the GPIB-RS232/485/422 takes itself offline. By default, the GPIB-RS232/485/422 powers up online, is in the Idle Controller state, and configures itself to be the System Controller.

Placing the GPIB-RS232/485/422 offline can be thought of as disconnecting its GPIB cable from the other GPIB devices.

Placing the GPIB-RS232/485/422 online allows the GPIB-RS232/485/422 to communicate over the GPIB and restores all settings except the ones changed with the xon command to their power-on values.

|  | Note Restoring all settings to their power-on values except the ones changed with the xon command is a difference from the GPIB-232/485/CT/CV-A. For more information about this and other differences, refer to Differences Between the GPIB-232/485CT/CV-A and GPIB-RS232/485/422. |
| --- | --- |

If you call onl without an argument, the GPIB-RS232/485/422 returns the current state, which is 0 if the GPIB-RS232/485/422 is offline and 1 if the GPIB-RS232/485/422 is online.

#### See Also

[S Mode Default Settings and Related Functions](smodedefaultsettingsandrelatedfunctions.html).

#### Example 1

Put the GPIB-RS232/485/422 online and restore its power on settings.

```text
char  buffer [] = "onl 1\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 2

Put the GPIB-RS232/485/422 offline to prevent it from communicating on GPIB.

```text
char  buffer [] = "onl 0\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/operatingincmode.html language=enus -->
## TOPIC 00049: Operating in C Mode

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/operatingincmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/operatingincmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Operating in C Mode

Set the GPIB-RS232/485/422 to operate in C Mode when transferring data between a single GPIB device with no Controller capabilities and a serial device. The following figure shows an example of a system requiring C Mode. The system includes a GPIB device, such as a digital multimeter, connected to a computer's serial port through a GPIB-RS232/485/422.

[IMAGE alt='image' src='cmodeoperation.gif']

Refer to [Using the NI GPIB-Serial Converter Wizard to Configure the GPIB-RS232/485/422](usingthenigpibserialconverterwizardtoconfigurethegpibrs232485422.html) for detailed information about setting up your GPIB-RS232/485/422 to operate in C mode. Refer to [C Mode Overview](cmode.html) for information about using C Mode.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/operatingindmode.html language=enus -->
## TOPIC 00050: Operating in D Mode

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/operatingindmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/operatingindmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Operating in D Mode

Set the GPIB-RS232/485/422 to operate in D Mode to connect a serial device to a GPIB system with a GPIB Controller responsible for addressing the GPIB-RS232/485/422 to talk or listen. The following figure shows an example of a system requiring D Mode. The system includes a serial device, such as a printer, connected to a GPIB system with an existing GPIB Controller, such as a computer with a National Instruments PCI-GPIB IEEE 488.2 board installed.

[IMAGE alt='image' src='dmodeoperation.gif']

Refer to [Using the NI GPIB-Serial Converter Wizard to Configure the GPIB-RS232/485/422](usingthenigpibserialconverterwizardtoconfigurethegpibrs232485422.html) for detailed information about setting up your GPIB-RS232/485/422 to operate in D mode. Refer to [D Mode Overview](dmode.html) for information about using D Mode.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/ppc.html language=enus -->
## TOPIC 00051: ppc

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/ppc.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/ppc.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

ppc

Parallel Poll Configure

#### Type

Parallel poll function

#### Syntax

**ppc** addr,ppr,s [addr,ppr,s]...<CR>

#### Purpose

You can use ppc to configure specified GPIB devices to respond to parallel polls in a certain manner.

#### Remarks

The argument addr specifies the GPIB address of the device to be enabled for parallel polls. addr consists of a primary address and an optional secondary address.

The argument ppr is an integer string between 1 and 8 that specifies the data line on which to respond.

The argument s is either 0 or 1 and is interpreted along with the value of the device's individual status bit to determine whether to drive the line true or false.

Each group of addr,ppr,s can be separated by either a comma or space, just as any list of arguments.

If this is the first function you call that requires GPIB Controller capability, and you have not disabled System Controller capability with rsc, the GPIB-RS232/485/422 sends Interface Clear (IFC*) to make itself CIC. It also asserts Remote Enable.

If you passed control to some other GPIB device, control must be passed back to you or you must send IFC* to make yourself CIC before making this call. Otherwise, the ECIC error is posted.

The GPIB-RS232/485/422 takes the arguments ppr and s and constructs the appropriate parallel poll enable (PPE) message for each addr specified.

If you call ppc without an argument, the GPIB-RS232/485/422 records the EARG error.

If only one addr,ppr,s is specified, and addr has the special value of 255 (hex FF), the GPIB-RS232/485/422 configures itself for parallel polls. To do this, the GPIB-RS232/485/422 must be using IEEE 488 Parallel Poll (PP) interface function subset PP2. You can do this by setting the PP2 option using the conf function. If the PP2 option is not set, the GPIB-RS232/485/422 records the ECAP error. The GPIB-RS232/485/422 does not require GPIB Controller capability to configure itself for parallel polls.

#### See Also

[conf](conf.html), [ist](ist.html), [ppu](ppu.html), [rpp](rpp.html), and [Parallel Polling](parallelpolling.html).

#### Example 1

Configure two devices for parallel poll.

```text
char  buffer [] = "ppc 18+23,8,0 23+10,7,1\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 2

Configure the GPIB-RS232/485/422 to respond to parallel polls on data line 7 if its individual status bit is 1.

```text
char  buffer [] = "ppc 255,7,1\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/ppu.html language=enus -->
## TOPIC 00052: ppu

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/ppu.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/ppu.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

ppu

Parallel Poll Unconfigure

#### Type

Parallel poll function

#### Syntax

**ppu** [alist]<CR>

#### Purpose

You can use ppu if you are performing parallel polls and you want to prevent certain GPIB devices from responding.

#### Remarks

The argument alist is a list of addresses separated by commas or spaces. Addresses specify the GPIB addresses of the devices to be disabled from parallel polls.

If you call ppu with alist, the GPIB-RS232/485/422 unconfigures from parallel polls only those devices specified in alist. If you call ppu without alist, the GPIB-RS232/485/422 unconfigures all devices from parallel polls.

If this is the first function you call that requires GPIB Controller capability, and you have not disabled System Controller capability with rsc, the GPIB-RS232/485/422 sends Interface Clear (IFC*) to make itself CIC. It also asserts Remote Enable.

If you passed control to some other GPIB device, control must be passed back to you or you must send IFC* to make yourself CIC before making this call. Otherwise, the ECIC error is posted.

If only addr is specified and it has the special value of 255 (hex FF), the GPIB-RS232/485/422 disables itself from responding to parallel polls. To do this, the GPIB-RS232/485/422 must be using IEEE 488 Parallel Poll (PP) interface function subset PP2. You can do this by setting the PP2 option using the conf function. If the PP2 option is not set, the GPIB-RS232/485/422 records the ECAP error. The GPIB-RS232/485/422 does not require GPIB Controller capability to disable itself from responding to parallel polls.

#### See Also

[conf](conf.html), [ist](ist.html), [ppc](ppc.html), [rpp](rpp.html), and [Parallel Polling](parallelpolling.html).

#### Example 1

Send the PPD command to the device at primary address 14.

```text
char  buffer [] = "ppu 14\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 2

Send the PPD command to all devices.

```text
char  buffer [] = "ppu\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 3

Disable the GPIB-RS232/485/422 from responding to parallel polls.

```text
char  buffer [] = "ppu 255\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/printing_this_help_file.html language=enus -->
## TOPIC 00053: Printing Help File Topics (Windows Only)

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/printing_this_help_file.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/printing_this_help_file.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Printing Help File Topics (Windows Only)

Complete the following steps to print an entire book from the **Contents** tab:

1. Right-click the book.
2. Select Print from the shortcut menu to display the Print Topics dialog box.
3. Select the Print the selected heading and all subtopics option.
 [IMAGE alt='image' src='note.gif']
**Note** Select **Print the selected topic** if you want to print the single topic you have selected in the **Contents** tab.
4. Click the OK button.

#### Printing PDF Documents

This help file may contain links to PDF documents. To print PDF documents, click the print button located on the Adobe Acrobat Viewer toolbar.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/programmingbackgroundandconsiderationsforthegpibrs232485422.html language=enus -->
## TOPIC 00054: Programming Background and Considerations for the GPIB-RS232/485/422

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/programmingbackgroundandconsiderationsforthegpibrs232485422.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/programmingbackgroundandconsiderationsforthegpibrs232485422.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Programming Background and Considerations for the GPIB-RS232/485/422

The following topics discuss programming steps and contain program examples you can use as guidelines as you start writing programs for the GPIB-RS232/485/422.

[Programming Steps and Examples](programmingstepsandexamples.html)

[General Programming Steps for Communicating with the GPIB-RS232/485/422 Over Serial](generalprogrammingstepsforcommunicatingwiththegpibrs232485422overserial.html)

[Serial Initialization Code Using VISA](serialinitializationcodeusingvisa.html)

[General Programming Steps for Communicating with the GPIB-RS232/485/422 Over GPIB](generalprogrammingstepsforcommunicatingwiththegpibrs232485422overgpib.html)

[GPIB Initialization Code Using VISA](gpibinitializationcodeusingvisa.html)

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/programmingconsiderationssmode.html language=enus -->
## TOPIC 00055: Programming Considerations

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/programmingconsiderationssmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/programmingconsiderationssmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Programming Considerations

The programming examples for each function description are in standard ANSI C, using NI-VISA. Although the examples in this help are written in C, you can program the GPIB-RS232/485/422 using any programming language with access to a serial port.

In the function syntax descriptions, arguments enclosed in square brackets ([]) are optional. Do not enter the brackets as part of your argument.

For all programming examples, the communications port has been opened using initialization code found in [General Programming Steps for Communicating with the GPIB-RS232/485/422 Over Serial](generalprogrammingstepsforcommunicatingwiththegpibrs232485422overserial.html).

The I/O and high-level bus management functions are the most frequently used and should meet most of your needs. In the function descriptions, these functions are marked with an asterisk (*).

You can use function name abbreviations, which include only as many characters as necessary to distinguish them from other functions. The abbreviated forms are indicated by bold text in the syntax description of each function.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/programmingmessageexamplewithdatastring.html language=enus -->
## TOPIC 00056: Programming Message Example with Data String

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/programmingmessageexamplewithdatastring.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/programmingmessageexamplewithdatastring.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Programming Message Example with Data String

The following lines of code are an example of a programming message with a data string:

viWrite(instr, "wrt 2\n",6, &retCount); 

viWrite(instr, "*idn?\r",6, &retCount);

This programming message contains the function name wrt, the argument 2, and the data string "*idn?". It tells S Mode to write to the device at primary address 2. "*idn?" is the data string that contains the data wrt sends out on the GPIB. In this case, a carriage return "\r" is added to the data string to terminate the wrt command.

Both the cmd and wrt programming messages are followed by a data string that can contain 7 or 8-bit data.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/programmingmessagesgmode.html language=enus -->
## TOPIC 00057: Programming Messages

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/programmingmessagesgmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/programmingmessagesgmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Programming Messages

You can program the GPIB-RS232/485/422 by sending it programming messages, which are ASCII strings, by way of its GPIB port.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/programmingmessagessmode.html language=enus -->
## TOPIC 00058: Programming Messages

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/programmingmessagessmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/programmingmessagessmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Programming Messages

You can program the GPIB-RS232/485/422 by sending programming messages (ASCII strings) and data strings to its serial port.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/programmingstepsandexamples.html language=enus -->
## TOPIC 00059: Programming Steps and Examples

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/programmingstepsandexamples.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/programmingstepsandexamples.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Programming Steps and Examples

[General Programming Steps for Communicating with the GPIB-RS232/485/422 over Serial](generalprogrammingstepsforcommunicatingwiththegpibrs232485422overserial.html) applies to programmatically communicating with the GPIB-RS232/485/422 over serial. [General Programming Steps for Communicating with the GPIB-RS232/485/422 over GPIB](generalprogrammingstepsforcommunicatingwiththegpibrs232485422overgpib.html) applies to communicating with the GPIB-RS232/485/422 over GPIB.

Programming examples in this help are in ANSI C using the VISA API for connectivity over GPIB and/or serial.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/rd.html language=enus -->
## TOPIC 00060: rd

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/rd.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/rd.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

rd

#### Type

I/O function

#### Syntax

**rd** #count [addr]<CR>

#### Purpose

You can use rd to read data from the GPIB.

#### Remarks

The argument count is a numeric string preceded by a number sign (#). count specifies the number of GPIB data bytes to read and can range from 1 to 4294967295.

The argument addr specifies the GPIB address of the device to be addressed as a Talker. Addr consists of a primary address and an optional secondary address.

The GPIB-RS232/485/422 reads data from the GPIB until one of the following events occurs:

- The GPIB-RS232/485/422 successfully transfers all data.
- The GPIB END message is received with a data byte.
- The EOS byte is received.
- The I/O time limit is exceeded. The EABO error is recorded.
- The GPIB-RS232/485/422 receives a Device Clear. The EABO error is recorded.
- The addr argument is specified and the requested GPIB addressing bytes cannot be sent. The EBUS error is recorded.

Because you might not know the number of bytes actually read from the GPIB, the GPIB-RS232/485/422 returns the received GPIB data to you in the following manner. First, the GPIB-RS232/485/422 returns all bytes it read from the GPIB. Next, if the number of bytes read is less than count, the GPIB-RS232/485/422 sends null bytes (decimal 0) until the total number of bytes returned to you matches the number specified in count. Finally, it returns a numeric string representing the number of bytes it actually read from the GPIB.

For example, if you send the GPIB-RS232/485/422 the programming message "rd #10"<CR>, it reads data from the GPIB until it receives 10 bytes of data, the END message, or an eos byte. If the GPIB-RS232/485/422 received END with the fourth data byte, it would return the 4 data bytes. Then it would send 6 null bytes followed by an ASCII 4 and <CR><LF>.

You should always read back count bytes of data from the serial port, then look at the numeric string to determine how many bytes were read from the GPIB.

If you call rd with the addr argument, the GPIB-RS232/485/422 must be CIC to perform the addressing. If this is the first function you call that requires GPIB Controller capability, and you have not disabled System Controller capability with rsc, the GPIB-RS232/485/422 sends Interface Clear (IFC*) to make itself CIC. It also asserts Remote Enable.

If you call rd with the addr argument, and you previously passed control to some other GPIB device, control must be passed back to you or you must send IFC* to make yourself CIC before making this call. Otherwise, the ECIC error is recorded.

When performing the addressing for a specified addr, the GPIB-RS232/485/422 sends out its own listen address as well as the talk address of the specified device. It then places itself in Standby Controller state with ATN* unasserted, and remains there after the read operation is complete.

If the addr argument is not specified, the GPIB-RS232/485/422 assumes it has already been addressed to listen by the Controller. If the GPIB-RS232/485/422 is the Controller, and did not address itself to listen before calling rd, the EADR error is recorded and no data bytes are transferred.

If you call rd without an argument, the GPIB-RS232/485/422 records EARG.

#### See Also

[eos](eossmode.html), [eot](eot.html), and [tmo](tmo.html).

#### Example

Read up to 10 bytes from the GPIB device at address 3.

```text
char  cmdBuffer [] = "rd #10 3\r";
char  rdBuffer[11];
char  countBuffer[5];
int count = 0;
memset(rdBuffer,0,11);
memset(countBuffer,0,5);
//Disable Termination Character to allow all NULL
//characters to be read from the serial port
viSetAttribute (instr, VI_ATTR_TERMCHAR_EN, VI_FALSE);
viSetAttribute (instr, VI_ATTR_ASRL_END_IN, VI_ASRL_END_NONE);
viWrite(instr, cmdBuffer, strlen(cmdBuffer), &retCount);
viRead(instr, rdBuffer, 10, &retCount);
//Re-enable Termination Character
viSetAttribute (instr, VI_ATTR_TERMCHAR_EN, VI_TRUE);
viSetAttribute (instr, VI_ATTR_ASRL_END_IN, VI_ASRL_END_TERMCHAR);
viRead(instr, countBuffer, 4, &retCount);
count = atoi(countBuffer);
printf("S Mode read %d bytes from device at PAD 3.\n", count);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/related_documentation.html language=enus -->
## TOPIC 00061: Related Documentation

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/related_documentation.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/related_documentation.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Related Documentation

The following documents contain information that you may find helpful as you use this help file:

- ANSI/EIA-232-D, Interface Between Data Terminal Equipment and Data Circuit-Terminating Equipment Employing Serial Binary Data Interchange
- EIA-485, Standard for Electrical Characteristics of Generators and Receivers for Use in Balanced Digital Multipoint Systems
- EIA-422-A, Electrical Characteristics of Balanced Voltage Digital Interface Circuits
- ANSI/IEEE Standard 488.1-1987, IEEE Standard Digital Interface for Programmable Instrumentation
- ANSI/IEEE Standard 488.2-1992, IEEE Standard Codes, Formats, Protocols, and Common Commands

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/rs232standard.html language=enus -->
## TOPIC 00062: RS232 Standard

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/rs232standard.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/rs232standard.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

RS232 Standard

RS232, as specified in the ANSI/EIA-232-D Standard, *Interface Between
Data Terminal Equipment and Data Circuit-Terminating Equipment
Employing Serial Binary Data Interchange*, standardizes serial
communication between computers and between computer terminals and
modems. Most applications use the RS232 standard for interfacing
peripherals to personal computers. RS232 uses transmission lines in which
the each signal state is represented by referencing the voltage level of a
single line to ground. RS232 was designed for serial communication up to
distances of 50 ft and with data rates up to 20 kbytes/s. However, because
of improvements in line drivers and cabling, you can often increase the
actual performance of the bus past the limitations on speed and distance
recommended in the specification. For more information about the RS232
standard, contact the following organization:

Global Engineering Documents 

15 Inverness Way East 
 
Englewood, CO 80112 
 
(800) 854-7179 

global.ihs.com

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/rs422.html language=enus -->
## TOPIC 00063: RS422

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/rs422.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/rs422.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

RS422

RS422, as specified in the EIA/RS422-A Standard, *Electrical
Characteristics of Balanced Voltage Digital Interface Circuits*, defines
a serial interface much like RS232. However, RS422 uses balanced
(or differential) transmission lines. Balanced transmission lines use
two transmission lines for each signal. The each signal state is
represented not by a voltage level on one line referenced to ground as in
RS232, but rather by the relative voltage of the two lines to each other.
For example, the TX signal is carried on two wires, wire A and wire B.
A logical 1 is represented by the voltage on line A being greater than the
voltage on line B. A logical 0 is represented by the voltage on line A being
less than the voltage on line B. Differential voltage transmission creates a
signal that is much more immune to noise as well as voltage loss due to
transmission line effects. Thus, you can use RS422 for much longer
distances (up to 4,000 ft) and much greater transmission speeds (up to
10 Mbytes/s) than RS232.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/rs485connector.html language=enus -->
## TOPIC 00064: RS485/RS422 Connector

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/rs485connector.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/rs485connector.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

RS485/RS422 Connector

The RS485 port on the GPIB-RS485/RS422 uses a standard 9-pin shielded D-Subminiature male connector with screwlock assemblies. The RS485 connector accepts standard 9-pin D-Subminiature female connectors. The following figure shows the serial connector and the signals supported. For more information about the RS485 signals, refer to [Interfacing to an RS485 Device](interfacingtoanrs485device.html).

[IMAGE alt='image' src='rs485connector.gif']

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/rsc.html language=enus -->
## TOPIC 00065: rsc

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/rsc.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/rsc.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

rsc

Request System Control

#### Type

Initialization function

#### Syntax

**rsc** [bool]<CR>

#### Purpose

You can use rsc to change which device in your GPIB system is System Controller.

#### Remarks

If the argument bool is 1, the GPIB-RS232/485/422 configures itself to be the GPIB System Controller. If the argument bool is 0, the GPIB-RS232/485/422 unconfigures itself to be the System Controller.

If you call rsc without an argument, the GPIB-RS232/485/422 returns its System Controller status, which is 0 if the GPIB-RS232/485/422 is not currently System Controller or 1 if the GPIB-RS232/485/422 is System Controller.

As System Controller, the GPIB-RS232/485/422 can send the Interface Clear (IFC*) and Remote Enable (REN*) messages to GPIB devices. If some other Controller asserts IFC*, the GPIB-RS232/485/422 can respond only if it is not configured as System Controller.

In most applications, the GPIB-RS232/485/422 is System Controller. In some applications, the GPIB-RS232/485/422 is never System Controller. In either case, rsc is used only if the computer will not be System Controller while the program executes. The IEEE 488 standard does not specifically allow schemes in which System Control can be passed from one device to another; however, rsc could be used in such a scheme. The GPIB-RS232/485/422 configures itself to be System Controller at power-on. The assignment made by rsc remains in effect until you call rsc again, call onl, or turn off the GPIB-RS232/485/422.

#### See Also

[sic](sic.html) and [sre](sre.html).

#### Example 1

Enable the GPIB-RS232/485/422 to be the System Controller.

```text
char  buffer [] = "rsc 1\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 2

Disable the System Controller.

```text
char  buffer [] = "rsc 0\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 3

Determine if the GPIB-RS232/485/422 is the System Controller.

```text
char  buffer [] = "rsc\r";
char rscString[4];
viWrite(instr, buffer, strlen(buffer), &retCount);
viRead(instr, rscString, 4, &retCount);
if(rscString[0] == '0')
{
   printf("S Mode is not system controller\n");
}
else if (rscString[0] == '1')
{
   printf("S Mode is system controller\n");
}
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/rsp.html language=enus -->
## TOPIC 00066: rsp

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/rsp.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/rsp.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

rsp

Request (Conduct) a Serial Poll

#### Type

Serial poll function

#### Syntax

**rsp** alist<CR>

#### Purpose

You can use rsp to conduct a serial poll to obtain device-specific status information from one or more GPIB devices.

#### Remarks

The argument alist is a list of addresses separated by commas or spaces. Addresses are device addresses that specify the GPIB addresses you want to poll.

rsp serial polls the specified devices to obtain their status bytes. If bit 6 (hex 40 or RQS bit) of a device's response is set, its status response is positive—that is, that device is requesting service. Before rsp completes, all devices are unaddressed.

The interpretation of each device response, other than the RQS bit, is device specific. For example, the polled device might set a particular bit in the response byte to indicate that it has data to transfer, and another bit to indicate a need for reprogramming. Consult the device documentation for interpretation of the response byte.

Each device serial poll response byte is returned as a numeric string giving the decimal value of the byte, followed by <CR> and <LF>. If a device does not respond in the timeout period, the GPIB-RS232/485/422 returns the string -1 and records the EABO error. The time limit is set to 0.1 second unless you called tmo to change it. Each response corresponds directly to an address you specify. So, the number of response lines, including -1, exactly matches the number of addresses you specify.

If this is the first function you call that requires GPIB Controller capability, and you have not disabled System Controller capability with rsc, the GPIB-RS232/485/422 sends Interface Clear (IFC*) to make itself CIC. It also asserts Remote Enable.

If you passed control to some other GPIB device, control must be passed back to you or you must send IFC* to make yourself CIC before making this call. Otherwise, the ECIC error is posted.

If you call rsp without an argument, the GPIB-RS232/485/422 records the EARG error.

#### See Also

[tmo](tmo.html).

#### Example

Serial poll three devices.

```text
char  buffer [] = "rsp 1+28,5,9\r";
char response1[6];
char response2[6];
char response3[6];
memset(response1,0,6);
memset(response2,0,6);
memset(response3,0,6);
viWrite(instr, buffer, strlen(buffer), &retCount);
viRead(instr, response1, 5, &retCount);
viRead(instr, response2, 5, &retCount);
viRead(instr, response3, 5, &retCount);
printf("Device at PAD 1, SAD 28 reponded %s",response1);
printf("Device at PAD 5 responded %s", response2);
printf("Device at PAD 9 responded %s", response3);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/rsv.html language=enus -->
## TOPIC 00067: rsv

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/rsv.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/rsv.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

rsv

Request Service/Set or Change Serial Poll Status Byte

#### Type

Serial poll function

#### Syntax

**rsv** [spbyte]<CR>

#### Purpose

You can use rsv if the GPIB-RS232/485/422 is not the GPIB Controller and you want to request service from the Controller using the Service Request (SRQ*) signal. The GPIB-RS232/485/422 provides a user-defined status byte when the Controller serial polls it.

#### Remarks

The argument spbyte is a numeric string specifying the decimal value of the new GPIB-RS232/485/422 serial poll response byte.

The serial poll response byte is the status byte the GPIB-RS232/485/422 provides when serial polled by another device that is CIC. If bit 6 (hex 40 or RQS bit) is also set, the GPIB-RS232/485/422 requests service by asserting the SRQ* line.

If you call rsv without an argument, the GPIB-RS232/485/422 returns a numeric string containing the decimal value of its serial poll status byte.

The assignment made by rsv remains in effect until you call rsv again, call onl, or turn off the GPIB-RS232/485/422.

#### Example 1

Request service with serial poll response of 0x46.

```text
char  buffer [] = "rsv \\x46\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 2

Query the current serial poll status byte.

```text
char  buffer [] = "rsv\r";
char rsvString[6];
memset(rsvString,0,6);
viWrite(instr, buffer, strlen(buffer), &retCount);
viRead(instr, rsvString, 6, &retCount);
printf("S Mode serial poll response byte is: 0x%X\n",atoi(rsvString));
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/searching.html language=enus -->
## TOPIC 00068: Searching Help (Windows Only)

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/searching.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/searching.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Searching Help (Windows Only)

Use the **Search** tab to the left of this window to locate content in this help file. If you want to search for words in a certain order, such as "related documentation," add quotation marks around the search words as shown in the example. Searching for terms on the **Search** tab allows you to quickly locate specific information and information in topics that are not included on the **Contents** tab.

#### Wildcards

You also can search using asterisk (*) or question mark (?) wildcards. Use the asterisk wildcard to return topics that contain a certain string. For example, a search for "prog*" lists topics that contain the words "program," "programmatically," "progress," and so on.

Use the question mark wildcard as a substitute for a single character in a search term. For example, "?ext" lists topics that contain the words "next," "text," and so on.

|  | Note Wildcard searching will not work on Simplified Chinese, Traditional Chinese, Japanese, and Korean systems. |
| --- | --- |

#### Nested Expressions

Use nested expressions to combine searches to further refine a search. You can use Boolean expressions and wildcards in a nested expression. For example, "example AND (program OR VI)" lists topics that contain "example program" or "example VI." You cannot nest expressions more than five levels.

#### Boolean Expressions

Click the [IMAGE alt='image' src='bool.gif'] button to add Boolean expressions to a search. The following Boolean operators are available:

- AND (default)—Returns topics that contain both search terms. You do not need to specify this operator unless you are using nested expressions.
- OR —Returns topics that contain either the first or second term.
- NOT —Returns topics that contain the first term without the second term.
- NEAR —Returns topics that contain both terms within eight words of each other.

#### Search Options

Use the following checkboxes on the **Search** tab to customize a search:

- Search previous results —Narrows the results from a search that returned too many topics. You must remove the checkmark from this checkbox to search all topics.
- Match similar words —Broadens a search to return topics that contain words similar to the search terms. For example, a search for "program" lists topics that include the words "programs," "programming," and so on.
- Search titles only —Searches only in the titles of topics.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/selectinganaction.html language=enus -->
## TOPIC 00069: Selecting an Action

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/selectinganaction.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/selectinganaction.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Selecting an Action

The NI GPIB-Serial Converter Wizard has now detected your GPIB-RS232/485/422 and read its current settings. The wizard now can either modify the GPIB-RS232/485/422 configuration or update the GPIB-RS232/485/422 firmware.

To proceed with modifying the GPIB-RS232/485/422 configuration, click **Change Configuration**. To update the GPIB-RS232/485/422 firmware, click **Update Firmware**. Click **Next** to continue with your selected action.

[Using the NI GPIB-Serial Converter Wizard to Configure the GPIB-RS232/485/422](usingthenigpibserialconverterwizardtoconfigurethegpibrs232485422.html)

[Using the NI GPIB-Serial Converter Wizard to Update the GPIB-RS232/485/422 Firmware](usingthenigpibserialconverterwizardtoupdatethegpibrs232485422firmware.html)

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/serialinitializationcodeusingvisa.html language=enus -->
## TOPIC 00070: Serial Initialization Code Using VISA

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/serialinitializationcodeusingvisa.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/serialinitializationcodeusingvisa.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Serial Initialization Code Using VISA

```text
#include "visa.h"

int main(void)
{

ViSession                           defaultRM;
ViSession                           instr;
ViUInt32                            retCount;
ViUInt32                            writeCount;
ViStatus                            status;
unsigned char                       buffer[100];
unsigned char                       stringinput[512];

/* Begin by initializing the system */
status = viOpenDefaultRM(&defaultRM);
if (status < VI_SUCCESS) { 
/* Error Initializing VISA...exiting */
return -1;
}

/* Open communication with serial port at COM1.*/
status = viOpen(defaultRM, "ASRL1::INSTR", VI_NULL, VI_NULL, &instr);

/* Set Baud Rate and other serial port settings */
viSetAttribute(instr, VI_ATTR_ASRL_BAUD, 9600);
viSetAttribute(instr, VI_ATTR_ASRL_DATA_BITS, 8);
viSetAttribute(instr, VI_ATTR_ASRL_PARITY, VI_ASRL_PAR_NONE);
viSetAttribute(instr, VI_ATTR_ASRL_STOP_BITS, VI_ASRL_STOP_ONE);
viSetAttribute (instr, VI_ATTR_ASRL_FLOW_CNTRL, VI_ASRL_FLOW_RTS_CTS);
viSetAttribute (instr, VI_ATTR_TERMCHAR, 10);
viSetAttribute (instr, VI_ATTR_TERMCHAR_EN, VI_TRUE);
viSetAttribute (instr, VI_ATTR_ASRL_END_IN, VI_ASRL_END_TERMCHAR);

/*
TODO: Insert application specific code here
*/

/* Close down the system */
status = viClose(instr);
status = viClose(defaultRM);
return 0;
}
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/serialpollresponses.html language=enus -->
## TOPIC 00071: Serial Poll Responses

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/serialpollresponses.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/serialpollresponses.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Serial Poll Responses

When serial polled, the GPIB-RS232/485/422 returns status information to the GPIB Controller through the serial poll response byte. The GPIB-RS232/485/422 maintains this status byte throughout operation, regardless of the srqen configuration.

|  | Note Be sure to serial poll the GPIB-RS232/485/422 address and not the serial device address to obtain the serial poll response byte. For more information about addressing, refer to Addressing the GPIB-RS232/485/422 and Serial Device. Unlike the GPIB-232/485/CT/CV-A, which responded to serial polls on either address, the GPIB-RS232/485/422 responds only to serial polls on the GPIB-RS232/485/422 address. For more information about this and other differences, refer to Differences Between the GPIB-232/485CT/CV-A and GPIB-RS232/485/422. |
| --- | --- |

The following table lists the meaning of each bit in the serial poll response byte.

##### Serial Poll Response Byte

| Bit | Mnemonic | Meaning |
| --- | --- | --- |
| 0 | — | Not Used |
| 1 | BF | Serial port receive buffer is full |
| 2 | GERR | GPIB error—refer to stat |
| 3 | SERR | Serial error—refer to stat |
| 4 | BNE | Serial port receive buffer not empty |
| 5 | EOS | EOS character received |
| 6 | RQS | Request service (SRQ* asserted) |
| 7 | — | Not Used |

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/serialporterrorcodes.html language=enus -->
## TOPIC 00072: Serial Port Error Codes

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/serialporterrorcodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/serialporterrorcodes.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Serial Port Error Codes

The following paragraphs describe the serial port errors in detail. The
number preceding each description is the error code numeric value.

In S Mode, when a serial port error occurs as the GPIB-RS232/485/422
receives a programming message, the error is recorded and the message is
discarded. If a serial port error occurs during a data transfer such as cmd,
rd, or wrt, that transfer is aborted. You can use the spign function to tell the GPIB-RS232/485/422 to ignore all serial port errors. When serial port
errors are ignored, bytes that arrive with errors are not discarded, and no
error is recorded in the serial port error code returned by stat.

| NSER | 0 |
| --- | --- |
|  | The GPIB-RS232/485/422 reports this value when there is no serial port error detected as a result of the last operation. |
| EPAR | 1 |
|  | The GPIB-RS232/485/422 records this error when the parity of the received character is not what was expected; one or more bits of the received character were corrupted in a way that changed the character's parity. |
| EORN | 2 |
|  | The GPIB-RS232/485/422 records this error when characters arrive at the serial port faster than the serial port can accept them. When this error occurs, one or more characters sent to the serial port have been lost. If this error occurs, check to see that the GPIB-RS232/485/422 and your serial device are using the same serial port settings. |
| EOFL | 3 |
|  | The GPIB-RS232/485/422 records this error when the GPIB-RS232/485/422 internal serial port buffer overflows. This error should occur only if XON/XOFF is disabled and no hardware handshake is in effect. |
| EFRM | 4 |
|  | The GPIB-RS232/485/422 records this error when a character is received whose stop bits are not in the expected place. This error can happen when the number-of-bits-per-character setting of the GPIB-RS232/485/422 does not match your serial device. It can also happen if the baud rates of the GPIB-RS232/485/422 and your serial device do not match, or if one side of the serial link does not use parity and the other side does. The GPIB-RS232/485/422 also records this error when it receives a serial break from the attached serial device. The reception of a serial break is detected when the Receive Data (RXD) line is unasserted for longer than a full word transmission time (that is, the total time of start bit + data bits + parity + stop bits). |

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/serialportfunctionsgmode.html language=enus -->
## TOPIC 00073: Serial Port Functions

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/serialportfunctionsgmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/serialportfunctionsgmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Serial Port Functions

Serial port functions initialize and manage the GPIB-RS232/485/422 serial port.

- [**ec**ho](echogmode.html)
- [**sps**et](spset.html)
- [**x**on](xongmode.html)
- [**spi**gn](spigngmode.html)

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/serialportfunctionssmode.html language=enus -->
## TOPIC 00074: Serial Port Functions

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/serialportfunctionssmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/serialportfunctionssmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Serial Port Functions

The serial port functions initialize and manage the GPIB-RS232/485/422 serial port.

- [echo](echosmode.html)
- [spign](spignsmode.html)
- [xon](xonsmode.html)

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/serialporttransmission.html language=enus -->
## TOPIC 00075: Serial Port Transmission

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/serialporttransmission.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/serialporttransmission.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Serial Port Transmission

The GPIB-RS232/485/422 checks the data received from the serial device for errors while it buffers data. If a serial port error occurs, the GPIB-RS232/485/422 records the appropriate error code. There are two ways to determine if a serial port error has occurred:

- Use the stat function to request the GPIB-RS232/485/422 status information. After the serial error code has been reported, it is cleared automatically, and no further action to the GPIB-RS232/485/422 is necessary.
- Serial poll the GPIB-RS232/485/422 and check the serial poll response byte to see if its SERR bit is set. Refer to Serial Poll Responses for more information.

You can program the GPIB-RS232/485/422 to ignore serial port errors using the spign function.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/specifications.html language=enus -->
## TOPIC 00076: Specifications

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/specifications.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/specifications.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Specifications

This topic includes the GPIB-RS232/485/422 physical, electrical, and environmental characteristics.

#### Physical

| Dimensions | 16.01 x 9.35 x 3.15 cm (6.3 x 3.68 x 1.24 in.) |
| --- | --- |
| Case material | PC-ABS plastic |
| Weight |  |
| RS232 | 192 g (6.75 oz) |
| RS485/RS422 | 196 g (6.875 oz) |
| GPIB cable | Type X2 shielded |

#### Connectors

| GPIB | IEEE 488 24-pin |
| --- | --- |
| RS232 | DB-9 male |
| RS485/RS422 | DB-9 male |
| DC power | Coaxial plug (single output models)5.5 mm outer diameter2.1 mm inner diameter, female11 mm length, center "+" |

#### Signaling

| GPIB | 3-wire |
| --- | --- |
| RS232/RS485 | Baud rates up to 115.2 kb/s |

#### Power Requirements

| Input voltage range | 9 to 28 VDC |
| --- | --- |
| Current consumption at 12 VDC | 300 mA typical, 800 mA maximum |
| Fuse rating and type | Fast acting 2.2 A 125 V, surface mount |

##### 12 VDC Power Supply

| Input voltage range | 100 to 240 VAC, 47 to 63 Hz |
| --- | --- |

#### Environment

| Maximum altitude | 2,000 m (at 25° C ambient temperature) |
| --- | --- |
| Pollution Degree | 2 |
| Indoor use only |  |

##### Operating Environment

|  | Note For the GPIB-RS232/485/422 to operate correctly over the entire specified ambient temperature range, stacking the product is not recommended. |
| --- | --- |

| Ambient temperature range | 0 to 55° C (Tested in accordance with IEC-60068-2-1 and IEC-60068-2-2.) |
| --- | --- |
| Relative humidity range | 10 to 90%, noncondensing (Tested in accordance with IEC-60068-2-56.) |

##### Storage Environment

| Ambient temperature range | –20 to 70° C (Tested in accordance with IEC-60068-2-1 and IEC-60068-2-2.) |
| --- | --- |
| Relative humidity range | 5 to 95%, noncondensing (Tested in accordance with IEC-60068-2-56.) |

##### Shock and Vibration

| Operational shock | 30 g peak, half-sine, 11 ms pulse (Tested in accordance with IEC-60068-2-27. Test profile developed in accordance with MIL-PRF-28800F.) |
| --- | --- |
| Random vibration |  |
| Operating | 5 to 500 Hz, 0.3 grms |
| Nonoperating | 5 to 500 Hz, 2.4 grms (Tested in accordance with IEC-60068-2-64. Nonoperating test profile exceeds the requirements of MIL-PRF-28800F, Class 3.) |

#### Safety

This product is designed to meet the requirements of the following standards of safety for information technology equipment:

- IEC 60950-1, EN 60950-1
- UL 60950-1, CAN/CSA C22.2 No. 60950-1

|  | Note For UL and other safety certifications, refer to the product label or visit ni.com/certification, search by model number or product line, and click the appropriate link in the Certification column. |
| --- | --- |

|  | Note The protection provided by this equipment may be impaired if it is used in a manner not described in this document. |
| --- | --- |

#### Electromagnetic Compatibility

This product is designed to meet the requirements of the following standards of EMC for electrical equipment for measurement, control, and laboratory use:

- EN 61326 EMC requirements; Minimum Immunity
- EN 55011 Emissions; Group 1, Class A
- CE, C-Tick, ICES, and FCC Part 15 Emissions; Class A

|  | Note For EMC compliance, operate this device according to product documentation. |
| --- | --- |

#### CE Compliance

This product meets the essential requirements of applicable European Directives, as amended for CE marking, as follows:

- 73/23/EEC; Low-Voltage Directive (safety)
- 89/336/EEC; Electromagnetic Compatibility Directive (EMC)

|  | Note Refer to the Declaration of Conformity (DoC) for this product for any additional regulatory compliance information. To obtain the DoC for this product, visit ni.com/certification, search by model number or product line, and click the appropriate link in the Certification column. |
| --- | --- |

#### Waste Electrical and Electronic Equipment (WEEE)

|  | EU Customers At the end of their life cycle, all products must be sent to a WEEE recycling center. For more information about WEEE recycling centers and National Instruments WEEE initiatives, visit ni.com/environment/weee.htm. |
| --- | --- |

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/spigngmode.html language=enus -->
## TOPIC 00077: spign

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/spigngmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/spigngmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

spign

Ignore Serial Port Errors

#### Type

Serial port function

#### Syntax

**spi**gn [bool]<CR>

#### Purpose

You can use spign at the beginning of your program to change the effect serial port errors have on the storage of a character received with a serial error. This function tells the GPIB-RS232/485/422 to ignore or not to ignore the occurrence of serial port errors. By default, the GPIB-RS232/485/422 ignores serial port errors.

#### Remarks

If the argument bool is 0, the GPIB-RS232/485/422 does not ignore serial port errors. In this case, the GPIB-RS232/485/422 does not store characters that contain serial errors. Also, the error is indicated in the serial error code the stat function returns.

The serial port errors include parity, overrun, framing, and overflow errors. [Status and Error Message Information](statusanderrormessageinformation.html) includes a list of serial port errors.

If the argument bool is 1, the GPIB-RS232/485/422 ignores serial port errors. Bytes that arrive with serial port errors are stored in the buffer and are later sent out of the GPIB port when the serial device is talk addressed. The stat function reports no serial error code.

If you call spign without an argument, the GPIB-RS232/485/422 returns the current setting.

The assignment spign makes remains in effect until you call spign again, call onl, or turn off the GPIB-RS232/485/422.

#### Example 1

```text
// Do not ignore serial port errors.
char spignCommand [] = "spign 0\r";
viWrite (GPIB232, spignCommand, strlen(spignCommand), &retCount);
```

#### Example 2

```text
// Ignore serial port errors.
char spignCommand [] = "spign 1\r";
viWrite (GPIB232, spignCommand, strlen(spignCommand), &retCount);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/spignsmode.html language=enus -->
## TOPIC 00078: spign

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/spignsmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/spignsmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

spign

Ignore Serial Port Errors

#### Type

Serial port function

#### Syntax

**spi**gn [bool]<CR>

#### Purpose

You can use spign at the beginning of your program to change the effect that serial port errors have on how the GPIB-RS232/485/422 processes programming messages and data. This function tells the GPIB-RS232/485/422 to ignore or not to ignore the occurrence of serial port errors. By default, serial port errors are ignored.

#### Remarks

If the argument bool is 0, the GPIB-RS232/485/422 does not ignore serial port errors. In this case, the GPIB-RS232/485/422 does not execute programming messages that contain serial port errors. Also, if a serial port error occurs with any byte contained in a cmd or wrt data string, the GPIB-RS232/485/422 discards that data byte and all remaining bytes in the string.

The serial port errors include parity, overrun, framing, and overflow errors. A list of serial port errors is in [Status and Error Message Information](statusanderrormessageinformation.html).

If the argument bool is 1, the GPIB-RS232/485/422 executes all programming messages and sends all data, even if serial port errors occur as the messages and data bytes are received. No serial error code is reported by the stat function.

If you call spign without an argument, the GPIB-RS232/485/422 returns the current setting.

The assignment made by spign remains in effect until you call spign again, call onl, or turn off the GPIB-RS232/485/422.

#### See Also

[cmd](cmd.html) and [wrt](wrt.html).

#### Example 1

Configure the GPIB-RS232/485/422 not to execute programming messages or process data that contains serial port errors.

```text
char  buffer [] = "spign 0\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 2

Configure the GPIB-RS232/485/422 to execute programming messages and send all data, even if serial port errors occur.

```text
char  buffer [] = "spign 1\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/spset.html language=enus -->
## TOPIC 00079: spset

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/spset.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/spset.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

spset

Change Serial Port Parameters

#### Type

Serial port function

#### Syntax

**sps**et [baud] [parity] [databits] [stopbits]<CR>

#### Purpose

You can use spset at the beginning of your program to set the GPIB-RS232/485/422 serial port characteristics (baud rate, parity, data bits, and stop bits) to match those your serial device requires.

#### Remarks

The argument baud is a numeric string specifying the baud rate (300, 600, 1200, 2400, 4800, 9600, 19200, 38400, 76800, or 115200). The argument parity is a character specifying the parity (e for even, o for odd, n for none). The argument databits is a character specifying the number of data bits (7 or 8). The argument stopbits is a character specifying the number of stop bits (1 or 2). If you call spset without an argument, the GPIB-RS232/485/422 returns its current serial port configuration.

Until you call spset, the following characteristics are in effect: 9600 is the baud rate, parity is disabled, 8 is the number of data bits, and 1 is the number of stop bits.

If you must reconfigure the GPIB-RS232/485/422 serial port, wait until communication with the serial port is not taking place. Remember that calling spset with one or more arguments also discards any serial data buffered inside the GPIB-RS232/485/422.

The assignment spset makes remains in effect until you call spset again, call onl, or turn off the GPIB-RS232/485/422.

#### Example 1

```text
// Set up the serial port of GPIB-RS232/485/422 to
// keep its current baud rate, current parity,
// and to use 7 data bits and 2 stop bits.
char spsetCommand [] = "spset 7 2\r"; 
viWrite (GPIB232, spsetCommand, strlen(spsetCommand), &retCount);
```

#### Example 2

```text
// What are the current GPIB-RS232/485/422 serial port settings?
char spsetQuery [] = "spset\r";
char buffer [30];

viWrite (GPIB232, spsetQuery, strlen(spsetQuery), &retCount);
viRead  (GPIB232, buffer, 30, &retCount);
// buffer will contain 9600 N 7 2<CR><LF>
// (9600 baud, no parity, 7 data bits,
// 2 stop bits).
```

#### Example 3

```text
// Set the GPIB-RS232/485/422 serial port to 115200
// baud, no parity, 8 data bits, and 1 stop bit.
char spsetCommand [] = "spset 115200 n 8 1\r";
viWrite (GPIB232, spsetCommand, strlen(spsetCommand), &retCount);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/srqen.html language=enus -->
## TOPIC 00080: srqen

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/srqen.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/srqen.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

srqen

Enable/Disable Setting of SRQ*

#### Type

GPIB function

#### Syntax

**srq**en [mask]<CR>

#### Purpose

You can use srqen when you want to allow the GPIB-RS232/485/422 to assert SRQ* under the conditions described in [Service Request Conditions](servicerequestconditions.html).

#### Remarks

When the argument mask is 0, the GPIB-RS232/485/422 never asserts SRQ*. When the argument mask is greater than 0, the GPIB-RS232/485/422 asserts SRQ* under the conditions each mask bit represents. The following table describes the mask bits.

##### SRQ Mask Bits in G Mode

| Bit | Hex Value | Decimal Value | Mnemonic | Description |
| --- | --- | --- | --- | --- |
| 0 | 1 | 1 | — | Not used |
| 1 | 2 | 2 | BF | Serial port receive buffer full |
| 2 | 4 | 4 | GERR | GPIB error; refer to stat |
| 3 | 8 | 8 | SERR | Serial error; refer to stat |
| 4 | 10 | 16 | BNE | Serial port receive buffer not empty |
| 5 | 20 | 32 | EOS | EOS character received |
| 6 | 40 | 64 | — | Not used |
| 7 | 80 | 128 | — | Not used |

To determine the mask value you want, add the hex or decimal values of the conditions on which you want SRQ* to be asserted. For example, if you want SRQ* asserted on GPIB errors and serial port errors, call srqen with a mask of 12 (4 for GERR and 8 for SERR).

The srqen power-on default is disabled—that is, SRQ* is never asserted.

If you call srqen without an argument, the GPIB-RS232/485/422 returns a decimal string indicating the the current setting decimal value.

The assignment srqen makes remains in effect until you call srqen again, call onl, or turn off the GPIB-RS232/485/422.

#### See Also

[eos](eosgmode.html), [spign](spigngmode.html), and [stat](statgmode.html).

#### Example 1

```text
// Never assert SRQ*
char srqenCommand [] = "srqen 0\r";
viWrite (GPIB232, srqenCommand, strlen(srqenCommand), &retCount);
```

#### Example 2

```text
// Assert SRQ* when a GPIB error occurs.
char srqenCommand [] = "srqen 4\r";
viWrite (GPIB232, srqenCommand, strlen (srqenCommand), &retCount);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/statgmode.html language=enus -->
## TOPIC 00081: stat

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/statgmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/statgmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

stat

Return GPIB-RS232/485/422 Status

#### Type

General-use function

#### Syntax

**st**at [[c] n]<CR>

or

**st**at [c] s<CR>

or

**st**at [c] n s<CR>

#### Purpose

You can use stat to obtain the GPIB-RS232/485/422 status to see if certain conditions are currently present. stat is used most often to see if the previous operation resulted in an error.

#### Remarks

The GPIB-RS232/485/422 responds with status information in a form depending on the mode or combination of modes you choose. n indicates that the status information is returned as numeric strings. s indicates that the status information is returned in symbolic format—that is, as mnemonic strings. Status bits are separated by a comma. Normally, you use s only when you are debugging your code and want to print the mnemonic for each piece of status information. c specifies that the status is returned after each programming message, eliminating the need to call stat after each programming message.

You would probably use s, or symbolic format, only when you are debugging your code and you want to print the mnemonic for each piece of status information.

If you call stat without an argument, continuous status reporting is disabled.

The status information returned by the GPIB-RS232/485/422 contains four pieces of information: the GPIB-RS232/485/422 status, a GPIB-error code, a serial-error code, and a count. The GPIB-RS232/485/422 returns a <CR><LF> following each piece of the response and asserts EOI* with the final <LF> that comes after count.

Status represents a combination of GPIB-RS232/485/422 conditions. Inside the GPIB-RS232/485/422, status is stored as a 16-bit integer. Each bit in the integer represents a single condition. A bit value of 1 indicates the corresponding condition is in effect. A bit value of 0 indicates the condition is not in effect. Because more than one GPIB-RS232/485/422 condition can exist at one time, more than one bit can be set in status. The highest order bit of status, also called the sign bit, is set when the GPIB-RS232/485/422 detects either a GPIB error or a serial port error. When status is negative, an error condition exists.

The following table lists the values and descriptions of GPIB status conditions the stat function might return.

##### G Mode Conditions stat Returns

| Numeric Value (n) | Symbolic Value (s) | Description | Bit |
| --- | --- | --- | --- |
| –32768 | ERR | Error detected | 15 |
| 16384 | — | Reserved | 14 |
| 8192 | — | Reserved | 13 |
| 4096 | — | Reserved | 12 |
| 2048 | — | Reserved | 11 |
| 1024 | — | Reserved | 10 |
| 512 | — | Reserved | 9 |
| 256 | CMPL | Operation completed | 8 |
| 128 | — | Reserved | 7 |
| 64 | — | Reserved | 6 |
| 32 | — | Reserved | 5 |
| 16 | — | Reserved | 4 |
| 8 | — | Reserved | 3 |
| 4 | — | Reserved | 2 |
| 2 | — | Reserved | 1 |
| 1 | — | Reserved | 0 |

The GPIB error code represents a single GPIB error condition present. The serial error code represents a single serial error condition present. count is the number of bytes currently contained in the GPIB-RS232/485/422 serial port receive buffer.

The following table lists the values and descriptions of GPIB error conditions the stat function might return.

##### G Mode GPIB Error Conditions stat Returns

| Numeric Value (n) | Symbolic Value (s) | Description |
| --- | --- | --- |
| 0 | NGER | No GPIB error condition to report |
| 1 | — | Reserved |
| 2 | — | Reserved |
| 3 | — | Reserved |
| 4 | EARG | Invalid argument or arguments |
| 5 | — | Reserved |
| 6 | — | Reserved |
| 7-10 | — | Reserved |
| 11 | ECAP | No capability for operation |
| 12-13 | — | Reserved |
| 14 | — | Reserved |
| 15-16 | — | Reserved |
| 17 | ECMD | Unrecognized command |

The following table lists the serial port errors the stat function might return.

##### Serial Port Error Conditions stat Returns

| Numeric Value (n) | Symbolic Value (s) | Description |
| --- | --- | --- |
| 0 | NSER | No serial port error condition to report |
| 1 | EPAR | Serial port parity error |
| 2 | EORN | Serial port overrun error |
| 3 | EOFL | Serial port receive buffer overflow |
| 4 | EFRM | Serial port framing error |

[Status and Error Message Information](statusanderrormessageinformation.html) includes a detailed description of the conditions under which each bit in status is set or cleared.

The GPIB-RS232/485/422 updates the status and count variables at the end of each programming message. The serial and GPIB error variables are updated whenever a new error occurs and are cleared automatically when status is reported.

When you want to begin continuous status reporting, send the stat c s<CR>, stat c n<CR>, or stat c n s<CR> programming message. When you call stat with both n and s modes specified, the numeric status is always returned first.

The continuous status setting remains in effect until you call stat again, call onl, or turn off the GPIB-RS232/485/422.

#### Example 1

```text
char statCommand [] = "stat n\r";
char statusString [11];
char gpibERR [11];
char serialERR [11];
char count [11];
int statusValue;

memset(statusString,0,11);
memset(gpibERR,0,11);
memset(serialERR,0,11);
memset(count,0,11);

//Enable EOS=<LF> in VISA so that viRead terminates on linefeed
viSetAttribute (GPIB232, VI_ATTR_TERMCHAR, 10);
viSetAttribute (GPIB232, VI_ATTR_TERMCHAR_EN, VI_TRUE);


// Tell GPIB-RS232/485/422 to send numeric
// status.
viWrite (GPIB232, statCommand, strlen(statCommand), &retCount);


// Read up to 10 bytes of each piece of status.
// The GPIB-RS232/485/422 returns 4 pieces of
// status. We are set up to terminate
// viRead on linefeed, which is what
// terminates each piece of status.

// Now read the status from the
// GPIB-RS232/485/422.
viRead (GPIB232, statusString, 10, &retCount);
statusValue = atoi (statusString);

// Read GPIB-error.
viRead (GPIB232, gpibERR, 10, &retCount);

// Read serial-error.
viRead (GPIB232, serialERR, 10, &retCount);

// Read count.
viRead (GPIB232, count, 10, &retCount);

// If error occurred
if (statusValue < 0)
{
    // Print GPIB-error and serial-error
    // values to determine what errors occurred.
    printf ("GPIB-error = %s\n", gpibERR);
    printf ("serial-error = %s\n", serialERR);
}
```

#### Example 2

```text
// Turn on continuous status reporting,
// in numeric format.
char statCommand [] = "stat c n\r";
char statusString [100];
memset(statusString,0,100);
viWrite (GPIB232, statCommand, strlen(statCommand), &retCount); 

// If we have 3 bytes in the serial port
// buffer, a typical response would be:
// 262<CR><LF>0<CR><LF>0<CR><LF>3<CR><LF>
// Read the GPIB-RS232/485/422 status; read 100
// bytes or until EOI is received.
viRead (GPIB232, statusString, 100, &retCount);
// Print the status information.
printf ("GPIB-RS232/485/422 status is: %s\n", statusString);
```

#### Example 3

```text
// Turn on continuous status reporting,
// in symbolic format.
char statCommand [] = "stat c s\r";
char statusString [51];
viWrite (GPIB232, statCommand, strlen(statCommand), &retCount); 
// Read the GPIB-RS232/485/422 status; read 50
// bytes or until EOI is received.
viRead (GPIB232, statusString, 50, &retCount);
statusString [retCount] = '\0';
// Print the status information.
printf ("GPIB-RS232/485/422 status is: %s\n", statusString);

Printed information is:
GPIB-RS232/485/422 status is :
CMPL
NGER
NSER
0
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/statsmode.html language=enus -->
## TOPIC 00082: stat

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/statsmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/statsmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

stat

Return GPIB-RS232/485/422 Status

#### Type

General-use function

#### Syntax

**st**at [[c] n]<CR>

or

**st**at [c] s<CR>

or

**st**at [c] n s<CR>

#### Purpose

You can use stat to obtain the GPIB-RS232/485/422 status to see if certain conditions are currently present. stat is used most often to see if the previous operation resulted in an error.

#### Remarks

You should use stat frequently in the early stages of your program development when the responses of your GPIB devices are likely to be unpredictable.

The GPIB-RS232/485/422 responds with status information in a form depending on the mode or combination of modes you choose. n indicates that the status information is returned as numeric strings. s indicates that the status information is returned in symbolic format—that is, as mnemonic strings. Status bits are separated by a comma. Normally, you use s only when you are debugging your code and want to print the mnemonic for each piece of status information. c specifies that the status is returned after each programming message, eliminating the need to call stat after each programming message.

If you call stat without an argument, continuous status reporting is disabled.

The status information returned by the GPIB-RS232/485/422 contains four pieces of information: the GPIB-RS232/485/422 status, a GPIB error code, a serial error code, and a count. A <CR><LF> follows each piece of the response.

Status represents a combination of GPIB-RS232/485/422 conditions. Inside the GPIB-RS232/485/422, status is stored as a 16-bit integer. Each bit in the integer represents a single condition. A bit value of 1 indicates that the corresponding condition is in effect. A bit value of 0 indicates that the condition is not in effect. Because more than one GPIB-RS232/485/422 condition can exist at one time, more than one bit can be set in status. The highest order bit of status, also called the sign bit, is set when the GPIB-RS232/485/422 detects either a GPIB error or a serial port error. When status is negative, an error condition exists.

The following table lists the values and descriptions of the GPIB status conditions that the stat function might return.

##### S Mode GPIB Status Conditions stat Returns

| Numeric Value (n) | Symbolic Value (s) | Description | Bit |
| --- | --- | --- | --- |
| –32768 | ERR | Error detected | 15 |
| 16384 | TIMO | Timeout | 14 |
| 8192 | END | EOI* or EOS detected | 13 |
| 4096 | SRQI | SRQ* detected while CIC | 12 |
| 2048 | — | Reserved | 11 |
| 1024 | — | Reserved | 10 |
| 512 | — | Reserved | 9 |
| 256 | CMPL | Operation completed | 8 |
| 128 | LOK | Lockout state | 7 |
| 64 | REM | Remote state | 6 |
| 32 | CIC | Controller-In-Charge | 5 |
| 16 | ATN | Attention asserted | 4 |
| 8 | TACS | Talker active | 3 |
| 4 | LACS | Listener active | 2 |
| 2 | DTAS | Device trigger active state | 1 |
| 1 | DCAS | Device clear active state | 0 |

The GPIB error code represents a single GPIB error condition present.

The serial error code represents a single serial port error condition present.

count is the number of bytes transferred over the GPIB by the last rd, wrt, or cmd function.

The following table lists values and descriptions of GPIB error conditions that the stat function might return.

##### S Mode GPIB Error Conditions stat Returns

| Numeric Value (n) | Symbolic Value (s) | Description |
| --- | --- | --- |
| 0 | NGER | No GPIB error condition to report |
| 1 | ECIC | Command requires GPIB-RS232/485/422 to be CIC |
| 2 | ENOL | Write detected no Listeners |
| 3 | EADR | GPIB-RS232/485/422 not addressed correctly |
| 4 | EARG | Invalid argument or arguments |
| 5 | ESAC | Command requires GPIB-RS232/485/422 to be System Controller |
| 6 | EABO | I/O operation aborted |
| 7-10 | — | Reserved |
| 11 | ECAP | No capability for operation |
| 12-13 | — | Reserved |
| 14 | EBUS | Command bytes could not be sent |
| 15-16 | — | Reserved |
| 17 | ECMD | Unrecognized command |

The following table lists the serial port error conditions that the stat function might return.

##### S Mode Serial Port Error Conditions stat Returns

| Numeric Value (n) | Symbolic Value (s) | Description |
| --- | --- | --- |
| 0 | NSER | No serial port error condition to report |
| 1 | EPAR | Serial port parity error |
| 2 | EORN | Serial port overrun error |
| 3 | EOFL | Serial port receive buffer overflow |
| 4 | EFRM | Serial port framing error |

A detailed description of the conditions under which each bit in status is set or cleared is in [Status and Error Message Information](statusanderrormessageinformation.html).

In general, the GPIB-RS232/485/422 updates the first three status variables at the end of each programming message. It updates the fourth status variable, count, after a cmd, rd, or wrt function. The errors reported correspond to the previous programming message. For example, if you call wrt and then stat s, any errors returned to you correspond to errors in the wrt programming message, not stat. However, if status is returned in continuous mode, the status information corresponds to the current programming message. For example, suppose you called stat c s to set up continuous status reporting. After reading the status information returned from the stat call, you call wrt. The GPIB-RS232/485/422 then returns the status information that corresponds to the wrt message.

To begin continuous status reporting, send the stat c s, stat c n, or stat c n s programming message. Status information is immediately returned indicating the current status conditions. When you call stat with both s and n, the numeric status is always returned first.

Notice that when you send several programming messages to the GPIB-RS232/485/422, it buffers them and processes each one without any delay in between. However, if you enable continuous status reporting and check the status of each programming message before sending the next, the GPIB-RS232/485/422 waits for each subsequent programming message to arrive at the serial port before processing it. This slows down the overall performance of your program. If speed is a primary concern, disable continuous status reporting.

The continuous status setting remains in effect until you call stat again, call onl, or turn off the GPIB-RS232/485/422.

#### Example 1

Get the GPIB-RS232/485/422 status as numeric values.

```text
char  statusValueBuffer[10];
int   statusValue;
char  gpibErrorBuffer[10];
int   gpibError;
char  serialErrorBuffer[10];
int   serialError;
char  countBuffer[10];
int   count;
char  buffer [] = "stat n\r";

memset(statusValueBuffer,0,10);
memset(gpibErrorBuffer,0,10);
memset(serialErrorBuffer,0,10);
memset(countBuffer,0,10);

viWrite(instr, buffer, strlen(buffer), &retCount);
viRead(instr, statusValueBuffer, 10, &retCount);

statusValue = atoi(statusValueBuffer);

if(statusValue & (1 << 15))
{
   printf("Error detected\n");
}
if(statusValue & (1 << 14))
{
   printf("Timeout\n");
}
if(statusValue & (1 << 13))
{
   printf("EOI* or EOS detected\n");
}
if(statusValue & (1 << 12))
{
   printf("SRQ* detected while CIC\n");
}
if(statusValue & (1 << 8))
{
   printf("Operation Complete\n");
}
if(statusValue & (1 << 7))
{
   printf("Lockout State\n");
}
if(statusValue & (1 << 6))
{
   printf("Remote State\n");
}
if(statusValue & (1 << 5))
{
   printf("Controller-In-Charge\n");
}
if(statusValue & (1 << 4))
{
   printf("Attention Asserted\n");
}
if(statusValue & (1 << 3))
{
   printf("Talker Active\n");
}
if(statusValue & (1 << 2))
{
   printf("Listener Active\n");
}
if(statusValue & (1 << 1))
{
   printf("Device Trigger Active State\n");
}
if(statusValue & 1)
{
   printf("Device Clear Active State\n");
}


viRead(instr, gpibErrorBuffer, 10, &retCount);
gpibError = atoi(gpibErrorBuffer);
switch(gpibError)
{
   case 0:
      printf("No GPIB error condition\n");
      break;
   case 1:
      printf("Command requires S Mode to be CIC\n");
      break;
   case 2:
      printf("No listeners detected\n");
      break;
   case 3:
      printf("S Mode not addressed correctly\n");
      break;
   case 4:
      printf("Invalid argument\n");
      break;
   case 5:
      printf("Command requires S Mode to be System Controller\n");
      break;
   case 6:
      printf("I/O operation aborted\n");
      break;
   case 11:
      printf("S Mode has no capability for that operation\n");
      break;
   case 14:
      printf("Command bytes could not be sent\n");
      break;
   case 17:
      printf("Unrecognized command\n");
      break;
}

viRead(instr, serialErrorBuffer, 10, &retCount);
serialError = atoi(serialErrorBuffer);
switch(serialError)
{
   case 0: 
      printf("No serial port error\n");
      break;
   case 1: 
      printf("Serial port parity error\n");
      break;
   case 2: 
      printf("Serial port overrun error \n");
      break;
   case 3: 
      printf("Serial port receive buffer overflow error \n");
      break;
   case 4: 
      printf("Serial port framing error\n");
      break;
}

viRead(instr, countBuffer, 10, &retCount);
count = atoi(countBuffer);
printf("Count is %d\n",count);
```

#### Example 2

Get the GPIB-RS232/485/422 status as symbolic values.

```text
char  statusValueBuffer[30];
char  gpibErrorBuffer[10];
char  serialErrorBuffer[10];
char  countBuffer[10];
int   count;

char  buffer [] = "stat s\r";

memset(statusValueBuffer,0,30);
memset(gpibErrorBuffer,0,10);
memset(serialErrorBuffer,0,10);
memset(countBuffer,0,10);

viWrite(instr, buffer, strlen(buffer), &retCount);

viRead(instr, statusValueBuffer, 30, &retCount);
viRead(instr, gpibErrorBuffer, 30, &retCount); 
viRead(instr, serialErrorBuffer, 30, &retCount); 
viRead(instr, countBuffer, 30, &retCount); 
count = atoi(countBuffer);
```

#### Example 3

The following list illustrates what appears on the screen when you are programming the GPIB-RS232/485/422 from a terminal. GPIB-RS232/485/422 responses are in bold text. The statements in parentheses are comments.

```text
stat c s n (Enable continuous status reporting.)
344
0
0
3
CMPL,REM,ATN,TACS ( Status returned. )
NGER
NSER
3
wrt 10
ABCDE ( Write the string ABCDE. )
296 ( to device 10. )
0 ( Status returned. )
0
5
CMPL,CIC,TACS
NGER
NSER
5
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/statusinformationanderrorhandlingcharacteristicsgmode.html language=enus -->
## TOPIC 00083: Status Information and Error Handling Characteristics

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/statusinformationanderrorhandlingcharacteristicsgmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/statusinformationanderrorhandlingcharacteristicsgmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Status Information and Error Handling Characteristics

The function descriptions in [G Mode Functions](gmodefunctions.html) explain that the GPIB-RS232/485/422 records specific status and error information. This means it stores the information in its memory, so the information is available when you request it.

The function descriptions also explain that the GPIB-RS232/485/422 returns certain information to you. This means the GPIB-RS232/485/422 sends information to you over the GPIB.

The GPIB-RS232/485/422 continuously monitors the serial port for transmission errors. If it encounters an error in the serial data, the GPIB-RS232/485/422 records the error. You can program the GPIB-RS232/485/422 to ignore serial port errors using the spign function.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/statusinformationanderrorhandlingcharacteristicssmode.html language=enus -->
## TOPIC 00084: Status Information and Error Handling Characteristics

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/statusinformationanderrorhandlingcharacteristicssmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/statusinformationanderrorhandlingcharacteristicssmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Status Information and Error Handling Characteristics

The function descriptions in [S Mode Functions](smodefunctions.html) explain that the GPIB-RS232/485/422 records specific status and error information. This means it stores the information in its memory so the information is available when you request it.

The function descriptions also explain that the GPIB-RS232/485/422 returns certain information to you. This means the GPIB-RS232/485/422 sends information to you over the serial port.

The GPIB-RS232/485/422 continuously monitors the serial port for transmission errors. If it encounters an error in the serial data, the GPIB-RS232/485/422 records the error. You can program the GPIB-RS232/485/422 to ignore serial port errors using the spign function.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/takecontroltct.html language=enus -->
## TOPIC 00085: Take Control (TCT)

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/takecontroltct.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/takecontroltct.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Take Control (TCT)

In G Mode, the GPIB-RS232/485/422 can act only as a GPIB Talker or Listener. Do not pass control to the GPIB-RS232/485/422 in G Mode. If you do, the GPIB circuitry in the GPIB-RS232/485/422 accepts control and immediately asserts the ATN* signal, a system error condition you should avoid.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/technical_support_resources.html language=enus -->
## TOPIC 00086: Technical Support and Professional Services

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/technical_support_resources.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/technical_support_resources.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Technical Support and Professional Services

Visit the following sections of the National Instruments Web site at ni.com for technical support and professional services:

- Support—Online technical support resources at ni.com/support include the following:
  - Self-Help Resources —For answers and solutions, visit the award-winning National Instruments Web site for software drivers and updates, a searchable KnowledgeBase, product manuals, step-by-step troubleshooting wizards, thousands of example programs, tutorials, application notes, instrument drivers, and so on.
  - Free Technical Support —All registered users receive free Basic Service, which includes access to hundreds of Applications Engineers worldwide in the NI Developer Exchange at ni.com/exchange . National Instruments Applications Engineers make sure every question receives an answer.

 For information about other technical support options in your area, visit ni.com/services or contact your local office at ni.com/contact.
- Training and Certification—Visit ni.com/training for self-paced training, eLearning virtual classrooms, interactive CDs, and Certification program information. You also can register for instructor-led, hands-on courses at locations around the world.
- System Integration—If you have time constraints, limited in-house technical resources, or other project challenges, National Instruments Alliance Partner members can help. To learn more, call your local NI office or visit ni.com/alliance .

If you searched ni.com and could not find the answers you need, contact your [local office](branch_offices.html) or NI corporate headquarters. You also can visit the Worldwide Offices section of ni.com/niglobal to access the branch office Web sites, which provide up-to-date contact information, support phone numbers, email addresses, and current events.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/theparallelpoll.html language=enus -->
## TOPIC 00087: The Parallel Poll

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/theparallelpoll.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/theparallelpoll.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

The Parallel Poll

In S Mode, after parallel poll configuration is complete, the GPIB-RS232/485/422 conducts a parallel poll by calling rpp. In the previous example, where the device was remotely configured using a PPE message of hex 6A, if the ist bit of the device is set, rpp returns a value of hex 04. Here, the third least significant bit is set, corresponding to DIO line 3. (If any other devices responded positively on other lines, those corresponding bits would be set also.)

|  | Note You can configure more than one device to respond on the same data line, in which case the bits in the response byte are set by ORing all the responses on that line. In G Mode, the GPIB-RS232/485/422 sets its ist bit whenever it asserts SRQ*, and clears it whenever it unasserts SRQ*. Refer to the srqen function description for the conditions under which the GPIB-RS232/485/422 asserts SRQ*. If the Controller remotely configures the GPIB-RS232/485/422 using a PPE message of hex 6D (binary 0110 1101) and parallel polls it while it is asserting SRQ*, it responds by asserting DIO line 6. If the Controller remotely configures the GPIB-RS232/485/422 using a PPE message hex 65 (binary 0110 0101) and parallel polls it while it is asserting SRQ*, it responds by not asserting DIO line 6. |
| --- | --- |

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/timeoutterminationmode.html language=enus -->
## TOPIC 00088: Timeout Termination Mode

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/timeoutterminationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/timeoutterminationmode.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Timeout Termination Mode

Timeout termination mode should be used for applications in which bidirectional communication is required, and neither a <CR> nor <LF> character is used to signal the end of a command string to the GPIB device.

[IMAGE alt='image' src='timeoutterminationmode.gif']

In timeout termination mode, the GPIB-RS232/485/422 addresses the GPIB device to talk, and any characters read from the GPIB port are passed along immediately to the serial port. When the GPIB-RS232/485/422 receives a serial character, it immediately readdresses the GPIB device to listen and passes the character to it. It remains in this mode until its serial input buffer becomes empty and no serial characters are received for 300 ms. After this period of inactivity, the GPIB-RS232/485/422 assumes that because no more serial data is being sent, the device might need to send data back to the GPIB-RS232/485/422. It then readdresses the device to talk and passes any characters read from the GPIB port along to the serial port.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/tmo.html language=enus -->
## TOPIC 00089: tmo

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/tmo.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/tmo.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

tmo

#### Type

Initialization function

#### Syntax

**tm**o [timeio][,timesp]<CR>

#### Purpose

You can use tmo at the beginning of your program to change the time limits in effect on the GPIB-RS232/485/422. The time limits prevent the GPIB-RS232/485/422 from waiting indefinitely for critical events to occur.

#### Remarks

The arguments timeio and timesp are numeric strings. timeio specifies the amount of time in seconds the GPIB-RS232/485/422 waits for an I/O operation (rd, wrt, cmd) or the wait function to complete. timesp specifies the amount of time in seconds each device is given to respond to a serial poll. The power-on timeouts are 10 seconds for timeio and 0.1 second for timesp.

timeio and timesp can be any decimal number between .00001 and 3600, which corresponds to time limits between 10 µs and 1 hour. For example, 10,.1 specifies a time of 10 seconds for I/O operations and 1/10 of a second for serial poll responses. timeio and timesp can also be 0, which disables either timeout accordingly. Neither timeio nor timesp can contain commas.

|  | Note There are minor behavioral differences between the GPIB-RS232/485/422 and GPIB-232/485CT/CV-A regarding this function. For more information about this and other behavioral differences, refer to Differences Between the GPIB-232/485CT/CV-A and GPIB-RS232/485/422. |
| --- | --- |

The timeio time limit is in effect for the cmd, rd, and wrt functions. If the GPIB-RS232/485/422 cannot complete any of these functions within the period of time set by timeio, it aborts the function and records the EABO error. Bytes transferred before the timeout are not affected. The timeio time limit is also the maximum amount of time the wait function waits when you call it with the TIMO bit set in the wait mask.

The timesp time limit is in effect only for the rsp function. If a polled device fails to respond within the amount of time indicated by timesp, the GPIB-RS232/485/422 reports an error.

To change only the timeout value for serial polls, a comma must precede the serial poll timeout value.

If you call tmo without an argument, the GPIB-RS232/485/422 returns a numeric string representing the current timeout settings. It records the EARG error if you specify a time value outside the range of .00001 to 3600 seconds.

The assignment made by tmo remains in effect until you call tmo again, call onl, or turn off the GPIB-RS232/485/422.

#### See Also

[rsp](rsp.html).

#### Example 1

Set the timeout for I/O operations to 30 seconds.

```text
char  buffer [] = "tmo 30\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 2

Set the serial poll timeout for one second, while leaving the I/O timeout unchanged.

```text
char  buffer [] = "tmo ,1\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

#### Example 3

Retrieve the current timeout settings.

```text
char  buffer [] = "tmo\r";
char tmoBuffer[20];
viWrite(instr, buffer, strlen(buffer), &retCount);
viRead(instr,tmoBuffer,20,&retCount);
memset(tmoBuffer,0,20);
printf("timeout settings are %s\n", tmoBuffer);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/trademarks.html language=enus -->
## TOPIC 00090: Trademarks

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/trademarks.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/trademarks.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Trademarks

National Instruments, NI, ni.com, and LabVIEW are trademarks of National Instruments Corporation. Refer to the *Terms of Use* section on ni.com/legal for more information about National Instruments trademarks.

FireWire® is the registered trademark of Apple Computer, Inc.

Handle Graphics®, MATLAB®, Real-Time Workshop®, Simulink®, Stateflow®, and xPC TargetBox® are registered trademarks, and TargetBox™ and Target Language Compiler™ are trademarks of The MathWorks, Inc.

Tektronix® and Tek are registered trademarks of Tektronix, Inc.

Other product and company names mentioned herein are trademarks or trade names of their respective companies.

Members of the National Instruments Alliance Partner Program are business entities independent from National Instruments and have no agency, partnership, or joint-venture relationship with National Instruments.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/trg.html language=enus -->
## TOPIC 00091: trg

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/trg.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/trg.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

trg

Trigger Selected Device(s)*

#### Type

High-level bus management function

#### Syntax

**tr**g alist<CR>

#### Purpose

You can use trg to trigger the specified GPIB devices. The documentation for each GPIB device explains when you should trigger it and what effect the trigger has.

#### Remarks

The argument alist is a list of addresses separated by commas or spaces. Addresses are device addresses that specify the GPIB addresses you want to trigger.

If you call trg without an argument, the EARG error is posted.

If this is the first function you call that requires GPIB Controller capability, and you have not disabled System Controller capability with rsc, the GPIB-RS232/485/422 sends Interface Clear (IFC*) to make itself CIC. It also asserts Remote Enable.

If you passed control to some other GPIB device, control must be passed back to you or you must send IFC* to make yourself CIC before making this call. Otherwise, the ECIC error is posted.

#### Example

Trigger three devices.

```text
char  buffer [] = "trg 2+10,4,5+7\r";
viWrite(instr, buffer, strlen(buffer), &retCount);
```

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/troubleshooting.html language=enus -->
## TOPIC 00092: Troubleshooting

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/troubleshooting.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/troubleshooting.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Troubleshooting

If you cannot communicate with the GPIB-RS232/485/422 or your instrument, the following suggestions may help troubleshoot your problem.

- If the PWR LED is not lit, verify that the power cable is connected.
- If the RDY LED is steady red and the BUSY LED is steady yellow, the firmware image inside the GPIB-RS232/485/422 has been corrupted. Most likely, this happened as a result of disconnecting power during the previous firmware update. To recover from this condition, rerun the NI GPIB-Serial Converter Wizard and follow the instructions described in Using the NI GPIB-Serial Converter Wizard to Update the GPIB-RS232/485/422 Firmware .
- If the RDY LED is steady red, contact National Instruments for support.
- If the RDY LED is flashing green, the box is powered on in configuration mode. To configure your box, refer to Using the NI GPIB-Serial Converter Wizard .
- If the RDY LED is a steady green, you are booted into one of four converter box modes. Refer to the S Mode, G Mode, C Mode, and D Mode documentation for more information about each mode. If you do not know what mode your box is in, refer to Using the NI GPIB-Serial Converter Wizard .
- If you are using S or C Mode, ensure that you have configured all serial port settings on the GPIB-RS232/485/422 to match the host machine's settings.
- If you are using C mode, ensure that you have configured the correct Primary and Secondary GPIB address of the device you are talking to.
- If you are using G or D Mode, pay close attention to the Primary and Secondary address you have configured the GPIB-RS232/485/422 to use. Be sure your program is using the correct GPIB addresses.
- In all modes, if you are using hardware handshaking, verify that your cable and serial device support it. Refer to Hardware Handshaking and the flow control topic for the mode you are using for more details about serial flow control behavior.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/typesofgpibmessages.html language=enus -->
## TOPIC 00093: Types of GPIB Messages

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/typesofgpibmessages.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/typesofgpibmessages.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Types of GPIB Messages

The GPIB carries device-dependent messages and interface messages.

Device-dependent messages, often called data or data messages,
contain device-specific information such as programming instructions,
measurement results, machine status, and data files.

Interface messages manage the bus. They are usually called commands
or command messages. Interface messages perform such tasks as
initializing the bus, addressing and unaddressing devices, and setting
device modes for remote or local programming. [Multiline
Interface Messages](multilineinterfacemessages.html) lists the GPIB command messages.

<!--NI_TOPIC bundle=ni-gpib-serial-converter path=nigpibserialconverter/updatefailed2.html language=enus -->
## TOPIC 00094: Update Failed

- bundle_id: `ni-gpib-serial-converter`
- source_path: `nigpibserialconverter/updatefailed2.html`
- source_url: https://docs-be.ni.com/bundle/ni-gpib-serial-converter/raw/resource/enus/nigpibserialconverter/updatefailed2.html
- document_id: `ni-gpib-serial-converter`
- page_type: `leaf`
- content_type: ``

Update Failed

If an error occurred during the firmware update, the There was an error updating the GPIB-RS232/485/422 configuration message appears. Follow these steps to resolve the error and update the GPIB-RS232/485/422 firmware:

1. Verify that the GPIB-RS232/485/422 is connected to the computer interface specified in Selecting an Interface .
2. Verify that the GPIB-RS232/485/422 is in Configuration mode. The RDY LED is blinking green if the GPIB-RS232/485/422 is in Configuration mode. Refer to Connecting the GPIB-RS232/485/422 for instructions on enabling Configuration mode.
3. Verify that the cable connecting the computer to the GPIB-RS232/485/422 is connected correctly.
4. If connecting to the GPIB-RS232/485/422 over GPIB, verify that the GPIB interface being used to configure the GPIB-RS232/485/422 is set as System Controller, is Controller In Charge of the GPIB bus, and has a Primary Address (PAD) other than 13.
5. If connecting to the GPIB-RS232/485/422 over GPIB, remove all devices from the GPIB bus other than your computer interface card and the GPIB-RS232/485/422.

After resolving the error causing the failure, click **Retry** to re-attempt the firmware update. If successful, proceed to [Using the GPIB-RS232/485/422 After Running the NI GPIB-Serial Converter Wizard](usingthegpibrs232485422afterrunningthenigpibserialconverterwizard.html). If errors persist, recheck the troubleshooting steps above.
