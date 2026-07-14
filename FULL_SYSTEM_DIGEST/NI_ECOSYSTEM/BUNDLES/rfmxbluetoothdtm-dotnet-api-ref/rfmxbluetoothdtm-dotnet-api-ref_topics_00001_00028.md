# NI DOCUMENT BUNDLE: rfmxbluetoothdtm-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxbluetoothdtm-dotnet-api-ref start=1 end=28 -->
<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-bluetoothdtmdirectionfindingmode.html language=enus -->
## TOPIC 00001: BluetoothDtmDirectionFindingMode Enumeration

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-bluetoothdtmdirectionfindingmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-bluetoothdtmdirectionfindingmode.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mode of direction finding. The default value is Disabled. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic enum BluetoothDtmDirectionFindingModeMembersNameValueDescriptionDisabled0Specifies that the LE packet does not have fields required for direction finding. AngleOfArrival1Sp

### BluetoothDtmDirectionFindingMode Enumeration

Specifies the mode of direction finding. The default value is Disabled.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public enum BluetoothDtmDirectionFindingMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | Specifies that the LE packet does not have fields required for direction finding. |
| AngleOfArrival | 1 | Specifies the LE packets uses the angle of arrival method of direction finding. |
| AngleOfDeparture | 2 | Specifies the LE packet uses angle of departure method of direction finding. |

Parent topic:

NationalInstruments.BluetoothDtm

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-bluetoothdtmexception-bluetoothdtmexception.html language=enus -->
## TOPIC 00002: BluetoothDtmException()

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-bluetoothdtmexception-bluetoothdtmexception.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-bluetoothdtmexception-bluetoothdtmexception.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the class BluetoothDtmException. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic BluetoothDtmException()

### BluetoothDtmException()

Initializes a new instance of the class BluetoothDtmException.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public BluetoothDtmException()

Parent topic:

BluetoothDtmException Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-bluetoothdtmexception-bluetoothdtmexception__string.html language=enus -->
## TOPIC 00003: BluetoothDtmException(string)

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-bluetoothdtmexception-bluetoothdtmexception__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-bluetoothdtmexception-bluetoothdtmexception__string.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the class BluetoothDtmException with a specified error message. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic BluetoothDtmException(string message)ParametersNameTypeDescriptionmessagestringThe message that describes the error.

### BluetoothDtmException(string)

Initializes a new instance of the class BluetoothDtmException with a specified error message.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public BluetoothDtmException(string message)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| message | string | The message that describes the error. |

Parent topic:

BluetoothDtmException Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-bluetoothdtmexception.html language=enus -->
## TOPIC 00004: BluetoothDtmException Class

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-bluetoothdtmexception.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-bluetoothdtmexception.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the BluetoothDtmException class with a specified error message. Derives fromExceptionSyntaxNamespace: NationalInstruments.BluetoothDtmpublic class BluetoothDtmException : ExceptionThread SafetyAny members of this type are not guaranteed to be thread safe.ConstructorsNam

### BluetoothDtmException Class

Initializes a new instance of the BluetoothDtmException class with a specified error message.

#### Derives from

- Exception

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public class BluetoothDtmException : Exception

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| BluetoothDtmException(string) | Initializes a new instance of the class BluetoothDtmException with a specified error message. |
| BluetoothDtmException() | Initializes a new instance of the class BluetoothDtmException. |

Parent topic:

NationalInstruments.BluetoothDtm

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-bluetoothdtmflowcontrol.html language=enus -->
## TOPIC 00005: BluetoothDtmFlowControl Enumeration

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-bluetoothdtmflowcontrol.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-bluetoothdtmflowcontrol.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the flow control method used for transmitting and receiving data. The default value is RtsCts. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic enum BluetoothDtmFlowControlMembersNameValueDescriptionNone0Does not use flow control, and the buffers on both sides of the connection are

### BluetoothDtmFlowControl Enumeration

