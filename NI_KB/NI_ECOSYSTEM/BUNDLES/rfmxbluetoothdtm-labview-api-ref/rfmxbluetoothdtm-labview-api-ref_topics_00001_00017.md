# NI DOCUMENT BUNDLE: rfmxbluetoothdtm-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxbluetoothdtm-labview-api-ref start=1 end=17 -->
<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=menus/categories/measurement/rfmx/bt/nibluetoothdtm/dir-mnu.html language=enus -->
## TOPIC 00001: niBluetoothDTM

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/bt/nibluetoothdtm/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/bt/nibluetoothdtm/dir-mnu.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to send commands to the device under test (DUT). These VIs help to control the DUT by directing it to perform tasks such as starting the transmitter or receiver test, ending the test, getting the BD address. © 2019–2026 National Instruments Corporation. All rights reserve

### niBluetoothDTM

Use the VIs on this palette to send commands to the device under test (DUT). These VIs help to control the DUT by directing it to perform tasks such as starting the transmitter or receiver test, ending the test, getting the BD address.

© 2019–2026 National Instruments Corporation. All rights reserved.

[IMAGE alt='icon' src='dir-mnu.png']

- [niBluetoothDTM VISA Open Session VI](../../../../../../vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-open-session-vi.html) Opens a session of the device under test (DUT) specified by the VISA resource name parameter, and returns a session identifier that can be used to call any other operations on that DUT.
- [niBluetoothDTM VISA Configure Serial Settings VI](../../../../../../vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-configure-serial-settings-vi.html) Configures the VISA serial settings for the device under test (DUT) specified by the VISA resource name parameter.
- [niBluetoothDTM VISA Set Timeout VI](../../../../../../vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-set-timeout-vi.html) Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the VISA resource name parameter.
- [niBluetoothDTM HCI Read BD_ADDR VI](../../../../../../vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-read-bd-addr-vi.html) Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address.
- [niBluetoothDTM HCI LE Transmitter Test VI](../../../../../../vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-transmitter-test-vi.html) Sends a command to the device under test (DUT) to start the transmitter test.
- [niBluetoothDTM HCI LE Receiver Test VI](../../../../../../vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-receiver-test-vi.html) Sends the command to the device under test (DUT) to start the receiver test.
- [niBluetoothDTM HCI LE Enhanced Transmitter Test VI](../../../../../../vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-enhanced-transmitter-test-vi.html) Sends the command to the device under test (DUT) to start the transmitter test.
- [niBluetoothDTM HCI LE Enhanced Receiver Test VI](../../../../../../vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-enhanced-receiver-test-vi.html) Sends a command to the device under test (DUT) to start the receiver test.
- [niBluetoothDTM HCI LE Direction Finding Transmitter Test VI](../../../../../../vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-direction-finding-transmitter-test-vi.html) Sends a command to the device under test (DUT) to start the transmitter test.
- [niBluetoothDTM HCI LE Direction Finding Receiver Test VI](../../../../../../vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-direction-finding-receiver-test-vi.html) Sends a command to the device under test (DUT) to start the receiver test.
- [niBluetoothDTM Create Custom Command VI](../../../../../../vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-create-custom-command-vi.html) Sends the specified custom command to the device under test (DUT).
- [niBluetoothDTM HCI LE Test End VI](../../../../../../vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-test-end-vi.html) Sends the command to the device under test (DUT) to end the transmitter or receiver test.
- [niBluetoothDTM HCI Reset VI](../../../../../../vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-reset-vi.html) Resets the device under test (DUT) specified by the VISA resource name parameter.
- [niBluetoothDTM VISA Close Session VI](../../../../../../vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-close-session-vi.html) Closes a device session or the event object that you specify in the VISA resource name parameter.

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-create-custom-command-vi.html language=enus -->
## TOPIC 00002: niBluetoothDTM Create Custom Command VI

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-create-custom-command-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-create-custom-command-vi.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the specified custom command to the device under test (DUT). icon Inputs/Outputs cvsrn.png VISA resource name VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. c1di32.png opcode opcode specifies an array of custom opco

