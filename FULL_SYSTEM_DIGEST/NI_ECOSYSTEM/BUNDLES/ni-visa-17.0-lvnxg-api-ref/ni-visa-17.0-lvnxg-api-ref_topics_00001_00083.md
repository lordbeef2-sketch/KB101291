# NI DOCUMENT BUNDLE: ni-visa-17.0-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-visa-17.0-lvnxg-api-ref start=1 end=83 -->
<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=find-resource-get-configured-aliases.html language=enus -->
## TOPIC 00001: Get Configured Aliases

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `find-resource-get-configured-aliases.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/find-resource-get-configured-aliases.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of configured aliases. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error found resources An array of strings. Each string specifies one resource found by the

Get Configured Aliases

Returns a list of configured aliases.

[IMAGE alt='1378' src='Find_Resource_(Get_Aliases).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### found resources

An array of strings. Each string specifies one resource found by the function.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Find Resource Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=find-resource-multimode-function.html language=enus -->
## TOPIC 00002: Find Resource Multimode Function

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `find-resource-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/find-resource-multimode-function.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the system to locate the devices associated with a specified interface.

Find Resource Multimode Function

Queries the system to locate the devices associated with a specified interface.

Advanced

Accomplish advanced NI-VISA tasks.

Search Resources

Searches for resources that match a user-defined expression.

Get Configured Aliases

Returns a list of configured aliases.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=find-resource-search-resources.html language=enus -->
## TOPIC 00003: Search Resources

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `find-resource-search-resources.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/find-resource-search-resources.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches for resources that match a user-defined expression. expression The search criteria that matches with the devices available for a particular interface. The description string specified sets the criteria to search an interface--GPIB, GPIB-VXI, VXI, All VXI, Serial, or All--for existing device

Search Resources

Searches for resources that match a user-defined expression.

[IMAGE alt='1378' src='Find_Resource_(Search_Resources).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### expression

The search criteria that matches with the devices available for a particular interface.

The description string specified sets the criteria to search an interface--GPIB, GPIB-VXI, VXI, All VXI, Serial, or All--for existing devices.

Default value: 
 ?*

##### Regular Expressions and Sample Matches

The search criteria specified in expression has two parts: a regular expression over a resource string and an optional logical expression over attribute values.

The regular expression is matched against the resource strings of resources known to the VISA Resource Manager. If the resource string matches the regular expression, the attribute values of the resource are matched against the expression over attribute values. If the match is successful, the resource has met the search criteria and is added to the list of resources found. The following table includes valid regular expressions.

| Regular Expression | Sample Matches |
| --- | --- |
| GPIB?*INSTR | Matches GPIB0::2::INSTR, GPIB1::1::1::INSTR, and GPIB-VXI1::8::INSTR. |
| GPIB[0-9]*::?*INSTR | Matches GPIB0::2::INSTR and GPIB1::1::1::INSTR but not GPIB-VXI1::8::INSTR. |
| GPIB[^0]::?*INSTR | Matches GPIB1::1::1::INSTR but not GPIB0::2::INSTR or GPIB12::8::INSTR. |
| VXI?*INSTR | Matches VXI0::1::INSTR but not GPIB-VXI0::1::INSTR |
| GPIB-VXI?*INSTR | Matches GPIB-VXI0::1::INSTR but not VXI0::1::INSTR. |
| ?*VXI[0-9]*::?*INSTR | Matches VXI0::1::INSTR and GPIB-VXI0::1::INSTR. |
| ASRL[0-9]*::?*INSTR | Matches ASRL1::INSTR but not VXI0::5::INSTR. |
| ASRL1+::INSTR | Matches ASRL1::INSTR and ASRL11::INSTR but not ASRL2::INSTR. |
| {GPIB\|VXI)?*INSTR | Matches GPIB1::5::INSTR and VXI0::3::INSTR but not ASRL2::INSTR. |
| (GPIB0\|VXI0)::1::INSTR | Matches GPIB0::1::INSTR and VXI0::1:INSTR. |
| ?*INSTR | Matches all INSTR (device) resources. |
| ?*VXI[0-9]*::?*MEMACC | Matches VXI0::MEMACC and GPIB-VXI1::MEMACC. |
| VXI0::?* | Matches VXI0::1::INSTR, VXI0::2::INSTR, and VXI0::MEMACC. |
| ?* | Matches all resources. |
| visa://hostname/?* | Matches all resources on the specified remote system. You can set the hostname as either an IP address (dot-notation) or a network machine name. This remote system does not need to be a configured remote system. |
| /?* | Matches all the resources on the local machine. Does not query configured remote systems. |
| visa:/ASRL?*INSTR | Matches all ASRL resources on the local machine and returns them in URL format, such as visa:/ASRL1::INSTR. |

##### Special Characters and Operators

The following table includes valid special characters and operators.

| Special Characters and Operations | Meaning |
| --- | --- |
| ? | Matches any one character. |
| \\ | Makes the character that follows it an ordinary character instead of a special character. For example, when a question mark follows a backslash (\\?), it matches the ? character instead of any one character. |
| [list] | Matches any one character from the enclosed list. You can use a hyphen to match a range of characters. |
| [^list] | Matches any character not in the enclosed list. You can use a hyphen to match a range of characters. |
| * | Matches 0 or more occurrences of the preceding character or expression. |
| + | Matches 1 or more occurrences of the preceding character or expression. |
| Exp \| exp | Matches either the preceding or the following expression. The OR operator \| matches the entire expression that precedes or follows it and not just the character that precedes or follows it. For example, VXI\|GPIB means (VXI)\|(GPIB), not VX(I\|G)PIB. |
| (exp) | Groups characters or expressions. |

##### Optional Attribute Expressions

By using the optional attribute expression, you can construct expressions with the use of logical ANDs (&&), ORs (||), and NOTs (!). You can use equal (==) and unequal (!=) comparators to compare attributes of any data type, and other inequality comparators (>, 
 <, 
 >=, 
 <=) to compare attributes of numeric data type. Use only global attributes in the attribute expression. Local attributes are not allowed in the logical expression part of the expression parameter. The following table includes valid expression parameters.

| Expression Parameter | Meaning |
| --- | --- |
| GPIB[0-9]*::?*::?*::INSTR[VI_ATTR_GPIB_SECONDARY_ADDR > 0 && VI_ATTR_GPIB_SECONDARY_ADDR <10} | Find all GPIB devices that have secondary addresses from 1 to 9. |
| ASRL?*INSTR{VI_ATTR_ASRL_BAUD == 9600} | Find all serial ports configured at 9600 baud. |
| ?*VXI?INSTR{VI_ATTR_MANF_ID == 0xFF6 && !(VI_ATTR_VXI_LA ==0 \|\| VI_ATTR_SLOT <= 0)} | Find all VXI instrument resources having manufacturer ID FF6 and which are not logical address 0, slot 0, or external controllers. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### return aliases if available?

A Boolean value that determines whether the function returns found interfaces by canonical names (VISA canonical spec-defined resource format) or by user-defined aliases.

| True | The function returns found interfaces by user-defined aliases, if they are available. |
| --- | --- |
| False | The function returns found interfaces by the VISA canonical spec-defined resource format only. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### found resources

An array of strings. Each string specifies one resource found by the function.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Find Resource Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=flush-buffer.html language=enus -->
## TOPIC 00004: Flush Buffer

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `flush-buffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/flush-buffer.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Flushes the I/O buffer. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error mode The flush behavior. Write Transmit Buffer to Device 32 Fl

Flush Buffer

Flushes the I/O buffer.