Specifies the flow control method used for transmitting and receiving data. The default value is RtsCts.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public enum BluetoothDtmFlowControl

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | Does not use flow control, and the buffers on both sides of the connection are assumed to be large enough to hold all the transferred data. |
| XOnXOff | 1 | Uses the XON and XOFF characters to complete flow control. The transfer mechanism controls input flow by transmitting XOFF when the low-level I/O receive buffer is nearly full, and it controls the output flow by suspending transmission when XOFF is received. |
| RtsCts | 2 | Uses the RTS output signal and the CTS input signal to complete flow control. The transfer mechanism controls input flow by unasserting the RTS signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the CTS signal is unasserted. |
| DtrDsr | 4 | Uses the DTR output signal and the DSR input signal to complete flow control. The transfer mechanism controls input flow by unasserting the DTR signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the DSR signal is unasserted. |

Parent topic:

NationalInstruments.BluetoothDtm

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-bluetoothdtmlepatterntype.html language=enus -->
## TOPIC 00006: BluetoothDtmLEPatternType Enumeration

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-bluetoothdtmlepatterntype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-bluetoothdtmlepatterntype.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of payload to use for the LE packet. Payload type values of Type_Prbs9, Type_11110000, and Type_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is Type_Prbs9. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic enum Blue

### BluetoothDtmLEPatternType Enumeration

Specifies the type of payload to use for the LE packet. Payload type values of Type_Prbs9, Type_11110000, and Type_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is Type_Prbs9.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public enum BluetoothDtmLEPatternType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Type_Prbs9 | 0 | Specifies that the bit sequence is PRBS9. |
| Type_11110000 | 1 | Specifies that the bit sequence is 11110000. |
| Type_10101010 | 2 | Specifies that the bit sequence is 10101010. |
| Type_Prbs15 | 3 | Specifies that the bit sequence is PRBS15. |
| Type_11111111 | 4 | Specifies that the bit sequence is 11111111. |
| Type_00000000 | 5 | Specifies that the bit sequence is 00000000. |
| Type_00001111 | 6 | Specifies that the bit sequence is 00001111. |
| Type_01010101 | 7 | Specifies that the bit sequence is 01010101. |

Parent topic:

NationalInstruments.BluetoothDtm

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-bluetoothdtmmodulationindex.html language=enus -->
## TOPIC 00007: BluetoothDtmModulationIndex Enumeration

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-bluetoothdtmmodulationindex.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-bluetoothdtmmodulationindex.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of modulation index at the generator. The default value is Standard. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic enum BluetoothDtmModulationIndexMembersNameValueDescriptionStandard0The packets are generated with standard modulation index. Stable1The packets are generat

### BluetoothDtmModulationIndex Enumeration

Specifies the type of modulation index at the generator. The default value is Standard.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public enum BluetoothDtmModulationIndex

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Standard | 0 | The packets are generated with standard modulation index. |
| Stable | 1 | The packets are generated with stable modulation index. |

Parent topic:

NationalInstruments.BluetoothDtm

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-bluetoothdtmparity.html language=enus -->
## TOPIC 00008: BluetoothDtmParity Enumeration

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-bluetoothdtmparity.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-bluetoothdtmparity.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the parity bit used with each transmitted or received frame. The default value is None. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic enum BluetoothDtmParityMembersNameValueDescriptionNone0Specifies that the frame does not contain a parity bit. Odd1Specifies that the parity is od

### BluetoothDtmParity Enumeration

Specifies the parity bit used with each transmitted or received frame. The default value is None.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public enum BluetoothDtmParity

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | Specifies that the frame does not contain a parity bit. |
| Odd | 1 | Specifies that the parity is odd. |
| Even | 2 | Specifies that the parity is even. |
| Mark | 3 | Specifies that the parity bit is always 1. |
| Space | 4 | Specifies that the parity bit is always 0. |

Parent topic:

NationalInstruments.BluetoothDtm

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-bluetoothdtmreceiverphy.html language=enus -->
## TOPIC 00009: BluetoothDtmReceiverPhy Enumeration

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-bluetoothdtmreceiverphy.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-bluetoothdtmreceiverphy.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of the generated packet by the physical layer of the DUT. The default value is Phy_1Mbps. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic enum BluetoothDtmReceiverPhyMembersNameValueDescriptionPhy_1Mbps1Receiver is set to use the LE 1M PHY. Phy_2Mbps2Receiver is set to use

### BluetoothDtmReceiverPhy Enumeration

Specifies the type of the generated packet by the physical layer of the DUT. The default value is Phy_1Mbps.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public enum BluetoothDtmReceiverPhy

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Phy_1Mbps | 1 | Receiver is set to use the LE 1M PHY. |
| Phy_2Mbps | 2 | Receiver is set to use the LE 2M PHY. |
| Phy_Coded | 3 | Receiver is set to use the Coded PHY. |