### niBluetoothDTM Create Custom Command VI

Sends the specified custom command to the device under test (DUT).

[IMAGE alt='icon' src='nibluetoothdtm-create-custom-command-vi.png']

#### Inputs/Outputs

| VISA resource name — VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. opcode — opcode specifies an array of custom opcode commands to send to the DUT. command parameters — command parameters specifies an array of the input parameters required for the custom command. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VISA resource name out — VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. return parameters — return parameters returns an array of the parameters sent by the DUT in response to the custom command. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niBluetoothDTM

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-direction-finding-receiver-test-vi.html language=enus -->
## TOPIC 00003: niBluetoothDTM HCI LE Direction Finding Receiver Test VI

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-direction-finding-receiver-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-direction-finding-receiver-test-vi.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a command to the device under test (DUT) to start the receiver test. icon Inputs/Outputs cdbl.png CTE Length (s) CTE Length specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the

### niBluetoothDTM HCI LE Direction Finding Receiver Test VI

Sends a command to the device under test (DUT) to start the receiver test.

[IMAGE alt='icon' src='nibluetoothdtm-hci-le-direction-finding-receiver-test-vi.png']

#### Inputs/Outputs

| CTE Length (s) — CTE Length specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the Direction Finding Mode parameter to either Angle of Arrival or Angle of Departure. The default value is 160 microseconds. CTE Slot Duration — CTE Slot Duration specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. The default value is 1 us. 1 us (0.000001) Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 1 microseconds. 2 us (0.000002) Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 2 microseconds. VISA resource name — VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. channel number — channel number specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. PHY — PHY specifies the type of the generated packet by the physical layer of the DUT. The default value is 1Mbps. 1Mbps (0) Receiver is set to use the LE 1M PHY. 2Mbps (1) Receiver is set to use the LE 2M PHY. Coded (2) Receiver is set to use the Coded PHY. Modulation index — modulation index specifies the type of modulation index at the generator. The default value is Standard. Standard (0) The packets are generated with standard modulation index. Stable (1) The packets are generated with stable modulation index. Direction Finding Mode — Direction Finding Mode specifies the mode of direction finding. The default value is Disabled. Disabled (0) Specifies that the LE packet does not have fields required for direction finding. Angle of Arrival (1) Specifies the LE packets uses the angle of arrival method of direction finding. Angle of Departure (2) Specifies the LE packet uses angle of departure method of direction finding. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Antenna IDs — Antenna IDs specifies the array of Antenna IDs in the antenna switching pattern. The length of Antenna IDs array must be equal to Length Of Switching Pattern. Switching Pattern Length — Switching Pattern Length specifies the length of the antenna switching pattern. The default value is 0. VISA resource name out — VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. status — status returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 1 us (0.000001) | Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 1 microseconds. |
| 2 us (0.000002) | Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 2 microseconds. |
| 1Mbps (0) | Receiver is set to use the LE 1M PHY. |
| 2Mbps (1) | Receiver is set to use the LE 2M PHY. |
| Coded (2) | Receiver is set to use the Coded PHY. |
| Standard (0) | The packets are generated with standard modulation index. |
| Stable (1) | The packets are generated with stable modulation index. |
| Disabled (0) | Specifies that the LE packet does not have fields required for direction finding. |
| Angle of Arrival (1) | Specifies the LE packets uses the angle of arrival method of direction finding. |
| Angle of Departure (2) | Specifies the LE packet uses angle of departure method of direction finding. |

Parent topic:

niBluetoothDTM

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-direction-finding-transmitter-test-vi.html language=enus -->
## TOPIC 00004: niBluetoothDTM HCI LE Direction Finding Transmitter Test VI

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-direction-finding-transmitter-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-direction-finding-transmitter-test-vi.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a command to the device under test (DUT) to start the transmitter test. icon Inputs/Outputs cdbl.png CTE Length (s) CTE Length specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set

