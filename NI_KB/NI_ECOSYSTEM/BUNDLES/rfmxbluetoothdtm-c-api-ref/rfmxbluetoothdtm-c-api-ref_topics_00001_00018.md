# NI DOCUMENT BUNDLE: rfmxbluetoothdtm-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxbluetoothdtm-c-api-ref start=1 end=18 -->
<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__attributes.html language=enus -->
## TOPIC 00001: Attributes

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__attributes.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNoneAttachmentsNone

### Attributes

#### Groups

None

#### Group members

None

#### Attachments

None

Parent topic:

niBluetoothDTM.h

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions.html language=enus -->
## TOPIC 00002: Functions

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniBluetoothDTM_CloseVISASessionCloses a device session or the event object that you specify in the session parameter. niBluetoothDTM_ConfigureVISASerialSettingsConfigures the VISA serial settings for the device under test (DUT) specified by the session parameter

### Functions

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niBluetoothDTM_CloseVISASession | Closes a device session or the event object that you specify in the session parameter. |
| niBluetoothDTM_ConfigureVISASerialSettings | Configures the VISA serial settings for the device under test (DUT) specified by the session parameter. |
| niBluetoothDTM_CreateCustomCommand | Sends the specified custom command to the device under test (DUT). |
| niBluetoothDTM_GetErrorString | Takes the error code returned by niBluetoothDTM generation functions and returns the interpretation as a user-readable string. |
| niBluetoothDTM_HCILEDirectionFindingReceiverTest | Sends the command to the device under test (DUT) to start the receiver test. |
| niBluetoothDTM_HCILEDirectionFindingTransmitterTest | Sends the command to the device under test (DUT) to start the transmitter test. |
| niBluetoothDTM_HCILEEnhancedReceiverTest | Sends the command to the device under test (DUT) to start the receiver test. |
| niBluetoothDTM_HCILEEnhancedTransmitterTest | Sends the command to the device under test (DUT) to start the transmitter test. |
| niBluetoothDTM_HCILEReceiverTest | Sends the command to the device under test (DUT) to start the receiver test. |
| niBluetoothDTM_HCILETestEnd | Sends the command to the DUT to end the transmitter or the receiver test. |
| niBluetoothDTM_HCILETransmitterTest | Sends the command to the device under test (DUT) to start the transmitter test. |
| niBluetoothDTM_HCIReadBD_Addr | Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address. |
| niBluetoothDTM_HCIReset | Resets the device under test (DUT) specified by the session parameter. |
| niBluetoothDTM_OpenVISASession | Opens a session of the device under test (DUT) specified by the session parameter, and returns a session identifier that can be used to call any other operations on that DUT. |
| niBluetoothDTM_SetVISATimeout | Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the session parameter. |

#### Attachments

None

Parent topic:

niBluetoothDTM.h

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1ga1aa61ca97005dc535bab42403ebb6d2f.html language=enus -->
## TOPIC 00003: niBluetoothDTM_HCILEEnhancedTransmitterTest

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1ga1aa61ca97005dc535bab42403ebb6d2f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1ga1aa61ca97005dc535bab42403ebb6d2f.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the device under test (DUT) to start the transmitter test. Syntaxint32 __stdcall niBluetoothDTM_HCILEEnhancedTransmitterTest(niBluetoothDTMSession session, int32 channelNumber, int32 payloadLengthBytes, int32 lePatternType, int32 phy, int32 status)ParametersNameDirectionTypeDesc

### niBluetoothDTM_HCILEEnhancedTransmitterTest

Sends the command to the device under test (DUT) to start the transmitter test.

#### Syntax