[IMAGE alt='1378' src='Flush_Buffer_(Instr).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### mode

The flush behavior.

| Write Transmit Buffer to Device | 32 | Flushes and discards contents of the transmit buffer by writing all the buffered data to the device. |
| --- | --- | --- |
| Discard Receive Buffer | 64 | Flushes and discards contents of the receive buffer (does not perform any I/O to the device). |
| Discard Transmit Buffer | 128 | Flushes and discards contents of the transmit buffer (does not perform any I/O to the device). |
| Discard Receive and Transmit Buffers | 192 | Flushes and discards contents of the receive and transmit buffers, but does not perform any I/O to the device. |

Default value: Discard Receive Buffer

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=gpib-control-atn.html language=enus -->
## TOPIC 00005: GPIB Control ATN

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `gpib-control-atn.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/gpib-control-atn.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls the state of the GPIB ATN interface line and, optionally, the active controller state of the local interface. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error

GPIB Control ATN

Controls the state of the GPIB ATN interface line and, optionally, the active controller state of the local interface.

[IMAGE alt='1378' src='GPIB_Control_ATN_(GPIB_Interface).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### mode

The state of the ATN line and, optionally, the local active controller state.

| Deassert ATN | 0 | Deasserts the ATN line. The GPIB interface corresponding to the VISA session goes to standby. |
| --- | --- | --- |
| Assert ATN | 1 | Assert ATN line and take control synchronously without corrupting transferred data. If a data handshake is in progress, ATN is not asserted until the handshake is complete. |
| Deassert ATN with Handshake | 2 | Deassert ATN line and enter shadow handshake mode. The local device participates in data handshakes as an Acceptor without actually reading the data. The GPIB interface corresponding to the VISA session goes to standby. |
| Assert ATN Immediately | 3 | Assert ATN line and take control asynchronously and immediately, without regard for any data transfer currently in progress. Use this mode only under error conditions. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Modifying the ATN Automatically

Most applications do not require this function. You can use the GPIB Command function to modify the ATN automatically and the GPIB Pass Control function to modify the ATN and controller-in-charge (CIC) state automatically.

Note

Parent topic:

GPIB

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=gpib-pass-control.html language=enus -->
## TOPIC 00006: GPIB Pass Control

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `gpib-pass-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/gpib-pass-control.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Tells the GPIB device at the specified address to become controller-in-charge (CIC). This function passes CIC status to the device specified by primary address and secondary address and deasserts the ATN line. This function assumes that the targeted device has controller capability. GPIB Pass Contro

GPIB Pass Control

Tells the GPIB device at the specified address to become controller-in-charge (CIC).

This function passes CIC status to the device specified by primary address and secondary address and deasserts the ATN line. This function assumes that the targeted device has controller capability.

Note

[IMAGE alt='1378' src='GPIB_Pass_Control_(GPIB_Interface).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### primary address

The primary address of the GPIB device to which you want to pass control

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### secondary address

The secondary address of the targeted GPIB device.

Default value: 65535, none

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

GPIB

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=gpib-send-command.html language=enus -->
## TOPIC 00007: GPIB Send Command

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `gpib-send-command.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/gpib-send-command.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes GPIB command bytes on the bus. This function does not accept VISA sessions of class Instr. The VISA session must be of class GPIB BoardInterface. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standa

GPIB Send Command

Writes GPIB command bytes on the bus.

Note

[IMAGE alt='1378' src='GPIB_Send_Command_(GPIB_Interface).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### command

Bytes to be written on the bus.

Command bytes should be valid IEEE 488-defined Multiline Interface Messages.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### return count

The number of bytes actually transferred.

Parent topic:

GPIB

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=gpib-send-interface-clear.html language=enus -->
## TOPIC 00008: GPIB Send Interface Clear

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `gpib-send-interface-clear.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/gpib-send-interface-clear.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pulses the interface clear line (IFC) for at least 100 microseconds. This function asserts the IFC line and becomes the controller-in-charge (CIC). The local device must be the system controller. This function does not accept VISA sessions of class Instr. The VISA session must be of class GPIB Board

GPIB Send Interface Clear

Pulses the interface clear line (IFC) for at least 100 microseconds.

This function asserts the IFC line and becomes the controller-in-charge (CIC). The local device must be the system controller.

Note

[IMAGE alt='1378' src='GPIB_Send_Interface_Clear_(GPIB_Interface).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

GPIB

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=in-multimode-function.html language=enus -->
## TOPIC 00009: In Multimode Function

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `in-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/in-multimode-function.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data.

In Multimode Function

Reads data.

Register Access

Use the Register Access VISA functions to program in an address space at a high level.

U8

Reads 8-bit data from a specific address space and offset.

U16

Reads 16-bit data from a specified address space and offset.

U32

Reads 32-bit data from a specific address space and offset.

U64

Reads 64-bit data from a specific address space and offset.

Parent topic:

Register Access

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=in-u16.html language=enus -->
## TOPIC 00010: U16

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `in-u16.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/in-u16.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads 16-bit data from a specified address space and offset. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error offset The offset, in byt

U16

Reads 16-bit data from a specified address space and offset.

[IMAGE alt='1378' src='In_(Instr,_U16).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, of the location to read from.

This function accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how offset specifies the offset.

- INSTR Specific --The offset for an INSTR Resource is the offset address relative to the device's allocated address base for the corresponding address space that was specified. For example, if address space specifies VXI/VME A16, offset specifies the offset from the logical address base address of the VXI device specified. If address space specifies VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.
- MEMACC Specific --For a MEMACC Resource, offset specifies an absolute address.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### address space

The address space.

The following table lists the valid entries for specifying address space:

| VXI/VME A16 | 1 | The A16 address space of a VXI or VME device. |
| --- | --- | --- |
| VXI/VME A24 | 2 | The A24 address space of a VXI or VME device. |
| VXI/VME A32 | 3 | The A32 address space of a VXI or VME device. |
| VXI/VME A64 | 4 | The A64 address space of a VXI or VME device. |
| PXI Memory Allocations | 9 | A physical, locally allocated address space. |
| PXI Configuration | 10 | The PXI configuration address space. |
| PXI BAR0 - PXI BAR5 | 11-16 | PXI memory or I/O address space 0 through 5. |

Default value: VXI/VME A16

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### next offset

The next byte offset after the data is read from the given address space.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### value

The read data.

Parent topic:

In Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=in-u64.html language=enus -->
## TOPIC 00011: U64

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `in-u64.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/in-u64.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads 64-bit data from a specific address space and offset. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error offset The offset, in byte

U64

Reads 64-bit data from a specific address space and offset.

[IMAGE alt='1378' src='In_(Instr,_U64).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, of the location to read from.

This function accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how offset specifies the offset.

- INSTR Specific --The offset for an INSTR Resource is the offset address relative to the device's allocated address base for the corresponding address space that was specified. For example, if address space specifies VXI/VME A16, offset specifies the offset from the logical address base address of the VXI device specified. If address space specifies VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.
- MEMACC Specific --For a MEMACC Resource, offset specifies an absolute address.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### address space

The address space.

The following table lists the valid entries for specifying address space:

| VXI/VME A16 | 1 | The A16 address space of a VXI or VME device. |
| --- | --- | --- |
| VXI/VME A24 | 2 | The A24 address space of a VXI or VME device. |
| VXI/VME A32 | 3 | The A32 address space of a VXI or VME device. |
| VXI/VME A64 | 4 | The A64 address space of a VXI or VME device. |
| PXI Memory Allocations | 9 | A physical, locally allocated address space. |
| PXI Configuration | 10 | The PXI configuration address space. |
| PXI BAR0 - PXI BAR5 | 11-16 | PXI memory or I/O address space 0 through 5. |

Default value: VXI/VME A16

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### next offset

The next byte offset after the data is read from the given address space.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### value

The read data.

Parent topic:

In Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=in-u8.html language=enus -->
## TOPIC 00012: U8

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `in-u8.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/in-u8.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads 8-bit data from a specific address space and offset. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error offset The offset, in bytes

U8

Reads 8-bit data from a specific address space and offset.

[IMAGE alt='1378' src='In_(Instr,_U8).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, of the location to read from.

This function accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how offset specifies the offset.

- INSTR Specific --The offset for an INSTR Resource is the offset address relative to the device's allocated address base for the corresponding address space that was specified. For example, if address space specifies VXI/VME A16, offset specifies the offset from the logical address base address of the VXI device specified. If address space specifies VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.
- MEMACC Specific --For a MEMACC Resource, offset specifies an absolute address.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### address space

The address space.

The following table lists the valid entries for specifying address space:

| VXI/VME A16 | 1 | The A16 address space of a VXI or VME device. |
| --- | --- | --- |
| VXI/VME A24 | 2 | The A24 address space of a VXI or VME device. |
| VXI/VME A32 | 3 | The A32 address space of a VXI or VME device. |
| VXI/VME A64 | 4 | The A64 address space of a VXI or VME device. |
| PXI Memory Allocations | 9 | A physical, locally allocated address space. |
| PXI Configuration | 10 | The PXI configuration address space. |
| PXI BAR0 - PXI BAR5 | 11-16 | PXI memory or I/O address space 0 through 5. |

Default value: VXI/VME A16

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### next offset

The next byte offset after the data is read from the given address space.

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### value

The read data.

Parent topic:

In Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=lock-exclusive.html language=enus -->
## TOPIC 00013: Exclusive

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `lock-exclusive.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/lock-exclusive.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obtains an exclusive lock that guarantees sole access to a device or resource. If a session has an exclusive lock, other sessions cannot modify global attributes or invoke operations but can still get attributes and set local attributes. lock timeout Maximum time period, in milliseconds, that the fu

Exclusive

Obtains an exclusive lock that guarantees sole access to a device or resource.

If a session has an exclusive lock, other sessions cannot modify global attributes or invoke operations but can still get attributes and set local attributes.

[IMAGE alt='1378' src='Lock_(Instr,_Exclusive).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### lock timeout

Maximum time period, in milliseconds, that the function waits for access to lock.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Lock Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=lock-multimode-function.html language=enus -->
## TOPIC 00014: Lock Multimode Function

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `lock-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/lock-multimode-function.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Attempts to establish access to a device or interface.

Lock Multimode Function

Attempts to establish access to a device or interface.

Advanced

Accomplish advanced NI-VISA tasks.

Exclusive

Obtains an exclusive lock that guarantees sole access to a device or resource.

Shared

Obtains a shared lock that allows shared access to a device or resource.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=lock-shared.html language=enus -->
## TOPIC 00015: Shared

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `lock-shared.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/lock-shared.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obtains a shared lock that allows shared access to a device or resource. If the session has a shared lock, other sessions that have shared locks also can modify global attributes and invoke operations. lock timeout Maximum time period, in milliseconds, that the function waits for access to lock. ses

Shared

Obtains a shared lock that allows shared access to a device or resource.

If the session has a shared lock, other sessions that have shared locks also can modify global attributes and invoke operations.

[IMAGE alt='1378' src='Lock_(Instr,_Shared).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### lock timeout

Maximum time period, in milliseconds, that the function waits for access to lock.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### requested key

Unique access key for the shared lock.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### access key

A unique access key for the lock.

After the function runs, you can share the lock with other sessions of the same resource by wiring this parameter as the requested key to subsequent Lock (Shared) operations.

Parent topic:

Lock Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=map-address.html language=enus -->
## TOPIC 00016: Map Address

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `map-address.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/map-address.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maps a memory space. The memory space that this function maps depends on the type of interface specified by session in and address space. After the window is mapped, VISA keeps track of the window that is mapped. VISA can map only one window for each VISA session. address space The address space. Th

Map Address

Maps a memory space.

The memory space that this function maps depends on the type of interface specified by session in and address space. After the window is mapped, VISA keeps track of the window that is mapped. VISA can map only one window for each VISA session.

[IMAGE alt='1378' src='Map_Address_(Instr).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### address space

The address space.

The following table lists the valid entries for specifying address space:

| VXI/VME A16 | 1 | The A16 address space of a VXI or VME device. |
| --- | --- | --- |
| VXI/VME A24 | 2 | The A24 address space of a VXI or VME device. |
| VXI/VME A32 | 3 | The A32 address space of a VXI or VME device. |
| VXI/VME A64 | 4 | The A64 address space of a VXI or VME device. |
| PXI Memory Allocations | 9 | A physical, locally allocated address space. |
| PXI Configuration | 10 | The PXI configuration address space. |
| PXI BAR0 - PXI BAR5 | 11-16 | PXI memory or I/O address space 0 through 5. |

Default value: VXI/VME A16

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### map base

The offset, in bytes, of the memory to be mapped.

The type of resource determines how map base specifies the offset.

Default value: 0

##### INSTR Specific Details

The map base specified in Map Address for an INSTR resource is the offset address relative to the device's allocated address base for the corresponding address space you specified. For example, if address space specifies VXI/VME A16, map base specifies the offset from the logical address base address of the specified device. If address space specifies VXI/VME A24, VXI/VME A32, or VXI/VME A64, map base specifies the offset from the base address of the VXI device's memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64 space.

##### MEMACC Specific Details

For a MEMACC resource, map base specifies an absolute address.

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### map size

The amount of memory to map.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=memory-allocation.html language=enus -->
## TOPIC 00017: Memory Allocation

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `memory-allocation.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/memory-allocation.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Allocates device memory of a specific size and returns the location of the memory. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error siz

Memory Allocation

Allocates device memory of a specific size and returns the location of the memory.

[IMAGE alt='1378' src='Memory_Allocation_(Instr).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### size

Size of the allocation.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### require 32-bit region

A Boolean value that forces the whole memory chunk to be in the 4 GB boundary and the 32-bit address range.

| True | Restricts memory allocation to the 32-bit address range. |
| --- | --- |
| False | Allows memory allocation to be done anywhere in the entire 64-bit address range. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### offset

The location of the allocated memory.

#### Locating and Allocating Memory

You can allocate the memory on either the device itself or on the computer's system memory. If the device specified with session in is located on the local interface card, the memory can be allocated either on the device itself or on the computer's system memory. The memory region referenced by offset can be accessed with Move In or Move Out, or it can be mapped using Map Address.

Parent topic:

Register Access

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=move-in-multimode-function.html language=enus -->
## TOPIC 00018: Move In Multimode Function

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `move-in-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/move-in-multimode-function.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies one or more units of data from device memory to local memory.

Move In Multimode Function

Copies one or more units of data from device memory to local memory.

Register Access

Use the Register Access VISA functions to program in an address space at a high level.

U8

Copies an array of 8-bit data from device memory to local memory.

U16

Copies an array of 16-bit data from device memory to local memory.

U32

Copies an array of 32-bit data from device memory to local memory.

U64

Copies an array of 64-bit data from device memory to local memory.

Parent topic:

Register Access

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=move-in-u16.html language=enus -->
## TOPIC 00019: U16

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `move-in-u16.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/move-in-u16.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies an array of 16-bit data from device memory to local memory. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error offset The offset,

U16

Copies an array of 16-bit data from device memory to local memory.

[IMAGE alt='1378' src='Move_In_(Instr,_U16).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, of the location to read from.

This function accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how offset specifies the offset.

- INSTR Specific --The offset for an INSTR Resource is the offset address relative to the device's allocated address base for the corresponding address space that was specified. For example, if address space specifies VXI/VME A16, offset specifies the offset from the logical address base address of the VXI device specified. If address space specifies VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.
- MEMACC Specific --For a MEMACC Resource, offset specifies an absolute address.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### count

The number of data items to move.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### address space

The address space.

The following table lists the valid entries for specifying address space:

| VXI/VME A16 | 1 | The A16 address space of a VXI or VME device. |
| --- | --- | --- |
| VXI/VME A24 | 2 | The A24 address space of a VXI or VME device. |
| VXI/VME A32 | 3 | The A32 address space of a VXI or VME device. |
| VXI/VME A64 | 4 | The A64 address space of a VXI or VME device. |
| PXI Memory Allocations | 9 | A physical, locally allocated address space. |
| PXI Configuration | 10 | The PXI configuration address space. |
| PXI BAR0 - PXI BAR5 | 11-16 | PXI memory or I/O address space 0 through 5. |

Default value: VXI/VME A16

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1du16.png']

##### data

The data read.

Parent topic:

Move In Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=move-in-u32.html language=enus -->
## TOPIC 00020: U32

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `move-in-u32.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/move-in-u32.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies an array of 32-bit data from device memory to local memory. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error offset The offset,

U32

Copies an array of 32-bit data from device memory to local memory.

[IMAGE alt='1378' src='Move_In_(Instr,_U32).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, of the location to read from.

This function accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how offset specifies the offset.

- INSTR Specific --The offset for an INSTR Resource is the offset address relative to the device's allocated address base for the corresponding address space that was specified. For example, if address space specifies VXI/VME A16, offset specifies the offset from the logical address base address of the VXI device specified. If address space specifies VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.
- MEMACC Specific --For a MEMACC Resource, offset specifies an absolute address.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### count

The number of data items to move.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### address space

The address space.

The following table lists the valid entries for specifying address space:

| VXI/VME A16 | 1 | The A16 address space of a VXI or VME device. |
| --- | --- | --- |
| VXI/VME A24 | 2 | The A24 address space of a VXI or VME device. |
| VXI/VME A32 | 3 | The A32 address space of a VXI or VME device. |
| VXI/VME A64 | 4 | The A64 address space of a VXI or VME device. |
| PXI Memory Allocations | 9 | A physical, locally allocated address space. |
| PXI Configuration | 10 | The PXI configuration address space. |
| PXI BAR0 - PXI BAR5 | 11-16 | PXI memory or I/O address space 0 through 5. |

Default value: VXI/VME A16

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1du32.png']

##### data

The data read.

Parent topic:

Move In Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=move-in-u8.html language=enus -->
## TOPIC 00021: U8

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `move-in-u8.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/move-in-u8.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies an array of 8-bit data from device memory to local memory. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error offset The offset, i

U8

Copies an array of 8-bit data from device memory to local memory.

[IMAGE alt='1378' src='Move_In_(Instr,_U8).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, of the location to read from.

This function accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how offset specifies the offset.

- INSTR Specific --The offset for an INSTR Resource is the offset address relative to the device's allocated address base for the corresponding address space that was specified. For example, if address space specifies VXI/VME A16, offset specifies the offset from the logical address base address of the VXI device specified. If address space specifies VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.
- MEMACC Specific --For a MEMACC Resource, offset specifies an absolute address.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### count

The number of data items to move.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### address space

The address space.

The following table lists the valid entries for specifying address space:

| VXI/VME A16 | 1 | The A16 address space of a VXI or VME device. |
| --- | --- | --- |
| VXI/VME A24 | 2 | The A24 address space of a VXI or VME device. |
| VXI/VME A32 | 3 | The A32 address space of a VXI or VME device. |
| VXI/VME A64 | 4 | The A64 address space of a VXI or VME device. |
| PXI Memory Allocations | 9 | A physical, locally allocated address space. |
| PXI Configuration | 10 | The PXI configuration address space. |
| PXI BAR0 - PXI BAR5 | 11-16 | PXI memory or I/O address space 0 through 5. |

Default value: VXI/VME A16

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### data

The data read.

Parent topic:

Move In Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=move-out-u16.html language=enus -->
## TOPIC 00022: U16

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `move-out-u16.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/move-out-u16.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies an array of 16-bit data from local memory to the specified address space and offset. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No

U16

Copies an array of 16-bit data from local memory to the specified address space and offset.

[IMAGE alt='1378' src='Move_Out_(Instr,_U16).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, of the location to read from.

This function accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how offset specifies the offset.

- INSTR Specific --The offset for an INSTR Resource is the offset address relative to the device's allocated address base for the corresponding address space that was specified. For example, if address space specifies VXI/VME A16, offset specifies the offset from the logical address base address of the VXI device specified. If address space specifies VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.
- MEMACC Specific --For a MEMACC Resource, offset specifies an absolute address.

[IMAGE alt='datatype_icon' src='/assets/img/c1du16.png']

##### data

The data to write.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### address space

The address space.

The following table lists the valid entries for specifying address space:

| VXI/VME A16 | 1 | The A16 address space of a VXI or VME device. |
| --- | --- | --- |
| VXI/VME A24 | 2 | The A24 address space of a VXI or VME device. |
| VXI/VME A32 | 3 | The A32 address space of a VXI or VME device. |
| VXI/VME A64 | 4 | The A64 address space of a VXI or VME device. |
| PXI Memory Allocations | 9 | A physical, locally allocated address space. |
| PXI Configuration | 10 | The PXI configuration address space. |
| PXI BAR0 - PXI BAR5 | 11-16 | PXI memory or I/O address space 0 through 5. |

Default value: VXI/VME A16

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Move Out Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=move-out-u32.html language=enus -->
## TOPIC 00023: U32

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `move-out-u32.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/move-out-u32.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies an array of 32-bit data from local memory to the specified address space and offset. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No

U32

Copies an array of 32-bit data from local memory to the specified address space and offset.

[IMAGE alt='1378' src='Move_Out_(Instr,_U32).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, of the location to read from.

This function accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how offset specifies the offset.

- INSTR Specific --The offset for an INSTR Resource is the offset address relative to the device's allocated address base for the corresponding address space that was specified. For example, if address space specifies VXI/VME A16, offset specifies the offset from the logical address base address of the VXI device specified. If address space specifies VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.
- MEMACC Specific --For a MEMACC Resource, offset specifies an absolute address.

[IMAGE alt='datatype_icon' src='/assets/img/c1du32.png']

##### data

The data to write.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### address space

The address space.

The following table lists the valid entries for specifying address space:

| VXI/VME A16 | 1 | The A16 address space of a VXI or VME device. |
| --- | --- | --- |
| VXI/VME A24 | 2 | The A24 address space of a VXI or VME device. |
| VXI/VME A32 | 3 | The A32 address space of a VXI or VME device. |
| VXI/VME A64 | 4 | The A64 address space of a VXI or VME device. |
| PXI Memory Allocations | 9 | A physical, locally allocated address space. |
| PXI Configuration | 10 | The PXI configuration address space. |
| PXI BAR0 - PXI BAR5 | 11-16 | PXI memory or I/O address space 0 through 5. |

Default value: VXI/VME A16

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Move Out Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=move-out-u64.html language=enus -->
## TOPIC 00024: U64

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `move-out-u64.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/move-out-u64.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies an array of 64-bit data from local memory to the specified address space and offset. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No

U64

Copies an array of 64-bit data from local memory to the specified address space and offset.

[IMAGE alt='1378' src='Move_Out_(Instr,_U64).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, of the location to read from.

This function accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how offset specifies the offset.

- INSTR Specific --The offset for an INSTR Resource is the offset address relative to the device's allocated address base for the corresponding address space that was specified. For example, if address space specifies VXI/VME A16, offset specifies the offset from the logical address base address of the VXI device specified. If address space specifies VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.
- MEMACC Specific --For a MEMACC Resource, offset specifies an absolute address.

[IMAGE alt='datatype_icon' src='/assets/img/c1du64.png']

##### data

The data to write.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### address space

The address space.

The following table lists the valid entries for specifying address space:

| VXI/VME A16 | 1 | The A16 address space of a VXI or VME device. |
| --- | --- | --- |
| VXI/VME A24 | 2 | The A24 address space of a VXI or VME device. |
| VXI/VME A32 | 3 | The A32 address space of a VXI or VME device. |
| VXI/VME A64 | 4 | The A64 address space of a VXI or VME device. |
| PXI Memory Allocations | 9 | A physical, locally allocated address space. |
| PXI Configuration | 10 | The PXI configuration address space. |
| PXI BAR0 - PXI BAR5 | 11-16 | PXI memory or I/O address space 0 through 5. |

Default value: VXI/VME A16

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Move Out Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=move-out-u8.html language=enus -->
## TOPIC 00025: U8

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `move-out-u8.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/move-out-u8.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies an array of 8-bit data from local memory to the specified address space and offset. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No e

U8

Copies an array of 8-bit data from local memory to the specified address space and offset.

[IMAGE alt='1378' src='Move_Out_(Instr,_U8).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, of the location to read from.

This function accepts a 32- or 64-bit unsigned integer as input. The type of resource determines how offset specifies the offset.

- INSTR Specific --The offset for an INSTR Resource is the offset address relative to the device's allocated address base for the corresponding address space that was specified. For example, if address space specifies VXI/VME A16, offset specifies the offset from the logical address base address of the VXI device specified. If address space specifies VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's memory space allocated by the VXI Resource Manager within VXI/VME A24, A32, or A64.
- MEMACC Specific --For a MEMACC Resource, offset specifies an absolute address.

[IMAGE alt='datatype_icon' src='/assets/img/c1du8.png']

##### data

The data to write.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### address space

The address space.

The following table lists the valid entries for specifying address space:

| VXI/VME A16 | 1 | The A16 address space of a VXI or VME device. |
| --- | --- | --- |
| VXI/VME A24 | 2 | The A24 address space of a VXI or VME device. |
| VXI/VME A32 | 3 | The A32 address space of a VXI or VME device. |
| VXI/VME A64 | 4 | The A64 address space of a VXI or VME device. |
| PXI Memory Allocations | 9 | A physical, locally allocated address space. |
| PXI Configuration | 10 | The PXI configuration address space. |
| PXI BAR0 - PXI BAR5 | 11-16 | PXI memory or I/O address space 0 through 5. |

Default value: VXI/VME A16

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Move Out Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=out-multimode-function.html language=enus -->
## TOPIC 00026: Out Multimode Function

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `out-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/out-multimode-function.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data.

Out Multimode Function

Writes data.

Register Access

Use the Register Access VISA functions to program in an address space at a high level.

U8

Writes 8-bit data to the specified address space and offset.

U16

Writes 16-bit data to the specified address space and offset.

U32

Writes 32-bit data to the specified address space and offset.

U64

Writes 64-bit data to a specified address space and offset.

Parent topic:

Register Access

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=out-u64.html language=enus -->
## TOPIC 00027: U64

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `out-u64.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/out-u64.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes 64-bit data to a specified address space and offset. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error offset The offset, in byte

U64

Writes 64-bit data to a specified address space and offset.

[IMAGE alt='1378' src='Out_(Instr,_U64).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, of the location to write to.

The type of resource you wire to session in determines how this parameter specifies the offset.

Default value: 0

##### INSTR Specific Behavior

The offset specified in Out operations for an INSTR resource is the offset address relative to the device's allocated address base for the corresponding address space that was specified. For example, if address space specifies VXI/VME A16, offset specifies the offset from the logical address base address of the specified VXI device. If address space specifies VXI/VME A24, A32, or A64, offset specifies the offset from the base address of the VXI device's memory space allocated by the VXI Resource Manager within VXI/VME A24, A32 or A64 space.

##### MEMACC Specific Behavior

For a MEMACC resource, offset specifies an absolute address.

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### value

The data to write to the address space.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### address space

The address space.

The following table lists the valid entries for specifying address space:

| VXI/VME A16 | 1 | The A16 address space of a VXI or VME device. |
| --- | --- | --- |
| VXI/VME A24 | 2 | The A24 address space of a VXI or VME device. |
| VXI/VME A32 | 3 | The A32 address space of a VXI or VME device. |
| VXI/VME A64 | 4 | The A64 address space of a VXI or VME device. |
| PXI Memory Allocations | 9 | A physical, locally allocated address space. |
| PXI Configuration | 10 | The PXI configuration address space. |
| PXI BAR0 - PXI BAR5 | 11-16 | PXI memory or I/O address space 0 through 5. |

Default value: VXI/VME A16

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### next offset

The next byte offset after the data is written to the given address space.

Parent topic:

Out Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=peek-u8.html language=enus -->
## TOPIC 00028: U8

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `peek-u8.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/peek-u8.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads an 8-bit value from a location in a memory window mapped by Map Address. You must use Map Address to map the address before you call this function. The address must be a valid memory address in the current process. session in The resource to be used. error in Error conditions that occur before

U8

Reads an 8-bit value from a location in a memory window mapped by Map Address.

You must use Map Address to map the address before you call this function. The address must be a valid memory address in the current process.

[IMAGE alt='1378' src='Peek_(Instr,_U8).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, from the beginning of the window mapped using Map Address.

This input accepts 32-bit and 64-bit unsigned integers.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### next offset

The next byte offset after the data is read from the given offset in the mapped memory window.

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### value

The read data.

Parent topic:

Peek Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=poke-multimode-function.html language=enus -->
## TOPIC 00029: Poke Multimode Function

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `poke-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/poke-multimode-function.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a value to a location in a memory window mapped by Map Address.

Poke Multimode Function

Writes a value to a location in a memory window mapped by Map Address.

Low Level

VISA functions for low level register access.

U8

Writes an 8-bit value to a location in a memory window mapped by Map Address.

U16

Writes a 16-bit value to a location in a memory window mapped by Map Address.

U32

Writes a 32-bit value to a location in a memory window mapped by Map Address.

U64

Writes a 64-bit value to a location in a memory window mapped by Map Address.

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=poke-u16.html language=enus -->
## TOPIC 00030: U16

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `poke-u16.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/poke-u16.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a 16-bit value to a location in a memory window mapped by Map Address. You must use Map Address to map the address before you call this function. The address must be a valid memory address in the current process. session in The resource to be used. error in Error conditions that occur before

U16

Writes a 16-bit value to a location in a memory window mapped by Map Address.

You must use Map Address to map the address before you call this function. The address must be a valid memory address in the current process.

[IMAGE alt='1378' src='Poke_(Instr,_U16).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, from the beginning of the window mapped using Map Address.

This input accepts 32-bit and 64-bit unsigned integers.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### value

The data to write to the memory window.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### next offset

The next byte offset after the data is written to the given offset in the mapped memory window.

Parent topic:

Poke Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=poke-u32.html language=enus -->
## TOPIC 00031: U32

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `poke-u32.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/poke-u32.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a 32-bit value to a location in a memory window mapped by Map Address. You must use Map Address to map the address before you call this function. The address must be a valid memory address in the current process. session in The resource to be used. error in Error conditions that occur before

U32

Writes a 32-bit value to a location in a memory window mapped by Map Address.

You must use Map Address to map the address before you call this function. The address must be a valid memory address in the current process.

[IMAGE alt='1378' src='Poke_(Instr,_U32).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, from the beginning of the window mapped using Map Address.

This input accepts 32-bit and 64-bit unsigned integers.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### value

The value to write to the memory window.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### next offset

The next byte offset after the data is written to the given offset in the mapped memory window.

Parent topic:

Poke Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=poke-u64.html language=enus -->
## TOPIC 00032: U64

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `poke-u64.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/poke-u64.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a 64-bit value to a location in a memory window mapped by Map Address. You must use Map Address to map the address before you call this function. The address must be a valid memory address in the current process. session in The resource to be used. error in Error conditions that occur before

U64

Writes a 64-bit value to a location in a memory window mapped by Map Address.

You must use Map Address to map the address before you call this function. The address must be a valid memory address in the current process.

[IMAGE alt='1378' src='Poke_(Instr,_U64).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, from the beginning of the window mapped using Map Address.

This input accepts 32-bit and 64-bit unsigned integers.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### value

The data to write to the memory window.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### next offset

The next byte offset after the data is written to the given offset in the mapped memory window.

Parent topic:

Poke Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=poke-u8.html language=enus -->
## TOPIC 00033: U8

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `poke-u8.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/poke-u8.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an 8-bit value to a location in a memory window mapped by Map Address. You must use Map Address to map the address before you call this function. The address must be a valid memory address in the current process. session in The resource to be used. error in Error conditions that occur before

U8

Writes an 8-bit value to a location in a memory window mapped by Map Address.

You must use Map Address to map the address before you call this function. The address must be a valid memory address in the current process.

[IMAGE alt='1378' src='Poke_(Instr,_U8).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### offset

The offset, in bytes, from the beginning of the window mapped using Map Address.

This input accepts 32-bit and 64-bit unsigned integers.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### value

The data to write to the memory window.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### next offset

The next byte offset after the data is written to the given offset in the mapped memory window.

Parent topic:

Poke Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=pxi-map-trigger.html language=enus -->
## TOPIC 00034: PXI Map Trigger

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `pxi-map-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/pxi-map-trigger.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes a trigger source line to a trigger destination line. This node creates a connection between trigger lines across bus segments. destination bus The bus segment of the destination trigger line. source bus The bus segment of the source trigger line. session in The resource to be used. error in E

PXI Map Trigger

Routes a trigger source line to a trigger destination line.

This node creates a connection between trigger lines across bus segments.

[IMAGE alt='1378' src='PXI_Map_Trigger_(PXI_Backplane).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### destination bus

The bus segment of the destination trigger line.

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### source bus

The bus segment of the source trigger line.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### source line

The source trigger line. This input accepts the following values:

| TTL0 | 0 | The TTL0 trigger line. |
| --- | --- | --- |
| TTL1 | 1 | The TTL1 trigger line. |
| TTL2 | 2 | The TTL2 trigger line. |
| TTL3 | 3 | The TTL3 trigger line. |
| TTL4 | 4 | The TTL4 trigger line. |
| TTL5 | 5 | The TTL5 trigger line. |
| TTL6 | 6 | The TTL6 trigger line. |
| TTL7 | 7 | The TTL7 trigger line. |

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### destination line

The destination trigger line.

This input accepts the following values:

| TTL0 | 0 | The TTL0 trigger line. |
| --- | --- | --- |
| TTL1 | 1 | The TTL1 trigger line. |
| TTL2 | 2 | The TTL2 trigger line. |
| TTL3 | 3 | The TTL3 trigger line. |
| TTL4 | 4 | The TTL4 trigger line. |
| TTL5 | 5 | The TTL5 trigger line. |
| TTL6 | 6 | The TTL6 trigger line. |
| TTL7 | 7 | The TTL7 trigger line. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Asserting Multiple Trigger Lines

If you call this function multiple times on the same backplane resource with the same source line and different destination lines, all of the specified destination lines are asserted when the source line is asserted. Calling this function multiple times on the same backplane resource with different source lines and the same destination line is not supported.

Parent topic:

PXI

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=pxi-reserve-trigger-multimode-function.html language=enus -->
## TOPIC 00035: PXI Reserve Trigger Multimode Function

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `pxi-reserve-trigger-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/pxi-reserve-trigger-multimode-function.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reserves one or more trigger lines for use in external triggering.Use this function to coordinate access to a trigger line to prevent multiple devices from driving trigger signals through a line at the same time.

PXI Reserve Trigger Multimode Function

Reserves one or more trigger lines for use in external triggering.Use this function to coordinate access to a trigger line to prevent multiple devices from driving trigger signals through a line at the same time.

PXI

VISA functions for PXI devices.

Single

Reserves a single trigger line.

Multiple

Reserves multiple trigger lines.

Parent topic:

PXI

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=pxi-reserve-trigger-multiple.html language=enus -->
## TOPIC 00036: Multiple

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `pxi-reserve-trigger-multiple.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/pxi-reserve-trigger-multiple.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reserves multiple trigger lines. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error lines The trigger lines. TTL1 1 The TTL1 trigger line

Multiple

Reserves multiple trigger lines.

[IMAGE alt='1378' src='PXI_Reserve_Triggers_(PXI_Backplane).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1du16.png']

##### lines

The trigger lines.

| TTL1 | 1 | The TTL1 trigger line. |
| --- | --- | --- |
| TTL2 | 2 | The TTL2 trigger line. |
| TTL3 | 3 | The TTL3 trigger line. |
| TTL4 | 4 | The TTL4 trigger line. |
| TTL5 | 5 | The TTL5 trigger line. |
| TTL6 | 6 | The TTL6 trigger line. |
| TTL7 | 7 | The TTL7 trigger line. |

[IMAGE alt='datatype_icon' src='/assets/img/c1du16.png']

##### buses

The bus segments that correspond to each trigger line from lines.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### failure index

The index where any potential errors in the array are located.

Parent topic:

PXI Reserve Trigger Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=pxi-reserve-trigger-single.html language=enus -->
## TOPIC 00037: Single

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `pxi-reserve-trigger-single.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/pxi-reserve-trigger-single.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reserves a single trigger line. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error line The trigger line. TTL0 0 The TTL0 trigger line. T

Single

Reserves a single trigger line.

[IMAGE alt='1378' src='PXI_Reserve_Trigger_(Instr).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### line

The trigger line.

| TTL0 | 0 | The TTL0 trigger line. |
| --- | --- | --- |
| TTL1 | 1 | The TTL1 trigger line. |
| TTL2 | 2 | The TTL2 trigger line. |
| TTL3 | 3 | The TTL3 trigger line. |
| TTL4 | 4 | The TTL4 trigger line. |
| TTL5 | 5 | The TTL5 trigger line. |
| TTL6 | 6 | The TTL6 trigger line. |
| TTL7 | 7 | The TTL7 trigger line. |

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### bus

The bus segment of the trigger line to be reserved.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

PXI Reserve Trigger Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=pxi-unmap-trigger-all.html language=enus -->
## TOPIC 00038: All

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `pxi-unmap-trigger-all.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/pxi-unmap-trigger-all.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unroutes all destination trigger lines that are currently connected to the specified source trigger line. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Defa

All

Unroutes all destination trigger lines that are currently connected to the specified source trigger line.

[IMAGE alt='1378' src='PXI_Unmap_Trigger_(PXI_Backplane,_All).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### source line

The source trigger line. This input accepts the following values:

| TTL0 | 0 | The TTL0 trigger line. |
| --- | --- | --- |
| TTL1 | 1 | The TTL1 trigger line. |
| TTL2 | 2 | The TTL2 trigger line. |
| TTL3 | 3 | The TTL3 trigger line. |
| TTL4 | 4 | The TTL4 trigger line. |
| TTL5 | 5 | The TTL5 trigger line. |
| TTL6 | 6 | The TTL6 trigger line. |
| TTL7 | 7 | The TTL7 trigger line. |

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### source bus

The bus segment of the source trigger line.

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### destination bus

The bus segment of the destination trigger line.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

PXI Unmap Trigger Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=pxi-unmap-trigger-multimode-function.html language=enus -->
## TOPIC 00039: PXI Unmap Trigger Multimode Function

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `pxi-unmap-trigger-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/pxi-unmap-trigger-multimode-function.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unroutes a previous map from a trigger source to a trigger destination line.

PXI Unmap Trigger Multimode Function

Unroutes a previous map from a trigger source to a trigger destination line.

PXI

VISA functions for PXI devices.

All

Unroutes all destination trigger lines that are currently connected to the specified source trigger line.

Wired In

Unroutes the specified source trigger line from the wired in destination trigger line.

Parent topic:

PXI

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=pxi-unmap-trigger-wired-in.html language=enus -->
## TOPIC 00040: Wired In

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `pxi-unmap-trigger-wired-in.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/pxi-unmap-trigger-wired-in.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unroutes the specified source trigger line from the wired in destination trigger line. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error

Wired In

Unroutes the specified source trigger line from the wired in destination trigger line.

[IMAGE alt='1378' src='PXI_Unmap_Trigger_(PXI_Backplane,_Wired).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### source line

The source trigger line. This input accepts the following values:

| TTL0 | 0 | The TTL0 trigger line. |
| --- | --- | --- |
| TTL1 | 1 | The TTL1 trigger line. |
| TTL2 | 2 | The TTL2 trigger line. |
| TTL3 | 3 | The TTL3 trigger line. |
| TTL4 | 4 | The TTL4 trigger line. |
| TTL5 | 5 | The TTL5 trigger line. |
| TTL6 | 6 | The TTL6 trigger line. |
| TTL7 | 7 | The TTL7 trigger line. |

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### destination line

The destination trigger line.

This input accepts the following values:

| TTL0 | 0 | The TTL0 trigger line. |
| --- | --- | --- |
| TTL1 | 1 | The TTL1 trigger line. |
| TTL2 | 2 | The TTL2 trigger line. |
| TTL3 | 3 | The TTL3 trigger line. |
| TTL4 | 4 | The TTL4 trigger line. |
| TTL5 | 5 | The TTL5 trigger line. |
| TTL6 | 6 | The TTL6 trigger line. |
| TTL7 | 7 | The TTL7 trigger line. |

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### source bus

The bus segment of the source trigger line.

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### destination bus

The bus segment of the destination trigger line.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

PXI Unmap Trigger Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=pxi-unreserve-trigger.html language=enus -->
## TOPIC 00041: PXI Unreserve Trigger

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `pxi-unreserve-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/pxi-unreserve-trigger.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Frees a reserved trigger line. Use this function to un-reserve a trigger line you reserved using PXI Reserve Trigger. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error B

PXI Unreserve Trigger

Frees a reserved trigger line.

Use this function to un-reserve a trigger line you reserved using PXI Reserve Trigger.

[IMAGE alt='1378' src='PXI_Unreserve_Trigger_(Instr).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### line

The trigger line.

| TTL0 | 0 | The TTL0 trigger line. |
| --- | --- | --- |
| TTL1 | 1 | The TTL1 trigger line. |
| TTL2 | 2 | The TTL2 trigger line. |
| TTL3 | 3 | The TTL3 trigger line. |
| TTL4 | 4 | The TTL4 trigger line. |
| TTL5 | 5 | The TTL5 trigger line. |
| TTL6 | 6 | The TTL6 trigger line. |
| TTL7 | 7 | The TTL7 trigger line. |

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### bus

The bus segment of the trigger line to be unreserved.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

PXI

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=read-byte-array.html language=enus -->
## TOPIC 00042: Byte Array

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `read-byte-array.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/read-byte-array.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the specified number of bytes from the device or interface and returns the results as an array of unsigned 8-bit integers. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Stand

Byte Array

Reads the specified number of bytes from the device or interface and returns the results as an array of unsigned 8-bit integers.

[IMAGE alt='1378' src='Read_(Instr,_Bytes).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### byte count

The number of bytes to read.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### read buffer

The actual data read from the device during the data phase of the control transfer.

Parent topic:

Read Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=read-multimode-function.html language=enus -->
## TOPIC 00043: Read Multimode Function

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `read-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/read-multimode-function.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns data from a device or interface.

Read Multimode Function

Returns data from a device or interface.

NI-VISA Nodes

Program instruments using NI-VISA.

Byte Array

Reads the specified number of bytes from the device or interface and returns the results as an array of unsigned 8-bit integers.

String

Reads the specified number of bytes from the device or interface and returns the results as string data.

Parent topic:

NI-VISA Nodes

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=read-stb.html language=enus -->
## TOPIC 00044: Read STB

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `read-stb.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/read-stb.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a service request status byte from the specified message-based device. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session o

Read STB

Reads a service request status byte from the specified message-based device.

[IMAGE alt='1378' src='Read_STB_(Instr).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### status byte

The status byte read from the instrument.

#### Status Bytes for 488.2 Instruments (GPIB, VXI, TCP/IP, USB)

GPIB

VXI

USB

#### Status Bytes for Non-488.2 Instruments (Serial Instr, TCP/IP Socket, USB Raw)

This function retrieves status information by sending a message in response to a service request. If the IO Protocol property is 
 Serial-TCPIP-USB/488 Strings, the device is sent the string 
 "*STB?\n" and then the device status byte is read; otherwise, this operation is not valid.

Parent topic:

NI-VISA Nodes

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=read-string.html language=enus -->
## TOPIC 00045: String

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `read-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/read-string.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the specified number of bytes from the device or interface and returns the results as string data. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Defau

String

Reads the specified number of bytes from the device or interface and returns the results as string data.

[IMAGE alt='1378' src='Read_(Instr,_String).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### byte count

The number of bytes to read.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### read buffer

The data read from the device.

Parent topic:

Read Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=resource-name-constant.html language=enus -->
## TOPIC 00046: VISA Resource Name Constant

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `resource-name-constant.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/resource-name-constant.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the resource to be used by VISA functions.

VISA Resource Name Constant

Defines the resource to be used by VISA functions.

[IMAGE alt='1378' src='Literal.Instr.Visa.Instr.png']

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=send-remote-local-command.html language=enus -->
## TOPIC 00047: Send Remote Local Command

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `send-remote-local-command.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/send-remote-local-command.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Puts a GPIB interface or instrument into remote, local, or lockout mode. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error mode The mode

Send Remote Local Command

Puts a GPIB interface or instrument into remote, local, or lockout mode.

[IMAGE alt='1378' src='Send_Remote_Local_Command_(Instr).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### mode

The mode to place the instrument in.

| Local | 6 | Send the GTL (Go To Local) command. The instrument will go into either LOCS (LOCal State) or LWLS (Local With Lockout State). |
| --- | --- | --- |
| Local without Lockout | 2 | Send the GTL (Go To Local) command and de-assert the REN (Remote ENable) interface line, putting it in LOCS (LOCal State). |
| Remote | 3 | Assert the REN (Remote ENable) interface line and address the device. The instrument will go into either REMS (REMote State) or RWLS (Remote With Lockout State). |
| Remote with Local Lockout | 5 | Address the device and send it an LLO (Local LockOut) command, putting it in the RWLS (Remote With Lockout State). |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=serial-break-break-length-property.html language=enus -->
## TOPIC 00048: Break Length Property

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `serial-break-break-length-property.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/serial-break-break-length-property.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a break on the specified serial port. This mode uses the Break Length property to determine the duration of the serial break. Set the Break Length property using VISA Properties before calling this function. session in The resource to be used. error in Error conditions that occur before this n

Break Length Property

Sends a break on the specified serial port. This mode uses the Break Length property to determine the duration of the serial break.

Set the Break Length property using VISA Properties before calling this function.

[IMAGE alt='1378' src='Serial_Break_(Instr,_Property).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Serial Break Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=serial-break-multimode-function.html language=enus -->
## TOPIC 00049: Serial Break Multimode Function

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `serial-break-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/serial-break-multimode-function.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a break on the specified serial port.

Serial Break Multimode Function

Sends a break on the specified serial port.

Serial

VISA functions for Serial devices.

Break Length Property

Sends a break on the specified serial port. This mode uses the Break Length property to determine the duration of the serial break.

Wired In

Sends a break on the specified serial port.

Parent topic:

Serial

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=serial-break-wired-in.html language=enus -->
## TOPIC 00050: Wired In

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `serial-break-wired-in.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/serial-break-wired-in.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a break on the specified serial port.This mode allows you to specify a duration for the break length. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior De

Wired In

Sends a break on the specified serial port.This mode allows you to specify a duration for the break length.

[IMAGE alt='1378' src='Serial_Break_(Instr,_Input).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### duration

Length of the break in milliseconds.

This value temporarily overrides the current setting of the Break Length property. After the function runs, it returns the current Break Length setting to its original value.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Serial Break Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=set-buffer-size.html language=enus -->
## TOPIC 00051: Set Buffer Size

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `set-buffer-size.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/set-buffer-size.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the size of the I/O buffer. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error buffer The buffer for which you want to set the size.

Set Buffer Size

Sets the size of the I/O buffer.

[IMAGE alt='1378' src='Set_Buffer_Size_(Instr).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### buffer

The buffer for which you want to set the size.

| Receive Buffer | 16 | Sets the size for the Receive buffer only. |
| --- | --- | --- |
| Transmit Buffer | 32 | Sets the size for the Transmit buffer only. |
| Receive and Transmit Buffers | 48 | Sets the size for both the Receive and Transmit buffers. |

Default value: Receive Buffer

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### size

The size of the buffer in bytes.

Set the buffer size slightly higher than the amount of data you expect to transmit or receive. If you do not call this function, the buffer size depends on both VISA and the operating system configuration.

Default value: 4096

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

Run Configure Serial Port first if you are setting the size of a serial port buffer.

#### User-Defined Buffer Sizes

Not all serial drivers support user-defined buffer sizes, so some implementations of VISA might not be able to perform this operation. If an application requires a specific buffer size for performance reasons and the VISA implementation cannot guarantee that size, use some form of handshaking to prevent overflow conditions.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=unmap-address.html language=enus -->
## TOPIC 00052: Unmap Address

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `unmap-address.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/unmap-address.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unmaps the memory window previously mapped by Map Address. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session out The resource to

Unmap Address

Unmaps the memory window previously mapped by Map Address.

[IMAGE alt='1378' src='Unmap_Address_(Instr).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=usb-control-in.html language=enus -->
## TOPIC 00053: USB Control In

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `usb-control-in.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/usb-control-in.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a USB control pipe transfer from a USB device. This function takes the values of the data payload in the setup stage of the control transfer as parameters. The function reads the optional data buffer read buffer if you require a data stage for this transfer. This function is only intended f

USB Control In

Performs a USB control pipe transfer from a USB device.

This function takes the values of the data payload in the setup stage of the control transfer as parameters. The function reads the optional data buffer read buffer if you require a data stage for this transfer.

Note

[IMAGE alt='1378' src='USB_Control_In_(Instr).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### index

Passes a parameter to the device.

The value you enter here depends on the value you entered in request. The index is often used in requests to specify an endpoint or an interface.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### value

Passes a parameter to the device.

request

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### request type

The numeric representation of the request you want to send to the device.

This parameter is a bitmapped field that identifies the characteristics of the specific request, such as the direction of the request, type of the request, and the designated recipient. The bit specifying the direction must be set to 
 1 (device-to-host).

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### request

The particular request. The request you can enter depends on the value you entered in request type.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### length

Length of the data to be transferred during the optional data phase of the control transfer. The direction is device-to-host.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### read buffer

The actual data read from the device during the data phase of the control transfer.

Parent topic:

USB

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=usb-control-out.html language=enus -->
## TOPIC 00054: USB Control Out

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `usb-control-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/usb-control-out.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a USB control pipe transfer to the device. This function takes the values of the data payload in the setup stage of the control transfer as parameters. The function sends an optional data buffer write buffer if you require a data stage for this transfer. This function is only intended for u

USB Control Out

Performs a USB control pipe transfer to the device.

This function takes the values of the data payload in the setup stage of the control transfer as parameters. The function sends an optional data buffer write buffer if you require a data stage for this transfer.

Note

[IMAGE alt='1378' src='USB_Control_Out_(Instr).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### index

Passes a parameter to the device.

The value you enter here depends on the value you entered in request. The index is often used in requests to specify an endpoint or an interface.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### value

Passes a parameter to the device.

request

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### request type

The numeric representation of the request you want to send to the device.

This parameter is a bitmapped field that identifies the characteristics of the specific request, such as the direction of the request, type of the request, and the designated recipient. The bit specifying the direction must be set to 
 0 (host-to-device).

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### request

The particular request. The request you can enter depends on the value you entered in request type.

[IMAGE alt='datatype_icon' src='/assets/img/c1du8.png']

##### write buffer

The data to be written to the device.

Default value: empty array

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

USB

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=visa-advanced.html language=enus -->
## TOPIC 00055: Advanced

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `visa-advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/visa-advanced.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accomplish advanced NI-VISA tasks.

Advanced

Accomplish advanced NI-VISA tasks.

NI-VISA Nodes

Program instruments using NI-VISA.

Assert Software Trigger

Sends a software trigger.

Find Resource Multimode Function

Queries the system to locate the devices associated with a specified interface.

Flush Buffer

Flushes the I/O buffer.

Lock Multimode Function

Attempts to establish access to a device or interface.

VISA Properties

Reads or writes properties to or from a VISA resource.

VISA Resource Name Constant

Defines the resource to be used by VISA functions.

Send Remote Local Command

Puts a GPIB interface or instrument into remote, local, or lockout mode.

Set Buffer Size

Sets the size of the I/O buffer.

Unlock

Relinquishes the lock previously obtained using Lock.

GPIB

VISA functions for GPIB devices.

PXI

VISA functions for PXI devices.

Serial

VISA functions for Serial devices.

USB

VISA functions for USB devices.

VXI

VISA functions for VXI devices.

Event Handling

VISA functions to handle events.

Register Access

Use the Register Access VISA functions to program in an address space at a high level.

Parent topic:

NI-VISA Nodes

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=visa-event-handling.html language=enus -->
## TOPIC 00056: Event Handling

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `visa-event-handling.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/visa-event-handling.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: VISA functions to handle events.

Event Handling

VISA functions to handle events.

Advanced

Accomplish advanced NI-VISA tasks.

Disable Event

Disables servicing of an event.

Discard Events

Discards all pending occurrences of a specific event type from the session's event queue.

Enable Event

Enables notification of a specific type of event.

Wait on Event Multimode Function

Suspends execution of an application thread and waits for an event for a specified time period.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=visa-low-level.html language=enus -->
## TOPIC 00057: Low Level

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `visa-low-level.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/visa-low-level.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: VISA functions for low level register access.

Low Level

VISA functions for low level register access.

Register Access

Use the Register Access VISA functions to program in an address space at a high level.

Map Address

Maps a memory space.

Peek Multimode Function

Reads a value from a location in a memory window mapped by Map Address.

Poke Multimode Function

Writes a value to a location in a memory window mapped by Map Address.

Unmap Address

Unmaps the memory window previously mapped by Map Address.

Parent topic:

Register Access

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=visa-pxi.html language=enus -->
## TOPIC 00058: PXI

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `visa-pxi.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/visa-pxi.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: VISA functions for PXI devices.

PXI

VISA functions for PXI devices.

Advanced

Accomplish advanced NI-VISA tasks.

PXI Map Trigger

Routes a trigger source line to a trigger destination line.

PXI Reserve Trigger Multimode Function

Reserves one or more trigger lines for use in external triggering.

PXI Unmap Trigger Multimode Function

Unroutes a previous map from a trigger source to a trigger destination line.

PXI Unreserve Trigger

Frees a reserved trigger line.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=visa-register-access.html language=enus -->
## TOPIC 00059: Register Access

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `visa-register-access.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/visa-register-access.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Register Access VISA functions to program in an address space at a high level.

Register Access

Use the Register Access VISA functions to program in an address space at a high level.

Advanced

Accomplish advanced NI-VISA tasks.

In Multimode Function

Reads data.

Move In Multimode Function

Copies one or more units of data from device memory to local memory.

Move Out Multimode Function

Copies an array of data from local memory to a specified address space and offset.

Memory Allocation

Allocates device memory of a specific size and returns the location of the memory.

Memory Free

Frees the memory previously allocated by Memory Allocation.

Out Multimode Function

Writes data.

Low Level

VISA functions for low level register access.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=visa-serial.html language=enus -->
## TOPIC 00060: Serial

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `visa-serial.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/visa-serial.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: VISA functions for Serial devices.

Serial

VISA functions for Serial devices.

Advanced

Accomplish advanced NI-VISA tasks.

Configure Serial Port

Initializes the specified serial port to the specified settings.

Serial Break Multimode Function

Sends a break on the specified serial port.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=visa-usb.html language=enus -->
## TOPIC 00061: USB

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `visa-usb.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/visa-usb.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: VISA functions for USB devices.

USB

VISA functions for USB devices.

Advanced

Accomplish advanced NI-VISA tasks.

USB Control In

Performs a USB control pipe transfer from a USB device.

USB Control Out

Performs a USB control pipe transfer to the device.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=visa-vxi.html language=enus -->
## TOPIC 00062: VXI

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `visa-vxi.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/visa-vxi.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: VISA functions for VXI devices.

VXI

VISA functions for VXI devices.

Advanced

Accomplish advanced NI-VISA tasks.

VXI Assert Hardware Trigger

Sends a hardware trigger along a VXI trigger line.

VXI Assert Interrupt Signal

Asserts the specified device interrupt or signal.

VXI Assert Utility Signal

Asserts or de-asserts the specified utility bus signal.

VXI Command or Query

Sends the device a miscellaneous command or query and/or retrieves the response to a previous query.

VXI Map Trigger

Routes a trigger source line to a trigger destination line.

VXI Move

Moves a specified number of elements of a specific bit depth from a source address space and offset to a destination address space and offset.

VXI Unmap Trigger Multimode Function

Unmaps a previously mapped trigger line connection.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=vxi-assert-hardware-trigger.html language=enus -->
## TOPIC 00063: VXI Assert Hardware Trigger

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `vxi-assert-hardware-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/vxi-assert-hardware-trigger.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a hardware trigger along a VXI trigger line. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error trigger ID The identity of the trig

VXI Assert Hardware Trigger

Sends a hardware trigger along a VXI trigger line.

[IMAGE alt='1378' src='VXI_Assert_Hardware_Trigger_(Instr).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### trigger ID

The identity of the trigger to assert.

| TTL0 - TTL7 | 0-7 | The TTL trigger lines of a VXI chassis. |
| --- | --- | --- |
| ECL0 - ECL5 | 8-13 | The ECL trigger lines of a VXI chassis. |
| Star Slot1 - Star Slot12 | 14-25 | The star trigger slots of a VXI chassis. Star trigger slots route one trigger to the Slot 0 Star Trigger distribution logic. |
| Star Instrument | 26 | An instrument connected to a VXI Star slot. |
| Panel In | 27 | The controller's front panel trigger input line. |
| Panel Out | 28 | The controller's front panel trigger output line. |
| Star VXI0 - Star VXI2 | 29-31 | The star trigger outputs of the VXI chassis. |

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### protocol

The triggering protocol.

| On | 1 | Broadcasts a start message to the device. |
| --- | --- | --- |
| Off | 2 | Broadcasts a stop message to the device. |
| Sync | 5 | Broadcasts a single-line, single-pulse trigger to the device. The sync pulse does not require any acknowledgment from the device. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

VXI

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=vxi-assert-interrupt-signal.html language=enus -->
## TOPIC 00064: VXI Assert Interrupt Signal

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `vxi-assert-interrupt-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/vxi-assert-interrupt-signal.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asserts the specified device interrupt or signal. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error mode Method to assert the interrupt.

VXI Assert Interrupt Signal

Asserts the specified device interrupt or signal.

[IMAGE alt='1378' src='VXI_Assert_Interrupt_Signal_(VXI_Backplane).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### mode

Method to assert the interrupt.

| VXI/VME IRQ 1 - VXI/VME IRQ 7 | 1-7 | Sends the interrupt through the specified VXI/VME IRQ line. This uses the standard VXI/VME ROAK (release on acknowledge) interrupt mechanism rather than the older VME RORA (release on register access) mechanism. |
| --- | --- | --- |

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### status ID

The status value to be presented during an interrupt acknowledge cycle.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

VXI

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=vxi-assert-utility-signal.html language=enus -->
## TOPIC 00065: VXI Assert Utility Signal

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `vxi-assert-utility-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/vxi-assert-utility-signal.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asserts or de-asserts the specified utility bus signal. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error bus signal The utility bus sig

VXI Assert Utility Signal

Asserts or de-asserts the specified utility bus signal.

[IMAGE alt='1378' src='VXI_Assert_Utility_Signal_(VXI_Backplane).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### bus signal

The utility bus signal to assert.

| Assert SYSRESET | 1 | Asserts the SYSRESET utility bus interrupt. |
| --- | --- | --- |
| Assert SYSFAIL | 2 | Asserts the SYSFAIL utility bus interrupt. |
| Deassert SYSFAIL | 3 | Deasserts the SYSFAIL utility bus interrupt. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

VXI

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=vxi-command-or-query.html language=enus -->
## TOPIC 00066: VXI Command or Query

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `vxi-command-or-query.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/vxi-command-or-query.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the device a miscellaneous command or query and/or retrieves the response to a previous query. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default v

VXI Command or Query

Sends the device a miscellaneous command or query and/or retrieves the response to a previous query.

[IMAGE alt='1378' src='VXI_Command_or_Query_(Instr).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### mode

Control that specifies whether to issue a command and/or retrieve a response.

| Send 16-Bit Command | 512 | Issues the 16-bit command specified in command. |
| --- | --- | --- |
| Send 16-bit Query; Get 16-bit Response | 514 | Issues a 16-bit query specified in command and returns a 16-bit response. |
| Get 16-bit Response from Previous Query | 2 | Returns a 16-bit response to a query you previously called. |
| Send 32-bit Command | 1024 | Issues the 32-bit command specified in command. |
| Send 32-bit Query; Get 16-bit Response | 1026 | Issues a 32-bit query specified in command and returns a 16-bit response. |
| Send 32-bit Query; Get 32-bit Response | 1028 | Issues a 32-bit query specified in command and returns a 32-bit response. |
| Get 32-bit Response from Previous Query | 4 | Returns a 32-bit response to a query you previously called. |

Default value: Send 16-bit Command

##### Ignoring Command or Response Parameters

The mode you specify can cause all or part of the command or response parameters to be ignored. The possible results of specifying a particular mode are the following:

- If mode specifies sending a 16-bit command, the upper half of command is ignored.
- If mode specifies retrieving a response only, command is ignored.
- If mode specifies sending a command only, response is ignored.
- If mode specifies to retrieve a 16-bit value, the upper half of response is set to 0.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### command

The miscellaneous command to send.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### response

The response retrieved from the device.

Parent topic:

VXI

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=vxi-map-trigger.html language=enus -->
## TOPIC 00067: VXI Map Trigger

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `vxi-map-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/vxi-map-trigger.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes a trigger source line to a trigger destination line. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error source line The source lin

VXI Map Trigger

Routes a trigger source line to a trigger destination line.

[IMAGE alt='1378' src='VXI_Map_Trigger_(VXI_Backplane).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### source line

The source line for the trigger.

| TTL0 - TTL7 | 0-7 | The TTL trigger lines of a VXI chassis. |
| --- | --- | --- |
| ECL0 - ECL5 | 8-13 | The ECL trigger lines of a VXI chassis. |
| Star Slot1 - Star Slot12 | 14-25 | The star trigger slots of a VXI chassis. Star trigger slots route one trigger to the Slot 0 Star Trigger distribution logic. |
| Star Instrument | 26 | An instrument connected to a VXI Star slot. |
| Panel In | 27 | The controller's front panel trigger input line. |
| Panel Out | 28 | The controller's front panel trigger output line. |
| Star VXI0 - Star VXI2 | 29-31 | The star trigger outputs of the VXI chassis. |

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### destination line

The destination line for a trigger source.

| TTL0 - TTL7 | 0-7 | The TTL trigger lines of a VXI chassis. |
| --- | --- | --- |
| ECL0 - ECL5 | 8-13 | The ECL trigger lines of a VXI chassis. |
| Star Slot1 - Star Slot12 | 14-25 | The star trigger slots of a VXI chassis. Star trigger slots route one trigger to the Slot 0 Star Trigger distribution logic. |
| Star Instrument | 26 | An instrument connected to a VXI star slot. |
| Panel In | 27 | The controller's front panel trigger input line. |
| Panel Out | 28 | The controller's front panel trigger output line. |
| Star VXI0 - Star VXI2 | 29-31 | The star trigger outputs of the VXI chassis. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

VXI

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-multimode-function.html language=enus -->
## TOPIC 00068: Wait on Event Multimode Function

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-multimode-function.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Suspends execution of an application thread and waits for an event for a specified time period.

Wait on Event Multimode Function

Suspends execution of an application thread and waits for an event for a specified time period.

Event Handling

VISA functions to handle events.

Clear

Waits for the device clear message to be sent to the local controller.

GPIB CIC

Waits until the GPIB controller has gained or lost CIC (controller-in-charge) status.

GPIB Talk

Waits until the GPIB controller is addressed to talk.

GPIB Listen

Waits until the GPIB controller has been addressed to listen.

PXI Interrupt

Waits for a PXI interrupt event.

Serial Break

Waits for a serial break event to occur.

Serial TermChar

Waits for the termination character for the serial device.

Serial CTS

Waits until the Clear to Send (CTS) line changes state.

Serial DSR

Waits until the Data Set Ready (DSR) line changes state.

Serial DCD

Waits until the Data Carrier Detect (DCD) line changes state.

Serial RI

Waits until the Ring Indicator (RI) input signal is asserted.

Serial Character

Waits until at least one data byte has been received.

Trigger

Waits for a trigger event.

USB Interrupt

Waits until a USB interrupt has occurred.

Wired In

Waits for the specified event that is wired in.

VXI/VME Interrupt

Waits until a VXIbus interrupt is received from the device.

VXI Signal

Waits until the application receives a VXIbus signal or VXIbus interrupt from the device.

VXI/VME Sysfail

Waits until the VXI/VME SYSFAIL* line is asserted.

VXI/VME Sysreset

Waits until the VXI/VME SYSRESET* line is asserted.

Parent topic:

Event Handling

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-pxi-interrupt.html language=enus -->
## TOPIC 00069: PXI Interrupt

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-pxi-interrupt.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-pxi-interrupt.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for a PXI interrupt event. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error wait timeout Time, in milliseconds, that the function

PXI Interrupt

Waits for a PXI interrupt event.

[IMAGE alt='1378' src='Wait_on_Event_(Instr,_PXI_Interrupt).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### wait timeout

Time, in milliseconds, that the function waits for the event.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### interrupt data

The first register read in the interrupt sequence.

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### interrupt sequence

The index of the interrupt sequence that detected the interrupt condition.

Parent topic:

Wait on Event Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-serial-break.html language=enus -->
## TOPIC 00070: Serial Break

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-serial-break.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-serial-break.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for a serial break event to occur. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error wait timeout Time, in milliseconds, that the

Serial Break

Waits for a serial break event to occur.

[IMAGE alt='1378' src='Wait_on_Event_(Instr,_Serial_Break).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### wait timeout

Time, in milliseconds, that the function waits for the event.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Wait on Event Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-serial-character.html language=enus -->
## TOPIC 00071: Serial Character

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-serial-character.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-serial-character.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until at least one data byte has been received. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error wait timeout Time, in millisecon

Serial Character

Waits until at least one data byte has been received.

[IMAGE alt='1378' src='Wait_on_Event_(Instr,_Serial_Character).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### wait timeout

Time, in milliseconds, that the function waits for the event.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Wait on Event Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-serial-cts.html language=enus -->
## TOPIC 00072: Serial CTS

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-serial-cts.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-serial-cts.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the Clear to Send (CTS) line changes state. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error wait timeout Time, in millisec

Serial CTS

Waits until the Clear to Send (CTS) line changes state.

[IMAGE alt='1378' src='Wait_on_Event_(Instr,_Serial_CTS).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### wait timeout

Time, in milliseconds, that the function waits for the event.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Wait on Event Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-serial-dcd.html language=enus -->
## TOPIC 00073: Serial DCD

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-serial-dcd.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-serial-dcd.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the Data Carrier Detect (DCD) line changes state. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error wait timeout Time, in mi

Serial DCD

Waits until the Data Carrier Detect (DCD) line changes state.

[IMAGE alt='1378' src='Wait_on_Event_(Instr,_Serial_DCD).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### wait timeout

Time, in milliseconds, that the function waits for the event.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Wait on Event Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-serial-dsr.html language=enus -->
## TOPIC 00074: Serial DSR

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-serial-dsr.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-serial-dsr.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the Data Set Ready (DSR) line changes state. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error wait timeout Time, in millise

Serial DSR

Waits until the Data Set Ready (DSR) line changes state.

[IMAGE alt='1378' src='Wait_on_Event_(Instr,_Serial_DSR).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### wait timeout

Time, in milliseconds, that the function waits for the event.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Wait on Event Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-serial-ri.html language=enus -->
## TOPIC 00075: Serial RI

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-serial-ri.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-serial-ri.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the Ring Indicator (RI) input signal is asserted. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error wait timeout Time, in mi

Serial RI

Waits until the Ring Indicator (RI) input signal is asserted.

[IMAGE alt='1378' src='Wait_on_Event_(Instr,_Serial_RI).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### wait timeout

Time, in milliseconds, that the function waits for the event.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Wait on Event Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-serial-termchar.html language=enus -->
## TOPIC 00076: Serial TermChar

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-serial-termchar.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-serial-termchar.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the termination character for the serial device. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error wait timeout Time, in milli

Serial TermChar

Waits for the termination character for the serial device.

[IMAGE alt='1378' src='Wait_on_Event_(Instr,_Serial_TermChar).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### wait timeout

Time, in milliseconds, that the function waits for the event.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Wait on Event Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-service-request-read-status-byte.html language=enus -->
## TOPIC 00077: Read Status Byte

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-service-request-read-status-byte.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-service-request-read-status-byte.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for a Service Request event from a device. If the event arrives within the specified timeout period, the status byte of the device is read and returned. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to

Read Status Byte

Waits for a Service Request event from a device.

If the event arrives within the specified timeout period, the status byte of the device is read and returned.

[IMAGE alt='1378' src='Wait_on_Event_(Instr,_Service_Request_with_STB).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### wait timeout

Time, in milliseconds, that the function waits for the event.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### status byte

The status byte read from the instrument.

Parent topic:

Wait on Event Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-trigger.html language=enus -->
## TOPIC 00078: Trigger

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-trigger.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for a trigger event. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error wait timeout Time, in milliseconds, that the function waits

Trigger

Waits for a trigger event.

[IMAGE alt='1378' src='Wait_on_Event_(Instr,_Trigger).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### wait timeout

Time, in milliseconds, that the function waits for the event.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### trigger ID

The source of the detected trigger.

| Software | -1 | A software trigger. |
| --- | --- | --- |
| TTL0 | 0 | The TTL0 trigger line. |
| TTL1 | 1 | The TTL1 trigger line. |
| TTL2 | 2 | The TTL2 trigger line. |
| TTL3 | 3 | The TTL3 trigger line. |
| TTL4 | 4 | The TTL4 trigger line. |
| TTL5 | 5 | The TTL5 trigger line. |
| TTL6 | 6 | The TTL6 trigger line. |
| TTL7 | 7 | The TTL7 trigger line. |
| ECL0 | 8 | The ECL0 trigger line. |
| ECL1 | 9 | The ECL1 trigger line. |

Parent topic:

Wait on Event Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-usb-interrupt.html language=enus -->
## TOPIC 00079: USB Interrupt

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-usb-interrupt.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-usb-interrupt.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until a USB interrupt has occurred. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error wait timeout Time, in milliseconds, that the

USB Interrupt

Waits until a USB interrupt has occurred.

[IMAGE alt='1378' src='Wait_on_Event_(Instr,_USB_Interrupt).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### wait timeout

Time, in milliseconds, that the function waits for the event.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### interrupt data

The actual data that was received from the USB interrupt-IN pipe.

Parent topic:

Wait on Event Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-vxi-signal.html language=enus -->
## TOPIC 00080: VXI Signal

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-vxi-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-vxi-signal.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the application receives a VXIbus signal or VXIbus interrupt from the device. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No er

VXI Signal

Waits until the application receives a VXIbus signal or VXIbus interrupt from the device.

[IMAGE alt='1378' src='Wait_on_Event_(Instr,_VXI_Signal).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### wait timeout

Time, in milliseconds, that the function waits for the event.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### signal processor status ID

The status or ID value retrieved from the Signal register.

Parent topic:

Wait on Event Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-vxi-vme-interrupt.html language=enus -->
## TOPIC 00081: VXI/VME Interrupt

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-vxi-vme-interrupt.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-vxi-vme-interrupt.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until a VXIbus interrupt is received from the device. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error wait timeout Time, in mill

VXI/VME Interrupt

Waits until a VXIbus interrupt is received from the device.

[IMAGE alt='1378' src='Wait_on_Event_(Instr,_VXI_Interrupt).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### wait timeout

Time, in milliseconds, that the function waits for the event.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### interrupt status ID

The status or ID value retrieved during the IACK cycle.

Parent topic:

Wait on Event Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-vxi-vme-sysfail.html language=enus -->
## TOPIC 00082: VXI/VME Sysfail

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-vxi-vme-sysfail.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-vxi-vme-sysfail.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the VXI/VME SYSFAIL* line is asserted. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session out The resource to which a

VXI/VME Sysfail

Waits until the VXI/VME SYSFAIL* line is asserted.

[IMAGE alt='1378' src='Wait_on_Event_(VXI_Backplane,_VXI_Sysfail).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Wait on Event Multimode Function

<!--NI_TOPIC bundle=ni-visa-17.0-lvnxg-api-ref path=wait-on-event-vxi-vme-sysreset.html language=enus -->
## TOPIC 00083: VXI/VME Sysreset

- bundle_id: `ni-visa-17.0-lvnxg-api-ref`
- source_path: `wait-on-event-vxi-vme-sysreset.html`
- source_url: https://docs-be.ni.com/bundle/ni-visa-17.0-lvnxg-api-ref/raw/resource/enus/wait-on-event-vxi-vme-sysreset.html
- document_id: `ni-visa-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the VXI/VME SYSRESET* line is asserted. session in The resource to be used. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error wait timeout Time, in milliseconds

VXI/VME Sysreset

Waits until the VXI/VME SYSRESET* line is asserted.

[IMAGE alt='1378' src='Wait_on_Event_(VXI_Backplane,_VXI_Sysreset).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The resource to be used.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### wait timeout

Time, in milliseconds, that the function waits for the event.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The resource to which a VISA session is opened.

This output also includes the class for the session, which matches that of session in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Wait on Event Multimode Function