### niBluetoothDTM HCI LE Direction Finding Transmitter Test VI

Sends a command to the device under test (DUT) to start the transmitter test.

[IMAGE alt='icon' src='nibluetoothdtm-hci-le-direction-finding-transmitter-test-vi.png']

#### Inputs/Outputs

| CTE Length (s) — CTE Length specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the Direction Finding Mode parameter to either Angle of Arrival or Angle of Departure. The default value is 160 microseconds. CTE Slot Duration — CTE Slot Duration specifies the length of the antenna switching and sampling slots in the constant tone extension field. This value is expressed in seconds. The default value is 1 us. 1 us (0.000001) Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 1 microseconds. 2 us (0.000002) Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 2 microseconds. VISA resource name — VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. channel number — channel number specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. payload length (bytes) — payload length specifies the length of payload data in each packet that the DUT transmits. This value is expressed in bytes. The default value is 37. LE pattern type — LE pattern type specifies the type of payload to use for the LE packet. The default value is PRBS9. Payload type values of PRBS9, 11110000, and 10101010 must be supported by the DUT. The remaining payload type values are optional. PRBS9 (0) Specifies that the bit sequence is PRBS9. 11110000 (1) Specifies that the bit sequence is 11110000. 10101010 (2) Specifies that the bit sequence is 10101010. PRBS15 (3) Specifies that the bit sequence is PRBS15. 11111111 (4) Specifies that the bit sequence is 11111111. 00000000 (5) Specifies that the bit sequence is 00000000. 00001111 (6) Specifies that the bit sequence is 00001111. 01010101 (7) Specifies that the bit sequence is 01010101. PHY — PHY specifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is 1Mbps. 1Mbps (0) Transmitter is set to use the LE 1M PHY. 2Mbps (1) Transmitter is set to use the LE 2M PHY. Coded 125kbps (2) Transmitter is set to use the LE Coded PHY with S = 8 data coding. Coded 500kbps (3) Transmitter is set to use the LE Coded PHY with S = 2 data coding. Direction Finding Mode — Direction Finding Mode specifies the mode of direction finding. The default value is Disabled. Disabled (0) Specifies that the LE packet does not have fields required for direction finding. Angle of Arrival (1) Specifies the LE packets uses the angle of arrival method of direction finding. Angle of Departure (2) Specifies the LE packet uses angle of departure method of direction finding. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Antenna IDs — Antenna IDs specifies the array of Antenna IDs in the antenna switching pattern. The length of Antenna IDs array must be equal to Length Of Switching Pattern. Switching Pattern Length — Switching Pattern Length specifies the length of the antenna switching pattern. The default value is 0. VISA resource name out — VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. status — status returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 1 us (0.000001) | Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 1 microseconds. |
| 2 us (0.000002) | Specifies that the length of the antenna switching and sampling slots in the constant tone extension field is 2 microseconds. |
| PRBS9 (0) | Specifies that the bit sequence is PRBS9. |
| 11110000 (1) | Specifies that the bit sequence is 11110000. |
| 10101010 (2) | Specifies that the bit sequence is 10101010. |
| PRBS15 (3) | Specifies that the bit sequence is PRBS15. |
| 11111111 (4) | Specifies that the bit sequence is 11111111. |
| 00000000 (5) | Specifies that the bit sequence is 00000000. |
| 00001111 (6) | Specifies that the bit sequence is 00001111. |
| 01010101 (7) | Specifies that the bit sequence is 01010101. |
| 1Mbps (0) | Transmitter is set to use the LE 1M PHY. |
| 2Mbps (1) | Transmitter is set to use the LE 2M PHY. |
| Coded 125kbps (2) | Transmitter is set to use the LE Coded PHY with S = 8 data coding. |
| Coded 500kbps (3) | Transmitter is set to use the LE Coded PHY with S = 2 data coding. |
| Disabled (0) | Specifies that the LE packet does not have fields required for direction finding. |
| Angle of Arrival (1) | Specifies the LE packets uses the angle of arrival method of direction finding. |
| Angle of Departure (2) | Specifies the LE packet uses angle of departure method of direction finding. |