int32 __stdcall niBluetoothDTM_HCILEEnhancedTransmitterTest(niBluetoothDTMSession session, int32 channelNumber, int32 payloadLengthBytes, int32 lePatternType, int32 phy, int32 status)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | [in] | int32 | Specifies the Bluetooth transmit channel number of the signal generated by the DUT. The default value is 0. |
| payloadLengthBytes | [in] | int32 | Specifies the length, in bytes, of payload data in each packet that the DUT transmits. The default value is 37. |
| lePatternType | [in] | int32 | Specifies the type of payload to use for the LE packet. Payload type values of NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9, NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000, and NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0)Specifies that the bit sequence is PRBS9.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1)Specifies that the bit sequence is 11110000.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2)Specifies that the bit sequence is 10101010.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3)Specifies that the bit sequence is PRBS15.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4)Specifies that the bit sequence is 11111111.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5)Specifies that the bit sequence is 00000000.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6)Specifies that the bit sequence is 00001111.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7)Specifies that the bit sequence is 01010101. |
|  |  |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) | Specifies that the bit sequence is PRBS9. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) | Specifies that the bit sequence is 11110000. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) | Specifies that the bit sequence is 10101010. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) | Specifies that the bit sequence is PRBS15. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) | Specifies that the bit sequence is 11111111. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) | Specifies that the bit sequence is 00000000. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) | Specifies that the bit sequence is 00001111. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) | Specifies that the bit sequence is 01010101. |  |  |
| phy | [in] | int32 | Specifies the type of the packet to be transmitted by the physical layer of the DUT. The default is NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS.NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS (0)Transmitter is set to use the LE 1M PHY.NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_2MBPS (1)Transmitter is set to use the LE 2M PHY.NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_125KBPS (2)Transmitter is set to use the LE Coded PHY with S = 8 data coding.NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_500KBPS (3)Transmitter is set to use the LE Coded PHY with S = 2 data coding. |
|  |  |  |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS (0) | Transmitter is set to use the LE 1M PHY. |  |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_2MBPS (1) | Transmitter is set to use the LE 2M PHY. |  |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_125KBPS (2) | Transmitter is set to use the LE Coded PHY with S = 8 data coding. |  |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_500KBPS (3) | Transmitter is set to use the LE Coded PHY with S = 2 data coding. |  |  |
| status | [out] | int32 | Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1ga3ddf724fe3e2094934f1ecbe8e5e9516.html language=enus -->
## TOPIC 00004: niBluetoothDTM_HCIReset

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1ga3ddf724fe3e2094934f1ecbe8e5e9516.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1ga3ddf724fe3e2094934f1ecbe8e5e9516.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the device under test (DUT) specified by the session parameter. Syntaxint32 __stdcall niBluetoothDTM_HCIReset(niBluetoothDTMSession session, int32 status)ParametersNameDirectionTypeDescriptionsession[out]niBluetoothDTMSessionSpecifies the name of the communication port to which the DUT is con

### niBluetoothDTM_HCIReset

Resets the device under test (DUT) specified by the **session** parameter.

#### Syntax