Parent topic:

NationalInstruments.BluetoothDtm

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-bluetoothdtmstopbits.html language=enus -->
## TOPIC 00010: BluetoothDtmStopBits Enumeration

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-bluetoothdtmstopbits.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-bluetoothdtmstopbits.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: specifies the number of stop bits used to indicate the end of a frame. The default value is StopBits1_0. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic enum BluetoothDtmStopBitsMembersNameValueDescriptionStopBits1_010Specifies that the number of stop bits used is 1. StopBits1_50xFSpecifies

### BluetoothDtmStopBits Enumeration

specifies the number of stop bits used to indicate the end of a frame. The default value is StopBits1_0.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public enum BluetoothDtmStopBits

#### Members

| Name | Value | Description |
| --- | --- | --- |
| StopBits1_0 | 10 | Specifies that the number of stop bits used is 1. |
| StopBits1_5 | 0xF | Specifies that the number of stop bits used is 1.5. |
| StopBits2_0 | 20 | Specifies that the number of stop bits used is 2. |

Parent topic:

NationalInstruments.BluetoothDtm

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-bluetoothdtmtransmitterphy.html language=enus -->
## TOPIC 00011: BluetoothDtmTransmitterPhy Enumeration

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-bluetoothdtmtransmitterphy.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-bluetoothdtmtransmitterphy.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is Phy_1Mbps. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic enum BluetoothDtmTransmitterPhyMembersNameValueDescriptionPhy_1Mbps1Transmitter is set to use the LE 1M PHY. Phy_2Mbps2Transmit

### BluetoothDtmTransmitterPhy Enumeration

Specifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is Phy_1Mbps.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public enum BluetoothDtmTransmitterPhy

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Phy_1Mbps | 1 | Transmitter is set to use the LE 1M PHY. |
| Phy_2Mbps | 2 | Transmitter is set to use the LE 2M PHY. |
| Phy_Coded_125Kbps | 3 | Transmitter is set to use the LE Coded PHY with S = 8 data coding. |
| Phy_Coded_500Kbps | 4 | Transmitter is set to use the LE Coded PHY with S = 2 data coding. |

Parent topic:

NationalInstruments.BluetoothDtm

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-close.html language=enus -->
## TOPIC 00012: Close()

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-close.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-close.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a device session or the event object that you specify in the VISA resource name parameter. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic void Close()Returns

### Close()

Closes a device session or the event object that you specify in the VISA resource name parameter.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public void Close()