Parent topic:

niBluetoothDTM

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-enhanced-receiver-test-vi.html language=enus -->
## TOPIC 00005: niBluetoothDTM HCI LE Enhanced Receiver Test VI

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-enhanced-receiver-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-enhanced-receiver-test-vi.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a command to the device under test (DUT) to start the receiver test. icon Inputs/Outputs cvsrn.png VISA resource name VISA resource name specifies the resource name corresponding to the DUT. ci32.png channel number channel number specifies the Bluetooth transmit channel number of the generated

### niBluetoothDTM HCI LE Enhanced Receiver Test VI

Sends a command to the device under test (DUT) to start the receiver test.

[IMAGE alt='icon' src='nibluetoothdtm-hci-le-enhanced-receiver-test-vi.png']

#### Inputs/Outputs

| VISA resource name — VISA resource name specifies the resource name corresponding to the DUT. channel number — channel number specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. PHY — PHY specifies the type of the generated packet by the physical layer of the DUT. The default value is 1Mbps. 1Mbps (0) Receiver is set to use the LE 1M PHY. 2Mbps (1) Receiver is set to use the LE 2M PHY. Coded (2) Receiver is set to use the Coded PHY. modulation index — modulation index specifies the type of modulation index at the generator. The default value is Standard. Standard (0) The packets are generated with standard modulation index. Stable (1) The packets are generated with stable modulation index. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VISA resource name out — VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. status — status returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 1Mbps (0) | Receiver is set to use the LE 1M PHY. |
| 2Mbps (1) | Receiver is set to use the LE 2M PHY. |
| Coded (2) | Receiver is set to use the Coded PHY. |
| Standard (0) | The packets are generated with standard modulation index. |
| Stable (1) | The packets are generated with stable modulation index. |

Parent topic:

niBluetoothDTM

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-enhanced-transmitter-test-vi.html language=enus -->
## TOPIC 00006: niBluetoothDTM HCI LE Enhanced Transmitter Test VI

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-enhanced-transmitter-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-enhanced-transmitter-test-vi.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the device under test (DUT) to start the transmitter test. icon Inputs/Outputs cvsrn.png VISA resource name VISA resource name specifies the resource name corresponding to the DUT. ci32.png channel number channel number specifies the Bluetooth transmit channel number of the sign

### niBluetoothDTM HCI LE Enhanced Transmitter Test VI

Sends the command to the device under test (DUT) to start the transmitter test.

[IMAGE alt='icon' src='nibluetoothdtm-hci-le-enhanced-transmitter-test-vi.png']

#### Inputs/Outputs