int32 __stdcall niBluetoothDTM_HCIReset(niBluetoothDTMSession session, int32 status)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| status | [out] | int32 | Returns the status of the reset command. The DUT receives and executes the reset command if the status parameter returns a 0x00 value. The reset command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1ga4caaca982ee94ffd8211c95191b2949a.html language=enus -->
## TOPIC 00005: niBluetoothDTM_HCILEDirectionFindingTransmitterTest

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1ga4caaca982ee94ffd8211c95191b2949a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1ga4caaca982ee94ffd8211c95191b2949a.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the device under test (DUT) to start the transmitter test. Syntaxint32 __stdcall niBluetoothDTM_HCILEDirectionFindingTransmitterTest(niBluetoothDTMSession session, int32 channelNumber, int32 payloadLength, int32 lePatternType, int32 phy, int32 directionFindingMode, int32 switchi

### niBluetoothDTM_HCILEDirectionFindingTransmitterTest

Sends the command to the device under test (DUT) to start the transmitter test.

#### Syntax

int32 __stdcall niBluetoothDTM_HCILEDirectionFindingTransmitterTest(niBluetoothDTMSession session, int32 channelNumber, int32 payloadLength, int32 lePatternType, int32 phy, int32 directionFindingMode, int32 switchingPatternLength, float64 cteLength, float64 cteSlotDuration, int32[] antennaID, int32 antennaIDArraySize, int32 status)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | [in] | int32 | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| payloadLength | [in] | int32 | Specifies the length of payload data in each packet that the DUT transmits. This value is expressed in bytes. The default value is 37. |
| lePatternType | [in] | int32 | Specifies the type of payload to use for the LE packet. Payload type values of NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9, NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000, and NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0)Specifies that the bit sequence is PRBS9.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1)Specifies that the bit sequence is 11110000.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2)Specifies that the bit sequence is 10101010.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3)Specifies that the bit sequence is PRBS15.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4)Specifies that the bit sequence is 11111111.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5)Specifies that the bit sequence is 00000000.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6)Specifies that the bit sequence is 00001111.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7)Specifies that the bit sequence is 01010101. |
|  |  |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) | Specifies that the bit sequence is PRBS9. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) | Specifies that the bit sequence is 11110000. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) | Specifies that the bit sequence is 10101010. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) | Specifies that the bit sequence is PRBS15. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) | Specifies that the bit sequence is 11111111. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) | Specifies that the bit sequence is 00000000. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) | Specifies that the bit sequence is 00001111. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) | Specifies that the bit sequence is 01010101. |  |  |
| phy | [in] | int32 | Specifies the type of the packet to be transmitted by the physical layer of the DUT. The default is NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS.NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS (0)Transmitter is set to use the LE 1M PHY.NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_2MBPS (1)Transmitter is set to use the LE 2M PHY.NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_125KBPS (2)Transmitter is set to use the LE Coded PHY with S = 8 data coding.NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_500KBPS (3)Transmitter is set to use the LE Coded PHY with S = 2 data coding. |
|  |  |  |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_1MBPS (0) | Transmitter is set to use the LE 1M PHY. |  |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_2MBPS (1) | Transmitter is set to use the LE 2M PHY. |  |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_125KBPS (2) | Transmitter is set to use the LE Coded PHY with S = 8 data coding. |  |  |
| NIBLUETOOTHDTM_VAL_TRANSMITTER_PHY_CODED_500KBPS (3) | Transmitter is set to use the LE Coded PHY with S = 2 data coding. |  |  |
| directionFindingMode | [in] | int32 | Specifies the mode of direction finding. The default value is NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED.NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED (0)Specifies that the LE packet does not have fields required for direction finding.NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1)Specifies the LE packets uses the angle of arrival method of direction finding.NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2)Specifies the LE packet uses angle of departure method of direction finding. |
|  |  |  |  |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED (0) | Specifies that the LE packet does not have fields required for direction finding. |  |  |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1) | Specifies the LE packets uses the angle of arrival method of direction finding. |  |  |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2) | Specifies the LE packet uses angle of departure method of direction finding. |  |  |
| switchingPatternLength | [in] | int32 | Specifies the length of the antenna switching pattern. The default value is 0. |
| cteLength | [in] | float64 | Specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the directionFindingMode parameter to either NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE. The default value is 160 microseconds. |
| cteSlotDuration | [in] | float64 | Specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. The default value is 1 us. |
| antennaID | [in] | int32[] | Specifies the array of Antenna IDs in the antenna switching pattern. The length of Antenna IDs array must be equal to length of the switching pattern. |
| antennaIDArraySize | [in] | int32 | Specifies the size of the array. |
| status | [out] | int32 | Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1ga59fef08db6f989701050833595a0b45b.html language=enus -->
## TOPIC 00006: niBluetoothDTM_HCIReadBD_Addr

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1ga59fef08db6f989701050833595a0b45b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1ga59fef08db6f989701050833595a0b45b.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address. Syntaxint32 __stdcall niBluetoothDTM_HCIReadBD_Addr(niBluetoothDTMSession session, int64_t bdAddress, int32 status)ParametersNameDirectionTypeDescriptionsession[out]niBluetoothDTMSessionSpecifies the name of t

### niBluetoothDTM_HCIReadBD_Addr

Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address.

#### Syntax

int32 __stdcall niBluetoothDTM_HCIReadBD_Addr(niBluetoothDTMSession session, int64_t bdAddress, int32 status)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| bdAddress | [out] | int64_t | Returns the BD address of the DUT. |
| status | [out] | int32 | Returns the status of the read BD_ADDR command. The DUT receives and executes the read BD_ADDR command if the status parameter returns a 0x00 value. The read BD_ADDR command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1ga6a71594b0e5ca392847ff566d1a85dcd.html language=enus -->
## TOPIC 00007: niBluetoothDTM_GetErrorString

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1ga6a71594b0e5ca392847ff566d1a85dcd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1ga6a71594b0e5ca392847ff566d1a85dcd.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Takes the error code returned by niBluetoothDTM generation functions and returns the interpretation as a user-readable string. Syntaxint32 __stdcall niBluetoothDTM_GetErrorString(niBluetoothDTMSession session, int32 errorCode, char[] errorMessage, int32 errorMessageLen)ParametersNameDirectionTypeDes

### niBluetoothDTM_GetErrorString

Takes the error code returned by niBluetoothDTM generation functions and returns the interpretation as a user-readable string.

