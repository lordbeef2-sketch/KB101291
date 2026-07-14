# NI DOCUMENT BUNDLE: ni-switch

<!--NI_BUNDLE_CHUNK bundle=ni-switch start=501 end=651 -->
<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2593-independent-topology.html language=enus -->
## TOPIC 00501: NI PXI/PXIe-2593 Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2593-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2593-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2593 (NI 2593) supports the independent topology, allowing you to utilize its full routing capabilities. Possible configurations include 3×1 multiplexers and dimensionally flexible sparse matrices. Making a Connection Control the individual relays with the niSwitch Relay Control VI o

### NI PXI/PXIe-2593 Independent Topology

The NI PXI/PXIe-2593 (NI 2593) supports the independent topology, allowing you to utilize
 its full routing capabilities. Possible configurations include 3×1 multiplexers and
 dimensionally flexible sparse matrices.

#### Making a Connection

Control the individual relays with the niSwitch Relay
 Control
 VI or the
 niSwitch_RelayControl
 function (refer to the NI 2593 hardware diagram for relay names). For example, to
 connect CH2 to COM0 on the NI 2593, call the niSwitch Relay Control VI or the
 niSwitch_RelayControl function with relay actionset to Relay Closed and relay
 name set to KA0. Repeat the call to the niSwitch
 Relay Control VI or the niSwitch_RelayControl function to close KB1
 then KC0.

When scanning the NI 2593, use the channel names in the scan list. A typical scan
 list entry could be ch2->com0;. This entry routes the signal
 connected to CH2 to COM0.

#### Valid Internal Channels

To determine the internal channel names, combine the names of all relays adjacent to
 a channel, in alphabetical order, and remove the K's. For example, the channel
 connecting KA0 and KB0 is called A0B0.

For example, to connect CH0 to COM0 using internal channel names, you need to call
 the following:

niSwitch_Connect (exampleSession, ch0, a0b0); niSwitch_Connect
 (exampleSession, a0b0, b0b1c0); niSwitch_Connect (exampleSession, b0b1c0,
 c0c1c2c3d0d1); niSwitch_Connect (exampleSession, c0c1c2c3d0d1, com0);

[IMAGE alt='image' src='GUID-EA0FCE66-BA25-49CF-9178-F5E361C49244-a5.gif']

The following is a list of the valid internal channel names:

| ch0 | a0b0 | b0b1 | b0b1c0 | c0c1c2c3d0d1 | com0 |
| --- | --- | --- | --- | --- | --- |
| ch1 | a1b1 |  |  |  |  |
| ch2 | a2b2 | b2b3 | b2b3c1 |  |  |
| ch3 | a3b3 |  |  |  |  |
| ch4 | a4b4 | b4b5 | b4b5c2 |  |  |
| ch5 | a5b5 |  |  |  |  |
| ch6 | a6b6 | b6b7 | b6b7c3 |  |  |
| ch7 | a7b7 |  |  |  |  |
| ch8 | a8b8 | b8b9 | b8b9c4 | c4c5c6c7d4d5 | com1 |
| ch9 | a9b9 |  |  |  |  |
| ch10 | a10b10 | b10b11 | b10b11c5 |  |  |
| ch11 | a11b11 |  |  |  |  |
| ch12 | a12b12 | b12b13 | b12b13c6 |  |  |
| ch13 | a13b13 |  |  |  |  |
| ch14 | a14b14 | b14b15 | b14b15c7 |  |  |
| ch15 | a15b15 |  |  |  |  |

Parent topic:

NI PXI/PXIe-2593

Related concepts:

- NI PXI/PXIe-2593 3×1 Multiplexers
- Dimensionally Flexible Sparse Matrix
- NI PXI/PXIe-2593 Hardware Diagram
- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2593-triggering.html language=enus -->
## TOPIC 00502: NI PXI/PXIe-2593 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2593-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2593-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This module can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI/PXIe-2593 (NI 2593). Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0

### NI PXI/PXIe-2593 Triggering

This module can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI/PXIe-2593
 (NI 2593).

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |
| Front Connector | External(NISWITCH_VAL_EXTERNAL) | TRIG IN on the front panel |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI 2593.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Front Connector | External(NISWITCH_VAL_EXTERNAL) | TRIG OUT on the front panel |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI/PXIe-2593

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2593.html language=enus -->
## TOPIC 00503: NI PXI/PXIe-2593

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2593.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2593.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2593 (NI 2593) is a high-density multiplexer switch module for the PXI or PXI Express platform. The NI 2593 is designed to handle RF signals up to 500 MHz. Operation Modes The following table lists the supported topology of the NI 2593 and possible operation modes. Topology Software

### NI PXI/PXIe-2593

The NI PXI/PXIe-2593 (NI 2593) is a high-density multiplexer switch module for the PXI or
 PXI Express platform. The NI 2593 is designed to handle RF signals up to 500 MHz.

#### Operation Modes

The following table lists the supported topology of the NI 2593 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Dual 8×1 Multiplexer | 2593/Dual 8x1 Mux(NISWITCH_TOPOLOGY_2593_DUAL_8X1_MUX) |  |  |
| Dual 4×1 Terminated Multiplexer | 2593/Dual 4x1 Terminated Mux(NISWITCH_TOPOLOGY_2593_DUAL_4X1_TERMINATED_MUX) |  |  |
| 16×1 Multiplexer | 2593/16x1 Mux(NISWITCH_TOPOLOGY_2593_16X1_MUX) |  |  |
| 8×1 Terminated Multiplexer | 2593/8x1 Terminated Mux(NISWITCH_TOPOLOGY_2593_8X1_TERMINATED_MUX) |  |  |
| Independent | 2593/Independent(NISWITCH_TOPOLOGY_2593_INDEPENDENT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Operation Modes
- NI PXI/PXIe-2593 Dual 8×1 Multiplexer Topology
- NI PXI/PXIe-2593 Dual 4×1 Terminated Multiplexer Topology
- NI PXI/PXIe-2593 16×1 Multiplexer Topology
- NI PXI/PXIe-2593 8×1 Terminated Multiplexer Topology
- NI PXI/PXIe-2593 Independent Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2524-1-wire-128-1-multiplexer-topolog.html language=enus -->
## TOPIC 00504: NI PXIe-2524 1-Wire 128×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2524-1-wire-128-1-multiplexer-topolog.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2524-1-wire-128-1-multiplexer-topolog.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2524 (NI 2524) in the 1-wire 128×1 multiplexer topology. Making a Connection When using the NI 2524 as a 1-wire 128×1 multiplexer, all channels route to com0. You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect funct

### NI PXIe-2524 1-Wire 128×1 Multiplexer Topology

The following figure represents the NI PXIe-2524 (NI 2524) in the 1-wire 128×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-963099E2-DDC0-41C3-AF7D-7B667158B8DE-a5.gif']

#### Making a Connection

When using the NI 2524 as a 1-wire 128×1 multiplexer, all channels route to com0. You can
 control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to connect channel 1 to com0, call niSwitch_Connect(vi, "ch1",
 "com0"). To disconnect channel 1 from com0, call niSwitch_Disconnect(vi,
 "ch1", "com0").

#### Pinout

The following figure identifies the pins for the NI 2524 in the 1-wire 128×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-15654258-B24F-4DDB-B6B9-5FE16CC00158-a5.gif']

The following table lists channel pairings and relay assignments for the NI 2524 in the
 1-wire 128×1 multiplexer topology.

| 1-Wire 128×1 Channel Name |  | Relay Name |
| --- | --- | --- |
| CH0 | CH4 | kb0s1 |
| CH1 | CH5 | kb0s2 |
| CH2 | CH6 | kb0s3 |
| CH3 | CH7 | kb0s4 |
| CH8 | CH12 | kb1s1 |
| CH9 | CH13 | kb1s2 |
| CH10 | CH14 | kb1s3 |
| CH11 | CH15 | kb1s4 |
| CH16 | CH20 | kb2s1 |
| CH17 | CH21 | kb2s2 |
| CH18 | CH22 | kb2s3 |
| CH19 | CH23 | kb2s4 |
| CH24 | CH28 | kb3s1 |
| CH25 | CH29 | kb3s2 |
| CH26 | CH30 | kb3s3 |
| CH27 | CH31 | kb3s4 |
| CH32 | CH36 | kb4s1 |
| CH33 | CH37 | kb4s2 |
| CH34 | CH38 | kb4s3 |
| CH35 | CH39 | kb4s4 |
| CH40 | CH44 | kb5s1 |
| CH41 | CH45 | kb5s2 |
| CH42 | CH46 | kb5s3 |
| CH43 | CH47 | kb5s4 |
| CH48 | CH52 | kb6s1 |
| CH49 | CH53 | kb6s2 |
| CH50 | CH54 | kb6s3 |
| CH51 | CH55 | kb6s4 |
| CH56 | CH60 | kb7s1 |
| CH57 | CH61 | kb7s2 |
| CH58 | CH62 | kb7s3 |
| CH59 | CH63 | kb7s4 |
| CH64 | CH68 | kb8s1 |
| CH65 | CH69 | kb8s2 |
| CH66 | CH70 | kb8s3 |
| CH67 | CH71 | kb8s4 |
| CH72 | CH76 | kb9s1 |
| CH73 | CH77 | kb9s2 |
| CH74 | CH78 | kb9s3 |
| CH75 | CH79 | kb9s4 |
| CH80 | CH84 | kb10s1 |
| CH81 | CH85 | kb10s2 |
| CH82 | CH86 | kb10s3 |
| CH83 | CH87 | kb10s4 |
| CH88 | CH92 | kb11s1 |
| CH89 | CH93 | kb11s2 |
| CH90 | CH94 | kb11s3 |
| CH91 | CH95 | kb11s4 |
| CH96 | CH100 | kb12s1 |
| CH97 | CH101 | kb12s2 |
| CH98 | CH102 | kb12s3 |
| CH99 | CH103 | kb12s4 |
| CH104 | CH108 | kb13s1 |
| CH105 | CH109 | kb13s2 |
| CH106 | CH110 | kb13s3 |
| CH107 | CH111 | kb13s4 |
| CH112 | CH116 | kb14s1 |
| CH113 | CH117 | kb14s2 |
| CH114 | CH118 | kb14s3 |
| CH115 | CH119 | kb14s4 |
| CH120 | CH124 | kb15s1 |
| CH121 | CH125 | kb15s2 |
| CH122 | CH126 | kb15s3 |
| CH123 | CH127 | kb15s4 |
| CH123 | CH127 | kb15s4 |
| COM 0 |  | kb0com1 |
| kb0com2 |  |  |
| kbc01 |  |  |
| kb1com1 |  |  |
| kb1com2 |  |  |
| kb1com2 |  |  |
| kbc02 |  |  |
| kb2com1 |  |  |
| kb2com2 |  |  |
| kbc23 |  |  |
| kb3com1 |  |  |
| kb3com2 |  |  |
| kbc04 |  |  |
| kb4com1 |  |  |
| kb4com2 |  |  |
| kbc45 |  |  |
| kb5com1 |  |  |
| kb5com2 |  |  |
| kbc46 |  |  |
| kb6com1 |  |  |
| kb6com2 |  |  |
| kbc67 |  |  |
| kb7com1 |  |  |
| kb7com2 |  |  |
| kbc08 |  |  |
| kb8com1 |  |  |
| kb8com2 |  |  |
| kbc89 |  |  |
| kb9com1 |  |  |
| kb9com2 |  |  |
| kbc810 |  |  |
| kb10com1 |  |  |
| kb10com2 |  |  |
| kbc1011 |  |  |
| kb11com1 |  |  |
| kb11com2 |  |  |
| kbc812 |  |  |
| kb12com1 |  |  |
| kb12com2 |  |  |
| kbc1213 |  |  |
| kb13com1 |  |  |
| kb13com2 |  |  |
| kbc1214 |  |  |
| kb14com1 |  |  |
| kb14com2 |  |  |
| kbc1415 |  |  |
| kb15com1 |  |  |
| kb15com2 |  |  |

Parent topic:

NI PXIe-2524

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2524-1-wire-dual-64-1-multiplexer-top.html language=enus -->
## TOPIC 00505: NI PXIe-2524 1-Wire Dual 64×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2524-1-wire-dual-64-1-multiplexer-top.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2524-1-wire-dual-64-1-multiplexer-top.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2524 (NI 2524) in the 1-wire dual 64×1 multiplexer topology. Making a Connection When using the NI 2524 as a 1-wire dual 64×1 multiplexer, all channels in a given bank route to the corresponding com. You can control the channels using the niSwitch Connect

### NI PXIe-2524 1-Wire Dual 64×1 Multiplexer Topology

The following figure represents the NI PXIe-2524 (NI 2524) in the 1-wire dual 64×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-973EBC25-A2FE-4306-A068-2CC1F39445B1-a5.gif']

#### Making a Connection

When using the NI 2524 as a 1-wire dual 64×1 multiplexer, all channels in a given
 bank route to the corresponding com. You can control the channels using the niSwitch
 Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to connect channel 1 to com0, call niSwitch_Connect(vi, "ch1",
 "com0"). To disconnect channel 1 from com0, call
 niSwitch_Disconnect(vi, "ch1", "com0").

#### Pinout

The following figure identifies the pins for the NI 2524 in the 1-wire dual 64×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-15654258-B24F-4DDB-B6B9-5FE16CC00158-a5.gif']

The following table lists channel pairings and relay assignments for the NI 2524 in
 the 1-wire dual 64×1 multiplexer topology.

| 1-Wire Dual 64×1 Channel Name |  | Relay Name |
| --- | --- | --- |
| CH0 | CH4 | kb0s1 |
| CH0 | CH4 | kb0s1 |
| CH1 | CH5 | kb0s2 |
| CH2 | CH6 | kb0s3 |
| CH3 | CH7 | kb0s4 |
| CH8 | CH12 | kb1s1 |
| CH9 | CH13 | kb1s2 |
| CH10 | CH14 | kb1s3 |
| CH11 | CH15 | kb1s4 |
| CH16 | CH20 | kb2s1 |
| CH17 | CH21 | kb2s2 |
| CH18 | CH22 | kb2s3 |
| CH19 | CH23 | kb2s4 |
| CH24 | CH28 | kb3s1 |
| CH25 | CH29 | kb3s2 |
| CH26 | CH30 | kb3s3 |
| CH27 | CH31 | kb3s4 |
| CH32 | CH36 | kb4s1 |
| CH33 | CH37 | kb4s2 |
| CH34 | CH38 | kb4s3 |
| CH35 | CH39 | kb4s4 |
| CH40 | CH44 | kb5s1 |
| CH41 | CH45 | kb5s2 |
| CH42 | CH46 | kb5s3 |
| CH43 | CH47 | kb5s4 |
| CH48 | CH52 | kb6s1 |
| CH49 | CH53 | kb6s2 |
| CH50 | CH54 | kb6s3 |
| CH51 | CH55 | kb6s4 |
| CH56 | CH60 | kb7s1 |
| CH57 | CH61 | kb7s2 |
| CH58 | CH62 | kb7s3 |
| CH59 | CH63 | kb7s4 |
| CH64 | CH68 | kb8s1 |
| CH65 | CH69 | kb8s2 |
| CH66 | CH70 | kb8s3 |
| CH67 | CH71 | kb8s4 |
| CH72 | CH76 | kb9s1 |
| CH73 | CH77 | kb9s2 |
| CH74 | CH78 | kb9s3 |
| CH75 | CH79 | kb9s4 |
| CH80 | CH84 | kb10s1 |
| CH81 | CH85 | kb10s2 |
| CH82 | CH86 | kb10s3 |
| CH83 | CH87 | kb10s4 |
| CH88 | CH92 | kb11s1 |
| CH89 | CH93 | kb11s2 |
| CH90 | CH94 | kb11s3 |
| CH91 | CH95 | kb11s4 |
| CH96 | CH100 | kb12s1 |
| CH97 | CH101 | kb12s2 |
| CH98 | CH102 | kb12s3 |
| CH99 | CH103 | kb12s4 |
| CH104 | CH108 | kb13s1 |
| CH105 | CH109 | kb13s2 |
| CH106 | CH110 | kb13s3 |
| CH107 | CH111 | kb13s4 |
| CH112 | CH116 | kb14s1 |
| CH113 | CH117 | kb14s2 |
| CH114 | CH118 | kb14s3 |
| CH115 | CH119 | kb14s4 |
| CH120 | CH124 | kb15s1 |
| CH121 | CH125 | kb15s2 |
| CH122 | CH126 | kb15s3 |
| CH123 | CH127 | kb15s4 |
| CH123 | CH127 | kb15s4 |
| COM 0 |  | kb0com1 |
| kb0com2 |  |  |
| kbc01 |  |  |
| kb1com1 |  |  |
| kb1com2 |  |  |
| kbc02 |  |  |
| kb2com1 |  |  |
| kb2com2 |  |  |
| kbc23 |  |  |
| kb3com1 |  |  |
| kb3com2 |  |  |
| kbc04 |  |  |
| kb4com1 |  |  |
| kb4com2 |  |  |
| kbc45 |  |  |
| kb5com1 |  |  |
| kb5com2 |  |  |
| kbc46 |  |  |
| kb6com1 |  |  |
| kb6com2 |  |  |
| kbc67 |  |  |
| kb7com1 |  |  |
| kb7com2 |  |  |
| COM 8 |  | kb8com1 |
| kb8com2 |  |  |
| kbc89 |  |  |
| kb9com1 |  |  |
| kb9com2 |  |  |
| kbc810 |  |  |
| kb10com1 |  |  |
| kb10com2 |  |  |
| kbc1011 |  |  |
| kb11com1 |  |  |
| kb11com2 |  |  |
| kbc812 |  |  |
| kb12com1 |  |  |
| kb12com2 |  |  |
| kbc1213 |  |  |
| kb13com1 |  |  |
| kb13com2 |  |  |
| kbc1214 |  |  |
| kb14com1 |  |  |
| kb14com2 |  |  |
| kbc1415 |  |  |
| kb15com1 |  |  |
| kb15com2 |  |  |

Parent topic:

NI PXIe-2524

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2524-1-wire-octal-16-1-multiplexer-to.html language=enus -->
## TOPIC 00506: NI PXIe-2524 1-Wire Octal 16×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2524-1-wire-octal-16-1-multiplexer-to.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2524-1-wire-octal-16-1-multiplexer-to.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2524 (NI 2524) in the 1-wire octal 16×1 multiplexer topology. Making a Connection When using the NI 2524 as a 1-wire octal 16×1 multiplexer, all channels in a given bank route to the corresponding com. You can control the channels using the niSwitch Connec

### NI PXIe-2524 1-Wire Octal 16×1 Multiplexer Topology

The following figure represents the NI PXIe-2524 (NI 2524) in the 1-wire octal 16×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-B453F208-F914-413D-B6EB-FE0319176703-a5.gif']

#### Making a Connection

When using the NI 2524 as a 1-wire octal 16×1 multiplexer, all channels in a given
 bank route to the corresponding com. You can control the channels using the niSwitch
 Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to connect channel 1 to com0, call niSwitch_Connect(vi, "ch1",
 "com0"). To disconnect channel 1 from com0, call
 niSwitch_Disconnect(vi, "ch1", "com0").

#### Pinout

The following figure identifies the pins for the NI 2524 in the 1-wire octal 16×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-15654258-B24F-4DDB-B6B9-5FE16CC00158-a5.gif']

The following table lists channel pairings and relay assignments for the NI 2524 in
 the 1-wire octal 16×1 multiplexer topology.

| 1-Wire Octal 16×1 Channel Name |  | Relay Name |
| --- | --- | --- |
| CH0 | CH4 | kb0s1 |
| CH0 | CH4 | kb0s1 |
| CH1 | CH5 | kb0s2 |
| CH2 | CH6 | kb0s3 |
| CH3 | CH7 | kb0s4 |
| CH8 | CH12 | kb1s1 |
| CH9 | CH13 | kb1s2 |
| CH10 | CH14 | kb1s3 |
| CH11 | CH15 | kb1s4 |
| CH16 | CH20 | kb2s1 |
| CH17 | CH21 | kb2s2 |
| CH18 | CH22 | kb2s3 |
| CH19 | CH23 | kb2s4 |
| CH24 | CH28 | kb3s1 |
| CH25 | CH29 | kb3s2 |
| CH26 | CH30 | kb3s3 |
| CH27 | CH31 | kb3s4 |
| CH32 | CH36 | kb4s1 |
| CH33 | CH37 | kb4s2 |
| CH34 | CH38 | kb4s3 |
| CH35 | CH39 | kb4s4 |
| CH40 | CH44 | kb5s1 |
| CH41 | CH45 | kb5s2 |
| CH42 | CH46 | kb5s3 |
| CH43 | CH47 | kb5s4 |
| CH48 | CH52 | kb6s1 |
| CH49 | CH53 | kb6s2 |
| CH50 | CH54 | kb6s3 |
| CH51 | CH55 | kb6s4 |
| CH56 | CH60 | kb7s1 |
| CH57 | CH61 | kb7s2 |
| CH58 | CH62 | kb7s3 |
| CH59 | CH63 | kb7s4 |
| CH64 | CH68 | kb8s1 |
| CH65 | CH69 | kb8s2 |
| CH66 | CH70 | kb8s3 |
| CH67 | CH71 | kb8s4 |
| CH72 | CH76 | kb9s1 |
| CH73 | CH77 | kb9s2 |
| CH74 | CH78 | kb9s3 |
| CH75 | CH79 | kb9s4 |
| CH80 | CH84 | kb10s1 |
| CH81 | CH85 | kb10s2 |
| CH82 | CH86 | kb10s3 |
| CH83 | CH87 | kb10s4 |
| CH88 | CH92 | kb11s1 |
| CH89 | CH93 | kb11s2 |
| CH90 | CH94 | kb11s3 |
| CH91 | CH95 | kb11s4 |
| CH96 | CH100 | kb12s1 |
| CH97 | CH101 | kb12s2 |
| CH98 | CH102 | kb12s3 |
| CH99 | CH103 | kb12s4 |
| CH104 | CH108 | kb13s1 |
| CH105 | CH109 | kb13s2 |
| CH106 | CH110 | kb13s3 |
| CH107 | CH111 | kb13s4 |
| CH112 | CH116 | kb14s1 |
| CH113 | CH117 | kb14s2 |
| CH114 | CH118 | kb14s3 |
| CH115 | CH119 | kb14s4 |
| CH120 | CH124 | kb15s1 |
| CH121 | CH125 | kb15s2 |
| CH122 | CH126 | kb15s3 |
| CH123 | CH127 | kb15s4 |
| CH123 | CH127 | kb15s4 |
| COM 0 |  | kb0com1 |
| kb0com2 |  |  |
| kbc01 |  |  |
| kb1com1 |  |  |
| kb1com2 |  |  |
| COM 2 |  | kb2com1 |
| kb2com2 |  |  |
| kbc23 |  |  |
| kb3com1 |  |  |
| kb3com2 |  |  |
| COM 4 |  | kb4com1 |
| kb4com2 |  |  |
| kbc45 |  |  |
| kb5com1 |  |  |
| kb5com2 |  |  |
| COM 6 |  | kb6com1 |
| kb6com2 |  |  |
| kbc67 |  |  |
| kb7com1 |  |  |
| kb7com2 |  |  |
| COM 8 |  | kb8com1 |
| kb8com2 |  |  |
| kbc89 |  |  |
| kb9com1 |  |  |
| kb9com2 |  |  |
| COM 10 |  | kb10com1 |
| kb10com2 |  |  |
| kbc1011 |  |  |
| kb11com1 |  |  |
| kb11com2 |  |  |
| COM 12 |  | kb12com1 |
| kb12com2 |  |  |
| kbc1213 |  |  |
| kb13com1 |  |  |
| kb13com2 |  |  |
| COM 14 |  | kb14com1 |
| kb14com2 |  |  |
| kbc1415 |  |  |
| kb15com1 |  |  |
| kb15com2 |  |  |

Parent topic:

NI PXIe-2524

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2524-1-wire-quad-32-1-multiplexer-top.html language=enus -->
## TOPIC 00507: NI PXIe-2524 1-Wire Quad 32×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2524-1-wire-quad-32-1-multiplexer-top.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2524-1-wire-quad-32-1-multiplexer-top.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2524 (NI 2524) in the 1-wire quad 32×1 multiplexer topology. Making a Connection When using the NI 2524 quad 32×1, all channels in a given bank route to the corresponding com. You can control the channels using the niSwitch Connect Channels VI or the niSwi

### NI PXIe-2524 1-Wire Quad 32×1 Multiplexer Topology

The following figure represents the NI PXIe-2524 (NI 2524) in the 1-wire quad 32×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-717589BC-80E0-4976-8E7E-90192D469D14-a5.gif']

#### Making a Connection

When using the NI 2524 quad 32×1, all channels in a given bank route to the
 corresponding com. You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to connect channel 1 to com0, call niSwitch_Connect(vi, "ch1",
 "com0"). To disconnect channel 1 from com0, call
 niSwitch_Disconnect(vi, "ch1", "com0").

#### Pinout

The following figure identifies the pins for the NI 2524 in the 1-wire quad 32×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-15654258-B24F-4DDB-B6B9-5FE16CC00158-a5.gif']

The following table lists channel pairings and relay assignments for the NI 2524 in
 the 1-wire quad 32×1 multiplexer topology.

| 1-Wire Quad 32×1 Channel Name |  | Relay Name |
| --- | --- | --- |
| CH0 | CH4 | kb0s1 |
| CH0 | CH4 | kb0s1 |
| CH1 | CH5 | kb0s2 |
| CH2 | CH6 | kb0s3 |
| CH3 | CH7 | kb0s4 |
| CH8 | CH12 | kb1s1 |
| CH9 | CH13 | kb1s2 |
| CH10 | CH14 | kb1s3 |
| CH11 | CH15 | kb1s4 |
| CH16 | CH20 | kb2s1 |
| CH17 | CH21 | kb2s2 |
| CH18 | CH22 | kb2s3 |
| CH19 | CH23 | kb2s4 |
| CH24 | CH28 | kb3s1 |
| CH25 | CH29 | kb3s2 |
| CH26 | CH30 | kb3s3 |
| CH27 | CH31 | kb3s4 |
| CH32 | CH36 | kb4s1 |
| CH33 | CH37 | kb4s2 |
| CH34 | CH38 | kb4s3 |
| CH35 | CH39 | kb4s4 |
| CH40 | CH44 | kb5s1 |
| CH41 | CH45 | kb5s2 |
| CH42 | CH46 | kb5s3 |
| CH43 | CH47 | kb5s4 |
| CH48 | CH52 | kb6s1 |
| CH49 | CH53 | kb6s2 |
| CH50 | CH54 | kb6s3 |
| CH51 | CH55 | kb6s4 |
| CH56 | CH60 | kb7s1 |
| CH57 | CH61 | kb7s2 |
| CH58 | CH62 | kb7s3 |
| CH59 | CH63 | kb7s4 |
| CH64 | CH68 | kb8s1 |
| CH65 | CH69 | kb8s2 |
| CH66 | CH70 | kb8s3 |
| CH67 | CH71 | kb8s4 |
| CH72 | CH76 | kb9s1 |
| CH73 | CH77 | kb9s2 |
| CH74 | CH78 | kb9s3 |
| CH75 | CH79 | kb9s4 |
| CH80 | CH84 | kb10s1 |
| CH81 | CH85 | kb10s2 |
| CH82 | CH86 | kb10s3 |
| CH83 | CH87 | kb10s4 |
| CH88 | CH92 | kb11s1 |
| CH89 | CH93 | kb11s2 |
| CH90 | CH94 | kb11s3 |
| CH91 | CH95 | kb11s4 |
| CH96 | CH100 | kb12s1 |
| CH97 | CH101 | kb12s2 |
| CH98 | CH102 | kb12s3 |
| CH99 | CH103 | kb12s4 |
| CH104 | CH108 | kb13s1 |
| CH105 | CH109 | kb13s2 |
| CH106 | CH110 | kb13s3 |
| CH107 | CH111 | kb13s4 |
| CH112 | CH116 | kb14s1 |
| CH113 | CH117 | kb14s2 |
| CH114 | CH118 | kb14s3 |
| CH115 | CH119 | kb14s4 |
| CH120 | CH124 | kb15s1 |
| CH121 | CH125 | kb15s2 |
| CH122 | CH126 | kb15s3 |
| CH123 | CH127 | kb15s4 |
| CH123 | CH127 | kb15s4 |
| COM 0 |  | kb0com1 |
| kb0com2 |  |  |
| kbc01 |  |  |
| kb1com1 |  |  |
| kb1com2 |  |  |
| kbc02 |  |  |
| kb2com1 |  |  |
| kb2com2 |  |  |
| kbc23 |  |  |
| kb3com1 |  |  |
| kb3com2 |  |  |
| COM 4 |  | kb4com1 |
| kb4com2 |  |  |
| kbc45 |  |  |
| kb5com1 |  |  |
| kb5com2 |  |  |
| kbc46 |  |  |
| kb6com1 |  |  |
| kb6com2 |  |  |
| kbc67 |  |  |
| kb7com1 |  |  |
| kb7com2 |  |  |
| COM 8 |  | kb8com1 |
| kb8com2 |  |  |
| kbc89 |  |  |
| kb9com1 |  |  |
| kb9com2 |  |  |
| kbc810 |  |  |
| kb10com1 |  |  |
| kb10com2 |  |  |
| kbc1011 |  |  |
| kb11com1 |  |  |
| kb11com2 |  |  |
| COM 12 |  | kb12com1 |
| kb12com2 |  |  |
| kbc1213 |  |  |
| kb13com1 |  |  |
| kb13com2 |  |  |
| kbc1214 |  |  |
| kb14com1 |  |  |
| kb14com2 |  |  |
| kbc1415 |  |  |
| kb15com1 |  |  |
| kb15com2 |  |  |

Parent topic:

NI PXIe-2524

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2524-1-wire-sixteen-8-1-multiplexer-t.html language=enus -->
## TOPIC 00508: NI PXIe-2524 1-Wire Sixteen 8×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2524-1-wire-sixteen-8-1-multiplexer-t.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2524-1-wire-sixteen-8-1-multiplexer-t.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2524 (NI 2524) in the 1-wire sixteen 8×1 multiplexer topology. Making a Connection When using the NI 2524 as a 1-wire sixteen 8×1 multiplexer, all channels in a given bank route to the corresponding com. You can control the channels using the niSwitch Conn

### NI PXIe-2524 1-Wire Sixteen 8×1 Multiplexer Topology

The following figure represents the NI PXIe-2524 (NI 2524) in the 1-wire sixteen 8×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-AB1C42B7-5756-46C9-8BCA-7F5BD507092A-a5.gif']

#### Making a Connection

When using the NI 2524 as a 1-wire sixteen 8×1 multiplexer, all channels in a given
 bank route to the corresponding com. You can control the channels using the niSwitch
 Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to connect channel 1 to com0, call niSwitch_Connect(vi, "ch1",
 "com0"). To disconnect channel 1 from com0, call
 niSwitch_Disconnect(vi, "ch1", "com0").

#### Pinout

The following figure identifies the pins for the NI 2524 in the 1-wire sixteen 8×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-15654258-B24F-4DDB-B6B9-5FE16CC00158-a5.gif']

The following table lists channel pairings and relay assignments for the NI 2524 in
 the 1-wire sixteen 8×1 multiplexer topology.

| 1-Wire Sixteen 8×1 Channel Name |  | Relay Name |
| --- | --- | --- |
| CH0 | CH4 | kb0s1 |
| CH0 | CH4 | kb0s1 |
| CH1 | CH5 | kb0s2 |
| CH2 | CH6 | kb0s3 |
| CH3 | CH7 | kb0s4 |
| CH8 | CH12 | kb1s1 |
| CH9 | CH13 | kb1s2 |
| CH10 | CH14 | kb1s3 |
| CH11 | CH15 | kb1s4 |
| CH16 | CH20 | kb2s1 |
| CH17 | CH21 | kb2s2 |
| CH18 | CH22 | kb2s3 |
| CH19 | CH23 | kb2s4 |
| CH24 | CH28 | kb3s1 |
| CH25 | CH29 | kb3s2 |
| CH26 | CH30 | kb3s3 |
| CH27 | CH31 | kb3s4 |
| CH32 | CH36 | kb4s1 |
| CH33 | CH37 | kb4s2 |
| CH34 | CH38 | kb4s3 |
| CH35 | CH39 | kb4s4 |
| CH40 | CH44 | kb5s1 |
| CH41 | CH45 | kb5s2 |
| CH42 | CH46 | kb5s3 |
| CH43 | CH47 | kb5s4 |
| CH48 | CH52 | kb6s1 |
| CH49 | CH53 | kb6s2 |
| CH50 | CH54 | kb6s3 |
| CH51 | CH55 | kb6s4 |
| CH56 | CH60 | kb7s1 |
| CH57 | CH61 | kb7s2 |
| CH58 | CH62 | kb7s3 |
| CH59 | CH63 | kb7s4 |
| CH64 | CH68 | kb8s1 |
| CH65 | CH69 | kb8s2 |
| CH66 | CH70 | kb8s3 |
| CH67 | CH71 | kb8s4 |
| CH72 | CH76 | kb9s1 |
| CH73 | CH77 | kb9s2 |
| CH74 | CH78 | kb9s3 |
| CH75 | CH79 | kb9s4 |
| CH80 | CH84 | kb10s1 |
| CH81 | CH85 | kb10s2 |
| CH82 | CH86 | kb10s3 |
| CH83 | CH87 | kb10s4 |
| CH88 | CH92 | kb11s1 |
| CH89 | CH93 | kb11s2 |
| CH90 | CH94 | kb11s3 |
| CH91 | CH95 | kb11s4 |
| CH96 | CH100 | kb12s1 |
| CH97 | CH101 | kb12s2 |
| CH98 | CH102 | kb12s3 |
| CH99 | CH103 | kb12s4 |
| CH104 | CH108 | kb13s1 |
| CH105 | CH109 | kb13s2 |
| CH106 | CH110 | kb13s3 |
| CH107 | CH111 | kb13s4 |
| CH112 | CH116 | kb14s1 |
| CH113 | CH117 | kb14s2 |
| CH114 | CH118 | kb14s3 |
| CH115 | CH119 | kb14s4 |
| CH120 | CH124 | kb15s1 |
| CH121 | CH125 | kb15s2 |
| CH122 | CH126 | kb15s3 |
| CH123 | CH127 | kb15s4 |
| CH123 | CH127 | kb15s4 |
| COM 0 |  | kb0com1 |
| kb0com2 |  |  |
| COM 1 |  | kb0com1 |
| kb1com2 |  |  |
| COM 2 |  | kb2com1 |
| kb2com2 |  |  |
| COM 3 |  | kb3com1 |
| kb3com2 |  |  |
| COM 4 |  | kb4com1 |
| kb4com2 |  |  |
| COM 5 |  | kb5com1 |
| kb5com2 |  |  |
| COM 6 |  | kb6com1 |
| kb6com2 |  |  |
| COM 7 |  | kb7com1 |
| kb7com2 |  |  |
| COM 8 |  | kb8com1 |
| kb8com2 |  |  |
| COM 9 |  | kb9com1 |
| kb9com2 |  |  |
| COM 10 |  | kb10com1 |
| kb10com2 |  |  |
| COM 11 |  | kb11com1 |
| kb10com2 |  |  |
| COM 12 |  | kb12com1 |
| kb12com2 |  |  |
| COM 13 |  | kb13com1 |
| kb13com1 |  |  |
| COM 14 |  | kb14com1 |
| kb14com2 |  |  |
| COM 15 |  | kb15com1 |
| kb15com2 |  |  |

Parent topic:

NI PXIe-2524

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2524-front-panel.html language=enus -->
## TOPIC 00509: NI PXIe-2524 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2524-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2524-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXIe-2524 front panel.

### NI PXIe-2524 Front Panel

The following figure illustrates the NI PXIe-2524 front panel.

[IMAGE alt='image' src='GUID-A88C4478-2D62-477C-AD5F-519BDC8AC7D1-a5.gif']

Parent topic:

NI PXIe-2524

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2524-hardware-diagram.html language=enus -->
## TOPIC 00510: NI PXIe-2524 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2524-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2524-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXIe-2524.

### NI PXIe-2524 Hardware Diagram

The following figure shows the hardware diagram for the NI PXIe-2524.

[IMAGE alt='image' src='GUID-422FDDD1-55EC-4841-9B59-D8B48E517645-a5.gif']

Parent topic:

NI PXIe-2524

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2524-relay-replacement.html language=enus -->
## TOPIC 00511: NI PXIe-2524 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2524-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2524-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2524 uses electromechanical armature relays. Refer to the following tables for information about ordering replacement relays. Use relays of the same brand that you are replacing. Relay Manufacturer Part Number Tyco 1462043-6 Relay Kit Part Number National Instruments (10 relays, Tyco) 78

### NI PXIe-2524 Relay Replacement

The NI PXIe-2524 uses electromechanical armature relays.

Refer to the following tables for information about ordering replacement relays. Use relays
 of the same brand that you are replacing.

| Relay Manufacturer | Part Number |
| --- | --- |
| Tyco | 1462043-6 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays, Tyco) | 782461-10 |

Complete the following steps to locate, remove, and replace a failed relay.

#### Locate the Relay

1. Ground yourself using a grounding strap or a ground connected to your PXI Express
 chassis. Note Properly grounding yourself prevents damage to your module
 from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table for relay
 locations. NI PXIe-2524 PCB 1 
 [IMAGE alt='image' src='GUID-BEFB67B4-67DB-4231-B343-CDC0C0BBA08A-a5.gif'] 
 Table 1.NI PXIe-2524 PCB 1 Relay LocationsRelay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designatorkb0s1
 K1
 kb4s1
 K33
 kb8s1
 K58
 kb12s1
 K85
 kbc01
 K12kb0s2
 K3
 kb4s2
 K33
 kb8s2
 K60
 kb12s2
 K87
 kbc23
 K19kb0s3
 K5
 kb4s3
 K37
 kb8s3
 K62
 kb12s3
 K89
 kbc45
 K23kb0s4
 K7
 kb4s4
 K39
 kb8s4
 K64
 kb12s4
 K91
 kbc67
 K66kb0com1
 K9
 kb4com1
 K41
 kb8com1
 K67
 kb12com1
 K95
 kbc89
 K93kb0com2
 K10
 kb4com2
 K42
 kb8com2
 K68
 kb12com2
 K94
 kbc1011
 K84kb1s1
 K2
 kb5s1
 K34
 kb9s1
 K59
 kb13s1
 K86
 kbc1213
 K111kb1s2
 K4
 kb5s2
 K36
 kb9s2
 K61
 kb13s2
 K88
 kbc1415
 K102kb1s3
 K6
 kb5s3
 K38
 kb9s3
 K63
 kb13s3
 K90
 kbc02
 K11kb1s4
 K8
 kb5s4
 K40
 kb9s4
 K65
 kb13s4
 K92
 kbc46
 K75kb1com1
 K13
 kb5com1
 K43
 kb9com1
 K69
 kb13com1
 K96
 kbc810
 K16kb1com2
 K14
 kb5com2
 K44
 kb9com2
 K70
 kb13com2
 K97
 kbc1214
 K15kb2s1
 K25
 kb6s1
 K49
 kb10s1
 K76
 kb14s1
 K103
 kbc04
 K20kb2s2
 K27
 kb6s2
 K51
 kb10s2
 K78
 kb14s2
 K105
 kbc812
 K57kb2s3
 K29
 kb6s3
 K53
 kb10s3
 K80
 kb14s3
 K107
 kbc08
 K24kb2s4
 K31
 kb6s4
 K55
 kb10s4
 K82
 kb14s4
 K109kb2com1
 K18
 kb6com1
 K46
 kb10com1
 K72
 kb14com1
 K99kb2com2
 K17
 kb6com2
 K45
 kb10com2
 K71
 kb14com2
 K98kb3s1
 K26
 kb7s1
 K50
 kb11s1
 K77
 kb15s1
 K104kb3s2
 K28
 kb7s2
 K52
 kb11s2
 K79
 kb15s2
 K106kb3s3
 K30
 kb7s3
 K54
 kb11s3
 K81
 kb15s3
 K108kb3s4
 K32
 kb7s4
 K56
 kb11s4
 K83
 kb15s4
 K110kb3com1
 K22
 kb7com1
 K48
 kb11com1
 K74
 kb15com1
 K100kb3com2
 K21
 kb7com2
 K47
 kb11com2
 K73
 kb15com2
 K101
3. Locate the assembly and serial number labels on the board with the relay you want to
 replace. White labels indicate the board was assembled using lead solder (Sn 63 Pb 37).
 Green labels indicate the board was assembled using lead-free solder (Sn 96.5 Ag 3.0 Cu
 0.5). Lead-free assemblies have assembly numbers ending in L. [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']

#### Replace the Relay

Note

Caution

Caution

Make sure you have the following:

- Temperature-regulated soldering iron set to 316 °C (600 °F) for lead solder rework or
 371 °C (700 °F) for lead-free solder rework
- 63/37 Tin/Lead solder (flux core) for lead solder rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Complete the following steps to replace a relay:

1. Locate the assembly and serial number labels on the board with the relay you want to
 replace. White labels indicate the board was assembled using lead solder (Sn 63 Pb 37).
 Green labels indicate the board was assembled using lead-free solder (Sn 96.5 Ag 3.0 Cu
 0.5). Lead-free assemblies have assembly numbers ending in L. The different label types
 are shown in the following figure. [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']
2. Replace the relay as you would any other through-hole part. Trim the replaced relay to
 no more than 0.41 mm (0.016 inch) from the PCB.

Tip

Switch
 Soft Front Panel Help

Parent topic:

NI PXIe-2524

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2524.html language=enus -->
## TOPIC 00512: NI PXIe-2524

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2524.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2524.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2524 (NI 2524) is a high-voltage multiplexer relay module for the PXI Express platform. The NI 2524 is composed of 111 armature relays. For certain applications, you may need to increase the default settling time. Refer to Adding Additional Settling Time for more information. Switching

### NI PXIe-2524

The NI PXIe-2524 (NI 2524) is a high-voltage multiplexer relay module for the PXI Express
 platform. The NI 2524 is composed of 111 armature relays.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2524 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 128x1 Multiplexer | 2524/1-Wire 128x1 Mux(NISWITCH_TOPOLOGY_2524_1_WIRE_128X1_MUX) |  |  |
| 1-Wire Dual 64×1 Multiplexer | 2524/1-Wire Dual 64x1 Mux(NISWITCH_TOPOLOGY_2524_1_WIRE_DUAL_64X1_MUX) |  |  |
| 1-Wire Quad 32×1 Multiplexer | 2524/1-Wire Quad 32x1 Mux(NISWITCH_TOPOLOGY_2524_1_WIRE_QUAD_32X1_MUX) |  |  |
| 1-Wire Octal 16×1 Multiplexer | 2524/1-Wire Octal 16x1 Mux(NISWITCH_TOPOLOGY_2524_1_WIRE_OCTAL_16X1_MUX) |  |  |
| 1-Wire Sixteen 8×1 Multiplexer | 2524/1-Wire Sixteen 8x1 Mux(NISWITCH_TOPOLOGY_2524_1_WIRE_SIXTEEN_8X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Armature Relays
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXIe-2524 1-Wire 128×1 Multiplexer Topology
- NI PXIe-2524 1-Wire Dual 64×1 Multiplexer Topology
- NI PXIe-2524 1-Wire Quad 32×1 Multiplexer Topology
- NI PXIe-2524 1-Wire Sixteen 8×1 Multiplexer Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2525-2-wire-64-1-multiplexer-topology.html language=enus -->
## TOPIC 00513: NI PXIe-2525 2-Wire 64×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2525-2-wire-64-1-multiplexer-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2525-2-wire-64-1-multiplexer-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2525 (NI 2525) in the 2-wire 64×1 multiplexer topology. Making a Connection When using the NI 2525 as a 2-wire 64×1 multiplexer, all positive leads (ch0+ through ch63+) route to com0+, and all negative leads (ch0– through ch63–) route to com0–. The pair co

### NI PXIe-2525 2-Wire 64×1 Multiplexer Topology

The following figure represents the NI PXIe-2525 (NI 2525) in the 2-wire 64×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-96EE8072-BE05-4CC9-95C1-E7B9E7220EFC-a5.gif']

#### Making a Connection

When using the NI 2525 as a 2-wire 64×1 multiplexer, all positive leads (ch0+ through
 ch63+) route to com0+, and all negative leads (ch0– through ch63–) route to com0–.
 The pair com0+ and com0– is addressed collectively as com0 in software.

The immediate operation command (the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function), with parameters ch2 and com0, result in
 the following connections:

signal connected to ch2+ is routed to com0+

signal connected to ch2– is routed to com0–

#### Pinout

The following figure identifies the pins for the NI 2525 in the 2-wire 64×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-21751E8E-2ACF-4C11-98B1-C2412952F3D7-a5.gif']

The following table lists the channel pairings and relay assignments for the NI 2525
 in the 2-wire 64×1 multiplexer topology.

| 2-Wire 64×1 Channel Name | Relay Name |
| --- | --- |
| CH0 | k0 |
| CH1 | k1 |
| CH2 | k2 |
| CH3 | k3 |
| CH4 | k4 |
| CH5 | k5 |
| CH6 | k6 |
| CH7 | k7 |
| CH8 | k8 |
| CH9 | k9 |
| CH10 | k10 |
| CH11 | k11 |
| CH12 | k12 |
| CH13 | k13 |
| CH14 | k14 |
| CH15 | k15 |
| CH16 | k16 |
| CH17 | k17 |
| CH18 | k18 |
| CH19 | k19 |
| CH20 | k20 |
| CH21 | k21 |
| CH22 | k22 |
| CH23 | k23 |
| CH24 | k24 |
| CH25 | k25 |
| CH26 | k26 |
| CH27 | k27 |
| CH28 | k28 |
| CH29 | k29 |
| CH30 | k30 |
| CH31 | k31 |
| CH32 | k32 |
| CH33 | k33 |
| CH34 | k34 |
| CH35 | k35 |
| CH36 | k36 |
| CH37 | k37 |
| CH38 | k38 |
| CH39 | k39 |
| CH40 | k40 |
| CH41 | k41 |
| CH42 | k42 |
| CH43 | k43 |
| CH44 | k44 |
| CH45 | k45 |
| CH46 | k46 |
| CH47 | k47 |
| CH48 | k48 |
| CH49 | k49 |
| CH50 | k50 |
| CH51 | k51 |
| CH52 | k52 |
| CH53 | k53 |
| CH54 | k54 |
| CH55 | k55 |
| CH56 | k56 |
| CH57 | k57 |
| CH58 | k58 |
| CH59 | k59 |
| CH60 | k60 |
| CH61 | k61 |
| CH62 | k62 |
| CH63 | k63 |
| COM 0 | kbc01 |
| kbc02 |  |
| kbc23 |  |
| kbc04 |  |
| kbc45 |  |
| kbc46 |  |
| kbc67 |  |
| kbc89 |  |
| kbc810 |  |
| kbc1011 |  |
| kbc812 |  |
| kbc1213 |  |
| kbc1214 |  |
| kbc1415 |  |

Parent topic:

NI PXIe-2525

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2525-2-wire-dual-32-1-multiplexer-top.html language=enus -->
## TOPIC 00514: NI PXIe-2525 2-Wire Dual 32×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2525-2-wire-dual-32-1-multiplexer-top.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2525-2-wire-dual-32-1-multiplexer-top.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2525 (NI 2525) in the 2-wire dual 32×1 multiplexer topology. Making a Connection When using the NI 2525 as a 2-wire dual 32×1 multiplexer, the positive leads of the first bank (ch0+ through ch31+) route to com0+, and the negative leads of the first bank (c

### NI PXIe-2525 2-Wire Dual 32×1 Multiplexer Topology

The following figure represents the NI PXIe-2525 (NI 2525) in the 2-wire dual 32×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-645A0EAE-2E66-4284-8D28-ABC23B36A261-a5.gif']

#### Making a Connection

When using the NI 2525 as a 2-wire dual 32×1 multiplexer, the positive leads of the
 first bank (ch0+ through ch31+) route to com0+, and the negative leads of the first
 bank (ch0– through ch31–) route to com0–. The pair com0+ and com0– is addressed
 collectively as com0 in software. The second bank follows a similar routing
 scheme.

The immediate operation command (the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function), with parameters ch2 and com0, result in
 the following connections:

signal connected to ch2+ is routed to com0+

signal connected to ch2– is routed to com0–

#### Pinout

The following figure identifies the pins for the NI 2525 in the 2-wire dual 32×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-21751E8E-2ACF-4C11-98B1-C2412952F3D7-a5.gif']

The following table lists the channel pairings and relay assignments for the NI 2525
 in the 2-wire dual 32×1 multiplexer topology.

| 2-Wire Dual 32×1 Channel Name | Relay Name |
| --- | --- |
| CH0 | k0 |
| CH1 | k1 |
| CH2 | k2 |
| CH3 | k3 |
| CH4 | k4 |
| CH5 | k5 |
| CH6 | k6 |
| CH7 | k7 |
| CH8 | k8 |
| CH9 | k9 |
| CH10 | k10 |
| CH11 | k11 |
| CH12 | k12 |
| CH13 | k13 |
| CH14 | k14 |
| CH15 | k15 |
| CH16 | k16 |
| CH17 | k17 |
| CH18 | k18 |
| CH19 | k19 |
| CH20 | k20 |
| CH21 | k21 |
| CH22 | k22 |
| CH23 | k23 |
| CH24 | k24 |
| CH25 | k25 |
| CH26 | k26 |
| CH27 | k27 |
| CH28 | k28 |
| CH29 | k29 |
| CH30 | k30 |
| CH31 | k31 |
| CH32 | k32 |
| CH33 | k33 |
| CH34 | k34 |
| CH35 | k35 |
| CH36 | k36 |
| CH37 | k37 |
| CH38 | k38 |
| CH39 | k39 |
| CH40 | k40 |
| CH41 | k41 |
| CH42 | k42 |
| CH43 | k43 |
| CH44 | k44 |
| CH45 | k45 |
| CH46 | k46 |
| CH47 | k47 |
| CH48 | k48 |
| CH49 | k49 |
| CH50 | k50 |
| CH51 | k51 |
| CH52 | k52 |
| CH53 | k53 |
| CH54 | k54 |
| CH55 | k55 |
| CH56 | k56 |
| CH57 | k57 |
| CH58 | k58 |
| CH59 | k59 |
| CH60 | k60 |
| CH61 | k61 |
| CH62 | k62 |
| CH63 | k63 |
| COM 0 | kbc01 |
| kbc02 |  |
| kbc23 |  |
| kbc04 |  |
| kbc45 |  |
| kbc46 |  |
| kbc67 |  |
| COM 8 | kbc89 |
| kbc810 |  |
| kbc1011 |  |
| kbc812 |  |
| kbc1213 |  |
| kbc1214 |  |
| kbc1415 |  |

Parent topic:

NI PXIe-2525

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2525-2-wire-octal-8-1-multiplexer-top.html language=enus -->
## TOPIC 00515: NI PXIe-2525 2-Wire Octal 8×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2525-2-wire-octal-8-1-multiplexer-top.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2525-2-wire-octal-8-1-multiplexer-top.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2525 (NI 2525) in the 2-wire octal 8×1 multiplexer topology. Making a Connection When using the NI 2525 as a 2-wire octal 8×1 multiplexer, the positive leads of the first bank (ch0+ through ch7+) route to com0+, and the negative leads of the first bank (ch

### NI PXIe-2525 2-Wire Octal 8×1 Multiplexer Topology

The following figure represents the NI PXIe-2525 (NI 2525) in the 2-wire octal 8×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-1538CFED-4EDA-40D7-9694-14D4DFA9ECF7-a5.gif']

#### Making a Connection

When using the NI 2525 as a 2-wire octal 8×1 multiplexer, the positive leads of the
 first bank (ch0+ through ch7+) route to com0+, and the negative leads of the first
 bank (ch0– through ch7–) route to com0–. The pair com0+ and com0– is addressed
 collectively as com0 in software. All other banks follow a similar routing
 scheme.

The immediate operation command (the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function), with parameters ch2 and com0, result in
 the following connections:

signal connected to ch2+ is routed to com0+

signal connected to ch2– is routed to com0–

#### Pinout

The following figure identifies the pins for the NI 2525 in the 2-wire octal 8×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-21751E8E-2ACF-4C11-98B1-C2412952F3D7-a5.gif']

The following table lists the channel pairings and relay assignments for the NI 2525
 in the 2-wire octal 8×1 multiplexer topology.

| 2-Wire Octal 8×1 Channel Name | Relay Name |
| --- | --- |
| CH0 | k0 |
| CH1 | k1 |
| CH2 | k2 |
| CH3 | k3 |
| CH4 | k4 |
| CH5 | k5 |
| CH6 | k6 |
| CH7 | k7 |
| CH8 | k8 |
| CH9 | k9 |
| CH10 | k10 |
| CH11 | k11 |
| CH12 | k12 |
| CH13 | k13 |
| CH14 | k14 |
| CH15 | k15 |
| CH16 | k16 |
| CH17 | k17 |
| CH18 | k18 |
| CH19 | k19 |
| CH20 | k20 |
| CH21 | k21 |
| CH22 | k22 |
| CH23 | k23 |
| CH24 | k24 |
| CH25 | k25 |
| CH26 | k26 |
| CH27 | k27 |
| CH28 | k28 |
| CH29 | k29 |
| CH30 | k30 |
| CH31 | k31 |
| CH32 | k32 |
| CH33 | k33 |
| CH34 | k34 |
| CH35 | k35 |
| CH36 | k36 |
| CH37 | k37 |
| CH38 | k38 |
| CH39 | k39 |
| CH40 | k40 |
| CH41 | k41 |
| CH42 | k42 |
| CH43 | k43 |
| CH44 | k44 |
| CH45 | k45 |
| CH46 | k46 |
| CH47 | k47 |
| CH48 | k48 |
| CH49 | k49 |
| CH50 | k50 |
| CH51 | k51 |
| CH52 | k52 |
| CH53 | k53 |
| CH54 | k54 |
| CH55 | k55 |
| CH56 | k56 |
| CH57 | k57 |
| CH58 | k58 |
| CH59 | k59 |
| CH60 | k60 |
| CH61 | k61 |
| CH62 | k62 |
| CH63 | k63 |
| COM 0 | kbc01 |
| COM 2 | kbc23 |
| COM 4 | kbc45 |
| COM 6 | kbc67 |
| COM 8 | kbc89 |
| COM 10 | kbc1011 |
| COM 12 | kbc1213 |
| COM 14 | kbc1415 |

Parent topic:

NI PXIe-2525

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2525-2-wire-quad-16-1-multiplexer-top.html language=enus -->
## TOPIC 00516: NI PXIe-2525 2-Wire Quad 16×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2525-2-wire-quad-16-1-multiplexer-top.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2525-2-wire-quad-16-1-multiplexer-top.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2525 (NI 2525) in the 2-wire quad 16×1 multiplexer topology. Making a Connection When using the NI 2525 as a 2-wire quad 16×1 multiplexer, the positive leads of the first bank (ch0+ through ch15+) route to com0+, and the negative leads of the first bank (c

### NI PXIe-2525 2-Wire Quad 16×1 Multiplexer Topology

The following figure represents the NI PXIe-2525 (NI 2525) in the 2-wire quad 16×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-959028F0-7CE6-4E13-A8EA-57AB6159058E-a5.gif']

#### Making a Connection

When using the NI 2525 as a 2-wire quad 16×1 multiplexer, the positive leads of the
 first bank (ch0+ through ch15+) route to com0+, and the negative leads of the first
 bank (ch0– through ch15–) route to com0–. The pair com0+ and com0– is addressed
 collectively as com0 in software. All other banks follow a similar routing
 scheme.

The immediate operation (the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function), with parameters ch2 and com0, result in
 the following connections:

signal connected to ch2+ is routed to com0+

signal connected to ch2– is routed to com0–

#### Pinout

The following figure identifies the pins for the NI 2525 in the 2-wire quad 16×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-21751E8E-2ACF-4C11-98B1-C2412952F3D7-a5.gif']

The following table lists the channel pairings and relay assignments for the NI 2525
 in the 2-wire quad 16×1 multiplexer topology.

| 2-Wire Quad 16×1 Channel Name | Relay Name |
| --- | --- |
| CH0 | k0 |
| CH1 | k1 |
| CH2 | k2 |
| CH3 | k3 |
| CH4 | k4 |
| CH5 | k5 |
| CH6 | k6 |
| CH7 | k7 |
| CH8 | k8 |
| CH9 | k9 |
| CH10 | k10 |
| CH11 | k11 |
| CH12 | k12 |
| CH13 | k13 |
| CH14 | k14 |
| CH15 | k15 |
| CH16 | k16 |
| CH17 | k17 |
| CH18 | k18 |
| CH19 | k19 |
| CH20 | k20 |
| CH21 | k21 |
| CH22 | k22 |
| CH23 | k23 |
| CH24 | k24 |
| CH25 | k25 |
| CH26 | k26 |
| CH27 | k27 |
| CH28 | k28 |
| CH29 | k29 |
| CH30 | k30 |
| CH31 | k31 |
| CH32 | k32 |
| CH33 | k33 |
| CH34 | k34 |
| CH35 | k35 |
| CH36 | k36 |
| CH37 | k37 |
| CH38 | k38 |
| CH39 | k39 |
| CH40 | k40 |
| CH41 | k41 |
| CH42 | k42 |
| CH43 | k43 |
| CH44 | k44 |
| CH45 | k45 |
| CH46 | k46 |
| CH47 | k47 |
| CH48 | k48 |
| CH49 | k49 |
| CH50 | k50 |
| CH51 | k51 |
| CH52 | k52 |
| CH53 | k53 |
| CH54 | k54 |
| CH55 | k55 |
| CH56 | k56 |
| CH57 | k57 |
| CH58 | k58 |
| CH59 | k59 |
| CH60 | k60 |
| CH61 | k61 |
| CH62 | k62 |
| CH63 | k63 |
| COM 0 | kbc01 |
| kbc02 |  |
| kbc23 |  |
| COM 4 | kbc45 |
| kbc46 |  |
| kbc67 |  |
| COM 8 | kbc89 |
| kbc810 |  |
| kbc1011 |  |
| COM 10 | kbc1213 |
| kbc1214 |  |
| kbc1415 |  |

Parent topic:

NI PXIe-2525

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2525-2-wire-sixteen-4-1-multiplexer-t.html language=enus -->
## TOPIC 00517: NI PXIe-2525 2-Wire Sixteen 4×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2525-2-wire-sixteen-4-1-multiplexer-t.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2525-2-wire-sixteen-4-1-multiplexer-t.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2525 (NI 2525) in the 2-wire sixteen 4×1 multiplexer topology. Making a Connection When using the NI 2525 as a 2-wire sixteen 4×1 multiplexer, the positive leads of the first bank (ch0+ through ch3+) route to com0+, and the negative leads of the first bank

### NI PXIe-2525 2-Wire Sixteen 4×1 Multiplexer Topology

The following figure represents the NI PXIe-2525 (NI 2525) in the 2-wire sixteen 4×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-820AEADC-EA99-4447-BCB3-AAEB68D41B93-a5.gif']

#### Making a Connection

When using the NI 2525 as a 2-wire sixteen 4×1 multiplexer, the positive leads of the
 first bank (ch0+ through ch3+) route to com0+, and the negative leads of the first
 bank (ch0– through ch3–) route to com0–. The pair com0+ and com0– is addressed
 collectively as com0 in software. All other banks follow a similar routing
 scheme.

The immediate operation command (the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function), with parameters ch2 and com0, result in
 the following connections:

signal connected to ch2+ is routed to com0+

signal connected to ch2– is routed to com0–

#### Pinout

The following figure identifies the pins for the NI 2525 in the 2-wire sixteen 4×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-21751E8E-2ACF-4C11-98B1-C2412952F3D7-a5.gif']

The following table lists the channel pairings and relay assignments for the NI 2525
 in the 2-wire sixteen 4×1 multiplexer topology.

| 2-Wire Sixteen 4×1 Channel Name | Relay Name |
| --- | --- |
| CH0 | k0 |
| CH1 | k1 |
| CH2 | k2 |
| CH3 | k3 |
| CH4 | k4 |
| CH5 | k5 |
| CH6 | k6 |
| CH7 | k7 |
| CH8 | k8 |
| CH9 | k9 |
| CH10 | k10 |
| CH11 | k11 |
| CH12 | k12 |
| CH13 | k13 |
| CH14 | k14 |
| CH15 | k15 |
| CH16 | k16 |
| CH17 | k17 |
| CH18 | k18 |
| CH19 | k19 |
| CH20 | k20 |
| CH21 | k21 |
| CH22 | k22 |
| CH23 | k23 |
| CH24 | k24 |
| CH25 | k25 |
| CH26 | k26 |
| CH27 | k27 |
| CH28 | k28 |
| CH29 | k29 |
| CH30 | k30 |
| CH31 | k31 |
| CH32 | k32 |
| CH33 | k33 |
| CH34 | k34 |
| CH35 | k35 |
| CH36 | k36 |
| CH37 | k37 |
| CH38 | k38 |
| CH39 | k39 |
| CH40 | k40 |
| CH41 | k41 |
| CH42 | k42 |
| CH43 | k43 |
| CH44 | k44 |
| CH45 | k45 |
| CH46 | k46 |
| CH47 | k47 |
| CH48 | k48 |
| CH49 | k49 |
| CH50 | k50 |
| CH51 | k51 |
| CH52 | k52 |
| CH53 | k53 |
| CH54 | k54 |
| CH55 | k55 |
| CH56 | k56 |
| CH57 | k57 |
| CH58 | k58 |
| CH59 | k59 |
| CH60 | k60 |
| CH61 | k61 |
| CH62 | k62 |
| CH63 | k63 |
| COM 0 | — |
| COM 1 | — |
| COM 2 | — |
| COM 3 | — |
| COM 4 | — |
| COM 5 | — |
| COM 6 | — |
| COM 7 | — |
| COM 8 | — |
| COM 9 | — |
| COM 10 | — |
| COM 11 | — |
| COM 12 | — |
| COM 13 | — |
| COM 14 | — |
| COM 15 | — |

Parent topic:

NI PXIe-2525

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2525-front-panel.html language=enus -->
## TOPIC 00518: NI PXIe-2525 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2525-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2525-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXIe-2525 front panel.

### NI PXIe-2525 Front Panel

The following figure illustrates the NI PXIe-2525 front panel.

[IMAGE alt='image' src='GUID-47A46463-B1FB-4413-ACA4-3730DE869369-a5.gif']

Parent topic:

NI PXIe-2525

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2525-hardware-diagram.html language=enus -->
## TOPIC 00519: NI PXIe-2525 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2525-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2525-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXIe-2525.

### NI PXIe-2525 Hardware Diagram

The following figure shows the hardware diagram for the NI PXIe-2525.

[IMAGE alt='image' src='GUID-FF574A65-F6BF-4EB9-A425-371C711520C8-a5.gif']

Parent topic:

NI PXIe-2525

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2525-relay-replacement.html language=enus -->
## TOPIC 00520: NI PXIe-2525 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2525-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2525-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2525 uses electromechanical armature relays. Refer to the following tables for information about ordering replacement relays. Use relays of the same brand that you are replacing. Relay Manufacturer Part Number Tyco 1462043-6 Relay Kit Part Number National Instruments (10 relays, Tyco) 78

### NI PXIe-2525 Relay Replacement

The NI PXIe-2525 uses electromechanical armature relays.

Refer to the following tables for information about ordering replacement relays. Use relays
 of the same brand that you are replacing.

| Relay Manufacturer | Part Number |
| --- | --- |
| Tyco | 1462043-6 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays, Tyco) | 782461-10 |

Complete the following steps to locate, remove, and replace a failed relay.

#### Locate the Relay

1. Ground yourself using a grounding strap or a ground connected to your PXI Express
 chassis. Note Properly grounding yourself prevents damage to your module
 from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figures and table for relay
 locations. NI PXIe-2525 PCB 1 
 [IMAGE alt='image' src='GUID-F0514D31-4A9C-4B36-BBC5-D761B804101E-a5.gif'] 
 Table 2.NI PXIe-2525 PCB 1 Relay LocationsRelay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designatork0
 K4
 k16
 25
 k32
 K48
 k48
 K67
 kbc01
 K6k1
 K3
 k17
 K24
 k33
 K47
 k49
 K66
 kbc23
 K21k2
 K2
 k18
 K23
 k34
 K46
 k50
 K65
 kbc45
 K35k3
 K1
 k19
 K22
 k35
 K45
 k51
 K64
 kbc67
 K33k4
 K16
 k20
 K36
 k36
 K44
 k52
 K63
 kbc89
 K49k5
 K15
 k21
 K28
 k37
 K43
 k53
 K62
 kbc1011
 K51k6
 K14
 k22
 K27
 k38
 K42
 k54
 K61
 kbc1213
 K71k7
 K13
 k23
 K26
 k39
 K41
 k55
 K60
 kbc1415
 K68k8
 K12
 k24
 K32
 k40
 K55
 k56
 K75
 kbc02
 K7k9
 K11
 k25
 K31
 k41
 K54
 k57
 K74
 kbc46
 K34k10
 K10
 k26
 K30
 k42
 K53
 k58
 K73
 kbc810
 K50k11
 K9
 k27
 K29
 k43
 K52
 k59
 K72
 kbc1214
 K69k12
 K20
 k28
 K40
 k44
 K59
 k60
 K79
 kbc04
 K5k13
 K19
 k29
 K39
 k45
 K58
 k61
 K78
 kbc812
 K70k14
 K18
 k30
 K38
 k46
 K57
 k62
 K77
 kbc08
 K8k15
 K17
 k31
 K37
 k47
 K56
 k63
 K76
3. Locate the assembly and serial number labels on the board with the relay you want to
 replace. White labels indicate the board was assembled using lead solder (Sn 63 Pb 37).
 Green labels indicate the board was assembled using lead-free solder (Sn 96.5 Ag 3.0 Cu
 0.5). Lead-free assemblies have assembly numbers ending in L. [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']

#### Replace the Relay

Note

Caution

Caution

Make sure you have the following:

- Temperature-regulated soldering iron set to 316 °C (600 °F) for lead solder rework or
 371 °C (700 °F) for lead-free solder rework
- 63/37 Tin/Lead solder (flux core) for lead solder rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Complete the following steps to replace a relay:

1. Locate the assembly and serial number labels on the board with the relay you want to
 replace. White labels indicate the board was assembled using lead solder (Sn 63 Pb 37).
 Green labels indicate the board was assembled using lead-free solder (Sn 96.5 Ag 3.0 Cu
 0.5). Lead-free assemblies have assembly numbers ending in L. The different label types
 are shown in the following figure. [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']
2. Replace the relay as you would any other through-hole part. Trim the replaced relay to
 no more than 0.41 mm (0.016 inch) from the PCB.

Tip

Switch
 Soft Front Panel Help

Parent topic:

NI PXIe-2525

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2525.html language=enus -->
## TOPIC 00521: NI PXIe-2525

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2525.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2525.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2525 (NI 2525) is a high-voltage multiplexer relay module for the PXI Express platform. The NI 2525 is composed of 79 armature relays. For certain applications, you may need to increase the default settling time. Refer to Adding Additional Settling Time for more information. Switching

### NI PXIe-2525

The NI PXIe-2525 (NI 2525) is a high-voltage multiplexer relay module for the PXI Express
 platform. The NI 2525 is composed of 79 armature relays.

Note

#### Operation Modes

The following table lists the supported topologies of the NI 2525 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 2-Wire 64×1 Multiplexer | 2525/2-Wire 64x1 Mux(NISWITCH_TOPOLOGY_2525_2_WIRE_64X1_MUX) |  |  |
| 2-Wire Dual 32×1 Multiplexer | 2525/2-Wire Dual 32x1 Mux(NISWITCH_TOPOLOGY_2525_2_WIRE_DUAL_32X1_MUX) |  |  |
| 2-Wire Quad 16×1 Multiplexer | 2525/2-Wire Quad 16x1 Mux(NISWITCH_TOPOLOGY_2525_2_WIRE_QUAD_16X1_MUX) |  |  |
| 2-Wire Octal 8×1 Multiplexer | 2525/2-Wire Octal 8x1 Mux(NISWITCH_TOPOLOGY_2525_2_WIRE_OCTAL_8X1_MUX) |  |  |
| 2-Wire Sixteen 4×1 Multiplexer | 2525/2-Wire Sixteen 4x1 Mux(NISWITCH_TOPOLOGY_2525_2_WIRE_SIXTEEN_4X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Armature Relays
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXIe-2525 2-Wire 64×1 Multiplexer Topology
- NI PXIe-2525 2-Wire Dual 32×1 Multiplexer Topology
- NI PXIe-2525 2-Wire Quad 16×1 Multiplexer Topology
- NI PXIe-2525 2-Wire Octal 8×1 Multiplexer Topology
- NI PXIe-2525 2-Wire Sixteen 4×1 Multiplexer Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2526-1-wire-158-1-multiplexer-topolog.html language=enus -->
## TOPIC 00522: NI PXIe-2526 1-Wire 158×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2526-1-wire-158-1-multiplexer-topolog.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2526-1-wire-158-1-multiplexer-topolog.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2526 (NI 2526) in the 1-wire 158×1 multiplexer topology. Making a Connection When using the NI 2526 as a 1-wire 158×1 multiplexer, all channels route to com0. You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect funct

### NI PXIe-2526 1-Wire 158×1 Multiplexer Topology

The following figure represents the NI PXIe-2526 (NI 2526) in the 1-wire 158×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-BB81CF66-BC76-418D-B41C-D9166F02685A-a5.gif']

#### Making a Connection

When using the NI 2526 as a 1-wire 158×1 multiplexer, all channels route to com0. You can
 control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to connect channel 1 to com0, call niSwitch_Connect(vi, "ch1",
 "com"). To disconnect channel 1 from com0, call niSwitch_Disconnect(vi,
 "ch1", "com").

#### Pinout

The following figure identifies the pins for the NI 2526 in the 1-wire 158×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-CC12ED6B-132B-439A-92FD-BC3BC167592C-a5.gif']

The following table lists the channel pairings and relay assignments for the NI 2526 in
 the 1-wire 158×1 multiplexer topology.

| 1-Wire 158×1 Channel Name |  | Relay Name |
| --- | --- | --- |
| CH0 | CH79 | k0 |
| CH1 | CH80 | k1 |
| CH2 | CH81 | k2 |
| CH3 | CH82 | k3 |
| CH4 | CH83 | k4 |
| CH4 | CH83 | k4 |
| CH5 | CH84 | k5 |
| CH6 | CH85 | k6 |
| CH7 | CH86 | k7 |
| CH8 | CH87 | k8 |
| CH9 | CH88 | k9 |
| CH10 | CH89 | k10 |
| CH11 | CH90 | k11 |
| CH12 | CH91 | k12 |
| CH13 | CH92 | k13 |
| CH14 | CH93 | k14 |
| CH14 | CH93 | k14 |
| CH15 | CH94 | k15 |
| CH16 | CH95 | k16 |
| CH17 | CH96 | k17 |
| CH18 | CH97 | k18 |
| CH19 | CH98 | k19 |
| CH20 | CH99 | k20 |
| CH20 | CH99 | k20 |
| CH21 | CH100 | k21 |
| CH22 | CH101 | k22 |
| CH23 | CH102 | k23 |
| CH24 | CH103 | k24 |
| CH25 | CH104 | k25 |
| CH26 | CH105 | k26 |
| CH27 | CH106 | k27 |
| CH28 | CH107 | k28 |
| CH29 | CH108 | k29 |
| CH30 | CH109 | k30 |
| CH31 | CH110 | k31 |
| CH32 | CH111 | k32 |
| CH33 | CH112 | k33 |
| CH34 | CH113 | k34 |
| CH35 | CH114 | k35 |
| CH36 | CH115 | k36 |
| CH37 | CH116 | k37 |
| CH38 | CH117 | k38 |
| CH39 | CH118 | k39 |
| CH40 | CH119 | k40 |
| CH41 | CH120 | k41 |
| CH42 | CH121 | k42 |
| CH43 | CH122 | k43 |
| CH44 | CH123 | k44 |
| CH45 | CH124 | k45 |
| CH46 | CH125 | k46 |
| CH47 | CH126 | k47 |
| CH48 | CH127 | k48 |
| CH49 | CH128 | k49 |
| CH50 | CH129 | k50 |
| CH51 | CH130 | k51 |
| CH52 | CH131 | k52 |
| CH53 | CH132 | k53 |
| CH54 | CH133 | k54 |
| CH55 | CH134 | k55 |
| CH56 | CH135 | k56 |
| CH57 | CH136 | k57 |
| CH58 | CH137 | k58 |
| CH59 | CH138 | k59 |
| CH60 | CH139 | k60 |
| CH61 | CH140 | k61 |
| CH62 | CH141 | k62 |
| CH63 | CH142 | k63 |
| CH64 | CH143 | k64 |
| CH65 | CH144 | k65 |
| CH66 | CH145 | k66 |
| CH67 | CH146 | k67 |
| CH68 | CH147 | k68 |
| CH69 | CH148 | k69 |
| CH70 | CH149 | k70 |
| CH71 | CH150 | k71 |
| CH72 | CH151 | k72 |
| CH73 | CH152 | k73 |
| CH74 | CH153 | k74 |
| CH75 | CH154 | k75 |
| CH76 | CH155 | k76 |
| CH77 | CH156 | k77 |
| CH78 | CH157 | k78 |
| COM |  | kcomhi |
| kcomlo |  |  |
| kcomlo1w |  |  |

Parent topic:

NI PXIe-2526

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2526-2-wire-79-1-multiplexer-topology.html language=enus -->
## TOPIC 00523: NI PXIe-2526 2-Wire 79×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2526-2-wire-79-1-multiplexer-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2526-2-wire-79-1-multiplexer-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2526 (NI 2526) in the 2-wire 79×1 multiplexer topology. Making a Connection When using the NI 2526 as a 2-wire 79×1 multiplexer, all positive leads (ch0+ through ch78+) route to com+, and all negative leads (ch0– through ch78–) route to com–. The pair com+

### NI PXIe-2526 2-Wire 79×1 Multiplexer Topology

The following figure represents the NI PXIe-2526 (NI 2526) in the 2-wire 79×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-62B2D1D1-547C-4E9A-A68A-BE6694CA494E-a5.gif']

#### Making a Connection

When using the NI 2526 as a 2-wire 79×1 multiplexer, all positive leads (ch0+ through
 ch78+) route to com+, and all negative leads (ch0– through ch78–) route to com–. The
 pair com+ and com– is addressed collectively as com in software.

The immediate operation (the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function), with parameters ch2 and com, result in
 the following connections:

signal connected to ch2+ is routed to com+

signal connected to ch2– is routed to com–

#### Pinout

The following figure identifies the pins for the NI 2526 in the 2-wire 79×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-287BEC9F-81F3-4612-A9A1-AFD55C4F846A-a5.gif']

The following table lists the channel pairings and relay assignments for the NI 2526
 in the 2-wire 79×1 multiplexer topology.

| 2-Wire 79×1 Channel Name | Relay Name |
| --- | --- |
| CH0 | k0 |
| CH1 | k1 |
| CH2 | k2 |
| CH3 | k3 |
| CH4 | k4 |
| CH4 | k4 |
| CH5 | k5 |
| CH6 | k6 |
| CH7 | k7 |
| CH8 | k8 |
| CH9 | k9 |
| CH10 | k10 |
| CH11 | k11 |
| CH12 | k12 |
| CH13 | k13 |
| CH14 | k14 |
| CH14 | k14 |
| CH15 | k15 |
| CH16 | k16 |
| CH17 | k17 |
| CH18 | k18 |
| CH19 | k19 |
| CH20 | k20 |
| CH20 | k20 |
| CH21 | k21 |
| CH22 | k22 |
| CH23 | k23 |
| CH24 | k24 |
| CH25 | k25 |
| CH26 | k26 |
| CH27 | k27 |
| CH28 | k28 |
| CH29 | k29 |
| CH30 | k30 |
| CH31 | k31 |
| CH32 | k32 |
| CH33 | k33 |
| CH34 | k34 |
| CH35 | k35 |
| CH36 | k36 |
| CH37 | k37 |
| CH38 | k38 |
| CH39 | k39 |
| CH40 | k40 |
| CH41 | k41 |
| CH42 | k42 |
| CH43 | k43 |
| CH44 | k44 |
| CH45 | k45 |
| CH46 | k46 |
| CH47 | k47 |
| CH48 | k48 |
| CH49 | k49 |
| CH50 | k50 |
| CH51 | k51 |
| CH52 | k52 |
| CH53 | k53 |
| CH54 | k54 |
| CH55 | k55 |
| CH56 | k56 |
| CH57 | k57 |
| CH58 | k58 |
| CH59 | k59 |
| CH60 | k60 |
| CH61 | k61 |
| CH62 | k62 |
| CH63 | k63 |
| CH64 | k64 |
| CH65 | k65 |
| CH66 | k66 |
| CH67 | k67 |
| CH68 | k68 |
| CH69 | k69 |
| CH70 | k70 |
| CH71 | k71 |
| CH72 | k72 |
| CH73 | k73 |
| CH74 | k74 |
| CH75 | k75 |
| CH76 | k76 |
| CH77 | k77 |
| CH78 | k78 |
| COM | kcomhi |
| kcomlo |  |

Parent topic:

NI PXIe-2526

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2526-front-panel.html language=enus -->
## TOPIC 00524: NI PXIe-2526 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2526-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2526-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXIe-2526 front panel.

### NI PXIe-2526 Front Panel

The following figure illustrates the NI PXIe-2526 front panel.

[IMAGE alt='image' src='GUID-5EF03CC9-153B-4965-9288-2C3551896566-a5.gif']

Parent topic:

NI PXIe-2526

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2526-hardware-diagram.html language=enus -->
## TOPIC 00525: NI PXIe-2526 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2526-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2526-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXIe-2526.

### NI PXIe-2526 Hardware Diagram

The following figure shows the hardware diagram for the NI PXIe-2526.

[IMAGE alt='image' src='GUID-726D0B92-02F1-4C50-8B1D-3ED2A07E5DC8-a5.gif']

Parent topic:

NI PXIe-2526

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2526-relay-replacement.html language=enus -->
## TOPIC 00526: NI PXIe-2526 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2526-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2526-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2526 uses electromechanical armature relays. Refer to the following tables for information about ordering replacement relays. Use relays of the same brand that you are replacing. Relay Manufacturer Part Number Tyco 1462043-6 Relay Kit Part Number National Instruments (10 relays, Tyco) 78

### NI PXIe-2526 Relay Replacement

The NI PXIe-2526 uses electromechanical armature relays.

Refer to the following tables for information about ordering replacement relays. Use relays
 of the same brand that you are replacing.

| Relay Manufacturer | Part Number |
| --- | --- |
| Tyco | 1462043-6 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays, Tyco) | 782461-10 |

Complete the following steps to locate, remove, and replace a failed relay.

#### Locate the Relay

1. Ground yourself using a grounding strap or a ground connected to your PXI Express
 chassis. Note Properly grounding yourself prevents damage to your module
 from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figures and table for relay
 locations. NI PXIe-2526 PCB 1 
 [IMAGE alt='image' src='GUID-174CFB7B-B90C-4E61-B85A-AC7B02BAF3E8-a5.gif'] 
 Table 3.NI PXIe-2526 PCB 1 Relay LocationsRelay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designatork0
 K1
 k16
 K17
 k32
 K33
 k48
 K49
 k64
 K65
 kcomhi
 K78k1
 K2
 k17
 K18
 k33
 K34
 k49
 K50
 k65
 K66
 kcomlo1w
 K79k2
 K3
 k18
 K19
 k34
 K35
 k50
 K51
 k66
 K67
 kcomlo
 K80k3
 K4
 k19
 K20
 k35
 K36
 k51
 K52
 k67
 K68k4
 K5
 k20
 K21
 k36
 K37
 k52
 K53
 k68
 K69k5
 K6
 k21
 K22
 k37
 K38
 k53
 K54
 k69
 K70k6
 K7
 k22
 K23
 k38
 K39
 k54
 K55
 k70
 K71k7
 K8
 k23
 K24
 k39
 K40
 k55
 K56
 k71
 K72k8
 K9
 k24
 K25
 k40
 K41
 k56
 K57
 k72
 K73k9
 K10
 k25
 K26
 k41
 K42
 k57
 K58
 k73
 K74k10
 K11
 k26
 K27
 k42
 K43
 k58
 K59
 k74
 K75k11
 K12
 k27
 K28
 k43
 K44
 k59
 K60
 k75
 K76k12
 K13
 k28
 K29
 k44
 K45
 k60
 K61
 k76
 K77k13
 K14
 k29
 K30
 k45
 K46
 k61
 K62
 k77
 K81k14
 K15
 k30
 K31
 k46
 K47
 k62
 K63
 k78
 K82k15
 K16
 k31
 K32
 k47
 K48
 k63
 K64
3. Locate the assembly and serial number labels on the board with the relay you want to
 replace. White labels indicate the board was assembled using lead solder (Sn 63 Pb 37).
 Green labels indicate the board was assembled using lead-free solder (Sn 96.5 Ag 3.0 Cu
 0.5). Lead-free assemblies have assembly numbers ending in L. [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']

#### Replace the Relay

Note

Caution

Caution

Make sure you have the following:

- Temperature-regulated soldering iron set to 316 °C (600 °F) for lead solder rework or
 371 °C (700 °F) for lead-free solder rework
- 63/37 Tin/Lead solder (flux core) for lead solder rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Complete the following steps to replace a relay:

1. Locate the assembly and serial number labels on the board with the relay you want to
 replace. White labels indicate the board was assembled using lead solder (Sn 63 Pb 37).
 Green labels indicate the board was assembled using lead-free solder (Sn 96.5 Ag 3.0 Cu
 0.5). Lead-free assemblies have assembly numbers ending in L. The different label types
 are shown in the following figure. [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']
2. Replace the relay as you would any other through-hole part. Trim the replaced relay to
 no more than 0.41 mm (0.016 inch) from the PCB.

Tip

Switch
 Soft Front Panel Help

Parent topic:

NI PXIe-2526

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2526.html language=enus -->
## TOPIC 00527: NI PXIe-2526

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2526.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2526.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2526 (NI 2526) is a 158×1 multiplexer relay module for the PXI Express platform. The NI 2526 is composed of 82 armature relays. For certain applications, you may need to increase the default settling time. Refer to Adding Additional Settling Time for more information. Switching inducti

### NI PXIe-2526

The NI PXIe-2526 (NI 2526) is a 158×1 multiplexer relay module for the PXI Express
 platform. The NI 2526 is composed of 82 armature relays.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2526 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 158×1 Multiplexer | 2526/1-Wire 158x1 Mux(NISWITCH_TOPOLOGY_2526_1_WIRE_158X1_MUX) |  |  |
| 2-Wire 79×1 Multiplexer | 2526/2-Wire 79x1 Mux(NISWITCH_TOPOLOGY_2526_2_WIRE_79X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Armature Relays
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXIe-2526 1-Wire 158×1 Multiplexer Topology
- NI PXIe-2526 2-Wire 79×1 Multiplexer Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2725-hardware-diagram.html language=enus -->
## TOPIC 00528: NI PXIe-2725 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2725-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2725-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXIe-2725. Resistance values are nominal. Please see the NI PXIe-2725 Specifications for resistor values and accuracy information The following table lists relay names for the NI PXIe-2725. Relays kb0r0, kb0r1...kb0r7 kb1r0, kb1r1...kb1r7

### NI PXIe-2725 Hardware Diagram

The following figure shows the hardware diagram for the NI PXIe-2725.

[IMAGE alt='image' src='GUID-63C2329A-157B-444D-BBE0-B8EF6FD078A9-a5.gif']

Note

NI PXIe-2725
 Specifications

The following table lists relay names for the NI PXIe-2725.

| Relays |
| --- |
| kb0r0, kb0r1...kb0r7 |
| kb1r0, kb1r1...kb1r7 |
| kb2r0, kb2r1...kb2r7 |
| kb3r0, kb3r1...kb3r7 |
| kb4r0, kb4r1...kb4r7 |
| kb5r0, kb5r1...kb5r7 |
| kb6r0, kb6r1...kb6r7 |
| kb7r0, kb7r1...kb7r7 |
| kb8r0, kb8r1...kb8r7 |
| kb9r0, kb9r1...kb9r7 |
| kb10r0, kb10r1...kb10r7 |
| kb11r0, kb11r1...kb11r7 |
| kb12r0, kb12r1...kb12r7 |
| kb13r0, kb13r1...kb13r7 |
| kb14r0, kb14r1...kb14r7 |
| kb15r0, kb15r1...kb15r7 |
| kb16r0, kb16r1...kb16r7 |
| kb17r0, kb17r1...kb17r7 |
| kb0...kb17 |
| kb0shunt...kb17shunt |
| kbc01, kbc12...kbc1617 |
| ktest0, ktest1...ktest9 |

Parent topic:

NI PXIe-2725

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2725-independent-topology.html language=enus -->
## TOPIC 00529: NI PXIe-2725 Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2725-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2725-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2725 in the independent topology. Making a Connection Bank connect relays allow adjacent banks or channels to connect together internally. For example, you can connect two or more adjacent channels together to create a potentiometer, a voltage divider, o

### NI PXIe-2725 Independent Topology

The following figure represents the NI PXIe-2725 in the independent topology.

[IMAGE alt='image' src='GUID-63C2329A-157B-444D-BBE0-B8EF6FD078A9-a5.gif']

#### Making a Connection

Note

#### Making a Connection

Each 8-bit channel is composed of one bank on the NI PXIe-2725. For example, ch0 is
 composed of bank 0 and ch1 is composed of bank 1. NI has created a set of reference
 VIs that will programmatically open and close relays based on a user-specified
 resistance value or RTD temperature to simulate. To access these reference VIs,
 visit ni.com/info and enter the Info Code
 272xOverview. NI recommends using this set of reference VIs for
 the easiest programming experience. If not using these reference VIs, NI recommends
 using the low-level relay control VIs or functions instead of the connect channel
 VIs or functions. The DAQmx Relay API supports closing multiple relays in a single
 driver call, which is faster than the channel API.

When a bank relay is closed, the corresponding resistor is placed in parallel with
 the low resistance of the relay, which nominally equates to a zero Ω shunt. Closing
 any of the 8 bank relays in a given bank decreases the resistance of that bank.

For example, the following procedure uses the NI-SWITCH Relay API to short across the
 largest resistor in bank 0 and join bank 0 and bank 1 in series.

1. Close b0r7 by calling the niSwitch Relay Control
 VI
 with the inputs of b0r7 and close .
2. Close bc01 by calling the niSwitch Relay Control
 VI
 with the inputs of bc01 and close .

You can perform the same operation using the NI-SWITCH Channel API, as shown
 below.

1. Connect b0 -> b0r7 by calling niSwitch
 Connect Channels
 VI
 with the inputs of b0 and b0r7 .
2. Connect b0 -> b1 by calling niSwitch Connect
 Channels
 VI
 with the inputs of b0 and b1 .

Each bank is initially in a high impedance (open) state across the bank terminals. To
 enable the desired output channel you must first connect the bank relay,
 bN.

Each bank includes a shunt relay that completely bypasses the bank's string of 8
 series relays. Closing the shunt relay
 bN->bNshunt, for example,
 b0->b0shunt or low-level
 kb0shunt, results in a low resistance across the bank, 0 Ω
 nominally. This allows the NI PXIe-2725 module to pass signals with minimal
 attenuation.

Note

The 4-pin front panel test connector can connect to any adjacent pair of even-odd
 banks, allowing resistance measurements, or voltage measurements, across those two
 banks, for example b0 to b1, b2
 to b3, b4 to b5. On 16-bit NI
 272x modules, this allows channel resistance measurements using a DMM with Offset
 Compensated Ohms (such as the NI PXI-4070, NI PXI-4071, or NI PXI-4072). To connect
 a pair of banks to the test leads, close the appropriate test relays using the
 command testN->testout. For example, to measure
 the resistance across banks 0 and 1, call
 test0->testout and
 test1->testout. For banks 2 and 3, call
 test1->testout and
 test2->testout. Refer to the device's
 hardware diagram for valid test relay connections.

Note

Note

#### Pinout

The following figure identifies the pins for the NI PXIe-2725.

[IMAGE alt='image' src='GUID-A193BC1B-9B05-4166-A4F1-794DF261A112-a5.gif']

Note

Parent topic:

NI PXIe-2725

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2725-relay-replacement.html language=enus -->
## TOPIC 00530: NI PXIe-2725 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2725-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2725-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2725 uses reed relays. The NI PXIe-2725 uses a custom lead length to meet safety standards. Trim leads per rework instructions or use one of the custom relays from the relay kit. Refer to the following tables for information about ordering replacement relays. Relay Relay Manufacturer P

### NI PXIe-2725 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay | Relay Manufacturer | Part Number |
| --- | --- | --- |
| All Relays | Coto | 9117-0001 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 781451-10 |

Complete the following sets of steps to disassemble the module, replace a failed relay,
 and reassemble your module.

#### Disassemble the Module

1. Ground yourself using a grounding strap or a ground connected to the PXI Express
 chassis. Note Properly grounding yourself prevents damage to
 your module from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figures and table
 for relay locations. NI PXIe 2725 Relay Map 
 [IMAGE alt='image' src='GUID-A2D53F53-70EB-4489-8549-1E38497D89D0-a5.gif'] 
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorkb0shunt
 K1
 kb4r2
 K53
 kb9shunt
 K105
 kb13r2
 K157kb0
 K2
 kb4r3
 K54
 kb9
 K106
 kb13r3
 K158kbc01
 K3
 kb4r4
 K55
 kbc910
 K107
 kb13r4
 K159test0
 K4
 kb4r5
 K56
 test5
 K108
 kb13r5
 K160kb0r0
 K5
 kb4r6
 K57
 kb9r0
 K109
 kb13r6
 K161kb0r1
 K6
 kb4r7
 K58
 kb9r1
 K110
 kb13r7
 K162kb0r2
 K7
 kb5shunt
 K59
 kb9r2
 K111
 kb14shunt
 K163kb0r3
 K8
 kb5
 K60
 kb9r3
 K112
 kb14
 K164kb0r4
 K9
 kbc56
 K61
 kb9r4
 K113
 kbc1415
 K165kb0r5
 K10
 test3
 K62
 kb9r5
 K114
 kb14r0
 K166kb0r6
 K11
 kb5r0
 K63
 kb9r6
 K115
 kb14r1
 K167kb0r7
 K12
 kb5r1
 K64
 kb9r7
 K116
 kb14r2
 K168kb1shunt
 K13
 kb5r2
 K65
 kb10shunt
 K117
 kb14r3
 K169kb1
 K14
 kb5r3
 K66
 kb10
 K118
 kb14r4
 K170kbc12
 K15
 kb5r4
 K67
 kbc1011
 K119
 kb14r5
 K171test1
 K16
 kb5r5
 K68
 kb10r0
 K120
 kb14r6
 K172kb1r0
 K17
 kb5r6
 K69
 kb10r1
 K121
 kb14r7
 K173kb1r1
 K18
 kb5r7
 K70
 kb10r2
 K122
 kb15shunt
 K174kb1r2
 K19
 kb6shunt
 K71
 kb10r3
 K123
 kb15
 K175kb1r3
 K20
 kb6
 K72
 kb10r4
 K124
 kbc1516
 K176kb1r4
 K21
 kbc67
 K73
 kb10r5
 K125
 test8
 K177kb1r5
 K22
 kb6r0
 K74
 kb10r6
 K126
 kb15r0
 K178kb1r6
 K23
 kb6r1
 K75
 kb10r7
 K127
 kb15r1
 K179kb1r7
 K24
 kb6r2
 K76
 kb11shunt
 K128
 kb15r2
 K180kb2shunt
 K25
 kb6r3
 K77
 kb11
 K129
 kb15r3
 K181kb2
 K26
 kb6r4
 K78
 kbc1112
 K130
 kb15r4
 K182kbc23
 K27
 kb6r5
 K79
 test6
 K131
 kb15r5
 K183kb2r0
 K28
 kb6r7
 K80
 kb11r0
 K132
 kb15r6
 K184kb2r1
 K29
 kb6r6
 K80
 kb11r1
 K133
 kb15r7
 K185kb2r2
 K30
 kb7shunt
 K82
 kb11r2
 K134
 kb16shunt
 K186kb2r3
 K31
 kb7
 K83
 kb11r3
 K135
 kb16
 K187kb2r4
 K32
 kbc78
 K84
 kb11r4
 K136
 kbc1617
 K188kb2r5
 K33
 test4
 K85
 kb11r5
 K137
 kb16r0
 K189kb2r6
 K34
 kb7r0
 K86
 kb11r6
 K138
 kb16r1
 K190kb2r7
 K35
 kb7r1
 K87
 kb11r7
 K139
 kb16r2
 K191kb3shunt
 K36
 kb7r2
 K88
 kb12shunt
 K140
 kb16r3
 K192kb3
 K37
 kb7r3
 K89
 kb12
 K141
 kb16r4
 K193kbc34
 K38
 kb7r4
 K90
 kbc1213
 K142
 kb16r5
 K194test2
 K39
 kb7r5
 K91
 kb12r0
 K143
 kb16r6
 K195kb3r0
 K40
 kb7r6
 K92
 kb12r1
 K144
 kb16r7
 K196kb3r1
 K41
 kb7r7
 K93
 kb12r2
 K145
 kb17shunt
 K197kb3r2
 K42
 kb8shunt
 K94
 kb12r3
 K146
 kb17
 K198kb3r3
 K43
 kb8
 K95
 kb12r4
 K147
 test9
 K199kb3r4
 K44
 kbc89
 K96
 kb12r5
 K148
 kb17r0
 K200kb3r5
 K45
 kb8r0
 K97
 kb12r6
 K149
 kb17r1
 K201kb3r6
 K46
 kb8r1
 K98
 kb12r7
 K150
 kb17r2
 K202kb3r7
 K47
 kb8r2
 K99
 kb13shunt
 K151
 kb17r3
 K203kb4shunt
 K48
 kb8r3
 K100
 kb13
 K152
 kb17r4
 K204kb4
 K49
 kb8r4
 K101
 kbc1314
 K153
 kb17r5
 K205kbc45
 K50
 kb8r5
 K102
 test7
 K154
 kb17r6
 K206kb4r0
 K51
 kb8r6
 K103
 kb13r0
 K155
 kb17r7
 K207kb4r1
 K52
 kb8r7
 K104
 kb13r1
 K156
 —
 —
3. Remove the front panel, as shown in the following image. 1
 Bracket2
 Front Panel3
 Front Panel Overlay4
 Screws
4. Remove the bracket, as shown in the following image. 
 1
 CA3 Digital Back End2
 Bracket3
 Daughter Card4
 Screws

#### Replace the Relay

The NI PXIe-2725 uses lead-free assemblies.

Note

Caution

Caution

Make sure you have the following:

- Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free solder
 rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part. Trim the replaced relay
 leads to no more than 1 mm (0.04 inch) from the PCB.

#### Reassemble the Module

Complete the Disassemble the Module steps in reverse order to reassemble your
 module.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXIe-2725

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2725-triggering.html language=enus -->
## TOPIC 00531: NI PXIe-2725 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2725-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2725-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXIe-2725. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger

### NI PXIe-2725 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXIe-2725.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXIe-2725.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXIe-2725

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2725.html language=enus -->
## TOPIC 00532: NI PXIe-2725

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2725.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2725.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2725 is a programmable resistor module for the PXI Express platform. The NI PXIe-2725 is composed of reed relays in parallel with discrete resistors. The NI PXIe-2725 has 18 channels that can nominally switch from 0 to 255 Ω in 1 Ω steps. NI has created a set of reference VIs that you

### NI PXIe-2725

Note

ni.com/info

272xOverview

Note

#### Operation Modes

The following table lists the supported topology of the NI PXIe-2725 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Eighteen 8-bit channels | 2725/Independent(NISWITCH_TOPOLOGY_2725_INDEPENDENT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXIe-2725 Independent Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2727-hardware-diagram.html language=enus -->
## TOPIC 00533: NI PXIe-2727 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2727-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2727-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXIe-2727. Resistance values are nominal. Please see the NI PXIe-2727 Specifications for resistor values and accuracy information The following table lists relay names for the NI PXIe-2727. Relays kb0r0, kb0r1...kb0r7 kb1r0, kb1r1...kb1r7

### NI PXIe-2727 Hardware Diagram

The following figure shows the hardware diagram for the NI PXIe-2727.

[IMAGE alt='image' src='GUID-0590338D-37EF-4DBC-96F9-1D43D45EFDE2-a5.gif']

Note

NI PXIe-2727
 Specifications

The following table lists relay names for the NI PXIe-2727.

| Relays |
| --- |
| kb0r0, kb0r1...kb0r7 |
| kb1r0, kb1r1...kb1r7 |
| kb2r0, kb2r1...kb2r7 |
| kb3r0, kb3r1...kb3r7 |
| kb4r0, kb4r1...kb4r7 |
| kb5r0, kb5r1...kb5r7 |
| kb6r0, kb6r1...kb6r7 |
| kb7r0, kb7r1...kb7r7 |
| kb8r0, kb8r1...kb8r7 |
| kb9r0, kb9r1...kb9r7 |
| kb10r0, kb10r1...kb10r7 |
| kb11r0, kb11r1...kb11r7 |
| kb12r0, kb12r1...kb12r7 |
| kb13r0, kb13r1...kb13r7 |
| kb14r0, kb14r1...kb14r7 |
| kb15r0, kb15r1...kb15r7 |
| kb16r0, kb16r1...kb16r7 |
| kb17r0, kb17r1...kb17r7 |
| kb0...kb17 |
| kb0shunt...kb17shunt |
| kbc01, kbc12...kbc1617 |
| ktest0, ktest1...ktest9 |

Parent topic:

NI PXIe-2727

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2727-independent-topology.html language=enus -->
## TOPIC 00534: NI PXIe-2727 Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2727-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2727-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2727 in the independent topology. Bank connect relays allow adjacent banks or channels to connect together internally. For example, you can connect two or more adjacent channels together to create a potentiometer, a voltage divider, or a multi-segment re

### NI PXIe-2727 Independent Topology

The following figure represents the NI PXIe-2727 in the independent topology.

[IMAGE alt='image' src='GUID-0590338D-37EF-4DBC-96F9-1D43D45EFDE2-a5.gif']

Note

#### Making a Connection

Each 16-bit channel is composed of two adjacent 8-bit banks on the NI PXIe-2727. For
 example, ch0 is composed of banks 0 and 1 and ch1 is composed of banks 2 and 3. NI
 has created a set of reference VIs that will programmatically open and close relays
 based on a user-specified resistance value or RTD temperature to simulate. To access
 these reference VIs, visit ni.com/info and enter the Info Code
 272xOverview. NI recommends using this set of reference VIs for
 the easiest programming experience. If not using these reference VIs, NI recommends
 using the low-level relay control VIs or functions instead of the connect channel
 VIs or functions. The DAQmx Relay API supports closing multiple relays in a single
 driver call, which is faster than the channel API.

When a bank relay is closed, the corresponding resistor is placed in parallel with
 the low resistance of the relay, which nominally equates to a zero Ω shunt. Closing
 any of the 8 bank relays in a given bank decreases the resistance of that bank.

For example, the following procedure uses the NI-SWITCH Relay API to short across the
 largest resistor in bank 0 and join bank 0 and bank 1 in series.

1. Close b0r7 by calling the niSwitch Relay Control
 VI
 with the inputs of b0r7 and close .
2. Close bc01 by calling the niSwitch Relay Control
 VI
 with the inputs of bc01 and close .

You can perform the same operation using the NI-SWITCH Channel API, as shown
 below.

1. Connect b0 -> b0r7 by calling niSwitch
 Connect Channels
 VI
 with the inputs of b0 and b0r7 .
2. Connect b0 -> b1 by calling niSwitch Connect
 Channels
 VI
 with the inputs of b0 and b1 .

Each bank is initially in a high impedance (open) state across the bank terminals. To
 enable the desired output channel you must first connect the bank relay,
 bN.

Each bank includes a shunt relay that completely bypasses the bank's string of 8
 series relays. Closing the shunt relay
 bN->bNshunt, for example,
 b0->b0shunt or low-level
 kb0shunt, results in a low resistance across the bank, 0 Ω
 nominally. This allows the NI PXIe-2727 module to pass signals with minimal
 attenuation. On 16-bit modules (NI PXI-2722 and NI PXIe-2727), closing the upper
 bank's shunt relay reduces the resistance when outputting values less than 64 Ω.

Note

The 4-pin front panel test connector can connect to any adjacent pair of even-odd
 banks, allowing resistance measurements, or voltage measurements, across those two
 banks ,for example b0 to b1, b2
 to b3, b4 to b5. On 16-bit NI
 272x modules, this allows channel resistance measurements using a DMM with Offset
 Compensated Ohms (such as the NI PXI-4070, NI PXI-4071, or NI PXI-4072). To connect
 a pair of banks to the test leads, close the appropriate test relays using the
 command testN->testout. For example, to measure
 the resistance across banks 0 and 1, call
 test0->testout and
 test1->testout. For banks 2 and 3, call
 test1->testout and
 test2->testout. Refer to the device's
 hardware diagram for valid test relay connections.

Note

Note

#### Pinout

The following figure identifies the pins for the NI PXIe-2727.

[IMAGE alt='image' src='GUID-02F4DB91-F1F7-4CBA-B55C-E203AF72CA2A-a5.gif']

Note

Parent topic:

NI PXIe-2727

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2727-relay-replacement.html language=enus -->
## TOPIC 00535: NI PXIe-2727 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2727-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2727-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2727 uses reed relays. The NI PXIe-2727 uses a custom lead length to meet safety standards. Trim leads per rework instructions or use one of the custom relays from the relay kit. Refer to the following tables for information about ordering replacement relays. Relay Relay Manufacturer P

### NI PXIe-2727 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay | Relay Manufacturer | Part Number |
| --- | --- | --- |
| All Relays | Coto | 9117-0001 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 781451-10 |

Complete the following sets of steps to disassemble the module, replace a failed relay,
 and reassemble your module.

#### Disassemble the Module

1. Ground yourself using a grounding strap or a ground connected to the PXI Express
 chassis. Note Properly grounding yourself prevents damage to
 your module from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figures and table
 for relay locations. NI PXIe 2727 Relay Map 
 [IMAGE alt='image' src='GUID-45423236-AB50-4D71-93E2-88A953F81DFF-a5.gif'] 
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorkb0shunt
 K1
 kb4r2
 K53
 kb9shunt
 K105
 kb13r2
 K157kb0
 K2
 kb4r3
 K54
 kb9
 K106
 kb13r3
 K158kbc01
 K3
 kb4r4
 K55
 kbc910
 K107
 kb13r4
 K159test0
 K4
 kb4r5
 K56
 test5
 K108
 kb13r5
 K160kb0r0
 K5
 kb4r6
 K57
 kb9r0
 K109
 kb13r6
 K161kb0r1
 K6
 kb4r7
 K58
 kb9r1
 K110
 kb13r7
 K162kb0r2
 K7
 kb5shunt
 K59
 kb9r2
 K111
 kb14shunt
 K163kb0r3
 K8
 kb5
 K60
 kb9r3
 K112
 kb14
 K164kb0r4
 K9
 kbc56
 K61
 kb9r4
 K113
 kbc1415
 K165kb0r5
 K10
 test3
 K62
 kb9r5
 K114
 kb14r0
 K166kb0r6
 K11
 kb5r0
 K63
 kb9r6
 K115
 kb14r1
 K167kb0r7
 K12
 kb5r1
 K64
 kb9r7
 K116
 kb14r2
 K168kb1shunt
 K13
 kb5r2
 K65
 kb10shunt
 K117
 kb14r3
 K169kb1
 K14
 kb5r3
 K66
 kb10
 K118
 kb14r4
 K170kbc12
 K15
 kb5r4
 K67
 kbc1011
 K119
 kb14r5
 K171test1
 K16
 kb5r5
 K68
 kb10r0
 K120
 kb14r6
 K172kb1r0
 K17
 kb5r6
 K69
 kb10r1
 K121
 kb14r7
 K173kb1r1
 K18
 kb5r7
 K70
 kb10r2
 K122
 kb15shunt
 K174kb1r2
 K19
 kb6shunt
 K71
 kb10r3
 K123
 kb15
 K175kb1r3
 K20
 kb6
 K72
 kb10r4
 K124
 kbc1516
 K176kb1r4
 K21
 kbc67
 K73
 kb10r5
 K125
 test8
 K177kb1r5
 K22
 kb6r0
 K74
 kb10r6
 K126
 kb15r0
 K178kb1r6
 K23
 kb6r1
 K75
 kb10r7
 K127
 kb15r1
 K179kb1r7
 K24
 kb6r2
 K76
 kb11shunt
 K128
 kb15r2
 K180kb2shunt
 K25
 kb6r3
 K77
 kb11
 K129
 kb15r3
 K181kb2
 K26
 kb6r4
 K78
 kbc1112
 K130
 kb15r4
 K182kbc23
 K27
 kb6r5
 K79
 test6
 K131
 kb15r5
 K183kb2r0
 K28
 kb6r7
 K80
 kb11r0
 K132
 kb15r6
 K184kb2r1
 K29
 kb6r6
 K80
 kb11r1
 K133
 kb15r7
 K185kb2r2
 K30
 kb7shunt
 K82
 kb11r2
 K134
 kb16shunt
 K186kb2r3
 K31
 kb7
 K83
 kb11r3
 K135
 kb16
 K187kb2r4
 K32
 kbc78
 K84
 kb11r4
 K136
 kbc1617
 K188kb2r5
 K33
 test4
 K85
 kb11r5
 K137
 kb16r0
 K189kb2r6
 K34
 kb7r0
 K86
 kb11r6
 K138
 kb16r1
 K190kb2r7
 K35
 kb7r1
 K87
 kb11r7
 K139
 kb16r2
 K191kb3shunt
 K36
 kb7r2
 K88
 kb12shunt
 K140
 kb16r3
 K192kb3
 K37
 kb7r3
 K89
 kb12
 K141
 kb16r4
 K193kbc34
 K38
 kb7r4
 K90
 kbc1213
 K142
 kb16r5
 K194test2
 K39
 kb7r5
 K91
 kb12r0
 K143
 kb16r6
 K195kb3r0
 K40
 kb7r6
 K92
 kb12r1
 K144
 kb16r7
 K196kb3r1
 K41
 kb7r7
 K93
 kb12r2
 K145
 kb17shunt
 K197kb3r2
 K42
 kb8shunt
 K94
 kb12r3
 K146
 kb17
 K198kb3r3
 K43
 kb8
 K95
 kb12r4
 K147
 test9
 K199kb3r4
 K44
 kbc89
 K96
 kb12r5
 K148
 kb17r0
 K200kb3r5
 K45
 kb8r0
 K97
 kb12r6
 K149
 kb17r1
 K201kb3r6
 K46
 kb8r1
 K98
 kb12r7
 K150
 kb17r2
 K202kb3r7
 K47
 kb8r2
 K99
 kb13shunt
 K151
 kb17r3
 K203kb4shunt
 K48
 kb8r3
 K100
 kb13
 K152
 kb17r4
 K204kb4
 K49
 kb8r4
 K101
 kbc1314
 K153
 kb17r5
 K205kbc45
 K50
 kb8r5
 K102
 test7
 K154
 kb17r6
 K206kb4r0
 K51
 kb8r6
 K103
 kb13r0
 K155
 kb17r7
 K207kb4r1
 K52
 kb8r7
 K104
 kb13r1
 K156
 —
 —
3. Remove the front panel, as shown in the following image. 1
 Bracket2
 Front Panel3
 Front Panel Overlay4
 Screws
4. Remove the bracket, as shown in the following image. 1
 CA3 Digital Back End2
 Bracket3
 Daughter Card4
 Screws

#### Replace the Relay

The NI PXIe-2727 uses lead-free assemblies.

Note

Caution

Caution

Make sure you have the following:

- Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free solder
 rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part. Trim the replaced relay
 leads to no more than 1 mm (0.04 inch) from the PCB.

#### Reassemble the Module

Complete the Disassemble the Module steps in reverse order to reassemble your
 module.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXIe-2727

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2727-triggering.html language=enus -->
## TOPIC 00536: NI PXIe-2727 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2727-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2727-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXIe-2727. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger

### NI PXIe-2727 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXIe-2727.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXIe-2727.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXIe-2727

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2727.html language=enus -->
## TOPIC 00537: NI PXIe-2727

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2727.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2727.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2727 is a programmable resistor module for the PXI Express platform. The NI PXIe-2727 is composed of reed relays in parallel with discrete resistors. The NI PXIe-2727 has nine channels that can nominally switch from 0 to 16,383 Ω in 0.25 Ω steps. NI has created a set of reference VIs t

### NI PXIe-2727

Note

ni.com/info

272xOverview

Note

#### Operation Modes

The following table lists the supported topology of the NI PXIe-2727 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Nine 16-bit channels | 2727/Independent(NISWITCH_TOPOLOGY_2727_INDEPENDENT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXIe-2727 Independent Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2737-2-wire-4-64-matrix-topology.html language=enus -->
## TOPIC 00538: NI PXIe-2737 2-Wire 4×64 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2737-2-wire-4-64-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2737-2-wire-4-64-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2737 (NI 2737) in the 2-wire 4×64 matrix topology. Making a Connection The NI 2737 is a 4×64 matrix. In this topology you can connect any row to any column. In software, R0 refers to the R0+ and R0– pair. All other channels follow a similar naming scheme.

### NI PXIe-2737 2-Wire 4×64 Matrix Topology

The following figure represents the NI PXIe-2737 (NI 2737) in the 2-wire 4×64 matrix
 topology.

|  |
| --- |
|  |

#### Making a Connection

The NI 2737 is a 4×64 matrix. In this topology you can connect any row to any
 column. In software, R0 refers to the R0+ and R0– pair. All other channels follow a
 similar naming scheme.

You can connect the channels of the NI 2737 using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function. For example, to connect row 1 to column 1, call the niSwitch Connect
 Channels VI or the niSwitch_Connect function with the
 channel 1 parameter set to r1 and the
 channel 2 parameter set to c1, or vice
 versa.

#### Pinout

The following figure identifies the pins for the NI 2737.

[IMAGE alt='image' src='GUID-DE06F79C-8F85-45C2-BB0E-F0A9E0E5164A-a5.gif']

Parent topic:

NI PXIe-2727

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2737-front-panel.html language=enus -->
## TOPIC 00539: NI PXIe-2737 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2737-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2737-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXIe-2737 front panel.

### NI PXIe-2737 Front Panel

The following figure illustrates the NI PXIe-2737 front panel.

[IMAGE alt='image' src='GUID-5DD846D3-29E5-41A6-82F1-F13BA42AE467-a5.gif']

Parent topic:

NI PXIe-2737

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2737-hardware-diagram.html language=enus -->
## TOPIC 00540: NI PXIe-2737 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2737-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2737-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXIe-2737 (NI 2737). The following table lists relay names for the NI 2737. Relays kr0c0...kr0c63 kr1c0...kr1c63 kr2c0...kr2c63 kr3c0...kr3c63

### NI PXIe-2737 Hardware Diagram

The following figure shows the hardware diagram for the NI PXIe-2737 (NI 2737).

[IMAGE alt='image' src='GUID-F4AACA6D-84CA-4A46-9AA5-1D0D4B80772D-a5.gif']

The following table lists relay names for the NI 2737.

| Relays |
| --- |
| kr0c0...kr0c63 |
| kr1c0...kr1c63 |
| kr2c0...kr2c63 |
| kr3c0...kr3c63 |

Parent topic:

NI PXIe-2737

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2737-relay-replacement.html language=enus -->
## TOPIC 00541: NI PXIe-2737 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2737-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2737-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2737 uses electromechanical armature relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Tyco Electronics 5-1462039-8 Relay Kit Part Number National Instruments (10 relays) 781089-10 Complete the following steps to disassemble y

### NI PXIe-2737 Relay Replacement

The NI PXIe-2737 uses electromechanical armature relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part |
| --- | --- |
| Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 781089-10 |

Complete the following steps to disassemble your module, replace a failed relay, and
 reassemble your module.

#### Locate the Relay

1. Ground yourself using a grounding strap or a ground connected to your PXI
 Express chassis. Note Properly grounding yourself prevents
 damage to your module from electrostatic discharge.
2. Refer to the following figures and table to locate the relay you want to
 replace. 
 NI PXIe-2737 PCB 1 
 [IMAGE alt='image' src='GUID-253B5066-3592-40F7-919F-C111A1629030-a5.gif'] 
 NI PXIe-2737 PCB 2 
 [IMAGE alt='image' src='GUID-3F6D4759-1EA8-4E40-992E-8E4682F2811C-a5.gif'] 
 NI PXIe-2737 Hardware Diagram 
 [IMAGE alt='image' src='GUID-F4AACA6D-84CA-4A46-9AA5-1D0D4B80772D-a5.gif'] 
 Table 14.NI PXIe-2737 PCB 1 Relay LocationsRelay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designatorkr0c0
 K1
 kr2c0
 K5
 kr0c16
 K65
 kr2c16
 K69kr0c1
 K2
 kr2c1
 K6
 kr0c17
 K66
 kr2c17
 K70kr0c2
 K9
 kr2c2
 K13
 kr0c18
 K73
 kr2c18
 K77kr0c3
 K10
 kr2c3
 K14
 kr0c19
 K74
 kr2c19
 K78kr0c4
 K17
 kr2c4
 K21
 kr0c20
 K81
 kr2c20
 K85kr0c5
 K18
 kr2c5
 K22
 kr0c21
 K82
 kr2c21
 K86kr0c6
 K25
 kr2c6
 K29
 kr0c22
 K89
 kr2c22
 K93kr0c7
 K26
 kr2c7
 K30
 kr0c23
 K90
 kr2c23
 K94kr0c8
 K33
 kr2c8
 K37
 kr0c24
 K97
 kr2c24
 K101kr0c9
 K34
 kr2c9
 K38
 kr0c25
 K98
 kr2c25
 K102kr0c10
 K41
 kr2c10
 K45
 kr0c26
 K105
 kr2c26
 K109kr0c11
 K42
 kr2c11
 K46
 kr0c27
 K106
 kr2c27
 K110kr0c12
 K49
 kr2c12
 K53
 kr1c16
 K67
 kr3c16
 K71kr0c13
 K50
 kr2c13
 K54
 kr1c17
 K68
 kr3c17
 K72kr0c14
 K57
 kr2c14
 K61
 kr1c18
 K75
 kr3c18
 K79kr0c15
 K58
 kr2c15
 K62
 kr1c19
 K76
 kr2c19
 K80kr1c0
 K3
 kr3c0
 K7
 kr1c20
 K83
 kr3c20
 K87kr1c1
 K4
 kr3c1
 K8
 kr1c21
 K84
 kr3c21
 K88kr1c2
 K11
 kr3c2
 K15
 kr1c22
 K91
 kr3c22
 K95kr1c3
 K12
 kr3c3
 K16
 kr1c23
 K92
 kr3c23
 K96kr1c4
 K19
 kr3c4
 K23
 kr1c24
 K99
 kr3c24
 K103kr1c5
 K20
 kr3c5
 K24
 kr1c25
 K100
 kr3c25
 K104kr1c6
 K27
 kr3c6
 K31
 kr1c26
 K107
 kr3c26
 K111kr1c7
 K28
 kr3c7
 K32
 kr1c27
 K108
 kr3c27
 K112kr1c8
 K35
 kr3c8
 K39kr1c9
 K36
 kr3c9
 K40kr1c10
 K43
 kr3c10
 K47kr1c11
 K44
 kr3c11
 K48kr1c12
 K51
 kr3c12
 K55kr1c13
 K52
 kr3c13
 K56kr1c14
 K59
 kr3c14
 K63kr1c15
 K60
 kr3c15
 K64 
 Table 15.NI PXIe-2737 PCB 2 Relay LocationsRelay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designatorkr0c28
 K11
 kr0c32
 K33
 kr2c32
 K29
 kr0c48
 K69
 kr2c48
 K65kr0c29
 K10
 kr0c33
 K32
 kr2c33
 K28
 kr0c49
 K68
 kr2c49
 K64kr0c30
 K22
 kr0c34
 K44
 kr2c34
 K40
 kr0c50
 K80
 kr2c50
 K76kr0c31
 K21
 kr0c35
 K43
 kr2c35
 K39
 kr0c51
 K79
 kr2c51
 K75kr1c28
 K9
 kr0c36
 K55
 kr2c36
 K51
 kr0c52
 K91
 kr2c52
 K87kr1c29
 K8
 kr0c37
 K54
 kr2c37
 K50
 kr0c53
 K90
 kr2c53
 K86kr1c30
 K20
 kr0c38
 K3
 kr2c38
 K1
 kr0c54
 K102
 kr2c54
 K98kr1c31
 K19
 kr0c39
 K14
 kr2c39
 K12
 kr0c55
 K101
 kr2c55
 K97kr2c28
 K7
 kr0c40
 K25
 kr2c40
 K23
 kr0c56
 K113
 kr2c56
 K109kr2c29
 K6
 kr0c41
 K36
 kr2c41
 K34
 kr0c57
 K112
 kr2c57
 K108kr2C30
 K18
 kr0c42
 K47
 kr2c42
 K45
 kr0c58
 K124
 kr2c58
 K120kr2c31
 K17
 kr0c43
 K58
 kr2c43
 K56
 kr0c59
 K123
 kr2c59
 K119kr3c28
 K5
 kr0c44
 K61
 kr2c44
 K59
 kr0c60
 K135
 kr2c60
 K131kr3c29
 K4
 kr0c45
 K72
 kr2c45
 K70
 kr0c61
 K134
 kr2c61
 K130kr3c30
 K16
 kr0c46
 K83
 kr2c46
 K81
 kr0c62
 K144
 kr2c62
 K140kr3c31
 K15
 kr0c47
 K94
 kr2c47
 K92
 kr0c63
 K143
 kr2c63
 K139kr1c32
 K31
 kr3c32
 K27
 kr1c48
 K67
 kr3c48
 K63kr1c33
 K30
 kr3c33
 K26
 kr1c49
 K66
 kr3c49
 K62kr1c34
 K42
 kr3c34
 K38
 kr1c50
 K78
 kr3c50
 K74kr1c35
 K41
 kr3c35
 K37
 kr1c51
 K77
 kr3c51
 K73kr1c36
 K53
 kr3c36
 K49
 kr1c52
 K89
 kr3c52
 K85kr1c37
 K52
 kr3c37
 K48
 kr1c53
 K88
 kr3c53
 K84kr1c38
 K2
 kr3c38
 K127
 kr1c54
 K100
 kr3c54
 K96kr1c39
 K13
 kr3c39
 K126
 kr1c55
 K99
 kr3c55
 K95kr1c40
 K24
 kr3c40
 K116
 kr1c56
 K111
 kr3c56
 K107kr1c41
 K35
 kr3c41
 K115
 kr1c57
 K110
 kr3c57
 K106kr1c42
 K46
 kr3c42
 K105
 kr1c58
 K122
 kr3c58
 K118kr1c43
 K57
 kr3c43
 K136
 kr1c59
 K121
 kr3c59
 K117kr1c44
 K60
 kr3c44
 K125
 kr1c60
 K133
 kr3c60
 K129kr1c45
 K71
 kr3c45
 K114
 kr1c61
 K132
 kr3c61
 K128kr1c46
 K82
 kr3c46
 K103
 kr1c62
 K142
 kr3c62
 K138kr1c47
 K93
 kr3c47
 K104
 kr1c63
 K141
 kr3c63
 K137
  1. Match the channel name to its corresponding relay name.
  2. Match the relay name with its reference designator using the tables
 below. Note Reference designators are printed on the
 PCB.

#### Disassemble the Module

1. Remove the four screws that secure PCB 2 to the switch assembly.
2. Gently separate PCB 1 and PCB 2. 1
 PCB 12
 PCB 23
 Screw

#### Replace the Relay

Note

Caution

Caution

Verify that you have the following items:

- Temperature-regulated soldering iron set to 316 °C (600 °F) for lead solder
 rework or 371 °C (700 °F) for lead-free solder rework
- 63/37 Tin/Lead solder (flux core) for lead solder rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Complete the following steps to replace a relay:

1. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. The different label types are shown in the following figure.
 [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']
2. Replace the relay as you would any other through-hole part. Trim the replaced
 relay to no more than 0.41 mm (0.016 inch) from the PCB.

#### Reassemble the Module

Complete the Disassemble the Module steps in reverse order to reassemble your
 module.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXIe-2737

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2737.html language=enus -->
## TOPIC 00542: NI PXIe-2737

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2737.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2737.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2737 (NI 2737) is a 256 crosspoint, high-density matrix switch module for the PXI Express platform. The NI 2737 is designed for switching low and high voltages. For low-voltage measurements, the NI 2737 uses relays with <10 µV thermal offset to ensure accurate measurements. Switching i

### NI PXIe-2737

Note

#### Operation Modes

The following table lists the supported topology of the NI 2737 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 2-Wire 4×64 Matrix | 2737/2-Wire 4x64 Matrix(NISWITCH_TOPOLOGY_2737_2_WIRE_4X64_MATRIX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXIe-2737 2-Wire 4×64 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2738-2-wire-8-32-matrix-topology.html language=enus -->
## TOPIC 00543: NI PXIe-2738 2-Wire 8×32 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2738-2-wire-8-32-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2738-2-wire-8-32-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2738 (NI 2738) in the 2-wire 8×32 matrix topology. Making a Connection The NI 2738 is an 8×32 matrix. In this topology you can connect any row to any column. In software, R0 refers to the R0+ and R0– pair. All other channels follow a similar naming scheme.

### NI PXIe-2738 2-Wire 8×32 Matrix Topology

The following figure represents the NI PXIe-2738 (NI 2738) in the 2-wire 8×32 matrix
 topology.

|  |
| --- |
|  |

#### Making a Connection

The NI 2738 is an 8×32 matrix. In this topology you can connect any row to any
 column. In software, R0 refers to the R0+ and R0– pair. All other channels follow a
 similar naming scheme.

You can connect the channels of the NI 2738 using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function. For example, to connect row 1 to column 1, call the niSwitch Connect
 Channels VI or the niSwitch_Connect function with the
 channel 1 parameter set to r1 and the
 channel 2 parameter set to c1, or vice
 versa.

#### Pinout

The following figure identifies the pins for the NI 2738.

[IMAGE alt='image' src='GUID-2290F9FA-AE4A-4E30-A44A-EC43D797DBE8-a5.gif']

Parent topic:

NI PXIe-2738

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2738-front-panel.html language=enus -->
## TOPIC 00544: NI PXIe-2738 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2738-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2738-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXIe-2738 front panel.

### NI PXIe-2738 Front Panel

The following figure illustrates the NI PXIe-2738 front panel.

[IMAGE alt='image' src='GUID-2ECC75E4-0553-467A-B694-C1A73887473E-a5.gif']

Parent topic:

NI PXIe-2738

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2738-hardware-diagram.html language=enus -->
## TOPIC 00545: NI PXIe-2738 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2738-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2738-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXIe-2738. The following table lists relay names for the NI 2738. Relays kr0c0...kr0c31 kr1c0...kr1c31 kr2c0...kr2c31 kr3c0...kr3c31 kr4c0...kr4c31 kr5c0...kr5c31 kr6c0...kr6c31 kr7c0...kr7c31

### NI PXIe-2738 Hardware Diagram

The following figure shows the hardware diagram for the NI PXIe-2738.

[IMAGE alt='image' src='GUID-026FD3BF-C891-477E-AA29-328C0FF7D19B-a5.gif']

The following table lists relay names for the NI 2738.

| Relays |
| --- |
| kr0c0...kr0c31 |
| kr1c0...kr1c31 |
| kr2c0...kr2c31 |
| kr3c0...kr3c31 |
| kr4c0...kr4c31 |
| kr5c0...kr5c31 |
| kr6c0...kr6c31 |
| kr7c0...kr7c31 |

Parent topic:

NI PXIe-2738

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2738-relay-replacement.html language=enus -->
## TOPIC 00546: NI PXIe-2738 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2738-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2738-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2738 uses electromechanical armature relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Tyco Electronics 5-1462039-8 Relay Kit Part Number National Instruments (10 relays) 781089-10 Complete the following steps to disassemble y

### NI PXIe-2738 Relay Replacement

The NI PXIe-2738 uses electromechanical armature relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part |
| --- | --- |
| Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 781089-10 |

Complete the following steps to disassemble your module, replace a failed relay, and
 reassemble your module.

#### Locate the Relay

1. Ground yourself using a grounding strap or a ground connected to your PXI
 Express chassis. Note Properly grounding yourself prevents
 damage to your module from electrostatic discharge.
2. Refer to the following figures and table for the relay you want to replace. NI PXIe-2738 PCB 1 [IMAGE alt='image' src='GUID-83ADD297-5CC8-454C-84DC-D2D03D964408-a5.gif'] NI PXIe-2738 PCB 2 [IMAGE alt='image' src='GUID-3919B51C-04B0-4E3F-B336-96204E365779-a5.gif'] NI PXIe-2738 Hardware
 Diagram [IMAGE alt='image' src='GUID-026FD3BF-C891-477E-AA29-328C0FF7D19B-a5.gif'] Table 16.NI PXIe-2738 PCB 1 Relay LocationsRelay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designatorkr0c0
 K1
 kr2c0
 K5
 kr0c16
 K65
 kr2c16
 K69kr0c1
 K2
 kr2c1
 K6
 kr0c17
 K66
 kr2c17
 K70kr0c2
 K9
 kr2c2
 K13
 kr0c18
 K73
 kr2c18
 K77kr0c3
 K10
 kr2c3
 K14
 kr0c19
 K74
 kr2c19
 K78kr0c4
 K17
 kr2c4
 K21
 kr0c20
 K81
 kr2c20
 K85kr0c5
 K18
 kr2c5
 K22
 kr0c21
 K82
 kr2c21
 K86kr0c6
 K25
 kr2c6
 K29
 kr0c22
 K89
 kr2c22
 K93kr0c7
 K26
 kr2c7
 K30
 kr0c23
 K90
 kr2c23
 K94kr0c8
 K33
 kr2c8
 K37
 kr0c24
 K97
 kr2c24
 K101kr0c9
 K34
 kr2c9
 K38
 kr0c25
 K98
 kr2c25
 K102kr0c10
 K41
 kr2c10
 K45
 kr0c26
 K105
 kr2c26
 K109kr0c11
 K42
 kr2c11
 K46
 kr0c27
 K106
 kr2c27
 K110kr0c12
 K49
 kr2c12
 K53
 kr1c16
 K67
 kr3c16
 K71kr0c13
 K50
 kr2c13
 K54
 kr1c17
 K68
 kr3c17
 K72kr0c14
 K57
 kr2c14
 K61
 kr1c18
 K75
 kr3c18
 K79kr0c15
 K58
 kr2c15
 K62
 kr1c19
 K76
 kr3c19
 K80kr1c0
 K3
 kr3c0
 K7
 kr1c20
 K83
 kr3c20
 K87kr1c1
 K4
 kr3c1
 K8
 kr1c21
 K84
 kr3c21
 K88kr1c2
 K11
 kr3c2
 K15
 kr1c22
 K91
 kr3c22
 K95kr1c3
 K12
 kr3c3
 K16
 kr1c23
 K92
 kr3c23
 K96kr1c4
 K19
 kr3c4
 K23
 kr1c24
 K99
 kr3c24
 K103kr1c5
 K20
 kr3c5
 K24
 kr1c25
 K100
 kr3c25
 K104kr1c6
 K27
 kr3c6
 K31
 kr1c26
 K107
 kr3c26
 K111kr1c7
 K28
 kr3c7
 K32
 kr1c27
 K108
 kr3c27
 K112kr1c8
 K35
 kr3c8
 K39kr1c9
 K36
 kr3c9
 K40kr1c10
 K43
 kr3c10
 K47kr1c11
 K44
 kr3c11
 K48kr1c12
 K51
 kr3c12
 K55kr1c13
 K52
 kr3c13
 K56kr1c14
 K59
 kr3c14
 K63kr1c15
 K60
 kr3c15
 K64 Table 17.NI PXIe-2738 PCB 2
 Relay LocationsRelay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designatorkr0c28
 K11
 kr4c0
 K33
 kr6c0
 K29
 kr4c16
 K69
 kr6c16
 K65kr0c29
 K10
 kr4c1
 K32
 kr6c1
 K28
 kr4c17
 K68
 kr6c17
 K64kr0c30
 K22
 kr4c2
 K44
 kr6c2
 K40
 kr4c18
 K80
 kr6c18
 K76kr0c31
 K21
 kr4c3
 K43
 kr6c3
 K39
 kr4c19
 K79
 kr6c19
 K75kr1c28
 K9
 kr4c4
 K55
 kr6c4
 K51
 kr4c20
 K91
 kr6c20
 K87kr1c29
 K8
 kr4c5
 K54
 kr6c5
 K50
 kr4c21
 K90
 kr6c21
 K86kr1c30
 K20
 kr4c6
 K3
 kr6c6
 K1
 kr4c22
 K102
 kr6c22
 K98kr1c31
 K19
 kr4c7
 K14
 kr6c7
 K12
 kr4c23
 K101
 kr6c23
 K97kr2c28
 K7
 kr4c8
 K25
 kr6c8
 K23
 kr4c24
 K113
 kr6c24
 K109kr2c29
 K6
 kr4c9
 K36
 kr6c9
 K34
 kr4c25
 K112
 kr6c25
 K108kr2c30
 K18
 kr4c10
 K47
 kr6c10
 K45
 kr4c26
 K124
 kr6c26
 K120kr2c31
 K17
 kr4c11
 K58
 kr6c11
 K56
 kr4c27
 K123
 kr6c27
 K119kr3c28
 K5
 kr4c12
 K61
 kr6c12
 K59
 kr4c28
 K135
 kr6c28
 K131kr3c29
 K4
 kr4c13
 K72
 kr6c13
 K70
 kr4c29
 K134
 kr6c29
 K130kr3c30
 K16
 kr4c14
 K83
 kr6c14
 K81
 kr4c30
 K144
 kr6c30
 K140kr3c31
 K15
 kr4c15
 K94
 kr6c15
 K92
 kr4c31
 K143
 kr6c31
 K139kr5c0
 K31
 kr7c0
 K27
 kr5c16
 K67
 kr7c16
 K63kr5c1
 K30
 kr7c1
 K26
 kr5c17
 K66
 kr7c17
 K62kr5c2
 K42
 kr7c2
 K38
 kr5c18
 K78
 kr7c18
 K74kr5c3
 K41
 kr7c3
 K37
 kr5c19
 K77
 kr7c19
 K73kr5c4
 K53
 kr7c4
 K49
 kr5c20
 K89
 kr7c20
 K85kr5c5
 K52
 kr7c5
 K48
 kr5c21
 K88
 kr7c21
 K84kr5c6
 K2
 kr7c6
 K127
 kr5c22
 K100
 kr7c22
 K96kr5c7
 K13
 kr7c7
 K126
 kr5c23
 K99
 kr7c23
 K95kr5c8
 K24
 kr7c8
 K116
 kr5c24
 K111
 kr7c24
 K107kr5c9
 K35
 kr7c9
 K115
 kr5c25
 K110
 kr7c25
 K106kr5c10
 K46
 kr7c10
 K105
 kr5c26
 K122
 kr7c26
 K118kr5c11
 K57
 kr7c11
 K136
 kr5c27
 K121
 kr7c27
 K117kr5c12
 K60
 kr7c12
 K125
 kr5c28
 K133
 kr7c28
 K129kr5c13
 K71
 kr7c13
 K114
 kr5c29
 K132
 kr7c29
 K128kr5c14
 K82
 kr7c14
 K103
 kr5c30
 K142
 kr7c30
 K138kr5c15
 K93
 kr7c15
 K104
 kr5c31
 K141
 kr7c31
 K137
  1. Match the channel name to its corresponding relay name.
  2. Match the relay name with its reference designator using the tables
 below. Note Reference designators are printed on the
 PCB.

#### Disassemble the Module

1. Remove the four screws that secure PCB 2 to the switch assembly.
2. Gently separate PCB 1 and PCB 2. 
 1
 PCB 12
 PCB 23
 Screw

#### Replace the Relay

Note

Caution

Caution

Verify that you have the following items:

- Temperature-regulated soldering iron set to 316 °C (600 °F) for lead solder
 rework or 371 °C (700 °F) for lead-free solder rework
- 63/37 Tin/Lead solder (flux core) for lead solder rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Complete the following steps to replace a relay:

1. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. The different label types are shown in the following figure.
 [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']
2. Replace the relay as you would any other through-hole part. Trim the replaced
 relay to no more than 0.41 mm (0.016 inch) from the PCB.

#### Reassemble the Module

Complete the Disassemble the Module steps in reverse order to reassemble your
 module.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXIe-2738

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2738.html language=enus -->
## TOPIC 00547: NI PXIe-2738

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2738.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2738.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2738 (NI 2738) is a 256 crosspoint, high-density matrix switch module for the PXI Express platform. The NI 2738 is designed for switching low and high voltages. For low-voltage measurements, the NI 2738 uses relays with <10 µV thermal offset to ensure accurate measurements. Switching i

### NI PXIe-2738

Note

#### Operation Modes

The following table lists the supported topologies of the NI 2738 and possible operation
 modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 2-Wire 8×32 Matrix | 2738/2-Wire 8x32 Matrix (NISWITCH_TOPOLOGY_2738_2_WIRE_8X32_MATRIX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXIe-2738 2-Wire 8×32 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2739-2-wire-16-16-matrix-topology.html language=enus -->
## TOPIC 00548: NI PXIe-2739 2-Wire 16×16 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2739-2-wire-16-16-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2739-2-wire-16-16-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2739 (NI 2739) in the 2-wire 16×16 matrix topology. Making a Connection The NI 2739 is a 16×16 matrix. In this topology, you can connect any row to any column. In software, R0 refers to the R0+ and R0- pair. All other channels follow a similar naming schem

### NI PXIe-2739 2-Wire 16×16 Matrix Topology

The following figure represents the NI PXIe-2739 (NI 2739) in the 2-wire 16×16 matrix
 topology.

|  |
| --- |

#### Making a Connection

The NI 2739 is a 16×16 matrix. In this topology, you can connect any row to any
 column. In software, R0 refers to the R0+ and R0- pair. All other channels follow a
 similar naming scheme.

You can connect the channels of the NI 2739 using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function. For example, to connect row 1 to column 1, call the niSwitch Connect
 Channels VI or the niSwitch_Connect function with the
 channel 1 parameter set to r1 and the
 channel 2 parameter set to c1.

#### Pinout

The following figure identifies the pins for the NI 2739.

[IMAGE alt='image' src='GUID-B97E638B-F4BB-4BDF-B337-53E451995CEE-a5.gif']

Parent topic:

NI PXIe-2739

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2739-front-panel.html language=enus -->
## TOPIC 00549: NI PXIe-2739 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2739-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2739-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXIe-2739 front panel.

### NI PXIe-2739 Front Panel

The following figure illustrates the NI PXIe-2739 front panel.

[IMAGE alt='image' src='GUID-94E569C9-BD2F-4F72-AB02-8E8FA71F9EC1-a5.gif']

Parent topic:

NI PXIe-2739

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2739-hardware-diagram.html language=enus -->
## TOPIC 00550: NI PXIe-2739 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2739-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2739-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXIe-2739. The following table lists relay names for the NI 2739. Relays kr0c0...kr0c15 kr1c0...kr1c15 kr2c0...kr2c15 kr3c0...kr3c15 kr4c0...kr4c15 kr5c0...kr5c15 kr6c0...kr6c15 kr7c0...kr7c15 kr8c0...kr8c15 kr9c0...kr9c15 kr10c0...kr10c15 k

### NI PXIe-2739 Hardware Diagram

The following figure shows the hardware diagram for the NI PXIe-2739.

[IMAGE alt='image' src='GUID-91F5E63B-11B6-4B00-AF75-AB74D66022ED-a5.gif']

The following table lists relay names for the NI 2739.

| Relays |
| --- |
| kr0c0...kr0c15 |
| kr1c0...kr1c15 |
| kr2c0...kr2c15 |
| kr3c0...kr3c15 |
| kr4c0...kr4c15 |
| kr5c0...kr5c15 |
| kr6c0...kr6c15 |
| kr7c0...kr7c15 |
| kr8c0...kr8c15 |
| kr9c0...kr9c15 |
| kr10c0...kr10c15 |
| kr11c0...kr11c15 |
| kr12c0...kr12c15 |
| kr13c0...kr13c15 |
| kr14c0...kr14c15 |
| kr15c0...kr15c15 |

Parent topic:

NI PXIe-2739

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2739-relay-replacement.html language=enus -->
## TOPIC 00551: NI PXIe-2739 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2739-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2739-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2739 uses electromechanical armature relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Tyco Electronics 5-1462039-8 Relay Kit Part Number National Instruments (10 relays) 781089-10 Complete the following steps to disassemble y

### NI PXIe-2739 Relay Replacement

The NI PXIe-2739 uses electromechanical armature relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part |
| --- | --- |
| Tyco Electronics | 5-1462039-8 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 781089-10 |

Complete the following steps to disassemble your module, replace a failed relay, and
 reassemble your module.

#### Locate the Relay

1. Ground yourself using a grounding strap or a ground connected to your PXI
 Express chassis. Note Properly grounding yourself prevents
 damage to your module from electrostatic discharge.
2. Refer to the following figures and table to locate the relay you want to replace. NI PXIe-2739 PCB 1 [IMAGE alt='image' src='GUID-0088E514-158F-4BC6-9AA7-226FE14947FC-a5.gif'] NI PXIe-2739 PCB 2 [IMAGE alt='image' src='GUID-EBC8833B-C4AA-4BFB-91FF-96B7D4344898-a5.gif'] NI PXIe-2739 Hardware
 Diagram [IMAGE alt='image' src='GUID-91F5E63B-11B6-4B00-AF75-AB74D66022ED-a5.gif'] Table 18.NI PXIe-2739 PCB 1 Relay LocationsRelay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designatorkr0c0
 K1
 kr2c0
 K5
 kr4c0
 K65
 kr6c0
 K69kr0c1
 K2
 kr2c1
 K6
 kr4c1
 K66
 kr6c1
 K70kr0c2
 K9
 kr2c2
 K13
 kr4c2
 K73
 kr6c2
 K77kr0c3
 K10
 kr2c3
 K14
 kr4c3
 K74
 kr6c3
 K78kr0c4
 K17
 kr2c4
 K21
 kr4c4
 K81
 kr6c4
 K85kr0c5
 K18
 kr2c5
 K22
 kr4c5
 K82
 kr6c5
 K86kr0c6
 K25
 kr2c6
 K29
 kr4c6
 K89
 kr6c6
 K93kr0c7
 K26
 kr2c7
 K30
 kr4c7
 K90
 kr6c7
 K94kr0c8
 K33
 kr2c8
 K37
 kr4c8
 K97
 kr6c8
 K101kr0c9
 K34
 kr2c9
 K38
 kr4c9
 K98
 kr6c9
 K102kr0c10
 K41
 kr2c10
 K45
 kr4c10
 K105
 kr6c10
 K109kr0c11
 K42
 kr2c11
 K46
 kr4c11
 K106
 kr6c11
 K110kr0c12
 K49
 kr2c12
 K53
 kr5c0
 K67
 kr7c0
 K71kr0c13
 K50
 kr2c13
 K54
 kr5c1
 K68
 kr7c1
 K72kr0c14
 K57
 kr2c14
 K61
 kr5c2
 K75
 kr7c2
 K79kr0c15
 K58
 kr2c15
 K62
 kr5c3
 K76
 kr7c3
 K80kr1c0
 K3
 kr3c0
 K7
 kr5c4
 K83
 kr7c4
 K87kr1c1
 K4
 kr3c1
 K8
 kr5c5
 K84
 kr7c5
 K88kr1c2
 K11
 kr3c2
 K15
 kr5c6
 K91
 kr7c6
 K95kr1c3
 K12
 kr3c3
 K16
 kr5c7
 K92
 kr7c7
 K96kr1c4
 K19
 kr3c4
 K23
 kr5c8
 K99
 kr7c8
 K103kr1c5
 K20
 kr3c5
 K24
 kr5c9
 K100
 kr7c9
 K104kr1c6
 K27
 kr3c6
 K31
 kr5c10
 K107
 kr7c10
 K111kr1c7
 K28
 kr3c7
 K32
 kr5c11
 K108
 kr7c11
 K112kr1c8
 K35
 kr3c8
 K39kr1c9
 K36
 kr3c9
 K40kr1c10
 K43
 kr3c10
 K47kr1c11
 K44
 kr3c11
 K48kr1c12
 K51
 kr3c12
 K55kr1c13
 K52
 kr3c13
 K56kr1c14
 K59
 kr3c14
 K63kr1c15
 K60
 kr3c15
 K64 Table 19.NI PXIe-2739 PCB 2
 Relay LocationsRelay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designator
 Relay Name
 Reference Designatorkr4c12
 K11
 kr8c0
 K33
 kr10c0
 K29
 kr12c0
 K69
 kr14c0
 K65kr4c13
 K10
 kr8c1
 K32
 kr10c1
 K28
 kr12c1
 K68
 kr14c1
 K64kr4c14
 K22
 kr8c2
 K44
 kr10c2
 K40
 kr12c2
 K80
 kr14c2
 K76kr4c15
 K21
 kr8c3
 K43
 kr10c3
 K39
 kr12c3
 K79
 kr14c3
 K75kr5c12
 K9
 kr8c4
 K55
 kr10c4
 K51
 kr12c4
 K91
 kr14c4
 K87kr5c13
 K8
 kr8c5
 K54
 kr10c5
 K50
 kr12c5
 K90
 kr14c5
 K86kr5c14
 K20
 kr8c6
 K3
 kr10c6
 K1
 kr12c6
 K102
 kr14c6
 K98kr5c15
 K19
 kr8c7
 K14
 kr10c7
 K12
 kr12c7
 K101
 kr14c7
 K97kr6c12
 K7
 kr8c8
 K25
 kr10c8
 K23
 kr12c8
 K113
 kr14c8
 K109kr6c13
 K6
 kr8c9
 K36
 kr10c9
 K34
 kr12c9
 K112
 kr14c9
 K108kr6c14
 K18
 kr8c10
 K47
 kr10c10
 K45
 kr12c10
 K124
 kr14c10
 K120kr6c15
 K17
 kr8c11
 K58
 kr10c11
 K56
 kr12c11
 K123
 kr14c11
 K119kr7c12
 K5
 kr8c12
 K61
 kr10c12
 K59
 kr12c12
 K135
 kr14c12
 K131kr7c13
 K4
 kr8c13
 K72
 kr10c13
 K70
 kr12c13
 K134
 kr14c13
 K130kr7c14
 K16
 kr8c14
 K83
 kr10c14
 K81
 kr12c14
 K144
 kr14c14
 K140kr7c15
 K15
 kr8c15
 K94
 kr10c15
 K92
 kr12c15
 K143
 kr14c15
 K139kr9c0
 K31
 kr11c0
 K27
 kr13c0
 K67
 kr15c0
 K63kr9c1
 K30
 kr11c1
 K26
 kr13c1
 K66
 kr15c1
 K62kr9c2
 K42
 kr11c2
 K38
 kr13c2
 K78
 kr15c2
 K74kr9c3
 K41
 kr11c3
 K37
 kr13c3
 K77
 kr15c3
 K73kr9c4
 K53
 kr11c4
 K49
 kr13c4
 K89
 kr15c4
 K85kr9c5
 K52
 kr11c5
 K48
 kr13c5
 K88
 kr15c5
 K84kr9c6
 K2
 kr11c6
 K127
 kr13c6
 K100
 kr15c6
 K96kr9c7
 K13
 kr11c7
 K126
 kr13c7
 K99
 kr15c7
 K95kr9c8
 K24
 kr11c8
 K116
 kr13c8
 K111
 kr15c8
 K107kr9c9
 K35
 kr11c9
 K115
 kr13c9
 K110
 kr15c9
 K106kr9c10
 K46
 kr11c10
 K105
 kr13c10
 K122
 kr15c10
 K118kr9c11
 K57
 kr11c11
 K136
 kr13c11
 K121
 kr15c11
 K117kr9c12
 K60
 kr11c12
 K125
 kr13c12
 K133
 kr15c12
 K129kr9c13
 K71
 kr11c13
 K114
 kr13c13
 K132
 kr15c13
 K128kr9c14
 K82
 kr11c14
 K103
 kr13c14
 K142
 kr15c14
 K138kr9c15
 K93
 kr11c15
 K104
 kr13c15
 K141
 kr15c15
 K137
  1. Match the channel name to its corresponding relay name.
  2. Match the relay name with its reference designator using the tables
 below. Note Reference designators are printed on the
 PCB.

#### Disassemble the Module

1. Remove the four screws that secure PCB 2 to the switch assembly.
2. Gently separate PCB 1 and PCB 2. 1
 PCB 12
 PCB 23
 Screw

#### Replace the Relay

Note

Caution

Caution

Make sure you have the following items:

- Temperature-regulated soldering iron set to 316 °C (600 °F) for lead solder
 rework or 371 °C (700 °F) for lead-free solder rework
- 63/37 Tin/Lead solder (flux core) for lead solder rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

Complete the following steps to replace a relay:

1. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. The different label types are shown in the following figure.
 [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']
2. Replace the relay as you would any other through-hole part. Trim the replaced
 relay to no more than 0.41 mm (0.016 inch) from the PCB.

#### Reassemble the Module

Complete the Disassemble the Module steps in reverse order to reassemble your
 module.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXIe-2739

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2739.html language=enus -->
## TOPIC 00552: NI PXIe-2739

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2739.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2739.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2739 (NI 2739) is a 256 crosspoint, high-density matrix switch module for the PXI Express platform. The NI 2739 is designed for switching low and high voltages. For low-voltage measurements, the NI 2739 uses relays with <10 µV thermal offset to ensure accurate measurements. Switching i

### NI PXIe-2739

Note

#### Operation Modes

The following table lists the supported topologies of the NI 2739 and possible operation
 modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 2-Wire 16×16 Matrix | 2739/2-Wire 16x16 Matrix (NISWITCH_TOPOLOGY_2739_2_WIRE_16X16_MATRIX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXIe-2739 2-Wire 16×16 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2746-front-panel.html language=enus -->
## TOPIC 00553: NI PXIe-2746 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2746-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2746-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXIe-2746 front panel.

### NI PXIe-2746 Front Panel

The following figure illustrates the NI PXIe-2746 front panel.

[IMAGE alt='image' src='GUID-9D5C5900-9A32-4444-90C3-B9AED459E21F-a5.gif']

Parent topic:

NI PXI-2746

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2746-hardware-diagram.html language=enus -->
## TOPIC 00554: NI PXIe-2746 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2746-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2746-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXIe-2746.

### NI PXIe-2746 Hardware Diagram

The following figure shows the hardware diagram for the NI PXIe-2746.

[IMAGE alt='image' src='GUID-8A0A4B92-29EC-49CD-A6CC-DB19B873C5D4-a5.gif']

Parent topic:

NI PXI-2746

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2747-dual-8-1-multiplexer-sp8t-topolo.html language=enus -->
## TOPIC 00555: NI PXIe-2747 Dual 8×1 Multiplexer (SP8T) Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2747-dual-8-1-multiplexer-sp8t-topolo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2747-dual-8-1-multiplexer-sp8t-topolo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2747 in the 8×1 multiplexer topology. Making a Connection Call the niSwitch Connect Channels VI or the niSwitch_Connect function to connect channels in this topology. If applicable, you must call the niSwitch Disconnect Channels VI or the niSwitch_Disconne

### NI PXIe-2747 Dual 8×1 Multiplexer (SP8T) Topology

The following figure represents the NI PXIe-2747 in the 8×1 multiplexer topology.

[IMAGE alt='image' src='GUID-7EF1FB82-790A-406E-A188-DC834AB10996-a5.gif']

#### Making a Connection

Call the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function to connect channels in this topology. If applicable, you must call the
 niSwitch Disconnect
 Channels
 VI or the
 niSwitch_Disconnect
 function to disconnect an existing connection before you call the
 niSwitch Connect Channels VI or the niSwitch_Connect function.

Note

niSwitch_Disconnect

not

niSwitch_Connect

niSwitch_DisconnectAll

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between CH1 and COM and the other between CH2 and
 COM:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch1 and com .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 ch1 and com .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch2 and com .

Parent topic:

NI PXIe-2747

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2747-front-panel.html language=enus -->
## TOPIC 00556: NI PXIe-2747 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2747-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2747-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXIe-2747 front panel.

### NI PXIe-2747 Front Panel

The following figure illustrates the NI PXIe-2747 front panel.

[IMAGE alt='image' src='GUID-B59381DA-0E19-4FD0-8767-AEFC57501F82-a5.gif']

Parent topic:

NI PXIe-2747

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2747-hardware-diagram.html language=enus -->
## TOPIC 00557: NI PXIe-2747 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2747-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2747-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXIe-2747.

### NI PXIe-2747 Hardware Diagram

The following figure shows the hardware diagram for the NI PXIe-2747.

[IMAGE alt='image' src='GUID-E5A79FCC-5105-49AB-A11F-12DA005CF984-a5.gif']

Parent topic:

NI PXIe-2747

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2747.html language=enus -->
## TOPIC 00558: NI PXIe-2747

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2747.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2747.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2747 (NI 2747) is a dual 8×1 multiplexer switch module for the PXI Express bus that can carry 50 Ω RF signals up to 3 GHz. Operation Modes The following table lists the supported topology of the NI 2747 and possible operation modes. Topology Software Name Immediate Scanning Dual 8×1 Mult

### NI PXIe-2747

The NI PXIe-2747 (NI 2747) is a dual 8×1 multiplexer switch module for the PXI Express bus
 that can carry 50 Ω RF signals up to 3 GHz.

#### Operation Modes

The following table lists the supported topology of the NI 2747 and possible operation
 modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Dual 8×1 Multiplexer | 2747/Dual 8x1 Mux (NISWITCH_TOPOLOGY_2747_DUAL_8X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- RF Switching Considerations
- Topologies
- Operation Modes
- NI PXIe-2747 Dual 8×1 Multiplexer (SP8T) Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2748-16-1-multiplexer-sp8t-topology.html language=enus -->
## TOPIC 00559: NI PXIe-2748 16×1 Multiplexer (SP8T) Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2748-16-1-multiplexer-sp8t-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2748-16-1-multiplexer-sp8t-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2748 in the 16×1 multiplexer topology. Making a Connection Call the niSwitch Connect Channels VI or the niSwitch_Connect function to connect channels in this topology. If applicable, you must call the niSwitch Disconnect Channels VI or the niSwitch_Disconn

### NI PXIe-2748 16×1 Multiplexer (SP8T) Topology

The following figure represents the NI PXIe-2748 in the 16×1 multiplexer topology.

[IMAGE alt='image' src='GUID-87EC598D-C1B9-4CAF-9B6F-FCAF66429400-a5.gif']

#### Making a Connection

Call the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function to connect channels in this topology. If applicable, you must call the
 niSwitch Disconnect
 Channels
 VI or the
 niSwitch_Disconnect
 function to disconnect an existing connection before you call the
 niSwitch Connect Channels VI or the niSwitch_Connect function.

Note

niSwitch_Disconnect

not

niSwitch_Connect

niSwitch_DisconnectAll

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between CH1 and COM and the other between CH2 and
 COM:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch1 and com .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 ch1 and com .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch2 and com .

Parent topic:

NI PXIe-2748

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2748-front-panel.html language=enus -->
## TOPIC 00560: NI PXIe-2748 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2748-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2748-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXIe-2748 front panel.

### NI PXIe-2748 Front Panel

The following figure illustrates the NI PXIe-2748 front panel.

[IMAGE alt='image' src='GUID-B6375517-B3BE-4B98-B57D-E2F5A0F19BD1-a5.gif']

Parent topic:

NI PXIe-2748

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2748-hardware-diagram.html language=enus -->
## TOPIC 00561: NI PXIe-2748 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2748-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2748-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXIe-2748.

### NI PXIe-2748 Hardware Diagram

The following figure shows the hardware diagram for the NI PXIe-2748.

[IMAGE alt='image' src='GUID-02A6A016-EA93-4991-BAC1-109096143199-a5.gif']

Parent topic:

NI PXIe-2748

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2748.html language=enus -->
## TOPIC 00562: NI PXIe-2748

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2748.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2748.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2748 (NI 2748) is a 16×1 multiplexer switch module for the PXI Express bus that can carry 50 Ω RF signals up to 3 GHz. Operation Modes The following table lists the supported topology of the NI 2748 and possible operation modes. Topology Software Name Immediate Scanning 16×1 Multiplexer

### NI PXIe-2748

The NI PXIe-2748 (NI 2748) is a 16×1 multiplexer switch module for the PXI Express bus that
 can carry 50 Ω RF signals up to 3 GHz.

#### Operation Modes

The following table lists the supported topology of the NI 2748 and possible operation
 modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 16×1 Multiplexer | 2748/16x1 Mux (NISWITCH_TOPOLOGY_2748_16X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- RF Switching Considerations
- Topologies
- Operation Modes
- NI PXI-2547 8×1 Multiplexer (SP8T) Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2790-front-panel.html language=enus -->
## TOPIC 00563: NI PXIe-2790 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2790-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2790-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXIe-2790 front panel.

### NI PXIe-2790 Front Panel

The following figure illustrates the NI PXIe-2790 front panel.

[IMAGE alt='image' src='GUID-7B55E67B-6514-4304-839D-9411DA0E378F-a5.gif']

Parent topic:

NI PXIe-2790

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2790-hardware-diagram.html language=enus -->
## TOPIC 00564: NI PXIe-2790 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2790-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2790-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXIe-2790.

### NI PXIe-2790 Hardware Diagram

The following figure shows the hardware diagram for the NI PXIe-2790.

[IMAGE alt='image' src='GUID-1EFD351C-83E3-432D-AA55-1223320753E1-a5.gif']

Parent topic:

NI PXIe-2790

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2790-independent-topology.html language=enus -->
## TOPIC 00565: NI PXIe-2790 Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2790-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2790-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2790 in the independent topology. Making a Connection Call the niSwitch Connect Channels VI or the niSwitch_Connect function to connect channels in this topology. If applicable, you must call the niSwitch Disconnect Channels VI or the niSwitch_Disconnect f

### NI PXIe-2790 Independent Topology

The following figure represents the NI PXIe-2790 in the independent topology.

[IMAGE alt='image' src='GUID-038F15A3-5660-49EC-97F2-7029446FD7EF-a5.gif']

#### Making a Connection

Call the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function to connect channels in this topology. If applicable, you must call the
 niSwitch Disconnect
 Channels
 VI or the
 niSwitch_Disconnect
 function to disconnect an existing connection before you call the
 niSwitch Connect Channels VI or the niSwitch_Connect function.

The initially connected channels on the NI 2790 are sumAB to comA and sumAB to comB.
 To connect ch1A to comA, disconnect sumAB from comA and connect ch1A to comA. To
 connect ch1B to comB, disconnect sumAB from comB and connect ch1B to comB. Banks A
 and B operate independently.

Parent topic:

NI PXIe-2790

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2790-triggering.html language=enus -->
## TOPIC 00566: NI PXIe-2790 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2790-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2790-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXIe-2790. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger

### NI PXIe-2790 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXIe-2790.

| Trigger Input | Software | Hardware |
| --- | --- | --- |
| Immediate | Immediate(NISWITCH_VAL_IMMEDIATE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |
| Software Trigger | niSwitch Send Software Trigger VI or niSwitch_SendSoftwareTrigger function | N/A |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXIe-2790.

| Scan Advanced Output | Software | Hardware |
| --- | --- | --- |
| None | None(NISWITCH_VAL_NONE) | N/A |
| TTL0 | TTL0(NISWITCH_VAL_TTL0) | PXI trigger line 0 |
| TTL1 | TTL1(NISWITCH_VAL_TTL1) | PXI trigger line 1 |
| TTL2 | TTL2(NISWITCH_VAL_TTL2) | PXI trigger line 2 |
| TTL3 | TTL3(NISWITCH_VAL_TTL3) | PXI trigger line 3 |
| TTL4 | TTL4(NISWITCH_VAL_TTL4) | PXI trigger line 4 |
| TTL5 | TTL5(NISWITCH_VAL_TTL5) | PXI trigger line 5 |
| TTL6 | TTL6(NISWITCH_VAL_TTL6) | PXI trigger line 6 |
| TTL7 | TTL7(NISWITCH_VAL_TTL7) | PXI trigger line 7 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXIe-2790

<!--NI_TOPIC bundle=ni-switch path=ni-pxie-2790.html language=enus -->
## TOPIC 00567: NI PXIe-2790

- bundle_id: `ni-switch`
- source_path: `ni-pxie-2790.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxie-2790.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2790 is an RF power combiner switch module for the PXI Express platform that uses CMOS switches and handles RF signals up to 6 GHz. Operation Modes The following table lists the supported topology of the NI PXIe-2790 and possible operation modes. Topology Software Name Immediate Scanning

### NI PXIe-2790

The NI PXIe-2790 is an RF power combiner switch module for the PXI Express platform that
 uses CMOS switches and handles RF signals up to 6 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXIe-2790 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Independent | 2790/Independent(NISWITCH_TOPOLOGY_2790_INDEPENDENT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- RF Switching Considerations
- Topologies
- Operation Modes
- NI PXIe-2790 Independent Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-quad-pxie-2746-4-1-multiplexer-quad-sp4t-t.html language=enus -->
## TOPIC 00568: NI Quad PXIe-2746 4×1 Multiplexer (Quad SP4T) Topology

- bundle_id: `ni-switch`
- source_path: `ni-quad-pxie-2746-4-1-multiplexer-quad-sp4t-t.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-quad-pxie-2746-4-1-multiplexer-quad-sp4t-t.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXIe-2746 (NI 2746) in the 4×1 multiplexer topology. Making a Connection Call the niSwitch Connect Channels VI or the niSwitch_Connect function to connect channels in this topology. If applicable, you must call the niSwitch Disconnect Channels VI or the niSwitc

### NI Quad PXIe-2746 4×1 Multiplexer (Quad SP4T) Topology

The following figure represents the NI PXIe-2746 (NI 2746) in the 4×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-4FFECC7F-7774-4B76-A1AB-6B49C15FA180-a5.gif']

#### Making a Connection

Call the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function to connect channels in this topology. If applicable, you must call the
 niSwitch Disconnect
 Channels
 VI or the
 niSwitch_Disconnect
 function to disconnect an existing connection before you call the
 niSwitch Connect Channels VI or the niSwitch_Connect function.

Note

niSwitch_Disconnect

not

niSwitch_Connect

niSwitch_DisconnectAll

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between CH1 and COM and the other between CH2 and
 COM:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch1 and com .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 ch1 and com .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch2 and com .

Parent topic:

NI PXI-2746

<!--NI_TOPIC bundle=ni-switch path=ni-switch-block-device-basics.html language=enus -->
## TOPIC 00569: NI SwitchBlock Device Basics

- bundle_id: `ni-switch`
- source_path: `ni-switch-block-device-basics.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switch-block-device-basics.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: What do you want to do? Run the NI-DAQmx Test Panels Use Test Panels to interactively test the functionality of your NI SwitchBlock device. To run the test panels, right-click the device name in the configuration tree, and select Test Panels. Because the NI SwitchBlock carrier is not a switch device

### NI SwitchBlock Device Basics

What do you want to do?

#### Run the NI-DAQmx Test Panels

Use Test Panels to interactively test the functionality of your NI SwitchBlock
 device. To run the test panels, right-click the device name in the configuration
 tree, and select Test Panels. Because the NI SwitchBlock
 carrier is not a switch device, there is no test panel for the carrier.

#### Insert Simulated Cards

To insert simulated cards into a simulated NI SwitchBlock carrier, right-click the
 simulated carrier in the configuration tree and select Insert or Remove
 Simulated Cards. Refer to the NI SwitchBlock Configuration
 Panel
 Help
 for more information about inserting simulated cards into a simulated NI SwitchBlock
 carrier.

#### Configure the NI SwitchBlock

To designate which cards compose devices in an NI SwitchBlock system, right-click the
 NI SwitchBlock carrier in the configuration tree and select
 Configure. Refer to the NI SwitchBlock
 Configuration Panel
 Help
 for more information about configuring an NI SwitchBlock system.

#### Test Relays

To access an integrated relay test and relay counts for cards in an NI SwitchBlock
 carrier, right-click the NI SwitchBlock carrier in the configuration tree and select
 NI Switch Health Center. Refer to the NI Switch
 Health Center
 Help
 for more information about the NI Switch Health Center.

#### Remove the Device or Carrier

Refer to the NI SwitchBlock Configuration Panel
 Help
 for information about removing a device or carrier from the configuration tree.

Parent topic:

NI SwitchBlock Configuration Panel Help

<!--NI_TOPIC bundle=ni-switch path=ni-switch-examples.html language=enus -->
## TOPIC 00570: NI-SWITCH Examples

- bundle_id: `ni-switch`
- source_path: `ni-switch-examples.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switch-examples.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-SWITCH includes several example applications that demonstrate the functionality of your device and can serve as interactive tools, programming models, and building blocks for your own applications. NI Example Finder The NI Example Finder is a utility that organizes examples into categories and al

### NI-SWITCH Examples

NI-SWITCH includes several example applications that demonstrate the functionality of
 your device and can serve as interactive tools, programming models, and building blocks
 for your own applications.

#### NI Example Finder

The NI Example Finder is a utility that organizes examples into categories and allows
 you to browse and search installed examples. For example, search for
 "SWITCH" to locate all NI-SWITCH examples. You can see
 descriptions and compatible hardware models for each example or see all the examples
 compatible with one particular hardware model.

To locate examples using the NI
 Example Finder within LabVIEW, select Help»Find
 Examples and navigate to Hardware Input and
 Output»Modular
 Instruments»NI-SWITCH.

#### Example Locations

| ADE | Example Locations |  |
| --- | --- | --- |
| LabVIEW | Within LabVIEW, select Help»Find Examples and navigate to Hardware Input and Output»Modular Instruments. |  |
| LabWindows/CVI | C:\\Users\\Public\\Documents\\National Instruments\\CVI\\samples\\niSwitch |  |
| C/C++ | Windows — Users\\Public\\Documents\\National Instruments\\NIDocDir\\NI-SWITCH\\examples Linux — usr/share/niswitch-devel/examples |  |
| .NET | 4.0 | C:\\Users\\Public\\Documents\\National Instruments\\NI-SWITCH\\Examples\\DotNET 4.0 |
| 4.5 | C:\\Users\\Public\\Documents\\National Instruments\\NI-SWITCH\\Examples\\DotNET 4.5 |  |
| Python | Refer to Python NI-SWITCH Examples. |  |

Parent topic:

Getting Started

<!--NI_TOPIC bundle=ni-switch path=ni-switch-health-center-help.html language=enus -->
## TOPIC 00571: NI Switch Health Center Help

- bundle_id: `ni-switch`
- source_path: `ni-switch-health-center-help.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switch-health-center-help.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This help file contains information about using the NI Switch Health Center to test relays on NI-SWITCH relay cards. The NI Switch Health Center executes a hardware-integrated relay test and provides access to the relay count tracking data stored on NI-SWITCH relay cards. Results from the relay test

### NI Switch Health Center Help

This help file contains information about using the NI Switch Health Center to test
 relays on NI-SWITCH relay cards.

The NI Switch Health Center executes a hardware-integrated relay test and provides access
 to the relay count tracking data stored on NI-SWITCH relay cards. Results from the relay
 test are graphically displayed on a relay card diagram, making it easy to locate relays
 that need to be replaced or relays are near end-of-life.

- [About the NI Switch Health Center](about-the-ni-switch-health-center.html)
- [Accessing the NI Switch Health Center](accessing-the-ni-switch-health-center.html)
- [Testing Relays with the NI Switch Health Center](testing-relays-ni-switch-health-center.html)
- [Generating Reports with the NI Switch Health Center](generating-reports-ni-switch-health-center.html)
- [Switch Relay Replacement](switch-relay-replacement.html)
- [Switch Relay Maintenance with the NI Switch Health Center](switch-relay-maintenance-ni-switch-health-center.html)
- [Relay Lifetime](relay-lifetime.html)
- [Error Cases in the NI Switch Health Center](error-cases-in-the-ni-switch-health-center.html)

<!--NI_TOPIC bundle=ni-switch path=ni-switch-programming-examples.html language=enus -->
## TOPIC 00572: NI-SWITCH Programming Examples

- bundle_id: `ni-switch`
- source_path: `ni-switch-programming-examples.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switch-programming-examples.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-SWITCH includes a collection of programming examples that demonstrate switch functionality. NI-SWITCH programming examples are instructional tools that you can use as stand-alone programs or integrate into your application. Whether you are developing a new application or modifying an existing app

### NI-SWITCH Programming Examples

NI-SWITCH includes a collection of programming examples that demonstrate switch
 functionality. NI-SWITCH programming examples are instructional tools that you can use
 as stand-alone programs or integrate into your application. Whether you are developing a
 new application or modifying an existing application, the NI-SWITCH programming examples
 can facilitate your application development.

Use the following partial list to identify NI-SWITCH programming example(s) to aid in
 your application development:

- niSwitch Making Connections on a Switch—Demonstrates how to connect channels.
- niSwitch Software Scanning—Demonstrates how to scan a series of channels on a switch
 using software scanning.
- niSwitch DMM Switch Synchronous Scanning—Demonstrates how to scan a series of
 channels on a switch module and take measurements with an NI digital multimeter
 using synchronous scanning. NI-DMM 2.0 or later is required.
- niSwitch DMM Switch Handshaking—Demonstrates how to scan a series of channels on a
 switch module and take measurements with an NI digital multimeter using handshaking.
 NI-DMM 2.0 or later is required.
- niSwitch Controlling an Individual Relay—Demonstrates how to control an individual
 relay on a switch module.

#### Accessing the Programming Examples

Examples are available for the following ADEs:

- LabVIEW
- LabWindows™/CVI™
- Visual C/C++
- Visual Basic

For example locations and supported ADE versions, refer to the NI-SWITCH
 Readme File.

NI-DAQmx includes programming examples for switch functionality, such as multiple
 module scanning, that is supported in NI-DAQmx. Access the NI-DAQmx programming
 examples for switches at
 <LabVIEW>\examples\DAQmx\Switches.

Parent topic:

Programming with NI-SWITCH

<!--NI_TOPIC bundle=ni-switch path=ni-switch-switches.html language=enus -->
## TOPIC 00573: NI-SWITCH Switches

- bundle_id: `ni-switch`
- source_path: `ni-switch-switches.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switch-switches.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `reference`

### NI-SWITCH Switches

- [NI PXI-2501/2503](ni-pxi-2501-2503.html)
- [NI PXI-2510](ni-pxi-2510.html)
- [NI PXI/PXIe-2512](ni-pxi-pxie-2512.html)
- [NI PXI/PXIe-2514](ni-pxi-pxie-2514.html)
- [NI PXI/PXIe-2515](ni-pxi-pxie-2515.html)
- [NI PXI-2520](ni-pxi-2520.html)
- [NI PXI-2521](ni-pxi-2521.html)
- [NI PXI-2522](ni-pxi-2522.html)
- [NI PXI-2523](ni-pxi-2523.html)
- [NI PXIe-2524](ni-pxie-2524.html)
- [NI PXIe-2525](ni-pxie-2525.html)
- [NI PXIe-2526](ni-pxie-2526.html)
- [NI PXI/PXIe-2527](ni-pxi-pxie-2527.html)
- [NI PXI/PXIe-2529](ni-pxi-pxie-2529.html)
- [NI PXI-2530/2530B](ni-pxi-2530-2530b.html)
- [NI PXI/PXIe-2531](ni-pxi-pxie-2531.html)
- [NI PXI/PXIe-2532/2532B](ni-pxi-pxie-2532-2532b.html)
- [NI PXI-2533](ni-pxi-2533.html)
- [NI PXI-2534](ni-pxi-2534.html)
- [NI PXI-2535](ni-pxi-2535.html)
- [NI PXI-2536](ni-pxi-2536.html)
- [NI PXI/PXIe-2540](ni-pxi-pxie-2540.html)
- [NI PXI/PXIe-2541](ni-pxi-pxie-2541.html)
- [NI PXI/PXIe-2542](ni-pxi-pxie-2542.html)
- [NI PXI/PXIe-2543](ni-pxi-pxie-2543.html)
- [NI PXI/PXIe-2544](ni-pxi-pxie-2544.html)
- [NI PXI-2545](ni-pxi-2545.html)
- [NI PXI-2546](ni-pxi-2546.html)
- [NI PXI-2547](ni-pxi-2547.html)
- [NI PXI-2548](ni-pxi-2548.html)
- [NI PXI-2549](ni-pxi-2549.html)
- [NI PXI-2554](ni-pxi-2554.html)
- [NI PXI-2555](ni-pxi-2555.html)
- [NI PXI-2556](ni-pxi-2556.html)
- [NI PXI-2557](ni-pxi-2557.html)
- [NI PXI-2558](ni-pxi-2558.html)
- [NI PXI-2559](ni-pxi-2559.html)
- [NI PXI-2564](ni-pxi-2564.html)
- [NI PXI-2565](ni-pxi-2565.html)
- [NI PXI-2566](ni-pxi-2566.html)
- [NI PXI-2567](ni-pxi-2567.html)
- [NI PXI-2568](ni-pxi-2568.html)
- [NI PXI/PXIe-2569](ni-pxi-pxie-2569.html)
- [NI PXI-2570](ni-pxi-2570.html)
- [NI PXI-2571](ni-pxi-2571.html)
- [NI PXI/PXIe-2575](ni-pxi-pxie-2575.html)
- [NI PXI-2576](ni-pxi-2576.html)
- [NI PXI-2584](ni-pxi-2584.html)
- [NI PXI-2585](ni-pxi-2585.html)
- [NI PXI-2586](ni-pxi-2586.html)
- [NI PXI-2590](ni-pxi-2590.html)
- [NI PXI-2591](ni-pxi-2591.html)
- [NI PXI/PXIe-2593](ni-pxi-pxie-2593.html)
- [NI PXI-2594/2595](ni-pxi-2594-2595.html)
- [NI PXI-2596](ni-pxi-2596.html)
- [NI PXI-2597](ni-pxi-2597.html)
- [NI PXI-2598](ni-pxi-2598.html)
- [NI PXI-2599](ni-pxi-2599.html)
- [NI PXI-2720](ni-pxi-2720.html)
- [NI PXI-2722](ni-pxi-2722.html)
- [NI PXIe-2725](ni-pxie-2725.html)
- [NI PXIe-2727](ni-pxie-2727.html)
- [NI PXIe-2737](ni-pxie-2737.html)
- [NI PXIe-2738](ni-pxie-2738.html)
- [NI PXIe-2739](ni-pxie-2739.html)
- [NI PXI-2746](ni-pxi-2746.html)
- [NI PXIe-2747](ni-pxie-2747.html)
- [NI PXIe-2748](ni-pxie-2748.html)
- [NI PXIe-2790](ni-pxie-2790.html)
- [NI PXI-2796](ni-pxi-2796.html)
- [NI PXI-2797](ni-pxi-2797.html)
- [NI PXI-2798](ni-pxi-2798.html)
- [NI PXI-2799](ni-pxi-2799.html)
- [NI 2810](ni-2810.html)
- [NI 2811](ni-2811.html)
- [NI 2812](ni-2812.html)
- [NI 2813](ni-2813.html)
- [NI 2814](ni-2814.html)
- [NI 2815](ni-2815.html)
- [NI 2816](ni-2816.html)
- [NI 2817](ni-2817.html)
- [NI 2833](ni-2833.html)
- [NI 2834](ni-2834.html)
- [NI 2865A](ni-2865a.html)

<!--NI_TOPIC bundle=ni-switch path=ni-switchblock-basics.html language=enus -->
## TOPIC 00574: NI SwitchBlock Basics

- bundle_id: `ni-switch`
- source_path: `ni-switchblock-basics.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switchblock-basics.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this book for basic information about the NI SwitchBlock.

### NI SwitchBlock Basics

Expand this book for basic information about the NI SwitchBlock.

Parent topic:

NI SwitchBlock Switching Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-switchblock-cards-and-devices.html language=enus -->
## TOPIC 00575: NI SwitchBlock Cards and Devices

- bundle_id: `ni-switch`
- source_path: `ni-switchblock-cards-and-devices.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switchblock-cards-and-devices.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI SwitchBlock carriers can be configured in the NI SwitchBlock Configuration Panel in MAX to create single-card or multicard NI SwitchBlock devices. NI SwitchBlock Cards NI SwitchBlock cards operate within an NI SwitchBlock carrier, occupying less space and offering greater switching density than P

### NI SwitchBlock Cards and Devices

NI SwitchBlock carriers can be configured in the NI SwitchBlock Configuration Panel in
 MAX to create single-card or multicard NI SwitchBlock devices.

#### NI SwitchBlock Cards

NI SwitchBlock cards operate within an NI SwitchBlock carrier, occupying less space
 and offering greater switching density than PXI switch modules. The following figure
 represents an NI SwitchBlock card and carrier.

[IMAGE alt='image' src='GUID-A5FB3F2E-BDC6-4A6D-A736-159CEC93940C-a5.gif']

| 1 | NI SwitchBlock Card |
| --- | --- |
| 2 | NI PXI-2800 Carrier |

Each card is available in two types, type A and type B, which vary only in which
 signals they route to the front panel connector. Refer to the NI SwitchBlock Device
 Reference for information about the differences between type A and type B cards.

Refer to the device book for your card for card-specific information.

#### NI SwitchBlock Devices

An NI SwitchBlock device is a software construct that represents one or more cards
 configured in software to function as a device. Refer to Configuring the
 NI SwitchBlock in
 MAX
 to designate which cards compose the devices in your NI SwitchBlock. The
 NI SwitchBlock Device Reference includes guidelines for combining cards into
 devices.

Note

#### Maximizing AC Performance of the Cards that Compose Your NI SwitchBlock
 Devices

To maximize the AC performance of the cards that compose your NI SwitchBlock devices,
 NI recommends the following practices, when possible:

- Keep point-to-point signals on the same card. Routing signals across the analog
 bus backplane increases the number of stubs attached to the
 signal path, which can degrade high-frequency signals.
- Reduce the number of stubs attached to the signal path by using only type B
 cards. While type A cards are required to directly access the analog bus
 channels, the cabling may create additional stubs and capacitively load the
 analog bus, which degrades high frequency performance.
- Do not fan out AC signals. Fanning out AC signals reduces bandwidth and
 increases crosstalk.

Parent topic:

NI SwitchBlock Basics

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-switchblock-configuration-panel-help.html language=enus -->
## TOPIC 00576: NI SwitchBlock Configuration Panel Help

- bundle_id: `ni-switch`
- source_path: `ni-switchblock-configuration-panel-help.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switchblock-configuration-panel-help.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This help file contains information about using the NI SwitchBlock Configuration Panel in Measurement & Automation Explorer (MAX) to configure the NI SwitchBlock. This help file also contains information about simulating the NI SwitchBlock in MAX and guidelines for combining NI SwitchBlock cards int

### NI SwitchBlock Configuration Panel Help

This help file contains information about using the NI SwitchBlock Configuration Panel in
 Measurement & Automation Explorer (MAX) to configure the NI SwitchBlock. This help
 file also contains information about simulating the NI SwitchBlock in MAX and guidelines
 for combining NI SwitchBlock cards into devices.

For information about programming the NI SwitchBlock, refer to the NI Switches
 Help.

Parent topic:

Getting Started

<!--NI_TOPIC bundle=ni-switch path=ni-switchblock-device-reference.html language=enus -->
## TOPIC 00577: NI SwitchBlock Device Reference

- bundle_id: `ni-switch`
- source_path: `ni-switchblock-device-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switchblock-device-reference.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: An NI SwitchBlock device represents one or more NI SwitchBlock cards that are configured in software to function as a device. All NI SwitchBlock devices are programmed in the same manner regardless of the number of NI SwitchBlock cards that compose them. Refer to the following sections for guideli

### NI SwitchBlock Device Reference

Note

Refer to the following sections for guidelines and requirements when configuring your
 cards to function as devices.

- NI SwitchBlock Card Types
- Card Combination Use Cases
- Requirements for Multicard Devices
- Topologies of Multicard Devices
- Channel Naming for NI SwitchBlock Devices
- Relay Naming for NI SwitchBlock Devices

#### NI SwitchBlock Card Types

Each card is available in two types, type A and type B, which vary only in the
 signals they route to the front panel connector. The letter at the end of the card
 model indicates the type of card. For example, NI 2810A indicates a type A card, and
 NI 2810B indicates a type B card. Refer to the following figure and table for
 differences between card types.

The following image represents a 1-wire device.

[IMAGE alt='image' src='GUID-CB4F6643-F95B-415E-94FD-3AF41F2784E1-a5.gif']

The following image represents a 2-wire device.

[IMAGE alt='image' src='GUID-DD4F4131-50EF-4D51-9464-543B60AC3479-a5.gif']

| Card Type | Characteristics |
| --- | --- |
| A | Front connector pins connect to all analog bus channels and columns of the matrix. Type A cards directly route analog bus lines on the NI SwitchBlock carrier to the front connector. |
| B | Front connector pins connect only to the columns of the matrix. |

#### Card Combination Use Cases

Create a multicard device according to the requirements for multicard devices when a
 single-card device cannot support the size of your application. Refer to the
 following use cases to decide how to compose your multicard device.

| Card Combination | Use Cases |
| --- | --- |
| One Type A Card + One or More Type B Cards | Recommended when an application requires direct access to the analog bus channels. Typical usage of this card combination involves connecting analog bus channels to columns. |
| All Type B Cards | Recommended when connecting only to columns. Analog bus channels may still be used for signal routing as needed, but they will not be routed to the front panel I/O connector. |

Note

#### Requirements for Multicard Devices

- While different card models may be installed and operated in the same
 NI SwitchBlock carrier, a device may only be composed of cards of the same
 model. For example, you can combine two NI 2811A/B cards into one device, but if
 you install an NI 2811A/B and an NI 2816A/B, you will have to operate them as
 separate devices.
- All cards in a multicard device must be installed in the same NI SwitchBlock
 carrier. If your switching system spans multiple carriers, NI recommends using
 NI Switch Executive to manage all cards as a single virtual device. Refer to the
 NI Switch Executive Help for information about creating
 virtual devices.
- While multicard devices may be composed of any combination of type A and type B
 cards, NI recommends reducing the total number of paths you expose a signal to
 by using no more than one type A card in an NI SwitchBlock system. Refer to the
 Card Combination Use Cases section of this help topic for more information about
 recommended card combination options.

Refer to the device book for your card in the NI Switches Help for
 information about card combinations for specific topologies.

#### Topologies of Multicard Devices

The topology of a multicard device is the merger of the topologies of each individual
 card. The number of columns in a multicard device can be determined by multiplying
 the number of cards combined by the number of columns on one card.

For example, the topology of a single NI 2810A/B card is a 1-Wire 4×43 matrix. If you
 create a multicard device using three NI 2810A/B cards, 43 columns multiplied by
 three cards would total 129 columns in the multicard device. The resulting topology
 for the multicard device would be a 1-Wire 4×129 matrix. Each card maintains its own
 row channels, and the analog bus channels are used to connect channels in different
 cards.

#### Channel Naming for NI SwitchBlock Devices

Refer to the following images and instructions to determine the row, column, and
 analog bus channel names for your NI SwitchBlock device.

[IMAGE alt='image' src='GUID-782A9404-6081-41FC-84B6-FA934E2000F2-a5.gif']

#### Row Channel Names

Row channel names are composed of the card number followed by the row number, written
 in the format, cardXrY, where
 X indicates the card number and Y indicates the row number. Card numbers correspond
 to the position of the card in relation to the other cards composing the device,
 starting with 1 for the leftmost card in the device.

Note

card1

#### Column Channel Names

Column channel names are written in the format
 cZ, where Z indicates the column number. In
 multicard devices, column numbers for each card resume where the columns for the
 previous card in the device ended, with column numbers for the leftmost card
 starting at zero. In separate SwitchBlock devices, column numbers start at c0 for
 the first relay card.

#### Analog Bus Channel Names

Analog bus channels connect the rows to the carrier analog bus. Analog bus channel
 names are written in the format abX, where
 X indicates the analog bus channel
 number and corresponds to the adjacent row channel. All relay cards within the same
 carrier, or within multiple carriers connected using an expansion bridge, connect to
 the same analog bus through their analog bus channels regardless of which NI
 SwitchBlock device they are in.

#### Relay Naming for NI SwitchBlock Devices

Refer to the following instructions to determine the relay names for your
 NI SwitchBlock device.

#### Matrix Relays

Matrix relay names for NI SwitchBlock 1-wire cards follow the format of
 kcardXrYcZ,
 where cardXrY indicates the
 name of the row channel that connects at that relay and
 cZ indicates the name of the column
 channel that connects at that relay. For example, a relay that connects
 card1r5 and c18 would be named
 kcard1r5c18. A relay that connects card2r2 and
 c44 would be named kcard2r2c44.

Matrix relay names for NI SwitchBlock 2-wire cards with SPST relays follow the
 formats of
 kcardXrYcZw0
 and
 kcardXrYcZw1
 for each wire on the channel.

#### Analog Bus Relays

Analog bus relay names for NI SwitchBlock 1-wire cards follow the format of
 kcardXabY, where
 cardX indicates the card number and
 abY indicates name of the analog bus
 channel that the relay connects to a corresponding row. For example, the relay that
 connects ab2 to card1r2 would be named
 kcard1ab2.

Analog bus relay names for NI SwitchBlock 2-wire cards with SPST relays follow the
 formats of kcardXabYw0 and
 kcardXabYw1 for each
 wire.

Note

kcard1ab0

kcard1ab0w0

kcard1ab0w1

Parent topic:

Setting Up and Configuring the NI SwitchBlock

<!--NI_TOPIC bundle=ni-switch path=ni-switchblock-integrated-relay-test.html language=enus -->
## TOPIC 00578: NI SwitchBlock Integrated Relay Test

- bundle_id: `ni-switch`
- source_path: `ni-switchblock-integrated-relay-test.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switchblock-integrated-relay-test.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI SwitchBlock has an integrated relay test feature that verifies the proper operation of each individual relay. When you disable the safety interlock on your NI SwitchBlock, certain rows on each card are connected together through resistors to enable integrated relay test. During an integrated

### NI SwitchBlock Integrated Relay Test

The NI SwitchBlock has an integrated relay test feature that verifies the proper
 operation of each individual relay. When you disable the safety interlock on your
 NI SwitchBlock, certain rows on each card are connected together through resistors to
 enable integrated relay test. During an integrated relay test, different combinations of
 relay connections are tested to determine the condition of each relay. Integrated relay
 test functionality enables you to increase the long-term reliability of your test system
 and reduce debug time.

Start

All
 Programs

National
 Instruments

NI-SWITCH

NI Switch Health
 Center

Note

Parent topic:

NI SwitchBlock Maintenance

<!--NI_TOPIC bundle=ni-switch path=ni-switchblock-maintenance.html language=enus -->
## TOPIC 00579: NI SwitchBlock Maintenance

- bundle_id: `ni-switch`
- source_path: `ni-switchblock-maintenance.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switchblock-maintenance.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this book for information about maintaining the NI SwitchBlock.

### NI SwitchBlock Maintenance

Expand this book for information about maintaining the NI SwitchBlock.

Parent topic:

NI SwitchBlock Switching Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-switchblock-overview.html language=enus -->
## TOPIC 00580: NI SwitchBlock Overview

- bundle_id: `ni-switch`
- source_path: `ni-switchblock-overview.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switchblock-overview.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI SwitchBlock is a switch platform designed for large matrix test systems. It includes internal column expansion features that can create matrices with more than 8,800 crosspoints in a single PXI chassis. To improve long-term system reliability, the NI SwitchBlock ships with the new NI Switch H

### NI SwitchBlock Overview

The NI SwitchBlock is a switch platform designed for large matrix test systems. It
 includes internal column expansion features that can create matrices with more than
 8,800 crosspoints in a single PXI chassis. To improve long-term system reliability, the
 NI SwitchBlock ships with the new NI Switch Health Center, which contains an integrated
 relay test, relay count tracking, and report generation tool.

Although National Instruments recommends using NI Switch Executive to program the NI
 SwitchBlock, you can program the NI SwitchBlock using the NI-SWITCH and NI-DAQmx driver
 APIs. NI Switch Executive intelligent route management software enables large matrix
 application programming and includes a configuration wizard that accelerates development
 with the NI SwitchBlock. This help topic explains how to program the NI SwitchBlock with
 the NI-SWITCH and NI-DAQmx driver APIs.

#### Important Information about Getting Started with NI SwitchBlock

For more information about getting started with the NI SwitchBlock, visit
 ni.com/info and enter the Info Code exbpzd.

For more information about the NI SwitchBlock hardware architecture, visit
 ni.com/info and enter the Info Code exmsq9.

For more information about programming the NI SwitchBlock, visit
 ni.com/info and enter the Info Code exy2pt.

For more information about connecting to the NI SwitchBlock, visit
 ni.com/info and enter the Info Code ex88cp.

To watch the "Programming the NI SwitchBlock" webcast, visit
 ni.com/info and enter the Info Code exee6e.

Parent topic:

Programming the NI SwitchBlock in NI-SWITCH and NI-DAQmx

<!--NI_TOPIC bundle=ni-switch path=ni-switchblock-power-limits.html language=enus -->
## TOPIC 00581: NI SwitchBlock Power Limits

- bundle_id: `ni-switch`
- source_path: `ni-switchblock-power-limits.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switchblock-power-limits.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI SwitchBlock carriers have a power consumption limit and a power dissipation limit (power limits) based on the available cooling capabilities of and power available from the PXI/PXI Express chassis in which the carrier is installed. Each slot in a carrier has power limits based on the characterist

### NI SwitchBlock Power Limits

NI SwitchBlock carriers have a power consumption limit and a
 power dissipation limit (power limits) based
 on the available cooling capabilities of and power available from the PXI/PXI Express
 chassis in which the carrier is installed. Each slot in a carrier has power limits based
 on the characteristics of the card installed in that slot. The carrier's power limit is
 based on the combination of cards installed in the carrier. These power limits determine
 the maximum number of relays that can be driven simultaneously while dissipating power
 from user-supplied signals. For information about how to determine carrier power limits,
 visit ni.com/info and enter the info code, sbpwrlim.

To prevent a blown fuse, the switch driver automatically checks before each operation
 whether the power required for that operation exceeds the carrier or slot power limits.
 If your desired operation exceeds the carrier or slot power limits, the switch driver
 will return an error. You can clear the error using the niSwitch
 Reset VI or
 niSwitch_reset
 function to reset each device, or using the niSwitch Disconnect All
 Channels
 VI or the
 niSwitch_DisconnectAll
 function to disconnect all channels on each device.

After clearing the error, examine your application to find ways to use less power by
 operating fewer relays simultaneously. The switch driver tracks power consumption, but
 you should also track your power dissipation because it varies depending on your
 application and system. For more information about tracking power consumption in your
 system, visit ni.com/info and enter the info code,
 sbpwrlim.

Parent topic:

NI SwitchBlock Programming Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-switchblock-programming-considerations.html language=enus -->
## TOPIC 00582: NI SwitchBlock Programming Considerations

- bundle_id: `ni-switch`
- source_path: `ni-switchblock-programming-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switchblock-programming-considerations.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this book for information about programming the NI SwitchBlock.

### NI SwitchBlock Programming Considerations

Expand this book for information about programming the NI SwitchBlock.

Parent topic:

NI SwitchBlock Switching Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-switchblock-safety-interlock.html language=enus -->
## TOPIC 00583: NI SwitchBlock Safety Interlock

- bundle_id: `ni-switch`
- source_path: `ni-switchblock-safety-interlock.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switchblock-safety-interlock.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI SwitchBlock cards require the use of a safety interlock resistor, without which you cannot route signals to or from the analog bus. Front Panel Cable Detection To prevent the front connectors of NI SwitchBlock cards from exposing high-voltage signals when disconnected from NI SwitchBlock accessor

### NI SwitchBlock Safety Interlock

NI SwitchBlock cards require the use of a safety interlock resistor, without which you
 cannot route signals to or from the analog bus.

#### Front Panel Cable Detection

To prevent the front connectors of NI SwitchBlock cards from exposing high-voltage
 signals when disconnected from NI SwitchBlock accessories, the cards detect whether
 a cable or other accessory is attached to the front connector. NI accessories for
 the NI SwitchBlock connect pin 96 to pin 48 through a 500 Ω resistor (500 Ω ±20%,
 1/10 W minimum) built into the accessory. If the resistor does not connect these two
 pins, no matrix lines can connect to the analog bus.

#### Creating Custom Test Fixtures

If you create your own cable or custom test fixture for your NI SwitchBlock,
 incorporate the interlock resistor into your design to ensure that your signal lines
 are touch-safe when the test fixture or cable is removed. Additionally,
 incorporating the safety interlock resistor allows the operation of an integrated
 relay test when your fixture is disconnected.

Parent topic:

NI SwitchBlock Basics

<!--NI_TOPIC bundle=ni-switch path=ni-switchblock-switching-considerations.html language=enus -->
## TOPIC 00584: NI SwitchBlock Switching Considerations

- bundle_id: `ni-switch`
- source_path: `ni-switchblock-switching-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switchblock-switching-considerations.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI SwitchBlock is a high-density, customizable, and expandable system that can operate within a PXI/PXI Express chassis and is composed of an NI SwitchBlock carrier that holds interconnectable NI SwitchBlock cards. Multiple cards can be combined in software to operate as one device, enabling cus

### NI SwitchBlock Switching Considerations

The NI SwitchBlock is a high-density, customizable, and expandable system that can
 operate within a PXI/PXI Express chassis and is composed of an NI SwitchBlock carrier
 that holds interconnectable NI SwitchBlock cards. Multiple cards can be combined in
 software to operate as one device, enabling customization of device topologies to fit
 testing needs.

Because six NI SwitchBlock cards can fit in the space occupied by four PXI modules, the
 NI SwitchBlock enables greater switching density per PXI slot than PXI switch modules.
 The integrated analog bus backplane enables clean routing of signals between the cards
 in a carrier. Installation of the NI 2806 expansion bridge enables connection of the
 analog bus between multiple carriers.

#### NI SwitchBlock Basics

- NI PXI-2800 Carrier for the NI SwitchBlock
- NI SwitchBlock Cards and Devices
- Safety Interlock

#### Setting Up and Configuring the NI SwitchBlock

- Installing the NI SwitchBlock
- Expanding Multiple NI SwitchBlock Carriers
- Simulating the NI SwitchBlock in
 MAX
- Configuring the NI SwitchBlock in
 MAX
- Removing an NI SwitchBlock Carrier or Device in
 MAX
- NI SwitchBlock Device Reference

#### NI SwitchBlock Programming Considerations

- Initializing with Topology for NI SwitchBlock Devices
- Using the Analog Bus on an NI SwitchBlock Carrier
- Power Limits

#### NI SwitchBlock Maintenance

- Replacing a Fuse on the NI SwitchBlock Carrier
- Integrated Relay Test

#### Programming the NI SwitchBlock in NI-SWITCH and NI-DAQmx

- NI SwitchBlock Overview
- The NI SwitchBlock Carrier and the Analog Bus
- System Configuration Options for the NI SwitchBlock
- Routing Signals Within One NI SwitchBlock Device
- Routing Signals Between Multiple NI SwitchBlock Devices

Parent topic:

Fundamentals

Related concepts:

- NI SwitchBlock Device Reference

<!--NI_TOPIC bundle=ni-switch path=ni-switchblock-troubleshooting.html language=enus -->
## TOPIC 00585: NI SwitchBlock Troubleshooting

- bundle_id: `ni-switch`
- source_path: `ni-switchblock-troubleshooting.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-switchblock-troubleshooting.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic describes common problems you may encounter with the NI SwitchBlock and suggests solutions or workarounds. Relays do not seem to be switching signals. Ensure that your signals are properly connected to the front panel of the module and that your connectivity solution includes the safety i

### NI SwitchBlock Troubleshooting

This topic describes common problems you may encounter with the NI SwitchBlock and
 suggests solutions or workarounds.

#### Relays do not seem to be switching signals.

- Ensure that your signals are properly connected to the front panel of the module
 and that your connectivity solution includes the safety interlock resistor.
- You may have a bad relay. Consider performing an integrated relay test, routing
 through a different relay path, or troubleshooting your relay connection with a
 DMM or other measurement instrument.
- You may have blown the fuse that provides power to the cards. Refer to Replacing
 a Fuse on the NI SwitchBlock Carrier to determine whether the fuse in your
 carrier has blown. If necessary, replace the fuse.

#### I am issuing commands to operate relays, but I do not see my signals being routed
 as I expect.

Refer to the considerations in the Relays do not seem to be switching
 signals section.

Parent topic:

NI SwitchBlock Switching Considerations

<!--NI_TOPIC bundle=ni-switch path=operation-modes.html language=enus -->
## TOPIC 00586: Operation Modes

- bundle_id: `ni-switch`
- source_path: `operation-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/operation-modes.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-SWITCH offers two operation modes for programming National Instruments switches: immediate operations and scanning. During scanning, each operation in the scan list occurs after an event. Immediate operations occur instantly or as fast as the relay or relays can actuate. Immediate Operations Duri

### Operation Modes

NI-SWITCH offers two operation modes for programming National Instruments switches:
 immediate operations and scanning. During scanning, each operation in the scan list
 occurs after an event. Immediate operations occur instantly or as fast as the relay or
 relays can actuate.

#### Immediate Operations

During immediate operations, relays are actuated after each VI or function call
 rather than waiting for a trigger.

#### Scanning

Scanning is typically used when timing of connections must be synchronized with an
 event from another device, such as a measurement device (hardware-timed scanning),
 or must be timed by software (software-timed scanning).

Connection operations are entered in a scan list that is downloaded to the memory of
 the switch module. The first entry in the scan list is executed when the scan is
 initiated. The trigger settings determine how the switch advances through subsequent
 entries in the list. The scan list can be executed once or repeatedly.

There are three trigger schemes for scanning: software trigger scanning for
 software-timed scanning, synchronous scanning for hardware-timed scanning, and
 handshaking for hardware-timed scanning.

Note

Parent topic:

Programming Flow

Related concepts:

- Immediate Operations
- Scan Lists
- Writing a Software Trigger Scanning Program
- Synchronous Scanning
- Handshaking

<!--NI_TOPIC bundle=ni-switch path=path-resistance.html language=enus -->
## TOPIC 00587: Path Resistance

- bundle_id: `ni-switch`
- source_path: `path-resistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/path-resistance.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Path resistance is the resistance of a complete signal path from source to destination terminals on a switch module. The total resistance includes the resistance of PCB traces, relays, and connectors. Trace and connector resistance is generally stable, but relay contact resistance increases with use

### Path Resistance

Path resistance is the resistance of a complete signal path from source to destination
 terminals on a switch module. The total resistance includes the resistance of PCB
 traces, relays, and connectors. Trace and connector resistance is generally stable, but
 relay contact resistance increases with use.

The following figure illustrates the typical path resistance of a switch module with a
 mechanical life of 50 million cycles.

[IMAGE alt='image' src='GUID-AE64F77F-5212-4F2B-AC32-93DCFF9D74C7-a5.gif']

Parent topic:

General Switching Considerations

Related concepts:

- Contact Resistance
- Relay Life

<!--NI_TOPIC bundle=ni-switch path=programming-flow.html language=enus -->
## TOPIC 00588: Programming Flow

- bundle_id: `ni-switch`
- source_path: `programming-flow.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/programming-flow.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram shows the programming flow of applications using NI-SWITCH. For more information about configuring attributes or setting properties, refer to Setting and Checking Properties and Attributes.

### Programming Flow

The following diagram shows the programming flow of applications using NI-SWITCH.

[IMAGE alt='image' src='GUID-034D58F8-C14E-4B8B-A5B4-5FFB4E723DF4-a5.gif']

Tip

Parent topic:

Programming with NI-SWITCH

Related concepts:

- Setting and Checking Properties and Attributes

<!--NI_TOPIC bundle=ni-switch path=programming-the-ni-switchblock-in-ni-switch-a.html language=enus -->
## TOPIC 00589: Programming the NI SwitchBlock in NI-SWITCH and NI-DAQmx

- bundle_id: `ni-switch`
- source_path: `programming-the-ni-switchblock-in-ni-switch-a.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/programming-the-ni-switchblock-in-ni-switch-a.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this book for information about programming the NI SwitchBlock in NI-SWITCH and NI-DAQmx.

### Programming the NI SwitchBlock in NI-SWITCH and NI-DAQmx

Expand this book for information about programming the NI SwitchBlock in NI-SWITCH and
 NI-DAQmx.

Parent topic:

NI SwitchBlock Switching Considerations

<!--NI_TOPIC bundle=ni-switch path=programming-with-ni-switch.html language=enus -->
## TOPIC 00590: Programming with NI-SWITCH

- bundle_id: `ni-switch`
- source_path: `programming-with-ni-switch.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/programming-with-ni-switch.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: To program your switch module, select an API—NI-SWITCH or NI-DAQmx. Refer to the NI Switches Getting Started Guide for more information about these APIs. With the NI-SWITCH API This book covers programming your switch module with the NI-SWITCH API. The following topics are covered: Getting Started—H

### Programming with NI-SWITCH

To program your switch module, select an API—NI-SWITCH or NI-DAQmx. Refer to the
 NI Switches Getting Started Guide for more information about
 these APIs.

#### With the NI-SWITCH API

This book covers programming your switch module with the NI-SWITCH API. The following
 topics are covered:

- Getting Started—How to begin creating your applications in LabVIEW,
 LabWindows/CVI, Visual C++, and Visual Basic
- Programming Flow—The programming flow for immediate operations, and
 scanning
- Features—Task-based information for using your switch module and its
 features
- Examples—Examples in NI LabVIEW, LabWindows/CVI, Visual C++, and Visual
 Basic
- Error and Status Codes—Error codes for NI-SWITCH and IviSwtch

#### With the NI-DAQmx API

To program your switch module with the NI-DAQmx API, refer to the NI-DAQmx
 Help.

Related concepts:

- Creating an application with NI-SWITCH
- Programming Flow
- Features
- NI-SWITCH Programming Examples
- Error and Status Codes

<!--NI_TOPIC bundle=ni-switch path=protecting-ni-switch-products-when-switching.html language=enus -->
## TOPIC 00591: Protecting NI Switch Products when Switching Inductive Loads

- bundle_id: `ni-switch`
- source_path: `protecting-ni-switch-products-when-switching.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/protecting-ni-switch-products-when-switching.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switching inductive loads, such as motors and solenoids, may produce high voltage transients in excess of the NI switch products' rated voltage. Without additional protection, these transients can interfere with NI switch product operation and impact relay life. For more information, visit ni.com/in

### Protecting NI Switch Products when Switching Inductive Loads

Switching inductive loads, such as motors and solenoids, may produce high voltage
 transients in excess of the NI switch products' rated voltage. Without additional
 protection, these transients can interfere with NI switch product operation and impact
 relay life. For more information, visit ni.com/info and enter the Info
 Code relayflyback.

Parent topic:

Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=pxi-express-compatibility.html language=enus -->
## TOPIC 00592: PXI Express Compatibility

- bundle_id: `ni-switch`
- source_path: `pxi-express-compatibility.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/pxi-express-compatibility.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: In an effort to incorporate PCI Express signaling into PXI, the PXI Systems Alliance (pxisa.org) has defined a modification for PXI modules. On modified PXI modules, known as hybrid slot compatible PXI modules, the top rear connector is replaced with a smaller connector. Hybrid slot compatible PXI m

### PXI Express Compatibility

In an effort to incorporate PCI Express signaling into PXI, the PXI Systems Alliance
 (pxisa.org) has defined a
 modification for PXI modules. On modified PXI modules, known as hybrid slot compatible
 PXI modules, the top rear connector is replaced with a smaller connector.

Hybrid slot compatible PXI modules preserve the following features:

- Software compatibility—Hybrid slot compatibility does not require any changes to
 existing applications and/or driver software.
- Specifications—Hybrid slot compatibility does not alter module specifications.
- PXI communication—Hybrid slot compatibility preserves the speed and capability of
 all PXI communication.
- PXI timing and triggering—Hybrid slot compatibility supports existing PXI timing and
 PXI triggering capabilities.
- Hybrid slot compatible PXI modules can operate in standard PXI slots in an NI
 PXI/PXI Express chassis, as well as in PXI Express hybrid slots in an NI PXI Express
 chassis, while PXI cards that are not hybrid slot compatible can only operate in
 standard PXI slots. To determine if your NI switch product is hybrid slot
 compatible, refer to the following figure.

Note

A comparison of a PXI module and a hybrid slot compatible PXI module is shown in the
 following figure.

[IMAGE alt='image' src='GUID-1D0E90AC-1B07-4998-B25E-E09EB6541008-a5.gif']

1. PXI Module
2. Hybrid Slot Compatible PXI Module

Parent topic:

Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=pxi-pxi-express-chassis-recommendations.html language=enus -->
## TOPIC 00593: PXI/PXI Express Chassis Recommendations

- bundle_id: `ni-switch`
- source_path: `pxi-pxi-express-chassis-recommendations.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/pxi-pxi-express-chassis-recommendations.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI PXI/PXI Express switch modules are designed to operate in any PXI-compliant PXI/PXI Express chassis. Temperature rise of the switch module can vary with slot position in the chassis. Observe the following recommendations to minimize this temperature variation and to ensure normal operating condit

### PXI/PXI Express Chassis Recommendations

NI PXI/PXI Express switch modules are designed to operate in any PXI-compliant PXI/PXI
 Express chassis. Temperature rise of the switch module can vary with slot position in
 the chassis. Observe the following recommendations to minimize this temperature
 variation and to ensure normal operating conditions for the NI switch module:

- Some chassis include fan filters. Depending on the amount of chassis use and the
 ambient dust levels, filters might require more frequent cleaning. NI recommends
 cleaning the chassis fan filters at least every six months and keeping the chassis
 environment clean to minimize the amount of dust that enters the chassis. Perform
 routine maintenance of the chassis cooling fan filters to assure continuous cooling
 effectiveness and to keep dust off of the NI switch module components. If regular
 maintenance of dirty or clogged filters is not possible, you can remove foam filters
 to maintain adequate cooling. NI does not recommend removing metal fan filters. For
 more information about cleaning the chassis fan filters, refer to the documentation
 for your chassis.
- Install PXI/PXI Express filler panels in all empty slots.
- Verify that the PXI/PXI Express chassis fans that provide forced air remain
 unobstructed to allow for proper cooling of the PXI/PXI Express chassis, devices,
 and controller.

Parent topic:

Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=reed-relay-protection.html language=enus -->
## TOPIC 00594: Reed Relay Protection

- bundle_id: `ni-switch`
- source_path: `reed-relay-protection.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/reed-relay-protection.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The life expectancy of a reed relay can be greatly affected by the nature of the load. To prolong the life of reed relays, consider the following list when using switches with reed relays: Bounce Arcing Inrush Current Switching Capacitive Loads Board Layout and Topology Example System In general, re

### Reed Relay Protection

The life expectancy of a reed relay can be greatly affected by the nature of the load. To
 prolong the life of reed relays, consider the following list when using switches with
 reed relays:

- Bounce
- Arcing
- Inrush Current
- Switching Capacitive Loads
- Board Layout and Topology
- Example System

In general, reed relays are vulnerable to contact welding from high currents. Parasitic
 capacitance within a system can unavoidably create high inrush currents that can damage
 the reed relay. To minimize inrush current, decrease or isolate external capacitance by:

1. Using lower switching voltages.
2. Avoiding large capacitive loads to the switch.
3. Isolating external capacitance with series impedance R p such that:

V/R<sub>p</sub>< switching current rating of the relay

Parent topic:

General Switching Considerations

Related concepts:

- Relay Life
- Reed Relays
- Bounce
- Arcing
- Inrush Current
- Switching Capacitive Loads
- Board Layout and Topology
- Example System

<!--NI_TOPIC bundle=ni-switch path=reed-relays.html language=enus -->
## TOPIC 00595: Reed Relays

- bundle_id: `ni-switch`
- source_path: `reed-relays.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/reed-relays.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Reed relays are a type of electromechanical relay composed of coils wrapped around reed switches. The reed switch has two overlapping ferromagnetic blades hermetically sealed within a glass capsule that is filled with an inert gas. When the coil is energized, the two reeds physically contact one ano

### Reed Relays

Reed relays are a type of electromechanical relay composed of coils wrapped around reed
 switches. The reed switch has two overlapping ferromagnetic blades hermetically sealed
 within a glass capsule that is filled with an inert gas. When the coil is energized, the
 two reeds physically contact one another to complete a path through the relay. When the
 coil is deenergized, the spring force in the reeds pulls the reeds apart. The following
 figure represents an open reed relay.

[IMAGE alt='image' src='GUID-48E5ED6F-C0B6-4BA8-ADDB-DE29E506A120-a5.gif']

The following figure represents a closed reed relay.

[IMAGE alt='image' src='GUID-B0FFD4FF-ED93-4022-8E0D-E3D782F6592B-a5.gif']

The reeds are generally smaller and therefore can actuate much faster than the armatures
 in armature relays. However, reeds are also more susceptible to damage from arcing than
 are armatures in armature relays. When a spark jumps across the contacts, it can melt a
 small section of the reed. If the contacts are still closed when the molten section
 resolidifies, the contacts may weld together. The spring force in the reeds is often
 insufficient to mechanically break the weld.

When using switch modules with reed relays, consider the effects of switching capacitive
 loads to protect the reed relays.

#### Related Topics

Armature Relays

Reed Relay Protection

Electromechanical Relays

Switching Capacitive Loads

Parent topic:

Electromechanical Relays

Related concepts:

- Armature Relays
- Reed Relay Protection
- Electromechanical Relays
- Switching Capacitive Loads

<!--NI_TOPIC bundle=ni-switch path=relay-count.html language=enus -->
## TOPIC 00596: Relay Count

- bundle_id: `ni-switch`
- source_path: `relay-count.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/relay-count.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Most switch modules and cards are capable of tracking relay usage using the niSwitch Get Relay Count VI or the niSwitch_GetRelayCount function. Relay counts are stored on your NI switch hardware in nonvolatile storage such as EEPROM or flash, and are backed up periodically as well as on system shutd

### Relay Count

Most switch modules and cards are capable of tracking relay usage using the niSwitch Get
 Relay
 Count
 VI or the
 niSwitch_GetRelayCount
 function.

Tip

Switch Soft Front Panel Help

The following switch modules do not support relay counting:

- NI PXI-2501
- NI PXI-2503
- NI PXI-2565
- NI PXI-2590
- NI PXI-2591

Parent topic:

Relay Operation

<!--NI_TOPIC bundle=ni-switch path=relay-forms.html language=enus -->
## TOPIC 00597: Relay Forms

- bundle_id: `ni-switch`
- source_path: `relay-forms.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/relay-forms.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Relays are classified by their number of poles and number of throws. The pole of a relay is the terminal common to every path. Each position where the pole can connect is called a throw. A relay can be made of n poles and m throws. For example, a single-pole single-throw (SPST) relay has one pole an

### Relay Forms

Relays are classified by their number of poles and number of throws. The pole of a relay
 is the terminal common to every path. Each position where the pole can connect is called
 a throw. A relay can be made of n poles and m
 throws. For example, a single-pole single-throw (SPST) relay has one pole and one throw,
 as illustrated in the following figure.

[IMAGE alt='image' src='GUID-B8302A7B-DB76-4CDB-AE32-9A188A011188-a5.gif']

A single-pole double-throw (SPDT) relay has one pole and two throws. Based on the default
 position of the pole, one throw is considered normally open (NO) while the other is
 normally closed (NC). The following figure illustrates a SPDT relay.

[IMAGE alt='image' src='GUID-5F6941DA-7BB2-4A8D-AE6B-4FCAC53BC2EE-a5.gif']

A double-pole double-throw (DPDT) relay has two poles, each with two simultaneously
 controlled throws, as illustrated in the following figure.

[IMAGE alt='image' src='GUID-37820A1E-D7C0-4B92-861A-AC516FE719B6-a5.gif']

An RF transfer switch (DPDT) has four ports (1–4) and two states (reset and set). In the
 reset state, port 1 is connected to port 2 and port 3 is connected to port 4. In the set
 state, port 1 is connected to port 3 and port 2 is connected port 4. The following
 figure illustrates the reset and set states of an RF transfer switch.

[IMAGE alt='image' src='GUID-FABA845A-3EA6-4D70-B6DA-0C3DBF7B1527-a5.gif']

Relays are then classified into forms. Relay forms are categorized by the number of poles
 and throws as well as the default position of the relay. The following table lists three
 common relay forms.

| Form | Symbol | Description |
| --- | --- | --- |
| Form A |  | SPST relays with a default state of normally open. |
| Form B |  | SPST relays with a default state of normally closed. |
| Form C |  | SPDT relays that break the connection with one throw before making contact with the other (break-before-make). |

Parent topic:

Fundamentals

<!--NI_TOPIC bundle=ni-switch path=relay-life.html language=enus -->
## TOPIC 00598: Relay Life

- bundle_id: `ni-switch`
- source_path: `relay-life.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/relay-life.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI switches typically specify a conservative estimation of the expected life of the electromechanical relay components. Relay life is specified as a minimum number of cycles before the end of the relay life. One cycle is defined as the action of opening and closing the relay. The expected life is di

### Relay Life

Tip

niSwitch_GetRelayCount

#### Mechanical Life

The contacts of mechanical relays wear with usage, and worn contacts have a higher
 contact resistance. The mechanical life specification is typically the number of
 switch cycles before the contact resistance rises above 1 Ω. This rating assumes no
 electrical load across contacts during actuation.

#### Electrical Life

Switching active electrical signals, especially high power signals, causes arcing
 across the relay contacts. This arcing produces pits on the contact surface and
 accelerates the contact wear described in Mechanical Life. The electrical life
 specification is the number of switch cycles, under load, before the contact
 resistance rises above 1 Ω.

Parent topic:

General Switching Considerations

Related concepts:

- Electromechanical Relays
- Relay Count
- Contact Resistance
- Arcing

<!--NI_TOPIC bundle=ni-switch path=relay-lifetime.html language=enus -->
## TOPIC 00599: Relay Lifetime

- bundle_id: `ni-switch`
- source_path: `relay-lifetime.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/relay-lifetime.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When selecting a relay for an application, an important characteristic to consider is the relay life expectancy. Relay life expectancy can be measured by relay cycles but can be more accurately measured by relay contact resistance. One relay cycle is defined as the action of opening and closing the

### Relay Lifetime

When selecting a relay for an application, an important characteristic to consider is the
 relay life expectancy. Relay life expectancy can be measured by relay cycles but can be
 more accurately measured by relay contact resistance. One relay cycle is defined as the
 action of opening and closing the relay. Most switching products provide both mechanical
 and electrical expected lifetimes.

#### Mechanical Lifetime

The mechanical lifetime is the typical number of cycles that a relay can sustain
 under dry switching conditions (switched with no electrical load). The mechanical
 lifetime is based on metal fatigue within the bending armature or reed switch. The
 typical number of cycles tends to be higher than the electrical lifetime and is
 rarely reached in switching systems.

#### Electrical Lifetime

Switching active electrical signals, especially high-power signals, causes arcing
 across the relay contacts. This arcing produces pits on the contact surface and
 accelerates the contact wear. The electrical lifetime is the number of switch cycles
 under load before the contact resistance rises above a certain value, or the
 contacts become stuck open or stuck closed. This electrical life specification is
 often used as the cycle limit for a given relay; however, it can only be used as a
 reliable indicator for relay failure if the load being switched in your test system
 matches the load that was used to determine the relay specification. Measuring relay
 contact resistance provides a more accurate indicator of electrical lifetime for
 relays.

Parent topic:

NI Switch Health Center Help

<!--NI_TOPIC bundle=ni-switch path=relay-operation.html language=enus -->
## TOPIC 00600: Relay Operation

- bundle_id: `ni-switch`
- source_path: `relay-operation.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/relay-operation.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This book contains information about concepts related to relay operation. Cycle Process Settling Time Relay Count

### Relay Operation

This book contains information about concepts related to relay operation.

- Cycle Process
- Settling Time
- Relay Count

Parent topic:

General Switching Considerations

Related concepts:

- Cycle Process
- Settling Time
- Relay Count

<!--NI_TOPIC bundle=ni-switch path=relay-replacement.html language=enus -->
## TOPIC 00601: Relay Replacement

- bundle_id: `ni-switch`
- source_path: `relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2503 uses electromechanical armature relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Number NEC-TOKIN EF2-4.5NUX-L6 Relay Kit Part Number M3 Distribution (10 relays) 197488A-01 Complete the following steps to replace a failed

### Relay Replacement

The NI PXI-2503 uses electromechanical armature relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| NEC-TOKIN | EF2-4.5NUX-L6 |

| Relay Kit | Part Number |
| --- | --- |
| M3 Distribution (10 relays) | 197488A-01 |

Complete the following steps to replace a failed relay.

1. Ground yourself using a grounding strap or a ground connected to your PXI chassis.
 Note Properly grounding yourself prevents damage to your module
 from electrostatic discharge.
2. Refer to the following figures and table to locate the relay you want to replace.
 NI PXI-2503 
 [IMAGE alt='image' src='GUID-ADFD674A-740A-4D25-95AF-D8D634350B36-a5.gif'] 
 NI PXI-2503 Hardware Diagram 
 [IMAGE alt='image' src='GUID-3398B085-4555-4A8B-84C9-D778B17D8D92-a5.gif'] 
 Relay Name
 Reference DesignatorCH0
 K32CH1
 K1CH2
 K2CH3
 K3CH4
 K4CH5
 K5CH6
 K6CH7
 K7CH8
 K8CH9
 K9CH10
 K10CH11
 K11CH12
 K12k13
 K12CH13
 K13CH14
 K14CH15
 K15CH16
 K16CH17
 K17CH18
 K18CH19
 K19CH20
 K20CH21
 K21CH22
 K22CH23
 K23BC01
 K24BC23
 K25BC02
 K26CJTEMP
 K271WIRE
 K28HLSEL
 K29AB0
 K30AB2
 K31
3. Locate the assembly and serial number labels on the board with the relay you want to
 replace. White labels indicate the board was assembled using lead solder (Sn 63 Pb
 37). Green labels indicate the board was assembled using lead-free solder (Sn 96.5
 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers ending in L. The
 different label types are shown in the following figure. [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']

#### Replace the Relay

Note

Caution

Caution

Make sure you have the following items:

- Temperature-regulated soldering iron set to 316 °C (600 °F) for lead solder
 rework or 371 °C (700 °F) for lead-free solder rework
- 63/37 Tin/Lead solder (flux core) for lead solder rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Isopropyl alcohol
- Cotton swabs

Replace the relay as you would any other through-hole part.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2501/2503

<!--NI_TOPIC bundle=ni-switch path=relay-types.html language=enus -->
## TOPIC 00602: Relay Types

- bundle_id: `ni-switch`
- source_path: `relay-types.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/relay-types.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI switch modules use the following relay types: Electromechanical Relays Solid-State Relays FET Switches To determine the relay type(s) of a specific switch module, refer to the specifications for that switch module.

### Relay Types

NI switch modules use the following relay types:

- Electromechanical Relays
- Solid-State Relays
- FET Switches

To determine the relay type(s) of a specific switch module, refer to the specifications
 for that switch module.

Parent topic:

Fundamentals

Related concepts:

- Electromechanical Relays
- Solid-State Relays (SSR)
- FET Switches

<!--NI_TOPIC bundle=ni-switch path=removing-ni-switchblock-carrier-device-max.html language=enus -->
## TOPIC 00603: Removing an NI SwitchBlock Carrier or Device in MAX

- bundle_id: `ni-switch`
- source_path: `removing-ni-switchblock-carrier-device-max.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/removing-ni-switchblock-carrier-device-max.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete one of the following procedures to remove an NI SwitchBlock carrier or device from your configuration in MAX. Removing an Installed Carrier To remove an installed carrier from the MAX configuration tree, power off and unplug the PXI/PXI Express chassis in which the carrier is installed, the

### Removing an NI SwitchBlock Carrier or Device in MAX

Complete one of the following procedures to remove an NI SwitchBlock carrier or device
 from your configuration in MAX.

#### Removing an Installed Carrier

To remove an installed carrier from the MAX configuration tree, power off and unplug
 the PXI/PXI Express chassis in which the carrier is installed, then physically
 remove the carrier from the PXI/PXI Express chassis. Power on the system, then
 right-click the carrier name in the configuration tree in MAX and select
 Delete.

#### Removing an Installed Device

To remove an installed device from the MAX configuration tree, power off and unplug
 the PXI/PXI Express chassis in which the carrier that contains the device is
 installed, then physically remove the cards that compose the device from the
 carrier. Power on the system, then right-click the device name in the configuration
 tree in MAX and select Delete.

#### Removing a Simulated Carrier or Device

To remove a simulated carrier or device from your configuration, right-click the
 simulated carrier or device in the configuration tree and select
 Delete.

Parent topic:

NI SwitchBlock Configuration Panel Help

<!--NI_TOPIC bundle=ni-switch path=replacing-a-fuse-on-the-ni-switchblock-carrie.html language=enus -->
## TOPIC 00604: Replacing a Fuse on the NI SwitchBlock Carrier

- bundle_id: `ni-switch`
- source_path: `replacing-a-fuse-on-the-ni-switchblock-carrie.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/replacing-a-fuse-on-the-ni-switchblock-carrie.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: An LED on the backplane inside the NI SwitchBlock carrier indicates the condition of the carrier fuse. The carrier fuse is field replaceable. If one of the following scenarios occurs, you need to replace the fuse: The LED inside the carrier is off when the chassis in which the carrier is installed i

### Replacing a Fuse on the NI SwitchBlock Carrier

An LED on the backplane inside the NI SwitchBlock carrier indicates the condition of the
 carrier fuse. The carrier fuse is field replaceable. If one of the following scenarios
 occurs, you need to replace the fuse:

- The LED inside the carrier is off when the chassis in which the carrier is installed
 is powered on.
- When you right-click a device in the carrier in the MAX configuration tree and
 select Self-Test , MAX returns an error that indicates the
 fuse in the carrier has blown.

Refer to the following table for information about ordering replacement fuses.

| Fuse Type | Rating | Blow Speed | Manufacturer | Part Number |
| --- | --- | --- | --- | --- |
| 5 V internal supply fuse | 7 A, 125 V | Very fast (FF) | Littelfuse | 0453007 |

Use the following instructions to locate and replace the fuse.

#### Locate the Fuse

Complete the following steps to locate the fuse:

1. Power off and unplug the NI PXI/PXI Express chassis.
2. Remove all NI SwitchBlock cards from the carrier.
3. Remove any installed NI 2806 expansion bridges.
4. Remove the carrier from the NI PXI/PXI Express chassis.
5. Locate the fuse on the backplane of the carrier directly below the connector for
 the leftmost card as shown in the following figure. 1
 Fuse2
 NI PXI-2800 Backplane Connector3
 NI PXI-2800 Backplane

#### Replace the Fuse

Complete one of the following procedures to replace the fuse.

#### Replacement Method 1

Complete the following procedure if you would like to minimize the number of steps
 and tools required to replace the fuse.

1. Insert a small pair of needle nose pliers into the front of the carrier and
 gently pull on the fuse to remove it from the fuse holder.
2. Replace the fuse.
3. Reinstall any cards and NI 2806 expansion bridges that you removed when you
 located the fuse. Caution If you removed one or more NI 2806
 expansion bridges but do not plan to reinstall them, you must reinstall the
 expansion bridge connector covers on any unused expansion bridge connectors
 on the carrier.

#### Replacement Method 2

Complete the following procedure if you would like more work space when replacing the
 fuse.

1. Use a T8 Torx ® screwdriver to remove the six T8 screws that connect
 the backplane to the back of the carrier. If the expansion bridge connector
 covers are attached to the carrier, also remove the four T8 screws that connect
 expansion bridge connector covers to the carrier. Refer to the following figure.
 1
 NI PXI-2800 Carrier2
 NI PXI-2800 Backplane3
 Expansion Bridge Connector Covers4
 Screws
2. Remove the expansion bridge connector covers.
3. Remove the backplane from the back of the carrier.
4. Use a pair of needle nose pliers to gently pull on the fuse to remove it from
 the fuse holder.
5. Replace the fuse.
6. Reattach the backplane to the back of the carrier using the six T8 screws
 removed previously.
7. Reinstall the carrier as well as any cards and NI 2806 expansion bridges that
 you removed when you located the fuse. Caution If you removed
 one or more NI 2806 expansion bridges but do not plan to reinstall them, you
 must reinstall the expansion bridge connector covers on any unused expansion
 bridge connectors on the carrier.

Parent topic:

NI SwitchBlock Maintenance

<!--NI_TOPIC bundle=ni-switch path=rf-switching-considerations.html language=enus -->
## TOPIC 00605: RF Switching Considerations

- bundle_id: `ni-switch`
- source_path: `rf-switching-considerations.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/rf-switching-considerations.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about the terminology and concepts related to RF switching applications.

### RF Switching Considerations

Learn about the terminology and concepts related to RF switching applications.

- [Characteristic Impedance](characteristic-impedance.html)
- [Rise Time](rise-time.html)
- [Bandwidth and Insertion Loss](bandwidth-and-insertion-loss.html)
- [Voltage Standing Wave Ratio (VSWR)](voltage-standing-wave-ratio-vswr.html)
- [Crosstalk](crosstalk.html)
- [Isolation](isolation.html)

Parent topic:

Fundamentals

<!--NI_TOPIC bundle=ni-switch path=rise-time.html language=enus -->
## TOPIC 00606: Rise Time

- bundle_id: `ni-switch`
- source_path: `rise-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/rise-time.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Given an ideal step input, rise time is the time required for the output signal voltage to rise from 10% to 90% of the step amplitude. Rise time is related to bandwidth using the following approximation: τ[r] = 0.35/bandwidth (Hz) The following figure illustrates rise time.

### Rise Time

Given an ideal step input, rise time is the time required for the
 output signal voltage to rise from 10% to 90% of the step amplitude. Rise time is
 related to bandwidth using the following approximation:

τ<sub>r</sub> = 0.35/bandwidth (Hz)

The following figure illustrates rise time.

[IMAGE alt='image' src='GUID-FC2A0EED-3AE8-4050-AF3E-C6322516F9DB-a5.gif']

Parent topic:

RF Switching Considerations

Related concepts:

- Bandwidth and Insertion Loss

<!--NI_TOPIC bundle=ni-switch path=routing-signals-between-multiple-ni-switchblo.html language=enus -->
## TOPIC 00607: Routing Signals Between Multiple NI SwitchBlock Devices

- bundle_id: `ni-switch`
- source_path: `routing-signals-between-multiple-ni-switchblo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/routing-signals-between-multiple-ni-switchblo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can route signals between multiple NI SwitchBlock devices in the same carrier or between multiple NI SwitchBlock devices in two or more NI SwitchBlock carriers. Sharing Signals Between Multiple SwitchBlock Devices Follow these steps to share signals between multiple NI SwitchBlock devices: If mo

### Routing Signals Between Multiple NI SwitchBlock Devices

You can route signals between multiple NI SwitchBlock devices in the same carrier or
 between multiple NI SwitchBlock devices in two or more NI SwitchBlock carriers.

#### Sharing Signals Between Multiple SwitchBlock Devices

1. If more than one
 carrier is present, install the NI 2806 Expansion Bridge between the two NI
 SwitchBlock carriers. Once the NI 2806 Expansion Bridge is installed, there is
 no difference between multiple NI SwitchBlock devices in a single carrier and
 multiple NI SwitchBlock devices in multiple carriers. Refer to Expanding
 Multiple NI SwitchBlock Carriers for more information.
2. Enable analog bus sharing on each analog bus line used to share signals between
 multiple NI SwitchBlock devices. Enabling analog bus sharing removes the default
 software setting that restricts two NI SwitchBlock devices from connecting to
 the same analog bus line simultaneously. Refer to Using the analog bus on an NI
 SwitchBlock Carrier for more information.

Note

#### Sharing Analog Bus Lines Between NI SwitchBlock Devices of Different
 Types

Analog bus lines between NI SwitchBlock relay cards of different types can be shared
 if they have the same wire mode.

For example, the NI 2815 is a four-row, 1-wire module that connects to analog bus
 lines ab0-3. The NI 2816 is an eight-row, 1-wire module that connects to analog bus
 lines ab0-7. The first four analog bus lines (ab0-3) can be shared between the NI
 2815 and NI 2816 and used to route signals between them. However, analog bus lines
 ab4-7 can only be shared with the NI 2816 or other 1-wire NI SwitchBlock relay cards
 with at least 8 rows.

NI SwitchBlock devices of different wire modes cannot share analog bus lines.  For
 example, the NI 2816 is an eight-row, 1-wire relay card and cannot share analog bus
 lines with the NI 2813, a four-row, 2-wire relay card.  Though both devices use
 eight analog bus lines, NI-DAQmx and NI-SWITCH do not allow analog bus sharing to be
 enabled between these devices.

Note

NI-SWITCH LabVIEW Reference

DAQmx Relay
 Operations VIs

LabVIEW Help

There are two ways to program multiple NI SwitchBlock devices after analog bus
 sharing has been enabled: endpoint programming and explicit path programming.

#### Endpoint Programming

Endpoint programming uses NI-DAQmx or NI-SWITCH to automatically determine the best
 route between two columns. This programming technique remains straightforward
 regardless of how many NI SwitchBlock relay cards are in an NI SwitchBlock device.

Follow these steps to use endpoint programming:

1. Enable analog bus sharing for all of the analog bus lines on each device. To
 enable analog bus sharing, set the NI-DAQmx Switch Channel property
 Analog Bus Sharing Enable to True, or set the
 NI-SWITCH Channel Configuration Analog Bus Sharing
 Enable
 property to True.
2. Set all rows within the NI SwitchBlock device as Reserved for Routing. To
 reserve a line for routing in NI-DAQmx, set the Channel
 Usage property to Reserved For Routing. In NI-SWITCH, set the
 Channel Configuration property Is Configuration
 Channel
 to True. NI-DAQmx and NI-SWITCH automatically determine the best route between
 the columns using any combination of the rows that have been reserved for
 routing. NI-DAQmx and NI-SWITCH return an error if no path is available or if no
 lines have been reserved for routing.
3. Specify the column and analog bus line to connect on each NI SwitchBlock device.
 This will require a separate NI-DAQmx Connect command or NI-SWITCH Connect
 Channels command for each NI SwitchBlock Device. NI-DAQmx and NI-SWITCH will
 automatically determine the route between the columns and the analog bus line
 using one of the rows that have been reserved for routing. NI-DAQmx and
 NI-SWITCH will return an error if no path is available or if no lines have been
 reserved for routing.

Note

NI Switches
 Help

The following examples show how to use endpoint programming to route signals between
 two NI SwitchBlock devices, each containing three NI 2810 relay cards. These
 examples contain a subVI that automatically determines the correct naming for all of
 the rows that must be reserved for routing and the analog bus lines that must be
 shared. This VI can be used with any NI SwitchBlock device.

For an example using NI-DAQmx for multiple device endpoint connections, visit
 ni.com/info and enter the Info Code excjkx.
 For an example using NI-SWITCH for multiple device endpoint connections, visit
 ni.com/info and enter the Info Code
 ex6dte.

#### Explicit Path Programming

Explicit path programming requires every individual path to be explicitly closed.
 This method provides additional customization by allowing the selection of which
 rows and analog bus lines are used to connect signals. Explicit path programming
 becomes more complicated as additional modules are required in the route. Explicit
 path programming does not require any path to be reserved for routing.

Follow these steps to use explicit path programming to connect two columns (cX and
 cY) on the same relay card (CardM):

1. Connect column cX to row CardMrN.
2. Connect cY to row CardMrN.

Follow these steps to use explicit path programming to connect two columns (cX and
 cY) on different relay cards (CardM and CardK) in different NI SwitchBlock
 devices:

1. Enable analog bus sharing for all of the analog bus lines on each device. To
 enable analog bus sharing, set the NI-DAQmx Switch Channel property
 Analog Bus Sharing Enable to True, or set the
 NI-SWITCH Channel Configuration Analog Bus Sharing
 Enable
 property to True.
2. Connect column cX to row CardMrN on the first relay card.
3. Connect row CardMrN to analog bus line abZ on the first relay card.
4. Connect analog bus line abZ to row CardKrN on the second relay card.
5. Connect row CardKrN to column cY on the second relay card.

Note

The following examples show how to route a signal between two NI SwitchBlock devices,
 each containing three NI 2810 relay cards. These examples can be used with any two
 NI SwitchBlock devices. These examples contain a subVI that automatically determines
 the correct naming for all of the analog bus lines that must be shared. This VI can
 be used with any NI SwitchBlock device.

For an example using NI-DAQmx for multiple device explicit path connections, visit
 ni.com/info and enter the Info Code ex5z4m.
 For an example using NI-SWITCH for multiple device explicit path connections, visit
 ni.com/info and enter the Info Code
 exmpji.

Parent topic:

Programming the NI SwitchBlock in NI-SWITCH and NI-DAQmx

<!--NI_TOPIC bundle=ni-switch path=routing-signals-within-one-ni-switchblock-dev.html language=enus -->
## TOPIC 00608: Routing Signals Within One NI SwitchBlock Device

- bundle_id: `ni-switch`
- source_path: `routing-signals-within-one-ni-switchblock-dev.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/routing-signals-within-one-ni-switchblock-dev.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can route signals in a single NI SwitchBlock device with NI-DAQmx and NI-SWITCH using either endpoint programming or explicit path programming. Endpoint Programming Endpoint programming uses NI-DAQmx or NI-SWITCH to automatically determine the best route between two columns. This programming tec

### Routing Signals Within One NI SwitchBlock Device

You can route signals in a single NI SwitchBlock device with NI-DAQmx and NI-SWITCH
 using either endpoint programming or explicit path programming.

#### Endpoint Programming

Endpoint programming uses NI-DAQmx or NI-SWITCH to automatically determine the best
 route between two columns. This programming technique remains straightforward
 regardless of how many NI SwitchBlock relay cards are in an NI SwitchBlock device.

Follow these steps to use endpoint programming:

1. Set all of the rows and analog bus lines within the NI SwitchBlock device as
 Reserved for Routing. To set Reserved for Routing in NI-DAQmx, set the
 Channel Usage property to Reserved For Routing. In
 NI-SWITCH, set the Channel Configuration property Is Configuration
 Channel
 to True.
2. Specify the two columns to connect using the NI-DAQmx Switch
 Connect function or the niSwitch Connect
 Channels
 VI. NI-DAQmx and NI-SWITCH automatically determine the best route between the
 columns using any combination of the rows and analog bus lines that have been
 reserved for routing. NI-DAQmx and NI-SWITCH return an error if no path is
 available or if no lines have been reserved for routing.

Note

NI Switches Help

The following examples show how to use endpoint programming to route signals within a
 single NI SwitchBlock device composed of six NI 2810s.  These examples contain a
 subVI that automatically determines the correct naming for all of the rows and
 analog bus lines that must be reserved. This VI can be used with any NI SwitchBlock
 device.

For an example using NI-DAQmx for single device endpoint connections, visit
 ni.com/info and enter the Info Code exv36g.
 For an example using NI-SWITCH for single device endpoint connections, visit
 ni.com/info and enter the Info Code
 exi3qv.

#### Explicit Path Programming

Explicit path programming is a technique that requires every individual path to be
 explicitly closed. This method provides additional customization by allowing
 selection of which rows and analog bus lines are used to connect signals. Explicit
 path programming becomes more complicated as additional modules are required in the
 route. Explicit path programming does not require any path to be reserved for
 routing.

Follow these steps to use explicit path programming to connect two columns (cX and
 cY) on the same relay card:

1. Connect column cX to row CardMrN.
2. Connect column cY to row CardMrN.

The following figure shows how connections are made on a single relay card with NI
 SwitchBlock devices.

[IMAGE alt='image' src='GUID-80033490-2775-449F-9F06-BB2AB5618257-a5.gif']

Follow these steps to use explicit path programming to connect two columns on
 different relay cards (CardM and CardK):

1. Connect column cX to row CardMrN on the first relay card.
2. Connect row CardMrN to analog bus line abZ on the first relay card.
3. Connect analog bus line abZ to row CardKrN on the second relay card.
4. Connect row CardKrN to column cY on the second relay card.

The following figure shows how connections are made between multiple relay cards on a
 single NI SwitchBlock device.

[IMAGE alt='image' src='GUID-D15D2A37-54F7-4797-87B8-06BB89216066-a5.gif']

The following examples show connections between multiple relay cards using six NI
 2810 relay cards combined into a single NI SwitchBlock device.

For an example using NI-DAQmx for single device explicit path connections, visit
 ni.com/info and enter the Info Code exut3a.
 For an example using NI-SWITCH for single device explicit path connections, visit
 ni.com/info and enter the Info Code
 exzh6m.

Parent topic:

Programming the NI SwitchBlock in NI-SWITCH and NI-DAQmx

<!--NI_TOPIC bundle=ni-switch path=scan-lists.html language=enus -->
## TOPIC 00609: Scan Lists

- bundle_id: `ni-switch`
- source_path: `scan-lists.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/scan-lists.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: A scan list is a string composed of channel names and characters that define connections, disconnections, triggering, and timing of the scan. Scan List Characters The following table shows characters that can be used in a scan list when programming with NI-SWITCH. Character(s) Definition -> Used in

### Scan Lists

A scan list is a string composed of channel names and characters that define connections,
 disconnections, triggering, and timing of the scan.

#### Scan List Characters

The following table shows characters that can be used in a scan list when programming
 with NI-SWITCH.

| Character(s) | Definition |
| --- | --- |
| -> | Used in a connect action (channel1->channel2). For example, the string ch0->com0 connects CH0 to COM0. |
| ~ | Used with '->' in a disconnect action (~channel1->channel2). Valid only in No Action mode. For example, ~ch0->com0 means disconnect CH0 and COM0. |
| ; | Wait for debounce, send scan advanced output signal*, then wait for trigger input |
| & | Separates connect and/or disconnect actions. For example, the string ch0->com0 & ch9->com1 means connect CH0 to COM0 and CH9 to COM1 (in no particular order and with minimal delay). |
| && | Wait for debounce. For example, ch0->com0 && ch9->com1 means connect CH0 to COM0, wait for the relays to settle, then connect CH9 to COM1. |
| : | Used in a channel range (channelX:Y, where X and Y are integers). Text containing a channel range represents multiple scan list entries. For example, the string ch0:7->com0; represents eight scan list entries. A semicolon must appear after the connect action using a channel range. |

Note

*

ch1->com1 &
 ~ch0->com0;

~ch0->com0;

ch0->com0;;;;

Tip

#### Scan List Entries

A scan list entry is the text delimited by semicolons (;). Scan lists are composed of
 one or more scan list entries. For example, the following scan list contains two
 scan list entries:

ch0->com0; ch1->com0;

#### Scan Modes

The scan mode affects how the driver interprets the scan list. Typical scanning
 applications use the Break Before Make scan mode.

| Mode | Description |
| --- | --- |
| Break Before Make (default) | Connections from the previous scan list entry are automatically disconnected before executing the current scan list entry. Disconnect actions, such as ~channel1->channel2, are not valid in this mode. |
| No Action | Connections remain connected until they are explicitly disconnected by a disconnect action. |
| Break After Make | Currently not supported. |

#### Scan List Examples

#### Example 1

Scan Mode: No Action

Scan List: ch0->com0; ~ch0->com0 &&
 ch1->com0; ~ch1->com0 &&

Meaning:

1. Connect ch0 to com0.
2. Wait for debounce, send scan advanced signal, then wait for trigger input.
3. Disconnect ch0 from com0 and wait for debounce.
4. Connect ch1 to com0.
5. Wait for debounce, send scan advanced signal, then wait for trigger input.
6. Disconnect ch1 from com0 and wait for debounce.
7. If the scan is set to
 continuous,
 return to step 1; otherwise, end the scan.

#### Example 2

Scan Mode: Break Before Make

Scan List: ch0->com0;
 ch1->com0;

Meaning:

The scan list in this example is equivalent to the scan list in Example 1. Notice
 that the disconnect actions in Example 1 are no longer required.

#### Example 3

Scan Mode: Break Before Make Scan List: ch0:1->com0;

Meaning:

This scan list is equivalent to Example 1 and Example 2. This scan list uses a
 channel range to reduce keystrokes.

Parent topic:

Single Module Scanning

Related concepts:

- Scanning
- Settling Time
- Multiple Module Scan Lists

<!--NI_TOPIC bundle=ni-switch path=scanning-fundamentals.html language=enus -->
## TOPIC 00610: Scanning Fundamentals

- bundle_id: `ni-switch`
- source_path: `scanning-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/scanning-fundamentals.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Scanning is typically used when the timing of connections must be synchronized with an event from another device, such as a measurement device (hardware-timed scanning), or must be timed by software (software-timed scanning). Connection operations are entered in a scan list that is downloaded to the

### Scanning Fundamentals

Scanning is typically used when the timing of connections must be synchronized with an
 event from another device, such as a measurement device (hardware-timed scanning), or
 must be timed by software (software-timed scanning).

Connection operations are entered in a scan list that is downloaded to the memory of the
 switch module. The first entry in the scan list is executed when the scan is initiated.
 The trigger settings determine how the switch advances through subsequent entries in the
 list. The scan list can be executed once or repeatedly.

There are three trigger schemes for scanning:

- Software trigger scanning—Used for software-timed scanning
- Synchronous scanning—Used for hardware-timed scanning
- Handshaking—Used for hardware-timed scanning

Note

Parent topic:

Fundamentals

Related concepts:

- Scan Lists
- Software Trigger Scanning
- Synchronous Scanning
- Handshaking

<!--NI_TOPIC bundle=ni-switch path=scanning-ni-switches-with-ni-digital-multimet.html language=enus -->
## TOPIC 00611: Scanning NI Switches with NI Digital Multimeters

- bundle_id: `ni-switch`
- source_path: `scanning-ni-switches-with-ni-digital-multimet.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/scanning-ni-switches-with-ni-digital-multimet.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: In applications where you are connecting multiple test points to a Digital Multimeter (DMM), it may be appropriate to incorporate a switch to route signals between the test points and the DMM. Scanning can be used when the timing of connections needs to be synchronized with the DMM. To determine whe

### Scanning NI Switches with NI Digital Multimeters

In applications where you are connecting multiple test points to a Digital Multimeter (DMM),
 it may be appropriate to incorporate a switch to route signals between the test points and the
 DMM. Scanning can be used when the timing of connections needs to be synchronized with the
 DMM. To determine whether your DMM can exchange signals with NI switches during multipoint
 scanning operations, refer to the Scanning Switch Modules topic in the
 NI Digital Multimeters Help. When scanning NI switches with NI DMMs, the
 following factors will influence your scanning setup:

- Trigger Options
- System Options
- Scanning Capabilities

Note

#### Trigger Options

The trigger inputs and outputs that are available for your NI switch, in conjunction with
 your system and scanning selections, will determine how trigger signals are sent between
 your NI Switch and your NI DMM. The following table lists the trigger input and output
 options for all NI switches.

#### Trigger Options for National Instruments Switches

| Switch | INPUT Trigger Input | OUTPUT Trigger Output |
| --- | --- | --- |
| PXI-2501 PXI-2503 PXI/PXIe-2529 PXI-2530 PXI-2530B PXI/PXIe-2543 PXI-2566 PXI-2567 PXI/PXIe-2593 | all PXI trig, Front |  |
| PXI-2510 PXI/PXIe-2512 PXI/PXIe-2514 PXI/PXIe-2515 PXI/PXIe-2527 PXI/PXIe-2531 PXI/PXIe-2532 PXI/PXIe-2532B PXI-2533 PXI-2534 PXI-2535 PXI-2536 PXI-2545 PXI-2546 PXI-2547 PXI-2548 PXI-2549 PXI-2554 PXI-2555 PXI-2556 PXI-2557 PXI-2558 PXI-2559 PXI-2564 PXI-2565 PXI-2568 PXI/PXIe-2569 PXI-2570 PXI-2571 PXI/PXIe-2575 PXI-2576 PXI-2584 PXI-2585 PXI-2586 PXI-2590 PXI-2591 PXI-2594 PXI-2595 PXI-2596 PXI-2597 PXI-2598 PXI-2599 PXI-2720 PXI-2722 PXIe-2725 PXIe-2727 | all PXI trig |  |
| PXIe-2524 PXIe-2525 PXIe-2526 PXIe-2737 PXIe-2738 PXIe-2739 PXIe-2746 PXIe-2747 PXIe-2748 NI 2810 NI 2811 NI 2812 NI 2813 NI 2814 NI 2815 NI 2816 NI 2817 NI 2833 NI 2834 | Triggering is not supported |  |

where

PXI trig refers to PXI trigger lines 0-7

Front refers to the front panel or terminal block

#### System Options

You can categorize different DMM/switch systems according to the DMM, the switch and the
 cable used. The following figure represents each possible system with a letter.

#### DMM/Switch System Options

[IMAGE alt='image' src='GUID-A2D628C3-BF55-4BC0-973B-D3166A1BDF17-a5.gif']

The systems are classified as follows:

- System A—The DMM triggers the PXI switch using PXI trigger lines. PXI-4060 uses only PXI
 trigger lines 0 to 6. PXI-4070 uses PXI trigger lines 0 to 7.
- System B—A PXI or PCI DMM triggers the PXI switch using the AUX trigger cable.

#### Scanning Capabilities

The following table shows the scanning capabilities for every NI switch. The number after S
 or H indicates the setup number. FThe links in the table direct you to Multiple Module
 Scanning setups. For single module setups, refer to Single Module Scanning.

#### Scanning Capabilities for NI
 Switches

| Switches | System A: PXI Trigger Lines | System B: AUX Trigger Cable |
| --- | --- | --- |
| PXI-2501 PXI-2503 PXI/PXIe-2529 PXI-2530 PXI-2530B PXI/PXIe-2543 PXI-2566 PXI-2567 PXI/PXIe-2593 | Synchronous scanning setup 1: Refer to section Setup 1—Using Internal PXI Trigger Lines in Multiple Module Scanning - Synchronous Handshaking setup 3: Refer to Setup 3—Using Internal PXI Trigger Lines in Multiple Module Scanning - Handshaking | Synchronous scanning setup 2: Refer to section Setup 2—Using AUX Trigger Cable Connected to Front of PXI/PXI Express Switch in Multiple Module Scanning - Synchronous Handshaking setup 4: Refer to section Setup 4—Using AUX Trigger Cable Connected to Front of PXI/PXI Express Switch in Multiple Module Scanning - Handshaking |
| PXI-2510 PXI/PXIe-2512 PXI/PXIe-2514 PXI/PXIe-2515 PXI/PXIe-2527 PXI/PXIe-2531 PXI/PXIe-2532 PXI/PXIe-2532B PXI-2533 PXI-2534 PXI-2535 PXI-2536 PXI-2545 PXI-2546 PXI-2547 PXI-2548 PXI-2549 PXI-2554 PXI-2555 PXI-2556 PXI-2557 PXI-2558 PXI-2559 PXI-2565 PXI-2568 PXI/PXIe-2569 PXI-2570 PXI-2571 PXI/PXIe-2575 PXI-2576 PXI-2584 PXI-2590 PXI-2591 PXI-2594 PXI-2595 PXI-2596 PXI-2597 PXI-2598 PXI-2599 PXI-2720 PXI-2722 PXIe-2725 PXIe-2727 | Synchronous scanning setup 1: Refer to section Setup 1—Using Internal PXI Trigger Lines in Multiple Module Scanning - Synchronous Handshaking setup 3: Refer to Setup 3—Using Internal PXI Trigger Lines in Multiple Module Scanning - Handshaking |  |
| NI 2810 NI 2811 NI 2812 NI 2813 NI 2814 NI 2815 NI 2816 NI 2817 NI 2833 NI 2834 | Scanning is not supported |  |

Parent topic:

Scanning

Related concepts:

- Single Module Scanning
- Multiple Module Scanning
- Multiple Module Scanning - Synchronous
- Multiple Module Scanning - Handshaking

<!--NI_TOPIC bundle=ni-switch path=scanning.html language=enus -->
## TOPIC 00612: Scanning

- bundle_id: `ni-switch`
- source_path: `scanning.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/scanning.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-SWITCH API offers the following three triggering schemes for scanning. Software trigger scanning Synchronous scanning Handshaking Refer to the switch module documentation in Devices to determine if the switch module supports scanning. Refer to Software Trigger Scanning for information on prog

### Scanning

The NI-SWITCH API offers the following three triggering schemes for scanning.

- Software trigger scanning
- Synchronous scanning
- Handshaking

Refer to the switch module documentation in Devices to determine if the switch module
 supports scanning.

Software Trigger Scanning

Note

Parent topic:

Features

Related concepts:

- Software Trigger Scanning
- Synchronous Scanning
- Handshaking
- Writing a Software Trigger Scanning Program
- Scanning NI Switches with NI Digital Multimeters

<!--NI_TOPIC bundle=ni-switch path=setting-and-checking-properties-and-attribute.html language=enus -->
## TOPIC 00613: Setting and Checking Properties and Attributes

- bundle_id: `ni-switch`
- source_path: `setting-and-checking-properties-and-attribute.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/setting-and-checking-properties-and-attribute.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Properties and attributes allow access to advanced configuration options and information for LabVIEW and CVI\C\C++\VB respectively. NI-SWITCH contains high-level VIs/functions that set most of the switch module properties/attributes. Use the high-level driver VIs/functions as much as possible becaus

### Setting and Checking Properties and Attributes

Properties and attributes allow access to advanced configuration options and information
 for LabVIEW and CVI\C\C++\VB respectively.

NI-SWITCH contains high-level VIs/functions that set most of the switch module
 properties/attributes. Use the high-level driver VIs/functions as much as possible
 because they handle order dependencies and multithread locking.

#### Properties

In LabVIEW, you can get (read) or set (write) properties with the NI-SWITCH Property
 Node.
 Refer to the niSwitch Property Node for more information.

Refer to niSwitch
 Properties
 for a complete listing of NI-SWITCH properties.

#### Attributes

In C and Visual Basic, attributes are accessed with the
 niSwitch_SetAttribute and
 niSwitch_GetAttribute functions. These functions correspond to
 a particular data type. For example, to set
 NISWITCH_ATTR_CONTINUOUS_SCAN (data type ViBoolean), use the
 niSwitch_SetAttributeViBoolean
 function.

Refer to NI-SWITCH
 Attributes
 for a complete listing of NI-SWITCH attributes.

Parent topic:

Programming Flow

<!--NI_TOPIC bundle=ni-switch path=setting-properties-and-attributes-before-read.html language=enus -->
## TOPIC 00614: Setting Properties and Attributes Before Reading Them

- bundle_id: `ni-switch`
- source_path: `setting-properties-and-attributes-before-read.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/setting-properties-and-attributes-before-read.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Properties and attributes are modified when you set them or when you call a configuration VI or function that sets them, respectively. It is important to set the properties or attributes or call any configuration VIs or functions before reading back any property or attribute values for the following

### Setting Properties and Attributes Before Reading Them

Properties and attributes are modified when you set them or when you call a configuration
 VI or function that sets them, respectively. It is important to set the properties or
 attributes or call any configuration VIs or functions before reading back any property
 or attribute values for the following reasons:

- Values read are coerced depending on the current configuration of the session. If
 you read a property or attribute value and then set other properties or attributes,
 the value read may no longer be valid.
- The driver verifies that the configuration of the device is valid at the time the
 property or attribute is read. It is possible to get an error when reading a
 property or attribute if the configuration is not valid at that point, even when a
 setting later could make it valid.
- Reading properties or attributes causes the driver to verify the current
 configuration. If you change some of the settings later, those settings need to be
 validated again.

Note

Parent topic:

Programming Flow

<!--NI_TOPIC bundle=ni-switch path=setting-source-and-configuration-channels.html language=enus -->
## TOPIC 00615: Setting Source and Configuration Channels

- bundle_id: `ni-switch`
- source_path: `setting-source-and-configuration-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/setting-source-and-configuration-channels.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use NI-SWITCH to set the channel type. Set a channel as a source channel to provide additional software protection against unintentional damage to your system. Set a channel as a configuration channel to complete connections supported by the architecture of the switch, but unsupported in sof

### Setting Source and Configuration Channels

source
 channel

configuration channel

Note

niSwitch_RelayControl

To edit a channel type, use the niSwitch Property
 Node
 or one of the
 niSwitch_SetAttribute
 functions.

The following figure represents a source channel (ab0) and a
 configuration channel (ch0) in the niSwitch Property Node.

[IMAGE alt='image' src='GUID-9957116B-E8BA-4988-AD2A-9FAADC3D0CCF-a5.gif']

#### Source Channels

Set a source channel to indicate to the driver that a signal source is connected to
 the channel. NI-SWITCH does not allow two user-defined source channels to be
 directly or indirectly connected.

Note

niSwitch_Disconnect

niSwitch_DisconnectAll

#### Configuration Channels

Set a configuration channel to allow NI-SWITCH to use the channel for internal path
 creation. Creating a column-to-column connection will fail in a matrix if a row
 channel is not set as a configuration channel.

Note

#### Creating a Route Example

Refer the matrix in the following figure, and complete the following steps to create
 a route connecting C0 and C2.

[IMAGE alt='image' src='GUID-EAA09D4B-31CB-416A-A876-5840A5A7D320-a5.gif']

1. Create a path between C0 and C2—Use the niSwitch Property Node or the
 appropriate niSwitch_SetAttribute function to set
 r0 as the configuration channel.
2. Create a route—Run the niSwitch Connect Channels VI or the
 niSwitch_Connect function with channel
 1 and channel 2 set to
 c0 and c2 , respectively.
3. Repeat steps 1 and 2 for rows r1 and r2 as
 configuration channels.

The following figures represent the routes you can create using R0, R1, and R2 as
 configuration channels, respectively.

[IMAGE alt='image' src='GUID-640BB857-4574-46F5-B903-2F58BF83D6B0-a5.gif']

[IMAGE alt='image' src='GUID-270EC352-CCCB-4E0E-BBF5-D4C8C8146332-a5.gif']

[IMAGE alt='image' src='GUID-49998CB7-CC50-4C20-9C4E-A3734E0A9837-a5.gif']

Parent topic:

Features

Related concepts:

- Immediate Operations
- Scanning
- Relay Forms

<!--NI_TOPIC bundle=ni-switch path=setting-up-and-configuring-the-ni-switchblock.html language=enus -->
## TOPIC 00616: Setting Up and Configuring the NI SwitchBlock

- bundle_id: `ni-switch`
- source_path: `setting-up-and-configuring-the-ni-switchblock.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/setting-up-and-configuring-the-ni-switchblock.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expand this book for information about installing and configuring the NI SwitchBlock.

### Setting Up and Configuring the NI SwitchBlock

Expand this book for information about installing and configuring the NI SwitchBlock.

Parent topic:

NI SwitchBlock Switching Considerations

<!--NI_TOPIC bundle=ni-switch path=settling-time.html language=enus -->
## TOPIC 00617: Settling Time

- bundle_id: `ni-switch`
- source_path: `settling-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/settling-time.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Settling time refers to the time required for a signal to reach a steady state after sending an actuation command to the relay. Steady state is determined by the required accuracy of the measurement. Highly accurate measurements require longer settling times than less accurate measurements. Settling

### Settling Time

Settling time refers to the time required for a signal to reach a steady state after
 sending an actuation command to the relay. Steady state is determined
 by the required accuracy of the measurement. Highly accurate measurements require longer
 settling times than less accurate measurements.

Settling time is an important consideration for solid-state relays with high path
 resistance and R-C time constants.

Some switch modules apply settling time only when relays are closed, not when relays are
 open.

For certain situations you may need to increase the default settling time. Refer to
 Adding Additional Settling Time for more information about increasing the default
 settling time. Refer to the Checking the Settling Time section of the Adding Additional
 Settling Time topic for more information about checking the default settling time of a
 switch.

Parent topic:

Relay Operation

Related concepts:

- Solid-State Relays (SSR)
- Adding Additional Settling Time

<!--NI_TOPIC bundle=ni-switch path=simulating-a-switch.html language=enus -->
## TOPIC 00618: Simulating a Switch

- bundle_id: `ni-switch`
- source_path: `simulating-a-switch.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/simulating-a-switch.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Simulate a switch using NI-SWITCH or Measurement & Automation Explorer (MAX) to develop, modify, and/or test an application without hardware. Using a simulated switch to test an application eliminates the risk of hardware damage. Additionally, you can use a simulated switch to evaluate an NI product

### Simulating a Switch

Tip

To simulate the NI SwitchBlock, refer to Simulating the NI SwitchBlock in
 MAX.

#### NI-SWITCH

Complete the following steps to create and configure a simulated switch using
 NI-SWITCH:

1. Run the niSwitch Initialize With
 Topology
 VI or the
 niSwitch_InitWithTopology 
 function.
2. Set the simulate parameter to Yes to
 ignore the resource name.
3. Specify the topology of the switch in the topology name 
 parameter. Refer to the switch module in Devices for a list of valid topology
 names.

Alternatively, you can run the niSwitch Initialize With
 Options
 VI or the
 niSwitch_InitWithOptions
 function.

#### MAX

Refer to the NI-DAQmx Simulated Devices topic in the
 Measurement & Automation Explorer Help for NI-DAQmx for
 detailed instructions about creating simulated switches.

Note

Parent topic:

Features

Related information:

- Simulate a SwitchBlock Device in NI MAX

<!--NI_TOPIC bundle=ni-switch path=simulating-ni-switchblock-max.html language=enus -->
## TOPIC 00619: Simulating the NI SwitchBlock in MAX

- bundle_id: `ni-switch`
- source_path: `simulating-ni-switchblock-max.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/simulating-ni-switchblock-max.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can simulate the NI SwitchBlock using Measurement & Automation Explorer (MAX) to develop, modify, and/or test an application without hardware. Using a simulated switch device to test an application eliminates the risk of hardware damage. Additionally, you can use a simulated switch device to eva

### Simulating the NI SwitchBlock in MAX

Tip

#### Simulating a Carrier

Refer to the NI-DAQmx Simulated Devices topic in the Measurement &
 Automation Explorer Help for NI-DAQmx for detailed instructions about
 creating a simulated NI SwitchBlock carrier. When creating an NI-DAQmx simulated
 device, NI SwitchBlock carriers are categorized under
 Switches.

#### Inserting, Removing, or Modifying Simulated Cards in a Simulated
 Carrier

Complete the following steps to insert or remove simulated NI SwitchBlock cards in a
 simulated carrier in MAX.

1. To launch the Simulated Cards panel, right-click the simulated carrier in the
 MAX device tree and select Insert or Remove Simulated
 Cards as shown in the following figure. [IMAGE alt='image' src='GUID-F81BBDD9-8F4E-4FFA-A74E-5EBC44B9C785-a5.gif']
2. For each slot in which you would like to insert a simulated card, select the
 card model you would like to simulate from the Card 
 drop-down list as shown in the following figure. [IMAGE alt='image' src='GUID-7911783A-72EC-416D-9ECD-B78B8E7BF9F4-a5.gif'] To leave a slot empty or
 remove a simulated card, select <None> from the
 Card list for that slot. If a multislot card is
 selected, the fields for the corresponding occupied slots are disabled. You can
 insert a multislot card only in slots that have an adequate number of empty
 slots after it. For example, you cannot insert a multislot card in the last slot
 of a carrier.
3. When you have selected the cards you would like to simulate, select
 OK to update the configuration tree in MAX, or select
 Cancel to revert to the existing configuration. Once
 the configuration is applied, the right pane in MAX displays the updated card
 configuration.

Simulated cards can only be inserted into a simulated carrier. Each simulated card is
 initially configured as a single-card device. Refer to *Configuring the
 NI SwitchBlock in MAX* to combine multiple simulated cards into a device.

Parent topic:

NI SwitchBlock Configuration Panel Help

Related concepts:

- Configuring the NI SwitchBlock in MAX

<!--NI_TOPIC bundle=ni-switch path=single-module-scanning-handshaking.html language=enus -->
## TOPIC 00620: Single Module Scanning - Handshaking

- bundle_id: `ni-switch`
- source_path: `single-module-scanning-handshaking.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/single-module-scanning-handshaking.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the trigger topic of the switch module in Devices for possible Trigger Input locations. Setup 3—Using Internal PXI Trigger Lines Setup 4—Using AUX Trigger Cable Connected to Front of PXI/PXI Express Switch Setup 3—Using Internal PXI Trigger Lines To handshake with a PXI/PXI Express switch,

### Single Module Scanning - Handshaking

Refer to the trigger topic of the switch module in Devices for possible
 Trigger Input locations.

- Setup 3—Using Internal PXI Trigger Lines
- Setup 4—Using AUX Trigger Cable Connected to Front of PXI/PXI Express Switch

#### Setup 3—Using Internal PXI Trigger Lines

To handshake with a PXI/PXI Express switch, you can use the internal PXI trigger
 lines of a PXI/PXI Express chassis. In this setup, no cable is used between the DMM
 and the PXI/PXI Express switch for triggering.

[IMAGE alt='image' src='GUID-E817A1E7-AD4E-432A-B44D-E3D68484C68A-a5.gif']

1. Set Trigger Input to
 TTLn in niSwitch Configure
 Trigger .
2. Set Scan Advanced Output to
 TTLm in niSwitch Configure
 Trigger .
3. Set Measurement Complete Destination to
 TTLn in niDMM Configure
 Measurement Complete Destination .
4. Set Trigger Source to
 TTLm in niDMM Configure
 Trigger .
5. Set Sample Trigger Source to
 TTLm in niDMM Configure
 Multi Point .

Refer to the switch module in Devices for possible Trigger
 Input and Scan Advanced Output locations.

#### Setup 4—Using AUX Trigger Cable Connected to Front of PXI/PXI Express
 Switch

Some PXI/PXI Express switches can receive their input trigger and send their scan
 advanced at the front panel or terminal block. This setup uses the AUX trigger cable
 to trigger the switch.

[IMAGE alt='image' src='GUID-052B90E9-633A-4259-ABD0-9EE190FFC742-a5.gif']

1. Connect the MC signal from the DMM to the external trigger input terminal on the
 front panel or in the terminal block of a PXI/PXI Express switch.
2. Connect the Ext Trig In signal of the DMM to the Scanner Advanced terminal on
 the front panel or in the terminal block of the same PXI/PXI Express
 switch.
3. Set Trigger Input to External in
 niSwitch Configure Trigger .
4. Set Scan Advanced Output to External in
 niSwitch Configure Trigger .
5. Set Measurement Complete Destination to
 External in niDMM Configure Measurement Complete
 Destination .
6. Set Trigger Source to External in
 niDMM Configure Trigger .
7. Set Sample Trigger Source to External in
 niDMM Configure Multi Point .

Refer to the switch module in Devices for possible Trigger
 Input and Scan Advanced Output locations.

Parent topic:

Single Module Scanning

<!--NI_TOPIC bundle=ni-switch path=single-module-scanning-synchronous.html language=enus -->
## TOPIC 00621: Single Module Scanning - Synchronous

- bundle_id: `ni-switch`
- source_path: `single-module-scanning-synchronous.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/single-module-scanning-synchronous.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the trigger topic of the switch module in Devices for possible Trigger Input locations. Setup 1—Using Internal PXI Trigger Lines Setup 2—Using AUX Trigger Cable Connected to Front of PXI/PXI Express Switch Setup 1—Using Internal PXI Trigger Lines All PXI/PXI Express switches can receive an

### Single Module Scanning - Synchronous

Refer to the trigger topic of the switch module in Devices for possible
 Trigger Input locations.

- Setup 1—Using Internal PXI Trigger Lines
- Setup 2—Using AUX Trigger Cable Connected to Front of PXI/PXI Express Switch

#### Setup 1—Using Internal PXI Trigger Lines

All PXI/PXI Express switches can receive an input trigger from PXI trigger lines of
 a PXI/PXI Express chassis. In this setup, no cable is used between the DMM and the
 PXI/PXI Express switch for triggering. The DMM sends its MC signal to the PXI/PXI
 Express switch through a PXI trigger line.

[IMAGE alt='image' src='GUID-700AED94-BD76-40EF-A494-28E726A5BD64-a5.gif']

1. Set Trigger Input to
 TTLn in niSwitch Configure
 Trigger .
2. Set Measurement Complete Destination in niDMM
 Configure Measurement to the same
 TTLn used in niSwitch Configure
 Trigger .

Refer to the switch module in Devices for possible Trigger
 Input locations.

#### Setup 2—Using AUX Trigger Cable Connected to Front of PXI/PXI Express
 Switch

Some PXI/PXI Express switches can receive an input trigger from the front panel or
 terminal block. This setup uses the AUX trigger cable to trigger the switch.

[IMAGE alt='image' src='GUID-E59B97CC-9AA9-419B-BA26-B29BAC4948A6-a5.gif']

1. Connect the MC signal from the DMM to the external trigger input terminal on the
 front panel or in the terminal block of a PXI/PXI Express switch.
2. Set Trigger Input to External in
 niSwitch Configure Trigger .
3. Set Measurement Complete Destination to
 External in niDMM Configure
 Measurement .

Refer to the switch module in Devices for possible Trigger
 Input locations.

Parent topic:

Single Module Scanning

<!--NI_TOPIC bundle=ni-switch path=single-module-scanning.html language=enus -->
## TOPIC 00622: Single Module Scanning

- bundle_id: `ni-switch`
- source_path: `single-module-scanning.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/single-module-scanning.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI-SWITCH supports single module scanning for PXI/PXI Express switches in NI-SWITCH and NI-DAQmx. Some devices may not support scanning. Refer to your device book for more information about supported features. NI-SWITCH To scan individual switches using NI-SWITCH, you can write a scan list or use

### Single Module Scanning

Note

#### NI-SWITCH

To scan individual switches using NI-SWITCH, you can write a scan list or use the
 programming examples.

#### NI-DAQmx

For information about developing a single switch scanning application using NI-DAQmx,
 refer to the NI-DAQmx Help.

#### Determining the Scanning Setup

The scanning setup is dependent on your hardware and triggering scheme. Based on your
 hardware and triggering scheme requirements, choose one of the following scanning
 setups:

#### PXI/PXI Express Scanning—Synchronous

- Setup 1—Using Internal PXI Trigger Lines
- Setup 2—Using AUX Trigger Cable Connected to Front of PXI/PXI Express
 Switch

#### PXI/PXI Express Scanning—Handshaking

- Setup 3—Using Internal PXI Trigger Lines
- Setup 4—Using AUX Trigger Cable Connected to Front of PXI/PXI Express
 Switch

Parent topic:

Scanning NI Switches with NI Digital Multimeters

Related concepts:

- Scan Lists
- NI-SWITCH Programming Examples
- Single Module Scanning - Synchronous
- Single Module Scanning - Handshaking

<!--NI_TOPIC bundle=ni-switch path=software-trigger-scanning.html language=enus -->
## TOPIC 00623: Software Trigger Scanning

- bundle_id: `ni-switch`
- source_path: `software-trigger-scanning.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/software-trigger-scanning.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The niSwitch Send Software Trigger VI and the niSwitch_SendSoftwareTrigger function allow you to advance to the next entry in a scan list through a software command. You can use this software command instead of sending triggers on the trigger input terminal. The switch can still optionally send a tr

### Software Trigger Scanning

niSwitch_SendSoftwareTrigger

niSwitch_SendSoftwareTrigger

Note

[IMAGE alt='image' src='GUID-4FFEE50F-084C-4DC2-988E-CB8CB756578C-a5.gif']

Parent topic:

Scanning Fundamentals

Related concepts:

- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=solid-state-relays-ssr.html language=enus -->
## TOPIC 00624: Solid-State Relays (SSR)

- bundle_id: `ni-switch`
- source_path: `solid-state-relays-ssr.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/solid-state-relays-ssr.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Solid-state relays incorporate an LED to control the gate of a photo-sensitive metal-oxide-semiconductor field-effect transistor (MOSFET). This relay structure provides an isolation barrier between the control circuitry and the load allowing the relay to switch high voltage. It takes about 1 ms (dep

### Solid-State Relays (SSR)

Solid-state relays incorporate an LED to control the gate of a photo-sensitive
 metal-oxide-semiconductor field-effect transistor (MOSFET). This relay structure
 provides an isolation barrier between the control circuitry and the load allowing the
 relay to switch high voltage. It takes about 1 ms (depending on the relay) for the LED
 to power on, and 0.5 ms for the LED to power off. These times restrict the switching
 speed of this relay, yet SSRs are faster than electromechanical relays.

The following figure shows a diagram of a typical solid-state relay. The digital control
 signal powers an LED that turns the MOSFET circuitry on and off. The LED is required to
 isolate the drive circuitry from the DUT signal.

[IMAGE alt='image' src='GUID-12F233FD-512D-47BA-915B-144602961D9F-a5.gif']

#### Related Information

Electromechanical Relays

Parent topic:

Relay Types

Related concepts:

- Electromechanical Relays

<!--NI_TOPIC bundle=ni-switch path=switch-relay-maintenance-ni-switch-health-center.html language=enus -->
## TOPIC 00625: Switch Relay Maintenance with the NI Switch Health Center

- bundle_id: `ni-switch`
- source_path: `switch-relay-maintenance-ni-switch-health-center.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/switch-relay-maintenance-ni-switch-health-center.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the NI Switch Health Center for switch relay maintenance using the following relay tests to determine whether a relay is functional or will need to be replaced. Integrated Relay Continuity Test The NI Switch Health Center tests relays by sending a signal through a combination of routes o

### Switch Relay Maintenance with the NI Switch Health Center

You can use the NI Switch Health Center for switch relay maintenance using the following
 relay tests to determine whether a relay is functional or will need to be replaced.

#### Integrated Relay Continuity Test

The NI Switch Health Center tests relays by sending a signal through a combination of
 routes on each card to verify the condition of each relay. When the test has
 finished, each relay is determined to be functional, stuck open, stuck closed, or
 unknown. A relay status can be reported as unknown if relay conditions may not be
 determinable because of specific combinations of failures. If the integrated relay
 test is aborted before completion, some relays may be untested.

#### Integrated Relay Resistance
 Test

Changes in contact resistance over time can indicate that a relay is approaching, or
 has reached, end-of-life. The NI Switch Health Center tests for changes in
 resistance using the integrated relay resistance test. When you run a relay test
 with the NI Switch Health Center, you can view the resistance change across
 individual relays to determine whether a relay is close to end-of-life.

The integrated relay resistance test reports the change in resistance relative to a
 baseline resistance measured at the time the device was manufactured. A large change
 in resistance from the baseline indicates that the relay will soon need to be
 replaced. If the change in resistance reaches 1 Ω, NI recommends that you replace
 the relay.

Note

#### Relay Count Tracking

Relay count tracking can also be used to determine relay lifetime and mechanical
 lifetime by maintaining an accurate count of relay cycles. All devices offer onboard
 relay count tracking that you can view in the NI Switch Health Center or the NI
 Switch Soft Front Panel. Relay counts are stored on the switch hardware, allowing
 you to monitor relay cycle count if hardware is moved between systems. Using this
 information, you can perform preventive relay maintenance, detect inefficient
 switching code, and in some applications, extend the life of your card by balancing
 the relay utilization across the card. If monitored over time, you can use relay
 count tracking to anticipate when a relay will fail.

Users can also
 programmatically access the relay count tracking feature to identify specific relays
 that have a greater cycle count, and thus shift their testing procedure to utilize
 relays with a lower cycle count.

You can read current relay counts from the
 hardware at any time using the NI Switch Health Center, NI Switch Soft Front Panel,
 or NI-SWITCH driver, and integrate it into your test code to supply operator
 warnings if relays exceed their electrical life expectancy.

Parent topic:

NI Switch Health Center Help

Related concepts:

- Testing Relays with the NI Switch Health Center
- Accessing the NI Switch Health Center
- About the NI Switch Health Center

<!--NI_TOPIC bundle=ni-switch path=switch-relay-replacement.html language=enus -->
## TOPIC 00626: Switch Relay Replacement

- bundle_id: `ni-switch`
- source_path: `switch-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/switch-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the NI Switches Help at Start Programs National Instruments NI-SWITCH Documentation NI Switches Help for detailed relay manufacturer information and relay replacement instructions. After completing the replacement procedure, refer to the NI Switches Help for information about resetting a re

### Switch Relay Replacement

NI Switches Help

Start

»

Programs

»

National Instruments

»

NI-SWITCH

»

Documentation

»

NI Switches Help

NI
 Switches Help

Note

NI Switches Help

If most of the relays on one of the cards need to be replaced at the same time or if one
 of the boards is damaged, you can contact NI support and arrange to send the entire card
 back to NI for relay replacement.

Parent topic:

NI Switch Health Center Help

<!--NI_TOPIC bundle=ni-switch path=switch-system-requirements.html language=enus -->
## TOPIC 00627: NI-SWITCH Operating Requirements

- bundle_id: `ni-switch`
- source_path: `switch-system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/switch-system-requirements.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `reference`
- source_description: Your system must meet the following minimum requirements to run and use NI-SWITCH. Supported Operating Systems Windows 11 or Windows 10 (64-bit) Windows Server 2022 (64-bit) Windows Server 2019 (64-bit) Windows Server 2016 (64-bit) RedHat Enterprise Linux 8 or 9.0 openSUSE Leap 15.3 or 15.4 Ubuntu 2

### NI-SWITCH Operating Requirements

Your system must meet the following minimum requirements to run and use NI-SWITCH.

- Supported Operating Systems
  - Windows 11 or Windows 10 (64-bit)
  - Windows Server 2022 (64-bit)
  - Windows Server 2019 (64-bit)
  - Windows Server 2016 (64-bit)
  - RedHat Enterprise Linux 8 or 9.0
  - openSUSE Leap 15.3 or 15.4
  - Ubuntu 22.04 or 20.04

<!--NI_TOPIC bundle=ni-switch path=switching-capacitive-loads.html language=enus -->
## TOPIC 00628: Switching Capacitive Loads

- bundle_id: `ni-switch`
- source_path: `switching-capacitive-loads.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/switching-capacitive-loads.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a switch closes, a transient current flows to charge the capacitance. This current may be substantially higher than the steady-state current through the system and cause contact welding. Even though the voltage and steady-state currents are within the switch specifications, damage may occur bec

### Switching Capacitive Loads

When a switch closes, a transient current flows to charge the capacitance. This current
 may be substantially higher than the steady-state current through the system and cause
 contact welding. Even though the voltage and steady-state currents are within the switch
 specifications, damage may occur because of this high inrush current.

To limit inrush current, an impedance, such as a resistor, should be placed in
 series between C<sub>int2</sub> and C<sub>external</sub>. This resistor
 isolates the unwanted effects of the load capacitance and limits damage to the relay
 contacts. A protection resistance, R<sub>p</sub>, should be selected such that

V/R<sub>p</sub>< switching current rating of the relay

The following figures illustrate the use of the protection resistor R<sub>p.</sub>

#### Resistor R<sub>p</sub> Added to Limit Current into
 C<sub>external</sub>

|  |
| --- |

#### Current Graph Comparison

|  |
| --- |

The energy associated with the inrush currents in these two circuits can be expressed
 as

E<sub>without protection</sub>=
 ½(C<sub>int2</sub>+C<sub>ext</sub>)V<sup>2</sup>=525
 nJ

and

E<sub>with protection</sub>= ½(C<sub>int2</sub>)V<sup>2</sup>=25
 nJ

Note

#### Related Topics

Inrush Current

Parent topic:

General Switching Considerations

Related concepts:

- Inrush Current

<!--NI_TOPIC bundle=ni-switch path=switching-capacity.html language=enus -->
## TOPIC 00629: Switching Capacity

- bundle_id: `ni-switch`
- source_path: `switching-capacity.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/switching-capacity.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Signal levels through a switch must account for the following specifications: Switching Voltage Switching Current Switching Power The following figure shows the valid operating range defined by these limits.

### Switching Capacity

Signal levels through a switch must account for the following specifications:

- Switching Voltage
- Switching Current
- Switching Power

The following figure shows the valid operating range defined by these limits.

[IMAGE alt='image' src='GUID-F5FD9329-9B0D-48F8-9972-99401E4A14D2-a5.gif']

Parent topic:

General Switching Considerations

Related concepts:

- Switching Voltage
- Switching Current
- Switching Power

<!--NI_TOPIC bundle=ni-switch path=switching-current.html language=enus -->
## TOPIC 00630: Switching Current

- bundle_id: `ni-switch`
- source_path: `switching-current.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/switching-current.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switching current is the maximum rated current that can flow through the switch as it makes or breaks a contact. Switching active currents results in arcing that can damage the contacts of electromechanical relays. A minimum current specification indicates the smallest current that can reliably flow

### Switching Current

Switching current is the maximum rated current that can flow through the switch as it
 makes or breaks a contact. Switching active currents results in arcing that can damage
 the contacts of electromechanical relays. A minimum current specification indicates the
 smallest current that can reliably flow through the switch.

Parent topic:

Switching Capacity

Related concepts:

- Arcing
- Relay Life
- Electromechanical Relays

<!--NI_TOPIC bundle=ni-switch path=switching-inductive-loads.html language=enus -->
## TOPIC 00631: Switching Inductive Loads

- bundle_id: `ni-switch`
- source_path: `switching-inductive-loads.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/switching-inductive-loads.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When inductive loads are connected to the relays, a large counter electromotive force may occur when the relay actuates because of the energy stored in the load. These flyback voltages can severely damage the relay contacts and greatly shorten the relay life. Limit these flyback voltages at your ind

### Switching Inductive Loads

When inductive loads are connected to the relays, a large counter electromotive force may
 occur when the relay actuates because of the energy stored in the load. These flyback
 voltages can severely damage the relay contacts and greatly shorten the relay life.

Limit these flyback voltages at your inductive load by installing a flyback diode for DC
 loads or a metal oxide varistor for AC loads, as shown in the following figure.

[IMAGE alt='image' src='GUID-046349EA-BB1A-4C98-AA6B-D04F9E6A3350-a5.gif']

Refer to the switch module documentation for information on preparing the switch module
 to properly handle inductive loads.

Parent topic:

General Switching Considerations

Related concepts:

- Relay Life

<!--NI_TOPIC bundle=ni-switch path=switching-power.html language=enus -->
## TOPIC 00632: Switching Power

- bundle_id: `ni-switch`
- source_path: `switching-power.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/switching-power.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switching power is the limit on the combined open-contact voltage and closed-contact current of a signal in the switch. Switching Power = Switching Voltage x Switching Current Switching high-power signals causes high-energy arcing at the electromechanical contacts during actuation, reducing the usef

### Switching Power

Switching power is the limit on the combined open-contact voltage and closed-contact
 current of a signal in the switch.

Switching Power = Switching Voltage x Switching Current

Switching high-power signals causes high-energy arcing at the electromechanical contacts
 during actuation, reducing the useful life of the switch.

Parent topic:

Switching Capacity

Related concepts:

- Arcing
- Relay Life

<!--NI_TOPIC bundle=ni-switch path=switching-voltage.html language=enus -->
## TOPIC 00633: Switching Voltage

- bundle_id: `ni-switch`
- source_path: `switching-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/switching-voltage.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Switching voltage refers to the maximum signal voltage that the switch module can safely maintain. Switching voltage is defined from channel-to-ground and from channel-to-channel. Channel-to-ground is the voltage potential between the signal line and the grounded chassis. Channel-to-channel is the v

### Switching Voltage

Note

rms

Read Me First: Safety and Electromagnetic Compatibility

Parent topic:

Switching Capacity

<!--NI_TOPIC bundle=ni-switch path=synchronous-scanning.html language=enus -->
## TOPIC 00634: Synchronous Scanning

- bundle_id: `ni-switch`
- source_path: `synchronous-scanning.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/synchronous-scanning.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI recommends using handshaking when using NI switch and DMM products. If using other brands of hardware that do not have a trigger input, NI recommends using synchronous mode. With synchronous scanning, the DMM takes a measurement and generates a digital pulse—the measurement complete (MC) signal.

### Synchronous Scanning

NI recommends using handshaking when using NI switch and DMM products. If using other
 brands of hardware that do not have a trigger input, NI recommends using synchronous
 mode.

interval

Note

[IMAGE alt='image' src='GUID-793E7D45-C46E-4EE5-A5BE-2C5FC463800B-a5.gif']

The following figure represents a synchronous scanning timing diagram.

[IMAGE alt='image' src='GUID-D6E3FC6A-49E7-4C32-929C-51D0AE5B4F25-a5.gif']

where

M = measurement

WFT = wait for trigger

S&S = switch and settle

Parent topic:

Scanning Fundamentals

Related concepts:

- Handshaking

<!--NI_TOPIC bundle=ni-switch path=system-configuration-options-for-the-ni-switc.html language=enus -->
## TOPIC 00635: System Configuration Options for the NI SwitchBlock

- bundle_id: `ni-switch`
- source_path: `system-configuration-options-for-the-ni-switc.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/system-configuration-options-for-the-ni-switc.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure your NI SwitchBlock system as one NI SwitchBlock device or as multiple NI SwitchBlock devices. One NI SwitchBlock Device The one NI SwitchBlock device method routes signals within a single NI SwitchBlock relay card in an NI SwitchBlock carrier or between multiple NI SwitchBlock rel

### System Configuration Options for the NI SwitchBlock

You can configure your NI SwitchBlock system as one NI SwitchBlock device or as multiple
 NI SwitchBlock devices.

#### One NI SwitchBlock Device

The one NI SwitchBlock device method routes signals within a single NI SwitchBlock
 relay card in an NI SwitchBlock carrier or between multiple NI SwitchBlock relay
 cards within the same NI SwitchBlock carrier that have been combined into a single
 NI SwitchBlock device.

The following figure shows multiple relay cards in one NI SwitchBlock carrier that
 have been combined into a single NI SwitchBlock device.

|  |  |
| --- | --- |

#### Multiple NI SwitchBlock Devices

The multiple NI SwitchBlock device method routes signals between multiple
 NI SwitchBlock devices within the same NI SwitchBlock carrier or between multiple
 NI SwitchBlock devices within multiple NI SwitchBlock carriers connected with the NI
 2806 Expansion Bridge.

The following figure shows multiple relay cards in one NI SwitchBlock carrier that
 are combined into multiple NI SwitchBlock devices.

|  |  |
| --- | --- |

The following figure shows multiple relay cards in multiple NI SwitchBlock carriers
 combined using the NI 2806 Expansion Bridge.

[IMAGE alt='image' src='GUID-28D62D01-4B38-4C1B-90C7-0E42CFEEA918-a5.gif']

Note

Parent topic:

Programming the NI SwitchBlock in NI-SWITCH and NI-DAQmx

<!--NI_TOPIC bundle=ni-switch path=testing-relays-ni-switch-health-center.html language=enus -->
## TOPIC 00636: Testing Relays with the NI Switch Health Center

- bundle_id: `ni-switch`
- source_path: `testing-relays-ni-switch-health-center.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/testing-relays-ni-switch-health-center.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: To test relays with the NI Switch Health Center, complete the following steps: Disconnect any cables or interchangeable test interfaces (ITAs) from the device(s). Safety interlock circuitry on the NI SwitchBlock relay cards prevents the relay test from running until all external connections have bee

### Testing Relays with the NI Switch Health Center

To test relays with the NI Switch Health Center, complete the following steps:

1. Disconnect any cables or interchangeable test interfaces (ITAs) from the device(s).
 Note Safety
 interlock circuitry on the NI SwitchBlock relay cards prevents the relay test
 from running until all external connections have been disconnected.
2. Launch the NI Switch Health Center from either MAX or the Start menu. From MAX,
 complete one of the following: Right-click on a resource and select NI Switch Health
 Center
 Select a resource and click NI Switch Health
 Center in the task bar.The NI Switch Health Center launches, initializes, and begins testing
 relays in the selected resource. 
 From the Start Menu, complete the following.If you have only one resource present, the relay test starts
 automatically. If you have more than one resource installed, select the
 resource you want to test in the listbox from the NI Switch Health
 Center - Setup dialog box that displays.
 Click the Start button. The NI Switch Health
 Center initializes and begins testing relays in the selected
 resource.
3. The relay test displays the following information: Note Some devices
 may not support the integrated relay resistance test. Click
 Abort at any time to stop the test and release the
 resource for use.
  - Relay functionality using the integrated relay continuity test
  - Relay contact resistance changes using the integrated relay resistance
 test
  - Relay cycle counts using relay count tracking
4. Click the Start button to repeat tests as necessary.

After completion of each relay test, you can generate a report documenting the results of
 the test.

Parent topic:

NI Switch Health Center Help

Related concepts:

- Accessing the NI Switch Health Center
- Generating Reports with the NI Switch Health Center
- Switch Relay Maintenance with the NI Switch Health Center

<!--NI_TOPIC bundle=ni-switch path=the-ni-switchblock-carrier-and-the-analog-bus.html language=enus -->
## TOPIC 00637: The NI SwitchBlock Carrier and the Analog Bus

- bundle_id: `ni-switch`
- source_path: `the-ni-switchblock-carrier-and-the-analog-bus.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/the-ni-switchblock-carrier-and-the-analog-bus.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: All NI SwitchBlock systems contain at least two components: one NI SwitchBlock carrier and one or more NI SwitchBlock relay cards. Each relay card contains a single switch matrix of rows and columns. If there are multiple relay cards in one NI SwitchBlock carrier, individual matrices can be column e

### The NI SwitchBlock Carrier and the Analog Bus

All NI SwitchBlock systems contain at least two components: one NI SwitchBlock carrier
 and one or more NI SwitchBlock relay cards. Each relay card contains a single switch
 matrix of rows and columns. If there are multiple relay cards in one NI SwitchBlock
 carrier, individual matrices can be column expanded using the analog bus lines to create
 large matrices.

The backplane of the NI SwitchBlock carrier includes 16 analog bus lines that can be used
 to route signals between relay cards. Analog bus relays are located between the rows of
 the relay cards and their respective analog bus line on the backplane of the NI
 SwitchBlock carrier. The Following figure represents an NI SwitchBlock carrier with two
 relay cards that have been combined into a single NI SwitchBlock device.

[IMAGE alt='image' src='GUID-D15D2A37-54F7-4797-87B8-06BB89216066-a5.gif']

The NI SwitchBlock carrier has analog bus expansion connectors on the left and right
 sides that can join with the NI 2806 Expansion Bridge to enable analog bus sharing
 between multiple NI SwitchBlock carriers in a PXI chassis. Multiple NI 2806 Expansion
 Bridges can be used to expand the analog bus to up to four NI SwitchBlock carriers in a
 single 18-slot NI PXI chassis for a total of 24 NI SwitchBlock relay cards. The
 following figures represent two NI SwitchBlock carriers with an NI 2806 Expansion
 Bridge. You can route a signal between NI SwitchBlock carriers using the NI
 2806 Expansion Bridge as shown in the first figure. You must remove the analog bus cover
 from the NI PXI-2800 carrier before inserting the expansion bridge, as shown in the
 second figure.

[IMAGE alt='image' src='GUID-F83AF92B-E80A-491F-A52A-B2A146A3A850-a5.gif']

Parent topic:

Programming the NI SwitchBlock in NI-SWITCH and NI-DAQmx

<!--NI_TOPIC bundle=ni-switch path=thermal-emf-and-offset-voltage.html language=enus -->
## TOPIC 00638: Thermal EMF and Offset Voltage

- bundle_id: `ni-switch`
- source_path: `thermal-emf-and-offset-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/thermal-emf-and-offset-voltage.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When two, dissimilar metals are joined a voltage is created. This voltage is known as the thermal electromotive force (EMF) or the Seebeck voltage. The Seebeck voltage is dependent on the temperature of the junction and the composition of the metals joined. The specific metal-to-metal junctions resu

### Thermal EMF and Offset Voltage

When two, dissimilar metals are joined a voltage is created. This voltage is known as
 the thermal electromotive force (EMF) or the Seebeck voltage. The Seebeck voltage is
 dependent on the temperature of the junction and the composition of the metals joined.
 The specific metal-to-metal junctions result in specific temperature coefficients
 (µV/°C), also known as Seebeck coefficients. The following table lists the most common
 metals and their respective Seebeck coefficients.

| Junction | µV/°C |
| --- | --- |
| Copper-Copper | <0.3 |
| Copper-Gold | 0.5 |
| Copper-Silver | 0.5 |
| Copper-Brass | 3 |
| Copper-Nickel | 10 |
| Copper-Lead-Tin Solder | 1-3 |
| Copper-Aluminum | 5 |
| Copper-Kovar | 40 |
| Copper-Copper Oxide | >500 |

#### Thermal EMF in Switches

The leads of electromechanical relays are usually composed of metal alloys, most
 often nickel-iron alloy, while the PCB of a switch module is usually composed of
 copper or copper alloy. The junction between these two, dissimilar metals creates a
 thermocouple, as illustrated in the following figure.

[IMAGE alt='image' src='GUID-5124FBDF-2430-4648-89E5-AC57090AC7F3-a5.gif']

Note

A signal path can transverse a single relay or multiple relays. The sum of all the
 thermocouples in a signal path is expressed as the thermal EMF. Thermal EMF can be
 specified as single path (single wire) or differential path thermal EMF. The
 following figure illustrates thermal EMF measured in a single path.

[IMAGE alt='image' src='GUID-0FFE2ED4-B92E-4557-8D95-32CAD38C7AB7-a5.gif']

The following figure illustrates thermal EMF measured in a differential path.

[IMAGE alt='image' src='GUID-86E634DC-4EFF-48B7-AF97-C81BE43AA30E-a5.gif']

#### Accuracy

When measuring voltage with a switch and a DMM, be sure to account for thermal EMF in
 the overall system accuracy calculation.

For example, if the DMM has an accuracy of 4 µV and the switch has a differential
 path thermal EMF of 3 µV, the overall system accuracy can be calculated as follows:

√(4² + 3²) = 5 µV

Thus, when measuring a 50 mV signal, the overall system accuracy is 0.01%.

Note

Parent topic:

General Switching Considerations

Related concepts:

- Thermocouple Measurement

<!--NI_TOPIC bundle=ni-switch path=thermocouple-measurement.html language=enus -->
## TOPIC 00639: Thermocouple Measurement

- bundle_id: `ni-switch`
- source_path: `thermocouple-measurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/thermocouple-measurement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2527 (NI 2527) and the NI TB-2627 can measure thermocouples. NI software can convert a thermocouple voltage to the thermocouple temperature. For example code, visit ni.com/examples and enter 2527 in the Search field. When measuring thermocouples, be sure to account for error in the

### Thermocouple Measurement

Tip

ni.com/examples

When measuring thermocouples, be sure to account for error in the measurements. The
 total error in thermocouple measurement is the sum of the system error (determined by
 the thermal EMF of the NI 2527 and the CJC temperature of the NI TB-2627) and the
 thermocouple error (determined by the type of thermocouple used).

#### Determining the System Error

To determine the system error for the NI 2527/TB-2627, first calculate the thermal
 EMF error of the NI 2527 using the following equation.

|  | EEMF = [(T+1 – T) / (V+1 – V)] × VEMF | (1) |
| --- | --- | --- |
| where | EEMF represents the thermal EMF error of the NI 2527 |  |
|  | T is the temperature being measured, in degrees Celsius |  |
|  | T+1 is (T + 1 °C) |  |
|  | V is the voltage that corresponds to T |  |
|  | V+1 is the voltage that corresponds to T+1 |  |
|  | VEMF represents the thermal EMF of the NI 2527 |  |

Note

T

+1

vs.

V

+1

T

+1

NI PXI/PXIe-2527 Specifications

EMF

After you have determined the thermal EMF error using Equation 1, calculate the
 system error using the following equation.

|  | ES = EEMF + ECJC | (2) |
| --- | --- | --- |
| where | ES represents the system error of the NI 2527/TB-2627 |  |
|  | EEMF represents the error due to thermal EMF of the NI 2527 |  |
|  | ECJC represents the error due to CJC temperature sensor of the NI TB-2627 |  |

#### Example

Measuring a K-type thermocouple at 200 °C with a CJC temperature of 25 °C, the system
 error of the NI 2527/TB-2627 is calculated in the following example.

Assuming typical thermal EMF (2.5 µV), first calculate the error due to thermal EMF
 using Equation 1.

| EEMF | = | [(201 °C – 200 °C)/(8.178 µV – 8.138 µV)] × 0.0025 µV |
| --- | --- | --- |
|  | = | 0.063 °C |

Note

V

+1

The Temperature Handbook

To determine the system error, add the error due to thermal EMF to the error due to
 the CJC temperature sensor using Equation 2.

| ES | = | 0.063 °C + 0.5 °C |
| --- | --- | --- |
|  | = | 0.563 °C |

#### Determining the Thermocouple Error

Independent of the NI 2527/TB-2627 system, thermocouple error is the greater of the
 following values: ± a temperature range or ± a percent of the measurement.

In the example, a standard grade K-type thermocouple is used to measure 200 °C.
 The Temperature Handbook lists the error for a standard grade
 K-type thermocouple as ±2.2 °C or ±0.75% of the measurement temperature. Because
 ±0.75% of 200 °C (±1.5 °C) is less than ±2.2 °C, the error of a standard grade
 K-type thermocouple is ±2.2 °C.

#### Determining the Total Error

The total error in thermocouple measurement is the sum of the system error and the
 thermocouple error. Use the following equation to determine the total error in
 thermocouple measurement.

|  | ET = ES + ETh | (3) |
| --- | --- | --- |
| where | ET represents the total error in thermocouple measurement |  |
|  | ES represents the system error |  |
|  | ETh represents the thermocouple error |  |

To determine the total error in thermocouple measurement in the example, add the
 thermocouple error to the system error using Equation 3, as illustrated in the
 following calculation.

| ET | = | 0.56 °C + 2.2 °C |
| --- | --- | --- |
|  | = | 2.76 °C |

Assuming typical thermal EMF, the total error in thermocouple measurement at 200 °C
 for the NI 2527/TB-2627 with a K-type thermocouple is ±2.76 °C.

Parent topic:

NI PXI/PXIe-2527

<!--NI_TOPIC bundle=ni-switch path=topologies.html language=enus -->
## TOPIC 00640: Topologies

- bundle_id: `ni-switch`
- source_path: `topologies.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/topologies.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: A switch topology is an organizational representation of the channels and relays on a switch module. Topologies often show the default connections for the relays on a module and label the channel names. Some switch modules can use multiple topologies or a variation of a topology. Some terminal block

### Topologies

A switch topology is an organizational representation of the channels and relays on a
 switch module. Topologies often show the default connections for the relays on a module
 and label the channel names. Some switch modules can use multiple topologies or a
 variation of a topology. Some terminal blocks or accessories may force the switch module
 to use a given topology or set of topologies.

NI-SWITCH supports the following topologies:

- General-Purpose
- Multiplexer
- Matrix
- Transfer Switches (Topology)
- Fault Insertion Units

Refer to Initialization for more information about setting the topology of the switch
 module.

Parent topic:

Fundamentals

Related concepts:

- General-Purpose Topologies
- Multiplexer
- Matrix
- Transfer Switches (Topology)
- Fault Insertion Units
- Initialization

<!--NI_TOPIC bundle=ni-switch path=transfer-switches-topology.html language=enus -->
## TOPIC 00641: Transfer Switches (Topology)

- bundle_id: `ni-switch`
- source_path: `transfer-switches-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/transfer-switches-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: An RF transfer switch (DPDT) has four ports (1–4) and two states (reset and set). In the reset state, port 1 is connected to port 2 and port 3 is connected to port 4. In the set state, port 1 is connected to port 3 and port 2 is connected port 4. Using a Transfer Switch The following figures illustr

### Transfer Switches (Topology)

An RF transfer switch (DPDT) has four ports (1–4) and two states (reset and set). In the
 reset state, port 1 is connected to port 2 and port 3 is connected to port 4. In the set
 state, port 1 is connected to port 3 and port 2 is connected port 4.

#### Using a Transfer Switch

The following figures illustrate example uses of a transfer switch.

- Testing two DUTs with different instruments [IMAGE alt='image' src='GUID-0B909D26-3806-47D0-9662-959B4D09D60F-a5.gif']
- Testing antennas [IMAGE alt='image' src='GUID-CAE2BA81-555B-4AF6-AB88-0F2DB843E639-a5.gif']
- Testing multiple filters with the NI PXI-2596 [IMAGE alt='image' src='GUID-0ADF7445-B8C7-4CFE-B6F4-B99D84CC5E61-a5.gif']

Parent topic:

Topologies

Related concepts:

- NI PXI-2596

<!--NI_TOPIC bundle=ni-switch path=transfer-switches.html language=enus -->
## TOPIC 00642: Transfer Switches

- bundle_id: `ni-switch`
- source_path: `transfer-switches.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/transfer-switches.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: An RF transfer switch (DPDT) is a type of armature relay that is composed of four ports (1–4) in one of two states (reset and set). In the reset state, port 1 is connected to port 2 and port 3 is connected to port 4. In the set state, port 1 is connected to port 3 and port 2 is connected port 4. The

### Transfer Switches

An RF transfer switch (DPDT) is a type of armature relay that is composed of four ports
 (1–4) in one of two states (reset and set). In the reset state, port 1 is connected to
 port 2 and port 3 is connected to port 4. In the set state, port 1 is connected to port
 3 and port 2 is connected port 4. The reset and set states of an RF transfer switch are
 illustrated in the following figures:

[IMAGE alt='image' src='GUID-FABA845A-3EA6-4D70-B6DA-0C3DBF7B1527-a5.gif']

#### Transfer Switch Operation Cycle

The following figures illustrate the operation cycle of a transfer switch with 2-coil
 latching:

1. The transfer switch begins in the reset state. [IMAGE alt='image' src='GUID-02609609-40B7-4644-8006-2E8B8310FC43-a5.gif']
2. Current flows through the lower coil to change the transfer switch to the set
 state. [IMAGE alt='image' src='GUID-0086DE34-3CCA-4479-96EE-218229D69097-a5.gif']
3. The transfer switch is now in the set state. [IMAGE alt='image' src='GUID-1155CBAC-FEE5-44E7-BCEA-9D736BE3AC41-a5.gif']
4. Current flows through the upper coil to change the transfer switch to the reset
 state. [IMAGE alt='image' src='GUID-527BC0F7-AD36-4FC1-B4F0-75AE7FCCEE56-a5.gif']
5. The transfer switch ends in the reset state. [IMAGE alt='image' src='GUID-02609609-40B7-4644-8006-2E8B8310FC43-a5.gif']

#### Related Topics

Armature Relays

Parent topic:

Armature Relays

Related concepts:

- Armature Relays

<!--NI_TOPIC bundle=ni-switch path=user-manual-welcome.html language=enus -->
## TOPIC 00643: NI-SWITCH User Manual

- bundle_id: `ni-switch`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI-SWITCH User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI-SWITCH
 User Manual

The NI-SWITCH User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download NI-SWITCH
- NI-SWITCH Release Notes
- Interactive Activation Guide
- NI-SWITCH Soft Front Panels
- NI-SWITCH Properties Reference
- NI-SWITCH LabVIEW API Reference
- NI-SWITCH C API Reference
- NI-SWITCH .NET API Reference
- NI Learning Center

<!--NI_TOPIC bundle=ni-switch path=using-ni-switch-in-labview.html language=enus -->
## TOPIC 00644: Using NI-SWITCH in LabVIEW

- bundle_id: `ni-switch`
- source_path: `using-ni-switch-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/using-ni-switch-in-labview.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using the NI LabVIEW ADE to manage your code development and that you are familiar with the ADE. To develop an NI-SWITCH application in LabVIEW, follow these general steps: Open a new or existing LabVIEW virtual instrument (VI). From the Functions palette, select Meas

### Using NI-SWITCH in LabVIEW

This topic assumes that you are using the NI LabVIEW ADE to manage your code development
 and that you are familiar with the ADE.

To develop an NI-SWITCH application in LabVIEW, follow these general steps:

1. Open a new or existing LabVIEW virtual instrument (VI).
2. From the Functions palette, select
 Measurement I/O»NI-SWITCH to access the NI-SWITCH
 API.
3. Select the VIs that you want to use and add them to the block diagram to build your
 application.

#### Example Programs

Use the NI Example Finder to search or browse NI-SWITCH examples. Search examples by
 keyword to find a particular device or measurement VI. To browse the NI-SWITCH
 examples available in LabVIEW, launch LabVIEW, and select Help»Find
 Examples. To browse examples by task, select Hardware
 Input and Output»Modular Instruments»NI-SWITCH (Switches); to browse
 examples by directory structure, select instr»niSwitch.

For more information about NI-SWITCH examples, refer to NI-SWITCH Programming
 Examples.

Parent topic:

Creating an application with NI-SWITCH

Related concepts:

- NI-SWITCH Programming Examples

<!--NI_TOPIC bundle=ni-switch path=using-ni-switch-in-labwindows-cvi.html language=enus -->
## TOPIC 00645: Using NI-SWITCH in LabWindows/CVI

- bundle_id: `ni-switch`
- source_path: `using-ni-switch-in-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/using-ni-switch-in-labwindows-cvi.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using the LabWindows/CVI ADE to manage your code development and that you are familiar with the ADE. To develop an NI-SWITCH application in LabWindows/CVI, follow these general steps: Open an existing or new project file. Load the NI-SWITCH function panel at IVI\Drive

### Using NI-SWITCH in LabWindows/CVI

This topic assumes that you are using the LabWindows/CVI ADE to manage your code
 development and that you are familiar with the ADE.

To develop an NI-SWITCH application in LabWindows/CVI, follow these general steps:

1. Open an existing or new project file.
2. Load the NI-SWITCH function panel at IVI\Drivers\NISWITCH .
3. Use the function panel to navigate the function hierarchy and to generate function
 calls with the proper syntax and variable values.

Note

.lib

\VXIpnp

IVI\

#### Example Programs

For more information about NI-SWITCH examples, refer to NI-SWITCH Programming
 Examples.

Note

Parent topic:

Creating an application with NI-SWITCH

Related concepts:

- NI-SWITCH Programming Examples

<!--NI_TOPIC bundle=ni-switch path=using-ni-switch-in-visual-basic.html language=enus -->
## TOPIC 00646: Using NI-SWITCH in Visual Basic

- bundle_id: `ni-switch`
- source_path: `using-ni-switch-in-visual-basic.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/using-ni-switch-in-visual-basic.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using the Microsoft Visual Basic ADE to manage your code development and that you are familiar with the ADE. To develop an NI-SWITCH application in Visual Basic, follow these general steps: Open an existing or new Visual Basic project. Create files necessary for your

### Using NI-SWITCH in Visual Basic

This topic assumes that you are using the Microsoft Visual Basic ADE to manage your code
 development and that you are familiar with the ADE.

To develop an NI-SWITCH application in Visual Basic, follow these general steps:

1. Open an existing or new Visual Basic project.
2. Create files necessary for your application and add them to the project.
3. Add a reference to the National Instruments Switch Library (NISWITCH), which is part
 of the NI-SWITCH DLL. In Visual Basic 6.0, select the
 Project»References menu option and National Instruments
 Switch Library (NISWITCH). If you do not see NISWITCH listed there, click
 Browse and locate NISWITCH_32.dll in
 your IVI\Bin directory.
4. Use the Object Browser <F2> to find function prototypes and constants.
5. Add NI-SWITCH function calls to your application.
6. Run your application by clicking Run .

#### Example Programs

To load an example project with Visual Basic 6.0 or later, select
 File»Open Project, then select the .vbp
 file of your choice.

For more information about NI-SWITCH examples, including example locations, refer to
 NI-SWITCH Programming Examples.

#### Special Considerations

#### String Passing

In Visual Basic, variables of data type String do not need special modifications to
 be passed to NI-SWITCH functions. Visual Basic automatically appends a null
 character to the end of a string before passing it (by reference, since strings
 cannot be passed by value in Visual Basic) to a procedure or function.

#### Parameter Passing

By default, Visual Basic passes parameters by reference. Prepend the ByVal keyword if
 you need to pass by value.

Parent topic:

Creating an application with NI-SWITCH

Related concepts:

- NI-SWITCH Programming Examples

<!--NI_TOPIC bundle=ni-switch path=using-ni-switch-in-visual-c-c.html language=enus -->
## TOPIC 00647: Using NI-SWITCH in Visual C/C++

- bundle_id: `ni-switch`
- source_path: `using-ni-switch-in-visual-c-c.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/using-ni-switch-in-visual-c-c.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic assumes that you are using the Microsoft Visual C or C++ ADE to manage your code development and that you are familiar with the following ADEs: Microsoft Visual C++ 6.0 Microsoft Visual Studio 2010 Using NI-SWITCH in Microsoft Visual C++ 6.0 To develop an NI-SWITCH application with Micros

### Using NI-SWITCH in Visual C/C++

This topic assumes that you are using the Microsoft Visual C or C++ ADE to manage your code
 development and that you are familiar with the following ADEs:

- Microsoft Visual C++ 6.0
- Microsoft Visual Studio 2010

#### Using NI-SWITCH in Microsoft Visual C++ 6.0

To develop an NI-SWITCH application with Microsoft Visual C++ 6.0, follow these general
 steps:

1. Open an existing or new Visual C/C++ project to manage your application code.
2. Create source code files of type .c (C) or .cpp 
 (C++).
3. Add the source code files to the project.
4. Add the following code in the source code files: #include
 "niswitch.h"
5. Add the NI-SWITCH include and library files to the project. <IVIROOTDIR32> is an alias
 to a specific National Instruments file folder location. Refer to the NI-SWITCH Readme File for
 more information about installed file locations.
  1. Select Project»Settings»C/C++»Preprocessor»Additional include
 directories , and add the paths, separated by a semicolon, to the
 niswitch.h and visa.h files. The
 niswitch.h and visa.h files are located in the
 <IVIROOTDIR32>\Include and
 <VXIPNPPATH>\WinNT\include directories, respectively.
  2. Select Project»Settings»Link»General»Object/Library Modules , and
 add niswitch.lib .
  3. Select Project»Settings»Link»Input»Additional library path , and add
 the path to the niswitch.lib file. The niswitch.lib file is
 located in the <IVIROOTDIR32>\Lib\msc or the
 <IVIROOTDIR32>\Lib x64\msc directory.
6. Build your application using the appropriate programming flow steps.

#### Using NI-SWITCH in Microsoft Visual Studio 2010

To develop an NI-SWITCH application with Microsoft Visual Studio 2010, follow these general
 steps:

1. Open an existing or new Visual C/C++ project to manage your application code.
2. Create source code files of type .c (C) or .cpp 
 (C++).
3. Add the source code files to the project.
4. Add the following code in the source code files: #include
 "niswitch.h"
5. Add the NI-SWITCH include and library files to the project. <IVIROOTDIR32> is an alias
 to a specific National Instruments file folder location. Refer to the NI-SWITCH Readme File for
 more information about installed file locations.
  1. Select Project»Properties»Configuration Properties»C/C++»General»Additional
 Include Directories , add the paths, separated by a semicolon, to the
 niswitch.h and visa.h files. The
 niswitch.h and visa.h files are located in the
 <IVIROOTDIR32>\Include and
 <VXIPNPPATH>\WinNT\Visa\include directories, respectively.
  2. Select Project»Properties»Configuration Properties»Linker»Input»Additional
 Dependencies , and add niswitch.lib .
  3. Select Project»Properties»Configuration Properties»Linker»General»Additional
 Library Directories , and add the path to the niswitch.lib file.
 The niswitch.lib file is located in the
 <IVIROOTDIR32>\Lib\msc or the <IVIROOTDIR32>\Lib
 x64\msc directory.
6. Build your application using the appropriate programming flow steps.

#### Microsoft Visual C Examples

Installed examples for Visual C/C++ are in the NI-SWITCH Readme File.

The C examples were built and tested using Microsoft Visual C++ 6.0 with Service Pack 5.0.
 These examples are console-based with no graphical interface.

To build the examples in Microsoft Visual C++ 6.0 using the Microsoft NMAKE utility, complete
 the following steps:

1. Go to the directory for the particular example you want to use.
2. Run the VCVARS32.BAT batch file (located in the \bin directory of the MSVC compiler) to set
 up the environment variables for command line usage if they are not already set. You might need
 to increase the initial environment size of the DOS box to accommodate the added environment
 variables.
3. To build an example run nmake CFG="Win32 Debug" . The executable is built
 to the debug subdirectory by default.

Parent topic:

Creating an application with NI-SWITCH

Related concepts:

- Programming Flow

<!--NI_TOPIC bundle=ni-switch path=using-ni-switches-in-ivi.html language=enus -->
## TOPIC 00648: Using NI Switches in IVI

- bundle_id: `ni-switch`
- source_path: `using-ni-switches-in-ivi.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/using-ni-switches-in-ivi.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create an IVI logical name and a corresponding driver session to use National Instruments switch modules in IVI. Complete the following steps to create an IVI logical and a corresponding driver session. Open Measurement & Automation Explorer (MAX). Expand IVI Drivers in the MAX configuration tree. C

### Using NI Switches in IVI

Create an IVI logical name and a corresponding driver session to use National Instruments
 switch modules in IVI. Complete the following steps to create an IVI logical and a
 corresponding driver session.

1. Open Measurement & Automation Explorer (MAX).
2. Expand IVI Drivers in the MAX configuration tree.
3. Create a new driver session.
  1. Right-click Driver Sessions in the configuration
 tree, and select Create New (case-sensitive) . The
 configuration panel opens in the configuration window.
  2. Complete the following steps to configure the new driver session.
    1. Select the Software tab, and select
 niSwitch from the Software Module
 listbox.
    2. Select the Hardware tab, and select the
 switch module you want to use from the Hardware Asset listbox. Note To create a new hardware asset, click
 Create New to the right of the
 Hardware Asset listbox.
    3. Select the General tab, and select
 Don't Simulate from the Simulate With
 listbox.
    4. In the Driver Setup textbox, enter the driver setup string for the
 switch module you want to use. Refer to Determining the
 Driver Setup String for more information about driver
 setup strings.
4. Create a new logical name.
  1. Right-click Logical Names in the configuration tree,
 and select Create New (case-sensitive) . The
 configuration panel opens in the configuration window.
  2. To configure the new logical name, select the driver session that you
 created in step 3 from the Driver Session listbox.
 Note To view the properties of the driver session you
 have selected, click Go To to the right of the
 Driver Session listbox.
5. To save the IVI configuration, click Save IVI Configuration 
 at the top of the configuration view. If you decide not to save your changes, click
 Revert to revert to the previous configuration.

#### Determining the Driver Setup String

Complete the following steps to determine the driver setup string for the switch
 module.

1. Determine the topology name.
  1. Open the NI Switches Help file.
  2. Select the Contents tab.
  3. Expand the Devices book, and select the switch
 module you want to use. The device overview for the switch module is
 displayed in the help window.
  4. In the device overview, the Operation Modes table(s) lists the topology
 and software names for each supported topology. The topology name is the
 first software name listed in the table not the
 constant name in parenthesis. For example, if you want to use the NI
 PXI-2501 in the 48x1 Mux mode, the topology name is "2501/1-Wire 48x1
 Mux" not 
 " NISWITCH_TOPOLOGY_2501_1_WIRE_48X1_MUX ."
2. Using the topology name, determine the driver setup string.
  - NI-DAQmx devices —The driver setup string is
 topology:<topology
 name> . If you are using the NI PXI-2501 in the
 48x1 Mux mode, for example, the driver setup string is
 topology:2501/1-Wire 48x1 Mux .

Parent topic:

Getting Started

<!--NI_TOPIC bundle=ni-switch path=using-the-analog-bus-on-an-ni-switchblock-car.html language=enus -->
## TOPIC 00649: Using the Analog Bus on an NI SwitchBlock Carrier

- bundle_id: `ni-switch`
- source_path: `using-the-analog-bus-on-an-ni-switchblock-car.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/using-the-analog-bus-on-an-ni-switchblock-car.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the following sections for information about the analog bus on your NI SwitchBlock carrier and how to use it. Basics Each carrier has an analog bus that you can use to make connections between cards that compose a multicard device, between devices in the same carrier, or between devices in

### Using the Analog Bus on an NI SwitchBlock Carrier

Refer to the following sections for information about the analog bus on your
 NI SwitchBlock carrier and how to use it.

#### Basics

Each carrier has an analog bus that you can use to make connections between cards
 that compose a multicard device, between devices in the same carrier, or between
 devices in different carriers when the NI 2806 expansion bridge is installed.

NI SwitchBlock devices contain analog bus channels used to connect to the analog bus
 on the carrier. To connect a row on a card to the analog bus on the carrier, connect
 the row to the analog bus channel of the same number on the device.

Note

Note

Because all cards in a carrier share the analog bus, multiple devices cannot connect
 to the same analog bus line simultaneously unless they are both of the same wire
 mode and you allow multiple devices to connect to the same analog bus lines using
 the Analog Bus Sharing
 Enable
 property or the
 NISWITCH_ATTR_ANALOG_BUS_SHARING_ENABLE
 attribute.

Note

niSwitch_RelayControl

#### Connecting Signals Between Cards in a Multicard Device

You can use analog bus channels to route signals between the cards that compose a
 multicard device. The following image illustrates signal connections to connect
 channels c0 and c43 in a multicard device composed
 of two cards.

[IMAGE alt='image' src='GUID-D15D2A37-54F7-4797-87B8-06BB89216066-a5.gif']

Complete the following steps to connect signals between cards in the same device:

1. Determine which channels you want to connect.
2. Set all channels between the channels selected in Step 1, including the analog
 bus channels, as reserved for routing. Note You can set a
 channel as reserved for routing only if it is not already in use and its
 Analog Bus Sharing
 Enable
 property is set to FALSE.
3. Connect the channels selected in Step 1 through any channels necessary to route
 the signals. Refer to the previous figure for an example of routing to connect
 c0 to c43 in a device composed of two
 NI 2810 cards.

#### Connecting Signals Between Devices

You can use the analog bus to route signals between multiple NI SwitchBlock devices
 with the same wire mode, whether the devices are installed in the same carrier or
 installed in separate carriers connected by the NI 2806 expansion bridge. The
 following image illustrates signal connections to connect channel
 c44 in a multicard device installed in one carrier to channel
 c0 in a single-card device installed in an adjacent carrier
 connected by the NI 2806 expansion bridge.

[IMAGE alt='image' src='GUID-1B644B13-2251-4C62-85E0-BD1D29F6CD32-a5.gif']

Complete the following steps to connect signals between multiple devices:

1. Verify that the devices are of the same wire mode.
2. If the devices you would like to connect are in separate carriers, verify that
 the NI 2806 expansion bridge has been installed.
3. Determine which analog bus channels, such as ab0 , you want to
 connect signals to on each of the devices.
4. Enable an analog bus channel on each of the devices to be shared across devices
 using the Analog Bus Sharing
 Enable
 property or the
 NISWITCH_ATTR_ANALOG_BUS_SHARING_ENABLE 
 attribute. Refer to the Basics section of this topic to determine which analog
 bus channel on each device corresponds to the analog bus line you would like to
 share. Note Analog bus channels can be shared only when the
 corresponding analog bus lines are not already in use. The analog bus
 channels on a 1-wire device connect to a single analog bus line each, while
 the analog bus channels on a 2-wire device connect to two lines each.
5. Reserve for routing any channels needed to connect the channels selected in
 Step 3 to the analog bus channel that will share the analog bus line. Note A channel that shares an analog bus line cannot be reserved
 for routing, and a channel that has been reserved for routing cannot share
 an analog bus line.
6. For each device, connect the channels selected in Step 3 to the analog bus
 channel that will share the analog bus line through any channels selected in
 Step 4. For example, to connect c44 on Device 1 to
 c0 on Device 2 in the system shown in the previous image,
 you would need to route signals between c44 and
 ab2 on Device 1 and between c0 and
 ab2 on Device 2.

#### Related Information:

- Analog Bus Sharing Enable
 Property
- Analog Bus Sharing Enable
 Attribute
- niSwitch
 Properties

Parent topic:

NI SwitchBlock Programming Considerations

Related concepts:

- Immediate Operations

<!--NI_TOPIC bundle=ni-switch path=voltage-standing-wave-ratio-vswr.html language=enus -->
## TOPIC 00650: Voltage Standing Wave Ratio (VSWR)

- bundle_id: `ni-switch`
- source_path: `voltage-standing-wave-ratio-vswr.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/voltage-standing-wave-ratio-vswr.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Any impedance mismatches along a transmission line causes partial reflection of the propagating signals. The impedance difference determines the magnitude of the reflection. The length of a mismatched section determines the lowest signal frequencies that reflect from the section. VSWR is a measure o

### Voltage Standing Wave Ratio (VSWR)

Any impedance mismatches along a transmission line causes partial reflection of the
 propagating signals. The impedance difference determines the magnitude of the
 reflection. The length of a mismatched section determines the lowest signal frequencies
 that reflect from the section. VSWR is a measure of that signal reflection.

With an incident sine wave into the switch module, some of the signal reflects down the
 line. This reflected wave interferes with the incident wave. VSWR is the ratio of
 maximum to minimum amplitude in the resulting interference wave, as shown in the
 following formula:

[IMAGE alt='image' src='GUID-50E42B2B-FF09-4AFD-AA1E-F4D661DD786D-a5.gif']

where p is the reflection coefficient

Reflections can also be represented as a logarithmic ratio of the reflected signal to
 the input signal. This ratio is called return loss:

| RL (dB) | = 10 log (PIn / PReflected) |
| --- | --- |
|  | = 20 log (VIn / VReflected) |
|  | = -20 log (VReflected / VIn) |
|  | = -20 log \|p\| |

Parent topic:

RF Switching Considerations

<!--NI_TOPIC bundle=ni-switch path=writing-a-software-trigger-scanning-program.html language=enus -->
## TOPIC 00651: Writing a Software Trigger Scanning Program

- bundle_id: `ni-switch`
- source_path: `writing-a-software-trigger-scanning-program.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/writing-a-software-trigger-scanning-program.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: To write a software trigger scanning program, complete the following steps: Set the topology of the switch module using the niSwitch Initialize With Topology VI or the niSwitch_InitWithTopology function. Set the trigger input (triggerInput) parameter to Software Trigger using the niSwitch Configure

### Writing a Software Trigger Scanning Program

To write a software trigger scanning program, complete the following steps:

1. Set the topology of the switch module using the niSwitch Initialize With
 Topology
 VI or the
 niSwitch_InitWithTopology 
 function.
2. Set the trigger input ( triggerInput )
 parameter to Software Trigger using the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger 
 function.
3. Set the number of times the switch cycles through the scan list, once or infinitely,
 using the niSwitch Set Continuous
 Scan
 VI or the
 niSwitch_SetContinuousScan 
 function.
4. Set up the list of connections using the niSwitch Configure Scan
 List
 VI or the
 niSwitch_ConfigureScanList 
 function. Refer to Scan Lists for syntax information.
5. Initiate the scan using the niSwitch Initiate
 Scan
 VI or the
 niSwitch_InitiateScan 
 function. The first entry in the scan list is executed and the switch waits for
 software triggers to execute the subsequent entries in the list.
6. Execute each set of connections in the scan list by calling the niSwitch Send
 Software
 Trigger
 VI and the
 niSwitch_SendSoftwareTrigger 
 function.
7. Terminate the scanning operation using the niSwitch Abort
 Scan
 VI or the
 niSwitch_AbortScan 
 function.
8. Release resources using the niSwitch
 Close VI or
 the
 niSwitch_close 
 function.

Note

Parent topic:

Scanning

Related concepts:

- Scan Lists
- NI-SWITCH Programming Examples