| VISA resource name — VISA resource name specifies the resource name corresponding to the DUT. channel number — channel number specifies the Bluetooth transmit channel number of the signal generated by the DUT. The default value is 0. payload length (bytes) — payload length specifies the length of payload data in each packet that the DUT transmits. This value is expressed in bytes. The default value is 37. LE pattern type — LE pattern type specifies the type of payload to use for the LE packet. The default value is PRBS9. Payload type values of PRBS9, 11110000, and 10101010 must be supported by the DUT. The remaining payload type values are optional. PRBS9 (0) Specifies that the bit sequence is PRBS9. 11110000 (1) Specifies that the bit sequence is 11110000. 10101010 (2) Specifies that the bit sequence is 10101010. PRBS15 (3) Specifies that the bit sequence is PRBS15. 11111111 (4) Specifies that the bit sequence is 11111111. 00000000 (5) Specifies that the bit sequence is 00000000. 00001111 (6) Specifies that the bit sequence is 00001111. 01010101 (7) Specifies that the bit sequence is 01010101. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. PHY — PHY specifies the type of the packet to be transmitted by the physical layer of the DUT. The default value is 1Mbps. 1Mbps (0) Transmitter is set to use the LE 1M PHY. 2Mbps (1) Transmitter is set to use the LE 2M PHY. Coded 125kbps (2) Transmitter is set to use the LE Coded PHY with S = 8 data coding. Coded 500kbps (3) Transmitter is set to use the LE Coded PHY with S = 2 data coding. VISA resource name out — VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. status — status returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| PRBS9 (0) | Specifies that the bit sequence is PRBS9. |
| 11110000 (1) | Specifies that the bit sequence is 11110000. |
| 10101010 (2) | Specifies that the bit sequence is 10101010. |
| PRBS15 (3) | Specifies that the bit sequence is PRBS15. |
| 11111111 (4) | Specifies that the bit sequence is 11111111. |
| 00000000 (5) | Specifies that the bit sequence is 00000000. |
| 00001111 (6) | Specifies that the bit sequence is 00001111. |
| 01010101 (7) | Specifies that the bit sequence is 01010101. |
| 1Mbps (0) | Transmitter is set to use the LE 1M PHY. |
| 2Mbps (1) | Transmitter is set to use the LE 2M PHY. |
| Coded 125kbps (2) | Transmitter is set to use the LE Coded PHY with S = 8 data coding. |
| Coded 500kbps (3) | Transmitter is set to use the LE Coded PHY with S = 2 data coding. |

Parent topic:

niBluetoothDTM

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-receiver-test-vi.html language=enus -->
## TOPIC 00007: niBluetoothDTM HCI LE Receiver Test VI

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-receiver-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-receiver-test-vi.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the device under test (DUT) to start the receiver test. icon Inputs/Outputs cvsrn.png VISA resource name VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. ci32.png channel number channel number specifies

### niBluetoothDTM HCI LE Receiver Test VI

Sends the command to the device under test (DUT) to start the receiver test.

[IMAGE alt='icon' src='nibluetoothdtm-hci-le-receiver-test-vi.png']

#### Inputs/Outputs

| VISA resource name — VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. channel number — channel number specifies the Bluetooth transmit channel number of the generated signal. The default value is 0. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VISA resource name out — VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. status — status returns the status of the receiver test command. The DUT receives and executes the receiver test command if the status parameter returns a 0x00 value. The receiver test command fails if the status parameter returns a non-zero (0x01-0xFF) value. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niBluetoothDTM

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-test-end-vi.html language=enus -->
## TOPIC 00008: niBluetoothDTM HCI LE Test End VI

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-test-end-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-test-end-vi.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the device under test (DUT) to end the transmitter or receiver test. icon Inputs/Outputs cvsrn.png VISA resource name VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. cerrcodeclst.png error in error in

### niBluetoothDTM HCI LE Test End VI

Sends the command to the device under test (DUT) to end the transmitter or receiver test.

[IMAGE alt='icon' src='nibluetoothdtm-hci-le-test-end-vi.png']

#### Inputs/Outputs

| VISA resource name — VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VISA resource name out — VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. packet count — packet count returns the number of packets received by the DUT. status — status returns the status of the test end command. The DUT receives and executes the test end command if the status parameter returns a 0x00 value. The test end command fails if the status parameter returns a non-zero (0x01-0xFF) value. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niBluetoothDTM

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-transmitter-test-vi.html language=enus -->
## TOPIC 00009: niBluetoothDTM HCI LE Transmitter Test VI

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-transmitter-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-le-transmitter-test-vi.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a command to the device under test (DUT) to start the transmitter test. icon Inputs/Outputs cvsrn.png VISA resource name VISA resource name specifies the resource name corresponding to the DUT. ci32.png channel number channel number specifies the Bluetooth transmit channel number of the signal

### niBluetoothDTM HCI LE Transmitter Test VI

Sends a command to the device under test (DUT) to start the transmitter test.

[IMAGE alt='icon' src='nibluetoothdtm-hci-le-transmitter-test-vi.png']

#### Inputs/Outputs