#### Syntax

int32 __stdcall niBluetoothDTM_GetErrorString(niBluetoothDTMSession session, int32 errorCode, char[] errorMessage, int32 errorMessageLen)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBluetoothDTMSession | Specifies the niBluetoothDTM generation session. |
| errorCode | [in] | int32 | Specifies the error code that is returned from any of the niBluetoothDTM generation functions. |
| errorMessage | [out] | char[] | Returns the user-readable message string that corresponds to the error code you specify. The errorMessage buffer must have at least as many elements as are indicated in the errorMessageLen parameter. If you pass NULL to the errorMessage parameter, the function returns the actual length of the error message. |
| errorMessageLen | [in] | int32 | Specifies the length of the errorMessage buffer. |

#### Returns

Returns the number of characters written in **errorMessage** buffer.

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1ga6db6d93c656917787c71dbede5dd17bd.html language=enus -->
## TOPIC 00008: niBluetoothDTM_HCILETransmitterTest

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1ga6db6d93c656917787c71dbede5dd17bd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1ga6db6d93c656917787c71dbede5dd17bd.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the device under test (DUT) to start the transmitter test. Syntaxint32 __stdcall niBluetoothDTM_HCILETransmitterTest(niBluetoothDTMSession session, int32 channelNumber, int32 payloadLengthBytes, int32 lePatternType, int32 status)ParametersNameDirectionTypeDescriptionsession[out]

### niBluetoothDTM_HCILETransmitterTest

Sends the command to the device under test (DUT) to start the transmitter test.

#### Syntax

int32 __stdcall niBluetoothDTM_HCILETransmitterTest(niBluetoothDTMSession session, int32 channelNumber, int32 payloadLengthBytes, int32 lePatternType, int32 status)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | [in] | int32 | Specifies the Bluetooth transmit channel number of the signal generated by the DUT. The default value is 0. |
| payloadLengthBytes | [in] | int32 | Specifies the length, in bytes, of payload data in each packet that the DUT transmits. The default value is 37. |
| lePatternType | [in] | int32 | Specifies the type of payload to use for the LE packet. Payload type values of NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9, NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000, and NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 must be supported by the DUT. The remaining payload type values are optional. The default value is NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0)Specifies that the bit sequence is PRBS9.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1)Specifies that the bit sequence is 11110000.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2)Specifies that the bit sequence is 10101010.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3)Specifies that the bit sequence is PRBS15.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4)Specifies that the bit sequence is 11111111.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5)Specifies that the bit sequence is 00000000.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6)Specifies that the bit sequence is 00001111.NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7)Specifies that the bit sequence is 01010101. |
|  |  |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS9 (0) | Specifies that the bit sequence is PRBS9. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11110000 (1) | Specifies that the bit sequence is 11110000. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_10101010 (2) | Specifies that the bit sequence is 10101010. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_PRBS15 (3) | Specifies that the bit sequence is PRBS15. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_11111111 (4) | Specifies that the bit sequence is 11111111. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00000000 (5) | Specifies that the bit sequence is 00000000. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_00001111 (6) | Specifies that the bit sequence is 00001111. |  |  |
| NIBLUETOOTHDTM_VAL_LE_PATTERN_TYPE_01010101 (7) | Specifies that the bit sequence is 01010101. |  |  |
| status | [out] | int32 | Returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1ga6dedbad422bad3e731484fffc9355cd0.html language=enus -->
## TOPIC 00009: niBluetoothDTM_HCILEEnhancedReceiverTest

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1ga6dedbad422bad3e731484fffc9355cd0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1ga6dedbad422bad3e731484fffc9355cd0.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the device under test (DUT) to start the receiver test. Syntaxint32 __stdcall niBluetoothDTM_HCILEEnhancedReceiverTest(niBluetoothDTMSession session, int32 channelNumber, int32 modulationIndex, int32 phy, int32 status)ParametersNameDirectionTypeDescriptionsession[out]niBluetooth

### niBluetoothDTM_HCILEEnhancedReceiverTest

Sends the command to the device under test (DUT) to start the receiver test.

#### Syntax

