# NI DOCUMENT BUNDLE: rfmx-btdtm-cvi

<!--NI_BUNDLE_CHUNK bundle=rfmx-btdtm-cvi start=1 end=16 -->
<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=bt_functions.html language=enus -->
## TOPIC 00001: Bluetooth Functions

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `bt_functions.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/bt_functions.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

Bluetooth (R) Direct Test Mode Functions

Contains functions to configure various parameters needed for generation on a signal that conforms to the Bluetooth specifications, as well as enable those measurements.

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=cvinibluetoothdtm_createcustomcommand.html language=enus -->
## TOPIC 00002: niBluetoothDTM_CreateCustomCommand

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `cvinibluetoothdtm_createcustomcommand.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/cvinibluetoothdtm_createcustomcommand.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

niBluetoothDTM_CreateCustomCommand

int32 __stdcall niBluetoothDTM_CreateCustomCommand (niBluetoothDTMSession* session,
 int32 opCode[],
 int32 opCodeLength,
 int32 commandParameters[],
 int32 commandParametersLength,
 int32 returnParameters[],
 int32 arraySize,
 int32 *actualArraySize);

#### Purpose

Sends the specified custom command to the device under test (DUT).

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| opCode | int32[] | Specifies the opcode of the custom commands to send to the DUT. |
| opCodeLength | int32 | Specifies the length of the opCode array. |
| commandParameters | int32[] | Specifies an array of the input parameters required for the custom command. |
| commandParametersLength | int32 | Specifies the length of the commandParameters array. |
| arraySize | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| Output |  |  |
| Name | Type | Description |
| returnParameters | int32[] | Returns an array of the parameters sent by the DUT in response to the custom command. |
| actualArraySize | int32* | Returns the actual size of the array, if you pass NULL to returnParameters array, and set the arraySize parameter to 0. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=cvinibluetoothdtm_hciledirectionfindingreceivertest.html language=enus -->
## TOPIC 00003: niBluetoothDTM_HCILEDirectionFindingReceiverTest

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `cvinibluetoothdtm_hciledirectionfindingreceivertest.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/cvinibluetoothdtm_hciledirectionfindingreceivertest.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

niBluetoothDTM_HCILEDirectionFindingReceiverTest

int32 __stdcall niBluetoothDTM_HCILEDirectionFindingReceiverTest(
 niBluetoothDTMSession session,
 int32 channelNumber,
 int32 modulationIndex,
 int32 PHY,
 int32 directionFindingMode,
 int32 switchingPatternLength,
 float64 CTELength,
 float64 CTESlotDuration,
 int32 antennaID[],
 int32 antennaIDArraySize,
 int32 *status);

#### Purpose

Sends the command to the device under test (DUT) to start the receiver test.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | int32 | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| modulationIndex | int32 | Specifies the type of modulation index at the generator. The default value is NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD. NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD (0) The packets are generated with standard modulation index. NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STABLE (1) The packets are generated with stable modulation index. |
| NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD (0) | The packets are generated with standard modulation index. |  |
| NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STABLE (1) | The packets are generated with stable modulation index. |  |
| PHY | int32 | Specifies the type of the generated packet by the physical layer of the DUT. The default value is NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS. NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS (0) Receiver is set to use the LE 1M PHY. NIBLUETOOTHDTM_VAL_RECEIVER_PHY_2MBPS (1) Receiver is set to use the LE 2M PHY. NIBLUETOOTHDTM_VAL_RECEIVER_PHY_CODED (2) Receiver is set to use the Coded PHY. |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS (0) | Receiver is set to use the LE 1M PHY. |  |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_2MBPS (1) | Receiver is set to use the LE 2M PHY. |  |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_CODED (2) | Receiver is set to use the Coded PHY. |  |
| directionFindingMode | int32 | Specifies the mode of direction finding. The default value is NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED. NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED (0) Specifies that the LE packet does not have fields required for direction finding. NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1) Specifies the LE packets uses the angle of arrival method of direction finding. NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2) Specifies the LE packet uses angle of departure method of direction finding. |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED (0) | Specifies that the LE packet does not have fields required for direction finding. |  |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1) | Specifies the LE packets uses the angle of arrival method of direction finding. |  |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2) | Specifies the LE packet uses angle of departure method of direction finding. |  |
| lengthOfSwitchingPattern | int32 | Specifies the length of the antenna switching pattern. The default value is 0. |
| CTELength | float64 | Specifies specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the directionFindingMode parameter to either NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE. The default value is 160 microseconds. |
| CTESlotDuration | float64 | Specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. The default value is 1 us. Valid values are 1 us and 2 us. |
| antennaID | int32[] | Specifies the array of Antenna IDs in the antenna switching pattern. The length of Antenna IDs array must be equal to Length Of Switching Pattern parameter. |
| antennaIDArraySize | int32 | Specifies size of antennaID parameter. |
| Output |  |  |
| Name | Type | Description |
| status | int32 | Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=cvinibluetoothdtm_hciledirectionfindingtransmittertest.html language=enus -->
## TOPIC 00004: niBluetoothDTM_HCILEDirectionFindingTransmitterTest

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `cvinibluetoothdtm_hciledirectionfindingtransmittertest.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/cvinibluetoothdtm_hciledirectionfindingtransmittertest.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