| VISA resource name — VISA resource name specifies the resource name corresponding to the DUT. channel number — channel number specifies the Bluetooth transmit channel number of the signal generated by the DUT. The default value is 0. payload length (bytes) — payload length specifies the length of payload data in each packet that the DUT transmits. This value is expressed in bytes. The default value is 37. LE pattern type — LE pattern type specifies the type of payload to use for the LE packet. The default value is PRBS9. Payload type values of PRBS9, 11110000, and 10101010 must be supported by the DUT. The remaining payload type values are optional. PRBS9 (0) Specifies that the bit sequence is PRBS9. 11110000 (1) Specifies that the bit sequence is 11110000. 10101010 (2) Specifies that the bit sequence is 10101010. PRBS15 (3) Specifies that the bit sequence is PRBS15. 11111111 (4) Specifies that the bit sequence is 11111111. 00000000 (5) Specifies that the bit sequence is 00000000. 00001111 (6) Specifies that the bit sequence is 00001111. 01010101 (7) Specifies that the bit sequence is 01010101. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VISA resource name out — VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. status — status returns the status of the transmitter test command. The DUT receives and executes the transmitter test command if the status parameter returns a 0x00 value. The transmitter test command fails if the status parameter returns a non-zero (0x01-0xFF) value. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| PRBS9 (0) | Specifies that the bit sequence is PRBS9. |
| 11110000 (1) | Specifies that the bit sequence is 11110000. |
| 10101010 (2) | Specifies that the bit sequence is 10101010. |
| PRBS15 (3) | Specifies that the bit sequence is PRBS15. |
| 11111111 (4) | Specifies that the bit sequence is 11111111. |
| 00000000 (5) | Specifies that the bit sequence is 00000000. |
| 00001111 (6) | Specifies that the bit sequence is 00001111. |
| 01010101 (7) | Specifies that the bit sequence is 01010101. |

Parent topic:

niBluetoothDTM

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-read-bd-addr-vi.html language=enus -->
## TOPIC 00010: niBluetoothDTM HCI Read BD_ADDR VI

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-read-bd-addr-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-read-bd-addr-vi.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address. icon Inputs/Outputs cvsrn.png VISA resource name VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. cerrcodeclst.png error in error in

### niBluetoothDTM HCI Read BD_ADDR VI

Sends the command to the device under test (DUT) to get its Bluetooth device (BD) address.

[IMAGE alt='icon' src='nibluetoothdtm-hci-read-bd-addr-vi.png']

#### Inputs/Outputs

| VISA resource name — VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VISA resource name out — VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. BD_ADDR — BD_ADDR returns the BD address of the DUT. status — status returns the status of the read BD_ADDR command. The DUT receives and executes the read BD_ADDR command if the status parameter returns a 0x00 value. The read BD_ADDR command fails if the status parameter returns a non-zero (0x01-0xFF) value. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niBluetoothDTM

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-reset-vi.html language=enus -->
## TOPIC 00011: niBluetoothDTM HCI Reset VI

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-reset-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-hci-reset-vi.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the device under test (DUT) specified by the VISA resource name parameter. icon Inputs/Outputs cvsrn.png VISA resource name VISA resource name specifies the resource name corresponding to the DUT. cerrcodeclst.png error in error in describes error conditions that occur before this node runs.

### niBluetoothDTM HCI Reset VI

Resets the device under test (DUT) specified by the **VISA resource name** parameter.

[IMAGE alt='icon' src='nibluetoothdtm-hci-reset-vi.png']

#### Inputs/Outputs

| VISA resource name — VISA resource name specifies the resource name corresponding to the DUT. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VISA resource name out — VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. status — status returns the status of the reset command. The DUT receives and executes the reset command if the status parameter returns a 0x00 value. The reset command fails if the parameter returns a non-zero (0x01-0xFF) value. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niBluetoothDTM

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-close-session-vi.html language=enus -->
## TOPIC 00012: niBluetoothDTM VISA Close Session VI

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-close-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-close-session-vi.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a device session or the event object that you specify in the VISA resource name parameter. icon Inputs/Outputs cvsrn.png VISA resource name VISA resource name specifies the name of the resource you want to close. This parameter also specifies the VISA session and class. cerrcodeclst.png error