int32 __stdcall niBluetoothDTM_HCILEEnhancedReceiverTest(niBluetoothDTMSession session, int32 channelNumber, int32 modulationIndex, int32 phy, int32 status)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | [in] | int32 | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| modulationIndex | [in] | int32 | Specifies the type of modulation index at the generator. The default value is NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD.NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD (0)The packets are generated with standard modulation index.NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STABLE (1)The packets are generated with stable modulation index. |
|  |  |  |  |
| NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD (0) | The packets are generated with standard modulation index. |  |  |
| NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STABLE (1) | The packets are generated with stable modulation index. |  |  |
| phy | [in] | int32 | Specifies the type of the generated packet by the physical layer of the DUT. The default value is NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS.NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS (0)Receiver is set to use the LE 1M PHY.NIBLUETOOTHDTM_VAL_RECEIVER_PHY_2MBPS (1)Receiver is set to use the LE 2M PHY.NIBLUETOOTHDTM_VAL_RECEIVER_PHY_CODED (2)Receiver is set to use the Coded PHY. |
|  |  |  |  |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS (0) | Receiver is set to use the LE 1M PHY. |  |  |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_2MBPS (1) | Receiver is set to use the LE 2M PHY. |  |  |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_CODED (2) | Receiver is set to use the Coded PHY. |  |  |
| status | [out] | int32 | Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1ga7b42a66c21dac47d589af43f35be5649.html language=enus -->
## TOPIC 00010: niBluetoothDTM_OpenVISASession

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1ga7b42a66c21dac47d589af43f35be5649.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1ga7b42a66c21dac47d589af43f35be5649.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a session of the device under test (DUT) specified by the session parameter, and returns a session identifier that can be used to call any other operations on that DUT. Syntaxint32 __stdcall niBluetoothDTM_OpenVISASession(char[] session, niBluetoothDTMSession sessionOut)ParametersNameDirection

### niBluetoothDTM_OpenVISASession

Opens a session of the device under test (DUT) specified by the **session** parameter, and returns a session identifier that can be used to call any other operations on that DUT.

#### Syntax

int32 __stdcall niBluetoothDTM_OpenVISASession(char[] session, niBluetoothDTMSession sessionOut)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | char[] | Specifies the name of the communication port to which the DUT is connected. |
| sessionOut | [out] | niBluetoothDTMSession | Returns the name of the communication port to which the DUT is connected. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1ga8892502f7aebf2b8866c92e14de63553.html language=enus -->
## TOPIC 00011: niBluetoothDTM_CloseVISASession

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1ga8892502f7aebf2b8866c92e14de63553.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1ga8892502f7aebf2b8866c92e14de63553.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a device session or the event object that you specify in the session parameter. Syntaxint32 __stdcall niBluetoothDTM_CloseVISASession(niBluetoothDTMSession session)ParametersNameDirectionTypeDescriptionsession[out]niBluetoothDTMSessionSpecifies the name of the communication port to which the

### niBluetoothDTM_CloseVISASession

Closes a device session or the event object that you specify in the **session** parameter.

#### Syntax

int32 __stdcall niBluetoothDTM_CloseVISASession(niBluetoothDTMSession session)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1gaa24bd9618a5e9b5f9fcb3cc6a736f2df.html language=enus -->
## TOPIC 00012: niBluetoothDTM_HCILETestEnd

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1gaa24bd9618a5e9b5f9fcb3cc6a736f2df.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1gaa24bd9618a5e9b5f9fcb3cc6a736f2df.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the DUT to end the transmitter or the receiver test. Syntaxint32 __stdcall niBluetoothDTM_HCILETestEnd(niBluetoothDTMSession session, int32 packetCount, int32 status)ParametersNameDirectionTypeDescriptionsession[out]niBluetoothDTMSessionSpecifies the name of the communication po

### niBluetoothDTM_HCILETestEnd

Sends the command to the DUT to end the transmitter or the receiver test.

#### Syntax