niBluetoothDTM_HCILEDirectionFindingTransmitterTest

int32 __stdcall niBluetoothDTM_HCILEDirectionFindingTransmitterTest(
 niBluetoothDTMSession session,
 int32 channelNumber,
 int32 payloadLength,
 int32 LEPatternType,
 int32 PHY,
 int32 directionFindingMode,
 int32 switchingPatternLength,
 float64 CTELength,
 float64 CTESlotDuration,
 int32 antennaID[],
 int32 antennaIDArraySize,
 int32 *status);

#### Purpose

Sends the command to the device under test (DUT) to start the transmitter test.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | int32 | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| payloadLength | int32 | Specifies the length of payload data in each packet that the DUT transmits. This value is expressed in bytes. The default value is 37. |
| LEPatternType | int32 | Specifies the type of payload to use for the LE packet. Payload type values of NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9, NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000, and NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) Specifies that the bit sequence is PRBS9. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) Specifies that the bit sequence is 11110000. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) Specifies that the bit sequence is 10101010. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) Specifies that the bit sequence is PRBS15. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) Specifies that the bit sequence is 11111111. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) Specifies that the bit sequence is 00000000. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) Specifies that the bit sequence is 00001111. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) Specifies that the bit sequence is 01010101. |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) | Specifies that the bit sequence is PRBS9. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) | Specifies that the bit sequence is 11110000. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) | Specifies that the bit sequence is 10101010. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) | Specifies that the bit sequence is PRBS15. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) | Specifies that the bit sequence is 11111111. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) | Specifies that the bit sequence is 00000000. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) | Specifies that the bit sequence is 00001111. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) | Specifies that the bit sequence is 01010101. |  |
| PHY | int32 | Specifies the type of the packet to be transmitted by the physical layer of the DUT. The default is NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS (0) Transmitter is set to use the LE 1M PHY. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_2MBPS (1) Transmitter is set to use the LE 2M PHY. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_125KBPS (2) Transmitter is set to use the LE Coded PHY with S = 8 data coding. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_500KBPS (3) Transmitter is set to use the LE Coded PHY with S = 2 data coding. |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS (0) | Transmitter is set to use the LE 1M PHY. |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_2MBPS (1) | Transmitter is set to use the LE 2M PHY. |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_125KBPS (2) | Transmitter is set to use the LE Coded PHY with S = 8 data coding. |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_500KBPS (3) | Transmitter is set to use the LE Coded PHY with S = 2 data coding. |  |
| directionFindingMode | int32 | Specifies the mode of direction finding. The default value is NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED. NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED (0) Specifies that the LE packet does not have fields required for direction finding. NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1) Specifies the LE packets uses the angle of arrival method of direction finding. NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2) Specifies the LE packet uses angle of departure method of direction finding. |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED (0) | Specifies that the LE packet does not have fields required for direction finding. |  |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1) | Specifies the LE packets uses the angle of arrival method of direction finding. |  |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2) | Specifies the LE packet uses angle of departure method of direction finding. |  |
| switchingPatternLength | int32 | Specifies the length of the antenna switching pattern. The default value is 0. |
| CTELength | float64 | Specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the directionFindingMode parameter to either NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE. The default value is 160 microseconds. |
| CTESlotDuration | float64 | Specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. The default value is 1 us. |
| antennaID | int32[] | Specifies the array of Antenna IDs in the antenna switching pattern. The length of Antenna IDs array must be equal to length of the switching pattern. |
| antennaIDArraySize | int32 | Specifies the size of the array. |
| Output |  |  |
| Name | Type | Description |
| status | int32 | Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=cvinibluetoothdtm_hcileenhancedreceivertest.html language=enus -->
## TOPIC 00005: niBluetoothDTM_HCILEEnhancedReceiverTest

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `cvinibluetoothdtm_hcileenhancedreceivertest.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/cvinibluetoothdtm_hcileenhancedreceivertest.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

niBluetoothDTM_HCILEEnhancedReceiverTest

int32 __stdcall niBluetoothDTM_HCILEEnhancedReceiverTest(
 niBluetoothDTMSession session,
 int32 channelNumber,
 int32 modulationIndex,
 int32 PHY,
 int32 *status);

#### Purpose

Sends the command to the device under test (DUT) to start the receiver test.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | int32 | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| modulationIndex | int32 | Specifies the type of modulation index at the generator. The default value is NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD. NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD (0) The packets are generated with standard modulation index. NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STABLE (1) The packets are generated with stable modulation index. |
| NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD (0) | The packets are generated with standard modulation index. |  |
| NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STABLE (1) | The packets are generated with stable modulation index. |  |
| PHY | int32 | Specifies the type of the generated packet by the physical layer of the DUT. The default value is NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS. NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS (0) Receiver is set to use the LE 1M PHY. NIBLUETOOTHDTM_VAL_RECEIVER_PHY_2MBPS (1) Receiver is set to use the LE 2M PHY. NIBLUETOOTHDTM_VAL_RECEIVER_PHY_CODED (2) Receiver is set to use the Coded PHY. |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS (0) | Receiver is set to use the LE 1M PHY. |  |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_2MBPS (1) | Receiver is set to use the LE 2M PHY. |  |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_CODED (2) | Receiver is set to use the Coded PHY. |  |
| Output |  |  |
| Name | Type | Description |
| status | int32 | Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=cvinibluetoothdtm_hcileenhancedtransmittertest.html language=enus -->
## TOPIC 00006: niBluetoothDTM_HCILEEnhancedTransmitterTest

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `cvinibluetoothdtm_hcileenhancedtransmittertest.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/cvinibluetoothdtm_hcileenhancedtransmittertest.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