### niBluetoothDTM VISA Close Session VI

Closes a device session or the event object that you specify in the **VISA resource name** parameter.

[IMAGE alt='icon' src='nibluetoothdtm-visa-close-session-vi.png']

#### Inputs/Outputs

| VISA resource name — VISA resource name specifies the name of the resource you want to close. This parameter also specifies the VISA session and class. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niBluetoothDTM

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-configure-serial-settings-vi.html language=enus -->
## TOPIC 00013: niBluetoothDTM VISA Configure Serial Settings VI

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-configure-serial-settings-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-configure-serial-settings-vi.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the VISA serial settings for the device under test (DUT) specified by the VISA resource name parameter. icon Inputs/Outputs cu16.png data bits data bits specifies the number of data bits contained in each frame. Valid values are 5 to 8, inclusive. The data bits for each frame are located

### niBluetoothDTM VISA Configure Serial Settings VI

Configures the VISA serial settings for the device under test (DUT) specified by the **VISA resource name** parameter.

[IMAGE alt='icon' src='nibluetoothdtm-visa-configure-serial-settings-vi.png']

#### Inputs/Outputs

| data bits — data bits specifies the number of data bits contained in each frame. Valid values are 5 to 8, inclusive. The data bits for each frame are located in the low-order bits of every byte stored in the memory. The default value is 8. VISA resource name — VISA resource name specifies the name of the resource to be configured. This parameter also specifies the VISA session and class. baud rate — baud rate specifies the baud rate of the given communication port. The default value is 115,200. flow control — flow control specifies the flow control method used for transmitting and receiving data. The default value is RTS/CTS. None (0) Does not use flow control, and the buffers on both sides of the connection are assumed to be large enough to hold all the transferred data. XON/XOFF (1) Uses the XON and XOFF characters to complete flow control. The transfer mechanism controls input flow by transmitting XOFF when the low-level I/O receive buffer is nearly full, and it controls the output flow by suspending transmission when XOFF is received. RTS/CTS (2) Uses the RTS output signal and the CTS input signal to complete flow control. The transfer mechanism controls input flow by unasserting the RTS signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the CTS signal is unasserted. XON/XOFF & RTS/CTS (3) Uses values of XON/XOFF and RTS/CTS. DTR/DSR (4) Uses the DTR output signal and the DSR input signal to complete flow control. The transfer mechanism controls input flow by unasserting the DTR signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the DSR signal is unasserted. XON/XOFF & DTR/DSR (5) Uses values of XON/XOFF and DTR/DSR. stop bits — stop bits specifies the number of stop bits used to indicate the end of a frame. The default value is 1.0. 1.0 (10) Specifies that the number of stop bits used is 1. 1.5 (15) Specifies that the number of stop bits used is 1.5. 2.0 (20) Specifies that the number of stop bits used is 2. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. parity — parity specifies the parity bit used with each transmitted or received frame. The default value is None. None (0) Specifies that the frame does not contain a parity bit. Odd (1) Specifies that the parity is odd. Even (2) Specifies that the parity is even. Mark (3) Specifies that the parity bit is always 1. Space (4) Specifies that the parity bit is always 0. VISA resource name out — VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| None (0) | Does not use flow control, and the buffers on both sides of the connection are assumed to be large enough to hold all the transferred data. |
| XON/XOFF (1) | Uses the XON and XOFF characters to complete flow control. The transfer mechanism controls input flow by transmitting XOFF when the low-level I/O receive buffer is nearly full, and it controls the output flow by suspending transmission when XOFF is received. |
| RTS/CTS (2) | Uses the RTS output signal and the CTS input signal to complete flow control. The transfer mechanism controls input flow by unasserting the RTS signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the CTS signal is unasserted. |
| XON/XOFF & RTS/CTS (3) | Uses values of XON/XOFF and RTS/CTS. |
| DTR/DSR (4) | Uses the DTR output signal and the DSR input signal to complete flow control. The transfer mechanism controls input flow by unasserting the DTR signal when the low-level I/O receive buffer is nearly full. The transfer mechanism also controls output flow by suspending the transmission when the DSR signal is unasserted. |
| XON/XOFF & DTR/DSR (5) | Uses values of XON/XOFF and DTR/DSR. |
| 1.0 (10) | Specifies that the number of stop bits used is 1. |
| 1.5 (15) | Specifies that the number of stop bits used is 1.5. |
| 2.0 (20) | Specifies that the number of stop bits used is 2. |
| None (0) | Specifies that the frame does not contain a parity bit. |
| Odd (1) | Specifies that the parity is odd. |
| Even (2) | Specifies that the parity is even. |
| Mark (3) | Specifies that the parity bit is always 1. |
| Space (4) | Specifies that the parity bit is always 0. |