int32 __stdcall niBluetoothDTM_HCILETestEnd(niBluetoothDTMSession session, int32 packetCount, int32 status)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| packetCount | [out] | int32 | Returns the number of packets received by the DUT. |
| status | [out] | int32 | Returns the status of the test end command. The DUT receives and executes the test end command if the status parameter returns a 0x00 value. The test end command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1gabc6c56f396cb2409c2768e072e907d3d.html language=enus -->
## TOPIC 00013: niBluetoothDTM_CreateCustomCommand

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1gabc6c56f396cb2409c2768e072e907d3d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1gabc6c56f396cb2409c2768e072e907d3d.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the specified custom command to the device under test (DUT). Syntaxint32 __stdcall niBluetoothDTM_CreateCustomCommand(niBluetoothDTMSession session, int32[] opCode, int32 opCodeLength, int32[] commandParameters, int32 commandParametersLength, int32[] returnParameters, int32 arraySize, int32 ac

### niBluetoothDTM_CreateCustomCommand

Sends the specified custom command to the device under test (DUT).

#### Syntax

int32 __stdcall niBluetoothDTM_CreateCustomCommand(niBluetoothDTMSession session, int32[] opCode, int32 opCodeLength, int32[] commandParameters, int32 commandParametersLength, int32[] returnParameters, int32 arraySize, int32 actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| opCode | [in] | int32[] | Specifies the opcode of the custom commands to send to the DUT. |
| opCodeLength | [in] | int32 | Specifies the length of the opCode array. |
| commandParameters | [in] | int32[] | Specifies an array of the input parameters required for the custom command. |
| commandParametersLength | [in] | int32 | Specifies the length of the commandParameters array. |
| returnParameters | [out] | int32[] | Returns an array of the parameters sent by the DUT in response to the custom command. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 | Returns the actual size of the array, if you pass NULL to returnParameters array, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1gac2dae395e81d110e8c069efe0e9d42d5.html language=enus -->
## TOPIC 00014: niBluetoothDTM_ConfigureVISASerialSettings

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1gac2dae395e81d110e8c069efe0e9d42d5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1gac2dae395e81d110e8c069efe0e9d42d5.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the VISA serial settings for the device under test (DUT) specified by the session parameter. Syntaxint32 __stdcall niBluetoothDTM_ConfigureVISASerialSettings(niBluetoothDTMSession session, uInt16 dataBits, uInt32 baudRate, uInt16 flowControl, uInt16 stopBits, uInt16 parity)ParametersNameD

### niBluetoothDTM_ConfigureVISASerialSettings

Configures the VISA serial settings for the device under test (DUT) specified by the **session** parameter.

#### Syntax

int32 __stdcall niBluetoothDTM_ConfigureVISASerialSettings(niBluetoothDTMSession session, uInt16 dataBits, uInt32 baudRate, uInt16 flowControl, uInt16 stopBits, uInt16 parity)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| dataBits | [in] | uInt16 | Specifies the number of data bits contained in each frame. Valid values are 5 to 8, inclusive. The data bits for each frame are located in the low-order bits of every byte stored in the memory. The default value is 8. |
| baudRate | [in] | uInt32 | Specifies the baud rate of the given communication port. The default value is 115,200. |
| flowControl | [in] | uInt16 | specifies the flow control method used for transmitting and receiving data. The default value is RTS/CTS.NIBLUETOOTHDTM_VAL_FLOW_CONTROL_NONE (0)Does not use flow control, and the buffers on both sides of the connection are assumed to be large enough to hold all the transferred data.NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF (1)Uses the XON and XOFF characters to complete flow control. The transfer mechanism controls input flow by transmitting XOFF when the low-level I/O receive buffer is nearly full, and it controls the output flow by suspending transmission when XOFF is received.NIBLUETOOTHDTM_VAL_FLOW_CONTROL_RTS_CTS (2)Uses the RTS output signal and the CTS input signal to complete flow control. The transfer mechanism controls input flow by unasserting the RTS signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the CTS signal is unasserted.NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF_AND_RTS_CTS (3)Uses values of XON/XOFF and RTS/CTS.NIBLUETOOTHDTM_VAL_FLOW_CONTROL_DTR_DSR (4)Uses the DTR output signal and the DSR input signal to complete flow control. The transfer mechanism controls input flow by unasserting the DTR signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the DSR signal is unasserted.NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF_AND_DTR_DSR (5)Uses values of XON/XOFF and DTR/DSR. |
|  |  |  |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_NONE (0) | Does not use flow control, and the buffers on both sides of the connection are assumed to be large enough to hold all the transferred data. |  |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF (1) | Uses the XON and XOFF characters to complete flow control. The transfer mechanism controls input flow by transmitting XOFF when the low-level I/O receive buffer is nearly full, and it controls the output flow by suspending transmission when XOFF is received. |  |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_RTS_CTS (2) | Uses the RTS output signal and the CTS input signal to complete flow control. The transfer mechanism controls input flow by unasserting the RTS signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the CTS signal is unasserted. |  |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF_AND_RTS_CTS (3) | Uses values of XON/XOFF and RTS/CTS. |  |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_DTR_DSR (4) | Uses the DTR output signal and the DSR input signal to complete flow control. The transfer mechanism controls input flow by unasserting the DTR signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the DSR signal is unasserted. |  |  |
| NIBLUETOOTHDTM_VAL_FLOW_CONTROL_XON_XOFF_AND_DTR_DSR (5) | Uses values of XON/XOFF and DTR/DSR. |  |  |
| stopBits | [in] | uInt16 | Specifies the number of stop bits used to indicate the end of a frame. The default value is 1.0. |
| parity | [in] | uInt16 | Specifies the parity bit used with each transmitted or received frame. The default value is NIBLUETOOTHDTM_VAL_PARITY_NONE.NIBLUETOOTHDTM_VAL_PARITY_NONE (0)Specifies that the frame does not contain a parity bit.NIBLUETOOTHDTM_VAL_PARITY_ODD (1)Specifies that the parity is odd.NIBLUETOOTHDTM_VAL_PARITY_EVEN (2)Specifies that the parity is even.NIBLUETOOTHDTM_VAL_PARITY_MARK (3)Specifies that the parity bit is always 1.NIBLUETOOTHDTM_VAL_PARITY_SPACE (4)Specifies that the parity bit is always 0. |
|  |  |  |  |
| NIBLUETOOTHDTM_VAL_PARITY_NONE (0) | Specifies that the frame does not contain a parity bit. |  |  |
| NIBLUETOOTHDTM_VAL_PARITY_ODD (1) | Specifies that the parity is odd. |  |  |
| NIBLUETOOTHDTM_VAL_PARITY_EVEN (2) | Specifies that the parity is even. |  |  |
| NIBLUETOOTHDTM_VAL_PARITY_MARK (3) | Specifies that the parity bit is always 1. |  |  |
| NIBLUETOOTHDTM_VAL_PARITY_SPACE (4) | Specifies that the parity bit is always 0. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1gada7ea019a8c28c514621da81093ee3c9.html language=enus -->
## TOPIC 00015: niBluetoothDTM_HCILEReceiverTest

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1gada7ea019a8c28c514621da81093ee3c9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1gada7ea019a8c28c514621da81093ee3c9.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the device under test (DUT) to start the receiver test. Syntaxint32 __stdcall niBluetoothDTM_HCILEReceiverTest(niBluetoothDTMSession session, int32 channelNumber, int32 status)ParametersNameDirectionTypeDescriptionsession[out]niBluetoothDTMSessionSpecifies the name of the commun

### niBluetoothDTM_HCILEReceiverTest

Sends the command to the device under test (DUT) to start the receiver test.

#### Syntax

int32 __stdcall niBluetoothDTM_HCILEReceiverTest(niBluetoothDTMSession session, int32 channelNumber, int32 status)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | [in] | int32 | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| status | [out] | int32 | Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1gae78cb59a90be72d5ad4bd7401c5c5c42.html language=enus -->
## TOPIC 00016: niBluetoothDTM_SetVISATimeout

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1gae78cb59a90be72d5ad4bd7401c5c5c42.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1gae78cb59a90be72d5ad4bd7401c5c5c42.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the session parameter. Syntaxint32 __stdcall niBluetoothDTM_SetVISATimeout(niBluetoothDTMSession session, uInt32 timeout)ParametersNameDirectionTypeDescriptionsession[out]niBluetoothDTMSes

### niBluetoothDTM_SetVISATimeout

Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the **session** parameter.

#### Syntax

int32 __stdcall niBluetoothDTM_SetVISATimeout(niBluetoothDTMSession session, uInt32 timeout)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| timeout | [in] | uInt32 | Specifies the minimum timeout value, in milliseconds (ms), to use when accessing the device. The default value is 2,000. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group____root__ni_bluetooth_d_t_m__functions_1gafa8f89947b86fdf7e29a5332f063e14c.html language=enus -->
## TOPIC 00017: niBluetoothDTM_HCILEDirectionFindingReceiverTest

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group____root__ni_bluetooth_d_t_m__functions_1gafa8f89947b86fdf7e29a5332f063e14c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group____root__ni_bluetooth_d_t_m__functions_1gafa8f89947b86fdf7e29a5332f063e14c.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the device under test (DUT) to start the receiver test. Syntaxint32 __stdcall niBluetoothDTM_HCILEDirectionFindingReceiverTest(niBluetoothDTMSession session, int32 channelNumber, int32 modulationIndex, int32 phy, int32 directionFindingMode, int32 lengthOfSwitchingPattern, float6

### niBluetoothDTM_HCILEDirectionFindingReceiverTest

Sends the command to the device under test (DUT) to start the receiver test.

#### Syntax

int32 __stdcall niBluetoothDTM_HCILEDirectionFindingReceiverTest(niBluetoothDTMSession session, int32 channelNumber, int32 modulationIndex, int32 phy, int32 directionFindingMode, int32 lengthOfSwitchingPattern, float64 cteLength, float64 cteSlotDuration, int32[] antennaID, int32 antennaIDArraySize, int32 status)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [out] | niBluetoothDTMSession | Specifies the name of the communication port to which the DUT is connected. |
| channelNumber | [in] | int32 | Specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. |
| modulationIndex | [in] | int32 | Specifies the type of modulation index at the generator. The default value is NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD.NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD (0)The packets are generated with standard modulation index.NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STABLE (1)The packets are generated with stable modulation index. |
|  |  |  |  |
| NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STANDARD (0) | The packets are generated with standard modulation index. |  |  |
| NIBLUETOOTHDTM_VAL_MODULATION_INDEX_STABLE (1) | The packets are generated with stable modulation index. |  |  |
| phy | [in] | int32 | Specifies the type of the generated packet by the physical layer of the DUT. The default value is NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS.NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS (0)Receiver is set to use the LE 1M PHY.NIBLUETOOTHDTM_VAL_RECEIVER_PHY_2MBPS (1)Receiver is set to use the LE 2M PHY.NIBLUETOOTHDTM_VAL_RECEIVER_PHY_CODED (2)Receiver is set to use the Coded PHY. |
|  |  |  |  |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_1MBPS (0) | Receiver is set to use the LE 1M PHY. |  |  |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_2MBPS (1) | Receiver is set to use the LE 2M PHY. |  |  |
| NIBLUETOOTHDTM_VAL_RECEIVER_PHY_CODED (2) | Receiver is set to use the Coded PHY. |  |  |
| directionFindingMode | [in] | int32 | Specifies the mode of direction finding. The default value is NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED.NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED (0)Specifies that the LE packet does not have fields required for direction finding.NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1)Specifies the LE packets uses the angle of arrival method of direction finding.NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2)Specifies the LE packet uses angle of departure method of direction finding. |
|  |  |  |  |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_DISABLED (0) | Specifies that the LE packet does not have fields required for direction finding. |  |  |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL (1) | Specifies the LE packets uses the angle of arrival method of direction finding. |  |  |
| NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE (2) | Specifies the LE packet uses angle of departure method of direction finding. |  |  |
| lengthOfSwitchingPattern | [in] | int32 | Specifies the length of the antenna switching pattern. The default value is 0. |
| cteLength | [in] | float64 | Specifies specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the directionFindingMode parameter to either NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_ARRIVAL or NIBLUETOOTHDTM_VAL_DIRECTION_FINDING_MODE_ANGLE_OF_DEPARTURE. The default value is 160 microseconds. |
| cteSlotDuration | [in] | float64 | Specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. The default value is 1 us. Valid values are 1 us and 2 us. |
| antennaID | [in] | int32[] | Specifies the array of Antenna IDs in the antenna switching pattern. The length of Antenna IDs array must be equal to Length Of Switching Pattern parameter. |
| antennaIDArraySize | [in] | int32 | Specifies size of antennaID parameter. |
| status | [out] | int32 | Returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning. Examine the status code from each call to an niBluetoothDTM function to determine if an error has occurred. The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxbluetoothdtm-c-api-ref path=group__root__ni_bluetooth_d_t_m.html language=enus -->
## TOPIC 00018: niBluetoothDTM.h

- bundle_id: `rfmxbluetoothdtm-c-api-ref`
- source_path: `group__root__ni_bluetooth_d_t_m.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-c-api-ref/raw/resource/enus/group__root__ni_bluetooth_d_t_m.html
- document_id: `rfmxbluetoothdtm-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAttributesFunctionsGroup membersNoneAttachmentsNone

### niBluetoothDTM.h

#### Groups

- Attributes
- Functions

#### Group members

None

#### Attachments

None