niBluetoothDTM_HCILEEnhancedTransmitterTest

int32 __stdcall niBluetoothDTM_HCILEEnhancedTransmitterTest(
 niBluetoothDTMSession session,
 int32 channelNumber,
 int32 payloadLengthBytes,
 int32 LEPatternType,
 int32 PHY,
 int32 *status);

#### Purpose

Sends the command to the device under test (DUT) to start the transmitter test.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | int32 | Specifies the Bluetooth transmit channel number of the signal generated by the DUT. The default value is 0. |
| payloadLengthBytes | int32 | Specifies the length, in bytes, of payload data in each packet that the DUT transmits. The default value is 37. |
| LEPatternType | int32 | Specifies the type of payload to use for the LE packet. Payload type values of NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9, NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000, and NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) Specifies that the bit sequence is PRBS9. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) Specifies that the bit sequence is 11110000. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) Specifies that the bit sequence is 10101010. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) Specifies that the bit sequence is PRBS15. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) Specifies that the bit sequence is 11111111. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) Specifies that the bit sequence is 00000000. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) Specifies that the bit sequence is 00001111. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) Specifies that the bit sequence is 01010101. |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) | Specifies that the bit sequence is PRBS9. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) | Specifies that the bit sequence is 11110000. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) | Specifies that the bit sequence is 10101010. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) | Specifies that the bit sequence is PRBS15. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) | Specifies that the bit sequence is 11111111. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) | Specifies that the bit sequence is 00000000. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) | Specifies that the bit sequence is 00001111. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) | Specifies that the bit sequence is 01010101. |  |
| PHY | int32 | Specifies the type of the packet to be transmitted by the physical layer of the DUT. The default is NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS (0) Transmitter is set to use the LE 1M PHY. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_2MBPS (1) Transmitter is set to use the LE 2M PHY. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_125KBPS (2) Transmitter is set to use the LE Coded PHY with S = 8 data coding. NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_500KBPS (3) Transmitter is set to use the LE Coded PHY with S = 2 data coding. |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS (0) | Transmitter is set to use the LE 1M PHY. |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_2MBPS (1) | Transmitter is set to use the LE 2M PHY. |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_125KBPS (2) | Transmitter is set to use the LE Coded PHY with S = 8 data coding. |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_500KBPS (3) | Transmitter is set to use the LE Coded PHY with S = 2 data coding. |  |
| Output |  |  |
| Name | Type | Description |
| status | int32 | Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=cvinibluetoothdtm_hcilereceivertest.html language=enus -->
## TOPIC 00007: niBluetoothDTM_HCILEReceiverTest

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `cvinibluetoothdtm_hcilereceivertest.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/cvinibluetoothdtm_hcilereceivertest.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

niBluetoothDTM_HCILEReceiverTest

int32 __stdcall niBluetoothDTM_HCILEReceiverTest (niBluetoothDTMSession* session, 
 int32 channelNumber,
 int32 *status);

#### Purpose

Sends the command to the device under test (DUT) to start the receiver test.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | int32 | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| Output |  |  |
| Name | Type | Description |
| status | int32* | Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=cvinibluetoothdtm_hciletestend.html language=enus -->
## TOPIC 00008: niBluetoothDTM_HCILETestEnd

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `cvinibluetoothdtm_hciletestend.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/cvinibluetoothdtm_hciletestend.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

niBluetoothDTM_HCILETestEnd

int32 __stdcall niBluetoothDTM_HCILETestEnd (niBluetoothDTMSession* session,
 int32* packetCount,
 int32* status);

#### Purpose

Sends the command to the DUT to end the transmitter or the receiver test.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| Output |  |  |
| Name | Type | Description |
| packetCount | int32* | Returns the number of packets received by the DUT. |
| status | int32* | Returns the status of the test end command. The DUT receives and executes the test end command if the status parameter returns a 0x00 value. The test end command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=cvinibluetoothdtm_hciletransmittertest.html language=enus -->
## TOPIC 00009: niBluetoothDTM_HCILEReceiverTest

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `cvinibluetoothdtm_hciletransmittertest.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/cvinibluetoothdtm_hciletransmittertest.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

niBluetoothDTM_HCILETransmitterTest

int32 __stdcall niBluetoothDTM_HCILETransmitterTest (niBluetoothDTMSession* session,
 int32 channelNumber,
 int32 payloadLengthBytes,
 int32 LEPatternType,
 int32 *status);

#### Purpose

Sends the command to the device under test (DUT) to start the transmitter test.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | int32 | Specifies the Bluetooth transmit channel number of the signal generated by the DUT. The default value is 0. |
| payloadLengthBytes | int32 | Specifies the length, in bytes, of payload data in each packet that the DUT transmits. The default value is 37. |
| LEPatternType | int32 | Specifies the type of payload to use for the LE packet. Payload type values of NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9, NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000, and NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) Specifies that the bit sequence is PRBS9. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) Specifies that the bit sequence is 11110000. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) Specifies that the bit sequence is 10101010. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) Specifies that the bit sequence is PRBS15. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) Specifies that the bit sequence is 11111111. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) Specifies that the bit sequence is 00000000. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) Specifies that the bit sequence is 00001111. NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) Specifies that the bit sequence is 01010101. |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) | Specifies that the bit sequence is PRBS9. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) | Specifies that the bit sequence is 11110000. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) | Specifies that the bit sequence is 10101010. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) | Specifies that the bit sequence is PRBS15. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) | Specifies that the bit sequence is 11111111. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) | Specifies that the bit sequence is 00000000. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) | Specifies that the bit sequence is 00001111. |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) | Specifies that the bit sequence is 01010101. |  |
| Output |  |  |
| Name | Type | Description |
| status | int32 | Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=cvinibluetoothdtm_hcireadbd_addr.html language=enus -->
## TOPIC 00010: niBluetoothDTM_HCIReadBD_ADDR

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `cvinibluetoothdtm_hcireadbd_addr.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/cvinibluetoothdtm_hcireadbd_addr.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

niBluetoothDTM_HCIReadBD_ADDR

int32 __stdcall niBluetoothDTM_HCIReadBD_ADDR (niBluetoothDTMSession* session,
 int64 *BDAddress,
 int32 *status);

#### Purpose

Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| Output |  |  |
| Name | Type | Description |
| BDAddress | int64* | Returns the BD address of the DUT. |
| status | int32* | Returns the status of the read BD_ADDR command. The DUT receives and executes the read BD_ADDR command if the status parameter returns a 0x00 value. The read BD_ADDR command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=cvinibluetoothdtm_hcireset.html language=enus -->
## TOPIC 00011: niBluetoothDTM_HCIReset

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `cvinibluetoothdtm_hcireset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/cvinibluetoothdtm_hcireset.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

niBluetoothDTM_HCIReset

int32 __stdcall niBluetoothDTM_HCIReset (niBluetoothDTMSession* session,
 int32 *status);

#### Purpose

Resets the device under test (DUT) specified by the **session** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| Output |  |  |
| Name | Type | Description |
| status | int32 | Returns the status of the reset command. The DUT receives and executes the reset command if the status parameter returns a 0x00 value. The reset command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=cvinibluetoothdtm_visaclosesession.html language=enus -->
## TOPIC 00012: niBluetoothDTM_VISACloseSession

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `cvinibluetoothdtm_visaclosesession.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/cvinibluetoothdtm_visaclosesession.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

niBluetoothDTM_VISACloseSession

int32 __stdcall niBluetoothDTM_VISACloseSession (niBluetoothDTMSession* session);

#### Purpose

Closes a device session or the event object that you specify in the **session** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=cvinibluetoothdtm_visaconfigureserialsettings.html language=enus -->
## TOPIC 00013: niBluetoothDTM_VISAConfigureSerialSettings

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `cvinibluetoothdtm_visaconfigureserialsettings.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/cvinibluetoothdtm_visaconfigureserialsettings.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

niBluetoothDTM_VISAConfigureSerialSettings

int32 __stdcall niBluetoothDTM_VISAConfigureSerialSettings (niBluetoothDTMSession *session,
 uInt16 dataBits,
 uInt32 baudRate,
 uInt16 flowControl,
 uInt16 stopBits,
 uInt16 parity);

#### Purpose

Configures the VISA serial settings for the device under test (DUT) specified by the **session** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| dataBits | uInt16 | Specifies the number of data bits contained in each frame. Valid values are 5 to 8, inclusive. The data bits for each frame are located in the low-order bits of every byte stored in the memory. The default value is 8. |
| baudRate | uInt32 | Specifies the baud rate of the given communication port. The default value is 115,200. |
| flowControl | int32 | specifies the flow control method used for transmitting and receiving data. The default value is RTS/CTS. NIBLUETOOTHDTM_VAL_FLOW_CONTROL_NONE (0) Does not use flow control, and the buffers on both sides of the connection are assumed to be large enough to hold all the transferred data. NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF (1) Uses the XON and XOFF characters to complete flow control. The transfer mechanism controls input flow by transmitting XOFF when the low-level I/O receive buffer is nearly full, and it controls the output flow by suspending transmission when XOFF is received. NIBLUETOOTHDTM_VAL_FLOW_CONTROL_RTS_CTS (2) Uses the RTS output signal and the CTS input signal to complete flow control. The transfer mechanism controls input flow by unasserting the RTS signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the CTS signal is unasserted. NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF_AND_RTS_CTS (3) Uses values of XON/XOFF and RTS/CTS. NIBLUETOOTHDTM_VAL_FLOW_CONTROL_DTR_DSR (4) Uses the DTR output signal and the DSR input signal to complete flow control. The transfer mechanism controls input flow by unasserting the DTR signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the DSR signal is unasserted. NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF_AND_DTR_DSR (5) Uses values of XON/XOFF and DTR/DSR. |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_NONE (0) | Does not use flow control, and the buffers on both sides of the connection are assumed to be large enough to hold all the transferred data. |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF (1) | Uses the XON and XOFF characters to complete flow control. The transfer mechanism controls input flow by transmitting XOFF when the low-level I/O receive buffer is nearly full, and it controls the output flow by suspending transmission when XOFF is received. |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_RTS_CTS (2) | Uses the RTS output signal and the CTS input signal to complete flow control. The transfer mechanism controls input flow by unasserting the RTS signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the CTS signal is unasserted. |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF_AND_RTS_CTS (3) | Uses values of XON/XOFF and RTS/CTS. |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_DTR_DSR (4) | Uses the DTR output signal and the DSR input signal to complete flow control. The transfer mechanism controls input flow by unasserting the DTR signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the DSR signal is unasserted. |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF_AND_DTR_DSR (5) | Uses values of XON/XOFF and DTR/DSR. |  |
| stopBits | uInt16 | Specifies the number of stop bits used to indicate the end of a frame. The default value is 1.0. |
| parity | uInt16 | Specifies the parity bit used with each transmitted or received frame. The default value is NIBLUETOOTHDTM_VAL_PARITY_NONE. NIBLUETOOTHDTM_VAL_PARITY_NONE (0) Specifies that the frame does not contain a parity bit. NIBLUETOOTHDTM_VAL_PARITY_ODD (1) Specifies that the parity is odd. NIBLUETOOTHDTM_VAL_PARITY_EVEN (2) Specifies that the parity is even. NIBLUETOOTHDTM_VAL_PARITY_MARK (3) Specifies that the parity bit is always 1. NIBLUETOOTHDTM_VAL_PARITY_SPACE (4) Specifies that the parity bit is always 0. |
| NIBLUETOOTHDTM_VAL_PARITY_NONE (0) | Specifies that the frame does not contain a parity bit. |  |
| NIBLUETOOTHDTM_VAL_PARITY_ODD (1) | Specifies that the parity is odd. |  |
| NIBLUETOOTHDTM_VAL_PARITY_EVEN (2) | Specifies that the parity is even. |  |
| NIBLUETOOTHDTM_VAL_PARITY_MARK (3) | Specifies that the parity bit is always 1. |  |
| NIBLUETOOTHDTM_VAL_PARITY_SPACE (4) | Specifies that the parity bit is always 0. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=cvinibluetoothdtm_visaopensession.html language=enus -->
## TOPIC 00014: niBluetoothDTM_VISAOpenSession

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `cvinibluetoothdtm_visaopensession.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/cvinibluetoothdtm_visaopensession.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

niBluetoothDTM_VISAOpenSession

int32 __stdcall niBluetoothDTM_VISAOpenSession (char session[],
 niBluetoothDTMSession* sessionOut);

#### Purpose

Opens a session of the device under test (DUT) specified by the **session** parameter, and returns a session identifier that can be used to call any other operations on that DUT.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | char[] | Specifies the name of the communication port to which the DUT is connected. |
| Output |  |  |
| Name | Type | Description |
| sessionOut | niBluetoothDTMSession* | Returns the name of the communication port to which the DUT is connected. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=cvinibluetoothdtm_visasettimeout.html language=enus -->
## TOPIC 00015: niBluetoothDTM_VISASetTimeout

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `cvinibluetoothdtm_visasettimeout.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/cvinibluetoothdtm_visasettimeout.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

niBluetoothDTM_VISASetTimeout

int32 __stdcall niBluetoothDTM_VISASetTimeout (niBluetoothDTMSession *session,
 uInt32 timeout);

#### Purpose

Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the **session** parameter.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| session | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| timeout | uInt32 | Specifies the minimum timeout value, in milliseconds (ms), to use when accessing the device. The default value is 2,000. Note The actual timeout that VISA returns may be higher than the specified timeout. |
|  | Note | The actual timeout that VISA returns may be higher than the specified timeout. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| returnValue | int32 | Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |
|  |  |  |

<!--NI_TOPIC bundle=rfmx-btdtm-cvi path=help_file_title.html language=enus -->
## TOPIC 00016: Bluetooth (R) Direct Test Mode C Reference

- bundle_id: `rfmx-btdtm-cvi`
- source_path: `help_file_title.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-btdtm-cvi/raw/resource/enus/help_file_title.html
- document_id: `rfmx-btdtm-cvi`
- page_type: `leaf`
- content_type: ``

Bluetooth (R) Direct Test Mode C Reference

This help file contains information about the Bluetooth(R) Direct Test Mode generation functions that you can use when programming your application.