#### Returns

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-configurevisaserialsettings__ushort-uint-bluetoothdtmflowcontrol-bluetoothdtmstopbits-bluetoothdtmparity.html language=enus -->
## TOPIC 00013: ConfigureVisaSerialSettings(ushort, uint, BluetoothDtmFlowControl, BluetoothDtmStopBits, BluetoothDtmParity)

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-configurevisaserialsettings__ushort-uint-bluetoothdtmflowcontrol-bluetoothdtmstopbits-bluetoothdtmparity.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-configurevisaserialsettings__ushort-uint-bluetoothdtmflowcontrol-bluetoothdtmstopbits-bluetoothdtmparity.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the VISA serial settings for the device under test (DUT) specified by the VISA resource name parameter. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic int ConfigureVisaSerialSettings(ushort dataBits, uint baudRate, BluetoothDtmFlowControl flowControl, BluetoothDtmStopBits stopBit

### ConfigureVisaSerialSettings(ushort, uint, BluetoothDtmFlowControl, BluetoothDtmStopBits, BluetoothDtmParity)

Configures the VISA serial settings for the device under test (DUT) specified by the VISA resource name parameter.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public int ConfigureVisaSerialSettings(ushort dataBits, uint baudRate, BluetoothDtmFlowControl flowControl, BluetoothDtmStopBits stopBits, BluetoothDtmParity parity)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| dataBits | ushort | Specifies the number of data bits contained in each frame. Valid values are 5 to 8, inclusive. The data bits for each frame are located in the low-order bits of every byte stored in the memory. The default value is 8. |
| baudRate | uint | Specifies the baud rate of the given communication port. The default value is 115,200. |
| flowControl | BluetoothDtmFlowControl | Specifies the baud rate of the given communication port. Specifies the flow control method used for transmitting and receiving data. The default value is RtsCts. |
| stopBits | BluetoothDtmStopBits | Specifies the number of stop bits used to indicate the end of a frame. Valid values are StopBits1_0, StopBits1_5, and StopBits2_0. The default value is StopBits1_0. |
| parity | BluetoothDtmParity | Specifies the parity bit used with each transmitted or received frame. The default value is None |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-createcustomcommand__int_arr1-int_arr1-ref.html language=enus -->
## TOPIC 00014: CreateCustomCommand(int[], int[], ref int[])

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-createcustomcommand__int_arr1-int_arr1-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-createcustomcommand__int_arr1-int_arr1-ref.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the specified custom command to the device under test (DUT). SyntaxNamespace: NationalInstruments.BluetoothDtmpublic int CreateCustomCommand(int[] opCode, int[] commandParameters, ref int[] returnParameters)ParametersNameTypeDescriptionopCodeint[]Specifies an array of custom opcode commands to

### CreateCustomCommand(int[], int[], ref int[])

Sends the specified custom command to the device under test (DUT).

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public int CreateCustomCommand(int[] opCode, int[] commandParameters, ref int[] returnParameters)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| opCode | int[] | Specifies an array of custom opcode commands to send to the DUT. |
| commandParameters | int[] | Specifies an array of the input parameters required for the custom command. |
| returnParameters | ref int[] | Returns an array of the parameters sent by the DUT in response to the custom command. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-dispose.html language=enus -->
## TOPIC 00015: Dispose()

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-dispose.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-dispose.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the VISA session. Call this method a number of times equal to the number of times you obtained a reference to the VISA session for a particular resource name. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic void Dispose()

### Dispose()

Closes the VISA session. Call this method a number of times equal to the number of times you obtained a reference to the VISA session for a particular resource name.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public void Dispose()

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-hciledirectionfindingreceivertest__int-bluetoothdtmmodulationindex-bluetoothdtmreceiverphy-bluetoothdtmdirectionfindingmode-int-double-do...d20e135.html language=enus -->
## TOPIC 00016: HciLEDirectionFindingReceiverTest(int, BluetoothDtmModulationIndex, BluetoothDtmReceiverPhy, BluetoothDtmDirectionFindingMode, int, double, double, int[], out int)

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-hciledirectionfindingreceivertest__int-bluetoothdtmmodulationindex-bluetoothdtmreceiverphy-bluetoothdtmdirectionfindingmode-int-double-do...d20e135.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-hciledirectionfindingreceivertest__int-bluetoothdtmmodulationindex-bluetoothdtmreceiverphy-bluetoothdtmdirectionfindingmode-int-double-do...d20e135.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a command to the device under test (DUT) to start the receiver test. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic int HciLEDirectionFindingReceiverTest(int channelNumber, BluetoothDtmModulationIndex modulationIndex, BluetoothDtmReceiverPhy phy, BluetoothDtmDirectionFindingMode direc

### HciLEDirectionFindingReceiverTest(int, BluetoothDtmModulationIndex, BluetoothDtmReceiverPhy, BluetoothDtmDirectionFindingMode, int, double, double, int[], out int)

Sends a command to the device under test (DUT) to start the receiver test.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public int HciLEDirectionFindingReceiverTest(int channelNumber, BluetoothDtmModulationIndex modulationIndex, BluetoothDtmReceiverPhy phy, BluetoothDtmDirectionFindingMode directionFindingMode, int switchingPatternLength, double cteLength, double cteSlotDuration, int[] antennaID, out int status)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelNumber | int | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| modulationIndex | BluetoothDtmModulationIndex | Specifies the type of modulation index at the generator. The default value is Standard. |
| phy | BluetoothDtmReceiverPhy | Specifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is Phy_1Mbps |
| directionFindingMode | BluetoothDtmDirectionFindingMode | Specifies the mode of direction finding. The default value is Disabled |
| switchingPatternLength | int | Specifies the length of the antenna switching pattern. The default value is 0. |
| cteLength | double | Specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the Direction Finding Mode parameter to either AngleofArrival or AngleofDeparture. The default value is 160 microseconds. |
| cteSlotDuration | double | Specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. The default value is 1 us. Valid values are 1 us and 2 us. |
| antennaID | int[] | Specifies the array of Antenna IDs in the antenna switching pattern. The length of Antenna IDs array must be equal to Length Of Switching Pattern. |
| status | out int | Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-hciledirectionfindingtransmittertest__int-int-bluetoothdtmlepatterntype-bluetoothdtmtransmitterphy-bluetoothdtmdirectionfindingmode-int-d...d20e229.html language=enus -->
## TOPIC 00017: HciLEDirectionFindingTransmitterTest(int, int, BluetoothDtmLEPatternType, BluetoothDtmTransmitterPhy, BluetoothDtmDirectionFindingMode, int, double, double, int[], out int)

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-hciledirectionfindingtransmittertest__int-int-bluetoothdtmlepatterntype-bluetoothdtmtransmitterphy-bluetoothdtmdirectionfindingmode-int-d...d20e229.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-hciledirectionfindingtransmittertest__int-int-bluetoothdtmlepatterntype-bluetoothdtmtransmitterphy-bluetoothdtmdirectionfindingmode-int-d...d20e229.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a command to the device under test (DUT) to start the transmitter test. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic int HciLEDirectionFindingTransmitterTest(int channelNumber, int payloadLength, BluetoothDtmLEPatternType lePatternType, BluetoothDtmTransmitterPhy phy, BluetoothDtmDi

### HciLEDirectionFindingTransmitterTest(int, int, BluetoothDtmLEPatternType, BluetoothDtmTransmitterPhy, BluetoothDtmDirectionFindingMode, int, double, double, int[], out int)

Sends a command to the device under test (DUT) to start the transmitter test.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public int HciLEDirectionFindingTransmitterTest(int channelNumber, int payloadLength, BluetoothDtmLEPatternType lePatternType, BluetoothDtmTransmitterPhy phy, BluetoothDtmDirectionFindingMode directionFindingMode, int switchingPatternLength, double cteLength, double cteSlotDuration, int[] antennaID, out int status)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelNumber | int | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| payloadLength | int | Specifies the length of payload data in each packet that the DUT transmits. This value is expressed in bytes. The default value is 37. |
| lePatternType | BluetoothDtmLEPatternType | Specifies the type of payload to use for the LE packet. Payload type values of Type_Prbs9, Type_11110000, and Type_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is Type_Prbs9. |
| phy | BluetoothDtmTransmitterPhy | Specifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is Phy_1Mbps |
| directionFindingMode | BluetoothDtmDirectionFindingMode | Specifies the mode of direction finding. The default value is Disabled. |
| switchingPatternLength | int | Specifies the length of the antenna switching pattern. The default value is 0. |
| cteLength | double | Specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the Direction Finding Mode parameter to either AngleofArrival or AngleofDeparture. The default value is 160 microseconds. |
| cteSlotDuration | double | Specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. The default value is 1 us. |
| antennaID | int[] | Specifies the array of Antenna IDs in the antenna switching pattern. The length of Antenna IDs array must be equal to Length Of Switching Pattern. |
| status | out int | Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-hcileenhancedreceivertest__int-bluetoothdtmmodulationindex-bluetoothdtmreceiverphy-out.html language=enus -->
## TOPIC 00018: HciLEEnhancedReceiverTest(int, BluetoothDtmModulationIndex, BluetoothDtmReceiverPhy, out int)

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-hcileenhancedreceivertest__int-bluetoothdtmmodulationindex-bluetoothdtmreceiverphy-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-hcileenhancedreceivertest__int-bluetoothdtmmodulationindex-bluetoothdtmreceiverphy-out.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a command to the device under test (DUT) to start the receiver test. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic int HciLEEnhancedReceiverTest(int channelNumber, BluetoothDtmModulationIndex modulationIndex, BluetoothDtmReceiverPhy phy, out int status)ParametersNameTypeDescriptionch

### HciLEEnhancedReceiverTest(int, BluetoothDtmModulationIndex, BluetoothDtmReceiverPhy, out int)

Sends a command to the device under test (DUT) to start the receiver test.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public int HciLEEnhancedReceiverTest(int channelNumber, BluetoothDtmModulationIndex modulationIndex, BluetoothDtmReceiverPhy phy, out int status)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelNumber | int | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| modulationIndex | BluetoothDtmModulationIndex | Specifies the type of modulation index at the generator. The default value is Standard. |
| phy | BluetoothDtmReceiverPhy | Specifies the type of the generated packet by the physical layer of the DUT. The default value is Phy_1Mbps. |
| status | out int | Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-hcileenhancedtransmittertest__int-int-bluetoothdtmlepatterntype-bluetoothdtmtransmitterphy-out.html language=enus -->
## TOPIC 00019: HciLEEnhancedTransmitterTest(int, int, BluetoothDtmLEPatternType, BluetoothDtmTransmitterPhy, out int)

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-hcileenhancedtransmittertest__int-int-bluetoothdtmlepatterntype-bluetoothdtmtransmitterphy-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-hcileenhancedtransmittertest__int-int-bluetoothdtmlepatterntype-bluetoothdtmtransmitterphy-out.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the device under test (DUT) to start the transmitter test. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic int HciLEEnhancedTransmitterTest(int channelNumber, int payloadLengthBytes, BluetoothDtmLEPatternType lePatternType, BluetoothDtmTransmitterPhy phy, out int status)

### HciLEEnhancedTransmitterTest(int, int, BluetoothDtmLEPatternType, BluetoothDtmTransmitterPhy, out int)

Sends the command to the device under test (DUT) to start the transmitter test.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public int HciLEEnhancedTransmitterTest(int channelNumber, int payloadLengthBytes, BluetoothDtmLEPatternType lePatternType, BluetoothDtmTransmitterPhy phy, out int status)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelNumber | int | Specifies the Bluetooth transmit channel number of the signal generated by the DUT. The default value is 0. |
| payloadLengthBytes | int | Specifies the length, in bytes, of payload data in each packet that the DUT transmits. The default value is 37. |
| lePatternType | BluetoothDtmLEPatternType | Specifies the type of payload to use for the LE packet. Payload type values of Type_Prbs9, Type_11110000, and Type_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is Type_Prbs9. |
| phy | BluetoothDtmTransmitterPhy | Specifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is Phy_1Mbps. |
| status | out int | Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-hcilereceivertest__int-out.html language=enus -->
## TOPIC 00020: HciLEReceiverTest(int, out int)

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-hcilereceivertest__int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-hcilereceivertest__int-out.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a command to the device under test (DUT) to start the receiver test. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic int HciLEReceiverTest(int channelNumber, out int status)ParametersNameTypeDescriptionchannelNumberintSpecifies the Bluetooth transmit channel number of the generated sig

### HciLEReceiverTest(int, out int)

Sends a command to the device under test (DUT) to start the receiver test.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public int HciLEReceiverTest(int channelNumber, out int status)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelNumber | int | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| status | out int | Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-hciletestend__out-out.html language=enus -->
## TOPIC 00021: HciLETestEnd(out int, out int)

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-hciletestend__out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-hciletestend__out-out.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the device under test (DUT) to end the transmitter or receiver test. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic int HciLETestEnd(out int packetCount, out int status)ParametersNameTypeDescriptionpacketCountout intReturns the number of packets received by the DUT.stat

### HciLETestEnd(out int, out int)

Sends the command to the device under test (DUT) to end the transmitter or receiver test.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public int HciLETestEnd(out int packetCount, out int status)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| packetCount | out int | Returns the number of packets received by the DUT. |
| status | out int | returns the status of the test end command. The DUT receives and executes the test end command if the status parameter returns a 0x00 value. The test end command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-hciletransmittertest__int-int-bluetoothdtmlepatterntype-out.html language=enus -->
## TOPIC 00022: HciLETransmitterTest(int, int, BluetoothDtmLEPatternType, out int)

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-hciletransmittertest__int-int-bluetoothdtmlepatterntype-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-hciletransmittertest__int-int-bluetoothdtmlepatterntype-out.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a command to the device under test (DUT) to start the transmitter test. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic int HciLETransmitterTest(int channelNumber, int payloadLengthBytes, BluetoothDtmLEPatternType lePatternType, out int status)ParametersNameTypeDescriptionchannelNumber

### HciLETransmitterTest(int, int, BluetoothDtmLEPatternType, out int)

Sends a command to the device under test (DUT) to start the transmitter test.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public int HciLETransmitterTest(int channelNumber, int payloadLengthBytes, BluetoothDtmLEPatternType lePatternType, out int status)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelNumber | int | Specifies the Bluetooth transmit channel number of the signal generated by the DUT. The default value is 0. |
| payloadLengthBytes | int | Specifies the length, in bytes, of payload data in each packet that the DUT transmits. The default value is 37. |
| lePatternType | BluetoothDtmLEPatternType | Specifies the type of payload to use for the LE packet. Payload type values of Type_Prbs9, Type_11110000, and Type_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is Type_Prbs9. |
| status | out int | Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-hcireadbluetoothdeviceaddress__out-out.html language=enus -->
## TOPIC 00023: HciReadBluetoothDeviceAddress(out long, out int)

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-hcireadbluetoothdeviceaddress__out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-hcireadbluetoothdeviceaddress__out-out.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic int HciReadBluetoothDeviceAddress(out long bluetoothDeviceAddress, out int status)ParametersNameTypeDescriptionbluetoothDeviceAddressout longreturns the

### HciReadBluetoothDeviceAddress(out long, out int)

Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public int HciReadBluetoothDeviceAddress(out long bluetoothDeviceAddress, out int status)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| bluetoothDeviceAddress | out long | returns the BD address of the DUT. |
| status | out int | Returns the status of the read BD_ADDR command. The DUT receives and executes the read BD_ADDR command if the status parameter returns a 0x00 value. The read BD_ADDR command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-hcireset__out.html language=enus -->
## TOPIC 00024: HciReset(out int)

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-hcireset__out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-hcireset__out.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the device under test (DUT) specified by the VISA resource name parameter. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic int HciReset(out int status)ParametersNameTypeDescriptionstatusout intReturns the status of the reset command. The DUT receives and executes the reset command if

### HciReset(out int)

Resets the device under test (DUT) specified by the VISA resource name parameter.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public int HciReset(out int status)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| status | out int | Returns the status of the reset command. The DUT receives and executes the reset command if the status parameter returns a 0x00 value. The reset command fails if the parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-nibluetoothdtm__string.html language=enus -->
## TOPIC 00025: NIBluetoothDtm(string)

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-nibluetoothdtm__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-nibluetoothdtm__string.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an NI-VISA session to the device you specify through the resourceName parameter. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic NIBluetoothDtm(string resourceName)ParametersNameTypeDescriptionresourceNamestringSpecifies the resource name of the device to initialize.

### NIBluetoothDtm(string)

Creates an NI-VISA session to the device you specify through the resourceName parameter.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public NIBluetoothDtm(string resourceName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | string | Specifies the resource name of the device to initialize. |

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm-setvisatimeout__uint.html language=enus -->
## TOPIC 00026: SetVisaTimeout(uint)

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm-setvisatimeout__uint.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm-setvisatimeout__uint.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the VISA resource name parameter. SyntaxNamespace: NationalInstruments.BluetoothDtmpublic int SetVisaTimeout(uint timeout)ParametersNameTypeDescriptiontimeoutuintSpecifies the minimum time

### SetVisaTimeout(uint)

Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the VISA resource name parameter.

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public int SetVisaTimeout(uint timeout)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| timeout | uint | Specifies the minimum timeout value, in milliseconds (ms), to use when accessing the device. The default value is 2000. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

NIBluetoothDtm Class

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm-nibluetoothdtm.html language=enus -->
## TOPIC 00027: NIBluetoothDtm Class

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm-nibluetoothdtm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm-nibluetoothdtm.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines a root class which is used to identify and control BluetoothDtm signal configuration. Derives fromIDisposableSyntaxNamespace: NationalInstruments.BluetoothDtmpublic class NIBluetoothDtm : IDisposableConstructorsNameDescriptionNIBluetoothDtm(string)Creates an NI-VISA session to the device you

### NIBluetoothDtm Class

Defines a root class which is used to identify and control BluetoothDtm signal configuration.

#### Derives from

- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.BluetoothDtm](nationalinstruments-bluetoothdtm.html)

public class NIBluetoothDtm : IDisposable

#### Constructors

| Name | Description |
| --- | --- |
| NIBluetoothDtm(string) | Creates an NI-VISA session to the device you specify through the resourceName parameter. |

#### Methods

| Name | Description |
| --- | --- |
| Close() | Closes a device session or the event object that you specify in the VISA resource name parameter. |
| ConfigureVisaSerialSettings(ushort, uint, BluetoothDtmFlowControl, BluetoothDtmStopBits, BluetoothDtmParity) | Configures the VISA serial settings for the device under test (DUT) specified by the VISA resource name parameter. |
| CreateCustomCommand(int[], int[], ref int[]) | Sends the specified custom command to the device under test (DUT). |
| Dispose() | Closes the VISA session. Call this method a number of times equal to the number of times you obtained a reference to the VISA session for a particular resource name. |
| HciLEDirectionFindingReceiverTest(int, BluetoothDtmModulationIndex, BluetoothDtmReceiverPhy, BluetoothDtmDirectionFindingMode, int, double, double, int[], out int) | Sends a command to the device under test (DUT) to start the receiver test. |
| HciLEDirectionFindingTransmitterTest(int, int, BluetoothDtmLEPatternType, BluetoothDtmTransmitterPhy, BluetoothDtmDirectionFindingMode, int, double, double, int[], out int) | Sends a command to the device under test (DUT) to start the transmitter test. |
| HciLEEnhancedReceiverTest(int, BluetoothDtmModulationIndex, BluetoothDtmReceiverPhy, out int) | Sends a command to the device under test (DUT) to start the receiver test. |
| HciLEEnhancedTransmitterTest(int, int, BluetoothDtmLEPatternType, BluetoothDtmTransmitterPhy, out int) | Sends the command to the device under test (DUT) to start the transmitter test. |
| HciLEReceiverTest(int, out int) | Sends a command to the device under test (DUT) to start the receiver test. |
| HciLETestEnd(out int, out int) | Sends the command to the device under test (DUT) to end the transmitter or receiver test. |
| HciLETransmitterTest(int, int, BluetoothDtmLEPatternType, out int) | Sends a command to the device under test (DUT) to start the transmitter test. |
| HciReadBluetoothDeviceAddress(out long, out int) | Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address. |
| HciReset(out int) | Resets the device under test (DUT) specified by the VISA resource name parameter. |
| SetVisaTimeout(uint) | Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the VISA resource name parameter. |

Parent topic:

NationalInstruments.BluetoothDtm

<!--NI_TOPIC bundle=rfmxbluetoothdtm-dotnet-api-ref path=nationalinstruments-bluetoothdtm.html language=enus -->
## TOPIC 00028: NationalInstruments.BluetoothDtm

- bundle_id: `rfmxbluetoothdtm-dotnet-api-ref`
- source_path: `nationalinstruments-bluetoothdtm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-dotnet-api-ref/raw/resource/enus/nationalinstruments-bluetoothdtm.html
- document_id: `rfmxbluetoothdtm-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionBluetoothDtmExceptionInitializes a new instance of the BluetoothDtmException class with a specified error message. NIBluetoothDtmDefines a root class which is used to identify and control BluetoothDtm signal configuration. InterfacesNoneStructuresNoneEnumerationsNameDescription

### NationalInstruments.BluetoothDtm

#### Classes

| Name | Description |
| --- | --- |
| BluetoothDtmException | Initializes a new instance of the BluetoothDtmException class with a specified error message. |
| NIBluetoothDtm | Defines a root class which is used to identify and control BluetoothDtm signal configuration. |

#### Interfaces

None

#### Structures

None

#### Enumerations

| Name | Description |
| --- | --- |
| BluetoothDtmDirectionFindingMode | Specifies the mode of direction finding. The default value is Disabled. |
| BluetoothDtmFlowControl | Specifies the flow control method used for transmitting and receiving data. The default value is RtsCts. |
| BluetoothDtmLEPatternType | Specifies the type of payload to use for the LE packet. Payload type values of Type_Prbs9, Type_11110000, and Type_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is Type_Prbs9. |
| BluetoothDtmModulationIndex | Specifies the type of modulation index at the generator. The default value is Standard. |
| BluetoothDtmParity | Specifies the parity bit used with each transmitted or received frame. The default value is None. |
| BluetoothDtmReceiverPhy | Specifies the type of the generated packet by the physical layer of the DUT. The default value is Phy_1Mbps. |
| BluetoothDtmStopBits | specifies the number of stop bits used to indicate the end of a frame. The default value is StopBits1_0. |
| BluetoothDtmTransmitterPhy | Specifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is Phy_1Mbps. |

#### Delegates

None