Parent topic:

niBluetoothDTM

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-open-session-vi.html language=enus -->
## TOPIC 00014: niBluetoothDTM VISA Open Session VI

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-open-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-open-session-vi.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a session of the device under test (DUT) specified by the VISA resource name parameter, and returns a session identifier that can be used to call any other operations on that DUT. icon Inputs/Outputs cvsrn.png VISA resource name VISA resource name specifies the name of the resource to be opene

### niBluetoothDTM VISA Open Session VI

Opens a session of the device under test (DUT) specified by the **VISA resource name** parameter, and returns a session identifier that can be used to call any other operations on that DUT.

[IMAGE alt='icon' src='nibluetoothdtm-visa-open-session-vi.png']

#### Inputs/Outputs

| VISA resource name — VISA resource name specifies the name of the resource to be opened. This parameter also specifies the VISA session and class. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VISA resource name out — VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niBluetoothDTM

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-set-timeout-vi.html language=enus -->
## TOPIC 00015: niBluetoothDTM VISA Set Timeout VI

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-set-timeout-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/nibluetoothdtm-visa-set-timeout-vi.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the VISA resource name parameter. icon Inputs/Outputs cvsrn.png VISA resource name VISA resource name specifies the name of the resource for which you set the timeout value. This parameter

### niBluetoothDTM VISA Set Timeout VI

Sets the timeout value, in milliseconds (ms), for the VISA session of the device under test (DUT), specified by the **VISA resource name** parameter.

[IMAGE alt='icon' src='nibluetoothdtm-visa-set-timeout-vi.png']

#### Inputs/Outputs

| VISA resource name — VISA resource name specifies the name of the resource for which you set the timeout value. This parameter also specifies the VISA session and class. timeout (ms) — timeout specifies the minimum timeout value, in milliseconds (ms), to use when accessing the device. The default value is 2000. Note The actual timeout that VISA returns may be higher than the specified timeout. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VISA resource name out — VISA resource name out returns the resource name to which a VISA session is opened and the resource class. The class name matches the VISA resource name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niBluetoothDTM

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00016: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/standard-functionality-for-error-in-parameters.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error

### Using the Standard Functionality for error in Parameters

Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error in behavior is as follows

Note

error in

error in

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The error in cluster contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=rfmxbluetoothdtm-labview-api-ref path=vi-lib/rfmx/nibluetoothdtm/standard-functionality-for-error-out-parameters.html language=enus -->
## TOPIC 00017: Using the Standard Functionality for error out Parameters

- bundle_id: `rfmxbluetoothdtm-labview-api-ref`
- source_path: `vi-lib/rfmx/nibluetoothdtm/standard-functionality-for-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxbluetoothdtm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nibluetoothdtm/standard-functionality-for-error-out-parameters.html
- document_id: `rfmxbluetoothdtm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard err

### Using the Standard Functionality for error out Parameters

Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

Standard error out functionality is as follows:

|  | error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

error out contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or during the running of this node or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |
