# NI DOCUMENT BUNDLE: ni-switch

<!--NI_BUNDLE_CHUNK bundle=ni-switch start=251 end=500 -->
<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2558-front-panel.html language=enus -->
## TOPIC 00251: NI PXI-2558 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2558-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2558-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2558 front panel.

### NI PXI-2558 Front Panel

The following figure illustrates the NI PXI-2558 front panel.

[IMAGE alt='image' src='GUID-D36EA746-1BFB-4AD0-97A7-C25C33960D97-a5.gif']

Parent topic:

NI PXI-2558

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2558-hardware-diagram.html language=enus -->
## TOPIC 00252: NI PXI-2558 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2558-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2558-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2558.

### NI PXI-2558 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2558.

[IMAGE alt='image' src='GUID-8A7B00B1-C7CC-4BF1-8F63-D2A4BD8B7440-a5.gif']

Parent topic:

NI PXI-2558

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2558-quad-spdt-topology.html language=enus -->
## TOPIC 00253: NI PXI-2558 Quad SPDT Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2558-quad-spdt-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2558-quad-spdt-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2558 in the quad SPDT general-purpose topology. Making a Connection Call the niSwitch Connect Channels VI or the niSwitch_Connect function to connect channels in this topology. If applicable, you must call the niSwitch Disconnect Channels VI or the niSwitch

### NI PXI-2558 Quad SPDT Topology

The following figure represents the NI PXI-2558 in the quad SPDT general-purpose
 topology.

|  |
| --- |
|  |

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

x

x

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between NO 1 and COM1 and the other between NC 1 and
 COM1:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters no1 and com1 .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 no1 and com1 .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters nc1 and com1 .

When scanning the NI PXI-2558, a typical scan list entry might be
 no1->com1;. This entry routes the signal connected to NO 1
 to COM 1.

Parent topic:

NI PXI-2558

Related concepts:

- General-Purpose Topologies
- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2558-triggering.html language=enus -->
## TOPIC 00254: NI PXI-2558 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2558-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2558-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2558. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2558 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2558.

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

The following table lists valid scan advanced outputs for the NI PXI-2558.

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

NI PXI-2558

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2558.html language=enus -->
## TOPIC 00255: NI PXI-2558

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2558.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2558.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2558 is a 4-channel, general-purpose switch module for the PXI bus that can carry 75 Ω RF signals up to 2.5 GHz. The NI PXI-2558 is composed of 4-SPDT relays. Operation Modes The following table lists the supported topology of the NI PXI-2558 and possible operation modes. Topology Softwar

### NI PXI-2558

The NI PXI-2558 is a 4-channel, general-purpose switch module for the PXI bus that can
 carry 75 Ω RF signals up to 2.5 GHz. The NI PXI-2558 is composed of 4-SPDT relays.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2558 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 4-SPDT | 2558/4-SPDT(NISWITCH_TOPOLOGY_2558_4_SPDT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- RF Switching Considerations
- NI PXI-2558 Quad SPDT Topology
- Topologies
- Operation Modes
- NI PXI-2548 Quad SPDT Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2559-dual-terminated-spdt-topology.html language=enus -->
## TOPIC 00256: NI PXI-2559 Dual Terminated SPDT Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2559-dual-terminated-spdt-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2559-dual-terminated-spdt-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2559 in the dual terminated SPDT general-purpose topology. The terminators on the NI PXI-2559 are rated for 1.5 W at 25 °C. When operating at ambient temperatures greater than 25 °C, a termination power derating applies. Refer the NI PXI-2559 Specificatio

### NI PXI-2559 Dual Terminated SPDT Topology

The following figure represents the NI PXI-2559 in the dual terminated SPDT
 general-purpose topology.

|  |
| --- |
|  |

Caution

NI PXI-2559 Specifications

cannot

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

x

x

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between NO 1 and COM1 and the other between NC 1 and
 COM1:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters no1 and com1 .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 no1 and com1 .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters nc1 and com1 .

When scanning the NI PXI-2559, a typical scan list entry might be
 no1->com1;. This entry routes the signal connected to NO 1
 to COM 1.

Parent topic:

NI PXI-2559

Related concepts:

- General-Purpose Topologies
- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2559-front-panel.html language=enus -->
## TOPIC 00257: NI PXI-2559 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2559-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2559-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2559 front panel.

### NI PXI-2559 Front Panel

The following figure illustrates the NI PXI-2559 front panel.

[IMAGE alt='image' src='GUID-778FFB40-5C65-4CDD-9502-452186F644D2-a5.gif']

Parent topic:

NI PXI-2559

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2559-hardware-diagram.html language=enus -->
## TOPIC 00258: NI PXI-2559 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2559-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2559-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2559.

### NI PXI-2559 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2559.

[IMAGE alt='image' src='GUID-BE3B913A-6D61-4DCC-A17A-B835D042EF18-a5.gif']

Parent topic:

NI PXI-2559

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2559-triggering.html language=enus -->
## TOPIC 00259: NI PXI-2559 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2559-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2559-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2559. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2559 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2559.

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

The following table lists valid scan advanced outputs for the NI PXI-2559.

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

NI PXI-2559

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2559.html language=enus -->
## TOPIC 00260: NI PXI-2559

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2559.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2559.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2559 is a 2-channel, general-purpose switch module for the PXI bus that can carry 75 Ω RF signals up to 2.5 GHz. The NI PXI-2559 is composed of two terminated SPDT relays. Operation Modes The following table lists the supported topology of the NI PXI-2559 and possible operation modes. Top

### NI PXI-2559

The NI PXI-2559 is a 2-channel, general-purpose switch module for the PXI bus that can
 carry 75 Ω RF signals up to 2.5 GHz. The NI PXI-2559 is composed of two terminated SPDT
 relays.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2559 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Terminated 2-SPDT | 2559/Terminated 2-SPDT(NISWITCH_TOPOLOGY_2559_TERMINATED_2_SPDT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- RF Switching Considerations
- NI PXI-2559 Dual Terminated SPDT Topology
- Topologies
- Operation Modes
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2564-16-spst-topology.html language=enus -->
## TOPIC 00261: NI PXI-2564 16-SPST Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2564-16-spst-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2564-16-spst-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2564 in the 16-SPST topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to close the relay of channel 2, call niSwitch_Connect(vi, "ch2", "com2"). To open the relay

### NI PXI-2564 16-SPST Topology

The following figure represents the NI PXI-2564 in the 16-SPST topology.

[IMAGE alt='image' src='GUID-BAC9394F-D2CD-4043-AE4B-FA0A8B854E1A-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to close the relay of channel 2, call niSwitch_Connect(vi, "ch2",
 "com2"). To open the relay of channel 2, call niSwitch_Disconnect(vi,
 "ch2", "com2").

When scanning the NI PXI-2564, a typical scan list entry could be
 ch2->com2;. This entry closes the relay between CH2 and COM2.

#### Pinout

The following figure identifies the pins for the NI PXI-2564 in the 16-SPST topology.

[IMAGE alt='image' src='GUID-31042A58-B9DA-4435-A1C5-029A7BC4B56D-a5.gif']

Parent topic:

NI PXI-2564

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2564-8-dpst-topology.html language=enus -->
## TOPIC 00262: NI PXI-2564 8-DPST Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2564-8-dpst-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2564-8-dpst-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2564 in the 8-DPST topology. Making a Connection Both the scanning command, ch2->com2;, and the immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters ch2 and com0, result in the following connections: signal conn

### NI PXI-2564 8-DPST Topology

The following figure represents the NI PXI-2564 in the 8-DPST topology.

[IMAGE alt='image' src='GUID-83F37D3A-2720-4C83-8752-02DCABE8863B-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com2;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in the
 following connections:

signal connected to CH2W0 is routed to COM2W0

signal connected to CH2W1 is routed to COM2W1

#### Pinout

The following figure identifies the pins for the NI PXI-2564 in the 8-DPST topology.

[IMAGE alt='image' src='GUID-9B9C7337-7AAF-473F-9902-FA02CAFE6516-a5.gif']

Parent topic:

NI PXI-2564

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2564-hardware-diagram.html language=enus -->
## TOPIC 00263: NI PXI-2564 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2564-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2564-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2564.

### NI PXI-2564 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2564.

[IMAGE alt='image' src='GUID-931599BB-FD5C-49AC-A20E-32297FA7940D-a5.gif']

Parent topic:

NI PXI-2564

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2564-relay-replacement.html language=enus -->
## TOPIC 00264: NI PXI-2564 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2564-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2564-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2564 uses electromechanical armature relays. Refer to the following tables for information about ordering replacement relays. Relay Manufacturer Part Number Fujitsu JY-5H-K Relay Kit Part Number National Instruments (16 relays) 780262-01 Complete the following sets of steps to disassemble

### NI PXI-2564 Relay Replacement

The NI PXI-2564 uses electromechanical armature relays.

Refer to the following tables for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| Fujitsu | JY-5H-K |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (16 relays) | 780262-01 |

Complete the following sets of steps to disassemble your module and replace a failed
 relay.

1. Ground yourself using a grounding strap or a ground connected to your PXI chassis.
 Note Properly grounding yourself prevents damage to your module
 from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table for
 relay locations. [IMAGE alt='image' src='GUID-BD0FE536-7F93-4CB9-A7EA-8A4A76B2DCF9-a5.gif'] 
 Channel Name
 Relay NameCH0
 K0CH1
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
 K12CH13
 K13CH14
 K14CH15
 K15
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
- Fine pick
- Isopropyl alcohol
- Cotton swabs

If you have a surface mount rework station, replace the relay as you would any other
 surface mount part. Otherwise, complete the following steps to replace the
 relay:

1. Use the soldering iron and solder wick to remove as much solder from the relay
 pads as possible. Do not leave the soldering iron on any lead for more than 5
 seconds. Note If it is necessary to reapply the soldering iron
 to the pad, allow the connection to cool completely before reapplying the
 soldering iron.
2. Apply heat to the pads one at a time, and use the pick to gently pry the relay
 pins from the pads. Make sure that the solder is molten before prying. Caution Using excessive force on a soldered pad can result in
 lifting the PCB trace and ruining the board.
3. Remove the relay.
4. Clean the pads with isopropyl alcohol and cotton swabs.
5. Place the new relay on the PCB pads and solder.
6. Remove the excess flux with isopropyl alcohol and cotton swabs. Caution Do not use flux remover to clean the
 board after relay replacement.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2564

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2564-triggering.html language=enus -->
## TOPIC 00265: NI PXI-2564 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2564-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2564-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2564 can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2564. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigg

### NI PXI-2564 Triggering

The NI PXI-2564 can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2564.

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

The following table lists valid scan advanced outputs for the NI PXI-2564.

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

NI PXI-2564

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2564.html language=enus -->
## TOPIC 00266: NI PXI-2564

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2564.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2564.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2564 is a 16-channel general-purpose power relay module for the PXI platform. The NI PXI-2564 is composed of 16 electromechanical armature latching SPST relays. For certain applications, you may need to increase the default settling time. Refer to Adding Additional Settling Time for more

### NI PXI-2564

The NI PXI-2564 is a 16-channel general-purpose power relay module for the PXI platform.
 The NI PXI-2564 is composed of 16 electromechanical armature latching SPST relays.

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2564 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 16-SPST | 2564/16-SPST(NISWITCH_TOPOLOGY_2564_16_SPST) |  |  |
| 8-DPST | 2564/8-DPST(NISWITCH_TOPOLOGY_2564_8_DPST) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- Electromechanical Relays
- Armature Relays
- Relay Forms
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2564 16-SPST Topology
- NI PXI-2564 8-DPST Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2565-16-spst-topology.html language=enus -->
## TOPIC 00267: NI PXI-2565 16-SPST Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2565-16-spst-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2565-16-spst-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2565 in the 16-SPST topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to close the relay of channel 2, call niSwitch_Connect(vi, "ch2", "com2"). To open the relay

### NI PXI-2565 16-SPST Topology

The following figure represents the NI PXI-2565 in the 16-SPST topology.

[IMAGE alt='image' src='GUID-B8276EFC-AB93-406E-9DC8-59AC1D9A8853-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to close the relay of channel 2, call niSwitch_Connect(vi, "ch2",
 "com2"). To open the relay of channel 2, call niSwitch_Disconnect(vi,
 "ch2", "com2").

When scanning the NI PXI-2565, a typical scan list entry could be
 ch2->com2;. This entry routes the signal connected to CH2 to COM2.

#### Pinout

The following figure identifies the pins for the NI PXI-2565 in the 16-SPST topology.

[IMAGE alt='image' src='GUID-11E4DEB3-10A5-499E-9702-39BF00A3B266-a5.gif']

Parent topic:

NI PXI-2565

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2565-flyback-voltage-protection.html language=enus -->
## TOPIC 00268: NI PXI-2565 Flyback Voltage Protection

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2565-flyback-voltage-protection.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2565-flyback-voltage-protection.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When inductive loads are connected to the relays, a large counter electromotive force may occur at relay switching time because of the energy stored in the inductive load. These flyback voltages can severely damage the relay contacts and significantly shorten the life of the relay. You can limit fly

### NI PXI-2565 Flyback Voltage Protection

When inductive loads are connected to the relays, a large counter electromotive force may
 occur at relay switching time because of the energy stored in the inductive load. These
 flyback voltages can severely damage the relay contacts and significantly shorten the
 life of the relay.

Caution

Before installing your switch module in the PXI chassis, install the diode/varistor by
 performing the steps described in the following sections.

#### Disassemble the Module

To disassemble the module, complete the following steps, referring to the parts
 locator diagram as needed.

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your module from electrostatic discharge.
2. Loosen the four screws that fasten the relay module to the carrier module and
 front panel. 
 1
 Carrier Module2
 Solder Location forFlyback Voltage Protection
 Device3
 Relay Module4
 Screws5
 Plastic Insulator Cover6
 Relay and Socket7
 Ribbon Cable
3. Remove the plastic insulator cover.
4. Lift up the card and disconnect the ribbon cable from the relay module.

#### Install the Diode/Varistor

Complete the following steps to install the diode/varistor.

1. Remove solder, as necessary, from the diode/varistor locations.
2. Insert the diode/varistor into the appropriate location, labeled
 RV x , where x corresponds to the
 channel number.
3. Solder and trim the leads.

#### Reassemble the Module

Complete the Disassemble the Module steps in reverse order to reassemble your
 module.

Parent topic:

NI PXI-2565

Related concepts:

- Switching Inductive Loads

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2565-hardware-diagram.html language=enus -->
## TOPIC 00269: NI PXI-2565 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2565-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2565-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2565.

### NI PXI-2565 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2565.

[IMAGE alt='image' src='GUID-D561123A-F507-4DAB-B6D3-51EA90B41E7C-a5.gif']

Parent topic:

NI PXI-2565

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2565-relay-replacement.html language=enus -->
## TOPIC 00270: NI PXI-2565 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2565-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2565-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2565 uses socketed electromechanical relays. Refer to the following tables for information about ordering replacement relays. Relay Manufacturer Part Number Aromat (NAiS) DSP1a-DC5V Relay Kit Part Number National Instruments (16 relays) 777880-01 Complete the following sets of steps to di

### NI PXI-2565 Relay Replacement

The NI PXI-2565 uses socketed electromechanical relays.

Refer to the following tables for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| Aromat (NAiS) | DSP1a-DC5V |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (16 relays) | 777880-01 |

Complete the following sets of steps to disassemble your module, replace a failed relay,
 and reassemble your module.

#### Disassemble the Module

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your module from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table
 for relay locations. NI PXI-2565 Relay Map 
 [IMAGE alt='image' src='GUID-9479F783-BCF7-4642-81C7-3FA4790EE759-a5.gif'] 
 ChannelName
 RelayName
 ChannelName
 RelayName
 ChannelName
 RelayName
 ChannelName
 RelayNameCH0
 K0
 CH4
 K4
 CH8
 K8
 CH12
 K12CH1
 K1
 CH5
 K5
 CH9
 K9
 CH13
 K13CH2
 K2
 CH6
 K6
 CH10
 K10
 CH14
 K14CH3
 K3
 CH7
 K7
 CH11
 K11
 CH15
 K15
3. Remove the four screws that fasten the NI PXI-2565 relay daughtercard to the
 main board.
4. Lift up the card as shown in the figure below. 1
 Carrier Module2
 Solder Location forFlyback Voltage Protection
 Device3
 Relay Module4
 Screws5
 Insulator6
 Relay and Socket7
 Ribbon Cable

#### Replace the Relay

1. Remove the relay by gently applying force.
2. Before inserting the new relay, match the direction of the relay and the
 socket.
3. Insert the relay, making sure the relay is properly seated and the socket hooks
 the top of the relay.

#### Reassemble the Module

Complete the Disassemble the Module steps in reverse order to reassemble your
 module.

Parent topic:

NI PXI-2565

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2565-triggering.html language=enus -->
## TOPIC 00271: NI PXI-2565 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2565-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2565-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2565. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2565 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2565.

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

The following table lists valid scan advanced outputs for the NI PXI-2565.

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

NI PXI-2565

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2565.html language=enus -->
## TOPIC 00272: NI PXI-2565

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2565.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2565.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2565 is a 16-channel general-purpose switch module for the PXI platform. The NI PXI-2565 is composed of 16 SPST relays. Switching inductive loads (for example, motors and solenoids) can produce high voltage transients in excess of the module's rated voltage. Without additional protectio

### NI PXI-2565

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2565 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 16-SPST | 2565/16-SPST(NISWITCH_TOPOLOGY_2565_16_SPST) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- Relay Forms
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2565 16-SPST Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2566-16-spdt-topology.html language=enus -->
## TOPIC 00273: NI PXI-2566 16-SPDT Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2566-16-spdt-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2566-16-spdt-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2566 in the 16-SPDT topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. To connect the NO terminal to the COM terminal of that channel, disconnect the NC terminal from the COM o

### NI PXI-2566 16-SPDT Topology

The following figure represents the NI PXI-2566 in the 16-SPDT topology.

[IMAGE alt='image' src='GUID-ACF664BF-AD96-4478-B73E-4E6306959248-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

To connect the NO terminal to the COM terminal of that channel, disconnect the NC
 terminal from the COM of that channel.

For example, to connect NO2 to COM2, use the following code:

niSwitch_Disconnect(vi, "nc2", "com2")

niSwitch_Connect(vi, "no2", "com2")

Note

niSwitch_DisconnectAll

Note

niSwitch_Disconnect(vi, "nc2", "com2")

niSwitch_Connect(vi, "no2", "com2")

To connect the NC terminal to the COM terminal of that channel, disconnect the NO
 terminal from the COM of that channel.

For example, to connect NC2 to COM2, use the following code:

niSwitch_Disconnect(vi, "no2", "com2")

niSwitch_Connect(vi, "nc2", "com2")

When scanning the NI PXI-2566, a typical scan list entry could be
 nc2->com2;. This entry routes the signal connected to NC2 to
 COM2.

#### Pinout

The following figure identifies the pins for the NI PXI-2566 in the 16-SPDT
 topology.

[IMAGE alt='image' src='GUID-EBC87DBD-5B20-4624-A728-F8133C733EEB-a5.svg']

Caution

Parent topic:

NI PXI-2566

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2566-8-dpdt-topology.html language=enus -->
## TOPIC 00274: NI PXI-2566 8-DPDT Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2566-8-dpdt-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2566-8-dpdt-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2566 in the 8-DPDT topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. To connect the NO terminal to the COM terminal of that channel, disconnect the NC terminal from the COM of

### NI PXI-2566 8-DPDT Topology

The following figure represents the NI PXI-2566 in the 8-DPDT topology.

[IMAGE alt='image' src='GUID-A291D6FA-42AA-49BA-8391-007B4897B57F-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

To connect the NO terminal to the COM terminal of that channel, disconnect the NC
 terminal from the COM of that channel.

For example, to connect NO2 to COM2, use the following code:

niSwitch_Disconnect(vi, "nc2", "com2")

niSwitch_Connect(vi, "no2", "com2")

Note

niSwitch_DisconnectAll

Note

niSwitch_Disconnect(vi, "nc2", "com2")

niSwitch_Connect(vi, "no2w0", "com2w0")

To connect the NC terminal to the COM terminal of that channel, disconnect the NO
 terminal from the COM of that channel.

For example, to connect NC2 to COM2, use the following code:

niSwitch_Disconnect(vi, "no2", "com2")

niSwitch_Connect(vi, "nc2", "com2")

When scanning the NI PXI-2566, a typical scan list entry could be
 nc2->com2;. This entry routes the signal connected to NC2 to
 COM2.

#### Pinout

The following figure identifies the pins for the NI PXI-2566 in the 8-DPDT
 topology.

[IMAGE alt='image' src='GUID-AD7DDB6C-86B4-4173-A6CE-7324377109E2-a5.svg']

Caution

Parent topic:

NI PXI-2566

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2566-hardware-diagram.html language=enus -->
## TOPIC 00275: NI PXI-2566 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2566-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2566-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2566.

### NI PXI-2566 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2566.

[IMAGE alt='image' src='GUID-0F3716B8-BC9F-4E04-822E-DB2C99DEC8A9-a5.gif']

Parent topic:

NI PXI-2566

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2566-relay-replacement.html language=enus -->
## TOPIC 00276: NI PXI-2566 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2566-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2566-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2566 uses electromechanical armature relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Number Aromat (NAiS) TQ2SA-5V Complete the following sets of steps to replace a failed relay. Ground yourself using a grounding strap or a g

### NI PXI-2566 Relay Replacement

The NI PXI-2566 uses electromechanical armature relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| Aromat (NAiS) | TQ2SA-5V |

Complete the following sets of steps to replace a failed relay.

1. Ground yourself using a grounding strap or a ground connected to your PXI chassis.
 Note Properly grounding yourself prevents damage to your module
 from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure for relay
 locations. [IMAGE alt='image' src='GUID-BC701F13-A263-4481-A74B-A1DC6FC1CD8D-a5.gif'] 
 Note Older versions of this module might have adhesive plastic lead
 covers that you must remove. The module retains full specifications even if the
 covers are not reinstalled.
3. Locate the assembly and serial number labels on the board with the relay you want to
 replace. White labels indicate the board was assembled using lead solder (Sn 63 Pb
 37). Green labels indicate the board was assembled using lead-free solder (Sn 96.5
 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers ending in L. The
 different label types are shown in the following figure. [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']
4. Replace the relay.

Note

Caution

Caution

Before you begin, make sure you have the following items:

- Temperature-regulated soldering iron set to 316 °C (600 °F) for lead solder rework
 or 371 °C (700 °F) for lead-free solder rework
- 63/37 Tin/Lead solder (flux core) for lead solder rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

If you have a surface mount rework station, replace the relay as you would any other
 surface mount part. Otherwise, complete the following steps to replace the relay:

1. Use the soldering iron and solder wick to remove as much solder from the relay pads
 as possible. Do not leave the soldering iron on any lead for more than 5 seconds.
 Note If it is necessary to reapply the soldering iron to the
 pad, allow the connection to cool completely before reapplying the soldering
 iron.
2. Apply heat to the pads one at a time, and use the pick to gently pry the relay pins
 from the pads. Make sure that the solder is molten before prying. Caution Using excessive force on a soldered pad can result in lifting
 the PCB trace and ruining the board.
3. Remove the relay.
4. Clean the pads with isopropyl alcohol and cotton swabs.
5. Place the new relay on the PCB pads and solder.
6. Remove the excess flux with isopropyl alcohol and cotton swabs. Caution Do not use flux remover to clean the board after relay
 replacement.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2566

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2566-triggering.html language=enus -->
## TOPIC 00277: NI PXI-2566 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2566-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2566-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This module can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2566. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger l

### NI PXI-2566 Triggering

This module can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2566.

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
| Front Connector | External(NISWITCH_VAL_EXTERNAL) | TRIG IN on TB-2666 terminal block |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2566.

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
| Front Connector | External(NISWITCH_VAL_EXTERNAL) | TRIG OUT on TB-2666 terminal block |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2566

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2566.html language=enus -->
## TOPIC 00278: NI PXI-2566

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2566.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2566.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2566 is a 16-channel general-purpose relay switch module for the PXI platform designed for switching and controlling low-level and power signals. Switching inductive loads (for example, motors and solenoids) can produce high voltage transients in excess of the module's rated voltage. Wi

### NI PXI-2566

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2566 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 16-SPDT | 2566/16-SPDT(NISWITCH_TOPOLOGY_2566_16_SPDT) |  |  |
| 8-DPDT | 2566/8-DPDT(NISWITCH_TOPOLOGY_2566_8_DPDT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2566 16-SPDT Topology
- NI PXI-2566 8-DPDT Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2567-hardware-diagram.html language=enus -->
## TOPIC 00279: NI PXI-2567 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2567-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2567-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2567.

### NI PXI-2567 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2567.

[IMAGE alt='image' src='GUID-7E5C9DE6-A224-4621-9580-3C1FD24F2921-a5.gif']

Parent topic:

NI PXI-2567

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2567-independent-topology.html language=enus -->
## TOPIC 00280: NI PXI-2567 Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2567-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2567-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure is a representation of the NI PXI-2567 topology. Making a Connection To drive your relay, use the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to actuate a relay connected to channel 7, you can connect the positive terminal of your voltage source t

### NI PXI-2567 Independent Topology

The following figure is a representation of the NI PXI-2567 topology.

[IMAGE alt='image' src='GUID-8D0F5648-C59D-46F7-80AE-40BC78E9E9EA-a5.gif']

#### Making a Connection

To drive your relay, use the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to actuate a relay connected to channel 7, you can connect the positive
 terminal of your voltage source to one side of the relay coil, and connect the other
 relay coil terminal to pin 44 of the front connector. Then connect the negative
 terminal of your voltage source to the common ground return of channel 7 (pin 42).
 Closing the channel 7 driver completes the circuit, driving your relay. The
 following figure illustrates how to actuate a relay connected to channel 7.

[IMAGE alt='image' src='GUID-DA9640CB-2A9F-4E64-B240-68A31C62D5E7-a5.gif']

To close the channel 7 relay, call niSwitch_Connect(vi, "ch7",
 "com7").

Alternatively, you can open and close relays by calling the niSwitch Relay
 Control
 VI or the
 niSwitch_RelayControl
 function. For the relay name, enter K0 for channel 0, K1 for channel 1, and so
 on.

When scanning the NI PXI-2567, a typical scan list entry could be
 ch2->com2;. This entry drives the relay connected to channel
 2.

#### Driving 2-Coil Relays

The following figure shows an example of a configuration using the NI PXI-2567 to
 drive a 2-coil relay.

[IMAGE alt='image' src='GUID-2ECA789F-7B47-4705-B14C-E777A014A882-a5.gif']

To close the relay in this example, you would call niSwitch_Connect(vi,
 "ch7", "com7"). To open the relay, then you would call
 niSwitch_Disconnect(vi, "ch7", "com7") and then
 niSwitch_Connect(vi, "ch6", "com6").

Alternatively, you can actuate the relay by calling the niSwitch Relay
 Control
 VI or the
 niSwitch_RelayControl
 function. To close the relay in this example, you would call
 niSwitch_RelayControl(vi, K7, NISWITCH_VAL_CLOSE_RELAY) to
 power on the lower coil in the diagram. Then call niSwitch_RelayControl(vi,
 K7, NISWITCH_VAL_OPEN_RELAY) to power off the lower coil, and call
 niSwitch_RelayControl(vi, K6, NISWITCH_VAL_CLOSE_RELAY) power
 on the other coil and open the relay.

#### Pinout

The following figure identifies the pins for the NI PXI-2567.

[IMAGE alt='image' src='GUID-43B5751E-8241-457F-B783-218D72B5A369-a5.gif']

Caution

Parent topic:

NI PXI-2567

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2567-triggering.html language=enus -->
## TOPIC 00281: NI PXI-2567 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2567-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2567-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This module can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2567. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger l

### NI PXI-2567 Triggering

This module can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2567.

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
| Front Connector | External(NISWITCH_VAL_EXTERNAL) | TRIG IN on pin 59 |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI PXI-2567.

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
| Front Connector | External(NISWITCH_VAL_EXTERNAL) | TRIG OUT on pin 20 |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI-2567

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2567.html language=enus -->
## TOPIC 00282: NI PXI-2567

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2567.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2567.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2567 is a 64-channel general-purpose relay driver module for the PXI platform. The NI PXI-2567 is designed to handle up to 0.6 A drive current and up to 50 V drive voltage. The NI PXI-2567 also has two sources available for driving relays. Operation Modes The following table lists the sup

### NI PXI-2567

The NI PXI-2567 is a 64-channel general-purpose relay driver module for the PXI platform.
 The NI PXI-2567 is designed to handle up to 0.6 A drive current and up to 50 V drive
 voltage. The NI PXI-2567 also has two sources available for driving relays.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2567 and possible
 operation modes.

Note

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Independent | 2567/Independent(NISWITCH_TOPOLOGY_2567_INDEPENDENT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- Available 5 V and 12 V Sources
- Operation Modes
- NI PXI-2567 Independent Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2568-15-dpst-topology.html language=enus -->
## TOPIC 00283: NI PXI-2568 15-DPST Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2568-15-dpst-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2568-15-dpst-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2568 in the 15-DPST topology. Making a Connection Both the scanning command, ch2->com2;, and the immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters ch2 and com2, result in the following connections: signal con

### NI PXI-2568 15-DPST Topology

The following figure represents the NI PXI-2568 in the 15-DPST topology.

[IMAGE alt='image' src='GUID-617BDB93-0433-4C1A-ADCC-28F6B8BA2290-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com2;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com2, result in the
 following connections:

signal connected to CH2W0 is routed to COM2W0

signal connected to CH2W1 is routed to COM2W1

#### Pinout

The following figure identifies the pins for the NI PXI-2568 in the 15-DPST topology.

[IMAGE alt='image' src='GUID-7D2C3B2E-58DC-4843-B4C7-9BF2D67F2EE1-a5.gif']

Parent topic:

NI PXI-2568

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2568-31-spst-topology.html language=enus -->
## TOPIC 00284: NI PXI-2568 31-SPST Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2568-31-spst-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2568-31-spst-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2568 in the 31-SPST topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to close the relay of channel 2, call niSwitch_Connect(vi, "ch2", "com2"). To open the relay

### NI PXI-2568 31-SPST Topology

The following figure represents the NI PXI-2568 in the 31-SPST topology.

[IMAGE alt='image' src='GUID-92460452-0928-4D20-85BE-8AA1BA943932-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to close the relay of channel 2, call niSwitch_Connect(vi, "ch2",
 "com2"). To open the relay of channel 2, call niSwitch_Disconnect(vi,
 "ch2", "com2").

When scanning the NI PXI-2568, a typical scan list entry could be
 ch2->com2;. This entry closes the relay between CH2 and COM2.

#### Pinout

The following figure identifies the pins for the NI PXI-2568 in the 31-SPST topology.

[IMAGE alt='image' src='GUID-92A00B18-1BE7-4DC5-8A19-2777D0863BFF-a5.gif']

Parent topic:

NI PXI-2568

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2568-hardware-diagram.html language=enus -->
## TOPIC 00285: NI PXI-2568 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2568-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2568-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2568.

### NI PXI-2568 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2568.

[IMAGE alt='image' src='GUID-7E46A0A5-DC21-4640-9454-1BD2D124DFB2-a5.gif']

Parent topic:

NI PXI-2568

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2568-relay-replacement.html language=enus -->
## TOPIC 00286: NI PXI-2568 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2568-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2568-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2568 uses electromechanical armature relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Number AXICOM (Tyco Electronics) IM42GR (3-1462037-1) Relay Kit Part Number National Instruments (10 relays) 779356-01 Complete the followin

### NI PXI-2568 Relay Replacement

The NI PXI-2568 uses electromechanical armature relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| AXICOM (Tyco Electronics) | IM42GR (3-1462037-1) |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 779356-01 |

Complete the following sets of steps to replace a failed relay.

1. Ground yourself using a grounding strap or a ground connected to your PXI chassis.
 Note Properly grounding yourself prevents damage to your module
 from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table for
 relay locations. [IMAGE alt='image' src='GUID-83D1FC9A-DB09-41F0-A458-E9B01CD970C3-a5.gif'] 
 Channel Name
 Relay Name
 Channel Name
 Relay NameCH0
 K1
 CH16
 K17CH1
 K2
 CH17
 K18CH2
 K3
 CH18
 K19CH3
 K4
 CH19
 K20CH4
 K5
 CH20
 K21CH5
 K6
 CH21
 K22CH6
 K7
 CH22
 K23CH7
 K8
 CH23
 K24CH8
 K9
 CH24
 K25CH9
 K10
 CH25
 K26CH10
 K11
 CH26
 K27CH11
 K12
 CH27
 K28CH12
 K13
 CH28
 K29CH13
 K14
 CH29
 K30CH14
 K15
 CH30
 K31CH15
 K16 
 Note Older versions of this module might have plastic lead covers
 that you must remove. The module retains full specifications even if these
 covers are not reinstalled.
3. Locate the assembly and serial number labels on the board with the relay you want to
 replace. White labels indicate the board was assembled using lead solder (Sn 63 Pb
 37). Green labels indicate the board was assembled using lead-free solder (Sn 96.5
 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers ending in L. [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']
4. Replace the relay. Note NI recommends using lead-free solder for
 relay replacement on lead-free assemblies, and lead solder for relay replacement
 on lead assemblies. 
 Caution Do not rework lead assemblies using a lead-free work
 station. Lead solder from the unit could contaminate the station. 
 Caution If a lead-free assembly is reworked with lead solder, label
 the assembly to indicate this. This can prevent the same unit from being
 reworked later on a lead-free solder station, which could contaminate the
 station. 
 Make sure you have the following: 
 
 If you have a surface mount rework station, replace the relay as you would any
 other surface mount part. Otherwise, complete the following steps to replace the
 relay:
  - Temperature-regulated soldering iron set to 316 °C (600 °F) for lead solder
 rework or 371 °C (700 °F) for lead-free solder rework
  - 63/37 Tin/Lead solder (flux core) for lead solder rework
  - 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
  - Solder wick
  - Fine pick
  - Isopropyl alcohol
  - Cotton swabs
  1. Use the soldering iron and solder wick to remove as much solder from the
 relay pads as possible. Do not leave the soldering iron on any lead for more
 than 5 seconds. Note If it is necessary to reapply the
 soldering iron to the pad, allow the connection to cool completely
 before reapplying the soldering iron.
  2. Apply heat to the pads one at a time, and use the pick to gently pry the
 relay pins from the pads. Make sure that the solder is molten before prying.
 Caution Using excessive force on a soldered pad can
 result in lifting the PCB trace and ruining the board.
  3. Remove the relay.
  4. Clean the pads with isopropyl alcohol and cotton swabs.
  5. Place the new relay on the PCB pads and solder.
  6. Remove the excess flux with isopropyl alcohol and cotton swabs. Caution Do not use flux remover to clean
 the board after relay replacement.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2568

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2568-triggering.html language=enus -->
## TOPIC 00287: NI PXI-2568 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2568-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2568-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This module can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2568. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger l

### NI PXI-2568 Triggering

This module can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2568.

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

The following table lists valid scan advanced outputs for the NI PXI-2568.

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

NI PXI-2568

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2568.html language=enus -->
## TOPIC 00288: NI PXI-2568

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2568.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2568.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2568 is a 31-channel general-purpose relay module for the PXI platform. The NI PXI-2568 is composed of 31 armature latching SPST relays. For certain applications, you may need to increase the default settling time. Refer to Adding Additional Settling Time for more information. Switching

### NI PXI-2568

The NI PXI-2568 is a 31-channel general-purpose relay module for the PXI platform. The NI
 PXI-2568 is composed of 31 armature latching SPST relays.

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2568 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 31-SPST | 2568/31-SPST(NISWITCH_TOPOLOGY_2568_31_SPST) |  |  |
| 15-DPST | 2568/15-DPST(NISWITCH_TOPOLOGY_2568_15_DPST) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- Armature Relays
- Relay Forms
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2568 31-SPST Topology
- NI PXI-2568 15-DPST Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2570-40-spdt-topology.html language=enus -->
## TOPIC 00289: NI PXI-2570 40-SPDT Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2570-40-spdt-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2570-40-spdt-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2570 in the 40-SPDT topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. To connect the NO terminal to the COM terminal of that channel, disconnect the NC terminal from the COM o

### NI PXI-2570 40-SPDT Topology

The following figure represents the NI PXI-2570 in the 40-SPDT topology.

|  |
| --- |
|  |

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

To connect the NO terminal to the COM terminal of that channel, disconnect the NC
 terminal from the COM of that channel.

For example, to connect NO2 to COM2, use the following code:

niSwitch_Disconnect(vi, "NC2", "COM2")

niSwitch_Connect(vi, "NO2", "COM2")

Note

niSwitch_DisconnectAll

Note

niSwitch_Disconnect(vi, "NC2", "COM2")

niSwitch_Connect(vi, "NO2", "COM2")

When scanning the NI PXI-2570, a typical scan list entry could be
 nc2->com2;. This entry routes the signal connected to NC2 to
 COM2.

#### Pinout

The following figure identifies the pins for the NI PXI-2570 in the 40-SPDT
 topology.

[IMAGE alt='image' src='GUID-7339ED19-CB40-4E36-8F1C-09C46455D1A5-a5.gif']

Parent topic:

NI PXI-2570

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2570-hardware-diagram.html language=enus -->
## TOPIC 00290: NI PXI-2570 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2570-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2570-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2570.

### NI PXI-2570 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2570.

[IMAGE alt='image' src='GUID-E61AE4BC-678A-4A56-A2E6-6B1E0902D0CD-a5.gif']

Parent topic:

NI PXI-2570

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2570-relay-replacement.html language=enus -->
## TOPIC 00291: NI PXI-2570 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2570-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2570-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2570 uses electromechanical armature relays. This topic provides relay replacement instructions for through-hole and surface-mount relays depending on the revision of your module assembly: NI PXI-2570 Through-Hole Relay Replacement NI PXI-2570 Surface-Mount Relay Replacement In NI-SWITC

### NI PXI-2570 Relay Replacement

The NI PXI-2570 uses electromechanical armature relays. This topic provides relay
 replacement instructions for through-hole and surface-mount relays depending on the
 revision of your module assembly:

- NI PXI-2570 Through-Hole Relay Replacement
- NI PXI-2570 Surface-Mount Relay Replacement

Tip

Switch Soft Front Panel Help

#### NI PXI-2570 Through-Hole Relay Replacement

The NI PXI-2570 uses electromechanical armature relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| AXICOM (Tyco Electronics) | IM42PNS (7-1462039-8) |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 781678-01 |

Complete the following steps to replace a failed relay.

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your module from electrostatic discharge.
2. Locate the relay you want to replace. Relay names are labeled on the back of
 module. The following table maps the relay names to the channel names.
 Channel Name
 Relay Name
 Channel Name
 Relay NameCH0
 K0
 CH20
 K20CH1
 K1
 CH21
 K21CH2
 K2
 CH22
 K22CH3
 K3
 CH23
 K23CH4
 K4
 CH24
 K24CH5
 K5
 CH25
 K25CH6
 K6
 CH26
 K26CH7
 K7
 CH27
 K27CH8
 K8
 CH28
 K28CH9
 K9
 CH29
 K29CH10
 K10
 CH30
 K30CH11
 K11
 CH31
 K31CH12
 K12
 CH32
 K32CH13
 K13
 CH33
 K33CH14
 K14
 CH34
 K34CH15
 K15
 CH35
 K35CH16
 K16
 CH36
 K36CH17
 K17
 CH37
 K37CH18
 K18
 CH38
 K38CH19
 K19
 CH39
 K39
3. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']
4. Replace the relay. Note NI recommends using lead-free solder for
 relay replacement on lead-free assemblies, and lead solder for relay
 replacement on lead assemblies. 
 Caution Do not rework lead assemblies using a lead-free work
 station. Lead solder from the unit could contaminate the station. 
 Caution If a lead-free assembly is reworked with lead solder,
 label the assembly to indicate this. This can prevent the same unit from
 being reworked later on a lead-free solder station, which could contaminate
 the station.
  1. Make sure you have the following:
    - Temperature-regulated soldering iron set to 316 °C (600 °F) for
 lead solder rework or 371 °C (700 °F) for lead-free solder
 rework
    - 63/37 Tin/Lead solder (flux core) for lead solder rework
    - 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free
 solder rework
    - Solder wick
    - Fine pick
    - Isopropyl alcohol
    - Cotton swabs
  2. Replace the relay as you would any other through-hole part.

#### NI PXI-2570 Surface-Mount Relay Replacement

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| AXICOM (Tyco Electronics) | IM42GR (3-1462037-1) |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 779356-01 |

Complete the following sets of steps to replace a failed relay.

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your module from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table
 for relay locations. [IMAGE alt='image' src='GUID-F48ECD75-FB9B-407E-96F4-F4C37C2E2417-a5.gif'] 
 Channel Name
 Relay Name
 Channel Name
 Relay NameCH0
 K0
 CH20
 K20CH1
 K1
 CH21
 K21CH2
 K2
 CH22
 K22CH3
 K3
 CH23
 K23CH4
 K4
 CH24
 K24CH5
 K5
 CH25
 K25CH6
 K6
 CH26
 K26CH7
 K7
 CH27
 K27CH8
 K8
 CH28
 K28CH9
 K9
 CH29
 K29CH10
 K10
 CH30
 K30CH11
 K11
 CH31
 K31CH12
 K12
 CH32
 K32CH13
 K13
 CH33
 K33CH14
 K14
 CH34
 K34CH15
 K15
 CH35
 K35CH16
 K16
 CH36
 K36CH17
 K17
 CH37
 K37CH18
 K18
 CH38
 K38CH19
 K19
 CH39
 K39 
 Note Older versions of this module might have adhesive plastic
 lead covers that you must remove. The module retains full specifications
 even if these covers are not reinstalled.
3. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. The different label types are shown in the following figure.
 [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']
4. Replace the relay.

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

If you have a surface mount rework station, replace the relay as you would any other
 surface mount part. Otherwise, complete the following steps to replace the
 relay:

1. Use the soldering iron and solder wick to remove as much solder from the relay
 pads as possible. Do not leave the soldering iron on any lead for more than 5
 seconds. Note If it is necessary to reapply the soldering iron
 to the pad, allow the connection to cool completely before reapplying the
 soldering iron.
2. Apply heat to the pads one at a time, and use the pick to gently pry the relay
 pins from the pads. Make sure that the solder is molten before prying. Caution Using excessive force on a soldered pad can result in
 lifting the PCB trace and ruining the board.
3. Remove the relay.
4. Clean the pads with isopropyl alcohol and cotton swabs.
5. Place the new relay on the PCB pads and solder.
6. Remove the excess flux with isopropyl alcohol and cotton swabs. Caution Do not use flux remover to clean the
 board after relay replacement.

Parent topic:

NI PXI-2570

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2570-triggering.html language=enus -->
## TOPIC 00292: NI PXI-2570 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2570-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2570-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This module can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2570. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger l

### NI PXI-2570 Triggering

This module can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2570.

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

The following table lists valid scan advanced outputs for the NI PXI-2570.

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

NI PXI-2570

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2570.html language=enus -->
## TOPIC 00293: NI PXI-2570

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2570.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2570.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2570 is a 40-channel general-purpose relay module for the PXI platform designed for switching and controlling low-level and power signals. The NI PXI-2570 is composed of 40 armature latching SPDT relays. For certain applications, you may need to increase the default settling time. Refer t

### NI PXI-2570

The NI PXI-2570 is a 40-channel general-purpose relay module for the PXI platform
 designed for switching and controlling low-level and power signals. The NI PXI-2570 is
 composed of 40 armature latching SPDT relays.

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2570 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 40-SPDT | 2570/40-SPDT(NISWITCH_TOPOLOGY_2570_40_SPDT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- Armature Relays
- Relay Forms
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2570 40-SPDT Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2571-66-spdt-topology.html language=enus -->
## TOPIC 00294: NI PXI-2571 66-SPDT Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2571-66-spdt-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2571-66-spdt-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2571 in the 66-SPDT topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. To connect the NO terminal to the COM terminal of that channel, disconnect the NC terminal from the COM t

### NI PXI-2571 66-SPDT Topology

The following figure represents the NI PXI-2571 in the 66-SPDT topology.

|  |
| --- |
|  |

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

To connect the NO terminal to the COM terminal of that channel, disconnect the NC
 terminal from the COM terminal of that channel.

For example, to connect NO2 to COM2, use the following code:

niSwitch_Disconnect(vi, "NC2", "COM2")

niSwitch_Connect(vi, "NO2", "COM2")

Note

niSwitch_DisconnectAll

Note

niSwitch_Disconnect(vi, "NC2", "COM2")

niSwitch_Connect(vi, "NO2", "COM2")

When scanning the NI PXI-2571, a typical scan list entry could be
 nc2->com2;. This entry routes the signal connected to NC2 to
 COM2.

#### Pinout

The following figure identifies the pins for the NI PXI-2571 in the 66-SPDT
 topology.

[IMAGE alt='image' src='GUID-16B5C024-C878-49D9-A04E-B5192A8AC398-a5.gif']

Parent topic:

NI PXI-2571

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2571-hardware-diagram.html language=enus -->
## TOPIC 00295: NI PXI-2571 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2571-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2571-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2571.

### NI PXI-2571 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2571.

[IMAGE alt='image' src='GUID-50F7425E-1406-442A-A175-CBC775C7D359-a5.gif']

Parent topic:

NI PXI-2571

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2571-relay-replacement.html language=enus -->
## TOPIC 00296: NI PXI-2571 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2571-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2571-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2571 uses electromechanical armature relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Number AXICOM (Tyco Electronics) IM42PNS (7-1462039-8) Relay Kit Part Number National Instruments (10 relays) 781678-01 Complete the followi

### NI PXI-2571 Relay Replacement

The NI PXI-2571 uses electromechanical armature relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| AXICOM (Tyco Electronics) | IM42PNS (7-1462039-8) |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 781678-01 |

Complete the following steps to disassemble your module and replace a failed relay.

1. Ground yourself using a grounding strap or a ground connected to your PXI chassis.
 Note Properly grounding yourself prevents damage to your module
 from electrostatic discharge.
2. Locate the relay you want to replace. Relay names are labeled on the back of module.
 The following table maps the relay names to the channel names. Channel Name
 Relay Name
 Channel Name
 Relay Name
 Channel Name
 Relay Name
 Channel Name
 Relay NameCH0
 K0
 CH20
 K20
 CH40
 K40
 CH60
 K60CH1
 K1
 CH21
 K21
 CH41
 K41
 CH61
 K61CH2
 K2
 CH22
 K22
 CH42
 K42
 CH62
 K62CH3
 K3
 CH23
 K23
 CH43
 K43
 CH63
 K63CH4
 K4
 CH24
 K24
 CH44
 K44
 CH64
 K64CH5
 K5
 CH25
 K25
 CH45
 K45
 CH65
 K65CH6
 K6
 CH26
 K26
 CH46
 K46
 —
 —CH7
 K7
 CH27
 K27
 CH47
 K47
 —
 —CH8
 K8
 CH28
 K28
 CH48
 K48
 —
 —CH9
 K9
 CH29
 K29
 CH49
 K49
 —
 —CH10
 K10
 CH30
 K30
 CH50
 K50
 —
 —CH11
 K11
 CH31
 K31
 CH51
 K51
 —
 —CH12
 K12
 CH32
 K32
 CH52
 K52
 —
 —CH13
 K13
 CH33
 K33
 CH53
 K53
 —
 —CH14
 K14
 CH34
 K34
 CH54
 K54
 —
 —CH15
 K15
 CH35
 K35
 CH55
 K55
 —
 —CH16
 K16
 CH36
 K36
 CH56
 K56
 —
 —CH17
 K17
 CH37
 K37
 CH57
 K57
 —
 —CH18
 K18
 CH38
 K38
 CH58
 K58
 —
 —CH19
 K19
 CH39
 K39
 CH59
 K59
 —
 —
3. Replace the Relay The NI PXI-2571 uses lead-free assemblies. 
 Note NI recommends using lead-free solder for relay replacement on
 lead-free assemblies and using lead solder for relay replacement on lead
 assemblies. 
 Caution Do not rework lead assemblies using a lead-free work
 station. Lead solder from the unit could contaminate the station. 
 Caution If a lead-free assembly is reworked with lead solder, label
 the assembly to indicate this condition. This rework can prevent the same unit
 from being reworked later on a lead-free solder station, because it could
 contaminate the station.
  1. Make sure you have the following items:
    - Temperature-regulated soldering iron set to 371 °C (700 °F) for
 lead-free solder rework
    - 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free
 solder rework
    - Solder wick
    - Fine pick
    - Isopropyl alcohol
    - Cotton swabs
  2. Replace the relay as you would any other through-hole part.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2571

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2571-triggering.html language=enus -->
## TOPIC 00297: NI PXI-2571 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2571-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2571-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The 2571 can send and receive triggers using synchronous and handshaking modes. This module can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the measurement complete path on the NI PXI-2571. Trigger I

### NI PXI-2571 Triggering

The 2571 can send and receive triggers using synchronous and handshaking modes. This
 module can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the measurement complete path on
 the NI PXI-2571.

| Trigger Input | Terminal Name | Hardware Terminal Used |
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

#### Scan Advanced Output Terminals

The following table lists valid scan advanced output terminals for the NI
 PXI-2571.

| Scan Advanced Output | Terminal Name | Hardware Terminal Used |
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
 function for description of the trigger input signals and scan advanced output
 signals.

Parent topic:

NI PXI-2571

Related concepts:

- Synchronous Scanning
- Handshaking
- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2571.html language=enus -->
## TOPIC 00298: NI PXI-2571

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2571.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2571.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2571 is a 66-channel general-purpose relay module for the PXI platform designed for switching and controlling low-level and power signals. The NI PXI-2571 is composed of 66 armature-latching SPDT relays. For certain applications, you may need to increase the default settling time. Refer t

### NI PXI-2571

The NI PXI-2571 is a 66-channel general-purpose relay module for the PXI platform
 designed for switching and controlling low-level and power signals. The NI PXI-2571 is
 composed of 66 armature-latching SPDT relays.

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2571 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 66-SPDT | 2571/66-SPDT(NISWITCH_TOPOLOGY_2571_66_SPDT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- Armature Relays
- Relay Forms
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2571 66-SPDT Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2576-2-wire-64-1-multiplexer-topology.html language=enus -->
## TOPIC 00299: NI PXI-2576 2-Wire 64×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2576-2-wire-64-1-multiplexer-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2576-2-wire-64-1-multiplexer-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2576 in the 2-wire 64×1 multiplexer topology. Making a Connection When using the NI PXI-2576 as a 2-wire 64×1 multiplexer, all positive leads (ch0+ through ch63+) route to com0+, and all negative leads (ch0– through ch63–) route to com0–. The pair com0+ and

### NI PXI-2576 2-Wire 64×1 Multiplexer Topology

The following figure represents the NI PXI-2576 in the 2-wire 64×1 multiplexer topology.

[IMAGE alt='image' src='GUID-15729F73-2399-47FE-963C-6ABC64CB9749-a5.gif']

#### Making a Connection

When using the NI PXI-2576 as a 2-wire 64×1 multiplexer, all positive leads (ch0+
 through ch63+) route to com0+, and all negative leads (ch0– through ch63–) route to
 com0–. The pair com0+ and com0– is addressed collectively as com0 in software.

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connections:

signal connected to ch2+ is routed to com0+

signal connected to ch2– is routed to com0–

#### Pinout

The following figure identifies the pins for the NI PXI-2576 in the 2-wire 64×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-6C5F106F-FB62-44F9-9516-49BD222F0CC0-a5.gif']

Parent topic:

NI PXI-2576

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2576-2-wire-dual-32-1-multiplexer-topo.html language=enus -->
## TOPIC 00300: NI PXI-2576 2-Wire Dual 32×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2576-2-wire-dual-32-1-multiplexer-topo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2576-2-wire-dual-32-1-multiplexer-topo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2576 in the 2-wire dual 32×1 multiplexer topology. Making a Connection When using the NI PXI-2576 as a 2-wire dual 32×1 multiplexer, the positive leads of the first bank (ch0+ through ch31+) route to com0+, and the negative leads of the first bank (ch0– thr

### NI PXI-2576 2-Wire Dual 32×1 Multiplexer Topology

The following figure represents the NI PXI-2576 in the 2-wire dual 32×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-02F6E5C2-B2D2-4589-847F-45E6C49BAE0D-a5.gif']

#### Making a Connection

When using the NI PXI-2576 as a 2-wire dual 32×1 multiplexer, the positive leads of
 the first bank (ch0+ through ch31+) route to com0+, and the negative leads of the
 first bank (ch0– through ch31–) route to com0–. The pair com0+ and com0– is
 addressed collectively as com0 in software. The second bank follows a similar
 routing scheme.

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connections:

signal connected to ch2+ is routed to com0+

signal connected to ch2– is routed to com0–

#### Pinout

The following figure identifies the pins for the NI PXI-2576 in the 2-wire dual 32×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-6C5F106F-FB62-44F9-9516-49BD222F0CC0-a5.gif']

Parent topic:

NI PXI-2576

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2576-2-wire-octal-8-1-multiplexer-topo.html language=enus -->
## TOPIC 00301: NI PXI-2576 2-Wire Octal 8×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2576-2-wire-octal-8-1-multiplexer-topo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2576-2-wire-octal-8-1-multiplexer-topo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2576 in the 2-wire octal 8×1 multiplexer topology. Making a Connection When using the NI PXI-2576 as a 2-wire octal 8×1 multiplexer, the positive leads of the first bank (ch0+ through ch7+) route to com0+, and the negative leads of the first bank (ch0– thro

### NI PXI-2576 2-Wire Octal 8×1 Multiplexer Topology

The following figure represents the NI PXI-2576 in the 2-wire octal 8×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-58868CB7-0E77-4501-9C5A-005E7660C651-a5.gif']

#### Making a Connection

When using the NI PXI-2576 as a 2-wire octal 8×1 multiplexer, the positive leads of
 the first bank (ch0+ through ch7+) route to com0+, and the negative leads of the
 first bank (ch0– through ch7–) route to com0–. The pair com0+ and com0– is addressed
 collectively as com0 in software. All other banks follow a similar routing
 scheme.

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connections:

signal connected to ch2+ is routed to com0+

signal connected to ch2– is routed to com0–

#### Pinout

The following figure identifies the pins for the NI PXI-2576 in the 2-wire octal 8×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-6C5F106F-FB62-44F9-9516-49BD222F0CC0-a5.gif']

Parent topic:

NI PXI-2576

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2576-2-wire-quad-16-1-multiplexer-topo.html language=enus -->
## TOPIC 00302: NI PXI-2576 2-Wire Quad 16×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2576-2-wire-quad-16-1-multiplexer-topo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2576-2-wire-quad-16-1-multiplexer-topo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2576 in the 2-wire quad 16×1 multiplexer topology. Making a Connection When using the NI PXI-2576 as a 2-wire quad 16×1 multiplexer, the positive leads of the first bank (ch0+ through ch15+) route to com0+, and the negative leads of the first bank (ch0– thr

### NI PXI-2576 2-Wire Quad 16×1 Multiplexer Topology

The following figure represents the NI PXI-2576 in the 2-wire quad 16×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-E3E85D37-FFB3-497F-90DF-E014957AAA45-a5.gif']

#### Making a Connection

When using the NI PXI-2576 as a 2-wire quad 16×1 multiplexer, the positive leads of
 the first bank (ch0+ through ch15+) route to com0+, and the negative leads of the
 first bank (ch0– through ch15–) route to com0–. The pair com0+ and com0– is
 addressed collectively as com0 in software. All other banks follow a similar routing
 scheme.

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connections:

signal connected to ch2+ is routed to com0+

signal connected to ch2– is routed to com0–

#### Pinout

The following figure identifies the pins for the NI PXI-2576 in the 2-wire quad 16×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-6C5F106F-FB62-44F9-9516-49BD222F0CC0-a5.gif']

Parent topic:

NI PXI-2576

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2576-2-wire-sixteen-4-1-multiplexer-to.html language=enus -->
## TOPIC 00303: NI PXI-2576 2-Wire Sixteen 4×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2576-2-wire-sixteen-4-1-multiplexer-to.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2576-2-wire-sixteen-4-1-multiplexer-to.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2576 in the 2-wire sixteen 4×1 multiplexer topology. Making a Connection When using the NI PXI-2576 as a 2-wire sixteen 4×1 multiplexer, the positive leads of the first bank (ch0+ through ch3+) route to com0+, and the negative leads of the first bank (ch0–

### NI PXI-2576 2-Wire Sixteen 4×1 Multiplexer Topology

The following figure represents the NI PXI-2576 in the 2-wire sixteen 4×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-6B33536C-9033-475A-9CD0-0790F87E648C-a5.gif']

#### Making a Connection

When using the NI PXI-2576 as a 2-wire sixteen 4×1 multiplexer, the positive leads of
 the first bank (ch0+ through ch3+) route to com0+, and the negative leads of the
 first bank (ch0– through ch3–) route to com0–. The pair com0+ and com0– is addressed
 collectively as com0 in software. All other banks follow a similar routing
 scheme.

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connections:

signal connected to ch2+ is routed to com0+

signal connected to ch2– is routed to com0–

#### Pinout

The following figure identifies the pins for the NI PXI-2576 in the 2-wire sixteen
 4×1 multiplexer topology.

[IMAGE alt='image' src='GUID-6C5F106F-FB62-44F9-9516-49BD222F0CC0-a5.gif']

Parent topic:

NI PXI-2576

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2576-hardware-diagram.html language=enus -->
## TOPIC 00304: NI PXI-2576 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2576-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2576-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2576.

### NI PXI-2576 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2576.

[IMAGE alt='image' src='GUID-66113387-9799-427B-9898-6C16589AF209-a5.gif']

Parent topic:

NI PXI-2576

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2576-independent-topology.html language=enus -->
## TOPIC 00305: NI PXI-2576 Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2576-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2576-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using the NI PXI-2576 in the independent topology, connect the signals using the NI TB-2676 terminal block. Select this topology to utilize the full routing capabilities of the NI PXI-2576. The following figure represents the NI PXI-2576 in the independent topology. Making a Connection With the

### NI PXI-2576 Independent Topology

When using the NI PXI-2576 in the independent topology, connect the signals using the
 NI TB-2676 terminal block. Select this topology to utilize the full routing capabilities
 of the NI PXI-2576. The following figure represents the NI PXI-2576 in the independent
 topology.

[IMAGE alt='image' src='GUID-66113387-9799-427B-9898-6C16589AF209-a5.gif']

#### Making a Connection

With the independent topology, you can let NI-SWITCH determine the path between two
 specified channels by setting the intermediate channels as reserved for routing and
 using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function, or you can control individual relays using the niSwitch Relay
 Control
 VI or the
 niSwitch_RelayControl
 function.

#### Pinout

The following figure and table identify the pins for the NI PXI-2576 in the
 independent topology.

[IMAGE alt='image' src='GUID-6C5F106F-FB62-44F9-9516-49BD222F0CC0-a5.gif']

Parent topic:

NI PXI-2576

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2576-relay-replacement.html language=enus -->
## TOPIC 00306: NI PXI-2576 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2576-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2576-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2576 uses electromechanical armature relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Number OMRON G6JU-2P-Y DC4.5 Relay Kit Part Number National Instruments (10 relays) 780383-01 Complete the following steps to replace a fail

### NI PXI-2576 Relay Replacement

The NI PXI-2576 uses electromechanical armature relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| OMRON | G6JU-2P-Y DC4.5 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 780383-01 |

Complete the following steps to replace a failed relay.

1. Ground yourself using a grounding strap or a ground connected to your PXI chassis.
 Note Properly grounding yourself prevents damage to your module
 from electrostatic discharge.
2. Refer to the following figures and table to locate the relay you want to replace.
 NI PXI-2576 
 [IMAGE alt='image' src='GUID-AE6B6DB5-480C-4024-824C-7BCB3B6A5388-a5.gif'] 
 NI PXI-2576 Hardware Diagram 
 [IMAGE alt='image' src='GUID-66113387-9799-427B-9898-6C16589AF209-a5.gif'] 
 Relay Name
 Reference Designator
 Relay Name
 Reference Designatork0
 K6
 k40
 K56k1
 K7
 k41
 K57k2
 K8
 k42
 K58k3
 K9
 k43
 K59k4
 K1
 k44
 K51k5
 K2
 k45
 K52k6
 K3
 k46
 K53k7
 K4
 k47
 K54k8
 K16
 k48
 K66k9
 K17
 k49
 K67k10
 K18
 k50
 K68k11
 K19
 k51
 K69k12
 K11
 k52
 K61k13
 K12
 k53
 K62k14
 K13
 k54
 K63k15
 K14
 k55
 K64k16
 K26
 k56
 K76k17
 K27
 k57
 K77k18
 K28
 k58
 K78k19
 K29
 k59
 K79k20
 K21
 k60
 K71k21
 K22
 k61
 K72k22
 K23
 k62
 K73k23
 K24
 k63
 K74k24
 K36
 kbc01
 K5k25
 K37
 kbc23
 K15k26
 K38
 kbc45
 K25k27
 K39
 kbc67
 K35k28
 K31
 kbc89
 K45k29
 K32
 kbc1011
 K55k30
 K33
 kbc1213
 K65k31
 K34
 kbc1415
 K75k32
 K46
 kbc02
 K10k33
 K47
 kbc46
 K30k34
 K48
 kbc810
 K50k35
 K49
 kbc1214
 K70k36
 K41
 kbc04
 K20k37
 K42
 kbc812
 K60k38
 K43
 kbc68
 K40k39
 K44
 —
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

NI PXI-2576

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2576-triggering.html language=enus -->
## TOPIC 00307: NI PXI-2576 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2576-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2576-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2576 can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2576. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigg

### NI PXI-2576 Triggering

The NI PXI-2576 can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2576.

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

The following table lists valid scan advanced outputs for the NI PXI-2576.

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

NI PXI-2576

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2576.html language=enus -->
## TOPIC 00308: NI PXI-2576

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2576.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2576.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2576 is a high-density multiplexer switch module for the PXI platform. The NI PXI-2576 is composed of electromechanical armature latching DPST relays. For certain applications, you may need to increase the default settling time. Refer to Adding Additional Settling Time for more informatio

### NI PXI-2576

The NI PXI-2576 is a high-density multiplexer switch module for the PXI platform. The NI
 PXI-2576 is composed of electromechanical armature latching DPST relays.

Note

#### Operation Modes

The following table lists the supported topologies of the NI PXI-2576 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 2-Wire Sixteen 4×1 Multiplexer | 2576/2-Wire Sixteen 4x1 Mux(NISWITCH_TOPOLOGY_2576_2_WIRE_SIXTEEN_4X1_MUX) |  |  |
| 2-Wire Octal 8×1 Multiplexer | 2576/2-Wire Octal 8x1 Mux(NISWITCH_TOPOLOGY_2576_2_WIRE_OCTAL_8X1_MUX) |  |  |
| 2-Wire Quad 16×1 Multiplexer | 2576/2-Wire Quad 16x1 Mux(NISWITCH_TOPOLOGY_2576_2_WIRE_QUAD_16X1_MUX) |  |  |
| 2-Wire Dual 32×1 Multiplexer | 2576/2-Wire Dual 32x1 Mux(NISWITCH_TOPOLOGY_2576_2_WIRE_DUAL_32X1_MUX) |  |  |
| 2-Wire 64×1 Multiplexer | 2576/2-Wire 64x1 Mux(NISWITCH_TOPOLOGY_2576_2_WIRE_64X1_MUX) |  |  |
| Independent | 2576/Independent(NISWITCH_TOPOLOGY_2576_INDEPENDENT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Electromechanical Relays
- Armature Relays
- Relay Forms
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2576 2-Wire Sixteen 4×1 Multiplexer Topology
- NI PXI-2576 2-Wire Octal 8×1 Multiplexer Topology
- NI PXI-2576 2-Wire Quad 16×1 Multiplexer Topology
- NI PXI-2576 2-Wire Dual 32×1 Multiplexer Topology
- NI PXI-2576 2-Wire 64×1 Multiplexer Topology
- NI PXI-2576 Independent Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2584-1-wire-12-1-multiplexer-topology.html language=enus -->
## TOPIC 00309: NI PXI-2584 1-Wire 12×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2584-1-wire-12-1-multiplexer-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2584-1-wire-12-1-multiplexer-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Install an external jumper wire between the COM0 and COM1 pins to use the NI PXI-2584 as a 1-wire 12×1 multiplexer. The following figure represents the NI PXI-2584 1-wire 12×1 multiplexer topology. Making a Connection Both the scanning command, ch2->com0;, and the immediate operation, niSwitch Conne

### NI PXI-2584 1-Wire 12×1 Multiplexer Topology

Install an external jumper wire between the COM0 and COM1 pins to use the NI PXI-2584 as a
 1-wire 12×1 multiplexer. The following figure represents the NI PXI-2584 1-wire 12×1
 multiplexer topology.

|  |
| --- |
|  |

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in the
 following connection:

Signal connected to CH2 is routed to COM0.

Both the scanning command, ch7->com0;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch7 and com0, result in the
 following connection:

Signal connected to CH7 is routed to COM1.

#### Pinout

The following figure identifies the pins for the NI PXI-2584 in the 1-wire 12×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-4E8D54C1-9163-4147-90C9-FCBCF4E37D89-a5.gif']

Parent topic:

NI PXI-2584

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2584-1-wire-dual-6-1-multiplexer-topol.html language=enus -->
## TOPIC 00310: NI PXI-2584 1-Wire Dual 6×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2584-1-wire-dual-6-1-multiplexer-topol.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2584-1-wire-dual-6-1-multiplexer-topol.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2584 in the 1-wire dual 6×1 multiplexer topology. Making a Connection Both the scanning command, ch2->com0;, and the immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters ch2 and com0, result in the following con

### NI PXI-2584 1-Wire Dual 6×1 Multiplexer Topology

The following figure represents the NI PXI-2584 in the 1-wire dual 6×1 multiplexer topology.

|  |
| --- |
|  |

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in the
 following connection:

Signal connected to CH2 is routed to COM0.

#### Pinout

The following figure identifies the pins for the NI PXI-2584 in the 1-wire dual 6×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-C954427C-AA67-4A2D-9625-5A87B157C509-a5.gif']

Parent topic:

NI PXI-2584

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2584-2-wire-6-1-multiplexer-topology.html language=enus -->
## TOPIC 00311: NI PXI-2584 2-Wire 6×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2584-2-wire-6-1-multiplexer-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2584-2-wire-6-1-multiplexer-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2584 in the 2-wire 6×1 multiplexer topology. Making a Connection Both the scanning command, ch1->com0;, and the immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters ch1 and com0, result in the following connecti

### NI PXI-2584 2-Wire 6×1 Multiplexer Topology

The following figure represents the NI PXI-2584 in the 2-wire 6×1 multiplexer topology.

|  |
| --- |
|  |

#### Making a Connection

Both the scanning command, ch1->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch1 and com0, result in
 the following connections:

- Signal connected to CH1 is routed to COM0.
- Signal connected to CH7 is routed to COM1.

#### Pinout

The following figure and table identify the pins for the NI PXI-2584 in the in the
 2-wire 6×1 multiplexer topology.

[IMAGE alt='image' src='GUID-C954427C-AA67-4A2D-9625-5A87B157C509-a5.gif']

| Software Name | Pin Name |  |
| --- | --- | --- |
| + | – |  |
| ch0 | CH0 | CH6 |
| ch1 | CH1 | CH7 |
| ch2 | CH2 | CH8 |
| ch3 | CH3 | CH9 |
| ch4 | CH4 | CH10 |
| ch5 | CH5 | CH11 |

Parent topic:

NI PXI-2584

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2584-hardware-diagram.html language=enus -->
## TOPIC 00312: NI PXI-2584 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2584-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2584-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2584.

### NI PXI-2584 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2584.

[IMAGE alt='image' src='GUID-7FBD2172-1BF7-49EA-A88F-D536332CFF87-a5.gif']

Parent topic:

NI PXI-2584

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2584-independent-topology.html language=enus -->
## TOPIC 00313: NI PXI-2584 Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2584-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2584-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the independent topology to utilize the full routing capabilities of the NI PXI-2584. For example, when measuring stacked signals, use the independent topology to configure the NI PXI-2584 as an interleaved multiplexer. The following figure represents the NI PXI-2584 in the independent topology.

### NI PXI-2584 Independent Topology

Use the independent topology to utilize the full routing capabilities of the NI PXI-2584. For
 example, when measuring stacked signals, use the independent topology to configure the
 NI PXI-2584 as an interleaved multiplexer.

The following figure represents the NI PXI-2584 in the independent topology.

|  |
| --- |
|  |

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in the
 following connection:

signal connected to CH2 is routed to COM0

#### Pinout

The following figure identifies the pins for the NI PXI-2584 in the independent topology.

[IMAGE alt='image' src='GUID-C954427C-AA67-4A2D-9625-5A87B157C509-a5.gif']

Parent topic:

NI PXI-2584

Related concepts:

- NI PXI-2584 Interleaved Multiplexer (User-Implemented)

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2584-interleaved-multiplexer-user-impl.html language=enus -->
## TOPIC 00314: NI PXI-2584 Interleaved Multiplexer (User-Implemented)

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2584-interleaved-multiplexer-user-impl.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2584-interleaved-multiplexer-user-impl.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the NI PXI-2584 independent topology to create a 2-wire 11×1 multiplexer. The independent topology interleaves the two multiplexer banks of the NI PXI-2584 to create one interleaved multiplexer. Interleaved multiplexing is useful for measuring stacked signals such as battery stacks where

### NI PXI-2584 Interleaved Multiplexer (User-Implemented)

You can use the NI PXI-2584 independent topology to create a 2-wire 11×1 multiplexer. The
 independent topology interleaves the two multiplexer banks of the NI PXI-2584 to create
 one interleaved multiplexer. Interleaved multiplexing is useful for measuring stacked
 signals such as battery stacks where each channel shares a connection with the channels
 before and after it. By sharing connections you can nearly double the channel count
 while still maintaining 2-wire (differential) measurements.

A representation of an interleaved multiplexer is shown in the following figure. The
 channels of the interleaved multiplexer are shown on the left of the figure.

[IMAGE alt='image' src='GUID-5A0DECA3-F912-42BC-8D63-9A92968B050D-a5.gif']

Note

Note

straddled
 channel

Use the Independent topology for both scanning and immediate operation of the NI PXI-2584
 when using it as a 2-wire 11×1 interleaved multiplexer.

#### Single Module Scanning

In single module scanning, to measure signals as shown in the preceding figure,
 complete the following steps:

1. Close CH0, and CH6. The DMM measures the signal between CH0 and CH6.
2. Open CH0, and close CH1 (CH6 remains closed). The DMM measures the signal
 between CH1 and CH6, in reverse polarity.
3. Open CH6, and close CH7 (CH1 remains closed). The DMM measures the signal
 between CH1 and CH7.
4. Open CH1, and close CH2 (CH7 remains closed). The DMM measures the signal
 between CH2 and CH7, in reverse polarity.
5. Continue this pattern for the rest of the channels.
6. Open CH10, and close CH11 (CH5 remains closed). The DMM measures the signal
 between CH5 and CH11.

Refer to the following example for scan list syntax.

/Dev1/ch0->com0 & ch6->com1; ~ch0->com0 && ch1->com0;
 ~ch6->com1 && ch7->com1;...~ch10->com1 && ch11->com1; ~ch5->com0 & ~ch11->com1 &&

Note

niSwitch_ConfigureScanList

No Action

scan
 mode

Refer to the NI-SWITCH or the NI-DAQmx programming example for more information about
 single module scanning with the NI PXI-2584.

#### Multiple Module Scanning

In multiple module scanning, to measure signals on multiple devices, including the
 straddled channel signal, as shown in the following figure, complete the following
 steps:

[IMAGE alt='image' src='GUID-8E29E8D4-254C-49F5-B572-1C1EDEDF2FFB-a5.gif']

1. Follow the steps in single module scanning to measure the signals on the first
 device.
2. Open CH5 on Dev1, and close CH0 on Dev2 (CH11 on Dev1 remains closed). The DMM
 measures the signal between CH11 on Dev1 and CH0 on Dev2 in reverse
 polarity.
3. Open CH11 on Dev1, and close CH6 on Dev2 (CH0 on Dev2 remains closed) The DMM
 measures the signal between CH0 on Dev2 and CH6 on Dev2.
4. Open CH0 on Dev2, and close CH1 on Dev2 (CH6 on Dev2 remains closed) The DMM
 measures the signal between CH1 on Dev2 and CH6 on Dev2 in reverse
 polarity.
5. Open CH6 on Dev2, and close CH7 on Dev2 (CH1 on Dev2 remains closed) The DMM
 measures the signal between CH2 on Dev2 and CH7 on Dev2.
6. Continue this pattern for the rest of the channels.
7. Open CH10 on Dev2, and close CH11 on Dev2 (CH5 on Dev2 remains closed). The DMM
 measures the signal between CH5 on Dev2 and CH11 on Dev2.

Refer to the following example for scan list syntax.

/Dev1/ch0->com0 & ch6->com1;
 ~ch0->com0 && ch1->com0;...~ch5->com0 && 
 /Dev2/ch0->com0; /Dev1/~ch11->com1 && /Dev2/ch6->com1;
 ~ch0->com0 && ch1->com0;...~ch10->com1 && ch11->com1; ~ch5->com0 & ~ch11->com1 &&

Note

niSwitch_ConfigureScanList

No Action

scan
 mode

Multiple module scanning with the NI PXI-2584 is supported only in
 NI-DAQmx. Refer to the NI-DAQmx programming example for more information about
 multiple module scanning with the NI PXI-2584.

#### Pinout

The following figure and table identify the pins for the NI PXI-2584 when used as a
 2-wire 11×1 interleaved multiplexer.

[IMAGE alt='image' src='GUID-C954427C-AA67-4A2D-9625-5A87B157C509-a5.gif']

| Interleaved Channel | Pin Name |  |
| --- | --- | --- |
| + | – |  |
| ch0 | CH0 | CH6 |
| ch1 | CH6 | CH1 |
| ch2 | CH1 | CH7 |
| ch3 | CH7 | CH2 |
| ch4 | CH2 | CH8 |
| ch5 | CH8 | CH3 |
| ch6 | CH3 | CH9 |
| ch7 | CH9 | CH4 |
| ch8 | CH4 | CH10 |
| ch9 | CH10 | CH5 |
| ch10 | CH5 | CH11 |

Parent topic:

NI PXI-2584

Related concepts:

- NI PXI-2584 Independent Topology
- Single Module Scanning
- NI-SWITCH Programming Examples
- Multiple Module Scanning

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2584-relay-replacement.html language=enus -->
## TOPIC 00315: NI PXI-2584 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2584-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2584-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2584 uses reed relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Coto Technology 9104-05-11 Complete the following sets of steps to disassemble your switch module, replace a failed relay, and reassemble your switch module. Disa

### NI PXI-2584 Relay Replacement

The NI PXI-2584 uses reed relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part |
| --- | --- |
| Coto Technology | 9104-05-11 |

Complete the following sets of steps to disassemble your switch module, replace a failed
 relay, and reassemble your switch module.

#### Disassemble the Switch Module

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your switch module from electrostatic discharge.
2. Remove the four screws that secure the plastic cover on the top and plastic lead
 cover on the bottom of the switch assembly. 1
 Screws2
 Plastic Cover3
 Plastic Lead Cover
3. Carefully separate the adhered top cover absorber from the relays by slowly
 prying up on the cover. (Note: some metal relay caps might come loose during
 this process and can be put back onto the relays after you have completed relay
 replacement.)
4. Locate the relay you want to replace. Refer to the following figure and table
 for relay locations. [IMAGE alt='image' src='GUID-5C347DE0-7918-4095-9DEA-9B247AE4C69E-a5.gif'] 
 Channel Name
 Relay NameCH0
 K0CH1
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
 K11
5. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. The different label types are shown in the following figure.
 [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']

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

Replace the relay as you would any other through-hole part. Trim the replaced relay
 leads to under 1.2 mm (0.05 inch) protrusion.

#### Reassemble the Switch Module

Replace the top cover while carefully aligning the standoffs with the mounting holes
 in the module. Secure the bottom cover using the four screws removed in Disassemble
 the Module, step 2.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2584

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2584-signal-connections.html language=enus -->
## TOPIC 00316: NI PXI-2584 Signal Connections

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2584-signal-connections.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2584-signal-connections.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the two reference (REF) connections of the NI PXI-2584 to lower emissions (noise) and preserve signal integrity. The reference connections of NI PXI-2584 should be electrically connected to each other at all times and used only in 1-wire topologies. 1-Wire Dual 6×1 Multiplexer Topology The follo

### NI PXI-2584 Signal Connections

Use the two reference (REF) connections of the NI PXI-2584 to lower emissions (noise) and
 preserve signal integrity. The reference connections of NI PXI-2584 should be
 electrically connected to each other at all times and used only in 1-wire topologies.

#### 1-Wire Dual 6×1 Multiplexer Topology

The following figures represent the NI PXI-2584 in the 1-wire dual 6×1 multiplexer
 topology using reference connections. Depending on the reference signals you want to
 connect, choose one of following configuration options:

- When the reference signals connected to both multiplexers are the same, connect
 the reference signals to REF, as shown in the following figure. [IMAGE alt='image' src='GUID-68DD28D3-F14D-4E62-8E08-3DF8DB88E6F2-a5.gif'][IMAGE alt='image' src='GUID-2DF14DDC-8CCC-4055-AFAA-488E15C7811E-a5.gif']
- When the reference signals connected to both multiplexers are
 not the same, connect the reference signals of one
 multiplexer to REF and the reference signals of the other multiplexer directly
 to the measurement device, as shown in the following figure. [IMAGE alt='image' src='GUID-CC45E628-5E82-49AC-98CD-67E3D7969B53-a5.gif'][IMAGE alt='image' src='GUID-2DF14DDC-8CCC-4055-AFAA-488E15C7811E-a5.gif']

#### 1-Wire 12×1 Multiplexer Topology

The following figure represents the NI PXI-2584 in the 1-wire 12×1 multiplexer
 topology using reference connections.

|  |
| --- |
|  |

Parent topic:

NI PXI-2584

Related concepts:

- NI PXI-2584 1-Wire Dual 6×1 Multiplexer Topology
- NI PXI-2584 1-Wire 12×1 Multiplexer Topology

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2584-triggering.html language=enus -->
## TOPIC 00317: NI PXI-2584 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2584-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2584-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This module can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2584. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger l

### NI PXI-2584 Triggering

This module can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2584.

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

The following table lists valid scan advanced outputs for the NI PXI-2584.

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

NI PXI-2584

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2584.html language=enus -->
## TOPIC 00318: NI PXI-2584

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2584.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2584.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2584 is a high-voltage multiplexer switch module for the PXI platform. The NI PXI-2584 uses reed relays. A number of factors can affect the life expectancy of reed relays. Refer to Reed Relay Protection for information about protecting the reed relays of the NI PXI-2584. For certain appli

### NI PXI-2584

The NI PXI-2584 is a high-voltage multiplexer switch module for the PXI platform. The
 NI PXI-2584 uses reed relays.

A number of factors can affect the life expectancy of reed relays. Refer to Reed Relay
 Protection for information about protecting the reed relays of the NI PXI-2584.

For certain applications, you may need to increase the default settling time. Refer to
 Adding Additional Settling Time for more information.

Note

#### Operation Modes

The following table lists the supported topologies of the NI PXI-2584 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire Dual 6×1 Multiplexer | 2584/1-Wire Dual 6x1 Mux(NISWITCH_TOPOLOGY_2584_1_WIRE_DUAL_6X1_MUX) |  |  |
| 1-Wire 12×1 Multiplexer | 2584/1-Wire 12x1 Mux(NISWITCH_TOPOLOGY_2584_1_WIRE_12X1_MUX) |  |  |
| 2-Wire 6×1 Multiplexer | 2584/2-Wire 6x1 Mux(NISWITCH_TOPOLOGY_2584_2_WIRE_6X1_MUX) |  |  |
| Independent | 2584/Independent(NISWITCH_TOPOLOGY_2584_INDEPENDENT) |  |  |

Tip

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Reed Relays
- Reed Relay Protection
- Settling Time
- Adding Additional Settling Time
- NI PXI-2584 Signal Connections
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2584 1-Wire Dual 6×1 Multiplexer Topology
- NI PXI-2584 1-Wire 12×1 Multiplexer Topology
- NI PXI-2584 2-Wire 6×1 Multiplexer Topology
- NI PXI-2584 Independent Topology
- NI PXI-2584 Interleaved Multiplexer (User-Implemented)
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2585-1-wire-10-1-multiplexer-topology.html language=enus -->
## TOPIC 00319: NI PXI-2585 1-Wire 10×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2585-1-wire-10-1-multiplexer-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2585-1-wire-10-1-multiplexer-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2585 in the 1-wire 10×1 multiplexer topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to close the relay of channel 2, call niSwitch_Connect(vi, "ch2", "com"). To

### NI PXI-2585 1-Wire 10×1 Multiplexer Topology

The following figure represents the NI PXI-2585 in the 1-wire 10×1 multiplexer topology.

[IMAGE alt='image' src='GUID-3CD09C7D-3F68-4888-9234-C663F91433B5-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to close the relay of channel 2, call niSwitch_Connect(vi, "ch2",
 "com"). To open the relay of channel 2, call niSwitch_Disconnect(vi,
 "ch2", "com").

When scanning the NI PXI-2585, a typical scan list entry could be
 ch2->com;. This entry closes the relay between CH2 and COM.

#### Pinout

The following figure identifies the pins for the NI PXI-2585 in the 1-wire 10×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-BA5F39CD-DA4B-46F3-A4C7-2C07F3D7C54C-a5.gif']

Parent topic:

NI PXI-2585

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2585-hardware-diagram.html language=enus -->
## TOPIC 00320: NI PXI-2585 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2585-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2585-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2586.

### NI PXI-2585 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2586.

[IMAGE alt='image' src='GUID-F7ED2E98-A821-4A9E-BAA3-5981E2999262-a5.gif']

Parent topic:

NI PXI-2585

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2585-relay-replacement.html language=enus -->
## TOPIC 00321: NI PXI-2585 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2585-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2585-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2585 uses electromechanical armature relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Number Potter & Brumfield (Tyco Electronics) RTB14005F (2-1419108-4) Complete the following sets of steps to disassemble your module and rep

### NI PXI-2585 Relay Replacement

The NI PXI-2585 uses electromechanical armature relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| Potter & Brumfield (Tyco Electronics) | RTB14005F (2-1419108-4) |

Complete the following sets of steps to disassemble your module and replace a failed
 relay.

#### Disassemble the Module

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your module from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table
 for relay locations. [IMAGE alt='image' src='GUID-E004D9C2-6620-4EFF-829C-3259B39A811D-a5.gif'] 
 Channel Name
 Relay NameCH0
 K0CH1
 K1CH2
 K2CH3
 K3CH4
 K4CH5
 K5CH6
 K6CH7
 K7CH8
 K8CH9
 K9
3. Remove the four screws from the back of the relay board, and carefully peel off
 the plastic safety shield. 
 1
 Screws2
 Plastic safety shield
4. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. The different label types are shown in the following figure.
 [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']

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

If you have a surface mount rework station, replace the relay as you would any other
 surface mount part. Otherwise, complete the following steps to replace the
 relay:

1. Use the soldering iron and solder wick to remove as much solder from the relay
 pads as possible. Do not leave the soldering iron on any lead for more than 5
 seconds. Note If it is necessary to reapply the soldering iron
 to the pad, allow the connection to cool completely before reapplying the
 soldering iron.
2. Apply heat to the pads one at a time, and use the pick to gently pry the relay
 pins from the pads. Make sure that the solder is molten before prying. Caution Using excessive force on a soldered pad can result in
 lifting the PCB trace and ruining the board.
3. Remove the relay.
4. Clean the pads with isopropyl alcohol and cotton swabs.
5. Place the new relay on the PCB pads and solder.
6. Remove the excess flux with isopropyl alcohol and cotton swabs. Caution Do not use flux remover to clean the
 board after relay replacement.

#### Reassemble the Module

Secure the plastic safety shield using the four screws removed in Disassemble the
 Module, step 3.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2585

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2585-triggering.html language=enus -->
## TOPIC 00322: NI PXI-2585 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2585-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2585-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2585 can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2585. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigg

### NI PXI-2585 Triggering

The NI PXI-2585 can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2585.

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

The following table lists valid scan advanced outputs for the NI PXI-2585.

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

NI PXI-2585

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2585.html language=enus -->
## TOPIC 00323: NI PXI-2585

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2585.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2585.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2585 is a 10×1 multiplexer module for the PXI platform. The NI PXI-2585 is composed of 10 SPST armature nonlatching relays. For certain applications, you may need to increase the default settling time. Refer to Adding Additional Settling Time for more information. Switching inductive lo

### NI PXI-2585

The NI PXI-2585 is a 10×1 multiplexer module for the PXI platform. The NI PXI-2585 is
 composed of 10 SPST armature nonlatching relays.

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2585 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 10×1 Multiplexer | 2585/1-Wire 10x1 Mux(NISWITCH_TOPOLOGY_2585_1_WIRE_10X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Relay Forms
- Armature Relays
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2585 1-Wire 10×1 Multiplexer Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2586-10-spst-topology.html language=enus -->
## TOPIC 00324: NI PXI-2586 10-SPST Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2586-10-spst-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2586-10-spst-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2586 in the 10-SPST topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to close the relay of channel 2, call niSwitch_Connect(vi, "ch2", "com2"). To open the relay

### NI PXI-2586 10-SPST Topology

The following figure represents the NI PXI-2586 in the 10-SPST topology.

[IMAGE alt='image' src='GUID-632B03FF-0D9E-4DE6-96BA-C5D9D088BE13-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to close the relay of channel 2, call niSwitch_Connect(vi,
 "ch2", "com2"). To open the relay of channel 2, call
 niSwitch_Disconnect(vi, "ch2", "com2").

When scanning the NI PXI-2586, a typical scan list entry could be
 ch2->com2;. This entry closes the relay between CH2 and
 COM2.

#### Pinout

The following figure identifies the pins for the NI PXI-2586 in the 10-SPST
 topology.

[IMAGE alt='image' src='GUID-E8DECD19-D11E-4E8C-992C-A9F895DC2CB5-a5.gif']

Parent topic:

NI PXI-2586

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2586-5-dpst-topology.html language=enus -->
## TOPIC 00325: NI PXI-2586 5-DPST Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2586-5-dpst-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2586-5-dpst-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2586 in the 5-DPST topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to close the relay of channel 2, call niSwitch_Connect(vi, "ch2", "com2"). To open the relay

### NI PXI-2586 5-DPST Topology

The following figure represents the NI PXI-2586 in the 5-DPST topology.

[IMAGE alt='image' src='GUID-35D87886-6319-47CC-BEF5-25521200C67F-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to close the relay of channel 2, call niSwitch_Connect(vi,
 "ch2", "com2"). To open the relay of channel 2, call
 niSwitch_Disconnect(vi, "ch2", "com2").

When scanning the NI PXI-2586, a typical scan list entry could be
 ch2->com2;. This entry closes the relays between CH2+ and
 COM2+ and between CH2- and COM2-.

#### Pinout

The following figure identifies the pins for the NI PXI-2586 in the 5-DPST
 topology.

[IMAGE alt='image' src='GUID-DD668F2F-6253-4638-BC15-DFA01CAE76A4-a5.gif']

Parent topic:

NI PXI-2586

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2586-hardware-diagram.html language=enus -->
## TOPIC 00326: NI PXI-2586 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2586-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2586-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2586.

### NI PXI-2586 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2586.

[IMAGE alt='image' src='GUID-632B03FF-0D9E-4DE6-96BA-C5D9D088BE13-a5.gif']

Parent topic:

NI PXI-2586

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2586-relay-replacement.html language=enus -->
## TOPIC 00327: NI PXI-2586 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2586-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2586-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2586 uses electromechanical armature relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Number Potter & Brumfield (Tyco Electronics) RTB14005F (2-1419108-4) Complete the following sets of steps to disassemble your module and rep

### NI PXI-2586 Relay Replacement

The NI PXI-2586 uses electromechanical armature relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| Potter & Brumfield (Tyco Electronics) | RTB14005F (2-1419108-4) |

Complete the following sets of steps to disassemble your module and replace a failed
 relay.

#### Disassemble the Module

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your module from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table
 for relay locations. [IMAGE alt='image' src='GUID-4190842F-584D-4A0D-89F6-8410595B3D94-a5.gif'] 
 Channel Name
 Relay NameCH0
 K0CH1
 K1CH2
 K2CH3
 K3CH4
 K4CH5
 K5CH6
 K6CH7
 K7CH8
 K8CH9
 K9
3. Remove the four screws from the back of the relay board, and carefully peel off
 the plastic safety shield. 1
 Screws2
 Plastic safety shield
4. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. The different label types are shown in the following figure.
 [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']

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

If you have a surface mount rework station, replace the relay as you would any other
 surface mount part. Otherwise, complete the following steps to replace the
 relay:

1. Use the soldering iron and solder wick to remove as much solder from the relay
 pads as possible. Do not leave the soldering iron on any lead for more than 5
 seconds. Note If it is necessary to reapply the soldering iron
 to the pad, allow the connection to cool completely before reapplying the
 soldering iron.
2. Apply heat to the pads one at a time, and use the pick to gently pry the relay
 pins from the pads. Make sure that the solder is molten before prying. Caution Using excessive force on a soldered pad can result in
 lifting the PCB trace and ruining the board.
3. Remove the relay.
4. Clean the pads with isopropyl alcohol and cotton swabs.
5. Place the new relay on the PCB pads and solder.
6. Remove the excess flux with isopropyl alcohol and cotton swabs. Caution Do not use flux remover to clean the
 board after relay replacement.

#### Reassemble the Module

Secure the plastic safety shield using the four screws removed in Disassemble the
 Module, step 3.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI-2586

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2586-triggering.html language=enus -->
## TOPIC 00328: NI PXI-2586 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2586-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2586-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2586 can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI-2586. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigg

### NI PXI-2586 Triggering

The NI PXI-2586 can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2586.

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

The following table lists valid scan advanced outputs for the NI PXI-2586.

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

NI PXI-2586

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2586.html language=enus -->
## TOPIC 00329: NI PXI-2586

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2586.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2586.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2586 is a 10-channel general-purpose relay module for the PXI platform designed for switching and controlling power signals. The NI PXI-2586 is composed of 10 SPST armature nonlatching relays. For certain applications, you may need to increase the default settling time. Refer to Adding Ad

### NI PXI-2586

The NI PXI-2586 is a 10-channel general-purpose relay module for the PXI platform
 designed for switching and controlling power signals. The NI PXI-2586 is composed of 10
 SPST armature nonlatching relays.

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2586 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 10-SPST | 2586/10-SPST(NISWITCH_TOPOLOGY_2586_10_SPST) |  |  |
| 5-DPST | 2586/5-DPST(NISWITCH_TOPOLOGY_2586_5_DPST) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- Relay Forms
- Armature Relays
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2586 10-SPST Topology
- NI PXI-2586 5-DPST Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2590-2591-triggering.html language=enus -->
## TOPIC 00330: NI PXI-2590/2591 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2590-2591-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2590-2591-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2590/2591. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trig

### NI PXI-2590/2591 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2590/2591.

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

The following table lists valid scan advanced outputs for the NI PXI-2590/2591.

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

NI PXI-2590

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2590-4-1-multiplexer-topology.html language=enus -->
## TOPIC 00331: NI PXI-2590 4×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2590-4-1-multiplexer-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2590-4-1-multiplexer-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2590 in the 4×1 multiplexer topology. Making a Connection In this topology, you can connect channels by calling the niSwitch Connect Channels VI or the niSwitch_Connect function. To connect the CHx terminal to the COM terminal, disconnect the previously con

### NI PXI-2590 4×1 Multiplexer Topology

The following figure represents the NI PXI-2590 in the 4×1 multiplexer topology.

|  |
| --- |
|  |

#### Making a Connection

In this topology, you can connect channels by calling the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

To connect the CHx terminal to the COM terminal, disconnect the
 previously connected terminal from the COM.

For example, to connect CH2 to COM after connecting CH1 to COM, use the following
 code:

niSwitch_Disconnect(vi, "ch1", "com")

niSwitch_Connect(vi, "ch2", "com")

Note

niSwitch_DisconnectAll

Note

niSwitch_Disconnect(vi, "ch1", "com")

niSwitch_Connect(vi, "ch2", "com")

When scanning the NI PXI-2590, a typical scan list entry could be
 ch1->com;. This entry routes the signal connected to CH1 to
 COM.

Parent topic:

NI PXI-2590

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2590-hardware-diagram.html language=enus -->
## TOPIC 00332: NI PXI-2590 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2590-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2590-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2590.

### NI PXI-2590 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2590.

[IMAGE alt='image' src='GUID-EF77BE86-62E6-446B-BF6E-2342F343D8F8-a5.gif']

Parent topic:

NI PXI-2590

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2590.html language=enus -->
## TOPIC 00333: NI PXI-2590

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2590.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2590.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2590 is a multiplexer switch module for the PXI bus designed to handle RF signals up to 1.3 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2590 and possible operation modes. Topology Software Name Immediate Scanning 4×1 Multiplexer 2590/4x1 Mux(NISWITC

### NI PXI-2590

The NI PXI-2590 is a multiplexer switch module for the PXI bus designed to handle RF
 signals up to 1.3 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2590 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 4×1 Multiplexer | 2590/4x1 Mux(NISWITCH_TOPOLOGY_2590_4X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Operation Modes
- NI PXI-2590 4×1 Multiplexer Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2591-4-1-multiplexer-topology.html language=enus -->
## TOPIC 00334: NI PXI-2591 4×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2591-4-1-multiplexer-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2591-4-1-multiplexer-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2591 in the 4×1 multiplexer topology. Making a Connection In this topology, you can connect channels by calling the niSwitch Connect Channels VI or the niSwitch_Connect function. To connect the CHx terminal to the COM terminal, disconnect the previously con

### NI PXI-2591 4×1 Multiplexer Topology

The following figure represents the NI PXI-2591 in the 4×1 multiplexer topology.

|  |
| --- |
|  |

#### Making a Connection

In this topology, you can connect channels by calling the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

To connect the CHx terminal to the COM terminal, disconnect the
 previously connected terminal from the COM.

For example, to connect CH2 to COM after connecting CH1 to COM, use the following
 code:

niSwitch_Disconnect(vi, "ch1", "com")

niSwitch_Connect(vi, "ch2", "com")

Note

niSwitch_DisconnectAll

Note

niSwitch_Disconnect(vi, "ch1", "com")

niSwitch_Connect(vi, "ch2", "com")

When scanning the NI PXI-2591, a typical scan list entry could be
 ch1->com;. This entry routes the signal connected to CH1 to
 COM.

Parent topic:

NI PXI-2591

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2591-hardware-diagram.html language=enus -->
## TOPIC 00335: NI PXI-2591 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2591-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2591-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2591.

### NI PXI-2591 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2591.

[IMAGE alt='image' src='GUID-EA1B59A0-10FC-4699-9056-5FF3E46E5413-a5.gif']

Parent topic:

NI PXI-2591

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2591.html language=enus -->
## TOPIC 00336: NI PXI-2591

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2591.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2591.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2591 is a multiplexer switch module for the PXI bus designed to handle RF signals up to 4 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2591 and possible operation modes. Topology Software Name Immediate Scanning 4×1 Multiplexer 2591/4x1 Mux(NISWITCH_

### NI PXI-2591

The NI PXI-2591 is a multiplexer switch module for the PXI bus designed to handle RF
 signals up to 4 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2591 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 4×1 Multiplexer | 2591/4x1 Mux(NISWITCH_TOPOLOGY_2591_4X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Operation Modes
- NI PXI-2591 4×1 Multiplexer Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2594-2595-4-1-multiplexer-topology.html language=enus -->
## TOPIC 00337: NI PXI-2594/2595 4×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2594-2595-4-1-multiplexer-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2594-2595-4-1-multiplexer-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2594/2595 in the 4×1 multiplexer topology. Making a Connection In this topology, you can connect channels by calling the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to connect ch1 to com, call niSwitch_Connect (vi, "ch1", "co

### NI PXI-2594/2595 4×1 Multiplexer Topology

The following figure represents the NI PXI-2594/2595 in the 4×1 multiplexer topology.

|  |
| --- |
|  |

#### Making a Connection

In this topology, you can connect channels by calling the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to connect ch1 to com, call niSwitch_Connect (vi, "ch1",
 "com"). If you now want to connect ch2 to com, first disconnect the
 existing connection. The sequence of calls for this task is as follows:

niSwitch_Disconnect(vi, "ch1", "com")

niSwitch_Connect(vi, "ch2", "com")

Note

niSwitch_Disconnect(vi, "ch1", "com")

niSwitch_Connect(vi, "ch2", "com")

Note

niSwitch_DisconnectAll

When scanning the NI PXI-2594/2595, a typical scan list entry could be
 ch1->com;. This entry routes the signal connected to CH1 to
 COM.

Parent topic:

NI PXI-2594/2595

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2594-2595-front-panels.html language=enus -->
## TOPIC 00338: NI PXI-2594/2595 Front Panels

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2594-2595-front-panels.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2594-2595-front-panels.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2594 front panel. The following figure illustrates the NI PXI-2595 front panel.

### NI PXI-2594/2595 Front Panels

The following figure illustrates the NI PXI-2594 front panel.

[IMAGE alt='image' src='GUID-F6A0F7D7-3D36-4D8E-B10A-7CC1C8146111-a5.gif']

The following figure illustrates the NI PXI-2595 front panel.

[IMAGE alt='image' src='GUID-8AF36464-DBE0-4106-9BAD-1C7CF56983EA-a5.gif']

Parent topic:

NI PXI-2594/2595

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2594-2595-hardware-diagram.html language=enus -->
## TOPIC 00339: NI PXI-2594/2595 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2594-2595-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2594-2595-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2594/2595.

### NI PXI-2594/2595 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2594/2595.

[IMAGE alt='image' src='GUID-1B7C9B5A-098D-4915-BE55-29B7EE7F39A1-a5.gif']

Parent topic:

NI PXI-2594/2595

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2594-2595-triggering.html language=enus -->
## TOPIC 00340: NI PXI-2594/2595 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2594-2595-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2594-2595-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2594/2595. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trig

### NI PXI-2594/2595 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2594/2595.

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

The following table lists valid scan advanced outputs for the NI PXI-2594/2595.

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

NI PXI-2594/2595

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2594-2595.html language=enus -->
## TOPIC 00341: NI PXI-2594/2595

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2594-2595.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2594-2595.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2594 and the NI PXI-2595 are multiplexer switch modules for the PXI bus designed to handle RF signals up to 2.5 GHz (NI PXI-2594) and 5 GHz (NI PXI-2595). NI PXI-2594 Operation Modes The following table lists the supported topology of the NI PXI-2594 and possible operation modes. Topology

### NI PXI-2594/2595

The NI PXI-2594 and the NI PXI-2595 are multiplexer switch modules for the PXI bus
 designed to handle RF signals up to 2.5 GHz (NI PXI-2594) and 5 GHz (NI PXI-2595).

#### NI PXI-2594 Operation Modes

The following table lists the supported topology of the NI PXI-2594 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 4×1 Multiplexer | 2594/4x1 Mux(NISWITCH_TOPOLOGY_2594_4X1_MUX) |  |  |

#### NI PXI-2595 Operation Modes

The following table lists the supported topology of the NI PXI-2595 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 4×1 Multiplexer | 2595/4x1 Mux(NISWITCH_TOPOLOGY_2595_4X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Topologies
- Operation Modes
- NI PXI-2594/2595 4×1 Multiplexer Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2596-dual-6-1-multiplexer-topology.html language=enus -->
## TOPIC 00342: NI PXI-2596 Dual 6×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2596-dual-6-1-multiplexer-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2596-dual-6-1-multiplexer-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2596 in the dual 6×1 multiplexer topology. Making a Connection In this topology, you can connect channels by calling the niSwitch Connect Channels VI or the niSwitch_Connect function. To connect the CHnx terminal to the COMx terminal, disconnect the previou

### NI PXI-2596 Dual 6×1 Multiplexer Topology

The following figure represents the NI PXI-2596 in the dual 6×1 multiplexer topology.

[IMAGE alt='image' src='GUID-98721A76-644C-41D9-B20E-5B4E4C470323-a5.gif']

#### Making a Connection

In this topology, you can connect channels by calling the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

To connect the CHnx terminal to the COMx
 terminal, disconnect the previously connected terminal from the
 COMx.

For example, to connect ch1A to comA, call niSwitch_Connect (vi, "ch1A",
 "comA"). If you now want to connect ch2A to comA, first disconnect the
 existing connection. The sequence of calls for this task is as follows:

niSwitch_Disconnect (vi, "ch1A", "comA")

niSwitch_Connect (vi, "ch2A", "comA")

Note

When scanning the NI PXI-2596, a typical scan list entry could be
 ch1A->comA;. This entry routes the signal connected to CH1A
 to COMA.

Parent topic:

NI PXI-2596

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2596-front-panel.html language=enus -->
## TOPIC 00343: NI PXI-2596 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2596-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2596-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2596 front panel.

### NI PXI-2596 Front Panel

The following figure illustrates the NI PXI-2596 front panel.

[IMAGE alt='image' src='GUID-B2AD1B6A-050B-4212-B194-34CB80C22B75-a5.gif']

Parent topic:

NI PXI-2596

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2596-hardware-diagram.html language=enus -->
## TOPIC 00344: NI PXI-2596 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2596-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2596-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2596.

### NI PXI-2596 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2596.

[IMAGE alt='image' src='GUID-1B360647-D558-48D8-81FB-87A6B7F979F4-a5.gif']

Parent topic:

NI PXI-2596

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2596-triggering.html language=enus -->
## TOPIC 00345: NI PXI-2596 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2596-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2596-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2596. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2596 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2596.

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

The following table lists valid scan advanced outputs for the NI PXI-2596.

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

NI PXI-2596

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2596.html language=enus -->
## TOPIC 00346: NI PXI-2596

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2596.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2596.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2596 is a multiplexer switch module for the PXI bus designed to handle RF signals up to 26.5 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2596 and possible operation modes. Topology Software Name Immediate Scanning Dual 6x1 Multiplexer 2596/Dual 6x1

### NI PXI-2596

The NI PXI-2596 is a multiplexer switch module for the PXI bus designed to handle RF
 signals up to 26.5 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2596 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Dual 6x1 Multiplexer | 2596/Dual 6x1 Mux(NISWITCH_TOPOLOGY_2596_DUAL_6X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Operation Modes
- NI PXI-2596 Dual 6×1 Multiplexer Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2597-6-1-terminated-multiplexer-topolo.html language=enus -->
## TOPIC 00347: NI PXI-2597 6×1 Terminated Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2597-6-1-terminated-multiplexer-topolo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2597-6-1-terminated-multiplexer-topolo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2597 in the 6×1 terminated multiplexer topology. The terminators on the NI PXI-2597 are rated for 1 W average power at 25 °C, with power on all terminators not to exceed 3 W. Terminators cannot withstand the full rated power of the NI PXI-2597. Making a C

### NI PXI-2597 6×1 Terminated Multiplexer Topology

The following figure represents the NI PXI-2597 in the 6×1 terminated multiplexer
 topology.

[IMAGE alt='image' src='GUID-4D2E452C-9625-4912-BAE6-5920CCE5F14E-a5.gif']

Caution

cannot

#### Making a Connection

In this topology, you can connect channels by calling the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

To connect the CHx terminal to the COM terminal, disconnect the
 previously connected terminal from the COM.

For example, to connect ch1 to com, call niSwitch_Connect (vi, "ch1",
 "com"). If you now want to connect ch2 to com, first disconnect the
 existing connection. The sequence of calls for this task is as follows:

niSwitch_Disconnect (vi, "ch1", "com")

niSwitch_Connect (vi, "ch2", "com")

Note

not

Note

When scanning the NI PXI-2597, a typical scan list entry could be
 ch2->com;. This entry routes signal connected to ch2 to
 com.

Parent topic:

NI PXI-2597

Related concepts:

- Operation Modes

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2597-front-panel.html language=enus -->
## TOPIC 00348: NI PXI-2597 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2597-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2597-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2597 front panel.

### NI PXI-2597 Front Panel

The following figure illustrates the NI PXI-2597 front panel.

[IMAGE alt='image' src='GUID-260DC990-EBDA-4B4C-A70E-0B8FB7B7ADE4-a5.gif']

Parent topic:

NI PXI-2597

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2597-hardware-diagram.html language=enus -->
## TOPIC 00349: NI PXI-2597 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2597-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2597-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2597.

### NI PXI-2597 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2597.

[IMAGE alt='image' src='GUID-979E1190-E863-475C-B017-19230DC3E7BD-a5.gif']

Parent topic:

NI PXI-2597

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2597-triggering.html language=enus -->
## TOPIC 00350: NI PXI-2597 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2597-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2597-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2597. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2597 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2597.

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

The following table lists valid scan advanced outputs for the NI PXI-2597.

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

NI PXI-2597

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2597.html language=enus -->
## TOPIC 00351: NI PXI-2597

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2597.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2597.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2597 is a terminated multiplexer switch module for the PXI bus designed to handle RF signals up to 26.5 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2597 and possible operation modes. Topology Software Name Immediate Scanning 6x1 Terminated Multiplex

### NI PXI-2597

The NI PXI-2597 is a terminated multiplexer switch module for the PXI bus designed to
 handle RF signals up to 26.5 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2597 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 6x1 Terminated Multiplexer | 2597/6x1 Terminated Mux(NISWITCH_TOPOLOGY_2597_6X1_TERMINATED_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Operation Modes
- NI PXI-2597 6×1 Terminated Multiplexer Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2598-dual-transfer-switch-topology.html language=enus -->
## TOPIC 00352: NI PXI-2598 Dual Transfer Switch Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2598-dual-transfer-switch-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2598-dual-transfer-switch-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figures represents the NI PXI-2598 in the dual transfer switch topology. The following figures show the two states of each transfer switch, reset and set. Application The dual transfer switch topology of the NI PXI-2598 enables customers to insert and remove components in a high-freque

### NI PXI-2598 Dual Transfer Switch Topology

The following figures represents the NI PXI-2598 in the dual transfer switch topology.

[IMAGE alt='image' src='GUID-DD20141B-F4A8-407F-94E4-7108AE86A466-a5.gif']

The following figures show the two states of each transfer switch, reset and set.

[IMAGE alt='image' src='GUID-AFDE967C-DD77-45E8-A41A-F76B590C0D63-a5.gif']

Application

The dual transfer switch topology of the NI PXI-2598 enables customers to insert and
 remove components in a high-frequency signal path. To insert the DUT, configure the
 transfer switch in its reset state. To remove the DUT, configure the transfer switch in
 its set state.

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

To set the transfer switch, disconnect the nc terminal from com, and connect no to
 com.

For example, to set the transfer switch K0, use the following code:

niSwitch_Disconnect(vi, "nc0", "com0")

niSwitch_Connect(vi, "no0", "com0")

Note

niSwitch_DisconnectAll

Note

niSwitch_Disconnect(vi, "nc0", "com0")

not

niSwitch_Connect(vi,
 "no0", "com0")

niSwitch_Disconnect(vi,
 "no0", "com0")

not

niSwitch_Connect(vi, "nc0", "com0")

To reset the transfer switch, disconnect the no terminal from com, and connect nc to
 com.

For example, to reset the transfer switch K0, use the following code:

niSwitch_Disconnect(vi, "no0", "com0")

niSwitch_Connect(vi, "nc0", "com0")

When scanning the NI PXI-2598, a typical scan list entry could be
 nc0->com0;. This entry resets transfer switch K0.

Parent topic:

NI PXI-2598

Related concepts:

- Transfer Switches
- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2598-front-panel.html language=enus -->
## TOPIC 00353: NI PXI-2598 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2598-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2598-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2598 front panel.

### NI PXI-2598 Front Panel

The following figure illustrates the NI PXI-2598 front panel.

[IMAGE alt='image' src='GUID-5321BC92-470A-4C44-B864-4DD0A0212DFA-a5.gif']

Parent topic:

NI PXI-2598

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2598-hardware-diagram.html language=enus -->
## TOPIC 00354: NI PXI-2598 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2598-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2598-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figures show the hardware diagram for the NI PXI-2598.

### NI PXI-2598 Hardware Diagram

The following figures show the hardware diagram for the NI PXI-2598.

[IMAGE alt='image' src='GUID-DD20141B-F4A8-407F-94E4-7108AE86A466-a5.gif']

Parent topic:

NI PXI-2598

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2598-triggering.html language=enus -->
## TOPIC 00355: NI PXI-2598 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2598-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2598-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2598. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2598 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2598.

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

The following table lists valid scan advanced outputs for the NI PXI-2598.

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

NI PXI-2598

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2598.html language=enus -->
## TOPIC 00356: NI PXI-2598

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2598.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2598.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2598 is an 2-channel, transfer switch module for the PXI platform designed to handle RF signals up to 26.5 GHz. The NI PXI-2598 is composed of transfer switch relays. Operation Modes The following table lists the supported topology of the NI PXI-2598 and possible operation modes. Topology

### NI PXI-2598

The NI PXI-2598 is an 2-channel, transfer switch module for the PXI platform designed to
 handle RF signals up to 26.5 GHz. The NI PXI-2598 is composed of transfer switch relays.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2598 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Dual Transfer | 2598/Dual Transfer(NISWITCH_TOPOLOGY_2598_DUAL_TRANSFER) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Transfer Switches
- RF Switching Considerations
- Operation Modes
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2599-2-spdt-topology.html language=enus -->
## TOPIC 00357: NI PXI-2599 2-SPDT Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2599-2-spdt-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2599-2-spdt-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2599 in the 2-SPDT general-purpose topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to connect the NO terminal of channel 1 to the COM terminal of channel 1, cal

### NI PXI-2599 2-SPDT Topology

The following figure represents the NI PXI-2599 in the 2-SPDT general-purpose topology.

[IMAGE alt='image' src='GUID-D8F4FD46-24BD-4616-B5DE-44B355995017-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to connect the NO terminal of channel 1 to the COM terminal of channel
 1, call niSwitch_Connect (vi, "no1", "com1"). If you now want to
 connect NC1 to COM1, first disconnect the existing connection. The sequence of calls
 for this task is as follows:

niSwitch_Disconnect(vi, "no1", "com1")

niSwitch_Connect(vi, "nc1", "com1")

Note

niSwitch_Disconnect(vi, "no1", "com1")

niSwitch_Connect(vi, "nc1", "com1")

Note

x

niSwitch_DisconnectAll

When scanning the NI PXI-2599, a typical scan list entry could be
 nc1->com1;. This entry routes the signal connected to NC1 to
 COM1.

Parent topic:

NI PXI-2599

Related concepts:

- General-Purpose Topologies
- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2599-front-panel.html language=enus -->
## TOPIC 00358: NI PXI-2599 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2599-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2599-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2599 front panel.

### NI PXI-2599 Front Panel

The following figure illustrates the NI PXI-2599 front panel.

[IMAGE alt='image' src='GUID-2324047A-A245-4272-8876-8BAAEE3DD4B8-a5.gif']

Parent topic:

NI PXI-2599

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2599-hardware-diagram.html language=enus -->
## TOPIC 00359: NI PXI-2599 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2599-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2599-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2599.

### NI PXI-2599 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2599.

[IMAGE alt='image' src='GUID-AC7113D1-9638-4457-872E-9CDED4F1005C-a5.gif']

Parent topic:

NI PXI-2599

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2599-triggering.html language=enus -->
## TOPIC 00360: NI PXI-2599 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2599-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2599-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2599. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2599 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2599.

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

The following table lists valid scan advanced outputs for the NI PXI-2599.

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

NI PXI-2599

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2599.html language=enus -->
## TOPIC 00361: NI PXI-2599

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2599.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2599.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2599 is an 2-channel, general-purpose switch module for the PXI platform designed to handle RF signals up to 26.5 GHz. The NI PXI-2599 is composed of 2-SPDT relays. Operation Modes The following table lists the supported topology of the NI PXI-2599 and possible operation modes. Topology S

### NI PXI-2599

The NI PXI-2599 is an 2-channel, general-purpose switch module for the PXI platform
 designed to handle RF signals up to 26.5 GHz. The NI PXI-2599 is composed of 2-SPDT
 relays.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2599 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 2-SPDT | 2599/2-SPDT(NISWITCH_TOPOLOGY_2599_2_SPDT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- RF Switching Considerations
- NI PXI-2599 2-SPDT Topology
- Operation Modes
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2720-hardware-diagram.html language=enus -->
## TOPIC 00362: NI PXI-2720 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2720-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2720-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2720. Resistance values are nominal. Please see the NI PXI-2720 Specifications for resistor values and accuracy information The following table lists relay names for the NI PXI-2720. Relays kb0r0, kb0r1...kb0r7 kb1r0, kb1r1...kb1r7 kb2

### NI PXI-2720 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2720.

[IMAGE alt='image' src='GUID-C9FE62C4-B70F-463C-998A-3824BB11B1FD-a5.gif']

Note

NI PXI-2720
 Specifications

The following table lists relay names for the NI PXI-2720.

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
| kb0...kb9 |
| kb0shunt...kb9shunt |
| kbc01, kbc12...kbc89 |
| ktest0, ktest1...ktest5 |

Parent topic:

NI PXI-2720

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2720-independent-topology.html language=enus -->
## TOPIC 00363: NI PXI-2720 Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2720-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2720-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2720 in the independent topology. Bank connect relays allow adjacent banks or channels to connect together internally. For example, you can connect two or more adjacent channels together to create a potentiometer, a voltage divider, or a multi-segment res

### NI PXI-2720 Independent Topology

The following figure represents the NI PXI-2720 in the independent topology.

[IMAGE alt='image' src='GUID-C9FE62C4-B70F-463C-998A-3824BB11B1FD-a5.gif']

Note

#### Making a Connection

ni.com/info

272xOverview

When a bank relay is closed, the corresponding
 resistor is placed in parallel with the low resistance of the relay, which nominally
 equates to a zero Ω shunt. Closing any of the 8 bank relays in a given bank
 decreases the resistance of that bank.

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
 nominally. This allows the NI PXI-2720 module to pass signals with minimal
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

The following figure identifies the pins for the NI PXI-2720.

[IMAGE alt='image' src='GUID-D9C0DF18-869B-4710-971F-F045B333804D-a5.gif']

Note

Parent topic:

NI PXI-2720

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2720-relay-replacement.html language=enus -->
## TOPIC 00364: NI PXI-2720 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2720-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2720-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2720 uses reed relays. The NI PXI-2720 uses a custom lead length to meet safety standards. Trim leads per rework instructions or use one of the custom relays from the relay kit. Refer to the following tables for information about ordering replacement relays. Relay Relay Manufacturer Par

### NI PXI-2720 Relay Replacement

Note

Refer to the following tables for information about ordering replacement relays.

| Relay | Relay Manufacturer | Part Number |
| --- | --- | --- |
| All Relays | Coto | 9117-0001 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 781451-10 |

Complete the following sets of steps to disassemble your module, replace a failed relay,
 and reassemble your module.

#### Disassemble the Module

1. Ground yourself using a grounding strap or a ground connected to the PXI
 chassis. Note Properly grounding yourself prevents damage to the
 module from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figure and table
 for relay locations. NI PXI 2720 Relay Map 
 [IMAGE alt='image' src='GUID-0DDE047F-3487-487A-91D3-0720F23334A4-a5.gif'] 
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorkb0shunt
 K1
 kb2r2
 K30
 kb5shunt
 K59
 kb7r2
 K88kb0
 K2
 kb2r3
 K31
 kb5
 K60
 kb7r3
 K89kbc01
 K3
 kb2r4
 K32
 kbc56
 K61
 kb7r4
 K90ktest0
 K4
 kb2r5
 K33
 ktest3
 K62
 kb7r5
 K91kb0r0
 K5
 kb2r6
 K34
 kb5r0
 K63
 kb7r6
 K92kb0r1
 K6
 kb2r7
 K35
 kb5r1
 K64
 kb7r7
 K93kb0r2
 K7
 kb3shunt
 K36
 kb5r2
 K65
 kb8shunt
 K94kb0r3
 K8
 kb3
 K37
 kb5r3
 K66
 kb8
 K95kb0r4
 K9
 kbc34
 K38
 kb5r4
 K67
 kbc89
 K96kb0r5
 K10
 ktest2
 K39
 kb5r5
 K68
 kb8r0
 K97kb0r6
 K11
 kb3r0
 K40
 kb5r6
 K69
 kb8r1
 K98kb0r7
 K12
 kb3r1
 K41
 kb5r7
 K70
 kb8r2
 K99kb1shunt
 K13
 kb3r2
 K42
 kb6shunt
 K71
 kb8r3
 K100kb1
 K14
 kb3r3
 K43
 kb6
 K72
 kb8r4
 K101kbc12
 K15
 kb3r4
 K44
 kbc67
 K73
 kb8r5
 K102test1
 K16
 kb3r5
 K45
 kb6r0
 K74
 kb8r6
 K103kb1r0
 K17
 kb3r6
 K46
 kb6r1
 K75
 kb8r7
 K104kb1r1
 K18
 kb3r7
 K47
 kb6r2
 K76
 kb9shunt
 K105kb1r2
 K19
 kb4shunt
 K48
 kb6r3
 K77
 kb9
 K106kb1r3
 K20
 kb4
 K49
 kb6r4
 K78
 test5
 K108kb1r4
 K21
 kbc45
 K50
 kb6r5
 K79
 kb9r0
 K109kb1r5
 K22
 kb4r0
 K51
 kb6r7
 K80
 kb9r1
 K110kb1r6
 K23
 kb4r1
 K52
 kb6r6
 K80
 kb9r2
 K111kb1r7
 K24
 kb4r2
 K53
 kb7shunt
 K82
 kb9r3
 K112kb2shunt
 K25
 kb4r3
 K54
 kb7
 K83
 kb9r4
 K113kb2
 K26
 kb4r4
 K55
 kbc78
 K84
 kb9r5
 K114kbc23
 K27
 kb4r5
 K56
 test4
 K85
 kb9r6
 K115kb2r0
 K28
 kb4r6
 K57
 kb7r0
 K86
 kb9r7
 K116kb2r1
 K29
 kb4r7
 K58
 kb7r1
 K87
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

The NI PXI-2720 uses lead-free assemblies.

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

NI PXI-2720

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2720-triggering.html language=enus -->
## TOPIC 00365: NI PXI-2720 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2720-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2720-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2720. NI recommends using the low-level relay control API instead of hardware triggers. Hardware triggers are supported but because of the nature of the independent topology, if hardware triggers are used, "no action" mode s

### NI PXI-2720 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2720. NI recommends
 using the low-level relay control API instead of hardware triggers. Hardware
 triggers are supported but because of the nature of the independent topology, if
 hardware triggers are used, "no action" mode should be used. Otherwise, each scan
 list entry must incorporate the state for all channels.

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

The following table lists valid scan advanced outputs for the NI PXI-2720.

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

NI PXI-2720

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2720.html language=enus -->
## TOPIC 00366: NI PXI-2720

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2720.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2720.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2720 is a programmable resistor module for the PXI platform. The NI PXI-2720 is composed of reed relays in parallel with discrete resistors. The NI PXI-2720 has 10 channels that can nominally switch from 0 to 255 Ω in 1 Ω steps. NI has created a set of reference VIs that you can use to

### NI PXI-2720

Note

ni.com/info

272xOverview

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2720 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Ten 8-bit channels | 2720/Independent(NISWITCH_TOPOLOGY_2720_INDEPENDENT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2720 Independent Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2722-hardware-diagram.html language=enus -->
## TOPIC 00367: NI PXI-2722 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2722-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2722-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2722. Resistance values are nominal. Please see the NI PXI-2722 Specifications for resistor values and accuracy information The following table lists relay names for the NI PXI-2722. Relays kb0r0, kb0r1...kb0r7 kb1r0, kb1r1...kb1r7 kb2

### NI PXI-2722 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2722.

[IMAGE alt='image' src='GUID-CC19E561-D6AB-497B-8A50-0B72B7AF4E45-a5.gif']

Note

NI PXI-2722
 Specifications

The following table lists relay names for the NI PXI-2722.

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
| kb0...kb9 |
| kb0shunt...kb9shunt |
| kbc01, kbc12...kbc89 |
| ktest0, ktest1...ktest5 |

Parent topic:

NI PXI-2722

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2722-independent-topology.html language=enus -->
## TOPIC 00368: NI PXI-2722 Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2722-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2722-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2722 in the independent topology. Bank connect relays allow adjacent banks or channels to connect together internally. For example, you can connect two or more adjacent channels together to create a potentiometer, a voltage divider, or a multi-segment res

### NI PXI-2722 Independent Topology

The following figure represents the NI PXI-2722 in the independent topology.

[IMAGE alt='image' src='GUID-CC19E561-D6AB-497B-8A50-0B72B7AF4E45-a5.gif']

Note

#### Making a Connection

ni.com/info

272xOverview

When a bank relay is closed, the corresponding resistor is placed in parallel
 with the low resistance of the relay, which nominally equates to a zero Ω shunt.
 Closing any of the 8 bank relays in a given bank decreases the resistance of that
 bank.

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
 nominally. This allows the NI PXI-2722 module to pass signals with minimal
 attenuation. On 16-bit modules (NI PXI-2722 and NI PXIe-2727), closing the upper
 bank's shunt relay reduces the resistance when outputting values less than 64 Ω.

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

The following figure identifies the pins for the NI PXI-2722.

[IMAGE alt='image' src='GUID-FDFFAECB-8C96-4313-8AD5-0CD719AFEE49-a5.gif']

Note

Parent topic:

NI PXI-2722

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2722-relay-replacement.html language=enus -->
## TOPIC 00369: NI PXI-2722 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2722-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2722-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2722 uses reed relays. The NI PXI-2722 uses a custom lead length to meet safety standards. Trim leads per rework instructions or use one of the custom relays from the relay kit. Refer to the following tables for information about ordering replacement relays. Relay Relay Manufacturer Par

### NI PXI-2722 Relay Replacement

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

1. Ground yourself using a grounding strap or a ground connected to the PXI
 chassis. Note Properly grounding yourself prevents damage to
 your module from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figures and table
 for relay locations. NI PXI 2722 Relay Map 
 [IMAGE alt='image' src='GUID-A241770C-99B8-493B-8E1E-7230F1610116-a5.gif'] 
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorkb0shunt
 K1
 kb2r2
 K30
 kb5shunt
 K59
 kb7r2
 K88kb0
 K2
 kb2r3
 K31
 kb5
 K60
 kb7r3
 K89kbc01
 K3
 kb2r4
 K32
 kbc56
 K61
 kb7r4
 K90test0
 K4
 kb2r5
 K33
 test3
 K62
 kb7r5
 K91kb0r0
 K5
 kb2r6
 K34
 kb5r0
 K63
 kb7r6
 K92kb0r1
 K6
 kb2r7
 K35
 kb5r1
 K64
 kb7r7
 K93kb0r2
 K7
 kb3shunt
 K36
 kb5r2
 K65
 kb8shunt
 K94kb0r3
 K8
 kb3
 K37
 kb5r3
 K66
 kb8
 K95kb0r4
 K9
 kbc34
 K38
 kb5r4
 K67
 kbc89
 K96kb0r5
 K10
 test2
 K39
 kb5r5
 K68
 kb8r0
 K97kb0r6
 K11
 kb3r0
 K40
 kb5r6
 K69
 kb8r1
 K98kb0r7
 K12
 kb3r1
 K41
 kb5r7
 K70
 kb8r2
 K99kb1shunt
 K13
 kb3r2
 K42
 kb6shunt
 K71
 kb8r3
 K100kb1
 K14
 kb3r3
 K43
 kb6
 K72
 kb8r4
 K101kbc12
 K15
 kb3r4
 K44
 kbc67
 K73
 kb8r5
 K102test1
 K16
 kb3r5
 K45
 kb6r0
 K74
 kb8r6
 K103kb1r0
 K17
 kb3r6
 K46
 kb6r1
 K75
 kb8r7
 K104kb1r1
 K18
 kb3r7
 K47
 kb6r2
 K76
 kb9shunt
 K105kb1r2
 K19
 kb4shunt
 K48
 kb6r3
 K77
 kb9
 K106kb1r3
 K20
 kb4
 K49
 kb6r4
 K78
 test5
 K108kb1r4
 K21
 kbc45
 K50
 kb6r5
 K79
 kb9r0
 K109kb1r5
 K22
 kb4r0
 K51
 kb6r7
 K80
 kb9r1
 K110kb1r6
 K23
 kb4r1
 K52
 kb6r6
 K80
 kb9r2
 K111kb1r7
 K24
 kb4r2
 K53
 kb7shunt
 K82
 kb9r3
 K112kb2shunt
 K25
 kb4r3
 K54
 kb7
 K83
 kb9r4
 K113kb2
 K26
 kb4r4
 K55
 kbc78
 K84
 kb9r5
 K114kbc23
 K27
 kb4r5
 K56
 test4
 K85
 kb9r6
 K115kb2r0
 K28
 kb4r6
 K57
 kb7r0
 K86
 kb9r7
 K116kb2r1
 K29
 kb4r7
 K58
 kb7r1
 K87
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

The NI PXI-2722 uses lead-free assemblies.

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

NI PXI-2722

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2722-triggering.html language=enus -->
## TOPIC 00370: NI PXI-2722 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2722-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2722-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2722. NI recommends using the low-level relay control API instead of hardware triggers. Hardware triggers are supported but because of the nature of the independent topology, if hardware triggers are used, "no action" mode s

### NI PXI-2722 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2722. NI recommends
 using the low-level relay control API instead of hardware triggers. Hardware
 triggers are supported but because of the nature of the independent topology, if
 hardware triggers are used, "no action" mode should be used. Otherwise, each scan
 list entry must incorporate the state for all channels.

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

The following table lists valid scan advanced outputs for the NI PXI-2722.

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

NI PXI-2722

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2722.html language=enus -->
## TOPIC 00371: NI PXI-2722

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2722.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2722.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2722 is a programmable resistor module for the PXI platform. The NI PXI-2722 is composed of reed relays in parallel with discrete resistors. The NI PXI-2722 has five channels that can nominally switch from 0 to 16,383 Ω in 0.25 Ω steps. NI has created a set of reference VIs that you can

### NI PXI-2722

Note

ni.com/info

272xOverview

Note

#### Operation Modes

The following table lists the supported topology of the NI PXI-2722 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Five 16-bit channels | 2722/Independent(NISWITCH_TOPOLOGY_2722_INDEPENDENT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI-2722 Independent Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2746.html language=enus -->
## TOPIC 00372: NI PXI-2746

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2746.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2746.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXIe-2746 (NI 2746) is a quad 4×1 multiplexer switch module for the PXI Express bus that can carry 50 Ω RF signals up to 3 GHz. Operation Modes The following table lists the supported topology of the NI 2746 and possible operation modes. Topology Software Name Immediate Scanning Quad 4×1 Mult

### NI PXI-2746

The NI PXIe-2746 (NI 2746) is a quad 4×1 multiplexer switch module for the PXI Express
 bus that can carry 50 Ω RF signals up to 3 GHz.

#### Operation Modes

The following table lists the supported topology of the NI 2746 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Quad 4×1 Multiplexer | 2746/Quad 4x1 Mux(NISWITCH_TOPOLOGY_2746_QUAD_4X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- RF Switching Considerations
- Topologies
- Operation Modes
- NI Quad PXIe-2746 4×1 Multiplexer (Quad SP4T) Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2796-dual-6-1-multiplexer-topology.html language=enus -->
## TOPIC 00373: NI PXI-2796 Dual 6×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2796-dual-6-1-multiplexer-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2796-dual-6-1-multiplexer-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2796 in the dual 6×1 multiplexer topology. Making a Connection In this topology, you can connect channels by calling the niSwitch Connect Channels VI or the niSwitch_Connect function. To connect the CHnx terminal to the COMx terminal, disconnect the previou

### NI PXI-2796 Dual 6×1 Multiplexer Topology

The following figure represents the NI PXI-2796 in the dual 6×1 multiplexer topology.

[IMAGE alt='image' src='GUID-98721A76-644C-41D9-B20E-5B4E4C470323-a5.gif']

#### Making a Connection

In this topology, you can connect channels by calling the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

To connect the CHnx terminal to the COMx
 terminal, disconnect the previously connected terminal from the
 COMx.

For example, to connect ch1A to comA, call niSwitch_Connect (vi, "ch1A",
 "comA"). If you now want to connect ch2A to comA, first disconnect the
 existing connection. The sequence of calls for this task is as follows:

niSwitch_Disconnect (vi, "ch1A", "comA")

niSwitch_Connect (vi, "ch2A", "comA")

Note

When scanning the NI PXI-2796, a typical scan list entry could be
 ch1A->comA;. This entry routes the signal connected to CH1A
 to COMA.

Parent topic:

NI PXI-2796

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2796-front-panel.html language=enus -->
## TOPIC 00374: NI PXI-2796 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2796-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2796-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2796 front panel.

### NI PXI-2796 Front Panel

The following figure illustrates the NI PXI-2796 front panel.

[IMAGE alt='image' src='GUID-9289F149-3EB9-43B4-883B-4F97AF1C94E0-a5.gif']

Parent topic:

NI PXI-2796

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2796-hardware-diagram.html language=enus -->
## TOPIC 00375: NI PXI-2796 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2796-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2796-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2796.

### NI PXI-2796 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2796.

[IMAGE alt='image' src='GUID-1B360647-D558-48D8-81FB-87A6B7F979F4-a5.gif']

Parent topic:

NI PXI-2796

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2796-triggering.html language=enus -->
## TOPIC 00376: NI PXI-2796 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2796-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2796-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2796. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2796 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2796.

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

The following table lists valid scan advanced outputs for the NI PXI-2796.

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

NI PXI-2796

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2796.html language=enus -->
## TOPIC 00377: NI PXI-2796

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2796.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2796.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2796 is a multiplexer switch module for the PXI bus designed to handle RF signals up to 40 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2796 and possible operation modes. Topology Software Name Immediate Scanning Dual 6x1 Multiplexer 2796/Dual 6x1 Mu

### NI PXI-2796

The NI PXI-2796 is a multiplexer switch module for the PXI bus designed to handle RF
 signals up to 40 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2796 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Dual 6x1 Multiplexer | 2796/Dual 6x1 Mux(NISWITCH_TOPOLOGY_2796_DUAL_6X1_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Operation Modes
- NI PXI-2796 Dual 6×1 Multiplexer Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2797-6-1-terminated-multiplexer-topolo.html language=enus -->
## TOPIC 00378: NI PXI-2797 6×1 Terminated Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2797-6-1-terminated-multiplexer-topolo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2797-6-1-terminated-multiplexer-topolo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2797 in the 6×1 terminated multiplexer topology. The terminators on the NI PXI-2797 are rated for 1 W average power at 25 °C, with power on all terminators not to exceed 3 W. Terminators cannot withstand the full rated power of the NI PXI-2797. Making a C

### NI PXI-2797 6×1 Terminated Multiplexer Topology

The following figure represents the NI PXI-2797 in the 6×1 terminated multiplexer
 topology.

[IMAGE alt='image' src='GUID-4D2E452C-9625-4912-BAE6-5920CCE5F14E-a5.gif']

Caution

cannot

#### Making a Connection

In this topology, you can connect channels by calling the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

To connect the CHx terminal to the COM terminal, disconnect the
 previously connected terminal from the COM.

For example, to connect ch1 to com, call niSwitch_Connect (vi, "ch1",
 "com"). If you now want to connect ch2 to com, first disconnect the
 existing connection. The sequence of calls for this task is as follows:

niSwitch_Disconnect (vi, "ch1", "com")

niSwitch_Connect (vi, "ch2", "com")

Note

not

Note

When scanning the NI PXI-2797, a typical scan list entry could be
 ch2->com;. This entry routes signal connected to ch2 to
 com.

Parent topic:

NI PXI-2797

Related concepts:

- Operation Modes

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2797-front-panel.html language=enus -->
## TOPIC 00379: NI PXI-2797 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2797-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2797-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2797 front panel.

### NI PXI-2797 Front Panel

The following figure illustrates the NI PXI-2797 front panel.

[IMAGE alt='image' src='GUID-CB208B0E-55B3-4726-94C3-3ACB238A8C22-a5.gif']

Parent topic:

NI PXI-2797

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2797-hardware-diagram.html language=enus -->
## TOPIC 00380: NI PXI-2797 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2797-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2797-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2797.

### NI PXI-2797 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2797.

[IMAGE alt='image' src='GUID-979E1190-E863-475C-B017-19230DC3E7BD-a5.gif']

Parent topic:

NI PXI-2797

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2797-triggering.html language=enus -->
## TOPIC 00381: NI PXI-2797 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2797-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2797-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2797. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2797 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2797.

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

The following table lists valid scan advanced outputs for the NI PXI-2797.

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

NI PXI-2797

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2797.html language=enus -->
## TOPIC 00382: NI PXI-2797

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2797.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2797.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2797 is a terminated multiplexer switch module for the PXI bus designed to handle RF signals up to 40 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2797 and possible operation modes. Topology Software Name Immediate Scanning 6x1 Terminated Multiplexer

### NI PXI-2797

The NI PXI-2797 is a terminated multiplexer switch module for the PXI bus designed to
 handle RF signals up to 40 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2797 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 6x1 Terminated Multiplexer | 2797/6x1 Terminated Mux(NISWITCH_TOPOLOGY_2797_6X1_TERMINATED_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Operation Modes
- NI PXI-2797 6×1 Terminated Multiplexer Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2798-dual-transfer-switch-topology.html language=enus -->
## TOPIC 00383: NI PXI-2798 Dual Transfer Switch Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2798-dual-transfer-switch-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2798-dual-transfer-switch-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figures represents the NI PXI-2798 in the dual transfer switch topology. The following figures show the two states of each transfer switch, reset and set. Application The dual transfer switch topology of the NI PXI-2798 enables customers to insert and remove components in a high-freque

### NI PXI-2798 Dual Transfer Switch Topology

The following figures represents the NI PXI-2798 in the dual transfer switch topology.

[IMAGE alt='image' src='GUID-DD20141B-F4A8-407F-94E4-7108AE86A466-a5.gif']

The following figures show the two states of each transfer switch, reset and set.

[IMAGE alt='image' src='GUID-AFDE967C-DD77-45E8-A41A-F76B590C0D63-a5.gif']

Application

The dual transfer switch topology of the NI PXI-2798 enables customers to insert and
 remove components in a high-frequency signal path. To insert the DUT, configure the
 transfer switch in its reset state. To remove the DUT, configure the transfer switch in
 its set state.

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

To set the transfer switch, disconnect the nc terminal from com, and connect no to
 com.

For example, to set the transfer switch K0, use the following code:

niSwitch_Disconnect(vi, "nc0", "com0")

niSwitch_Connect(vi, "no0", "com0")

Note

niSwitch_DisconnectAll

Note

niSwitch_Disconnect(vi, "nc0", "com0")

not

niSwitch_Connect(vi,
 "no0", "com0")

niSwitch_Disconnect(vi,
 "no0", "com0")

not

niSwitch_Connect(vi, "nc0", "com0")

To reset the transfer switch, disconnect the no terminal from com, and connect nc to
 com.

For example, to reset the transfer switch K0, use the following code:

niSwitch_Disconnect(vi, "no0", "com0")

niSwitch_Connect(vi, "nc0", "com0")

When scanning the NI PXI-2798, a typical scan list entry could be
 nc0->com0;. This entry resets transfer switch K0.

Parent topic:

NI PXI-2798

Related concepts:

- Transfer Switches
- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2798-front-panel.html language=enus -->
## TOPIC 00384: NI PXI-2798 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2798-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2798-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2798 front panel.

### NI PXI-2798 Front Panel

The following figure illustrates the NI PXI-2798 front panel.

[IMAGE alt='image' src='GUID-4E4593F0-3F26-45C5-9123-1ECC55980D4D-a5.gif']

Parent topic:

NI PXI-2798

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2798-hardware-diagram.html language=enus -->
## TOPIC 00385: NI PXI-2798 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2798-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2798-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figures show the hardware diagram for the NI PXI-2798.

### NI PXI-2798 Hardware Diagram

The following figures show the hardware diagram for the NI PXI-2798.

[IMAGE alt='image' src='GUID-DD20141B-F4A8-407F-94E4-7108AE86A466-a5.gif']

Parent topic:

NI PXI-2798

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2798-triggering.html language=enus -->
## TOPIC 00386: NI PXI-2798 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2798-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2798-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2798. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2798 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2798.

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

The following table lists valid scan advanced outputs for the NI PXI-2798.

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

NI PXI-2798

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2798.html language=enus -->
## TOPIC 00387: NI PXI-2798

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2798.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2798.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2798 is an 2-channel, transfer switch module for the PXI platform designed to handle RF signals up to 40 GHz. The NI PXI-2798 is composed of transfer switch relays. Operation Modes The following table lists the supported topology of the NI PXI-2798 and possible operation modes. Topology S

### NI PXI-2798

The NI PXI-2798 is an 2-channel, transfer switch module for the PXI platform designed to
 handle RF signals up to 40 GHz. The NI PXI-2798 is composed of transfer switch relays.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2798 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Dual Transfer | 2798/Dual Transfer(NISWITCH_TOPOLOGY_2798_DUAL_TRANSFER) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Transfer Switches
- RF Switching Considerations
- Operation Modes
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2799-2-spdt-topology.html language=enus -->
## TOPIC 00388: NI PXI-2799 2-SPDT Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2799-2-spdt-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2799-2-spdt-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI-2799 in the 2-SPDT general-purpose topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to connect the NO terminal of channel 1 to the COM terminal of channel 1, cal

### NI PXI-2799 2-SPDT Topology

The following figure represents the NI PXI-2799 in the 2-SPDT general-purpose topology.

[IMAGE alt='image' src='GUID-D8F4FD46-24BD-4616-B5DE-44B355995017-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to connect the NO terminal of channel 1 to the COM terminal of channel
 1, call niSwitch_Connect (vi, "no1", "com1"). If you now want to
 connect NC1 to COM1, first disconnect the existing connection. The sequence of calls
 for this task is as follows:

niSwitch_Disconnect(vi, "no1", "com1")

niSwitch_Connect(vi, "nc1", "com1")

Note

niSwitch_Disconnect(vi, "no1", "com1")

niSwitch_Connect(vi, "nc1", "com1")

Note

x

niSwitch_DisconnectAll

When scanning the NI PXI-2799, a typical scan list entry could be
 nc1->com1;. This entry routes the signal connected to NC1 to
 COM1.

Parent topic:

NI PXI-2799

Related concepts:

- General-Purpose Topologies
- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2799-front-panel.html language=enus -->
## TOPIC 00389: NI PXI-2799 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2799-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2799-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI-2799 front panel.

### NI PXI-2799 Front Panel

The following figure illustrates the NI PXI-2799 front panel.

[IMAGE alt='image' src='GUID-6FDD7962-4E2C-4DD7-A1A4-67ED328504B6-a5.gif']

Parent topic:

NI PXI-2799

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2799-hardware-diagram.html language=enus -->
## TOPIC 00390: NI PXI-2799 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2799-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2799-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI-2799.

### NI PXI-2799 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI-2799.

[IMAGE alt='image' src='GUID-AC7113D1-9638-4457-872E-9CDED4F1005C-a5.gif']

Parent topic:

NI PXI-2799

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2799-triggering.html language=enus -->
## TOPIC 00391: NI PXI-2799 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2799-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2799-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI-2799. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trigger l

### NI PXI-2799 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI-2799.

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

The following table lists valid scan advanced outputs for the NI PXI-2799.

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

NI PXI-2799

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2799.html language=enus -->
## TOPIC 00392: NI PXI-2799

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2799.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2799.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2799 is an 2-channel, general-purpose switch module for the PXI platform designed to handle RF signals up to 40 GHz. The NI PXI-2799 is composed of 2-SPDT relays. Operation Modes The following table lists the supported topology of the NI PXI-2799 and possible operation modes. Topology Sof

### NI PXI-2799

The NI PXI-2799 is an 2-channel, general-purpose switch module for the PXI platform
 designed to handle RF signals up to 40 GHz. The NI PXI-2799 is composed of 2-SPDT
 relays.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2799 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 2-SPDT | 2799/2-SPDT(NISWITCH_TOPOLOGY_2799_2_SPDT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- RF Switching Considerations
- NI PXI-2799 2-SPDT Topology
- Operation Modes
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-2800-carrier-for-the-ni-switchblock.html language=enus -->
## TOPIC 00393: NI PXI-2800 Carrier for the NI SwitchBlock

- bundle_id: `ni-switch`
- source_path: `ni-pxi-2800-carrier-for-the-ni-switchblock.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-2800-carrier-for-the-ni-switchblock.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI-2800 carrier for the NI SwitchBlock operates within a PXI chassis or, when connected to a PXI peripheral slot or a PXI Express hybrid peripheral slot, within a PXI Express chassis. The carrier occupies four PXI/PXI Express chassis slots while allowing up to six NI SwitchBlock cards to be

### NI PXI-2800 Carrier for the NI SwitchBlock

The NI PXI-2800 carrier for the NI SwitchBlock operates within a PXI chassis or, when
 connected to a PXI peripheral slot or a PXI Express hybrid peripheral slot, within a PXI
 Express chassis. The carrier occupies four PXI/PXI Express chassis slots while allowing
 up to six NI SwitchBlock cards to be inserted, enabling greater switching density than
 PXI switch modules. The installed cards can be combined in software to operate as
 multicard devices that fit testing needs. The following figure represents a SwitchBlock
 card and carrier with a PXI/PXI Express chassis.

[IMAGE alt='image' src='GUID-0F9E6EE9-CDCF-458B-ABEE-422A090E7021-a5.gif']

| 1 | NI SwitchBlock Card |
| --- | --- |
| 2 | NI PXI-2800 Carrier |
| 3 | NI PXI-2800 Backplane Connector |
| 4 | NI PXI/PXI Express Chassis |

Note

You can expand multiple NI SwitchBlock carriers using the NI 2806 expansion bridge.

Parent topic:

NI SwitchBlock Basics

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2512-front-panel.html language=enus -->
## TOPIC 00394: NI PXI/PXIe-2512 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2512-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2512-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI/PXIe-2512 front panel. Item Description A Module Status Indicator LED B DUT0 Status Indicator LED C DUT1 Status Indicator LED D DUT2 Status Indicator LED E DUT3 Status Indicator LED F DUT4 Status Indicator LED G DUT5 Status Indicator LED H DUT6 Status Indi

### NI PXI/PXIe-2512 Front Panel

The following figure illustrates the NI PXI/PXIe-2512 front panel.

[IMAGE alt='image' src='GUID-456B9BB6-5651-4A62-8D76-ADD2BA3D34B8-a5.gif']

| Item |  | Description |
| --- | --- | --- |
| A | Module Status Indicator | LED |
| B | DUT0 Status Indicator | LED |
| C | DUT1 Status Indicator | LED |
| D | DUT2 Status Indicator | LED |
| E | DUT3 Status Indicator | LED |
| F | DUT4 Status Indicator | LED |
| G | DUT5 Status Indicator | LED |
| H | DUT6 Status Indicator | LED |

#### Status Indicators

Status indicators on the front panel of the NI PXI/PXIe-2512 provide feedback about
 device operation.

Use the following table to determine the state of the module using the status
 indicator.

| Status Indicator | Auxiliary Power Input State |
| --- | --- |
| Green | OK, no channel errors present. |
| Red | Error detected on one or more channels. |

Use the following table to determine the state of DUTn channel
 using a status indicator.

| Status Indicator | Channel Output State |
| --- | --- |
| (Off) | Open |
| Green | Pass-through channel closed (CHn to DUTn) |
| Blink Amber Once | DUTn connected to fault bus A |
| Blink Amber Twice | DUTn connected to fault bus B |
| Solid Amber | Any combination of multiple DUTn paths closed (CHn,BusA, BusB) |
| Blink Red Once* | Overtemperature error detected on DUTn |
| Solid Red** | Overcurrent error detected on DUTn |
| *Overcurrent condition does not exist at the time the overtemperature condition was detected. **Overtemperature condition might or might not exist. |  |

Parent topic:

NI PXI/PXIe-2512

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2512-hardware-diagram.html language=enus -->
## TOPIC 00395: NI PXI/PXIe-2512 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2512-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2512-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2512 (NI 2512). The following table lists relay names for the NI 2512. Relays k0...k6 k0a...k6a k0b...k6b

### NI PXI/PXIe-2512 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI/PXIe-2512 (NI 2512).

[IMAGE alt='image' src='GUID-6840E5D9-6954-45B4-80F5-CA711128AACC-a5.gif']

The following table lists relay names for the NI 2512.

| Relays |
| --- |
| k0...k6 |
| k0a...k6a |
| k0b...k6b |

Parent topic:

NI PXI/PXIe-2512

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2512-independent-topology.html language=enus -->
## TOPIC 00396: NI PXI/PXIe-2512 Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2512-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2512-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2512 (NI 2512) in the independent topology. Making a Connection Both the scanning command, dut1->busA;, and the immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters dut1 and busA, result in the following co

### NI PXI/PXIe-2512 Independent Topology

The following figure represents the NI PXI/PXIe-2512 (NI 2512) in the independent
 topology.

[IMAGE alt='image' src='GUID-6840E5D9-6954-45B4-80F5-CA711128AACC-a5.gif']

#### Making a Connection

Both the scanning command, dut1->busA;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters dut1 and busA, result in
 the following connection:

signal connected to DUT1 is routed to busA

#### Pinout

The following figure identifies the pins for the NI 2512.

[IMAGE alt='image' src='GUID-B67509B4-BB99-449B-B035-6F7F982162F2-a5.gif']

Parent topic:

NI PXI/PXIe-2512

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2512-triggering.html language=enus -->
## TOPIC 00397: NI PXI/PXIe-2512 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2512-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2512-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2512 (NI 2512) can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI 2512. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0

### NI PXI/PXIe-2512 Triggering

The NI PXI/PXIe-2512 (NI 2512) can recognize trigger pulse widths less than 150 ns by
 disabling digital filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI 2512.

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

The following table lists valid scan advanced outputs for the NI 2512.

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

NI PXI/PXIe-2512

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2512.html language=enus -->
## TOPIC 00398: NI PXI/PXIe-2512

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2512.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2512.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2512 (NI 2512) is an FIU switch module for the PXI or PXI Express platforms. The NI 2512 is composed of FET switches. Operation Modes The following table lists the supported topology of the NI 2512 and possible operation modes. Topology Software Name Immediate Scanning Independent 25

### NI PXI/PXIe-2512

The NI PXI/PXIe-2512 (NI 2512) is an FIU switch module for the PXI or PXI Express
 platforms. The NI 2512 is composed of FET switches.

#### Operation Modes

The following table lists the supported topology of the NI 2512 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Independent | 2512/Independent(NISWITCH_TOPOLOGY_2512_INDEPENDENT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Fault Insertion Units
- FET Switches
- Operation Modes
- NI PXI/PXIe-2512 Independent Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2514-front-panel.html language=enus -->
## TOPIC 00399: NI PXI/PXIe-2514 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2514-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2514-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI/PXIe-2514 front panel. Item Description A Module Status Indicator LED B DUT0 Status Indicator LED C DUT1 Status Indicator LED D DUT2 Status Indicator LED E DUT3 Status Indicator LED F DUT4 Status Indicator LED G DUT5 Status Indicator LED H DUT6 Status Indi

### NI PXI/PXIe-2514 Front Panel

The following figure illustrates the NI PXI/PXIe-2514 front panel.

[IMAGE alt='image' src='GUID-D3C6256D-5407-407D-8423-563BDCBD94A5-a5.gif']

| Item |  | Description |
| --- | --- | --- |
| A | Module Status Indicator | LED |
| B | DUT0 Status Indicator | LED |
| C | DUT1 Status Indicator | LED |
| D | DUT2 Status Indicator | LED |
| E | DUT3 Status Indicator | LED |
| F | DUT4 Status Indicator | LED |
| G | DUT5 Status Indicator | LED |
| H | DUT6 Status Indicator | LED |

#### Status Indicators

Status indicators on the front panel of the NI PXI/PXIe-2514 provide feedback about
 device operation.

Use the following table to determine the state of the module using the status
 indicator.

| Status Indicator | Auxiliary Power Input State |
| --- | --- |
| Green | OK, no channel errors present. |
| Red | Error detected on one or more channels. |

Use the following table to determine the state of DUTn channel
 using a status indicator.

| Status Indicator | Channel Output State |
| --- | --- |
| (Off) | Open |
| Green | Pass-through channel closed (CHn to DUTn) |
| Blink Amber Once | DUTn connected to fault bus A |
| Blink Amber Twice | DUTn connected to fault bus B |
| Solid Amber | Any combination of multiple DUTn paths closed (CHn,BusA, BusB) |
| Blink Red Once* | Overtemperature error detected on DUTn |
| Solid Red** | Overcurrent error detected on DUTn |
| *Overcurrent condition does not exist at the time the overtemperature condition was detected. **Overtemperature condition might or might not exist. |  |

Parent topic:

NI PXI/PXIe-2514

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2514-hardware-diagram.html language=enus -->
## TOPIC 00400: NI PXI/PXIe-2514 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2514-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2514-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2514 (NI 2514). The following table lists relay names for the NI 2514. Relays k0...k6 k0a...k6a k0b...k6b

### NI PXI/PXIe-2514 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI/PXIe-2514 (NI 2514).

[IMAGE alt='image' src='GUID-6840E5D9-6954-45B4-80F5-CA711128AACC-a5.gif']

The following table lists relay names for the NI 2514.

| Relays |
| --- |
| k0...k6 |
| k0a...k6a |
| k0b...k6b |

Parent topic:

NI PXI/PXIe-2514

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2514-independent-topology.html language=enus -->
## TOPIC 00401: NI PXI/PXIe-2514 Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2514-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2514-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2514 (NI 2514) in the independent topology. Making a Connection Both the scanning command, dut1->busA;, and the immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters dut1 and busA, result in the following co

### NI PXI/PXIe-2514 Independent Topology

The following figure represents the NI PXI/PXIe-2514 (NI 2514) in the independent
 topology.

[IMAGE alt='image' src='GUID-6840E5D9-6954-45B4-80F5-CA711128AACC-a5.gif']

#### Making a Connection

Both the scanning command, dut1->busA;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters dut1 and busA, result in
 the following connection:

signal connected to DUT1 is routed to busA

#### Pinout

The following figure identifies the pins for the NI 2514.

[IMAGE alt='image' src='GUID-B67509B4-BB99-449B-B035-6F7F982162F2-a5.gif']

Parent topic:

NI PXI/PXIe-2514

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2514-triggering.html language=enus -->
## TOPIC 00402: NI PXI/PXIe-2514 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2514-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2514-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2514 (NI 2514) can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI 2514. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0

### NI PXI/PXIe-2514 Triggering

The NI PXI/PXIe-2514 (NI 2514) can recognize trigger pulse widths less than 150 ns by
 disabling digital filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI 2514.

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

The following table lists valid scan advanced outputs for the NI 2514.

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

NI PXI/PXIe-2514

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2514.html language=enus -->
## TOPIC 00403: NI PXI/PXIe-2514

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2514.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2514.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2514 (NI 2514) is an FIU switch module for the PXI or PXI Express platforms. The NI 2514 is composed of FET switches. Operation Modes The following table lists the supported topology of the NI 2514 and possible operation modes. Topology Software Name Immediate Scanning Independent 25

### NI PXI/PXIe-2514

The NI PXI/PXIe-2514 (NI 2514) is an FIU switch module for the PXI or PXI Express
 platforms. The NI 2514 is composed of FET switches.

#### Operation Modes

The following table lists the supported topology of the NI 2514 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Independent | 2514/Independent(NISWITCH_TOPOLOGY_2514_INDEPENDENT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Fault Insertion Units
- FET Switches
- Operation Modes
- NI PXI/PXIe-2514 Independent Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2515-analog-channel-expansion.html language=enus -->
## TOPIC 00404: NI PXI/PXIe-2515 Analog Channel Expansion

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2515-analog-channel-expansion.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2515-analog-channel-expansion.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can expand the number of analog channels beyond two with additional NI PXI/PXIe-2515 (NI 2515) modules. Each additional NI 2515 module provides two additional analog channels. The number of digital lines does not change when you add analog channels. Analog Channel Expansion on the NI 2515 Comple

### NI PXI/PXIe-2515 Analog Channel Expansion

You can expand the number of analog channels beyond two with additional NI PXI/PXIe-2515
 (NI 2515) modules. Each additional NI 2515 module provides two additional analog
 channels. The number of digital lines does not change when you add analog channels.

#### Analog Channel Expansion on the NI 2515

Complete the following steps to expand the number of analog channels.

1. Connect the first NI 2515 to the NI PXI-654x or 655x HSDIO module as described
 in NI PXI/PXIe-2515 Intended Use.
2. For each additional NI 2515 module, connect the "IO NI 2515" side of an
 additional SCH68-C68-D5 cable to the "HSDIO" connector of an additional module.
 Note You must use the SCH68-C68-D5 cable. The pinouts are
 different from other SCH68 cables.
3. Connect the other end of the SCH68-C68-D5 cable to the "DUT" connector of the
 previous module.

[IMAGE alt='image' src='GUID-9957C26B-77A3-4562-A4C4-D1353F7701F3-a5.gif']

Note

Parent topic:

NI PXI/PXIe-2515

Related concepts:

- NI PXI/PXIe-2515 Intended Use

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2515-front-panel.html language=enus -->
## TOPIC 00405: NI PXI/PXIe-2515 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2515-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2515-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI/PXIe-2515 front panel. Refer to the NI PXI/PXIe-2515 Intended Use topic for an example of the NI 2515 connected to a system. Item Description 1 BNC connectors 2 VHDCI connector for connection to high-speed DIO device 3 VHDCI connector for connection to DUT

### NI PXI/PXIe-2515 Front Panel

The following figure illustrates the NI PXI/PXIe-2515 front panel. Refer to the NI
 PXI/PXIe-2515 Intended Use topic for an example of the NI 2515 connected to a system.

[IMAGE alt='image' src='GUID-034F618E-C0E7-4DD5-982A-F1A7EABAD7EE-a5.gif']

| Item | Description |
| --- | --- |
| 1 | BNC connectors |
| 2 | VHDCI connector for connection to high-speed DIO device |
| 3 | VHDCI connector for connection to DUT |

Parent topic:

NI PXI/PXIe-2515

Related concepts:

- NI PXI/PXIe-2515 Intended Use

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2515-hardware-diagram.html language=enus -->
## TOPIC 00406: NI PXI/PXIe-2515 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2515-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2515-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2515. ctrl0, ctrl2, and ctrl3 do not route through relays, but rather pass through from the left connector to the right connector. These channels cannot be connected to the analog bus channels, busa and busb.

### NI PXI/PXIe-2515 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI/PXIe-2515.

[IMAGE alt='image' src='GUID-2CFE5085-43A5-42E9-A437-7ACE2AFF86A9-a5.gif']

Note

Parent topic:

NI PXI/PXIe-2515

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2515-independent-topology.html language=enus -->
## TOPIC 00407: NI PXI/PXIe-2515 Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2515-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2515-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI PXI/PXIe-2515 (NI 2515) independent topology to connect a single pin of a DUT to a supported NI high-speed DIO device and parametric measurement devices. Refer to the following sections for more information about the intended use of the NI 2515. Hardware Diagram Making a Connection Pinout

### NI PXI/PXIe-2515 Independent Topology

Use the NI PXI/PXIe-2515 (NI 2515) independent topology to connect a single pin of a DUT
 to a supported NI high-speed DIO device and parametric measurement devices. Refer to the
 following sections for more information about the intended use of the NI 2515.

- Hardware Diagram
- Making a Connection
- Pinout
- Pin Associations

#### Hardware Diagram

The following figure represents the NI 2515 in the independent topology.

[IMAGE alt='image' src='GUID-2CFE5085-43A5-42E9-A437-7ACE2AFF86A9-a5.gif']

Note

#### Making a Connection

With the independent topology, you can let NI-SWITCH determine the path between two
 specified channels by setting the intermediate channels as reserved for routing and
 using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function, or you can control individual relays using the niSwitch Relay
 Control
 VI or the
 niSwitch_RelayControl
 function.

#### Pinout

The following figure identifies the pins for the NI 2515 in the independent
 topology.

[IMAGE alt='image' src='GUID-682E1832-8638-471A-97F5-F7989ECAE389-a5.gif']

Caution

not

Caution

HSDIO

Note

#### Pin Associations

The NI 2515 is recommended for use with the NI 6535/6536/6537, the
 NI 654x, the NI 655x, and the NI 6581
 high-speed DIO devices, using the designated cable for connection between the
 NI 2515 and the supported NI high-speed DIO device. Refer to the following table for
 corresponding signals on the NI 2515 and supported NI high-speed DIO devices.

#### Using the NI 2515 Pin Associations Table

To use the following table, first find the high-speed DIO signal you want to route to
 your DUT. Look across the table row that contains the high-speed DIO signal to find
 the NI 2515 right connector and left connector channels necessary to route that
 signal. For cables recommended to connect the NI 2515 to your system, refer to
 NI 2515 Signal Connections.

| Pin | High-speed DIO Channel | NI 2515 Left Connector | NI 2515 Left Connector |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NI 6535/6536/6537 | NI 654x | NI 6551/6552 | NI 6555/6556 | NI 6581 | Pin | Channel | Pin | Channel |  |
| 1 | P3.7 | DIO 31 | RESERVED | PFI 31 | RESERVED | 34 | ch31 | 1 | dut31 |
| 2 | GND | GND | GND | GND | GND | 33 | GND | 2 | GND |
| 3 | P3.5 | DIO 29 | RESERVED | PFI 29 | RESERVED | 32 | ch29 | 3 | dut29 |
| 4 | GND | GND | GND | GND | GND | 31 | GND | 4 | GND |
| 5 | P3.3 | DIO 27 | RESERVED | PFI 27 | RESERVED | 30 | ch27 | 5 | dut27 |
| 6 | GND | GND | GND | GND | GND | 29 | GND | 6 | GND |
| 7 | P3.1 | DIO 25 | RESERVED | PFI 25 | RESERVED | 28 | ch25 | 7 | dut25 |
| 8 | RESERVED | RESERVED | RESERVED | GND | GND | 27 | NO CONNECT | 8 | NO CONNECT |
| 9 | P2.7 | DIO 23 | RESERVED | DIO 23 | P2.7 | 26 | ch23 | 9 | dut23 |
| 10 | GND | GND | GND | GND | GND | 25 | GND | 10 | GND |
| 11 | P2.5 | DIO 21 | RESERVED | DIO 21 | P2.5 | 24 | ch21 | 11 | dut21 |
| 12 | GND | GND | GND | GND | GND | 23 | GND | 12 | GND |
| 13 | P2.3 | DIO 19 | DIO 19 | DIO 19 | P2.3 | 22 | ch19 | 13 | dut19 |
| 14 | GND | GND | GND | GND | GND | 21 | GND | 14 | GND |
| 15 | P2.1 | DIO 17 | DIO 17 | DIO 17 | P2.1 | 20 | ch17 | 15 | dut17 |
| 16 | GND | GND | GND | GND | GND | 19 | GND | 16 | GND |
| 17 | P1.7 | DIO 15 | DIO 15 | DIO 15 | P1.7 | 18 | ch15 | 17 | dut15 |
| 18 | GND | GND | GND | GND | GND | 17 | GND | 18 | GND |
| 19 | P1.5 | DIO 13 | DIO 13 | DIO 13 | P1.5 | 16 | ch13 | 19 | dut13 |
| 20 | GND | GND | GND | GND | GND | 15 | GND | 20 | GND |
| 21 | P1.3 | DIO 11 | DIO 11 | DIO 11 | P1.3 | 14 | ch11 | 21 | dut11 |
| 22 | GND | GND | GND | GND | GND | 13 | GND | 22 | GND |
| 23 | P1.1 | DIO 9 | DIO 9 | DIO 9 | P1.1 | 12 | ch9 | 23 | dut9 |
| 24 | GND | GND | GND | GND | GND | 11 | GND | 24 | GND |
| 25 | P0.7 | DIO 7 | DIO 7 | DIO 7 | P0.7 | 10 | ch7 | 25 | dut7 |
| 26 | PFI 1 | PFI 1 | PFI 1 | PFI 1 | PFI 1 | 9 | ctrl1 | 26 | dutctrl1 |
| 27 | P0.5 | DIO 5 | DIO 5 | DIO 5 | P0.5 | 8 | ch5 | 27 | dut5 |
| 28 | GND | GND | GND | X | GND | GND | GND | 28 | GND |
| 29 | P0.3 | DIO 3 | DIO 3 | DIO 3 | P0.3 | 6 | ch3 | 29 | dut3 |
| 30 | PFI 3 | PFI 3 | PFI 3 | PFI 3 | GND | 5 | ctrl3 | 30 | ctrl3 |
| 31 | P0.1 | DIO 1 | DIO 1 | DIO 1 | P0.1 | 4 | ch1 | 31 | dut1 |
| 32 | GND | GND | GND | GND | GND | 3 | GND | 32 | GND |
| 33 | PFI 4 | DDC CLK OUT | DDC CLK OUT | PFI 4/DDC CLK OUT | CLOCK OUT | 2 | ctrl4 | 33 | dutctrl4 |
| 34 | GND | GND | GND | GND | GND | 1 | GND | 34 | GND |
| 35 | P3.6 | DIO 30 | RESERVED | PFI 30 | RESERVED | 68 | ch30 | 35 | dut30 |
| 36 | GND | GND | GND | GND | GND | 67 | GND | 36 | GND |
| 37 | P3.4 | DIO 28 | RESERVED | PFI 28 | RESERVED | 66 | ch28 | 37 | dut28 |
| 38 | GND | GND | GND | GND | GND | 65 | GND | 38 | GND |
| 39 | P3.2 | DIO 26 | RESERVED | PFI 26 | RESERVED | 64 | ch26 | 39 | dut26 |
| 40 | GND | GND | GND | GND | GND | 63 | GND | 40 | GND |
| 41 | P3.0 | DIO 24 | RESERVED | PFI 24 | RESERVED | 62 | ch24 | 41 | dut24 |
| 42 | GND | GND | GND | GND | GND | 61 | GND | 42 | GND |
| 43 | P2.6 | DIO 22 | RESERVED | DIO 22 | P2.6 | 60 | ch22 | 43 | dut22 |
| 44 | GND | GND | GND | GND | GND | 59 | GND | 44 | GND |
| 45 | P2.4 | DIO 20 | RESERVED | DIO 20 | P2.4 | 58 | ch20 | 45 | dut20 |
| 46 | GND | GND | GND | GND | GND | 57 | GND | 46 | GND |
| 47 | P2.2 | DIO 18 | DIO 18 | DIO 18 | P2.2 | 56 | ch18 | 47 | dut18 |
| 48 | GND | GND | GND | GND | GND | 55 | GND | 48 | GND |
| 49 | P2.0 | DIO 16 | DIO 16 | DIO 16 | P2.0 | 54 | ch16 | 49 | dut16 |
| 50 | GND | GND | GND | GND | GND | 53 | GND | 50 | GND |
| 51 | P1.6 | DIO 14 | DIO 14 | DIO 14 | P1.6 | 52 | ch14 | 51 | dut14 |
| 52 | PFI 0 | RESERVED | RESERVED | GND | GND | 51 | ctrl0 | 52 | dutctrl0 |
| 53 | P1.4 | DIO 12 | DIO 12 | DIO 12 | P1.4 | 50 | ch12 | 53 | dut12 |
| 54 | GND | GND | GND | GND | GND | 49 | GND | 54 | GND |
| 55 | P1.2 | DIO 10 | DIO 10 | DIO 10 | P1.2 | 48 | ch10 | 55 | dut10 |
| 56 | GND | GND | GND | GND | GND | 47 | GND | 56 | GND |
| 57 | P1.0 | DIO 8 | DIO 8 | DIO 8 | P1.0 | 46 | ch8 | 57 | dut8 |
| 58 | GND | GND | GND | GND | GND | 45 | GND | 58 | GND |
| 59 | P0.6 | DIO 6 | DIO 6 | DIO 6 | P0.6 | 44 | ch6 | 59 | dut6 |
| 60 | RESERVED | RESERVED | RESERVED | RESERVED | NO CONNECT | 43 | Res0 | 60 | Res0 |
| 61 | P0.4 | DIO 4 | DIO 4 | DIO 4 | P0.4 | 42 | ch4 | 61 | dut4 |
| 62 | GND | GND | GND | GND | GND | 41 | GND | 62 | GND |
| 63 | P0.2 | DIO 2 | DIO 2 | DIO 2 | P0.2 | 40 | ch2 | 63 | dut2 |
| 64 | PFI 2 | PFI 2 | PFI 2 | PFI 2 | PFI 2 | 39 | ctrl2 | 64 | ctrl2 |
| 65 | P0.0 | DIO 0 | DIO 0 | DIO 0 | P0.0 | 38 | ch0 | 65 | dut0 |
| 66 | GND | GND | GND | GND | GND | 37 | GND | 66 | GND |
| 67 | PFI 5 | STROBE | STROBE | PFI 5/STROBE | GLOBAL CLOCK 0 | 36 | ctrl5 | 67 | dutctrl5 |
| 68 | GND | GND | GND | GND | GND | 35 | GND | 68 | GND |

Parent topic:

NI PXI/PXIe-2515

Related concepts:

- NI PXI/PXIe-2515 Intended Use

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2515-intended-use.html language=enus -->
## TOPIC 00408: NI PXI/PXIe-2515 Intended Use

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2515-intended-use.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2515-intended-use.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The two analog buses of the NI PXI/PXIe-2515 (NI 2515) are intended to facilitate connectivity in performing DC parametric measurements. The analog buses of the NI 2515 are not intended for high-bandwidth analog measurements (for example, rise time and skew). Refer to the following sections for more

### NI PXI/PXIe-2515 Intended Use

The two analog buses of the NI PXI/PXIe-2515 (NI 2515) are intended to facilitate
 connectivity in performing DC parametric measurements. The analog buses of the NI 2515
 are not intended for high-bandwidth analog measurements (for example, rise time and
 skew). Refer to the following sections for more information about the intended use of
 the NI 2515.

- NI 2515 Intended Use
- NI 2515 Signal Connections

#### NI 2515 Intended Use

You can connect the NI 2515 to one supported NI high-speed DIO device and up to two
 other instruments. Refer to NI PXI/PXIe-2515 Analog Channel Expansion if your system
 requires the connection of more than two other instruments. The NI 2515 is intended
 for use with any supported single-ended NI high-speed DIO device (for example, the
 NI 654x or the NI 655x), and it is not
 intended for use with a low-voltage differential signaling (LVDS) NI high-speed DIO
 device (for example, the NI 656x). Refer to the following figure
 and the NI 2515 Signal Connections table for an example of the intended use of the
 NI 2515 in a system.

[IMAGE alt='image' src='GUID-02900055-A3AC-4F6D-8074-53D1DFFE1D0A-a5.gif']

Note

Note

#### NI 2515 Signal Connections

Refer to the following table to select accessories that connect the NI 2515 to your
 system.

| Connection Indicated in Intended Use Diagram | Cable Connection | Recommended Accessories | Notes |
| --- | --- | --- | --- |
| A | VHDCI connector on supported NI high-speed DIO device to left VHDCI connector on NI 2515 | NI SHC68-C68-D5 0.5m Shielded Single-Ended Cable for High-Speed Digital Signal Insertion Switch | Caution Use only the NI SHC68-C68-D5 cable to connect the supported NI high-speed DIO device to the NI 2515. The cable translates the pinout of the supported NI high-speed DIO device to the HSDIO connector on the NI 2515 so that the pinout of the DUT connector on the NI 2515 matches that of the supported NI high-speed DIO device. |
| B and C | BNC connectors on NI 2515 to parametric measurement devices | — | There is not a designated cable to connect the BNC connectors on the NI 2515 to parametric measurement devices. Select a cable that fits the connectivity needs of your system. Note The outer shields of both analog bus channels (B and C in the diagram) are connected to chassis ground. Therefore, the negative lead of any analog bus channel must be at chassis ground. |
| D | Right VHDCI connector on NI 2515 to DUT | You have the following options: NI CB-2162 connector block and NI SHC68-C68-D4 Shielded Single-Ended Cable for High-Speed Digital Devices NI SMB-2163 breakout box and NI SHC68-C68-D4 Shielded Single-Ended Cable for High-Speed Digital Devices NI SHC68-H1X38 Shielded Single-Ended Flying-Lead Cable | Refer to ni.com/manuals for information on the use of these signal connection options. |

Parent topic:

NI PXI/PXIe-2515

Related concepts:

- NI PXI/PXIe-2515 Analog Channel Expansion

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2515-triggering.html language=enus -->
## TOPIC 00409: NI PXI/PXIe-2515 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2515-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2515-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2515 (NI 2515) can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI 2515. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0

### NI PXI/PXIe-2515 Triggering

The NI PXI/PXIe-2515 (NI 2515) can recognize trigger pulse widths less than 150 ns by
 disabling digital filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI 2515.

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

The following table lists valid scan advanced outputs for the NI 2515.

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

NI PXI/PXIe-2515

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2515.html language=enus -->
## TOPIC 00410: NI PXI/PXIe-2515

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2515.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2515.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2515 (NI 2515) is a multiplexer switch module for the PXI or PXI Express platform that enables connectivity by routing high-speed digital I/O (DIO) signals between a device under test (DUT) and a supported NI high-speed DIO device or parametric measurement devices. Refer to the NI 25

### NI PXI/PXIe-2515

The NI PXI/PXIe-2515 (NI 2515) is a multiplexer switch module for the PXI or PXI Express
 platform that enables connectivity by routing high-speed digital I/O (DIO) signals
 between a device under test (DUT) and a supported NI high-speed DIO device or parametric
 measurement devices. Refer to the NI 2515 Pin Associations table for a list of supported
 NI high-speed DIO devices.

The NI 2515 uses reed relays. A number of factors can affect the life expectancy of reed
 relays. Refer to Reed Relay Protection for information about protecting the reed relays
 on the NI 2515.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2515 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Independent | 2515/Independent(NISWITCH_TOPOLOGY_2515_INDEPENDENT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- NI PXI/PXIe-2515 Independent Topology
- Reed Relays
- Reed Relay Protection
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Topologies
- Operation Modes
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2527-1-wire-64-1-multiplexer-topo.html language=enus -->
## TOPIC 00411: NI PXI/PXIe-2527 1-Wire 64×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2527-1-wire-64-1-multiplexer-topo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2527-1-wire-64-1-multiplexer-topo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Connect to the pins of the NI TB-2627 terminal block to use the NI PXI/PXIe-2527 (NI 2527) as a 1-wire 64×1 multiplexer. In this topology, all channel terminals (CH0 through CH63) route to COM0+. The 1WREF0 lead is always connected to COM0–. COM0+ is addressed as com0 in software. The following figu

### NI PXI/PXIe-2527 1-Wire 64×1 Multiplexer Topology

Connect to the pins of the NI TB-2627 terminal block to use the NI PXI/PXIe-2527
 (NI 2527) as a 1-wire 64×1 multiplexer. In this topology, all channel terminals (CH0
 through CH63) route to COM0+. The 1WREF0 lead is always connected to COM0–. COM0+ is
 addressed as com0 in software.

The following figure represents the NI 2527 in the 1-wire 64×1 multiplexer topology.

[IMAGE alt='image' src='GUID-77A74834-1BA5-40D9-8EEC-348517F7AAE3-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connections:

- signal connected to CH2 is routed to COM0

#### Pinout

The following figure and table identify the pins for the NI 2527 in the 1-wire 64×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-5B0C3E40-AF78-4477-9966-DAA82055366A-a5.gif']

| Software Name | Pin Number | Software Name | Pin Number |
| --- | --- | --- | --- |
| ch0 | A1 | ch36 | B3 |
| ch1 | D1 | ch37 | C3 |
| ch2 | A2 | ch38 | B4 |
| ch3 | D2 | ch39 | C4 |
| ch4 | A3 | ch40 | B5 |
| ch5 | D3 | ch41 | C5 |
| ch6 | A4 | ch42 | B6 |
| ch7 | D4 | ch43 | C6 |
| ch8 | A5 | ch44 | B7 |
| ch9 | D5 | ch45 | C7 |
| ch10 | A6 | ch46 | B8 |
| ch11 | D6 | ch47 | C8 |
| ch12 | A7 | ch48 | B10 |
| ch13 | D7 | ch49 | C10 |
| ch14 | A8 | ch50 | B11 |
| ch15 | D8 | ch51 | C11 |
| ch16 | A10 | ch52 | B12 |
| ch17 | D10 | ch53 | C12 |
| ch18 | A11 | ch54 | B13 |
| ch19 | D11 | ch55 | C13 |
| ch20 | A12 | ch56 | B14 |
| ch21 | D12 | ch57 | C14 |
| ch22 | A13 | ch58 | B15 |
| ch23 | D13 | ch59 | C15 |
| ch24 | A14 | ch60 | B16 |
| ch25 | D14 | ch61 | C16 |
| ch26 | A15 | ch62 | B17 |
| ch27 | D15 | ch63 | C17 |
| ch28 | A16 | com0 | A9 |
| ch29 | D16 | — | — |
| ch30 | A17 | — | — |
| ch31 | D17 | — | — |
| ch32 | B1 | — | — |
| ch33 | C1 | — | — |
| ch34 | B2 | — | — |
| ch35 | C2 | — | — |

#### Additional Pin References

| NI 2527 Connector Pin Number | Signal Name |
| --- | --- |
| B9 | com0– |
| A18 | com1+ |
| B18 | com1– |
| C9 | 1wref0 |
| C18 | 1wref1 |
| A25 | cjtemp+ |
| D25 | cjtemp– |

Note

Parent topic:

NI PXI/PXIe-2527

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2527-1-wire-dual-32-1-multiplexer.html language=enus -->
## TOPIC 00412: NI PXI/PXIe-2527 1-Wire Dual 32×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2527-1-wire-dual-32-1-multiplexer.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2527-1-wire-dual-32-1-multiplexer.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Connect to the pins of the NI TB-2627 terminal block to use the NI PXI/PXIe-2527 (NI 2527) as a 1-wire dual 32×1 multiplexer. In this topology, CH0 through CH31 route to COM0+, and CH32 through CH63 route to COM1+. The 1WREF0 lead is connected to COM0– and the 1WREF1 lead is connected to COM1–. The

### NI PXI/PXIe-2527 1-Wire Dual 32×1 Multiplexer Topology

Connect to the pins of the NI TB-2627 terminal block to use the NI PXI/PXIe-2527
 (NI 2527) as a 1-wire dual 32×1 multiplexer. In this topology, CH0 through CH31 route to
 COM0+, and CH32 through CH63 route to COM1+. The 1WREF0 lead is connected to COM0– and
 the 1WREF1 lead is connected to COM1–. The pair COM0+ and COM0– is addressed as com0 in
 software, and the pair COM1+ and COM1– is addressed as com1 in software.

The following figure represents the NI 2527 in the 1-wire dual 32×1 multiplexer topology.

[IMAGE alt='image' src='GUID-B2FD3BEB-A786-4C20-91AA-080B7340E245-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connection:

- signal connected to CH2 is routed to COM0

#### Pinout

The following figure and table identify the pins for the NI 2527 in the 1-wire dual
 32×1 multiplexer topology.

[IMAGE alt='image' src='GUID-5B0C3E40-AF78-4477-9966-DAA82055366A-a5.gif']

| Software Name | Pin Number | Software Name | Pin Number |
| --- | --- | --- | --- |
| ch0 | A1 | ch36 | A12 |
| ch1 | D1 | ch37 | D12 |
| ch2 | A2 | ch38 | A13 |
| ch3 | D2 | ch39 | D13 |
| ch4 | A3 | ch40 | A14 |
| ch5 | D3 | ch41 | D14 |
| ch6 | A4 | ch42 | A15 |
| ch7 | D4 | ch43 | D15 |
| ch8 | A5 | ch44 | A16 |
| ch9 | D5 | ch45 | D16 |
| ch10 | A6 | ch46 | A17 |
| ch11 | D6 | ch47 | D17 |
| ch12 | A7 | ch48 | B10 |
| ch13 | D7 | ch49 | C10 |
| ch14 | A8 | ch50 | B11 |
| ch15 | D8 | ch51 | C11 |
| ch16 | B1 | ch52 | B12 |
| ch17 | C1 | ch53 | C12 |
| ch18 | B2 | ch54 | B13 |
| ch19 | C2 | ch55 | C13 |
| ch20 | B3 | ch56 | B14 |
| ch21 | C3 | ch57 | C14 |
| ch22 | B4 | ch58 | B15 |
| ch23 | C4 | ch59 | C15 |
| ch24 | B5 | ch60 | B16 |
| ch25 | C5 | ch61 | C16 |
| ch26 | B6 | ch62 | B17 |
| ch27 | C6 | ch63 | C17 |
| ch28 | B7 | com0 | A9 |
| ch29 | C7 | com1 | A18 |
| ch30 | B8 | — | — |
| ch31 | C8 | — | — |
| ch32 | A10 | — | — |
| ch33 | D10 | — | — |
| ch34 | A11 | — | — |
| ch35 | D11 | — | — |

#### Additional Pin References

| NI 2527 Connector Pin Number | Signal Name |
| --- | --- |
| B9 | com0– |
| B18 | com1– |
| C9 | 1wref0 |
| C18 | 1wref1 |
| A25 | cjtemp+ |
| D25 | cjtemp– |

Parent topic:

NI PXI/PXIe-2527

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2527-2-wire-32-1-multiplexer-topo.html language=enus -->
## TOPIC 00413: NI PXI/PXIe-2527 2-Wire 32×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2527-2-wire-32-1-multiplexer-topo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2527-2-wire-32-1-multiplexer-topo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Connect to the pins of the NI TB-2627 terminal block to use the NI PXI/PXIe-2527 (NI 2527) as a 2-wire 32×1 multiplexer. In this topology, all positive leads (CH0+ through CH31+) route to COM0+ and all negative leads (CH0– through CH31–) route to COM0–. The pair COM0+ and COM0– is addressed as com0

### NI PXI/PXIe-2527 2-Wire 32×1 Multiplexer Topology

Connect to the pins of the NI TB-2627 terminal block to use the NI PXI/PXIe-2527
 (NI 2527) as a 2-wire 32×1 multiplexer. In this topology, all positive leads (CH0+
 through CH31+) route to COM0+ and all negative leads (CH0– through CH31–) route to
 COM0–. The pair COM0+ and COM0– is addressed as com0 in software.

The following figure represents the NI 2527 in the 2-wire 32×1 multiplexer topology.

[IMAGE alt='image' src='GUID-7049D5C0-7FFB-432E-8C98-5A490494D559-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in
 the following connections:

- signal connected to CH2+ is routed to COM0+
- signal connected to CH2– is routed COM0–

#### Pinout

The following figure and table identify the pins for the NI 2527 in the 2-wire 32×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-5B0C3E40-AF78-4477-9966-DAA82055366A-a5.gif']

| Software Name | + Pin Number | – Pin Number | Software Name | + Pin Number | – Pin Number |
| --- | --- | --- | --- | --- | --- |
| ch0 | A1 | B1 | ch18 | A11 | B11 |
| ch1 | D1 | C1 | ch19 | D11 | C11 |
| ch2 | A2 | B2 | ch20 | A12 | B12 |
| ch3 | D2 | C2 | ch21 | D12 | C12 |
| ch4 | A3 | B3 | ch22 | A13 | B13 |
| ch5 | D3 | C3 | ch23 | D13 | C13 |
| ch6 | A4 | B4 | ch24 | A14 | B14 |
| ch7 | D4 | C4 | ch25 | D14 | C14 |
| ch8 | A5 | B5 | ch26 | A15 | B15 |
| ch9 | D5 | C5 | ch27 | D15 | C15 |
| ch10 | A6 | B6 | ch28 | A16 | B16 |
| ch11 | D6 | C6 | ch29 | D16 | C16 |
| ch12 | A7 | B7 | ch30 | A17 | B17 |
| ch13 | D7 | C7 | ch31 | D17 | C17 |
| ch14 | A8 | B8 | com0 | A9 | B9 |
| ch15 | D8 | C8 | cjtemp | A25 | D25 |
| ch16 | A10 | B10 | — | — | — |
| ch17 | D10 | C10 | — | — | — |

#### Additional Pin References

| NI 2527 Connector Pin Number | Signal Name |
| --- | --- |
| A18 | com1+ |
| B18 | com1– |
| C9 | 1wref0 |
| C18 | 1wref1 |

Note

Parent topic:

NI PXI/PXIe-2527

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2527-2-wire-dual-16-1-multiplexer.html language=enus -->
## TOPIC 00414: NI PXI/PXIe-2527 2-Wire Dual 16×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2527-2-wire-dual-16-1-multiplexer.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2527-2-wire-dual-16-1-multiplexer.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Connect to the pins of the NI TB-2627 terminal block to use the NI PXI/PXIe-2527 (NI 2527) as a 2-wire dual 16×1 multiplexer. In this topology, CH0+ through CH15+ route to COM0+, and CH0– through CH15– route to COM0–. Additionally, CH16+ through CH31+ route to COM1+, and CH16– through CH31– route to

### NI PXI/PXIe-2527 2-Wire Dual 16×1 Multiplexer Topology

Connect to the pins of the NI TB-2627 terminal block to use the NI PXI/PXIe-2527 (NI 2527) as a
 2-wire dual 16×1 multiplexer. In this topology, CH0+ through CH15+ route to COM0+, and CH0–
 through CH15– route to COM0–. Additionally, CH16+ through CH31+ route to COM1+, and CH16– through
 CH31– route to COM1–. The pair COM0+ and COM0– is addressed as com0 in software, and the pair
 COM1+ and COM1– is addressed as com1 in software.

The following figure represents the NI 2527 in the 2-wire dual 16×1 multiplexer topology.

[IMAGE alt='image' src='GUID-8A491345-3344-4F48-9B16-C2996FCEF500-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in the following
 connections:

- signal connected to CH2+ is routed to COM0+
- signal connected to CH2– is routed COM0–

#### Pinout

The following figure and table identify the pins for the NI 2527 in the 2-wire dual 16×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-5B0C3E40-AF78-4477-9966-DAA82055366A-a5.gif']

| Software Name | + Pin Number | – Pin Number | Software Name | + Pin Number | – Pin Number |
| --- | --- | --- | --- | --- | --- |
| ch0 | A1 | B1 | ch18 | A11 | B11 |
| ch1 | D1 | C1 | ch19 | D11 | C11 |
| ch2 | A2 | B2 | ch20 | A12 | B12 |
| ch3 | D2 | C2 | ch21 | D12 | C12 |
| ch4 | A3 | B3 | ch22 | A13 | B13 |
| ch5 | D3 | C3 | ch23 | D13 | C13 |
| ch6 | A4 | B4 | ch24 | A14 | B14 |
| ch7 | D4 | C4 | ch25 | D14 | C14 |
| ch8 | A5 | B5 | ch26 | A15 | B15 |
| ch9 | D5 | C5 | ch27 | D15 | C15 |
| ch10 | A6 | B6 | ch28 | A16 | B16 |
| ch11 | D6 | C6 | ch29 | D16 | C16 |
| ch12 | A7 | B7 | ch30 | A17 | B17 |
| ch13 | D7 | C7 | ch31 | D17 | C17 |
| ch14 | A8 | B8 | com0 | A9 | B9 |
| ch15 | D8 | C8 | com1 | A18 | B18 |
| ch16 | A10 | B10 | cjtemp | A25 | D25 |
| ch17 | D10 | C10 | - | - | - |

Parent topic:

NI PXI/PXIe-2527

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2527-4-wire-16-1-multiplexer-topo.html language=enus -->
## TOPIC 00415: NI PXI/PXIe-2527 4-Wire 16×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2527-4-wire-16-1-multiplexer-topo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2527-4-wire-16-1-multiplexer-topo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Connect to the pins of the NI TB-2627 terminal block to use the NI PXI/PXIe-2527 (NI 2527) as a 4-wire 16×1 multiplexer. In this topology, all positive "A" leads (CH0A+ through CH15A+) route to COM0+. All negative "A" leads (CH0A– through CH15A–) route to COM0–. All positive "B" leads (CH0B+ through

### NI PXI/PXIe-2527 4-Wire 16×1 Multiplexer Topology

Connect to the pins of the NI TB-2627 terminal block to use the NI PXI/PXIe-2527 (NI 2527) as a
 4-wire 16×1 multiplexer. In this topology, all positive "A" leads (CH0A+ through CH15A+) route to
 COM0+. All negative "A" leads (CH0A– through CH15A–) route to COM0–. All positive "B" leads
 (CH0B+ through CH15B+) route to COM1+. All negative "B" leads (CH0B– through CH15B–) route to
 COM1–. COM0+, COM0–, COM1+, and COM1– are addressed as com0 in software.

The following figure represents the NI 2527 in the 4-wire 16×1 multiplexer topology.

[IMAGE alt='image' src='GUID-EDB0073C-FAAE-479F-A50F-11D049547AE2-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com0;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com0, result in the following
 connections:

- signal connected to CH2A+ is routed to COM0A+
- signal connected to CH2A– is routed to COM0A–
- signal connected to CH2B+ is routed to COM0B+
- signal connected to CH2B– is routed to COM0B–

#### Pinout

The following figure and table identify the pins for the NI 2527 in the 4-wire 16×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-5B0C3E40-AF78-4477-9966-DAA82055366A-a5.gif']

| Software Name | A+ Pin Number | A– Pin Number | B+ Pin Number | B– Pin Number |
| --- | --- | --- | --- | --- |
| ch0 | A1 | B1 | A10 | B10 |
| ch1 | D1 | C1 | D10 | C10 |
| ch2 | A2 | B2 | A11 | B11 |
| ch3 | D2 | C2 | D11 | C11 |
| ch4 | A3 | B3 | A12 | B12 |
| ch5 | D3 | C3 | D12 | C12 |
| ch6 | A4 | B4 | A13 | B13 |
| ch7 | D4 | C4 | D13 | C13 |
| ch8 | A5 | B5 | A14 | B14 |
| ch9 | D5 | C5 | D14 | C14 |
| ch10 | A6 | B6 | A15 | B15 |
| ch11 | D6 | C6 | D15 | C15 |
| ch12 | A7 | B7 | A16 | B16 |
| ch13 | D7 | C7 | D16 | C16 |
| ch14 | A8 | B8 | A17 | B17 |
| ch15 | D8 | C8 | D17 | C17 |
| com0 | A9 | B9 | A18 | B18 |
| cjtemp | A25 | D25 | — | — |

Parent topic:

NI PXI/PXIe-2527

Related concepts:

- N-Wire Switching Modes
- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2527-hardware-diagram.html language=enus -->
## TOPIC 00416: NI PXI/PXIe-2527 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2527-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2527-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2527. Relay names are the same for every topology.

### NI PXI/PXIe-2527 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-FE3446FA-FDFC-4979-8D3F-74E820C96CF5-a5.gif']

Parent topic:

NI PXI/PXIe-2527

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2527-independent-topology.html language=enus -->
## TOPIC 00417: NI PXI/PXIe-2527 Independent Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2527-independent-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2527-independent-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using the NI PXI/PXIe-2527 (NI 2527) in the independent topology, connect the signals using the NI TB-2627 terminal block. Select this topology to utilize the full routing capabilities of the NI 2527. Making a Connection With the independent topology, you can let NI-SWITCH determine the path be

### NI PXI/PXIe-2527 Independent Topology

When using the NI PXI/PXIe-2527 (NI 2527) in the independent topology, connect the
 signals using the NI TB-2627 terminal block. Select this topology to utilize the full
 routing capabilities of the NI 2527.

[IMAGE alt='image' src='GUID-FED8DF8E-F35F-442D-8CF0-2EEAB73C1F77-a5.gif']

#### Making a Connection

With the independent topology, you can let NI-SWITCH determine the path between two
 specified channels by setting the intermediate channels as reserved for routing and
 using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function, or you can control individual relays using the niSwitch Relay
 Control
 VI or the
 niSwitch_RelayControl
 function.

#### Pinout

The following figure and table identify the pins for the NI 2527 in the independent
 topology.

[IMAGE alt='image' src='GUID-5B0C3E40-AF78-4477-9966-DAA82055366A-a5.gif']

| Software Name | + Pin Number | – Pin Number | Software Name | + Pin Number | – Pin Number |
| --- | --- | --- | --- | --- | --- |
| ch0 | A1 | B1 | ch17 | D10 | C10 |
| ch1 | D1 | C1 | ch18 | A11 | B11 |
| ch2 | A2 | B2 | ch19 | D11 | C11 |
| ch3 | D2 | C2 | ch20 | A12 | B12 |
| ch4 | A3 | B3 | ch21 | D12 | C12 |
| ch5 | D3 | C3 | ch22 | A13 | B13 |
| ch6 | A4 | B4 | ch23 | D13 | C13 |
| ch7 | D4 | C4 | ch24 | A14 | B14 |
| ch8 | A5 | B5 | ch25 | D14 | C14 |
| ch9 | D5 | C5 | ch26 | A15 | B15 |
| ch10 | A6 | B6 | ch27 | D15 | C15 |
| ch11 | D6 | C6 | ch28 | A16 | B16 |
| ch12 | A7 | B7 | ch29 | D16 | C16 |
| ch13 | D7 | C7 | ch30 | A17 | B17 |
| ch14 | A8 | B8 | ch31 | D17 | C17 |
| ch15 | D8 | C8 | com0 | A9 | B9 |
| ch16 | A10 | B10 | com1 | A18 | B18 |
| cjtemp | A25 | D25 | — | — | — |

The following is a list of the valid internal channel names:

| pcom0 | pcom1 |
| --- | --- |
| 1wref0 | 1wref1 |
| cjtemp | icom0 |
| pcom1plus | pcom1minus |
| icom0plus | icom0minus |
| pcom0plus | pcom0minus |
| com1plus | com1minus |

Parent topic:

NI PXI/PXIe-2527

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2527-relay-replacement.html language=enus -->
## TOPIC 00418: NI PXI/PXIe-2527 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2527-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2527-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2527 (NI 2527) uses electromechanical armature relays. Refer to the following tables for information about ordering replacement relays. Relay Manufacturer Part Number AXICOM (Tyco Electronics) IM42PGR (5-1462039-7) Relay Kit Part Number National Instruments (10 relays) 782051-01 Comp

### NI PXI/PXIe-2527 Relay Replacement

The NI PXI/PXIe-2527 (NI 2527) uses electromechanical armature relays.

Refer to the following tables for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| AXICOM (Tyco Electronics) | IM42PGR (5-1462039-7) |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 782051-01 |

Complete the following sets of steps to disassemble your module, replace a failed relay,
 and reassemble your module.

#### Disassemble the Module

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your module from electrostatic discharge.
2. Refer to the following figure and table to locate the relay you want to replace.
 NI 2527 Hardware Diagram 
 [IMAGE alt='image' src='GUID-FE3446FA-FDFC-4979-8D3F-74E820C96CF5-a5.gif'] 
 Note Use the numbers printed on the board to verify the revision
 letter of the NI 2527. (Revision B = ASSY192245B-01; Revision A =
 ASSY192245A-01.) Use the revision letter to determine the correct reference
 designator for the relay you want to replace. 
 Relay Name
 Reference Designator(Revision B)
 Reference Designator (Revision A)k0
 k0
 k33k1
 k1
 k35k2
 k2
 k30k3
 k3
 k38k4
 k4
 k34k5
 k5
 k29k6
 k6
 k25k7
 k7
 k24k8
 k8
 k21k9
 k9
 k20k10
 k10
 k17k11
 k11
 k31k12
 k12
 k16k13
 k13
 k37k14
 k14
 k36k15
 k15
 k26k16
 k16
 k13k17
 k17
 k22k18
 k18
 k6k19
 k19
 k18k20
 k20
 k14k21
 k21
 k11k22
 k22
 k8k23
 k23
 k12k24
 k24
 k9k25
 k25
 k7k26
 k26
 k5k27
 k27
 k10k28
 k28
 k1k29
 k29
 k3k30
 k30
 k4k31
 k31
 k2kbc01
 k32
 k32khlselect0
 k33
 k28kref0
 k34
 k27khlselect1
 k35
 k23kref1
 k36
 k19kcjtemp
 k37
 k15
3. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. The different label types are shown in the following figure.
 [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']

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

If you have a surface mount rework station, replace the relay as you would any other
 surface mount part. Otherwise, complete the following steps to replace the
 relay:

1. Use the soldering iron and solder wick to remove as much solder from the relay
 pads as possible. Do not leave the soldering iron on any lead for more than 5
 seconds. Note If it is necessary to reapply the soldering iron
 to the pad, allow the connection to cool completely before reapplying the
 soldering iron.
2. Apply heat to the pads one at a time, and use the pick to gently pry the relay
 pins from the pads. Make sure that the solder is molten before prying. Caution Using excessive force on a soldered pad can result in
 lifting the PCB trace and ruining the board.
3. Remove the relay.
4. Clean the pads with isopropyl alcohol and cotton swabs.
5. Place the new relay on the PCB pads and solder.
6. Remove the excess flux with isopropyl alcohol and cotton swabs. Caution Do not use flux remover to clean the
 board after relay replacement.

#### Reassemble the Module

Complete the Disassemble the Module steps in reverse order to reassemble your
 module.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI/PXIe-2527

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2527-triggering.html language=enus -->
## TOPIC 00419: NI PXI/PXIe-2527 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2527-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2527-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2527 (NI 2527) recognizes trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI 2527. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) P

### NI PXI/PXIe-2527 Triggering

The NI PXI/PXIe-2527 (NI 2527) recognizes trigger pulse widths less than 150 ns by
 disabling digital filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI 2527.

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

The following table lists valid scan advanced outputs for the NI 2527.

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

NI PXI/PXIe-2527

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2527.html language=enus -->
## TOPIC 00420: NI PXI/PXIe-2527

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2527.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2527.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2527 (NI 2527) is a high-density multiplexer switch module for the PXI or PXI Express platform. The NI 2527 uses armature relays. Switching inductive loads (for example, motors and solenoids) can produce high voltage transients in excess of the module's rated voltage. Without addit

### NI PXI/PXIe-2527

Note

#### Operation Modes

The following table lists the supported topologies of the NI 2527 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 64×1 Multiplexer | 2527/1-Wire 64x1 Mux(NISWITCH_TOPOLOGY_2527_1_WIRE_64X1_MUX) |  |  |
| 1-Wire Dual 32×1 Multiplexer | 2527/1-Wire Dual 32x1 Mux(NISWITCH_TOPOLOGY_2527_1_WIRE_DUAL_32X1_MUX) |  |  |
| 2-Wire 32×1 Multiplexer | 2527/2-Wire 32x1 Mux(NISWITCH_TOPOLOGY_2527_2_WIRE_32X1_MUX) |  |  |
| 2-Wire Dual 16×1 Multiplexer | 2527/2-Wire Dual 16x1 Mux(NISWITCH_TOPOLOGY_2527_2_WIRE_DUAL_16X1_MUX) |  |  |
| 4-Wire 16×1 Multiplexer | 2527/4-Wire 16x1 Mux(NISWITCH_TOPOLOGY_2527_4_WIRE_16X1_MUX) |  |  |
| Independent | 2527/Independent(NISWITCH_TOPOLOGY_2527_INDEPENDENT) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Armature Relays
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI/PXIe-2527 1-Wire 64×1 Multiplexer Topology
- NI PXI/PXIe-2527 1-Wire Dual 32×1 Multiplexer Topology
- NI PXI/PXIe-2527 2-Wire 32×1 Multiplexer Topology
- NI PXI/PXIe-2527 2-Wire Dual 16×1 Multiplexer Topology
- NI PXI/PXIe-2527 4-Wire 16×1 Multiplexer Topology
- NI PXI/PXIe-2527 Independent Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2529-2-wire-4-32-matrix-topology.html language=enus -->
## TOPIC 00421: NI PXI/PXIe-2529 2-Wire 4×32 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2529-2-wire-4-32-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2529-2-wire-4-32-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2634 or the NI TB-2636 terminal block creates a 2-wire 4×32 matrix topology with the NI PXI/PXIe-2529 (NI 2529). The following figure represents the NI 2529 in the 2-wire 4×32 matrix topology. Making a Connection The NI 2529 combined with the NI TB-2634 or the NI TB-2636 creates a 4×32 mat

### NI PXI/PXIe-2529 2-Wire 4×32 Matrix Topology

The NI TB-2634 or the NI TB-2636 terminal block creates a 2-wire 4×32 matrix topology
 with the NI PXI/PXIe-2529 (NI 2529). The following figure represents the NI 2529 in the
 2-wire 4×32 matrix topology.

|  |
| --- |
|  |

#### Making a Connection

The NI 2529 combined with the NI TB-2634 or the NI TB-2636 creates a 4×32 matrix. In
 this topology, you can connect any row to any column. When connecting signals to r1,
 you would connect them to R1+ and R1– in the terminal block. When connecting signals
 to c0, you would connect them to C0+ and C0– in the terminal block.

You can connect the channels of the NI 2529 using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function. For example, to connect row 1 to column 1, call the niSwitch Connect
 Channels VI or the niSwitch_Connect function with the
 channel 1 parameter set to r1 and the
 channel 2 parameter set to c1.

When scanning the NI 2529 in 4×32 matrix topology, a typical scan list entry could be
 r1->c20;. This entry routes the signal connected to row 1 to
 column 20.

#### Bank Connection Diagram

[IMAGE alt='image' src='GUID-2C1E590E-EB00-41EA-A124-6B0549E41FDF-a5.gif']

#### Terminal Block Connections

The NI TB-2634 and NI TB-2636 terminal blocks configure the NI 2529 as a 2-wire 4×32
 matrix.

The following table lists the NI 2529 pins and their associated column connections.
 Refer to the NI 2529 pinout for pin locations.

| Connection | Pins | Connection | Pins | Connection | Pins | Connection | Pins |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C0+ | B24 | C8+ | B19 | C16+ | B14 | C24+ | B9 |
| C0- | A24 | C8- | A19 | C16- | A14 | C24- | A9 |
| C1+ | B23 | C9+ | B18 | C17+ | B13 | C25+ | B8 |
| C1- | A23 | C9- | A18 | C17- | A13 | C25- | A8 |
| C2+ | B22 | C10+ | B17 | C18+ | B12 | C26+ | B7 |
| C2- | A22 | C10- | A17 | C18- | A12 | C26- | A7 |
| C3+ | B21 | C11+ | B16 | C19+ | B11 | C27+ | B6 |
| C3- | A21 | C11- | A16 | C19- | A11 | C27- | A6 |
| C4+ | C24 | C12+ | C19 | C20+ | C14 | C28+ | C9 |
| C4- | D24 | C12- | D19 | C20- | D14 | C28- | D9 |
| C5+ | C23 | C13+ | C18 | C21+ | C13 | C29+ | C8 |
| C5- | D23 | C13- | D18 | C21- | D13 | C29- | D8 |
| C6+ | C22 | C14+ | C17 | C22+ | C12 | C30+ | C7 |
| C6- | D22 | C14- | D17 | C22- | D12 | C30- | D7 |
| C7+ | C21 | C15+ | C16 | C23+ | C11 | C31+ | C6 |
| C7- | D21 | C15- | D16 | C23- | D11 | C32- | D6 |

The following table lists the NI 2529 pins that the NI TB-2634 and NI TB-2636 short
 and the row connections created.

| Connection | Pins | Connection | Pins | Connection | Pins | Connection | Pins |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R0+ | B25,B15 | R1+ | C25,C15 | R2+ | B20,B10 | R3+ | C20,C10 |
| R0- | A25,A15 | R1- | D25,D15 | R2- | A20,A10 | R3- | D20,D10 |

#### Pinout

The following figure identifies the pins for the NI 2529.

[IMAGE alt='image' src='GUID-34E68B48-BA36-4C4E-83ED-BA16B3A205C8-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2529

Related concepts:

- N-Wire Switching Modes
- Matrix
- Operation Modes

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2529-2-wire-8-16-matrix-topology.html language=enus -->
## TOPIC 00422: NI PXI/PXIe-2529 2-Wire 8×16 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2529-2-wire-8-16-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2529-2-wire-8-16-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TB-2635 terminal block creates a 2-wire 8×16 matrix topology with the NI PXI/PXIe-2529 (NI 2529). The following figure represents the NI 2529 in the 2-wire 8×16 matrix topology. Making a Connection The NI 2529 combined with the NI TB-2635 creates an 8×16 matrix. In this topology you can connect

### NI PXI/PXIe-2529 2-Wire 8×16 Matrix Topology

The TB-2635 terminal block creates a 2-wire 8×16 matrix topology with the NI
 PXI/PXIe-2529 (NI 2529). The following figure represents the NI 2529 in the 2-wire 8×16
 matrix topology.

|  |
| --- |
|  |

#### Making a Connection

The NI 2529 combined with the NI TB-2635 creates an 8×16 matrix. In this topology
 you can connect any row to any column. When connecting signals to r1, you would
 connect them to R1+ and R1– in the terminal block. When connecting signals to c0,
 you would connect them to C0+ and C0– in the terminal block.

You can connect the channels of the NI 2529 using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function. For example, to connect row 1 to column 1, call the niSwitch Connect
 Channels VI or the niSwitch_Connect function with the
 channel 1 parameter set to r1 and the
 channel 2 parameter set to c1.

When scanning the NI 2529 in 8×16 matrix topology, a typical scan list entry could be
 r5->c1;. This entry routes the signal connected to row 5 to
 column 1.

#### Bank Connection Diagram

[IMAGE alt='image' src='GUID-4B91611F-A3E2-45AB-8C2F-1F66626984A5-a5.gif']

#### Terminal Block Connections

The NI TB-2635 terminal block configures the NI 2529 as a 2-wire 8×16 matrix.

The following table lists the NI 2529 pins that the NI TB-2635 terminal block shorts
 and the column connections created. If you do not use the NI TB-2635 terminal block,
 short the pins externally to achieve a 2-wire 8×16 matrix topology. Refer to the
 NI 2529 pinout for pin locations.

| Connection | Pins | Connection | Pins | Connection | Pins | Connection | Pins |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C0+ | B24, B14 | C4+ | C24,C14 | C8+ | B19,B9 | C12+ | C19,C9 |
| C0- | A24,A14 | C4- | D24,D14 | C8- | A19,A9 | C12- | D19,D9 |
| C1+ | B23,B13 | C5+ | C23,C13 | C9+ | B18,B8 | C13+ | C18,C8 |
| C1- | A23,A13 | C5- | D23,D13 | C9- | A18,A8 | C13- | D18,D8 |
| C2+ | B22,B12 | C6+ | C22,C12 | C10+ | B17,B7 | C14+ | C17,C7 |
| C2- | A22,A12 | C6- | D22,D12 | C10- | A17,A7 | C14- | D17,D7 |
| C3+ | B21,B11 | C7+ | C21,C11 | C11+ | B16,B6 | C15+ | C16,C6 |
| C3- | A21,A11 | C7- | D21,D11 | C11- | A16,A6 | C15- | D16,D6 |

The following table lists the NI 2529 pins and their associated row connection.

| Connection | Pins | Connection | Pins | Connection | Pins | Connection | Pins |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R0+ | B25 | R2+ | B20 | R4+ | B15 | R6+ | B10 |
| R0- | A25 | R2- | A20 | R4- | A15 | R6- | A10 |
| R1+ | C25 | R3+ | C20 | R5+ | C15 | R7+ | C10 |
| R1- | D25 | R3- | D20 | R5- | D15 | R7- | D10 |

#### Pinout

The following figure identifies the pins for the NI 2529.

[IMAGE alt='image' src='GUID-34E68B48-BA36-4C4E-83ED-BA16B3A205C8-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2529

Related concepts:

- N-Wire Switching Modes
- Matrix
- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2529-2-wire-dual-4-16-matrix-topo.html language=enus -->
## TOPIC 00423: NI PXI/PXIe-2529 2-Wire Dual 4×16 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2529-2-wire-dual-4-16-matrix-topo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2529-2-wire-dual-4-16-matrix-topo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2529 (NI 2529) in the 2-wire dual 4×16 matrix topology. Making a Connection The NI 2529 in this topology creates two banks of 4×16 matrices. You can only connect rows and columns to rows and columns in the same bank. For more information about how to u

### NI PXI/PXIe-2529 2-Wire Dual 4×16 Matrix Topology

The following figure represents the NI PXI/PXIe-2529 (NI 2529) in the 2-wire dual 4×16
 matrix topology.

|  |
| --- |
|  |

#### Making a Connection

The NI 2529 in this topology creates two banks of 4×16 matrices. You can only
 connect rows and columns to rows and columns in the same bank. For more information
 about how to use the NI 2529 in a dual 4×16 matrix configuration, visit
 ni.com/info and enter the info code,
 exudrg.

You can connect the channels of the NI 2529 using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function. For example, to connect bank 0 row 1 to bank 0 column 1, call the niSwitch
 Connect Channels VI or the niSwitch_Connect function with the
 channel 1 parameter set to b0r1 and the
 channel 2 parameter set to b0c1.

When scanning the NI 2529 in dual 4×16 matrix topology, a typical scan list entry
 could be b0r1->b0c1;. This entry routes the signal connected to
 bank 0 row 1 to bank 0 column 1.

Note

#### Bank Connection Diagram

[IMAGE alt='image' src='GUID-4B5CE39E-E843-4C98-9A5C-B156DFD06459-a5.gif']

#### Pinout

The following figure identifies the pins for the NI 2529.

[IMAGE alt='image' src='GUID-34E68B48-BA36-4C4E-83ED-BA16B3A205C8-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2529

Related concepts:

- N-Wire Switching Modes
- Matrix
- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2529-hardware-diagram.html language=enus -->
## TOPIC 00424: NI PXI/PXIe-2529 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2529-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2529-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2529 (NI 2529). Relay names are the same for every topology. The following table lists relay names for the NI 2529. Bank 1Relays Bank 2Relays B0R0C0...B0R0C15 B1R0C0...B1R0C15 B0R1C0...B0R1C15 B1R1C0...B1R1C15 B0R2C0...B0R2C15 B1R

### NI PXI/PXIe-2529 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-5BE00416-C220-44C4-A663-8F716D336834-a5.gif']

The following table lists relay names for the NI 2529.

| Bank 1Relays | Bank 2Relays |
| --- | --- |
| B0R0C0...B0R0C15 | B1R0C0...B1R0C15 |
| B0R1C0...B0R1C15 | B1R1C0...B1R1C15 |
| B0R2C0...B0R2C15 | B1R2C0...B1R2C15 |
| B0R3C0...B0R3C15 | B1R3C0...B1R3C15 |

Parent topic:

NI PXI/PXIe-2529

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2529-matrix-expansion.html language=enus -->
## TOPIC 00425: NI PXI/PXIe-2529 Matrix Expansion

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2529-matrix-expansion.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2529-matrix-expansion.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can expand the NI PXI/PXIe-2529 (NI 2529) matrix using either the NI TB-2634, NI TB-2635, or the NI TB-2636 terminal block. The terminal block you are using determines the matrix expansion procedure you will follow. The following table lists the terminal blocks and matrix topologies available fo

### NI PXI/PXIe-2529 Matrix Expansion

You can expand the NI PXI/PXIe-2529 (NI 2529) matrix using either the NI TB-2634,
 NI TB-2635, or the NI TB-2636 terminal block. The terminal block you are using
 determines the matrix expansion procedure you will follow. The following table lists the
 terminal blocks and matrix topologies available for the NI 2529.

| Terminal Block | Topology(Row x Column) |
| --- | --- |
| NI TB-2634 | 2-wire 4×32, 2-wire dual 4×16 |
| NI TB-2635 | 2-wire 8×16 |
| NI TB-2636 | 2-wire 4×32 |

Parent topic:

NI PXI/PXIe-2529

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2529-relay-replacement.html language=enus -->
## TOPIC 00426: NI PXI/PXIe-2529 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2529-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2529-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2529 uses electromechanical armature relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Aromat (NAiS) AGQ210A4H Complete the following sets of steps to disassemble your module, replace a failed relay, and reassemble your mo

### NI PXI/PXIe-2529 Relay Replacement

The NI PXI/PXIe-2529 uses electromechanical armature relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part |
| --- | --- |
| Aromat (NAiS) | AGQ210A4H |

Complete the following sets of steps to disassemble your module, replace a failed relay,
 and reassemble your module.

#### Disassemble the Module

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your module from electrostatic discharge.
2. Locate the relay you want to replace.
  1. Determine the channel name for the
 relay using the Bank Connection Diagram for your topology.
  2. Match the channel name to its corresponding relay name using the
 following tables. Table 4.Daughterboard Relay Locations (Top
 View)ChannelName
 RelayName
 ChannelName
 RelayName
 ChannelName
 RelayName
 ChannelName
 RelayNameB0ROC0
 K72
 B0R1C0
 K80
 B0R2CO
 K88
 B0R3C0
 K96B0ROC1
 K71
 B0R1C1
 K79
 B0R2C1
 K87
 B0R3C1
 K95B0ROC2
 K70
 B0R1C2
 K78
 B0R2C2
 K86
 B0R3C2
 K94B0ROC3
 K69
 B0R1C3
 K77
 B0R2C3
 K85
 B0R3C3
 K93B0ROC4
 K1
 B0R1C4
 K9
 B0R2C4
 K17
 B0R3C4
 K25B0ROC5
 K2
 B0R1C5
 K10
 B0R2C5
 K18
 B0R3C5
 K26B0ROC6
 K3
 B0R1C6
 K11
 B0R2C6
 K19
 B0R3C6
 K27B0ROC7
 K4
 B0R1C7
 K12
 B0R2C7
 K20
 B0R3C7
 K28B0ROC8
 K68
 B0R1C8
 K76
 B0R2C8
 K84
 B0R3C8
 K92B0ROC9
 K67
 B0R1C9
 K75
 B0R2C9
 K83
 B0R3C9
 K91B0ROC10
 K66
 B0R1C10
 K74
 B0R2C10
 K82
 B0R3C10
 K90B0ROC11
 K65
 B0R1C11
 K73
 B0R2C11
 K81
 B0R3C11
 K89B0ROC12
 K5
 B0R1C12
 K13
 B0R2C12
 K21
 B0R3C12
 K29B0ROC13
 K6
 B0R1C13
 K14
 B0R2C13
 K22
 B0R3C13
 K30B0ROC14
 K7
 B0R1C14
 K15
 B0R2C14
 K23
 B0R3C14
 K31B0ROC15
 K8
 B0R1C15
 K16
 B0R2C15
 K24
 B0R3C15
 K32 
 Table 5.Daughterboard Relay Locations (Bottom View)ChannelName
 RelayName
 ChannelName
 RelayName
 ChannelName
 RelayName
 ChannelName
 RelayNameB1ROC0
 K104
 B1R1C0
 K112
 B1R2CO
 K120
 B1R3C0
 K128B1ROC1
 K103
 B1R1C1
 K111
 B1R2C1
 K119
 B1R3C1
 K127B1ROC2
 K102
 B1R1C2
 K110
 B1R2C2
 K118
 B1R3C2
 K126B1ROC3
 K101
 B1R1C3
 K109
 B1R2C3
 K117
 B1R3C3
 K125B1ROC4
 K33
 B1R1C4
 K41
 B1R2C4
 K49
 B1R3C4
 K57B1ROC5
 K34
 B1R1C5
 K42
 B1R2C5
 K50
 B1R3C5
 K58B1ROC6
 K35
 B1R1C6
 K43
 B1R2C6
 K51
 B1R3C6
 K59B1ROC7
 K36
 B1R1C7
 K44
 B1R2C7
 K52
 B1R3C7
 K60B1ROC8
 K100
 B1R1C8
 K108
 B1R2C8
 K116
 B1R3C8
 K124B1ROC9
 K99
 B1R1C9
 K107
 B1R2C9
 K115
 B1R3C9
 K123B1ROC10
 K98
 B1R1C10
 K106
 B1R2C10
 K114
 B1R3C10
 K122B1ROC11
 K97
 B1R1C11
 K105
 B1R2C11
 K113
 B1R3C11
 K121B1ROC12
 K37
 B1R1C12
 K45
 B1R2C12
 K53
 B1R3C12
 K61B1ROC13
 K38
 B1R1C13
 K46
 B1R2C13
 K54
 B1R3C13
 K62B1ROC14
 K39
 B1R1C14
 K47
 B1R2C14
 K55
 B1R3C14
 K63B1ROC15
 K40
 B1R1C15
 K48
 B1R2C15
 K56
 B1R3C15
 K64
  3. Use the relay name to locate the relay on the daughterboard. Note Relay names are printed on the PCB. 
 Note Older versions of this module might have plastic
 lead covers that you must remove. The module retains full
 specifications even if these covers are not reinstalled.
3. Remove the four screws and two lead covers (if present) that secure the
 daughterboard to the switch assembly. 1
 Screws2
 Lead Covers (if present)
4. To gain access the bottom of the daughterboard, disconnect the PCB interconnect
 cable by lifting the PCB cable latch on the J1 connector. 1
 PCB Interconnect Cable2
 PCB Cable Latch3
 J1 Connector
5. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. The different label types are shown in the following figure.
 [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']

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

If you have a surface mount rework station, replace the relay as you would any other
 surface mount part. Otherwise, complete the following steps to replace the
 relay:

1. Use the soldering iron and solder wick to remove as much solder from the relay
 pads as possible. Do not leave the soldering iron on any lead for more than 5
 seconds. Note If it is necessary to reapply the soldering iron
 to the pad, allow the connection to cool completely before reapplying the
 soldering iron.
2. Apply heat to the pads one at a time, and use the pick to gently pry the relay
 pins from the pads. Make sure that the solder is molten before prying. Caution Using excessive force on a soldered pad can result in
 lifting the PCB trace and ruining the board.
3. Remove the relay.
4. Clean the pads with isopropyl alcohol and cotton swabs.
5. Place the new relay on the PCB pads and solder.
6. Remove the excess flux with isopropyl alcohol and cotton swabs. Caution Do not use flux remover to clean the
 board after relay replacement.

#### Reassemble the Module

Complete the Disassemble the Module steps in reverse order to reassemble your
 module.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI/PXIe-2529

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2529-triggering.html language=enus -->
## TOPIC 00427: NI PXI/PXIe-2529 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2529-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2529-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This module can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI/PXIe-2529 (NI 2529). Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0

### NI PXI/PXIe-2529 Triggering

This module can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI/PXIe-2529
 (NI 2529).

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
| Front Connector | External(NISWITCH_VAL_EXTERNAL) | TRIGIN on TB-2634/2635 terminal blocks |

#### Scan Advanced Output

The following table lists valid scan advanced outputs for the NI 2529.

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
| Front Connector | External(NISWITCH_VAL_EXTERNAL) | TRIGOUT on TB-2634/2635 terminal blocks |

Refer to the niSwitch Configure Scan
 Trigger
 VI or the
 niSwitch_ConfigureScanTrigger
 function for descriptions and values of the trigger inputs and scan advanced
 outputs.

Parent topic:

NI PXI/PXIe-2529

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2529.html language=enus -->
## TOPIC 00428: NI PXI/PXIe-2529

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2529.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2529.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2529 (NI 2529) is a 128 crosspoint, high-density matrix switch module for the PXI or PXI Express platform. The NI 2529 is designed for switching low and high voltages. For low-voltage measurements, the NI 2529 uses relays with <9 µV thermal offset to ensure accurate measurements. S

### NI PXI/PXIe-2529

Note

#### Operation Modes

The following table lists the supported topologies of the NI 2529 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 2-Wire Dual 4×16 Matrix | 2529/2-Wire Dual 4x16 Matrix(NISWITCH_TOPOLOGY_2529_2_WIRE_DUAL_4X16_MATRIX) |  |  |
| 2-Wire 8×16 Matrix | 2529/2-Wire 8x16 Matrix(NISWITCH_TOPOLOGY_2529_2_WIRE_8X16_MATRIX) |  |  |
| 2-Wire 4×32 Matrix | 2529/2-Wire 4x32 Matrix(NISWITCH_TOPOLOGY_2529_2_WIRE_4X32_MATRIX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI/PXIe-2529 2-Wire Dual 4×16 Matrix Topology
- NI PXI/PXIe-2529 2-Wire 8×16 Matrix Topology
- NI PXI/PXIe-2529 2-Wire 4×32 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2531-1-wire-4-128-matrix-topology.html language=enus -->
## TOPIC 00429: NI PXI/PXIe-2531 1-Wire 4×128 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2531-1-wire-4-128-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2531-1-wire-4-128-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2648 terminal block creates a 1-wire 4×128 matrix topology with the NI PXI/PXIe-2531 (NI 2531). The following figure represents the NI 2531 in the 1-wire 4×128 matrix topology. Making a Connection Both the scanning command, r2->c1;, and the immediate operation, niSwitch Connect Channels VI

### NI PXI/PXIe-2531 1-Wire 4×128 Matrix Topology

The NI TB-2648 terminal block creates a 1-wire 4×128 matrix topology with the NI
 PXI/PXIe-2531 (NI 2531). The following figure represents the NI 2531 in the 1-wire 4×128
 matrix topology.

[IMAGE alt='image' src='GUID-0271A590-9880-4550-B289-7AADFF5FE5FB-a5.gif']

#### Making a Connection

Both the scanning command, r2->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r2 and c1, result in the
 following connection:

signal connected to R2 is routed to C1

#### Terminal Block Connections

The NI TB-2648 terminal block connects banks of the NI 2531 to create the 1-wire
 4×128 matrix topology.

#### Bank Connection Diagram

The following figure illustrates how the native banks of the NI 2531 connect using
 the NI TB-2648 to create the 1-wire 4×128 matrix topology.

[IMAGE alt='image' src='GUID-9D8025B0-EE84-41E0-833E-71AAA1AA75F4-a5.gif']

#### Terminal Block Connector Pinouts

The following figure identifies the pins for the NI TB-2648 connectors.

[IMAGE alt='image' src='GUID-97033905-9A84-4569-8DE4-CDC5100EC52F-a5.gif']

#### Pinout

The following figure identifies the pins for the NI 2531.

[IMAGE alt='image' src='GUID-27261C8B-7B65-40BC-B56C-3B221A7410CE-a5.gif']

Parent topic:

NI PXI/PXIe-2531

Related concepts:

- N-Wire Switching Modes
- Matrix

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2531-1-wire-8-64-matrix-topology.html language=enus -->
## TOPIC 00430: NI PXI/PXIe-2531 1-Wire 8×64 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2531-1-wire-8-64-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2531-1-wire-8-64-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2650 terminal block creates a 1-wire 8×64 matrix topology with the NI PXI/PXIe-2531 (NI 2531). The following figure represents the NI 2531 in the 1-wire 8×64 matrix topology. Making a Connection Both the scanning command, r1->c1;, and the immediate operation, niSwitch Connect Channels VI o

### NI PXI/PXIe-2531 1-Wire 8×64 Matrix Topology

The NI TB-2650 terminal block creates a 1-wire 8×64 matrix topology with the NI
 PXI/PXIe-2531 (NI 2531). The following figure represents the NI 2531 in the 1-wire 8×64
 matrix topology.

[IMAGE alt='image' src='GUID-70A123FF-3A51-44B3-A6EB-7A78FD9492A6-a5.gif']

#### Making a Connection

Both the scanning command, r1->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r1 and c1, result in the
 following connection:

signal connected to R1 is routed to C1

#### Terminal Block Connections

The NI TB-2650 terminal block connects banks of the NI 2531 to create the 1-wire 8×64
 matrix topology.

#### Bank Connection Diagram

The following figure illustrates how the native banks of the NI 2531 connect using
 the NI TB-2650 to create the 1-wire 8×64 matrix topology.

[IMAGE alt='image' src='GUID-165DDE9E-7D1D-4670-B946-557E0C2EFF9B-a5.gif']

#### Terminal Block Connector Pinouts

The following figure identifies the pins for the NI TB-2650 connectors.

[IMAGE alt='image' src='GUID-D8D09EFA-DB09-44FC-AF9F-268602652742-a5.gif']

#### Pinout

The following figure identifies the pins for the NI 2531.

[IMAGE alt='image' src='GUID-27261C8B-7B65-40BC-B56C-3B221A7410CE-a5.gif']

Parent topic:

NI PXI/PXIe-2531

Related concepts:

- N-Wire Switching Modes
- Matrix

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2531-1-wire-dual-4-64-matrix-topo.html language=enus -->
## TOPIC 00431: NI PXI/PXIe-2531 1-Wire Dual 4×64 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2531-1-wire-dual-4-64-matrix-topo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2531-1-wire-dual-4-64-matrix-topo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2649 terminal block creates a 1-wire dual 4×64 matrix topology with the NI PXI/PXIe-2531 (NI 2531). The following figure represents the NI 2531 in the 1-wire dual 4×64 matrix topology. Making a Connection For bank 0, both the scanning command, b0r2->b0c1;, and the immediate operation, niSw

### NI PXI/PXIe-2531 1-Wire Dual 4×64 Matrix Topology

The NI TB-2649 terminal block creates a 1-wire dual 4×64 matrix topology with the NI
 PXI/PXIe-2531 (NI 2531). The following figure represents the NI 2531 in the 1-wire dual
 4×64 matrix topology.

[IMAGE alt='image' src='GUID-4D376DE0-203C-4386-BF10-EDB03D3B3570-a5.gif']

#### Making a Connection

For bank 0, both the scanning command, b0r2->b0c1;, and the
 immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters b0r2 and b0c1, result in
 the following connection:

signal connected to B0R2 is routed to B0C1

For bank 1, both the scanning command, b1r2->b1c1;, and the
 immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters b1r2 and b1c1, result in
 the following connection:

signal connected to B1R2 is routed to B1C1

Note

#### Terminal Block Connections

The NI TB-2649 terminal block connects banks of the NI 2531 to create the 1-wire dual
 4×64 matrix topology.

#### Bank Connection Diagram

The following figure illustrates how the native banks of the NI 2531 connect using
 the NI TB-2649 to create the 1-wire dual 4×64 matrix topology.

[IMAGE alt='image' src='GUID-8F5E064C-38AD-4E71-817E-40B72404E38E-a5.gif']

#### Terminal Block Connector Pinouts

The following figure identifies the pins for the NI TB-2649 connectors.

[IMAGE alt='image' src='GUID-660E4A56-A71B-4496-A7A4-130B2793F36A-a5.gif']

#### Pinout

The following figure identifies the pins for the NI 2531.

[IMAGE alt='image' src='GUID-27261C8B-7B65-40BC-B56C-3B221A7410CE-a5.gif']

Parent topic:

NI PXI/PXIe-2531

Related concepts:

- N-Wire Switching Modes
- Matrix

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2531-1-wire-dual-8-32-matrix-topo.html language=enus -->
## TOPIC 00432: NI PXI/PXIe-2531 1-Wire Dual 8×32 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2531-1-wire-dual-8-32-matrix-topo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2531-1-wire-dual-8-32-matrix-topo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2651 terminal block creates a 1-wire dual 8×32 matrix topology with the NI PXI/PXIe-2531 (NI 2531). The following figure represents the NI 2531 in the 1-wire dual 8×32 matrix topology. Making a Connection For bank 0, both the scanning command, b0r1->b0c1;, and the immediate operation, niSw

### NI PXI/PXIe-2531 1-Wire Dual 8×32 Matrix Topology

The NI TB-2651 terminal block creates a 1-wire dual 8×32 matrix topology with the NI
 PXI/PXIe-2531 (NI 2531). The following figure represents the NI 2531 in the 1-wire dual
 8×32 matrix topology.

[IMAGE alt='image' src='GUID-500FD972-F87B-42C4-92B5-3D4DFD9646B5-a5.gif']

#### Making a Connection

For bank 0, both the scanning command, b0r1->b0c1;, and the
 immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters b0r1 and b0c1, result in
 the following connection:

signal connected to B0R1 is routed to B0C1

For bank 1, both the scanning command, b1r1->b1c1;, and the
 immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters b1r1 and b1c1, result in
 the following connection:

signal connected to B1R1 is routed to B1C1

Note

#### Terminal Block Connections

The NI TB-2651 terminal block connects the banks of the NI 2531 to create the 1-wire
 dual 8×32 matrix topology.

#### Bank Connection Diagram

The following figure illustrates how the native banks on the NI 2531 connect using
 the NI TB-2651 to create the 1-wire dual 8×32 matrix topology.

[IMAGE alt='image' src='GUID-75AC66BA-98D3-465F-B145-B567D82C3588-a5.gif']

#### Terminal Block Connector Pinouts

The following figure identifies the pins for the NI TB-2651 connectors.

[IMAGE alt='image' src='GUID-BB6A267D-DB4A-45DA-B62C-D385135FFDD0-a5.gif']

#### Pinout

The following figure identifies the pins for the NI 2531.

[IMAGE alt='image' src='GUID-27261C8B-7B65-40BC-B56C-3B221A7410CE-a5.gif']

Parent topic:

NI PXI/PXIe-2531

Related concepts:

- N-Wire Switching Modes
- Matrix

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2531-1-wire-sixteen-2-16-matrix-t.html language=enus -->
## TOPIC 00433: NI PXI/PXIe-2531 1-Wire Sixteen 2×16 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2531-1-wire-sixteen-2-16-matrix-t.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2531-1-wire-sixteen-2-16-matrix-t.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2531 in the 1-wire sixteen 2×16 matrix topology. Making a Connection Both the scanning command, b15r0->b15c1;, and the immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters b15r0 and b15c1, result in the fol

### NI PXI/PXIe-2531 1-Wire Sixteen 2×16 Matrix Topology

The following figure represents the NI PXI/PXIe-2531 in the 1-wire sixteen 2×16 matrix
 topology.

[IMAGE alt='image' src='GUID-75FACBBF-B0DD-47A0-83FD-99856D7AADE0-a5.gif']

#### Making a Connection

Both the scanning command, b15r0->b15c1;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters b15r0 and b15c1, result
 in the following connection:

signal connected to B15R0 is routed to B15C1

Note

#### Pinout

The following figure identifies the pins for the NI 2531.

[IMAGE alt='image' src='GUID-27261C8B-7B65-40BC-B56C-3B221A7410CE-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2531

Related concepts:

- N-Wire Switching Modes
- Matrix

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2531-hardware-diagram.html language=enus -->
## TOPIC 00434: NI PXI/PXIe-2531 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2531-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2531-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2531 (NI 2531). Hardware relay names are for the native 1-wire sixteen 2×16 matrix topology. The following table lists relay names for the NI 2531. Bank 0Relays Bank 1Relays ... Bank 15Relays kB0R0C0...kB0R0C15 kB1R0C0...kB1R0C1

### NI PXI/PXIe-2531 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-54332090-BC42-47D7-BE96-0C82F073A261-a5.gif']

The following table lists relay names for the NI 2531.

| Bank 0Relays | Bank 1Relays | ... | Bank 15Relays |
| --- | --- | --- | --- |
| kB0R0C0...kB0R0C15 | kB1R0C0...kB1R0C15 | ... | kB15R0C0...kB15R0C15 |
| kB0R1C0...kB0R1C15 | kB1R1C0...kB1R1C15 | ... | kB15R1C0...kB15R1C15 |

Parent topic:

NI PXI/PXIe-2531

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2531-relay-replacement.html language=enus -->
## TOPIC 00435: NI PXI/PXIe-2531 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2531-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2531-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2531 uses reed relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Number Meder CRR05-1A Complete the following sets of steps to disassemble your switch module, replace a failed relay, and reassemble your switch module. Disa

### NI PXI/PXIe-2531 Relay Replacement

The NI PXI/PXIe-2531 uses reed relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| Meder | CRR05-1A |

Complete the following sets of steps to disassemble your switch module, replace a failed
 relay, and reassemble your switch module.

#### Disassemble the Switch Module

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your switch module from electrostatic discharge.
2. Locate the relay you want to replace.
  1. Determine the relay name using the
 Bank Connection Diagram for your topology.
  2. Match the relay name to its corresponding reference designator and
 locate the relay using the following figures and tables. Note The reference designator locations for the top and
 bottom mezzanine boards are identical. Relays are located on both
 sides of each mezzanine board. 
 Top-Left Notched Side of Mezzanine Boards 
 The following figure illustrates relay locations on the side of each
 mezzanine board that has a notch in the top left corner. 
 [IMAGE alt='image' src='GUID-468EF337-DB2F-4AF7-BEB8-314FD7F785FF-a5.gif'] 
 Top-Right Notched Side of Mezzanine Boards 
 The following figure illustrates relay locations on the side of each
 mezzanine board that has a notch in the top right corner. 
 [IMAGE alt='image' src='GUID-AC9736F6-1756-4976-8EF6-2EDCE42BE407-a5.gif'] 
 Table 8.Top Mezzanine Board Relay LocationsRelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorB8R0C0
 K144
 B10R0C0
 K176
 B12R0C0
 K193
 B14R0C0
 K225B8R0C1
 K143
 B10R0C1
 K175
 B12R0C1
 K194
 B14R0C1
 K226B8R0C2
 K142
 B10R0C2
 K174
 B12R0C2
 K195
 B14R0C2
 K227B8R0C3
 K141
 B10R0C3
 K173
 B12R0C3
 K196
 B14R0C3
 K228B8R0C4
 K140
 B10R0C4
 K172
 B12R0C4
 K197
 B14R0C4
 K229B8R0C5
 K139
 B10R0C5
 K171
 B12R0C5
 K198
 B14R0C5
 K230B8R0C6
 K138
 B10R0C6
 K170
 B12R0C6
 K199
 B14R0C6
 K231B8R0C7
 K137
 B10R0C7
 K169
 B12R0C7
 K200
 B14R0C7
 K232B8R0C8
 K136
 B10R0C8
 K168
 B12R0C8
 K201
 B14R0C8
 K233B8R0C9
 K135
 B10R0C9
 K167
 B12R0C9
 K202
 B14R0C9
 K234B8R0C10
 K134
 B10R0C10
 K166
 B12R0C10
 K203
 B14R0C10
 K235B8R0C11
 K133
 B10R0C11
 K165
 B12R0C11
 K204
 B14R0C11
 K236B8R0C12
 K132
 B10R0C12
 K164
 B12R0C12
 K205
 B14R0C12
 K237B8R0C13
 K131
 B10R0C13
 K163
 B12R0C13
 K206
 B14R0C13
 K238B8R0C14
 K130
 B10R0C14
 K162
 B12R0C14
 K207
 B14R0C14
 K239B8R0C15
 K129
 B10R0C15
 K161
 B12R0C15
 K208
 B14R0C15
 K240B8R1C0
 K1
 B10R1C0
 K33
 B12R1C0
 K80
 B14R1C0
 K112B8R1C1
 K2
 B10R1C1
 K34
 B12R1C1
 K79
 B14R1C1
 K111B8R1C2
 K3
 B10R1C2
 K35
 B12R1C2
 K78
 B14R1C2
 K110B8R1C3
 K4
 B10R1C3
 K36
 B12R1C3
 K77
 B14R1C3
 K109B8R1C4
 K5
 B10R1C4
 K37
 B12R1C4
 K76
 B14R1C4
 K108B8R1C5
 K6
 B10R1C5
 K38
 B12R1C5
 K75
 B14R1C5
 K107B8R1C6
 K7
 B10R1C6
 K39
 B12R1C6
 K74
 B14R1C6
 K106B8R1C7
 K8
 B10R1C7
 K40
 B12R1C7
 K73
 B14R1C7
 K105B8R1C8
 K9
 B10R1C8
 K41
 B12R1C8
 K72
 B14R1C8
 K104B8R1C9
 K10
 B10R1C9
 K42
 B12R1C9
 K71
 B14R1C9
 K103B8R1C10
 K11
 B10R1C10
 K43
 B12R1C10
 K70
 B14R1C10
 K102B8R1C11
 K12
 B10R1C11
 K44
 B12R1C11
 K69
 B14R1C11
 K101B8R1C12
 K13
 B10R1C12
 K45
 B12R1C12
 K68
 B14R1C12
 K100B8R1C13
 K14
 B10R1C13
 K46
 B12R1C13
 K67
 B14R1C13
 K99B8R1C14
 K15
 B10R1C14
 K47
 B12R1C14
 K66
 B14R1C14
 K98B8R1C15
 K16
 B10R1C15
 K48
 B12R1C15
 K65
 B14R1C15
 K97B9R0C0
 K160
 B11R0C0
 K192
 B13R0C0
 K209
 B15R0C0
 K241B9R0C1
 K159
 B11R0C1
 K191
 B13R0C1
 K210
 B15R0C1
 K242B9R0C2
 K158
 B11R0C2
 K190
 B13R0C2
 K211
 B15R0C2
 K243B9R0C3
 K157
 B11R0C3
 K189
 B13R0C3
 K212
 B15R0C3
 K244B9R0C4
 K156
 B11R0C4
 K188
 B13R0C4
 K213
 B15R0C4
 K245B9R0C5
 K155
 B11R0C5
 K187
 B13R0C5
 K214
 B15R0C5
 K246B9R0C6
 K154
 B11R0C6
 K186
 B13R0C6
 K215
 B15R0C6
 K247B9R0C7
 K153
 B11R0C7
 K185
 B13R0C7
 K216
 B15R0C7
 K248B9R0C8
 K152
 B11R0C8
 K184
 B13R0C8
 K217
 B15R0C8
 K249B9R0C9
 K151
 B11R0C9
 K183
 B13R0C9
 K218
 B15R0C9
 K250B9R0C10
 K150
 B11R0C10
 K182
 B13R0C10
 K219
 B15R0C10
 K251B9R0C11
 K149
 B11R0C11
 K181
 B13R0C11
 K220
 B15R0C11
 K252B9R0C12
 K148
 B11R0C12
 K180
 B13R0C12
 K221
 B15R0C012
 K253B9R0C13
 K147
 B11R0C13
 K179
 B13R0C13
 K222
 B15R0C13
 K254B9R0C14
 K146
 B11R0C14
 K178
 B13R0C14
 K223
 B15R0C14
 K255B9R0C15
 K145
 B11R0C15
 K177
 B13R0C15
 K224
 B15R0C15
 K256B9R1C0
 K17
 B11R1C0
 K49
 B13R1C0
 K96
 B15R1C0
 K128B9R1C1
 K18
 B11R1C1
 K50
 B13R1C1
 K95
 B15R1C1
 K127B9R1C2
 K19
 B11R1C2
 K51
 B13R1C2
 K94
 B15R1C2
 K126B9R1C3
 K20
 B11R1C3
 K52
 B13R1C3
 K93
 B15R1C3
 K125B9R1C4
 K21
 B11R1C4
 K53
 B13R1C4
 K92
 B15R1C4
 K124B9R1C5
 K22
 B11R1C5
 K54
 B13R1C5
 K91
 B15R1C5
 K123B9R1C6
 K23
 B11R1C6
 K55
 B13R1C6
 K90
 B15R1C6
 K122B9R1C7
 K24
 B11R1C7
 K56
 B13R1C7
 K89
 B15R1C7
 K121B9R1C8
 K25
 B11R1C8
 K57
 B13R1C8
 K88
 B15R1C8
 K120B9R1C9
 K26
 B11R1C9
 K58
 B13R1C9
 K87
 B15R1C9
 K119B9R1C10
 K27
 B11R1C10
 K59
 B13R1C10
 K86
 B15R1C10
 K118B9R1C11
 K28
 B11R1C11
 K60
 B13R1C11
 K85
 B15R1C11
 K117B9R1C12
 K29
 B11R1C12
 K61
 B13R1C12
 K84
 B15R1C12
 K116B9R1C13
 K30
 B11R1C13
 K62
 B13R1C13
 K83
 B15R1C13
 K115B9R1C14
 K31
 B11R1C14
 K63
 B13R1C14
 K82
 B15R1C14
 K114B9R1C15
 K32
 B11R1C15
 K64
 B13R1C15
 K81
 B15R1C15
 K113 
 Table 9.Bottom Mezzanine Board Relay LocationsRelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorB0R0C0
 K144
 B2R0C0
 K176
 B4R0C0
 K193
 B6R0C0
 K225B0R0C1
 K143
 B2R0C1
 K175
 B4R0C1
 K194
 B6R0C1
 K226B0R0C2
 K142
 B2R0C2
 K174
 B4R0C2
 K195
 B6R0C2
 K227B0R0C3
 K141
 B2R0C3
 K173
 B4R0C3
 K196
 B6R0C3
 K228B0R0C4
 K140
 B2R0C4
 K172
 B4R0C4
 K197
 B6R0C4
 K229B0R0C5
 K139
 B2R0C5
 K171
 B4R0C5
 K198
 B6R0C5
 K230B0R0C6
 K138
 B2R0C6
 K170
 B4R0C6
 K199
 B6R0C6
 K231B0R0C7
 K137
 B2R0C7
 K169
 B4R0C7
 K200
 B6R0C7
 K232B0R0C8
 K136
 B2R0C8
 K168
 B4R0C8
 K201
 B6R0C8
 K233B0R0C9
 K135
 B2R0C9
 K167
 B4R0C9
 K202
 B6R0C9
 K234B0R0C10
 K134
 B2R0C10
 K166
 B4R0C10
 K203
 B6R0C10
 K235B0R0C11
 K133
 B2R0C11
 K165
 B4R0C11
 K204
 B6R0C11
 K236B0R0C12
 K132
 B2R0C12
 K164
 B4R0C12
 K205
 B6R0C12
 K237B0R0C13
 K131
 B2R0C13
 K163
 B4R0C13
 K206
 B6R0C13
 K238B0R0C14
 K130
 B2R0C14
 K162
 B4R0C14
 K207
 B6R0C14
 K239B0R0C15
 K129
 B2R0C15
 K161
 B4R0C15
 K208
 B6R0C15
 K240B0R1C0
 K1
 B2R1C0
 K33
 B4R1C0
 K80
 B6R1C0
 K112B0R1C1
 K2
 B2R1C1
 K34
 B4R1C1
 K79
 B6R1C1
 K111B0R1C2
 K3
 B2R1C2
 K35
 B4R1C2
 K78
 B6R1C3
 K110B0R1C3
 K4
 B2R1C3
 K36
 B4R1C3
 K77
 B6R1C3
 K109B0R1C4
 K5
 B2R1C4
 K37
 B4R1C4
 K76
 B6R1C4
 K108B0R1C5
 K6
 B2R1C5
 K38
 B4R1C5
 K75
 B6R1C5
 K107B0R1C6
 K7
 B2R1C6
 K39
 B4R1C6
 K74
 B6R1C6
 K106B0R1C7
 K8
 B2R1C7
 K40
 B4R1C7
 K73
 B6R1C7
 K105B0R1C8
 K9
 B2R1C8
 K41
 B4R1C8
 K72
 B6R1C8
 K104B0R1C9
 K10
 B2R1C9
 K42
 B4R1C9
 K71
 B6R1C9
 K103B0R1C10
 K11
 B2R1C10
 K43
 B4R1C10
 K70
 B6R1C10
 K102B0R1C11
 K12
 B2R1C11
 K44
 B4R1C11
 K69
 B6R1C11
 K101B0R1C12
 K13
 B2R1C12
 K45
 B4R1C12
 K68
 B6R1C12
 K100B0R1C13
 K14
 B2R1C13
 K46
 B4R1C13
 K67
 B6R1C13
 K99B0R1C14
 K15
 B2R1C14
 K47
 B4R1C14
 K66
 B6R1C14
 K98B0R1C15
 K16
 B2R1C15
 K48
 B4R1C15
 K65
 B6R1C15
 K97B1R0C0
 K160
 B3R0C0
 K192
 B5R0C0
 K209
 B7R0C0
 K241B1R0C1
 K159
 B3R0C1
 K191
 B5R0C1
 K210
 B7R0C1
 K242B1R0C2
 K158
 B3R0C2
 K190
 B5R0C2
 K211
 B7R0C2
 K243B1R0C3
 K157
 B3R0C3
 K189
 B5R0C3
 K212
 B7R0C3
 K244B1R0C4
 K156
 B3R0C4
 K188
 B5R0C4
 K213
 B7R0C4
 K245B1R0C5
 K155
 B3R0C5
 K187
 B5R0C5
 K214
 B7R0C5
 K246B1R0C6
 K154
 B3R0C6
 K186
 B5R0C6
 K215
 B7R0C6
 K247B1R0C7
 K153
 B3R0C7
 K185
 B5R0C7
 K216
 B7R0C7
 K248B1R0C8
 K152
 B3R0C8
 K184
 B5R0C8
 K217
 B7R0C8
 K249B1R0C9
 K151
 B3R0C9
 K183
 B5R0C9
 K218
 B7R0C9
 K250B1R0C10
 K150
 B3R0C10
 K182
 B5R0C10
 K219
 B7R0C10
 K251B1R0C11
 K149
 B3R0C11
 K181
 B5R0C11
 K220
 B7R0C11
 K252B1R0C12
 K148
 B3R0C12
 K180
 B5R0C12
 K221
 B7R0C12
 K253B1R0C13
 K147
 B3R0C13
 K179
 B5R0C13
 K222
 B7R0C13
 K254B1R0C14
 K146
 B3R0C14
 K178
 B5R0C14
 K223
 B7R0C14
 K255B1R0C15
 K145
 B3R0C15
 K177
 B5R0C15
 K224
 B7R0C15
 K256B1R1C0
 K17
 B3R1C0
 K49
 B5R1C0
 K96
 B7R1C0
 K128B1R1C1
 K18
 B3R1C1
 K50
 B5R1C1
 K95
 B7R1C1
 K127B1R1C2
 K19
 B3R1C2
 K51
 B5R1C2
 K94
 B7R1C2
 K126B1R1C3
 K20
 B3R1C3
 K52
 B5R1C3
 K93
 B7R1C3
 K125B1R1C4
 K21
 B3R1C4
 K53
 B5R1C4
 K92
 B7R1C4
 K124B1R1C5
 K22
 B3R1C5
 K54
 B5R1C5
 K91
 B7R1C5
 K123B1R1C6
 K23
 B3R1C6
 K55
 B5R1C6
 K90
 B7R1C6
 K122B1R1C7
 K24
 B3R1C7
 K56
 B5R1C7
 K89
 B7R1C7
 K121B1R1C8
 K25
 B3R1C8
 K57
 B5R1C8
 K88
 B7R1C8
 K120B1R1C9
 K26
 B3R1C9
 K58
 B5R1C9
 K87
 B7R1C9
 K119B1R1C10
 K27
 B3R1C10
 K59
 B5R1C10
 K86
 B7R1C10
 K118B1R1C11
 K28
 B3R1C11
 K60
 B5R1C11
 K85
 B7R1C11
 K117B1R1C12
 K29
 B3R1C12
 K61
 B5R1C12
 K84
 B7R1C12
 K116B1R1C13
 K30
 B3R1C13
 K62
 B5R1C13
 K83
 B7R1C13
 K115B1R1C14
 K31
 B3R1C14
 K63
 B5R1C14
 K82
 B7R1C14
 K114B1R1C15
 K32
 B3R1C15
 K64
 B5R1C15
 K81
 B7R1C15
 K113
  3. Use the reference designator to locate the relay on the mezzanine board.
 Note Reference designators are printed on the
 mezzanine boards.
3. Disassemble the module. Refer to Disconnecting the Top Mezzanine Board if the
 relay you want to replace is located on the top mezzanine board. Refer to
 Disconnecting the Bottom Mezzanine Board if the relay you want to replace is
 located on the bottom mezzanine board. Refer to both procedures if you want to
 replace relays on both boards.

#### Disconnecting the Top Mezzanine Board

Complete the following steps to disconnect the top mezzanine board from the driver
 board.

1. Remove the top mezzanine board screws. 1
 Mezzanine Board Screws2
 Driver Board
2. Use a plastic screwdriver to gently pry the top mezzanine board from the driver
 board, prying a little at each corner for an even distribution of pressure until
 the top mezzanine board pops loose. Retain the spacers from between the boards.
 1
 Top Mezzanine Board2
 Driver Board3
 Plastic Screwdriver4
 Spacer

#### Disconnecting the Bottom Mezzanine Board

Complete the following steps to disconnect the bottom mezzanine board from the driver
 board.

1. Remove the mezzanine board screws. 1
 Mezzanine Board Screws2
 Driver Board
2. Disconnect the PCB interconnect cable by lifting the PCB cable latch on the J2
 connector. 1
 J2 Connector2
 PCB Interconnect Cable3
 PCB Cable Latch
3. Separate the daughterboard assembly from the CMI bracket. 1
 CMI Bracket2
 Daughterboard Assembly
4. Use a plastic screwdriver to gently pry the bottom mezzanine board from the
 driver board, prying a little at each corner for an even distribution of
 pressure until the bottom mezzanine board pops loose. Retain the spacers from
 between the boards. 1
 Driver Board2
 Bottom Mezzanine Board3
 Spacer4
 Plastic Screwdriver

#### Replace the Relay

The NI PXI/PXIe-2531 uses lead-free assemblies.

Note

Caution

Make sure you have the following items:

- Hot air rework station with hot air gun set to 371 °C (700 °F) for lead-free
 solder rework
- Temperature-regulated soldering iron set to 371 °C (700 °F) for lead-free solder
 rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Fine tweezers

Complete the following steps to replace the relay:

1. Apply heat with the hot air gun for 30 to 45 seconds in a circular motion around
 the relay, keeping the hot air gun 0.75 to 1 inch (1.91 to 2.54 cm) above the
 daughterboard.
2. Gently lift the relay with tweezers to remove it from the PCB. If the relay does
 not lift easily, apply hot air in a circular motion around the relay two to
 three times and gently try to lift the relay again. Repeat until the solder
 reflows and the relay lifts easily.
3. Use the soldering iron to tin the leads of the new relay.
4. Use the soldering iron to create a uniform distribution of solder on the pads of
 the daughterboard PCB.
5. Use the hot air gun to heat the PCB and the relay leads.
6. Hold the new relay in place on the board with the tweezers while using the hot
 air gun to apply heat in a circular motion until the solder reflows.

#### Reassemble the Module

Refer to the following procedures to reconnect the boards that you disconnected in
 Disassemble the Switch Module.

Tip

Switch Soft Front Panel Help

#### Reconnecting the Top Mezzanine Board

Complete the following steps to reconnect the top mezzanine board to the driver
 board.

1. Align pin holes 179 and 180 on the J4 and J5 connectors of the top mezzanine
 board with pins 179 and 180 of the J3 and J4 connectors on the driver board.
 Gently fold the mezzanine board over onto the driver board as shown in the
 following figure. Leave approximately 6 mm of clearance between the mezzanine
 board and the driver board. Do not press the boards together. Note 
 Ensure the black surface mount J2 and J3 connectors on the mezzanine board
 face away from the driver board, and the notch in the corner of the
 mezzanine board faces the bottom front of the module. 
 1
 Driver Board J4 Connector2
 Driver Board J3 Connector3
 Mezzanine Board J4 Connector4
 Mezzanine Board J5 Connector
2. Replace the spacers between the driver board and top mezzanine board.
3. Secure the top mezzanine board to the driver board using the screws from step
 1.

#### Reconnecting the Bottom Mezzanine Board

Complete the following steps to reconnect the bottom mezzanine board to the driver
 board.

1. Align pin holes 179 and 180 on the J2 and J3 connectors of the bottom mezzanine
 board with pins 179 and 180 of the J5 and J6 connectors on the driver board.
 Gently fold the mezzanine board over onto the driver board as shown in the
 following figure. Leave approximately 6 mm of clearance between the mezzanine
 board and the driver board. Do not press the boards together. Note 
 Ensure the black surface mount J4 and J5 connectors on the mezzanine board
 face away from the driver board, and the notch in the corner of the
 mezzanine board faces the bottom front of the module. 
 1
 Mezzanine Board J2 Connector2
 Mezzanine Board J3 Connector3
 Driver Board J5 Connector4
 Driver Board J6 Connector
2. Connect the PCB interconnect cable to the J2 connector on the bottom mezzanine
 board.
3. Reconnect the daughterboard to the CMI bracket.
4. Replace the spacers between the driver board and bottom mezzanine board.
5. Secure the daughterboard assembly to the CMI bracket using the screws from step
 2.
6. Replace the ejector handle assembly screw from step 1.

Parent topic:

NI PXI/PXIe-2531

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2531-triggering.html language=enus -->
## TOPIC 00436: NI PXI/PXIe-2531 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2531-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2531-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2531 (NI 2531) can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI 2531. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0

### NI PXI/PXIe-2531 Triggering

The NI PXI/PXIe-2531 (NI 2531) can recognize trigger pulse widths less than 150 ns by
 disabling digital filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI 2531.

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

The following table lists valid scan advanced outputs for the NI 2531.

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

NI PXI/PXIe-2531

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2531.html language=enus -->
## TOPIC 00437: NI PXI/PXIe-2531

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2531.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2531.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2531 (NI 2531) is a 512-crosspoint, high-density matrix switch module for the PXI or PXI Express platform. The NI 2531 is designed for switching high and low voltages. Switching inductive loads (for example, motors and solenoids) can produce high voltage transients in excess of the

### NI PXI/PXIe-2531

Note

#### Operation Modes

The following table lists the supported topologies of the NI 2531 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 4×128 Matrix | 2531/1-Wire 4x128 Matrix(NISWITCH_TOPOLOGY_2531_1_WIRE_4X128_MATRIX) |  |  |
| 1-Wire 8×64 Matrix | 2531/1-Wire 8x64 Matrix(NISWITCH_TOPOLOGY_2531_1_WIRE_8X64_MATRIX) |  |  |
| 1-Wire Dual 4×64 Matrix | 2531/1-Wire Dual 4x64 Matrix(NISWITCH_TOPOLOGY_2531_1_WIRE_DUAL_4X64_MATRIX) |  |  |
| 1-Wire Dual 8×32 Matrix | 2531/1-Wire Dual 8x32 Matrix(NISWITCH_TOPOLOGY_2531_1_WIRE_DUAL_8X32_MATRIX) |  |  |
| 1-Wire Sixteen 2×16 Matrix | 2531/1-Wire Dual 8x32 Matrix(NISWITCH_TOPOLOGY_2531_1_WIRE_SIXTEEN_2X16_MATRIX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI/PXIe-2531 1-Wire 4×128 Matrix Topology
- NI PXI/PXIe-2531 1-Wire 8×64 Matrix Topology
- NI PXI/PXIe-2531 1-Wire Dual 4×64 Matrix Topology
- NI PXI/PXIe-2531 1-Wire Dual 8×32 Matrix Topology
- NI PXI/PXIe-2531 1-Wire Sixteen 2×16 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-1-wire-16-32-matrix-to.html language=enus -->
## TOPIC 00438: NI PXI/PXIe-2532/2532B 1-Wire 16×32 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-1-wire-16-32-matrix-to.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-1-wire-16-32-matrix-to.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2642 terminal block creates a 1-wire 16×32 matrix topology with the NI PXI/PXIe-2532 (NI 2532). The NI TB-2642B terminal block creates a 1-wire 16×32 matrix topology with the NI PXI/PXIe-2532B (NI 2532B). The following figure represents the NI 2532/2532B in the 1-wire 16×32 matrix topology

### NI PXI/PXIe-2532/2532B 1-Wire 16×32 Matrix Topology

The NI TB-2642 terminal block creates a 1-wire 16×32 matrix topology with the NI
 PXI/PXIe-2532 (NI 2532). The NI TB-2642B terminal block creates a 1-wire 16×32 matrix
 topology with the NI PXI/PXIe-2532B (NI 2532B). The following figure represents the
 NI 2532/2532B in the 1-wire 16×32 matrix topology.

[IMAGE alt='image' src='GUID-AB2F42D7-2F52-4643-886D-4D50666425AE-a5.gif']

#### Making a Connection

Both the scanning command, r1->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r1 and c1, result in the
 following connection:

signal connected to R1 is routed to C1

#### Terminal Block Connections

The NI TB-2642 terminal block connects banks of the NI 2532 to create the 1-wire
 16×32 matrix topology. The NI TB-2642B terminal block connects banks of the NI 2532B
 to create the 1-wire 16×32 matrix topology. The following figure illustrates how the
 native banks of the NI 2532/2532B connect using the NI TB-2642/2642B to create the
 1-wire 16×32 matrix topology.

#### Bank Connection Diagram

[IMAGE alt='image' src='GUID-33E02998-F6E1-4E0E-B285-32D0753441C2-a5.gif']

The following table lists the pin assignments for the NI TB-2642/2642B column ribbon
 cable headers.

#### Column Pin Connections

The following table refers to the J3 connector on the NI TB-2642 column connection
 board and the J13 connector on the NI TB-2642B.

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | C0 | Pin 9 | C8 | Pin 17 | C16 | Pin 25 | C24 |
| Pin 2 | C1 | Pin 10 | C9 | Pin 18 | C17 | Pin 26 | C25 |
| Pin 3 | C2 | Pin 11 | C10 | Pin 19 | C18 | Pin 27 | C26 |
| Pin 4 | C3 | Pin 12 | C11 | Pin 20 | C19 | Pin 28 | C27 |
| Pin 5 | C4 | Pin 13 | C12 | Pin 21 | C20 | Pin 29 | C28 |
| Pin 6 | C5 | Pin 14 | C13 | Pin 22 | C21 | Pin 30 | C29 |
| Pin 7 | C6 | Pin 15 | C14 | Pin 23 | C22 | Pin 31 | C30 |
| Pin 8 | C7 | Pin 16 | C15 | Pin 24 | C23 | Pin 32 | C31 |

Note

not

#### Row Pin Connections

The NI TB-2642 and NI TB-2642B provide two ribbon cable headers for row connection.
 Use one cable header to connect to your application. Use the other cable header for
 column expansion.

The following table lists the pin assignments for row connection.

| Pin Number | Row |
| --- | --- |
| 1 | RO |
| 2 | R1 |
| 3 | R2 |
| 4 | R3 |
| 5 | R4 |
| 6 | R5 |
| 7 | R6 |
| 8 | R7 |
| 9 | R8 |
| 10 | R9 |
| 11 | R10 |
| 12 | R11 |
| 13 | R12 |
| 14 | R13 |
| 15 | R14 |
| 16 | R15 |

#### Row Protection Bypass Header

Each row signal is isolated from the reed relays through a 100 Ω resistor. To bypass
 this resistor, install a jumper on the appropriate pins of the header indicated in
 the table below. The following table lists the appropriate jumper position for
 bypassing the resistor on each row signal.

| Bypassed Row | NI TB-2642 Module Interface Board |  | NI TB-2642B |  |
| --- | --- | --- | --- | --- |
| Header | Pins Connected | Header | Pins Connected |  |
| R0 | N/A | N/A | J14 | 1-2 |
| R1 | N/A | N/A | J14 | 5-6 |
| R2 | N/A | N/A | J14 | 9-10 |
| R3 | N/A | N/A | J14 | 13-14 |
| R4 | N/A | N/A | J15 | 1-2 |
| R5 | N/A | N/A | J15 | 5-6 |
| R6 | N/A | N/A | J15 | 9-10 |
| R7 | N/A | N/A | J15 | 13-14 |
| R8 | N/A | N/A | J16 | 1-2 |
| R9 | N/A | N/A | J16 | 5-6 |
| R10 | N/A | N/A | J16 | 9-10 |
| R11 | N/A | N/A | J16 | 13-14 |
| R12 | N/A | N/A | J17 | 1-2 |
| R13 | N/A | N/A | J17 | 5-6 |
| R14 | N/A | N/A | J17 | 9-10 |
| R15 | N/A | N/A | J17 | 13-14 |

#### Pinout

The following figure identifies the pins for the NI 2532.

[IMAGE alt='image' src='GUID-0406BFC1-336B-484F-B871-86930D41E140-a5.gif']

Caution

The following figure identifies the pins for the NI 2532B.

[IMAGE alt='image' src='GUID-67DB7EC1-7DE3-4585-A3C4-29F47CDF5F11-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2532/2532B

Related concepts:

- N-Wire Switching Modes
- Matrix
- NI PXI/PXIe-2532/2532B Matrix Expansion

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-1-wire-4-128-matrix-to.html language=enus -->
## TOPIC 00439: NI PXI/PXIe-2532/2532B 1-Wire 4×128 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-1-wire-4-128-matrix-to.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-1-wire-4-128-matrix-to.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2640 terminal block creates a 1-wire 4×128 matrix topology with the NI PXI/PXIe-2532 (NI 2532). The NI TB-2640B terminal block creates a 1-wire 4×128 matrix topology with the NI PXI/PXIe-2532B (NI 2532B). The following figure represents the NI 2532/2532B in the 1-wire 4×128 matrix topology

### NI PXI/PXIe-2532/2532B 1-Wire 4×128 Matrix Topology

The NI TB-2640 terminal block creates a 1-wire 4×128 matrix topology with the NI
 PXI/PXIe-2532 (NI 2532). The NI TB-2640B terminal block creates a 1-wire 4×128 matrix
 topology with the NI PXI/PXIe-2532B (NI 2532B). The following figure represents the
 NI 2532/2532B in the 1-wire 4×128 matrix topology.

[IMAGE alt='image' src='GUID-85BB4AAF-79B6-439D-BDC3-C7EA43150DFF-a5.gif']

#### Making a Connection

Both the scanning command, r2->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r2 and c1, result in the
 following connection:

signal connected to R2 is routed to C1

#### Terminal Block Connections

The NI TB-2640 terminal block connects banks of the NI 2532 to create the 1-wire
 4×128 matrix topology. The NI TB-2640B terminal block connects banks of the NI 2532B
 to create the 1-wire 4×128 matrix topology. The following figure illustrates how the
 native banks of the NI 2532/2532B connect using the NI TB-2640/2640B to create the
 1-wire 4×128 matrix topology.

#### Bank Connection Diagram

[IMAGE alt='image' src='GUID-AEC986E6-493A-4290-B35A-84BAF91D5E7B-a5.gif']

The following tables list the pin assignments for the NI TB-2640/2640B column ribbon
 cable headers.

#### Column Pin Connections

The following table refers to the J3 connector on the upper column connection board
 of the NI TB-2640 and the J13 connector on the NI TB-2640B.

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | C127 | Pin 9 | C119 | Pin 17 | C111 | Pin 25 | C103 |
| Pin 2 | C126 | Pin 10 | C118 | Pin 18 | C110 | Pin 26 | C102 |
| Pin 3 | C125 | Pin 11 | C117 | Pin 19 | C109 | Pin 27 | C101 |
| Pin 4 | C124 | Pin 12 | C116 | Pin 20 | C108 | Pin 28 | C100 |
| Pin 5 | C123 | Pin 13 | C115 | Pin 21 | C107 | Pin 29 | C99 |
| Pin 6 | C122 | Pin 14 | C114 | Pin 22 | C106 | Pin 30 | C98 |
| Pin 7 | C121 | Pin 15 | C113 | Pin 23 | C105 | Pin 31 | C97 |
| Pin 8 | C120 | Pin 16 | C112 | Pin 24 | C104 | Pin 32 | C96 |

The following table refers to the J2 connector on the upper column
 connection board of the NI TB-2640 and the J12 connector on the NI TB-2640B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | C95 | Pin 9 | C87 | Pin 17 | C79 | Pin 25 | C71 |
| Pin 2 | C94 | Pin 10 | C86 | Pin 18 | C78 | Pin 26 | C70 |
| Pin 3 | C93 | Pin 11 | C85 | Pin 19 | C77 | Pin 27 | C69 |
| Pin 4 | C92 | Pin 12 | C84 | Pin 20 | C76 | Pin 28 | C68 |
| Pin 5 | C91 | Pin 13 | C83 | Pin 21 | C75 | Pin 29 | C67 |
| Pin 6 | C90 | Pin 14 | C82 | Pin 22 | C74 | Pin 30 | C66 |
| Pin 7 | C89 | Pin 15 | C81 | Pin 23 | C73 | Pin 31 | C65 |
| Pin 8 | C88 | Pin 16 | C80 | Pin 24 | C72 | Pin 32 | C64 |

The following table refers to the J3 connector on the lower column
 connection board of the NI TB-2640 and the J3 connector on the NI TB-2640B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | C0 | Pin 9 | C8 | Pin 17 | C16 | Pin 25 | C24 |
| Pin 2 | C1 | Pin 10 | C9 | Pin 18 | C17 | Pin 26 | C25 |
| Pin 3 | C2 | Pin 11 | C10 | Pin 19 | C18 | Pin 27 | C26 |
| Pin 4 | C3 | Pin 12 | C11 | Pin 20 | C19 | Pin 28 | C27 |
| Pin 5 | C4 | Pin 13 | C12 | Pin 21 | C20 | Pin 29 | C28 |
| Pin 6 | C5 | Pin 14 | C13 | Pin 22 | C21 | Pin 30 | C29 |
| Pin 7 | C6 | Pin 15 | C14 | Pin 23 | C22 | Pin 31 | C30 |
| Pin 8 | C7 | Pin 16 | C15 | Pin 24 | C23 | Pin 32 | C31 |

The following table refers to the J2 connector on the lower column
 connection board of the NI TB-2640 and the J2 connector on the NI TB-2640B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | C32 | Pin 9 | C40 | Pin 17 | C48 | Pin 25 | C56 |
| Pin 2 | C33 | Pin 10 | C41 | Pin 18 | C49 | Pin 26 | C57 |
| Pin 3 | C34 | Pin 11 | C42 | Pin 19 | C50 | Pin 27 | C58 |
| Pin 4 | C35 | Pin 12 | C43 | Pin 20 | C51 | Pin 28 | C59 |
| Pin 5 | C36 | Pin 13 | C44 | Pin 21 | C52 | Pin 29 | C60 |
| Pin 6 | C37 | Pin 14 | C45 | Pin 22 | C53 | Pin 30 | C61 |
| Pin 7 | C38 | Pin 15 | C46 | Pin 23 | C54 | Pin 31 | C62 |
| Pin 8 | C39 | Pin 16 | C47 | Pin 24 | C55 | Pin 32 | C63 |

#### Row Pin Connections

The NI TB-2640 and NI TB-2640B provide two ribbon cable headers for row connection.
 Use one cable header to connect to your application. Use the other cable header for
 column expansion.

The following table lists the pin assignments for row
 connection:

| Pin Number | Row |
| --- | --- |
| 1 | RO |
| 2 | R1 |
| 3 | R2 |
| 4 | R3 |
| 5–16 | — |

#### Row Protection Bypass
 Header

Each row signal is isolated from the reed relays through a 100 Ω resistor. To bypass
 this resistor, install a jumper on the appropriate pins of the header indicated in
 the table below. The following table lists the appropriate jumper position for
 bypassing the resistor on each row signal:

|  | NI TB-2640 Module Interface Board | NI TB-2640B |  |  |
| --- | --- | --- | --- | --- |
| Bypassed Row | Header | Pins Connected | Header | Pins Connected |
| R0 | J5 | 1-2 | J14 | 1-2 |
| R1 | J5 | 5-6 | J14 | 3-4 |
| R2 | J5 | 9-10 | J14 | 5-6 |
| R3 | J5 | 13-14 | J14 | 7-8 |

#### Pinout

The following figure identifies the pins for the NI 2532:

[IMAGE alt='image' src='GUID-0406BFC1-336B-484F-B871-86930D41E140-a5.gif']

Caution

The following figure identifies the pins for the
 NI 2532B:

[IMAGE alt='image' src='GUID-67DB7EC1-7DE3-4585-A3C4-29F47CDF5F11-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2532/2532B

Related concepts:

- N-Wire Switching Modes
- Matrix
- NI PXI/PXIe-2532/2532B Matrix Expansion

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-1-wire-8-64-matrix-top.html language=enus -->
## TOPIC 00440: NI PXI/PXIe-2532/2532B 1-Wire 8×64 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-1-wire-8-64-matrix-top.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-1-wire-8-64-matrix-top.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2641 terminal block creates a 1-wire 8×64 matrix topology with the NI PXI/PXIe-2532 (NI 2532). The NI TB-2641B terminal block creates a 1-wire 8×64 matrix topology with the NI PXI/PXIe-2532B (NI 2532B).The following figure represents the NI 2532/2532B in the 1-wire 8×64 matrix topology: Ma

### NI PXI/PXIe-2532/2532B 1-Wire 8×64 Matrix Topology

The NI TB-2641 terminal block creates a 1-wire 8×64 matrix topology with the NI
 PXI/PXIe-2532 (NI 2532). The NI TB-2641B terminal block creates a 1-wire 8×64 matrix
 topology with the NI PXI/PXIe-2532B (NI 2532B).The following figure represents the
 NI 2532/2532B in the 1-wire 8×64 matrix topology:

[IMAGE alt='image' src='GUID-F0D330C8-EA63-4078-AC9A-212C37FE423B-a5.gif']

#### Making a Connection

Both the scanning command, r1->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r1 and c1, result in the
 following connection:

signal connected to R1 is routed to C1

#### Terminal Block Connections

The NI TB-2641 terminal block connects banks of the NI 2532 to create the 1-wire 8×64
 matrix topology. The NI TB-2641B terminal block connects banks of the NI 2532B to
 create the 1-wire 8×64 matrix topology. The following figure illustrates how the
 native banks of the NI 2532/2532B connect using the NI TB-2641/2641B to create the
 1-wire 8×64 matrix topology:

#### Bank Connection Diagram

[IMAGE alt='image' src='GUID-360173D1-773E-4C3B-A8A7-BAC2C16424C8-a5.gif']

The following tables list the pin assignments for the NI TB-2641/2641B column ribbon
 cable headers:

#### Column Pin Connections

The following table refers to the J3 connector on the NI TB-2641 column connection
 board and the J3 connector on the NI TB-2641B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | C0 | Pin 9 | C8 | Pin 17 | C16 | Pin 25 | C24 |
| Pin 2 | C1 | Pin 10 | C9 | Pin 18 | C17 | Pin 26 | C25 |
| Pin 3 | C2 | Pin 11 | C10 | Pin 19 | C18 | Pin 27 | C26 |
| Pin 4 | C3 | Pin 12 | C11 | Pin 20 | C19 | Pin 28 | C27 |
| Pin 5 | C4 | Pin 13 | C12 | Pin 21 | C20 | Pin 29 | C28 |
| Pin 6 | C5 | Pin 14 | C13 | Pin 22 | C21 | Pin 30 | C29 |
| Pin 7 | C6 | Pin 15 | C14 | Pin 23 | C22 | Pin 31 | C30 |
| Pin 8 | C7 | Pin 16 | C15 | Pin 24 | C23 | Pin 32 | C31 |

The following table refers to the J2 connector on the NI TB-2641 column connection
 board and the J2 connector on the NI TB-2641B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | C32 | Pin 9 | C40 | Pin 17 | C48 | Pin 25 | C56 |
| Pin 2 | C33 | Pin 10 | C41 | Pin 18 | C49 | Pin 26 | C57 |
| Pin 3 | C34 | Pin 11 | C42 | Pin 19 | C50 | Pin 27 | C58 |
| Pin 4 | C35 | Pin 12 | C43 | Pin 20 | C51 | Pin 28 | C59 |
| Pin 5 | C36 | Pin 13 | C44 | Pin 21 | C52 | Pin 29 | C60 |
| Pin 6 | C37 | Pin 14 | C45 | Pin 22 | C53 | Pin 30 | C61 |
| Pin 7 | C38 | Pin 15 | C46 | Pin 23 | C54 | Pin 31 | C62 |
| Pin 8 | C39 | Pin 16 | C47 | Pin 24 | C55 | Pin 32 | C63 |

#### Row Pin Connections

The NI TB-2641 and NI TB-2641B provide two ribbon cable headers for row connection.
 Use one cable header to connect to your application. Use the other cable header for
 column expansion.

The following table lists the pin assignments for row connection:

| Pin Number | Row |
| --- | --- |
| 1 | RO |
| 2 | R1 |
| 3 | R2 |
| 4 | R3 |
| 5 | R4 |
| 6 | R5 |
| 7 | R6 |
| 8 | R7 |
| 9–16 | — |

#### Row Protection Bypass
 Header

Each row signal is isolated from the reed relays through a 100 Ω resistor. To bypass
 this resistor, install a jumper on the appropriate pins of the header indicated in
 the table below. The following table lists the appropriate jumper position for
 bypassing the resistor on each row signal:

|  | NI TB-2641 Module Interface Board | NI TB-2641B |  |  |
| --- | --- | --- | --- | --- |
| Bypassed Row | Header | Pins Connected | Header | Pins Connected |
| R0 | J4 | 1-2 | J14 | 1-2 |
| R1 | J4 | 3-4 | J14 | 3-4 |
| R2 | J4 | 5-6 | J14 | 5-6 |
| R3 | J4 | 7-8 | J14 | 7-8 |
| R4 | J4 | 9-10 | J14 | 9-10 |
| R5 | J4 | 11-12 | J14 | 11-12 |
| R6 | J4 | 13-14 | J14 | 13-14 |
| R7 | J4 | 15-16 | J14 | 15-16 |

#### Pinout

The following figure identifies the pins for the NI 2532:

[IMAGE alt='image' src='GUID-0406BFC1-336B-484F-B871-86930D41E140-a5.gif']

Caution

The following figure identifies the pins for the NI 2532B:

[IMAGE alt='image' src='GUID-67DB7EC1-7DE3-4585-A3C4-29F47CDF5F11-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2532/2532B

Related concepts:

- N-Wire Switching Modes
- Matrix
- NI PXI/PXIe-2532/2532B Matrix Expansion

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-1-wire-dual-16-16-matr.html language=enus -->
## TOPIC 00441: NI PXI/PXIe-2532/2532B 1-Wire Dual 16×16 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-1-wire-dual-16-16-matr.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-1-wire-dual-16-16-matr.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2645 terminal block creates a 1-wire dual 16×16 matrix topology with the NI PXI/PXIe-2532 (NI 2532). The NI TB-2645B terminal block creates a 1-wire dual 16×16 matrix topology with the NI PXI/PXIe-2532B (NI 2532B).The following figure represents the NI 2532/2532B in the 1-wire dual 16×16 m

### NI PXI/PXIe-2532/2532B 1-Wire Dual 16×16 Matrix Topology

The NI TB-2645 terminal block creates a 1-wire dual 16×16 matrix topology with the NI
 PXI/PXIe-2532 (NI 2532). The NI TB-2645B terminal block creates a 1-wire dual 16×16
 matrix topology with the NI PXI/PXIe-2532B (NI 2532B).The following figure represents
 the NI 2532/2532B in the 1-wire dual 16×16 matrix topology:

[IMAGE alt='image' src='GUID-DFC7E26F-978C-489B-857A-61588D5B32C2-a5.gif']

#### Making a Connection

For bank 0, both the scanning command, b0r1->b0c1;, and the
 immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters b0r1 and b0c1, result in
 the following connection:

signal connected to B0R1 is routed to B0C1

For
 bank 1, both the scanning command, b1r1->b1c1;, and the
 immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters b1r1 and b1c1, result in
 the following connection:

signal connected to B1R1 is routed to B1C1

Note

#### Terminal Block Connections

The NI TB-2645 terminal block connects the banks of the NI 2532 to create the 1-wire
 dual 16×16 matrix topology. The NI TB-2645B terminal block connects the banks of the
 NI 2532B to create the 1-wire dual 16×16 matrix topology. The following figure
 illustrates how the native banks on the NI 2532/2532B connect using the NI
 TB-2645/2645B to create the 1-wire dual 16×16 matrix topology:

#### Bank Connection Diagram

[IMAGE alt='image' src='GUID-CE971336-29A3-4BBD-9ED4-7A590010A947-a5.gif']

The following table lists the pin assignments for the NI TB-2645/2645B column
 ribbon cable headers:

#### Column Pin Connections

The following table refers to the J3 connector on the NI TB-2645 column connection
 board and the J3 connector on the NI TB-2645B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B0C0 | Pin 9 | B0C4 | Pin 17 | B0C8 | Pin 25 | B0C12 |
| Pin 2 | B1C0 | Pin 10 | B1C4 | Pin 18 | B1C8 | Pin 26 | B1C12 |
| Pin 3 | B0C1 | Pin 11 | B0C5 | Pin 19 | B0C9 | Pin 27 | B0C13 |
| Pin 4 | B1C1 | Pin 12 | B1C5 | Pin 20 | B1C9 | Pin 28 | B1C13 |
| Pin 5 | B0C2 | Pin 13 | B0C6 | Pin 21 | B0C10 | Pin 29 | B0C14 |
| Pin 6 | B1C2 | Pin 14 | B1C6 | Pin 22 | B1C10 | Pin 30 | B1C14 |
| Pin 7 | B0C3 | Pin 15 | B0C7 | Pin 23 | B0C11 | Pin 31 | B0C15 |
| Pin 8 | B1C3 | Pin 16 | B1C7 | Pin 24 | B1C11 | Pin 32 | B1C15 |

Note

not

#### Row Pin Connections

The NI TB-2645/2645B requires two row ribbon cables for row connections. The NI
 TB-2645 provides one pair of ribbon cable headers to connect your application. The
 NI TB-2645B provides two pairs of ribbon cable headers. Use one cable header pair to
 connect to your application and the other for column expansion.

The following
 tables list the pin assignments for row connection.

The following table refers
 to the J2 connector on the NI TB-2645 Module Interface Board and the J4 and J5
 connectors on the NI TB-2645B:

| Pin Number | Row |
| --- | --- |
| Pin 1 | B0R0 |
| Pin 2 | B1R0 |
| Pin 3 | B0R1 |
| Pin 4 | B1R1 |
| Pin 5 | B0R2 |
| Pin 6 | B1R2 |
| Pin 7 | B0R3 |
| Pin 8 | B1R3 |
| Pin 9 | B0R4 |
| Pin 10 | B1R4 |
| Pin 11 | B0R5 |
| Pin 12 | B1R5 |
| Pin 13 | B0R6 |
| Pin 14 | B1R6 |
| Pin 15 | B0R7 |
| Pin 16 | B1R7 |

The following table refers to the J3 connector on the NI TB-2645 Module
 Interface Board and the J6 and J7 connectors on the NI TB-2645B:

| Pin Number | Row |
| --- | --- |
| Pin 1 | B0R8 |
| Pin 2 | B1R8 |
| Pin 3 | B0R9 |
| Pin 4 | B1R9 |
| Pin 5 | B0R10 |
| Pin 6 | B1R10 |
| Pin 7 | B0R11 |
| Pin 8 | B1R11 |
| Pin 9 | B0R12 |
| Pin 10 | B1R12 |
| Pin 11 | B0R13 |
| Pin 12 | B1R13 |
| Pin 13 | B0R14 |
| Pin 14 | B1R14 |
| Pin 15 | B0R15 |
| Pin 16 | B1R15 |

#### Row Protection Bypass
 Header

Each row signal is isolated from the reed relays through a 100 Ω resistor. To bypass
 this resistor, install a jumper on the appropriate pins of the header indicated in
 the table below. The following table lists the appropriate jumper position for
 bypassing the resistor on each row signal.

|  | NI TB-2645 Module Interface Board | NI TB-2645B |  |  |
| --- | --- | --- | --- | --- |
| Bypassed Row | Header | Pins Connected | Header | Pins Connected |
| B0R0 | N/A | N/A | J14 | 1-2 |
| B1R0 | N/A | N/A | J14 | 3-4 |
| B0R1 | N/A | N/A | J14 | 5-6 |
| B1R1 | N/A | N/A | J14 | 7-8 |
| B0R2 | N/A | N/A | J14 | 9-10 |
| B1R2 | N/A | N/A | J14 | 11-12 |
| B0R3 | N/A | N/A | J14 | 13-14 |
| B1R3 | N/A | N/A | J14 | 15-16 |
| B0R4 | N/A | N/A | J15 | 1-2 |
| B1R4 | N/A | N/A | J15 | 3-4 |
| B0R5 | N/A | N/A | J15 | 5-6 |
| B1R5 | N/A | N/A | J15 | 7-8 |
| B0R6 | N/A | N/A | J15 | 9-10 |
| B1R6 | N/A | N/A | J15 | 11-12 |
| B0R7 | N/A | N/A | J15 | 13-14 |
| B1R7 | N/A | N/A | J15 | 15-16 |
| B0R8 | N/A | N/A | J16 | 1-2 |
| B1R8 | N/A | N/A | J16 | 3-4 |
| B0R9 | N/A | N/A | J16 | 5-6 |
| B1R9 | N/A | N/A | J16 | 7-8 |
| B0R10 | N/A | N/A | J16 | 9-10 |
| B1R10 | N/A | N/A | J16 | 11-12 |
| B0R11 | N/A | N/A | J16 | 13-14 |
| B1R11 | N/A | N/A | J16 | 15-16 |
| B0R12 | N/A | N/A | J17 | 1-2 |
| B1R12 | N/A | N/A | J17 | 3-4 |
| B0R13 | N/A | N/A | J17 | 5-6 |
| B1R13 | N/A | N/A | J17 | 7-8 |
| B0R14 | N/A | N/A | J17 | 9-10 |
| B1R14 | N/A | N/A | J17 | 11-12 |
| B0R15 | N/A | N/A | J17 | 13-14 |
| B1R15 | N/A | N/A | J17 | 15-16 |

#### Pinout

The following figure identifies the pins for the NI 2532:

[IMAGE alt='image' src='GUID-0406BFC1-336B-484F-B871-86930D41E140-a5.gif']

Caution

The following figure identifies the pins for the
 NI 2532B:

[IMAGE alt='image' src='GUID-67DB7EC1-7DE3-4585-A3C4-29F47CDF5F11-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2532/2532B

Related concepts:

- N-Wire Switching Modes
- Matrix
- NI PXI/PXIe-2532/2532B Matrix Expansion

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-1-wire-dual-4-64-matri.html language=enus -->
## TOPIC 00442: NI PXI/PXIe-2532/2532B 1-Wire Dual 4×64 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-1-wire-dual-4-64-matri.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-1-wire-dual-4-64-matri.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2643 terminal block creates a 1-wire dual 4×64 matrix topology with the NI PXI/PXIe-2532 (NI 2532). The NI TB-2643B terminal block creates a 1-wire dual 4×64 matrix topology with the NI PXI/PXIe-2532B (NI 2532B). The following figure represents the NI 2532/2532B in the 1-wire dual 4×64 mat

### NI PXI/PXIe-2532/2532B 1-Wire Dual 4×64 Matrix Topology

The NI TB-2643 terminal block creates a 1-wire dual 4×64 matrix topology with the NI
 PXI/PXIe-2532 (NI 2532). The NI TB-2643B terminal block creates a 1-wire dual 4×64
 matrix topology with the NI PXI/PXIe-2532B (NI 2532B). The following figure represents
 the NI 2532/2532B in the 1-wire dual 4×64 matrix topology:

[IMAGE alt='image' src='GUID-EB7DA25D-F31C-4533-B926-92A2A519AD78-a5.gif']

#### Making a Connection

For bank 0, both the scanning command, b0r2->b0c1;, and the
 immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters b0r2 and b0c1, result in
 the following connection:

signal connected to B0R2 is routed to B0C1

For
 bank 1, both the scanning command, b1r2->b1c1;, and the
 immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters b1r2 and b1c1, result in
 the following connection:

signal connected to B1R2 is routed to B1C1

Note

#### Terminal Block Connections

The NI TB-2643 terminal block connects banks of the NI 2532 to create the 1-wire dual
 4×64 matrix topology. The NI TB-2643B terminal block connects banks of the NI 2532B
 to create the 1-wire dual 4×64 matrix topology. The following figure illustrates how
 the native banks of the NI 2532/2532B connect using the NI TB-2643/2643B to create
 the 1-wire dual 4×64 matrix topology:

#### Bank Connection Diagram

[IMAGE alt='image' src='GUID-8B2513FB-E3B4-4A75-BAA1-E5DE5368C674-a5.gif']

The following tables list the pin assignments for the NI TB-2643/2643B column
 ribbon cable headers.

#### Column Pin Connections

The following table refers to the J3 connector on the upper column connection board
 of the NI TB-2643 and the J13 connector on the NI TB-2643B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B1C63 | Pin 9 | B1C59 | Pin 17 | B1C55 | Pin 25 | B1C51 |
| Pin 2 | B0C63 | Pin 10 | B0C59 | Pin 18 | B0C55 | Pin 26 | B0C51 |
| Pin 3 | B1C62 | Pin 11 | B1C58 | Pin 19 | B1C54 | Pin 27 | B1C50 |
| Pin 4 | B0C62 | Pin 12 | B0C58 | Pin 20 | B0C54 | Pin 28 | B0C50 |
| Pin 5 | B1C61 | Pin 13 | B1C57 | Pin 21 | B1C53 | Pin 29 | B1C49 |
| Pin 6 | B0C61 | Pin 14 | B0C57 | Pin 22 | B0C53 | Pin 30 | B0C49 |
| Pin 7 | B1C60 | Pin 15 | B1C56 | Pin 23 | B1C52 | Pin 31 | B1C48 |
| Pin 8 | B0C60 | Pin 16 | B0C56 | Pin 24 | B0C52 | Pin 32 | B0C48 |

The following table refers to the J2 connector on the upper column connection
 board of the NI TB-2643 and the J12 connector on the NI TB-2643B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B1C47 | Pin 9 | B1C43 | Pin 17 | B1C39 | Pin 25 | B1C35 |
| Pin 2 | B0C47 | Pin 10 | B0C43 | Pin 18 | B0C39 | Pin 26 | B0C35 |
| Pin 3 | B1C46 | Pin 11 | B1C42 | Pin 19 | B1C38 | Pin 27 | B1C34 |
| Pin 4 | B0C46 | Pin 12 | B0C42 | Pin 20 | B0C38 | Pin 28 | B0C34 |
| Pin 5 | B1C45 | Pin 13 | B1C41 | Pin 21 | B1C37 | Pin 29 | B1C33 |
| Pin 6 | B0C45 | Pin 14 | B0C41 | Pin 22 | B0C37 | Pin 30 | B0C33 |
| Pin 7 | B1C44 | Pin 15 | B1C40 | Pin 23 | B1C36 | Pin 31 | B1C32 |
| Pin 8 | B0C44 | Pin 16 | B0C40 | Pin 24 | B0C36 | Pin 32 | B0C32 |

The following table refers to the J3 connector on the lower column connection
 board of the NI TB-2643 and the J3 connector on the NI TB-2643B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B0C0 | Pin 9 | B0C4 | Pin 17 | B0C8 | Pin 25 | B0C12 |
| Pin 2 | B1C0 | Pin 10 | B1C4 | Pin 18 | B1C8 | Pin 26 | B1C12 |
| Pin 3 | B0C1 | Pin 11 | B0C5 | Pin 19 | B0C9 | Pin 27 | B0C13 |
| Pin 4 | B1C1 | Pin 12 | B1C5 | Pin 20 | B1C9 | Pin 28 | B1C13 |
| Pin 5 | B0C2 | Pin 13 | B0C6 | Pin 21 | B0C10 | Pin 29 | B0C14 |
| Pin 6 | B1C2 | Pin 14 | B1C6 | Pin 22 | B1C10 | Pin 30 | B1C14 |
| Pin 7 | B0C3 | Pin 15 | B0C7 | Pin 23 | B0C11 | Pin 31 | B0C15 |
| Pin 8 | B1C3 | Pin 16 | B1C7 | Pin 24 | B1C11 | Pin 32 | B1C15 |

The following table refers to the J2 connector on the lower column connection
 board of the NI TB-2643 and the J2 connector on the NI TB-2643B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B0C16 | Pin 9 | B0C20 | Pin 17 | B0C24 | Pin 25 | B0C28 |
| Pin 2 | B1C16 | Pin 10 | B1C20 | Pin 18 | B1C24 | Pin 26 | B1C28 |
| Pin 3 | B0C17 | Pin 11 | B0C21 | Pin 19 | B0C25 | Pin 27 | B0C29 |
| Pin 4 | B1C17 | Pin 12 | B1C21 | Pin 20 | B1C25 | Pin 28 | B1C29 |
| Pin 5 | B0C18 | Pin 13 | B0C22 | Pin 21 | B0C26 | Pin 29 | B0C30 |
| Pin 6 | B1C18 | Pin 14 | B1C22 | Pin 22 | B1C26 | Pin 30 | B1C30 |
| Pin 7 | B0C19 | Pin 15 | B0C23 | Pin 23 | B0C27 | Pin 31 | B0C31 |
| Pin 8 | B1C19 | Pin 16 | B1C23 | Pin 24 | B1C27 | Pin 32 | B1C31 |

#### Row Pin Connections

The NI TB-2643 and NI TB-2643B provide two ribbon cable headers for row connection.
 Use one cable header to connect to your application. Use the other cable header for
 column expansion.

The following table lists the pin assignments for row
 connection:

| Pin Number | Row |
| --- | --- |
| 1 | B0R0 |
| 2 | B1R0 |
| 3 | B0R1 |
| 4 | B1R1 |
| 5 | B0R2 |
| 6 | B1R2 |
| 7 | B0R3 |
| 8 | B1R3 |
| 9–16 | — |

#### Row Protection Bypass
 Header

Each row signal is isolated from the reed relays through a 100 Ω resistor. To bypass
 this resistor, install a jumper on the appropriate pins of the header indicated in
 the table below. The following table lists the appropriate jumper position for
 bypassing the resistor on each row signal:

|  | NI TB-2643 Module Interface Board | NI TB-2643B |  |  |
| --- | --- | --- | --- | --- |
| Bypassed Row | Header | Pins Connected | Header | Pins Connected |
| B0R0 | J5 | 1-2 | J14 | 1-2 |
| B1R0 | J5 | 3-4 | J14 | 3-4 |
| B0R1 | J5 | 5-6 | J14 | 5-6 |
| B1R1 | J5 | 7-8 | J14 | 7-8 |
| B0R2 | J5 | 9-10 | J14 | 9-10 |
| B1R2 | J5 | 11-12 | J14 | 11-12 |
| B0R3 | J5 | 13-14 | J14 | 13-14 |
| B1R3 | J5 | 15-16 | J14 | 15-16 |

#### Pinout

The following figure identifies the pins for the NI 2532:

[IMAGE alt='image' src='GUID-0406BFC1-336B-484F-B871-86930D41E140-a5.gif']

Caution

The following figure identifies the pins for the
 NI 2532B:

[IMAGE alt='image' src='GUID-67DB7EC1-7DE3-4585-A3C4-29F47CDF5F11-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2532/2532B

Related concepts:

- N-Wire Switching Modes
- Matrix
- NI PXI/PXIe-2532/2532B Matrix Expansion

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-1-wire-dual-8-32-matri.html language=enus -->
## TOPIC 00443: NI PXI/PXIe-2532/2532B 1-Wire Dual 8×32 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-1-wire-dual-8-32-matri.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-1-wire-dual-8-32-matri.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2644 terminal block creates a 1-wire dual 8×32 matrix topology with the NI PXI/PXIe-2532 (NI 2532). The NI TB-2644B terminal block creates a 1-wire dual 8×32 matrix topology with the NI PXI/PXIe-2532B (NI 2532B).The following figure represents the NI 2532/2532B in the 1-wire dual 8×32 matr

### NI PXI/PXIe-2532/2532B 1-Wire Dual 8×32 Matrix Topology

The NI TB-2644 terminal block creates a 1-wire dual 8×32 matrix topology with the NI
 PXI/PXIe-2532 (NI 2532). The NI TB-2644B terminal block creates a 1-wire dual 8×32
 matrix topology with the NI PXI/PXIe-2532B (NI 2532B).The following figure represents
 the NI 2532/2532B in the 1-wire dual 8×32 matrix topology:

[IMAGE alt='image' src='GUID-90A3BC9A-3059-4900-8FC8-E25DB33444F6-a5.gif']

#### Making a Connection

For bank 0, both the scanning command, b0r1->b0c1;, and the
 immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters b0r1 and b0c1, result in
 the following connection:

signal connected to B0R1 is routed to B0C1

For
 bank 1, both the scanning command, b1r1->b1c1;, and the
 immediate operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters b1r1 and b1c1, result in
 the following connection:

signal connected to B1R1 is routed to B1C1

Note

#### Terminal Block Connections

The NI TB-2644 terminal block connects the banks of the NI 2532 to create the 1-wire
 dual 8×32 matrix topology. The NI TB-2644B terminal block connects the banks of the
 NI 2532B to create the 1-wire dual 8×32 matrix topology. The following figure
 illustrates how the native banks on the NI 2532/2532B connect using the NI
 TB-2644/2644B to create the 1-wire dual 8×32 matrix topology:

#### Bank Connection Diagram

[IMAGE alt='image' src='GUID-2449FE23-6C94-4652-81A4-63F2A6088384-a5.gif']

The following tables list the pin assignments for the NI TB-2644/2644B column
 ribbon cable headers.

#### Column Pin Connections

The following table refers to the J3 connector on the NI TB-2644 column connection
 board and the J3 connector on the NI TB-2644B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B0C0 | Pin 9 | B0C4 | Pin 17 | B0C8 | Pin 25 | B0C12 |
| Pin 2 | B1C0 | Pin 10 | B1C4 | Pin 18 | B1C8 | Pin 26 | B1C12 |
| Pin 3 | B0C1 | Pin 11 | B0C5 | Pin 19 | B0C9 | Pin 27 | B0C13 |
| Pin 4 | B1C1 | Pin 12 | B1C5 | Pin 20 | B1C9 | Pin 28 | B1C13 |
| Pin 5 | B0C2 | Pin 13 | B0C6 | Pin 21 | B0C10 | Pin 29 | B0C14 |
| Pin 6 | B1C2 | Pin 14 | B1C6 | Pin 22 | B1C10 | Pin 30 | B1C14 |
| Pin 7 | B0C3 | Pin 15 | B0C7 | Pin 23 | B0C11 | Pin 31 | B0C15 |
| Pin 8 | B1C3 | Pin 16 | B1C7 | Pin 24 | B1C11 | Pin 32 | B1C15 |

The following table refers to the J2 connector on the NI TB-2644 column
 connection board and the J2 connector on the NI TB-2644B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B0C16 | Pin 9 | B0C20 | Pin 17 | B0C24 | Pin 25 | B0C28 |
| Pin 2 | B1C16 | Pin 10 | B1C20 | Pin 18 | B1C24 | Pin 26 | B1C28 |
| Pin 3 | B0C17 | Pin 11 | B0C21 | Pin 19 | B0C25 | Pin 27 | B0C29 |
| Pin 4 | B1C17 | Pin 12 | B1C21 | Pin 20 | B1C25 | Pin 28 | B1C29 |
| Pin 5 | B0C18 | Pin 13 | B0C22 | Pin 21 | B0C26 | Pin 29 | B0C30 |
| Pin 6 | B1C18 | Pin 14 | B1C22 | Pin 22 | B1C26 | Pin 30 | B1C30 |
| Pin 7 | B0C19 | Pin 15 | B0C23 | Pin 23 | B0C27 | Pin 31 | B0C31 |
| Pin 8 | B1C19 | Pin 16 | B1C23 | Pin 24 | B1C27 | Pin 32 | B1C31 |

#### Row Pin Connections

The NI TB-2644 and NI TB-2644B provide two ribbon cable headers for row connection.
 Use one cable header to connect to your application. Use the other cable header for
 column expansion.

The following table lists the pin assignments for row
 connection:

| Pin Number | Row |
| --- | --- |
| 1 | B0R0 |
| 2 | B1R0 |
| 3 | B0R1 |
| 4 | B1R1 |
| 5 | B0R2 |
| 6 | B1R2 |
| 7 | B0R3 |
| 8 | B1R3 |
| 9 | B0R4 |
| 10 | B1R4 |
| 11 | B0R5 |
| 12 | B1R5 |
| 13 | B0R6 |
| 14 | B1R6 |
| 15 | B0R7 |
| 16 | B1R7 |

#### Row Protection Bypass
 Header

Each row signal is isolated from the reed relays through a 100 Ω resistor. To bypass
 this resistor, install a jumper on the appropriate pins of the header indicated in
 the table below. The following table lists the appropriate jumper position for
 bypassing the resistor on each row signal:

|  | NI TB-2644 Module Interface Board | NI TB-2644B |  |  |
| --- | --- | --- | --- | --- |
| Bypassed Row | Header | Pins Connected | Header | Pins Connected |
| B0R0 | N/A | N/A | J14 | 1-2 |
| B1R0 | N/A | N/A | J14 | 3-4 |
| B0R1 | N/A | N/A | J14 | 5-6 |
| B1R1 | N/A | N/A | J14 | 7-8 |
| B0R2 | N/A | N/A | J14 | 9-10 |
| B1R2 | N/A | N/A | J14 | 11-12 |
| B0R3 | N/A | N/A | J14 | 13-14 |
| B1R3 | N/A | N/A | J14 | 15-16 |
| B0R4 | N/A | N/A | J15 | 1-2 |
| B1R4 | N/A | N/A | J15 | 3-4 |
| B0R5 | N/A | N/A | J15 | 5-6 |
| B1R5 | N/A | N/A | J15 | 7-8 |
| B0R6 | N/A | N/A | J15 | 9-10 |
| B1R6 | N/A | N/A | J15 | 11-12 |
| B0R7 | N/A | N/A | J15 | 13-14 |
| B1R7 | N/A | N/A | J15 | 15-16 |

#### Pinout

The following figure identifies the pins for the NI 2532:

[IMAGE alt='image' src='GUID-0406BFC1-336B-484F-B871-86930D41E140-a5.gif']

Caution

The following figure identifies the pins for the
 NI 2532B:

[IMAGE alt='image' src='GUID-67DB7EC1-7DE3-4585-A3C4-29F47CDF5F11-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2532/2532B

Related concepts:

- N-Wire Switching Modes
- Matrix
- NI PXI/PXIe-2532/2532B Matrix Expansion

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-1-wire-quad-4-32-matri.html language=enus -->
## TOPIC 00444: NI PXI/PXIe-2532/2532B 1-Wire Quad 4×32 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-1-wire-quad-4-32-matri.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-1-wire-quad-4-32-matri.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2646B terminal block creates a 1-wire quad 4×32 matrix topology with the NI PXI/PXIe-2532B (NI 2532B).The following figure represents the NI 2532/2532B in the 1-wire quad 4×32 matrix topology: Making a Connection Both the scanning command, b0r2->b0c1;, and the immediate operation, niSwitch

### NI PXI/PXIe-2532/2532B 1-Wire Quad 4×32 Matrix Topology

The NI TB-2646B terminal block creates a 1-wire quad 4×32 matrix topology with the NI
 PXI/PXIe-2532B (NI 2532B).The following figure represents the NI 2532/2532B in the
 1-wire quad 4×32 matrix topology:

[IMAGE alt='image' src='GUID-57F3AC43-3772-415C-A714-98CFD2475927-a5.gif']

#### Making a Connection

Both the scanning command, b0r2->b0c1;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters b0r2 and b0c1, results in
 the following connection:

signal connected to B0R2 is routed to B0C1.

Note

#### Terminal Block Connections

The NI TB-2646B terminal block connects banks of the NI 2532B to create the 1-wire
 quad 4×32 matrix topology. The following figure illustrates how the sixteen native
 banks of the NI 2532B connect using the NI TB-2646B to create the 1-wire quad 4×32
 matrix topology:

#### Bank Connection Diagram

[IMAGE alt='image' src='GUID-F6F2FE23-89B6-409B-96D6-BA3B39730152-a5.gif']

The following tables list the pin assignments for the NI TB-2646B column ribbon cable
 headers.

#### Column Pin Connections

The following table refers to the J13 connector on the NI TB-2646B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B3C31 | Pin 9 | B3C27 | Pin 17 | B3C23 | Pin 25 | B3C19 |
| Pin 2 | B1C31 | Pin 10 | B1C27 | Pin 18 | B1C23 | Pin 26 | B1C19 |
| Pin 3 | B3C30 | Pin 11 | B3C26 | Pin 19 | B3C22 | Pin 27 | B3C18 |
| Pin 4 | B1C30 | Pin 12 | B1C26 | Pin 20 | B1C22 | Pin 28 | B1C18 |
| Pin 5 | B3C29 | Pin 13 | B3C25 | Pin 21 | B3C21 | Pin 29 | B3C17 |
| Pin 6 | B1C29 | Pin 14 | B1C25 | Pin 22 | B1C21 | Pin 30 | B1C17 |
| Pin 7 | B3C28 | Pin 15 | B3C24 | Pin 23 | B3C20 | Pin 31 | B3C16 |
| Pin 8 | B1C28 | Pin 16 | B1C24 | Pin 24 | B1C20 | Pin 32 | B1C16 |

The following table refers to the J12 connector on the NI TB-2646B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B3C15 | Pin 9 | B3C11 | Pin 17 | B3C7 | Pin 25 | B3C3 |
| Pin 2 | B1C15 | Pin 10 | B1C11 | Pin 18 | B1C7 | Pin 26 | B1C3 |
| Pin 3 | B3C14 | Pin 11 | B3C10 | Pin 19 | B3C6 | Pin 27 | B3C2 |
| Pin 4 | B1C14 | Pin 12 | B1C10 | Pin 20 | B1C6 | Pin 28 | B1C2 |
| Pin 5 | B3C13 | Pin 13 | B3C9 | Pin 21 | B3C5 | Pin 29 | B3C1 |
| Pin 6 | B1C13 | Pin 14 | B1C9 | Pin 22 | B1C5 | Pin 30 | B1C1 |
| Pin 7 | B3C12 | Pin 15 | B3C8 | Pin 23 | B3C4 | Pin 31 | B3C0 |
| Pin 8 | B1C12 | Pin 16 | B1C8 | Pin 24 | B1C4 | Pin 32 | B1C0 |

The following table refers to the J3 connector on the NI TB-2646B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B0C0 | Pin 9 | B0C4 | Pin 17 | B0C8 | Pin 25 | B0C12 |
| Pin 2 | B2C0 | Pin 10 | B2C4 | Pin 18 | B2C8 | Pin 26 | B2C12 |
| Pin 3 | B0C1 | Pin 11 | B0C5 | Pin 19 | B0C9 | Pin 27 | B0C13 |
| Pin 4 | B2C1 | Pin 12 | B2C5 | Pin 20 | B2C9 | Pin 28 | B2C13 |
| Pin 5 | B0C2 | Pin 13 | B0C6 | Pin 21 | B0C10 | Pin 29 | B0C14 |
| Pin 6 | B2C2 | Pin 14 | B2C6 | Pin 22 | B2C10 | Pin 30 | B2C14 |
| Pin 7 | B0C3 | Pin 15 | B0C7 | Pin 23 | B0C11 | Pin 31 | B0C15 |
| Pin 8 | B2C3 | Pin 16 | B2C7 | Pin 24 | B2C11 | Pin 32 | B2C15 |

The following table refers to the J2 connector on the NI TB-2646B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B0C16 | Pin 9 | B0C20 | Pin 17 | B0C24 | Pin 25 | B0C28 |
| Pin 2 | B2C16 | Pin 10 | B2C20 | Pin 18 | B2C24 | Pin 26 | B2C28 |
| Pin 3 | B0C17 | Pin 11 | B0C21 | Pin 19 | B0C25 | Pin 27 | B0C29 |
| Pin 4 | B2C17 | Pin 12 | B2C21 | Pin 20 | B2C25 | Pin 28 | B2C29 |
| Pin 5 | B0C18 | Pin 13 | B0C22 | Pin 21 | B0C26 | Pin 29 | B0C30 |
| Pin 6 | B2C18 | Pin 14 | B2C22 | Pin 22 | B2C26 | Pin 30 | B2C30 |
| Pin 7 | B0C19 | Pin 15 | B0C23 | Pin 23 | B0C27 | Pin 31 | B0C31 |
| Pin 8 | B2C19 | Pin 16 | B2C23 | Pin 24 | B2C27 | Pin 32 | B2C31 |

#### Row Pin Connections

The NI TB-2646B provides two ribbon cable headers for row connection. Use one cable
 header to connect to your application. Use the other cable header for column
 expansion.

The following tables list the pin assignments for the row
 connections.

The following table refers to the J9 connector on the NI
 TB-2646B:

| Pin Number | Row |
| --- | --- |
| 1 | B1R0 |
| 2 | B3R0 |
| 3 | B1R1 |
| 4 | B3R1 |
| 5 | B1R2 |
| 6 | B3R2 |
| 7 | B1R3 |
| 8 | B3R3 |
| 9 | B0R0 |
| 10 | B2R0 |
| 11 | B0R1 |
| 12 | B2R1 |
| 13 | B0R2 |
| 14 | B2R2 |
| 15 | B0R3 |
| 16 | B2R3 |

The following table refers to the J4 connector on the NI TB-2646B:

| Pin Number | Row |
| --- | --- |
| 1 | B0R0 |
| 2 | B2R0 |
| 3 | B0R1 |
| 4 | B2R1 |
| 5 | B0R2 |
| 6 | B2R2 |
| 7 | B0R3 |
| 8 | B2R3 |
| 9 | B1R0 |
| 10 | B3R0 |
| 11 | B1R1 |
| 12 | B3R1 |
| 13 | B1R2 |
| 14 | B3R2 |
| 15 | B1R3 |
| 16 | B3R3 |

#### Row Protection Bypass
 Header

Each row signal is isolated from the reed relays through a 100 Ω resistor. To bypass
 this resistor, install a jumper on the appropriate pins of the header indicated in
 the table below. The following table lists the appropriate jumper position for
 bypassing the resistor on each row signal:

|  | NI TB-2646B |  |
| --- | --- | --- |
| Bypassed Row | Header | Pins Connected |
| B0R0 | J14 | 1-2 |
| B2R0 | J14 | 3-4 |
| B0R1 | J14 | 5-6 |
| B2R1 | J14 | 7-8 |
| B0R2 | J14 | 9-10 |
| B2R2 | J14 | 11-12 |
| B0R3 | J14 | 13-14 |
| B2R3 | J14 | 15-16 |
| B1R0 | J15 | 1-2 |
| B3R0 | J15 | 3-4 |
| B1R1 | J15 | 5-6 |
| B3R1 | J15 | 7-8 |
| B1R2 | J15 | 9-10 |
| B3R2 | J15 | 11-12 |
| B1R3 | J15 | 13-14 |
| B3R3 | J15 | 15-16 |

#### Pinout

The following figure identifies the pins for the NI 2532B:

[IMAGE alt='image' src='GUID-67DB7EC1-7DE3-4585-A3C4-29F47CDF5F11-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2532/2532B

Related concepts:

- N-Wire Switching Modes
- Matrix
- NI PXI/PXIe-2532/2532B Matrix Expansion

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-1-wire-sixteen-2-16-ma.html language=enus -->
## TOPIC 00445: NI PXI/PXIe-2532/2532B 1-Wire Sixteen 2×16 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-1-wire-sixteen-2-16-ma.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-1-wire-sixteen-2-16-ma.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2532/2532B (NI 2532/2532B) in the 1-wire sixteen 2×16 matrix topology. Making a Connection Both the scanning command, b15r0->b15c1;, and the immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters b15r0 and b1

### NI PXI/PXIe-2532/2532B 1-Wire Sixteen 2×16 Matrix Topology

The following figure represents the NI PXI/PXIe-2532/2532B (NI 2532/2532B) in the 1-wire
 sixteen 2×16 matrix topology.

[IMAGE alt='image' src='GUID-F3141CA6-8780-4692-935B-11A5E226200A-a5.gif']

#### Making a Connection

Both the scanning command, b15r0->b15c1;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters b15r0 and b15c1, result
 in the following connection:

signal connected to B15R0 is routed to B15C1

Note

#### Pinout

The following figure identifies the pins for the NI 2532.

[IMAGE alt='image' src='GUID-0406BFC1-336B-484F-B871-86930D41E140-a5.gif']

Caution

The following figure identifies the pins for the NI 2532B.

[IMAGE alt='image' src='GUID-67DB7EC1-7DE3-4585-A3C4-29F47CDF5F11-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2532/2532B

Related concepts:

- N-Wire Switching Modes
- Matrix

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-2-wire-16-16-matrix-to.html language=enus -->
## TOPIC 00446: NI PXI/PXIe-2532/2532B 2-Wire 16×16 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-2-wire-16-16-matrix-to.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-2-wire-16-16-matrix-to.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2645 terminal block creates a 2-wire 16×16 matrix topology with the NI PXI/PXIe-2532 (NI 2532). The NI TB-2645B terminal block creates a 2-wire 16×16 matrix topology with the NI PXI/PXIe-2532B (NI 2532B). The following figure represents the NI 2532/2532B in the 2-wire 16×16 matrix topology

### NI PXI/PXIe-2532/2532B 2-Wire 16×16 Matrix Topology

The NI TB-2645 terminal block creates a 2-wire 16×16 matrix topology with the
 NI PXI/PXIe-2532 (NI 2532). The NI TB-2645B terminal block creates a 2-wire 16×16 matrix
 topology with the NI PXI/PXIe-2532B (NI 2532B). The following figure represents the
 NI 2532/2532B in the 2-wire 16×16 matrix topology:

[IMAGE alt='image' src='GUID-CEE89284-66AE-4C40-848C-347B26D34AE9-a5.gif']

#### Making a Connection

Both the scanning command, r6->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r6 and c1, result in the
 following connections:

- signal connected to R6+ is routed to C1+
- signal connected to R6– is routed to C1–

#### Terminal Block Connections

The NI TB-2645 terminal block connects the banks of the NI 2532 to create the 2-wire
 16×16 matrix topology. The NI TB-2645B terminal block connects the banks of the
 NI 2532B to create the 2-wire 16×16 matrix topology. The following figure
 illustrates how the native banks on the NI 2532/2532B connect using the NI
 TB-2645/2645B to create the 2-wire 16×16 matrix topology:

#### Bank Connection Diagram

[IMAGE alt='image' src='GUID-BFF3F8F7-0760-4A44-9B9C-E52D60042A7B-a5.gif']

The following tables list the pin assignments for the NI TB-2645/2645B column
 ribbon cable headers:

#### Column Pin Connections

The following table refers to the J3 connector on the NI TB-2645 column connection
 board and the J3 connector on the NI TB-2645B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | C0+ | Pin 9 | C4+ | Pin 17 | C8+ | Pin 25 | C12+ |
| Pin 2 | C0– | Pin 10 | C4– | Pin 18 | C8– | Pin 26 | C12– |
| Pin 3 | C1+ | Pin 11 | C5+ | Pin 19 | C9+ | Pin 27 | C13+ |
| Pin 4 | C1– | Pin 12 | C5– | Pin 20 | C9– | Pin 28 | C13– |
| Pin 5 | C2+ | Pin 13 | C6+ | Pin 21 | C10+ | Pin 29 | C14+ |
| Pin 6 | C2– | Pin 14 | C6– | Pin 22 | C10– | Pin 30 | C14– |
| Pin 7 | C3+ | Pin 15 | C7+ | Pin 23 | C11+ | Pin 31 | C15+ |
| Pin 8 | C3– | Pin 16 | C7– | Pin 24 | C11– | Pin 32 | C15– |

Note

not

#### Row Pin Connections

The NI TB-2645/2645B requires two row ribbon cables for row connections. The TB-2645
 provides one pair of ribbon cable headers to connect your application. The TB-2645B
 provides two pairs of ribbon cable headers. Use one cable header pair to connect to
 your application and the other for column expansion.

The following tables list
 the pin assignments for row connection.

The following table refers to the J2
 connector on the NI TB-2645 Module Interface Board and the J4 and J5 connectors on
 the NI TB-2645B:

| Pin Number | Row |
| --- | --- |
| Pin 1 | R0+ |
| Pin 2 | R0– |
| Pin 3 | R1+ |
| Pin 4 | R1– |
| Pin 5 | R2+ |
| Pin 6 | R2– |
| Pin 7 | R3+ |
| Pin 8 | R3– |
| Pin 9 | R4+ |
| Pin 10 | R4– |
| Pin 11 | R5+ |
| Pin 12 | R5– |
| Pin 13 | R6+ |
| Pin 14 | R6– |
| Pin 15 | R7+ |
| Pin 16 | R7– |

The following table refers to the J3 connector on the NI TB-2645 Module
 Interface Board and the J6 and J7 connectors on the NI TB-2645B:

| Pin Number | Row |
| --- | --- |
| Pin 1 | R8+ |
| Pin 2 | R8– |
| Pin 3 | R9+ |
| Pin 4 | R9– |
| Pin 5 | R10+ |
| Pin 6 | R10– |
| Pin 7 | R11+ |
| Pin 8 | R11– |
| Pin 9 | R12+ |
| Pin 10 | R12– |
| Pin 11 | R13+ |
| Pin 12 | R13– |
| Pin 13 | R14+ |
| Pin 14 | R14– |
| Pin 15 | R15+ |
| Pin 16 | R15– |

#### Row Protection Bypass
 Header

Each row signal is isolated from the reed relays through a 100 Ω resistor. To bypass
 this resistor, install a jumper on the appropriate pins of the header indicated in
 the table below. The following table lists the appropriate jumper position for
 bypassing the resistor on each row signal:

|  | NI TB-2645 Module Interface Board | NI TB-2645B |  |  |
| --- | --- | --- | --- | --- |
| Bypassed Row | Header | Pins Connected | Header | Pins Connected |
| R0+ | N/A | N/A | J14 | 1-2 |
| R0- | N/A | N/A | J14 | 3-4 |
| R1+ | N/A | N/A | J14 | 5-6 |
| R1- | N/A | N/A | J14 | 7-8 |
| R2+ | N/A | N/A | J14 | 9-10 |
| R2- | N/A | N/A | J14 | 11-12 |
| R3+ | N/A | N/A | J14 | 13-14 |
| R3- | N/A | N/A | J14 | 15-16 |
| R4+ | N/A | N/A | J15 | 1-2 |
| R4- | N/A | N/A | J15 | 3-4 |
| R5+ | N/A | N/A | J15 | 5-6 |
| R5- | N/A | N/A | J15 | 7-8 |
| R6+ | N/A | N/A | J15 | 9-10 |
| R6- | N/A | N/A | J15 | 11-12 |
| R7+ | N/A | N/A | J15 | 13-14 |
| R7- | N/A | N/A | J15 | 15-16 |
| R8+ | N/A | N/A | J16 | 1-2 |
| R8- | N/A | N/A | J16 | 3-4 |
| R9+ | N/A | N/A | J16 | 5-6 |
| R9- | N/A | N/A | J16 | 7-8 |
| R10+ | N/A | N/A | J16 | 9-10 |
| R10- | N/A | N/A | J16 | 11-12 |
| R11+ | N/A | N/A | J16 | 13-14 |
| R11- | N/A | N/A | J16 | 15-16 |
| R12+ | N/A | N/A | J17 | 1-2 |
| R12- | N/A | N/A | J17 | 3-4 |
| R13+ | N/A | N/A | J17 | 5-6 |
| R13- | N/A | N/A | J17 | 7-8 |
| R14+ | N/A | N/A | J17 | 9-10 |
| R14- | N/A | N/A | J17 | 11-12 |
| R15+ | N/A | N/A | J17 | 13-14 |
| R15- | N/A | N/A | J17 | 15-16 |

#### Pinout

The following figure identifies the pins for the NI 2532:

[IMAGE alt='image' src='GUID-0406BFC1-336B-484F-B871-86930D41E140-a5.gif']

Caution

The following figure identifies the pins for the
 NI 2532B:

[IMAGE alt='image' src='GUID-67DB7EC1-7DE3-4585-A3C4-29F47CDF5F11-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2532/2532B

Related concepts:

- N-Wire Switching Modes
- Matrix
- NI PXI/PXIe-2532/2532B Matrix Expansion

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-2-wire-4-64-matrix-top.html language=enus -->
## TOPIC 00447: NI PXI/PXIe-2532/2532B 2-Wire 4×64 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-2-wire-4-64-matrix-top.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-2-wire-4-64-matrix-top.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2643 terminal block creates a 2-wire 4×64 matrix topology with the NI PXI/PXIe-2532 (NI 2532). The NI TB-2643B terminal block creates a 2-wire 4×64 matrix topology with the NI PXI/PXIe-2532B (NI 2532B). The following figure represents the NI 2532/2532B in the 2-wire 4×64 matrix topology: M

### NI PXI/PXIe-2532/2532B 2-Wire 4×64 Matrix Topology

The NI TB-2643 terminal block creates a 2-wire 4×64 matrix topology with the NI
 PXI/PXIe-2532 (NI 2532). The NI TB-2643B terminal block creates a 2-wire 4×64 matrix
 topology with the NI PXI/PXIe-2532B (NI 2532B). The following figure represents the
 NI 2532/2532B in the 2-wire 4×64 matrix topology:

[IMAGE alt='image' src='GUID-184E615D-5E28-4A5E-89EB-A9CCA858A9D9-a5.gif']

#### Making a Connection

Both the scanning command, r2->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r2 and c1, result in the
 following connections:

- signal connected to R2+ is routed to C1+
- signal connected to R2– is routed to C1–

#### Terminal Block Connections

The NI TB-2643 terminal block connects banks of the NI 2532 to create the 2-wire 4×64
 matrix topology. The NI TB-2643B terminal block connects banks of the NI 2532B to
 create the 2-wire 4×64 matrix topology. The following figure illustrates how the
 native banks of the NI 2532/2532B connect using the NI TB-2643/2643B to create the
 2-wire 4×64 matrix topology:

#### Bank Connection Diagram

[IMAGE alt='image' src='GUID-F1A3CB07-F4F8-44AE-AAFE-EDE5D6315D15-a5.gif']

The following tables list the pin assignments for the NI TB-2643/2643B upper and
 lower column ribbon cable headers:

#### Column Pin Connections

The following table refers to the J3 connector on the upper column connection board
 of the NI TB-2643 and the J13 connector on the NI TB-2643B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | C63– | Pin 9 | C59– | Pin 17 | C55– | Pin 25 | C51– |
| Pin 2 | C63+ | Pin 10 | C59+ | Pin 18 | C55+ | Pin 26 | C51+ |
| Pin 3 | C62– | Pin 11 | C58– | Pin 19 | C54– | Pin 27 | C50– |
| Pin 4 | C62+ | Pin 12 | C58+ | Pin 20 | C54+ | Pin 28 | C50+ |
| Pin 5 | C61– | Pin 13 | C57– | Pin 21 | C53– | Pin 29 | C49– |
| Pin 6 | C61+ | Pin 14 | C57+ | Pin 22 | C53+ | Pin 30 | C49+ |
| Pin 7 | C60– | Pin 15 | C56– | Pin 23 | C52– | Pin 31 | C48– |
| Pin 8 | C60+ | Pin 16 | C56+ | Pin 24 | C52+ | Pin 32 | C48+ |

The following table refers to the J2 connector on the upper column connection
 board of the NI TB-2643 and the J12 connector on the NI TB-2643B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | C47– | Pin 9 | C43– | Pin 17 | C39– | Pin 25 | C35– |
| Pin 2 | C47+ | Pin 10 | C43+ | Pin 18 | C39+ | Pin 26 | C35+ |
| Pin 3 | C46– | Pin 11 | C42– | Pin 19 | C38– | Pin 27 | C34– |
| Pin 4 | C46+ | Pin 12 | C42+ | Pin 20 | C38+ | Pin 28 | C34+ |
| Pin 5 | C45– | Pin 13 | C41– | Pin 21 | C37– | Pin 29 | C33– |
| Pin 6 | C45+ | Pin 14 | C41+ | Pin 22 | C37+ | Pin 30 | C33+ |
| Pin 7 | C44– | Pin 15 | C40– | Pin 23 | C36– | Pin 31 | C32– |
| Pin 8 | C44+ | Pin 16 | C40+ | Pin 24 | C36+ | Pin 32 | C32+ |

The following table refers to the J3 connector on the lower column connection
 board of the NI TB-2643 and the J3 connector on the NI TB-2643B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | C0+ | Pin 9 | C4+ | Pin 17 | C8+ | Pin 25 | C12+ |
| Pin 2 | C0– | Pin 10 | C4– | Pin 18 | C8– | Pin 26 | C12– |
| Pin 3 | C1+ | Pin 11 | C5+ | Pin 19 | C9+ | Pin 27 | C13+ |
| Pin 4 | C1– | Pin 12 | C5– | Pin 20 | C9– | Pin 28 | C13– |
| Pin 5 | C2+ | Pin 13 | C6+ | Pin 21 | C10+ | Pin 29 | C14+ |
| Pin 6 | C2– | Pin 14 | C6– | Pin 22 | C10– | Pin 30 | C14– |
| Pin 7 | C3+ | Pin 15 | C7+ | Pin 23 | C11+ | Pin 31 | C15+ |
| Pin 8 | C3– | Pin 16 | C7– | Pin 24 | C11– | Pin 32 | C15– |

The following table refers to the J2 connector on the lower column connection
 board of the NI TB-2643 and the J2 connector on the NI TB-2643B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | C16+ | Pin 9 | C20+ | Pin 17 | C24+ | Pin 25 | C28+ |
| Pin 2 | C16– | Pin 10 | C20– | Pin 18 | C24– | Pin 26 | C28– |
| Pin 3 | C17+ | Pin 11 | C21+ | Pin 19 | C25+ | Pin 27 | C29+ |
| Pin 4 | C17– | Pin 12 | C21– | Pin 20 | C25– | Pin 28 | C29– |
| Pin 5 | C18+ | Pin 13 | C22+ | Pin 21 | C26+ | Pin 29 | C30+ |
| Pin 6 | C18– | Pin 14 | C22– | Pin 22 | C26– | Pin 30 | C30– |
| Pin 7 | C19+ | Pin 15 | C23+ | Pin 23 | C27+ | Pin 31 | C31+ |
| Pin 8 | C19– | Pin 16 | C23– | Pin 24 | C27– | Pin 32 | C31– |

#### Row Pin Connections

The NI TB-2643 and NI TB-2643B provide two ribbon cable headers for row connection.
 Use one cable header to connect to your application. Use the other cable header for
 column expansion.

The following table lists the pin assignments for row
 connection:

| Pin Number | Row |
| --- | --- |
| 1 | R0+ |
| 2 | R0– |
| 3 | R1+ |
| 4 | R1– |
| 5 | R2+ |
| 6 | R2– |
| 7 | R3+ |
| 8 | R3– |
| 9–16 | — |

#### Row Protection Bypass
 Header

Each row signal is isolated from the reed relays through a 100 Ω resistor. To bypass
 this resistor, install a jumper on the appropriate pins of the header indicated in
 the table below. The following table lists the appropriate jumper position for
 bypassing the resistor on each row signal.

|  | NI TB-2643 Module Interface Board | NI TB-2643B |  |  |
| --- | --- | --- | --- | --- |
| Bypassed Row | Header | Pins Connected | Header | Pins Connected |
| R0+ | J5 | 1-2 | J14 | 1-2 |
| R0- | J5 | 3-4 | J14 | 3-4 |
| R1+ | J5 | 5-6 | J14 | 5-6 |
| R1- | J5 | 7-8 | J14 | 7-8 |
| R2+ | J5 | 9-10 | J14 | 9-10 |
| R2- | J5 | 11-12 | J14 | 11-12 |
| R3+ | J5 | 13-14 | J14 | 13-14 |
| R3- | J5 | 15-16 | J14 | 15-16 |

#### Pinout

The following figure identifies the pins for the NI 2532:

[IMAGE alt='image' src='GUID-0406BFC1-336B-484F-B871-86930D41E140-a5.gif']

Caution

The following figure identifies the pins for the
 NI 2532B:

[IMAGE alt='image' src='GUID-67DB7EC1-7DE3-4585-A3C4-29F47CDF5F11-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2532/2532B

Related concepts:

- N-Wire Switching Modes
- Matrix
- NI PXI/PXIe-2532/2532B Matrix Expansion

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-2-wire-8-32-matrix-top.html language=enus -->
## TOPIC 00448: NI PXI/PXIe-2532/2532B 2-Wire 8×32 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-2-wire-8-32-matrix-top.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-2-wire-8-32-matrix-top.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2644 terminal block creates a 2-wire 8×32 matrix topology with the NI PXI/PXIe-2532 (NI 2532). The NI TB-2644B terminal block creates a 2-wire 8×32 matrix topology with the NI PXI/PXIe-2532B (NI 2532B). The following figure represents the NI 2532/2532B in the 2-wire 8×32 matrix topology: M

### NI PXI/PXIe-2532/2532B 2-Wire 8×32 Matrix Topology

The NI TB-2644 terminal block creates a 2-wire 8×32 matrix topology with the NI
 PXI/PXIe-2532 (NI 2532). The NI TB-2644B terminal block creates a 2-wire 8×32 matrix
 topology with the NI PXI/PXIe-2532B (NI 2532B). The following figure represents the
 NI 2532/2532B in the 2-wire 8×32 matrix topology:

[IMAGE alt='image' src='GUID-10C86859-91CD-4E92-B958-64E9A3859084-a5.gif']

#### Making a Connection

Both the scanning command, r6->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r6 and c1, result in the
 following connections:

- signal connected to R6+ is routed to C1+
- signal connected to R6– is routed to C1–

#### Terminal Block Connections

The NI TB-2644 terminal block connects the banks of the NI 2532 to create the 2-wire
 8×32 matrix topology. The NI TB-2644B terminal block connects the banks of the
 NI 2532B to create the 2-wire 8×32 matrix topology. The following figure illustrates
 how the native banks on the NI 2532/2532B connect using the NI TB-2644/2644B to
 create the 2-wire 8×32 matrix topology:

#### Bank Connection Diagram

[IMAGE alt='image' src='GUID-3DA6E45A-824B-448A-871C-DCFFE371434D-a5.gif']

The following tables list the pin assignments for the NI TB-2644/2644B column
 ribbon cable headers:

#### Column Pin Connections

The following table refers to the J3 connector on the NI TB-2644 column connection
 board and the J3 connector on the NI TB-2644B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | C0+ | Pin 9 | C4+ | Pin 17 | C8+ | Pin 25 | C12+ |
| Pin 2 | C0– | Pin 10 | C4– | Pin 18 | C8– | Pin 26 | C12– |
| Pin 3 | C1+ | Pin 11 | C5+ | Pin 19 | C9+ | Pin 27 | C13+ |
| Pin 4 | C1– | Pin 12 | C5– | Pin 20 | C9– | Pin 28 | C13– |
| Pin 5 | C2+ | Pin 13 | C6+ | Pin 21 | C10+ | Pin 29 | C14+ |
| Pin 6 | C2– | Pin 14 | C6– | Pin 22 | C10– | Pin 30 | C14– |
| Pin 7 | C3+ | Pin 15 | C7+ | Pin 23 | C11+ | Pin 31 | C15+ |
| Pin 8 | C3– | Pin 16 | C7– | Pin 24 | C11– | Pin 32 | C15– |

The following table refers to the J2 connector on the NI TB-2644 column
 connection board and the J2 connector on the NI TB-2644B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | C16+ | Pin 9 | C20+ | Pin 17 | C24+ | Pin 25 | C28+ |
| Pin 2 | C16– | Pin 10 | C20– | Pin 18 | C24– | Pin 26 | C28– |
| Pin 3 | C17+ | Pin 11 | C21+ | Pin 19 | C25+ | Pin 27 | C29+ |
| Pin 4 | C17– | Pin 12 | C21– | Pin 20 | C25– | Pin 28 | C29– |
| Pin 5 | C18+ | Pin 13 | C22+ | Pin 21 | C26+ | Pin 29 | C30+ |
| Pin 6 | C18– | Pin 14 | C22– | Pin 22 | C26– | Pin 30 | C30– |
| Pin 7 | C19+ | Pin 15 | C23+ | Pin 23 | C27+ | Pin 31 | C31+ |
| Pin 8 | C19– | Pin 16 | C23– | Pin 24 | C27– | Pin 32 | C31– |

#### Row Pin Connections

The NI TB-2644 and NI TB-2644B provide two ribbon cable headers for row connection.
 Use one cable header to connect to your application. Use the other cable header for
 column expansion.

The following table lists the pin assignments for row
 connection:

| Pin Number | Row |
| --- | --- |
| 1 | R0+ |
| 2 | R0– |
| 3 | R1+ |
| 4 | R1– |
| 5 | R2+ |
| 6 | R2– |
| 7 | R3+ |
| 8 | R3– |
| 9 | R4+ |
| 10 | R4– |
| 11 | R5+ |
| 12 | R5– |
| 13 | R6+ |
| 14 | R6– |
| 15 | R7+ |
| 16 | R7– |

#### Row Protection Bypass
 Header

Each row signal is isolated from the reed relays through a 100 Ω resistor. To bypass
 this resistor, install a jumper on the appropriate pins of the header indicated in
 the table below. The following table lists the appropriate jumper position for
 bypassing the resistor on each row signal:

|  | NI TB-2644 Module Interface Board | NI TB-2644B |  |  |
| --- | --- | --- | --- | --- |
| Bypassed Row | Header | Pins Connected | Header | Pins Connected |
| R0+ | N/A | N/A | J14 | 1-2 |
| R0- | N/A | N/A | J14 | 3-4 |
| R1+ | N/A | N/A | J14 | 5-6 |
| R1- | N/A | N/A | J14 | 7-8 |
| R2+ | N/A | N/A | J14 | 9-10 |
| R2- | N/A | N/A | J14 | 11-12 |
| R3+ | N/A | N/A | J14 | 13-14 |
| R3- | N/A | N/A | J14 | 15-16 |
| R4+ | N/A | N/A | J15 | 1-2 |
| R4- | N/A | N/A | J15 | 3-4 |
| R5+ | N/A | N/A | J15 | 5-6 |
| R5- | N/A | N/A | J15 | 7-8 |
| R6+ | N/A | N/A | J15 | 9-10 |
| R6- | N/A | N/A | J15 | 11-12 |
| R7+ | N/A | N/A | J15 | 13-14 |
| R7- | N/A | N/A | J15 | 15-16 |

#### Pinout

The following figure identifies the pins for the NI 2532:

[IMAGE alt='image' src='GUID-0406BFC1-336B-484F-B871-86930D41E140-a5.gif']

Caution

The following figure identifies the pins for the
 NI 2532B:

[IMAGE alt='image' src='GUID-67DB7EC1-7DE3-4585-A3C4-29F47CDF5F11-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2532/2532B

Related concepts:

- N-Wire Switching Modes
- Matrix
- NI PXI/PXIe-2532/2532B Matrix Expansion

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-2-wire-dual-4-32-matri.html language=enus -->
## TOPIC 00449: NI PXI/PXIe-2532/2532B 2-Wire Dual 4×32 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-2-wire-dual-4-32-matri.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-2-wire-dual-4-32-matri.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI TB-2646B terminal block creates a 2-wire dual 4×32 matrix topology with the NI PXI/PXIe-2532B (NI 2532B). The following figure represents the NI 2532/2532B in the 2-wire dual 4×32 matrix topology: Making a Connection Both the scanning command, b0r2->b0c1;, and the immediate operation, niSwitc

### NI PXI/PXIe-2532/2532B 2-Wire Dual 4×32 Matrix Topology

The NI TB-2646B terminal block creates a 2-wire dual 4×32 matrix topology with the NI
 PXI/PXIe-2532B (NI 2532B). The following figure represents the NI 2532/2532B in the
 2-wire dual 4×32 matrix topology:

[IMAGE alt='image' src='GUID-64812A81-A868-4AFC-9EA2-61657D4F636F-a5.gif']

#### Making a Connection

Both the scanning command, b0r2->b0c1;, and the immediate
 operation, niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters b0r2 and b0c1, result in
 the following connections:

- signal connected to B0R2+ is routed to B0C1+
- signal connected to B0R2– is routed to B0C1–

Note

#### Terminal Block Connections

The NI TB-2646B terminal block connects banks of the NI 2532B to create the 2-wire
 dual 4×32 matrix topology. The following figure illustrates how the native banks of
 the NI 2532B connect using the NI TB-2646B to create the 2-wire dual 4×32 matrix
 topology:

#### Bank Connection Diagram

[IMAGE alt='image' src='GUID-FAE6FD56-813E-4D22-B94A-6D1B2E41FE15-a5.gif']

The following tables list the pin assignments for the NI TB-2646B column ribbon
 cable headers.

#### Column Pin Connections

The following table refers to the J13 connector on the NI TB-2646B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B1C31– | Pin 9 | B1C27– | Pin 17 | B1C23– | Pin 25 | B1C19– |
| Pin 2 | B1C31+ | Pin 10 | B1C27+ | Pin 18 | B1C23+ | Pin 26 | B1C19+ |
| Pin 3 | B1C30– | Pin 11 | B1C26– | Pin 19 | B1C22– | Pin 27 | B1C18– |
| Pin 4 | B1C30+ | Pin 12 | B1C26+ | Pin 20 | B1C22+ | Pin 28 | B1C18+ |
| Pin 5 | B1C29– | Pin 13 | B1C25– | Pin 21 | B1C21– | Pin 29 | B1C17– |
| Pin 6 | B1C29+ | Pin 14 | B1C25+ | Pin 22 | B1C21+ | Pin 30 | B1C17+ |
| Pin 7 | B1C28– | Pin 15 | B1C24– | Pin 23 | B1C20– | Pin 31 | B1C16– |
| Pin 8 | B1C28+ | Pin 16 | B1C24+ | Pin 24 | B1C20+ | Pin 32 | B1C16+ |

The following table refers to the J12 connector on the NI TB-2646B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B1C15– | Pin 9 | B1C11– | Pin 17 | B1C7– | Pin 25 | B1C3– |
| Pin 2 | B1C15+ | Pin 10 | B1C11+ | Pin 18 | B1C7+ | Pin 26 | B1C3+ |
| Pin 3 | B1C14– | Pin 11 | B1C10– | Pin 19 | B1C6– | Pin 27 | B1C2– |
| Pin 4 | B1C14+ | Pin 12 | B1C10+ | Pin 20 | B1C6+ | Pin 28 | B1C2+ |
| Pin 5 | B1C13– | Pin 13 | B1C9– | Pin 21 | B1C5– | Pin 29 | B1C1– |
| Pin 6 | B1C13+ | Pin 14 | B1C9+ | Pin 22 | B1C5+ | Pin 30 | B1C1+ |
| Pin 7 | B1C12– | Pin 15 | B1C8– | Pin 23 | B1C4– | Pin 31 | B1C0– |
| Pin 8 | B1C12+ | Pin 16 | B1C8+ | Pin 24 | B1C4+ | Pin 32 | B1C0+ |

The following table refers to the J3 connector on the NI TB-2646B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B0C0+ | J3 Pin 9 | B0C4+ | J3 Pin 17 | B0C8+ | J3 Pin 25 | B0C12+ |
| J3 Pin 2 | B0C0– | J3 Pin 10 | B0C4– | J3 Pin 18 | B0C8– | J3 Pin 26 | B0C12– |
| J3 Pin 3 | B0C1+ | J3 Pin 11 | B0C5+ | J3 Pin 19 | B0C9+ | J3 Pin 27 | B0C13+ |
| J3 Pin 4 | B0C1– | J3 Pin 12 | B0C5– | J3 Pin 20 | B0C9– | J3 Pin 28 | B0C13– |
| J3 Pin 5 | B0C2+ | J3 Pin 13 | B0C6+ | J3 Pin 21 | B0C10+ | J3 Pin 29 | B0C14+ |
| J3 Pin 6 | B0C2– | J3 Pin 14 | B0C6– | J3 Pin 22 | B0C10– | J3 Pin 30 | B0C14– |
| J3 Pin 7 | B0C3+ | J3 Pin 15 | B0C7+ | J3 Pin 23 | B0C11+ | J3 Pin 31 | B0C15+ |
| J3 Pin 8 | B0C3– | J3 Pin 16 | B0C7– | J3 Pin 24 | B0C11– | J3 Pin 32 | B0C15– |

The following table refers to the J2 connector on the NI TB-2646B:

| Pin Number | Column | Pin Number | Column | Pin Number | Column | Pin Number | Column |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin 1 | B0C16+ | Pin 9 | B0C20+ | Pin 17 | B0C24+ | Pin 25 | B0C28+ |
| Pin 2 | B0C16– | Pin 10 | B0C20– | Pin 18 | B0C24– | Pin 26 | B0C28– |
| Pin 3 | B0C17+ | Pin 11 | B0C21+ | Pin 19 | B0C25+ | Pin 27 | B0C29+ |
| Pin 4 | B0C17– | Pin 12 | B0C21– | Pin 20 | B0C25– | Pin 28 | B0C29– |
| Pin 5 | B0C18+ | Pin 13 | B0C22+ | Pin 21 | B0C26+ | Pin 29 | B0C30+ |
| Pin 6 | B0C18– | Pin 14 | B0C22– | Pin 22 | B0C26– | Pin 30 | B0C30– |
| Pin 7 | B0C19+ | Pin 15 | B0C23+ | Pin 23 | B0C27+ | Pin 31 | B0C31+ |
| Pin 8 | B0C19– | Pin 16 | B0C23– | Pin 24 | B0C27– | Pin 32 | B0C31– |

#### Row Pin Connections

The NI TB-2646B provides two ribbon cable headers for row connection. Use one cable
 header to connect to your application. Use the other cable header for column
 expansion.

The following tables list the pin assignments for row
 connection.

The following table refers to the J9 connector on the NI
 TB-2646B:

| Pin Number | Row |
| --- | --- |
| 1 | B1R0+ |
| 2 | B1R0– |
| 3 | B1R1+ |
| 4 | B1R1– |
| 5 | B1R2+ |
| 6 | B1R2– |
| 7 | B1R3+ |
| 8 | B1R3– |
| 9 | B0R0+ |
| 10 | B0R0– |
| 11 | B0R1+ |
| 12 | B0R1– |
| 13 | B0R2+ |
| 14 | B0R2– |
| 15 | B0R3+ |
| 16 | B0R3– |

The following table refers to the J4 connector on the NI TB-2646B:

| Pin Number | Row |
| --- | --- |
| 1 | B0R0+ |
| 2 | B0R0– |
| 3 | B0R1+ |
| 4 | B0R1– |
| 5 | B0R2+ |
| 6 | B0R2– |
| 7 | B0R3+ |
| 8 | B0R3– |
| 9 | B1R0+ |
| 10 | B1R0– |
| 11 | B1R1+ |
| 12 | B1R1– |
| 13 | B1R2+ |
| 14 | B1R2– |
| 15 | B1R3+ |
| 16 | B1R3– |

#### Row Protection Bypass
 Header

Each row signal is isolated from the reed relays through a 100 Ω resistor. To bypass
 this resistor, install a jumper on the appropriate pins of the header indicated in
 the table below. The following table lists the appropriate jumper position for
 bypassing the resistor on each row signal:

|  | NI TB-2646B |  |
| --- | --- | --- |
| Bypassed Row | Header | Pins Connected |
| B0R0+ | J14 | 1-2 |
| B0R0- | J14 | 3-4 |
| B0R1+ | J14 | 5-6 |
| B0R1- | J14 | 7-8 |
| B0R2+ | J14 | 9-10 |
| B0R2- | J14 | 11-12 |
| B0R3+ | J14 | 13-14 |
| B0R3- | J14 | 15-16 |
| B1R0+ | J15 | 1-2 |
| B1R0- | J15 | 3-4 |
| B1R1+ | J15 | 5-6 |
| B1R1- | J15 | 7-8 |
| B1R2+ | J15 | 9-10 |
| B1R2- | J15 | 11-12 |
| B1R3+ | J15 | 13-14 |
| B1R3- | J15 | 15-16 |

#### Pinout

The following figure identifies the pins for the NI 2532B:

[IMAGE alt='image' src='GUID-67DB7EC1-7DE3-4585-A3C4-29F47CDF5F11-a5.gif']

Caution

Parent topic:

NI PXI/PXIe-2532/2532B

Related concepts:

- N-Wire Switching Modes
- Matrix
- NI PXI/PXIe-2532/2532B Matrix Expansion

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-hardware-diagram.html language=enus -->
## TOPIC 00450: NI PXI/PXIe-2532/2532B Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2532/2532B (NI 2532/2532B). Hardware relay names are for the native 1-wire sixteen 2×16 matrix topology. The following table lists relay names for the NI 2532/2532B. Bank 0Relays Bank 1Relays ... Bank 15Relays kB0R0C0...kB0R0C15

### NI PXI/PXIe-2532/2532B Hardware Diagram

Note

[IMAGE alt='image' src='GUID-28DE131B-4D14-4EC9-9923-F91E24D393BC-a5.gif']

The following table lists relay names for the NI 2532/2532B.

| Bank 0Relays | Bank 1Relays | ... | Bank 15Relays |
| --- | --- | --- | --- |
| kB0R0C0...kB0R0C15 | kB1R0C0...kB1R0C15 | ... | kB15R0C0...kB15R0C15 |
| kB0R1C0...kB0R1C15 | kB1R1C0...kB1R1C15 | ... | kB15R1C0...kB15R1C15 |

Parent topic:

NI PXI/PXIe-2532/2532B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-matrix-expansion.html language=enus -->
## TOPIC 00451: NI PXI/PXIe-2532/2532B Matrix Expansion

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-matrix-expansion.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-matrix-expansion.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can expand the matrices of the NI PXI/PXIe-2532/2532B (NI 2532/2532B) by increasing the number of columns in the matrix. To expand the number of columns, use the terminal block row connection headers to connect the rows on adjacent terminal blocks. The following table lists the available termina

### NI PXI/PXIe-2532/2532B Matrix Expansion

You can expand the matrices of the NI PXI/PXIe-2532/2532B (NI 2532/2532B) by increasing
 the number of columns in the matrix.

To expand the number of columns, use the terminal block row connection headers to connect
 the rows on adjacent terminal blocks. The following table lists the available terminal
 blocks and matrix configurations that support column expansion.

| Terminal Block | Configuration(Row x Column) |
| --- | --- |
| NI TB-2640/2640B | 1-wire 4×128 |
| NI TB-2641/2641B | 1-wire 8×64 |
| NI TB-2642/2642B | 1-wire 16×32 |
| NI TB-2643/2643B | 1-wire Dual 4×64 |
| NI TB-2643/2643B | 2-wire 4×64 |
| NI TB-2644/2644B | 1-wire Dual 8×32 |
| NI TB-2644/2644B | 2-wire 8×32 |
| NI TB-2645B | 1-wire Dual 16×16 |
| NI TB-2645B | 2-wire 16×16 |
| NI TB-2646B | 1- wire Quad 4×32 |
| NI TB-2646B | 2-wire Dual 4×32 |

Note

#### Column Expansion on the NI 2532/2532B

Most terminal blocks feature row connection headers that enable you to join rows on
 two adjacent terminal blocks to expand the number of columns in a matrix. These
 terminal blocks include two row connection header sets with identical pinouts. The
 NI TB-2646B includes two row connection header sets with differing pinouts. Refer to
 the NI Switches Help and the NI TB-2646B Installation
 Instructions for row connection header pinouts.

#### Terminal Blocks with Two Identical Row Connection Headers

The column expansion procedure is the same for all of the terminal block modules with
 two identical row connection headers. This includes the NI
 TB-2640/2641/2642/2643/2644 and NI TB-2640B/2641B/2642B/2643B/2644B/2645B.

Note

Complete the following steps to expand the number of columns of a matrix using a NI
 TB-2640/2641/2642/2643/2644.

1. Connect one end of the ribbon cable to either row connection header on one of
 the terminal blocks.
2. Connect the other end of the ribbon cable to either row connection header on the
 other terminal block.

The following figure illustrates how to use ribbon cables to connect rows on multiple
 NI TB-2640 modules and expand the number of columns.

[IMAGE alt='image' src='GUID-55C5D5BD-BB48-4551-AFFC-4FFD4D85A54A-a5.gif']

The same procedure is used on NI TB-2640/2641/2642/2643/2644 terminal blocks by using
 the appropriate row ribbon cable header as specified in the following table.

| Terminal Block Module | Row Connection Header 1 | Row Connection Header 2 |
| --- | --- | --- |
| NI TB-2640 | J3 | J4 |
| NI TB-2641 | J2 | J3 |
| NI TB-2642 | J2 | J3 |
| NI TB-2643 | J3 | J4 |
| NI TB-2644 | J2 | J3 |

Complete the following steps to expand the number of columns of a matrix using a NI
 TB-2640B/2641B/2642B/2643B/2644B/2645B.

1. Connect one end of the ribbon cable to either row connection header on one of
 the terminal blocks.
2. Connect the other end of the ribbon cable to either row connection header on the
 other terminal block.

The following figure illustrates how to use ribbon cables to connect rows on multiple
 NI TB-2640B modules and expand the number of columns.

[IMAGE alt='image' src='GUID-B4797CF9-6778-4F90-B84A-8415003F5B33-a5.gif']

The same procedure is used on NI TB-2640B/2641B/2642B/2643B/2644B/2645B terminal
 blocks by using the appropriate row ribbon cable header as specified in the
 following table.

| Terminal Block Module | Row Connection Header 1 | Row Connection Header 2 |
| --- | --- | --- |
| NI TB-2640B | J4 | J5 |
| NI TB-2641B | J4 | J5 |
| NI TB-2642B | J8 | J9 |
| NI TB-2643B | J4 | J5 |
| NI TB-2644B | J4 | J5 |
| NI TB-2645B | Cable 1 - J4 Cable 2 - J6 | Cable 1 - J5 Cable 2 - J7 |

Note

#### Terminal Blocks with a Row Connection Headers with Modified Pinout

The NI TB-2646B has a second row connection header with a modified pinout that is not
 identical to the first row connection header. Column expansion can only be achieved
 by connecting a row ribbon cable from the row connection header of one terminal
 block to the same row connection header of an adjacent terminal block. Refer to the
 NI TB-2646B Installation Instructions for row connection
 header pinouts.

Complete the following steps to expand the number of columns of a matrix using a NI
 TB-2646B.

1. Connect one end of the ribbon cable to either row connection header 1 or row
 connection header 2 on one of the NI TB-2646B terminal blocks.
2. Connect the other end of the ribbon cable to the same row connection header on
 another NI TB-2646B terminal block.

The same procedure is used on NI TB-2646B terminal blocks by using the appropriate
 row ribbon cable header as specified in the following table.

| Terminal Block Module | Row Connection Header 1 | Row Connection Header 2 |
| --- | --- | --- |
| NI TB-2646B | J4 | J9 |

Parent topic:

NI PXI/PXIe-2532/2532B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b-triggering.html language=enus -->
## TOPIC 00452: NI PXI/PXIe-2532/2532B Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2532/2532B (NI 2532/2532B) can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI 2532/2532B. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0

### NI PXI/PXIe-2532/2532B Triggering

The NI PXI/PXIe-2532/2532B (NI 2532/2532B) can recognize trigger pulse widths less than
 150 ns by disabling digital filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI 2532/2532B.

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

The following table lists valid scan advanced outputs for the NI 2532/2532B.

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

NI PXI/PXIe-2532/2532B

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-2532b.html language=enus -->
## TOPIC 00453: NI PXI/PXIe-2532/2532B

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-2532b.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-2532b.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2532 and NI PXI/PXIe-2532B (NI 2532/2532B) are 512-crosspoint, high-density matrix switch modules for the PXI or PXI Express platform. The NI 2532/2532B are designed for switching high and low voltages. In MAX, both the NI PXI-2532 and NI PXI-2532B appear as "NI PXI-2532" and both

### NI PXI/PXIe-2532/2532B

Note

Note

#### Operation Modes

The following table lists the supported topologies of the NI 2532/2532B and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 4×128 Matrix | 2532/1-Wire 4x128 Matrix(NISWITCH_TOPOLOGY_2532_1_WIRE_4X128_MATRIX) |  |  |
| 1-Wire 8×64 Matrix | 2532/1-Wire 8x64 Matrix(NISWITCH_TOPOLOGY_2532_1_WIRE_8X64_MATRIX) |  |  |
| 1-Wire 16×32 Matrix | 2532/1-Wire 16x32 Matrix(NISWITCH_TOPOLOGY_2532_1_WIRE_16X32_MATRIX) |  |  |
| 1-Wire Dual 4×64 Matrix | 2532/1-Wire Dual 4x64 Matrix(NISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_4X64_MATRIX) |  |  |
| 1-Wire Dual 8×32 Matrix | 2532/1-Wire Dual 8x32 Matrix(NISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_8X32_MATRIX) |  |  |
| 1-Wire Dual 16×16 Matrix | 2532/1-Wire Dual 16x16 Matrix(NISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_16X16_MATRIX) |  |  |
| 1-Wire Quad 4×32 Matrix | 2532/1-Wire Quad 4x32 Matrix(NISWITCH_TOPOLOGY_2532_1_WIRE_QUAD_4X32_MATRIX) |  |  |
| 1-Wire Sixteen 2×16 Matrix | 2532/1-Wire Sixteen 2x16 Matrix(NISWITCH_TOPOLOGY_2532_1_WIRE_SIXTEEN_2X16_MATRIX) |  |  |
| 2-Wire 4×64 Matrix | 2532/2-Wire 4x64 Matrix(NISWITCH_TOPOLOGY_2532_2_WIRE_4X64_MATRIX) |  |  |
| 2-Wire 8×32 Matrix | 2532/2-Wire 8x32 Matrix(NISWITCH_TOPOLOGY_2532_2_WIRE_8X32_MATRIX) |  |  |
| 2-Wire 16×16 Matrix | 2532/2-Wire 16x16 Matrix(NISWITCH_TOPOLOGY_2532_2_WIRE_16X16_MATRIX) |  |  |
| 2-Wire Dual 4×32 Matrix | 2532/2-Wire Dual 4x32 Matrix(NISWITCH_TOPOLOGY_2532_2_WIRE_DUAL_4X32_MATRIX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI/PXIe-2532/2532B 1-Wire 4×128 Matrix Topology
- NI PXI/PXIe-2532/2532B 1-Wire 8×64 Matrix Topology
- NI PXI/PXIe-2532/2532B 1-Wire 16×32 Matrix Topology
- NI PXI/PXIe-2532/2532B 1-Wire Dual 4×64 Matrix Topology
- NI PXI/PXIe-2532/2532B 1-Wire Dual 8×32 Matrix Topology
- NI PXI/PXIe-2532/2532B 1-Wire Dual 16×16 Matrix Topology
- NI PXI/PXIe-2532/2532B 1-Wire Quad 4×32 Matrix Topology
- NI PXI/PXIe-2532/2532B 1-Wire Sixteen 2×16 Matrix Topology
- NI PXI/PXIe-2532/2532B 2-Wire 4×64 Matrix Topology
- NI PXI/PXIe-2532/2532B 2-Wire 8×32 Matrix Topology
- NI PXI/PXIe-2532/2532B 2-Wire 16×16 Matrix Topology
- NI PXI/PXIe-2532/2532B 2-Wire Dual 4×32 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532-relay-replacement.html language=enus -->
## TOPIC 00454: NI PXI/PXIe-2532 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2532 uses reed relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Number Meder CRR05-1A Complete the following sets of steps to disassemble your switch module, replace a failed relay, and reassemble your switch module. Disa

### NI PXI/PXIe-2532 Relay Replacement

The NI PXI/PXIe-2532 uses reed relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| Meder | CRR05-1A |

Complete the following sets of steps to disassemble your switch module, replace a failed
 relay, and reassemble your switch module.

#### Disassemble the Switch Module

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your switch module from electrostatic discharge.
2. Locate the relay you want to replace.
  1. Determine the relay name using the
 Bank Connection Diagram for your topology.
  2. Match the relay name to its corresponding reference designator and
 locate the relay using the following figures and tables. Note The reference designator locations for the top and
 bottom mezzanine boards are identical. Relays are located on both
 sides of each mezzanine board. 
 Top-Left Notched Side of Mezzanine Boards 
 The following figure illustrates relay locations on the side of each
 mezzanine board that has a notch in the top left corner. 
 [IMAGE alt='image' src='GUID-468EF337-DB2F-4AF7-BEB8-314FD7F785FF-a5.gif'] 
 Top-Right Notched Side of Mezzanine Boards 
 The following figure illustrates relay locations on the side of each
 mezzanine board that has a notch in the top right corner. 
 [IMAGE alt='image' src='GUID-AC9736F6-1756-4976-8EF6-2EDCE42BE407-a5.gif'] 
 Table 10.Top Mezzanine Board Relay LocationsRelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorB8R0C0
 K144
 B10R0C0
 K176
 B12R0C0
 K193
 B14R0C0
 K225B8R0C1
 K143
 B10R0C1
 K175
 B12R0C1
 K194
 B14R0C1
 K226B8R0C2
 K142
 B10R0C2
 K174
 B12R0C2
 K195
 B14R0C2
 K227B8R0C3
 K141
 B10R0C3
 K173
 B12R0C3
 K196
 B14R0C3
 K228B8R0C4
 K140
 B10R0C4
 K172
 B12R0C4
 K197
 B14R0C4
 K229B8R0C5
 K139
 B10R0C5
 K171
 B12R0C5
 K198
 B14R0C5
 K230B8R0C6
 K138
 B10R0C6
 K170
 B12R0C6
 K199
 B14R0C6
 K231B8R0C7
 K137
 B10R0C7
 K169
 B12R0C7
 K200
 B14R0C7
 K232B8R0C8
 K136
 B10R0C8
 K168
 B12R0C8
 K201
 B14R0C8
 K233B8R0C9
 K135
 B10R0C9
 K167
 B12R0C9
 K202
 B14R0C9
 K234B8R0C10
 K134
 B10R0C10
 K166
 B12R0C10
 K203
 B14R0C10
 K235B8R0C11
 K133
 B10R0C11
 K165
 B12R0C11
 K204
 B14R0C11
 K236B8R0C12
 K132
 B10R0C12
 K164
 B12R0C12
 K205
 B14R0C12
 K237B8R0C13
 K131
 B10R0C13
 K163
 B12R0C13
 K206
 B14R0C13
 K238B8R0C14
 K130
 B10R0C14
 K162
 B12R0C14
 K207
 B14R0C14
 K239B8R0C15
 K129
 B10R0C15
 K161
 B12R0C15
 K208
 B14R0C15
 K240B8R1C0
 K1
 B10R1C0
 K33
 B12R1C0
 K80
 B14R1C0
 K112B8R1C1
 K2
 B10R1C1
 K34
 B12R1C1
 K79
 B14R1C1
 K111B8R1C2
 K3
 B10R1C2
 K35
 B12R1C2
 K78
 B14R1C2
 K110B8R1C3
 K4
 B10R1C3
 K36
 B12R1C3
 K77
 B14R1C3
 K109B8R1C4
 K5
 B10R1C4
 K37
 B12R1C4
 K76
 B14R1C4
 K108B8R1C5
 K6
 B10R1C5
 K38
 B12R1C5
 K75
 B14R1C5
 K107B8R1C6
 K7
 B10R1C6
 K39
 B12R1C6
 K74
 B14R1C6
 K106B8R1C7
 K8
 B10R1C7
 K40
 B12R1C7
 K73
 B14R1C7
 K105B8R1C8
 K9
 B10R1C8
 K41
 B12R1C8
 K72
 B14R1C8
 K104B8R1C9
 K10
 B10R1C9
 K42
 B12R1C9
 K71
 B14R1C9
 K103B8R1C10
 K11
 B10R1C10
 K43
 B12R1C10
 K70
 B14R1C10
 K102B8R1C11
 K12
 B10R1C11
 K44
 B12R1C11
 K69
 B14R1C11
 K101B8R1C12
 K13
 B10R1C12
 K45
 B12R1C12
 K68
 B14R1C12
 K100B8R1C13
 K14
 B10R1C13
 K46
 B12R1C13
 K67
 B14R1C13
 K99B8R1C14
 K15
 B10R1C14
 K47
 B12R1C14
 K66
 B14R1C14
 K98B8R1C15
 K16
 B10R1C15
 K48
 B12R1C15
 K65
 B14R1C15
 K97B9R0C0
 K160
 B11R0C0
 K192
 B13R0C0
 K209
 B15R0C0
 K241B9R0C1
 K159
 B11R0C1
 K191
 B13R0C1
 K210
 B15R0C1
 K242B9R0C2
 K158
 B11R0C2
 K190
 B13R0C2
 K211
 B15R0C2
 K243B9R0C3
 K157
 B11R0C3
 K189
 B13R0C3
 K212
 B15R0C3
 K244B9R0C4
 K156
 B11R0C4
 K188
 B13R0C4
 K213
 B15R0C4
 K245B9R0C5
 K155
 B11R0C5
 K187
 B13R0C5
 K214
 B15R0C5
 K246B9R0C6
 K154
 B11R0C6
 K186
 B13R0C6
 K215
 B15R0C6
 K247B9R0C7
 K153
 B11R0C7
 K185
 B13R0C7
 K216
 B15R0C7
 K248B9R0C8
 K152
 B11R0C8
 K184
 B13R0C8
 K217
 B15R0C8
 K249B9R0C9
 K151
 B11R0C9
 K183
 B13R0C9
 K218
 B15R0C9
 K250B9R0C10
 K150
 B11R0C10
 K182
 B13R0C10
 K219
 B15R0C10
 K251B9R0C11
 K149
 B11R0C11
 K181
 B13R0C11
 K220
 B15R0C11
 K252B9R0C12
 K148
 B11R0C12
 K180
 B13R0C12
 K221
 B15R0C012
 K253B9R0C13
 K147
 B11R0C13
 K179
 B13R0C13
 K222
 B15R0C13
 K254B9R0C14
 K146
 B11R0C14
 K178
 B13R0C14
 K223
 B15R0C14
 K255B9R0C15
 K145
 B11R0C15
 K177
 B13R0C15
 K224
 B15R0C15
 K256B9R1C0
 K17
 B11R1C0
 K49
 B13R1C0
 K96
 B15R1C0
 K128B9R1C1
 K18
 B11R1C1
 K50
 B13R1C1
 K95
 B15R1C1
 K127B9R1C2
 K19
 B11R1C2
 K51
 B13R1C2
 K94
 B15R1C2
 K126B9R1C3
 K20
 B11R1C3
 K52
 B13R1C3
 K93
 B15R1C3
 K125B9R1C4
 K21
 B11R1C4
 K53
 B13R1C4
 K92
 B15R1C4
 K124B9R1C5
 K22
 B11R1C5
 K54
 B13R1C5
 K91
 B15R1C5
 K123B9R1C6
 K23
 B11R1C6
 K55
 B13R1C6
 K90
 B15R1C6
 K122B9R1C7
 K24
 B11R1C7
 K56
 B13R1C7
 K89
 B15R1C7
 K121B9R1C8
 K25
 B11R1C8
 K57
 B13R1C8
 K88
 B15R1C8
 K120B9R1C9
 K26
 B11R1C9
 K58
 B13R1C9
 K87
 B15R1C9
 K119B9R1C10
 K27
 B11R1C10
 K59
 B13R1C10
 K86
 B15R1C10
 K118B9R1C11
 K28
 B11R1C11
 K60
 B13R1C11
 K85
 B15R1C11
 K117B9R1C12
 K29
 B11R1C12
 K61
 B13R1C12
 K84
 B15R1C12
 K116B9R1C13
 K30
 B11R1C13
 K62
 B13R1C13
 K83
 B15R1C13
 K115B9R1C14
 K31
 B11R1C14
 K63
 B13R1C14
 K82
 B15R1C14
 K114B9R1C15
 K32
 B11R1C15
 K64
 B13R1C15
 K81
 B15R1C15
 K113 
 Table 11.Bottom Mezzanine Board Relay LocationsRelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorB0R0C0
 K144
 B2R0C0
 K176
 B4R0C0
 K193
 B6R0C0
 K225B0R0C1
 K143
 B2R0C1
 K175
 B4R0C1
 K194
 B6R0C1
 K226B0R0C2
 K142
 B2R0C2
 K174
 B4R0C2
 K195
 B6R0C2
 K227B0R0C3
 K141
 B2R0C3
 K173
 B4R0C3
 K196
 B6R0C3
 K228B0R0C4
 K140
 B2R0C4
 K172
 B4R0C4
 K197
 B6R0C4
 K229B0R0C5
 K139
 B2R0C5
 K171
 B4R0C5
 K198
 B6R0C5
 K230B0R0C6
 K138
 B2R0C6
 K170
 B4R0C6
 K199
 B6R0C6
 K231B0R0C7
 K137
 B2R0C7
 K169
 B4R0C7
 K200
 B6R0C7
 K232B0R0C8
 K136
 B2R0C8
 K168
 B4R0C8
 K201
 B6R0C8
 K233B0R0C9
 K135
 B2R0C9
 K167
 B4R0C9
 K202
 B6R0C9
 K234B0R0C10
 K134
 B2R0C10
 K166
 B4R0C10
 K203
 B6R0C10
 K235B0R0C11
 K133
 B2R0C11
 K165
 B4R0C11
 K204
 B6R0C11
 K236B0R0C12
 K132
 B2R0C12
 K164
 B4R0C12
 K205
 B6R0C12
 K237B0R0C13
 K131
 B2R0C13
 K163
 B4R0C13
 K206
 B6R0C13
 K238B0R0C14
 K130
 B2R0C14
 K162
 B4R0C14
 K207
 B6R0C14
 K239B0R0C15
 K129
 B2R0C15
 K161
 B4R0C15
 K208
 B6R0C15
 K240B0R1C0
 K1
 B2R1C0
 K33
 B4R1C0
 K80
 B6R1C0
 K112B0R1C1
 K2
 B2R1C1
 K34
 B4R1C1
 K79
 B6R1C1
 K111B0R1C2
 K3
 B2R1C2
 K35
 B4R1C2
 K78
 B6R1C3
 K110B0R1C3
 K4
 B2R1C3
 K36
 B4R1C3
 K77
 B6R1C3
 K109B0R1C4
 K5
 B2R1C4
 K37
 B4R1C4
 K76
 B6R1C4
 K108B0R1C5
 K6
 B2R1C5
 K38
 B4R1C5
 K75
 B6R1C5
 K107B0R1C6
 K7
 B2R1C6
 K39
 B4R1C6
 K74
 B6R1C6
 K106B0R1C7
 K8
 B2R1C7
 K40
 B4R1C7
 K73
 B6R1C7
 K105B0R1C8
 K9
 B2R1C8
 K41
 B4R1C8
 K72
 B6R1C8
 K104B0R1C9
 K10
 B2R1C9
 K42
 B4R1C9
 K71
 B6R1C9
 K103B0R1C10
 K11
 B2R1C10
 K43
 B4R1C10
 K70
 B6R1C10
 K102B0R1C11
 K12
 B2R1C11
 K44
 B4R1C11
 K69
 B6R1C11
 K101B0R1C12
 K13
 B2R1C12
 K45
 B4R1C12
 K68
 B6R1C12
 K100B0R1C13
 K14
 B2R1C13
 K46
 B4R1C13
 K67
 B6R1C13
 K99B0R1C14
 K15
 B2R1C14
 K47
 B4R1C14
 K66
 B6R1C14
 K98B0R1C15
 K16
 B2R1C15
 K48
 B4R1C15
 K65
 B6R1C15
 K97B1R0C0
 K160
 B3R0C0
 K192
 B5R0C0
 K209
 B7R0C0
 K241B1R0C1
 K159
 B3R0C1
 K191
 B5R0C1
 K210
 B7R0C1
 K242B1R0C2
 K158
 B3R0C2
 K190
 B5R0C2
 K211
 B7R0C2
 K243B1R0C3
 K157
 B3R0C3
 K189
 B5R0C3
 K212
 B7R0C3
 K244B1R0C4
 K156
 B3R0C4
 K188
 B5R0C4
 K213
 B7R0C4
 K245B1R0C5
 K155
 B3R0C5
 K187
 B5R0C5
 K214
 B7R0C5
 K246B1R0C6
 K154
 B3R0C6
 K186
 B5R0C6
 K215
 B7R0C6
 K247B1R0C7
 K153
 B3R0C7
 K185
 B5R0C7
 K216
 B7R0C7
 K248B1R0C8
 K152
 B3R0C8
 K184
 B5R0C8
 K217
 B7R0C8
 K249B1R0C9
 K151
 B3R0C9
 K183
 B5R0C9
 K218
 B7R0C9
 K250B1R0C10
 K150
 B3R0C10
 K182
 B5R0C10
 K219
 B7R0C10
 K251B1R0C11
 K149
 B3R0C11
 K181
 B5R0C11
 K220
 B7R0C11
 K252B1R0C12
 K148
 B3R0C12
 K180
 B5R0C12
 K221
 B7R0C12
 K253B1R0C13
 K147
 B3R0C13
 K179
 B5R0C13
 K222
 B7R0C13
 K254B1R0C14
 K146
 B3R0C14
 K178
 B5R0C14
 K223
 B7R0C14
 K255B1R0C15
 K145
 B3R0C15
 K177
 B5R0C15
 K224
 B7R0C15
 K256B1R1C0
 K17
 B3R1C0
 K49
 B5R1C0
 K96
 B7R1C0
 K128B1R1C1
 K18
 B3R1C1
 K50
 B5R1C1
 K95
 B7R1C1
 K127B1R1C2
 K19
 B3R1C2
 K51
 B5R1C2
 K94
 B7R1C2
 K126B1R1C3
 K20
 B3R1C3
 K52
 B5R1C3
 K93
 B7R1C3
 K125B1R1C4
 K21
 B3R1C4
 K53
 B5R1C4
 K92
 B7R1C4
 K124B1R1C5
 K22
 B3R1C5
 K54
 B5R1C5
 K91
 B7R1C5
 K123B1R1C6
 K23
 B3R1C6
 K55
 B5R1C6
 K90
 B7R1C6
 K122B1R1C7
 K24
 B3R1C7
 K56
 B5R1C7
 K89
 B7R1C7
 K121B1R1C8
 K25
 B3R1C8
 K57
 B5R1C8
 K88
 B7R1C8
 K120B1R1C9
 K26
 B3R1C9
 K58
 B5R1C9
 K87
 B7R1C9
 K119B1R1C10
 K27
 B3R1C10
 K59
 B5R1C10
 K86
 B7R1C10
 K118B1R1C11
 K28
 B3R1C11
 K60
 B5R1C11
 K85
 B7R1C11
 K117B1R1C12
 K29
 B3R1C12
 K61
 B5R1C12
 K84
 B7R1C12
 K116B1R1C13
 K30
 B3R1C13
 K62
 B5R1C13
 K83
 B7R1C13
 K115B1R1C14
 K31
 B3R1C14
 K63
 B5R1C14
 K82
 B7R1C14
 K114B1R1C15
 K32
 B3R1C15
 K64
 B5R1C15
 K81
 B7R1C15
 K113
  3. Use the reference designator to locate the relay on the mezzanine board.
 Note Reference designators are printed on the
 mezzanine boards.
3. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']
4. Disassemble the module. Refer to Disconnecting the Top Mezzanine Board if the
 relay you want to replace is located on the top mezzanine board. Refer to
 Disconnecting the Bottom Mezzanine Board if the relay you want to replace is
 located on the bottom mezzanine board. Refer to both procedures if you would
 like to replace relays on both boards.

#### Disconnecting the Top Mezzanine Board

Complete the following steps to disconnect the top mezzanine board from the driver
 board.

1. Remove the top mezzanine board screws. 1
 Mezzanine Board Screws2
 Driver Board
2. Use a plastic screwdriver to gently pry the top mezzanine board from the driver
 board, prying a little at each corner for an even distribution of pressure until
 the top mezzanine board pops loose. Retain the spacers from between the boards. 
 
 1
 Top Mezzanine Board2
 Driver Board3
 Plastic Screwdriver4
 Spacer

#### Disconnecting the Bottom Mezzanine Board

Complete the following steps to disconnect the bottom mezzanine board from the driver
 board.

1. Remove the ejector handle assembly screw. 1
 Ejector Handle Screw2
 Ejector Handle Assembly
2. Remove the mezzanine board screws. 1
 Mezzanine Board Screws2
 Driver Board
3. Disconnect the PCB interconnect cable by lifting the PCB cable latch on the J2
 connector. 1
 J2 Connector2
 PCB Interconnect Cable3
 PCB Cable Latch
4. Separate the daughterboard assembly from the CMI bracket. 1
 CMI Bracket2
 Daughterboard Assembly
5. Use a plastic screwdriver to gently pry the bottom mezzanine board from the
 driver board, prying a little at each corner for an even distribution of
 pressure until the bottom mezzanine board pops loose. Retain the spacers from
 between the boards. 1
 Driver Board2
 Bottom Mezzanine Board3
 Spacer4
 Plastic Screwdriver

#### Replace the Relay

Note

Caution

Caution

Make sure you have the following items:

- Hot air rework station with hot air gun set to 316 °C (600 °F) for lead solder
 rework or 371 °C (700 °F) for lead-free solder rework
- Temperature-regulated soldering iron set to 316 °C (600 °F) for lead solder
 rework or 371 °C (700 °F) for lead-free solder rework
- 63/37 Tin/Lead solder (flux core) for lead solder rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Fine tweezers

Complete the following steps to replace the relay:

1. Apply heat with the hot air gun for 30 to 45 seconds in a circular motion around
 the relay, keeping the hot air gun 0.75 to 1 inch (1.91 to 2.54 cm) above the
 daughterboard.
2. Gently lift the relay with tweezers to remove it from the PCB. If the relay does
 not lift easily, apply hot air in a circular motion around the relay two to
 three times and gently try to lift the relay again. Repeat until the solder
 reflows and the relay lifts easily.
3. Use the soldering iron to tin the leads of the new relay.
4. Use the soldering iron to create a uniform distribution of solder on the pads of
 the daughterboard PCB.
5. Use the hot air gun to heat the PCB and the relay leads.
6. Hold the new relay in place on the board with the tweezers while using the hot
 air gun to apply heat in a circular motion until the solder reflows.

#### Reassemble the Module

Refer to the following procedures to reconnect the boards that you disconnected in
 Disassemble the Switch Module.

Tip

Switch Soft Front Panel Help

#### Reconnecting the Top Mezzanine Board

Complete the following steps to reconnect the top mezzanine board to the driver
 board.

1. Align pin holes 179 and 180 on the J4 and J5 connectors of the top mezzanine
 board with pins 179 and 180 of the J3 and J4 connectors on the driver board.
 Gently fold the mezzanine board over onto the driver board as shown in the
 following figure. Leave approximately 6 mm of clearance between the mezzanine
 board and the driver board. Do not press the boards together. Note 
 Ensure the black surface mount J2 and J3 connectors on the mezzanine board
 face away from the driver board, and the notch in the corner of the
 mezzanine board faces the bottom front of the module. 
 1
 Driver Board J4 Connector2
 Driver Board J3 Connector3
 Mezzanine Board J4 Connector4
 Mezzanine Board J5 Connector
2. Replace the spacers between the driver board and top mezzanine board.
3. Secure the top mezzanine board to the driver board using the screws from step
 1.

#### Reconnecting the Bottom Mezzanine Board

Complete the following steps to reconnect the bottom mezzanine board to the driver
 board.

1. Align pin holes 179 and 180 on the J2 and J3 connectors of the bottom mezzanine
 board with pins 179 and 180 of the J5 and J6 connectors on the driver board.
 Gently fold the mezzanine board over onto the driver board as shown in the
 following figure. Leave approximately 6 mm of clearance between the mezzanine
 board and the driver board. Do not press the boards together. Note 
 Ensure the black surface mount J4 and J5 connectors on the mezzanine board
 face away from the driver board, and the notch in the corner of the
 mezzanine board faces the bottom front of the module. 
 1
 Mezzanine Board J2 Connector2
 Mezzanine Board J3 Connector3
 Driver Board J5 Connector4
 Driver Board J6 Connector
2. Connect the PCB interconnect cable to the J2 connector on the bottom mezzanine
 board.
3. Reconnect the daughterboard to the CMI bracket.
4. Replace the spacers between the driver board and bottom mezzanine board.
5. Secure the daughterboard assembly to the CMI bracket using the screws from step
 2.
6. Replace the ejector handle assembly screw from step 1.

Parent topic:

NI PXI/PXIe-2532/2532B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2532b-relay-replacement.html language=enus -->
## TOPIC 00455: NI PXI/PXIe-2532B Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2532b-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2532b-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2532B uses reed relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Number Meder CRR05-1A Complete the following sets of steps to disassemble your switch module, replace a failed relay, and reassemble your switch module. Dis

### NI PXI/PXIe-2532B Relay Replacement

The NI PXI/PXIe-2532B uses reed relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| Meder | CRR05-1A |

Complete the following sets of steps to disassemble your switch module, replace a failed
 relay, and reassemble your switch module.

#### Disassemble the Switch Module

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your switch module from electrostatic discharge.
2. Locate the relay you want to replace.
  1. Determine the relay name using the
 Bank Connection Diagram for your topology.
  2. Match the relay name to its corresponding reference designator and
 locate the relay using the following figures and tables. Note The reference designator locations for the top and
 bottom mezzanine boards are identical. Relays are located on both
 sides of each mezzanine board. 
 Top-Left Notched Side of Mezzanine Boards 
 The following figure illustrates relay locations on the side of each
 mezzanine board that has notch in the top left corner. 
 1
 Left Notch 
 Top-Right Notched Side of Mezzanine Boards 
 The following figure illustrates relay locations on the side of each
 mezzanine board that has a notch in the top right corner. 
 1
 Right Notch 
 Table 12.Top Mezzanine Board Relay LocationsRelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorB8R0C0
 K144
 B10R0C0
 K176
 B12R0C0
 K193
 B14R0C0
 K225B8R0C1
 K143
 B10R0C1
 K175
 B12R0C1
 K194
 B14R0C1
 K226B8R0C2
 K142
 B10R0C2
 K174
 B12R0C2
 K195
 B14R0C2
 K227B8R0C3
 K141
 B10R0C3
 K173
 B12R0C3
 K196
 B14R0C3
 K228B8R0C4
 K140
 B10R0C4
 K172
 B12R0C4
 K197
 B14R0C4
 K229B8R0C5
 K139
 B10R0C5
 K171
 B12R0C5
 K198
 B14R0C5
 K230B8R0C6
 K138
 B10R0C6
 K170
 B12R0C6
 K199
 B14R0C6
 K231B8R0C7
 K137
 B10R0C7
 K169
 B12R0C7
 K200
 B14R0C7
 K232B8R0C8
 K136
 B10R0C8
 K168
 B12R0C8
 K201
 B14R0C8
 K233B8R0C9
 K135
 B10R0C9
 K167
 B12R0C9
 K202
 B14R0C9
 K234B8R0C10
 K134
 B10R0C10
 K166
 B12R0C10
 K203
 B14R0C10
 K235B8R0C11
 K133
 B10R0C11
 K165
 B12R0C11
 K204
 B14R0C11
 K236B8R0C12
 K132
 B10R0C12
 K164
 B12R0C12
 K205
 B14R0C12
 K237B8R0C13
 K131
 B10R0C13
 K163
 B12R0C13
 K206
 B14R0C13
 K238B8R0C14
 K130
 B10R0C14
 K162
 B12R0C14
 K207
 B14R0C14
 K239B8R0C15
 K129
 B10R0C15
 K161
 B12R0C15
 K208
 B14R0C15
 K240B8R1C0
 K1
 B10R1C0
 K33
 B12R1C0
 K80
 B14R1C0
 K112B8R1C1
 K2
 B10R1C1
 K34
 B12R1C1
 K79
 B14R1C1
 K111B8R1C2
 K3
 B10R1C2
 K35
 B12R1C2
 K78
 B14R1C2
 K110B8R1C3
 K4
 B10R1C3
 K36
 B12R1C3
 K77
 B14R1C3
 K109B8R1C4
 K5
 B10R1C4
 K37
 B12R1C4
 K76
 B14R1C4
 K108B8R1C5
 K6
 B10R1C5
 K38
 B12R1C5
 K75
 B14R1C5
 K107B8R1C6
 K7
 B10R1C6
 K39
 B12R1C6
 K74
 B14R1C6
 K106B8R1C7
 K8
 B10R1C7
 K40
 B12R1C7
 K73
 B14R1C7
 K105B8R1C8
 K9
 B10R1C8
 K41
 B12R1C8
 K72
 B14R1C8
 K104B8R1C9
 K10
 B10R1C9
 K42
 B12R1C9
 K71
 B14R1C9
 K103B8R1C10
 K11
 B10R1C10
 K43
 B12R1C10
 K70
 B14R1C10
 K102B8R1C11
 K12
 B10R1C11
 K44
 B12R1C11
 K69
 B14R1C11
 K101B8R1C12
 K13
 B10R1C12
 K45
 B12R1C12
 K68
 B14R1C12
 K100B8R1C13
 K14
 B10R1C13
 K46
 B12R1C13
 K67
 B14R1C13
 K99B8R1C14
 K15
 B10R1C14
 K47
 B12R1C14
 K66
 B14R1C14
 K98B8R1C15
 K16
 B10R1C15
 K48
 B12R1C15
 K65
 B14R1C15
 K97B9R0C0
 K160
 B11R0C0
 K192
 B13R0C0
 K209
 B15R0C0
 K241B9R0C1
 K159
 B11R0C1
 K191
 B13R0C1
 K210
 B15R0C1
 K242B9R0C2
 K158
 B11R0C2
 K190
 B13R0C2
 K211
 B15R0C2
 K243B9R0C3
 K157
 B11R0C3
 K189
 B13R0C3
 K212
 B15R0C3
 K244B9R0C4
 K156
 B11R0C4
 K188
 B13R0C4
 K213
 B15R0C4
 K245B9R0C5
 K155
 B11R0C5
 K187
 B13R0C5
 K214
 B15R0C5
 K246B9R0C6
 K154
 B11R0C6
 K186
 B13R0C6
 K215
 B15R0C6
 K247B9R0C7
 K153
 B11R0C7
 K185
 B13R0C7
 K216
 B15R0C7
 K248B9R0C8
 K152
 B11R0C8
 K184
 B13R0C8
 K217
 B15R0C8
 K249B9R0C9
 K151
 B11R0C9
 K183
 B13R0C9
 K218
 B15R0C9
 K250B9R0C10
 K150
 B11R0C10
 K182
 B13R0C10
 K219
 B15R0C10
 K251B9R0C11
 K149
 B11R0C11
 K181
 B13R0C11
 K220
 B15R0C11
 K252B9R0C12
 K148
 B11R0C12
 K180
 B13R0C12
 K221
 B15R0C012
 K253B9R0C13
 K147
 B11R0C13
 K179
 B13R0C13
 K222
 B15R0C13
 K254B9R0C14
 K146
 B11R0C14
 K178
 B13R0C14
 K223
 B15R0C14
 K255B9R0C15
 K145
 B11R0C15
 K177
 B13R0C15
 K224
 B15R0C15
 K256B9R1C0
 K17
 B11R1C0
 K49
 B13R1C0
 K96
 B15R1C0
 K128B9R1C1
 K18
 B11R1C1
 K50
 B13R1C1
 K95
 B15R1C1
 K127B9R1C2
 K19
 B11R1C2
 K51
 B13R1C2
 K94
 B15R1C2
 K126B9R1C3
 K20
 B11R1C3
 K52
 B13R1C3
 K93
 B15R1C3
 K125B9R1C4
 K21
 B11R1C4
 K53
 B13R1C4
 K92
 B15R1C4
 K124B9R1C5
 K22
 B11R1C5
 K54
 B13R1C5
 K91
 B15R1C5
 K123B9R1C6
 K23
 B11R1C6
 K55
 B13R1C6
 K90
 B15R1C6
 K122B9R1C7
 K24
 B11R1C7
 K56
 B13R1C7
 K89
 B15R1C7
 K121B9R1C8
 K25
 B11R1C8
 K57
 B13R1C8
 K88
 B15R1C8
 K120B9R1C9
 K26
 B11R1C9
 K58
 B13R1C9
 K87
 B15R1C9
 K119B9R1C10
 K27
 B11R1C10
 K59
 B13R1C10
 K86
 B15R1C10
 K118B9R1C11
 K28
 B11R1C11
 K60
 B13R1C11
 K85
 B15R1C11
 K117B9R1C12
 K29
 B11R1C12
 K61
 B13R1C12
 K84
 B15R1C12
 K116B9R1C13
 K30
 B11R1C13
 K62
 B13R1C13
 K83
 B15R1C13
 K115B9R1C14
 K31
 B11R1C14
 K63
 B13R1C14
 K82
 B15R1C14
 K114B9R1C15
 K32
 B11R1C15
 K64
 B13R1C15
 K81
 B15R1C15
 K113 
 Table 13.Bottom Mezzanine Board Relay LocationsRelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignator
 RelayName
 ReferenceDesignatorB0R0C0
 K144
 B2R0C0
 K176
 B4R0C0
 K193
 B6R0C0
 K225B0R0C1
 K143
 B2R0C1
 K175
 B4R0C1
 K194
 B6R0C1
 K226B0R0C2
 K142
 B2R0C2
 K174
 B4R0C2
 K195
 B6R0C2
 K227B0R0C3
 K141
 B2R0C3
 K173
 B4R0C3
 K196
 B6R0C3
 K228B0R0C4
 K140
 B2R0C4
 K172
 B4R0C4
 K197
 B6R0C4
 K229B0R0C5
 K139
 B2R0C5
 K171
 B4R0C5
 K198
 B6R0C5
 K230B0R0C6
 K138
 B2R0C6
 K170
 B4R0C6
 K199
 B6R0C6
 K231B0R0C7
 K137
 B2R0C7
 K169
 B4R0C7
 K200
 B6R0C7
 K232B0R0C8
 K136
 B2R0C8
 K168
 B4R0C8
 K201
 B6R0C8
 K233B0R0C9
 K135
 B2R0C9
 K167
 B4R0C9
 K202
 B6R0C9
 K234B0R0C10
 K134
 B2R0C10
 K166
 B4R0C10
 K203
 B6R0C10
 K235B0R0C11
 K133
 B2R0C11
 K165
 B4R0C11
 K204
 B6R0C11
 K236B0R0C12
 K132
 B2R0C12
 K164
 B4R0C12
 K205
 B6R0C12
 K237B0R0C13
 K131
 B2R0C13
 K163
 B4R0C13
 K206
 B6R0C13
 K238B0R0C14
 K130
 B2R0C14
 K162
 B4R0C14
 K207
 B6R0C14
 K239B0R0C15
 K129
 B2R0C15
 K161
 B4R0C15
 K208
 B6R0C15
 K240B0R1C0
 K1
 B2R1C0
 K33
 B4R1C0
 K80
 B6R1C0
 K112B0R1C1
 K2
 B2R1C1
 K34
 B4R1C1
 K79
 B6R1C1
 K111B0R1C2
 K3
 B2R1C2
 K35
 B4R1C2
 K78
 B6R1C3
 K110B0R1C3
 K4
 B2R1C3
 K36
 B4R1C3
 K77
 B6R1C3
 K109B0R1C4
 K5
 B2R1C4
 K37
 B4R1C4
 K76
 B6R1C4
 K108B0R1C5
 K6
 B2R1C5
 K38
 B4R1C5
 K75
 B6R1C5
 K107B0R1C6
 K7
 B2R1C6
 K39
 B4R1C6
 K74
 B6R1C6
 K106B0R1C7
 K8
 B2R1C7
 K40
 B4R1C7
 K73
 B6R1C7
 K105B0R1C8
 K9
 B2R1C8
 K41
 B4R1C8
 K72
 B6R1C8
 K104B0R1C9
 K10
 B2R1C9
 K42
 B4R1C9
 K71
 B6R1C9
 K103B0R1C10
 K11
 B2R1C10
 K43
 B4R1C10
 K70
 B6R1C10
 K102B0R1C11
 K12
 B2R1C11
 K44
 B4R1C11
 K69
 B6R1C11
 K101B0R1C12
 K13
 B2R1C12
 K45
 B4R1C12
 K68
 B6R1C12
 K100B0R1C13
 K14
 B2R1C13
 K46
 B4R1C13
 K67
 B6R1C13
 K99B0R1C14
 K15
 B2R1C14
 K47
 B4R1C14
 K66
 B6R1C14
 K98B0R1C15
 K16
 B2R1C15
 K48
 B4R1C15
 K65
 B6R1C15
 K97B1R0C0
 K160
 B3R0C0
 K192
 B5R0C0
 K209
 B7R0C0
 K241B1R0C1
 K159
 B3R0C1
 K191
 B5R0C1
 K210
 B7R0C1
 K242B1R0C2
 K158
 B3R0C2
 K190
 B5R0C2
 K211
 B7R0C2
 K243B1R0C3
 K157
 B3R0C3
 K189
 B5R0C3
 K212
 B7R0C3
 K244B1R0C4
 K156
 B3R0C4
 K188
 B5R0C4
 K213
 B7R0C4
 K245B1R0C5
 K155
 B3R0C5
 K187
 B5R0C5
 K214
 B7R0C5
 K246B1R0C6
 K154
 B3R0C6
 K186
 B5R0C6
 K215
 B7R0C6
 K247B1R0C7
 K153
 B3R0C7
 K185
 B5R0C7
 K216
 B7R0C7
 K248B1R0C8
 K152
 B3R0C8
 K184
 B5R0C8
 K217
 B7R0C8
 K249B1R0C9
 K151
 B3R0C9
 K183
 B5R0C9
 K218
 B7R0C9
 K250B1R0C10
 K150
 B3R0C10
 K182
 B5R0C10
 K219
 B7R0C10
 K251B1R0C11
 K149
 B3R0C11
 K181
 B5R0C11
 K220
 B7R0C11
 K252B1R0C12
 K148
 B3R0C12
 K180
 B5R0C12
 K221
 B7R0C12
 K253B1R0C13
 K147
 B3R0C13
 K179
 B5R0C13
 K222
 B7R0C13
 K254B1R0C14
 K146
 B3R0C14
 K178
 B5R0C14
 K223
 B7R0C14
 K255B1R0C15
 K145
 B3R0C15
 K177
 B5R0C15
 K224
 B7R0C15
 K256B1R1C0
 K17
 B3R1C0
 K49
 B5R1C0
 K96
 B7R1C0
 K128B1R1C1
 K18
 B3R1C1
 K50
 B5R1C1
 K95
 B7R1C1
 K127B1R1C2
 K19
 B3R1C2
 K51
 B5R1C2
 K94
 B7R1C2
 K126B1R1C3
 K20
 B3R1C3
 K52
 B5R1C3
 K93
 B7R1C3
 K125B1R1C4
 K21
 B3R1C4
 K53
 B5R1C4
 K92
 B7R1C4
 K124B1R1C5
 K22
 B3R1C5
 K54
 B5R1C5
 K91
 B7R1C5
 K123B1R1C6
 K23
 B3R1C6
 K55
 B5R1C6
 K90
 B7R1C6
 K122B1R1C7
 K24
 B3R1C7
 K56
 B5R1C7
 K89
 B7R1C7
 K121B1R1C8
 K25
 B3R1C8
 K57
 B5R1C8
 K88
 B7R1C8
 K120B1R1C9
 K26
 B3R1C9
 K58
 B5R1C9
 K87
 B7R1C9
 K119B1R1C10
 K27
 B3R1C10
 K59
 B5R1C10
 K86
 B7R1C10
 K118B1R1C11
 K28
 B3R1C11
 K60
 B5R1C11
 K85
 B7R1C11
 K117B1R1C12
 K29
 B3R1C12
 K61
 B5R1C12
 K84
 B7R1C12
 K116B1R1C13
 K30
 B3R1C13
 K62
 B5R1C13
 K83
 B7R1C13
 K115B1R1C14
 K31
 B3R1C14
 K63
 B5R1C14
 K82
 B7R1C14
 K114B1R1C15
 K32
 B3R1C15
 K64
 B5R1C15
 K81
 B7R1C15
 K113
  3. Use the reference designator to locate the relay on the mezzanine board.
 Note Reference designators are printed on the
 mezzanine boards.
3. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']
4. Disassemble the module. Refer to Disconnecting the Top Mezzanine Board if the
 relay you want to replace is located on the top mezzanine board. Refer to
 Disconnecting the Bottom Mezzanine Board if the relay you want to replace is
 located on the bottom mezzanine board. Refer to both procedures if you would
 like to replace relays on both boards.

#### Disconnecting the Top Mezzanine Board

Complete the following steps to disconnect the top mezzanine board from the driver
 board.

1. Remove the top mezzanine board screws. 1
 Mezzanine Board Screws2
 Driver Board
2. Use a plastic screwdriver to gently pry the top mezzanine board from the driver
 board, prying a little at each corner for an even distribution of pressure until
 the top mezzanine board pops loose. Retain the spacers from between the boards.
 1
 Top Mezzanine Board2
 Driver Board3
 Plastic Screwdriver4
 Spacer

#### Disconnecting the Bottom Mezzanine Board

Complete the following steps to disconnect the bottom mezzanine board from the driver
 board.

1. Remove the mezzanine board screws. 1
 Mezzanine Board Screws2
 Driver Board
2. Disconnect the PCB interconnect cable by lifting the PCB cable latch on the J2
 connector. 1
 J2 Connector2
 PCB Interconnect Cable3
 PCB Cable Latch
3. Separate the daughterboard assembly from the CMI bracket. 1
 CMI Bracket2
 Daughterboard Assembly
4. Use a plastic screwdriver to gently pry the bottom mezzanine board from the
 driver board, prying a little at each corner for an even distribution of
 pressure until the bottom mezzanine board pops loose. Retain the spacers from
 between the boards. 1
 Driver Board2
 Bottom Mezzanine Board3
 Spacer4
 Plastic Screwdriver

#### Replace the Relay

Note

Caution

Caution

Make sure you have the following items:

- Hot air rework station with hot air gun set to 316 °C (600 °F) for lead solder
 rework or 371 °C (700 °F) for lead-free solder rework
- Temperature-regulated soldering iron set to 316 °C (600 °F) for lead solder
 rework or 371 °C (700 °F) for lead-free solder rework
- 63/37 Tin/Lead solder (flux core) for lead solder rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Fine tweezers

Complete the following steps to replace the relay:

1. Apply heat with the hot air gun for 30 to 45 seconds in a circular motion around
 the relay, keeping the hot air gun 0.75 to 1 inch (1.91 to 2.54 cm) above the
 daughterboard.
2. Gently lift the relay with tweezers to remove it from the PCB. If the relay does
 not lift easily, apply hot air in a circular motion around the relay two to
 three times and gently try to lift the relay again. Repeat until the solder
 reflows and the relay lifts easily.
3. Use the soldering iron to tin the leads of the new relay.
4. Use the soldering iron to create a uniform distribution of solder on the pads of
 the daughterboard PCB.
5. Use the hot air gun to heat the PCB and the relay leads.
6. Hold the new relay in place on the board with the tweezers while using the hot
 air gun to apply heat in a circular motion until the solder reflows.

#### Reassemble the Module

Refer to the following procedures to reconnect the boards that you disconnected in
 Disassemble the Switch Module.

Tip

Switch Soft Front Panel Help

#### Reconnecting the Top Mezzanine Board

Complete the following steps to reconnect the top mezzanine board to the driver
 board.

1. Align pin holes 179 and 180 on the J4 and J5 connectors of the top mezzanine
 board with pins 179 and 180 of the J3 and J4 connectors on the driver board.
 Gently fold the mezzanine board over onto the driver board as shown in the
 following figure. Leave approximately 6 mm of clearance between the mezzanine
 board and the driver board. Do not press the boards together. Note 
 Ensure the black surface mount J2 and J3 connectors on the mezzanine board
 face away from the driver board, and the notch in the corner of the
 mezzanine board faces the bottom front of the module. 
 1
 Driver Board J4 Connector2
 Driver Board J3 Connector3
 Mezzanine Board J4 Connector4
 Mezzanine Board J5 Connector
2. Replace the spacers between the driver board and top mezzanine board.
3. Secure the top mezzanine board to the driver board using the screws from step
 1.

#### Reconnecting the Bottom Mezzanine Board

Complete the following steps to reconnect the bottom mezzanine board to the driver
 board.

1. Align pin holes 179 and 180 on the J2 and J3 connectors of the bottom mezzanine
 board with pins 179 and 180 of the J5 and J6 connectors on the driver board.
 Gently fold the mezzanine board over onto the driver board as shown in the
 following figure. Leave approximately 6 mm of clearance between the mezzanine
 board and the driver board. Do not press the boards together. Note 
 Ensure the black surface mount J4 and J5 connectors on the mezzanine board
 face away from the driver board, and the notch in the corner of the
 mezzanine board faces the bottom front of the module. 
 1
 Mezzanine Board J2 Connector2
 Mezzanine Board J3 Connector3
 Driver Board J5 Connector4
 Driver Board J6 Connector
2. Connect the PCB interconnect cable to the J2 connector on the bottom mezzanine
 board.
3. Reconnect the daughterboard to the CMI bracket.
4. Replace the spacers between the driver board and bottom mezzanine board.
5. Secure the daughterboard assembly to the CMI bracket using the screws from step
 2.

Parent topic:

NI PXI/PXIe-2532/2532B

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2540-1-wire-8-9-matrix-topology.html language=enus -->
## TOPIC 00456: NI PXI/PXIe-2540 1-Wire 8×9 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2540-1-wire-8-9-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2540-1-wire-8-9-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2540 in the 1-wire 8×9 matrix topology. Making a Connection Both the scanning command, r2->c1;, and the immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters r2 and c1, result in the following connection: si

### NI PXI/PXIe-2540 1-Wire 8×9 Matrix Topology

The following figure represents the NI PXI/PXIe-2540 in the 1-wire 8×9 matrix topology.

[IMAGE alt='image' src='GUID-E549785C-6024-4E57-B1E0-788B83865238-a5.gif']

#### Making a Connection

Both the scanning command, r2->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r2 and c1, result in the
 following connection:

signal connected to R2 is routed to C1

Parent topic:

NI PXI/PXIe-2540

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2540-front-panel.html language=enus -->
## TOPIC 00457: NI PXI/PXIe-2540 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2540-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2540-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figures illustrate the NI PXI-2540 and NI PXIe-2540 front panels.

### NI PXI/PXIe-2540 Front Panel

The following figures illustrate the NI PXI-2540 and NI PXIe-2540 front panels.

|  |  |
| --- | --- |

Parent topic:

NI PXI/PXIe-2540

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2540-hardware-diagram.html language=enus -->
## TOPIC 00458: NI PXI/PXIe-2540 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2540-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2540-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2540 (NI 2540). The following table lists relay names and their functions for the NI 2540. Relay Name Function kr0iso...kr7iso Row Isolation Relays kr0s1...kr7s1 kr0s2...kr7s2 kr0s3...kr7s3 kr0c0...kr0c8 Crosspoint Relays kr1c0...kr

### NI PXI/PXIe-2540 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI/PXIe-2540 (NI 2540).

[IMAGE alt='image' src='GUID-E549785C-6024-4E57-B1E0-788B83865238-a5.gif']

The following table lists relay names and their functions for the NI 2540.

| Relay Name | Function |
| --- | --- |
| kr0iso...kr7iso | Row Isolation Relays |
| kr0s1...kr7s1 |  |
| kr0s2...kr7s2 |  |
| kr0s3...kr7s3 |  |
| kr0c0...kr0c8 | Crosspoint Relays |
| kr1c0...kr1c8 |  |
| kr2c0...kr2c8 |  |
| kr3c0...kr3c8 |  |
| kr4c0...kr4c8 |  |
| kr5c0...kr5c8 |  |
| kr6c0...kr6c8 |  |
| kr7c0...kr7c8 |  |
| kc0iso...kc8iso | Column Isolation Relays |
| kc0s1...kc8s1 |  |
| kc0s2...kc8s2 |  |

Parent topic:

NI PXI/PXIe-2540

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2540-triggering.html language=enus -->
## TOPIC 00459: NI PXI/PXIe-2540 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2540-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2540-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2540 (NI 2540) can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI 2540. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0

### NI PXI/PXIe-2540 Triggering

The NI PXI/PXIe-2540 (NI 2540) can recognize trigger pulse widths less than 150 ns by
 disabling digital filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI 2540.

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

The following table lists valid scan advanced outputs for the NI 2540.

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

NI PXI/PXIe-2540

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2540.html language=enus -->
## TOPIC 00460: NI PXI/PXIe-2540

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2540.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2540.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2540 (NI 2540) is an RF matrix switch module for the PXI or PXI Express platform. The NI 2540 is designed to handle RF signals up to 350 MHz. Operation Modes The following table lists the supported topology of the NI 2540 and possible operation modes. Topology Software Name Immediate

### NI PXI/PXIe-2540

The NI PXI/PXIe-2540 (NI 2540) is an RF matrix switch module for the PXI or PXI Express
 platform. The NI 2540 is designed to handle RF signals up to 350 MHz.

#### Operation Modes

The following table lists the supported topology of the NI 2540 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 8x9 Matrix | 2540/1-Wire 8x9 Matrix(NISWITCH_TOPOLOGY_2540_1_WIRE_8X9_MATRIX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Operation Modes
- NI PXI/PXIe-2540 1-Wire 8×9 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2541-1-wire-8-12-matrix-topology.html language=enus -->
## TOPIC 00461: NI PXI/PXIe-2541 1-Wire 8×12 Matrix Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2541-1-wire-8-12-matrix-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2541-1-wire-8-12-matrix-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2541 in the 1-wire 8×12 matrix topology. Making a Connection Both the scanning command, r2->c1;, and the immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters r2 and c1, result in the following connection: s

### NI PXI/PXIe-2541 1-Wire 8×12 Matrix Topology

The following figure represents the NI PXI/PXIe-2541 in the 1-wire 8×12 matrix topology.

[IMAGE alt='image' src='GUID-AD9E8952-DE06-4F6B-894D-C12FE9ABAC95-a5.gif']

#### Making a Connection

Both the scanning command, r2->c1;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters r2 and c1, result in the
 following connection:

signal connected to R2 is routed to C1

Parent topic:

NI PXI/PXIe-2541

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2541-front-panel.html language=enus -->
## TOPIC 00462: NI PXI/PXIe-2541 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2541-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2541-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figures illustrate the NI PXI-2541 and NI PXIe-2541 front panels.

### NI PXI/PXIe-2541 Front Panel

The following figures illustrate the NI PXI-2541 and NI PXIe-2541 front panels.

|  |  |
| --- | --- |

Parent topic:

NI PXI/PXIe-2541

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2541-hardware-diagram.html language=enus -->
## TOPIC 00463: NI PXI/PXIe-2541 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2541-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2541-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2541 (NI 2541). The following table lists relay names and their functions for the NI 2541. Relay Name Function kr0iso...kr7iso Row Isolation Relays kr0out...kr7out kr0s1...kr7s1 kr0s2...kr7s2 kr0s3...kr7s3 kr0s4...kr7s4 kr0c0...kr0c

### NI PXI/PXIe-2541 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI/PXIe-2541 (NI 2541).

[IMAGE alt='image' src='GUID-AD9E8952-DE06-4F6B-894D-C12FE9ABAC95-a5.gif']

The following table lists relay names and their functions for the NI 2541.

| Relay Name | Function |
| --- | --- |
| kr0iso...kr7iso | Row Isolation Relays |
| kr0out...kr7out |  |
| kr0s1...kr7s1 |  |
| kr0s2...kr7s2 |  |
| kr0s3...kr7s3 |  |
| kr0s4...kr7s4 |  |
| kr0c0...kr0c11 | Crosspoint Relays |
| kr1c0...kr1c11 |  |
| kr2c0...kr2c11 |  |
| kr3c0...kr3c11 |  |
| kr4c0...kr4c11 |  |
| kr5c0...kr5c11 |  |
| kr6c0...kr6c11 |  |
| kr7c0...kr7c11 |  |
| kc0iso...kc11iso | Column Isolation Relays |
| kc0s1...kc11s1 |  |
| kc0s2...kc11s2 |  |

Parent topic:

NI PXI/PXIe-2541

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2541-triggering.html language=enus -->
## TOPIC 00464: NI PXI/PXIe-2541 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2541-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2541-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2541 (NI 2541) can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI 2541. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0

### NI PXI/PXIe-2541 Triggering

The NI PXI/PXIe-2541 (NI 2541) can recognize trigger pulse widths less than 150 ns by
 disabling digital filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI 2541.

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

The following table lists valid scan advanced outputs for the NI 2541.

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

NI PXI/PXIe-2541

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2541.html language=enus -->
## TOPIC 00465: NI PXI/PXIe-2541

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2541.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2541.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2541 (NI 2541) is an RF matrix switch module for the PXI or PXI Express platform. The NI 2541 is designed to handle RF signals up to 300 MHz. Operation Modes The following table lists the supported topology of the NI 2541 and possible operation modes. Topology Software Name Immediate

### NI PXI/PXIe-2541

The NI PXI/PXIe-2541 (NI 2541) is an RF matrix switch module for the PXI or PXI Express
 platform. The NI 2541 is designed to handle RF signals up to 300 MHz.

#### Operation Modes

The following table lists the supported topology of the NI 2541 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 8x12 Matrix | 2541/1-Wire 8x12 Matrix(NISWITCH_TOPOLOGY_2541_1_WIRE_8X12_MATRIX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Matrix
- Operation Modes
- NI PXI/PXIe-2541 1-Wire 8×12 Matrix Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2542-front-panel.html language=enus -->
## TOPIC 00466: NI PXI/PXIe-2542 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2542-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2542-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI/PXIe-2542 front panel.

### NI PXI/PXIe-2542 Front Panel

The following figure illustrates the NI PXI/PXIe-2542 front panel.

[IMAGE alt='image' src='GUID-1D5446BB-0D05-4003-90EA-6CCBB7424337-a5.gif']

Parent topic:

NI PXI/PXIe-2542

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2542-hardware-diagram.html language=enus -->
## TOPIC 00467: NI PXI/PXIe-2542 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2542-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2542-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2542.

### NI PXI/PXIe-2542 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI/PXIe-2542.

[IMAGE alt='image' src='GUID-A1BBF5D9-23BF-4C1B-A36C-6150B12D6F69-a5.gif']

Parent topic:

NI PXI/PXIe-2542

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2542-quad-2-1-terminated-multiple.html language=enus -->
## TOPIC 00468: NI PXI/PXIe-2542 Quad 2×1 Terminated Multiplexer (Quad SP2T) Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2542-quad-2-1-terminated-multiple.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2542-quad-2-1-terminated-multiple.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2542 (NI 2542) in the quad 2×1 terminated multiplexer topology. Making a Connection Call the niSwitch Connect Channels VI or the niSwitch_Connect function to connect channels in this topology. If applicable, you must call the niSwitch Disconnect Channe

### NI PXI/PXIe-2542 Quad 2×1 Terminated Multiplexer (Quad SP2T) Topology

The following figure represents the NI PXI/PXIe-2542 (NI 2542) in the quad 2×1 terminated
 multiplexer topology.

|  |
| --- |

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

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between CH 1A and COM 1 and the other between CH 2B and
 COM 2:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch1A and com1 .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 ch1A and com1 .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch2B and com2 .

When scanning the NI 2542, a typical scan list entry might be
 ch1A->com1;. This entry routes the signal connected to CH 1A
 to COM 1.

Parent topic:

NI PXI/PXIe-2542

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2542-triggering.html language=enus -->
## TOPIC 00469: NI PXI/PXIe-2542 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2542-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2542-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI/PXIe-2542 (NI 2542). Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2

### NI PXI/PXIe-2542 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI/PXIe-2542 (NI
 2542).

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

The following table lists valid scan advanced outputs for the NI 2542.

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

NI PXI/PXIe-2542

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2542.html language=enus -->
## TOPIC 00470: NI PXI/PXIe-2542

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2542.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2542.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2542 (NI 2542) is a terminated multiplexer switch module for the PXI bus that can carry 50 Ω RF signals up to 6.6 GHz. Operation Modes The following table lists the supported topology of the NI 2542 and possible operation modes. Topology Software Name Immediate Scanning Quad 2×1 Term

### NI PXI/PXIe-2542

The NI PXI/PXIe-2542 (NI 2542) is a terminated multiplexer switch module for the PXI bus
 that can carry 50 Ω RF signals up to 6.6 GHz.

#### Operation Modes

The following table lists the supported topology of the NI 2542 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Quad 2×1 Terminated Multiplexer | 2542/Quad 2x1 Terminated Mux(NISWITCH_TOPOLOGY_2542_Quad_2X1_TERMINATED_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- RF Switching Considerations
- Topologies
- Operation Modes
- NI PXI/PXIe-2542 Quad 2×1 Terminated Multiplexer (Quad SP2T) Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2543-dual-4-1-terminated-multiple.html language=enus -->
## TOPIC 00471: NI PXI/PXIe-2543 Dual 4×1 Terminated Multiplexer (Dual SP4T) Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2543-dual-4-1-terminated-multiple.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2543-dual-4-1-terminated-multiple.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2543 in the dual 4×1 terminated multiplexer topology. Making a Connection Call the niSwitch Connect Channels VI or the niSwitch_Connect function to connect channels in this topology. If applicable, you must call the niSwitch Disconnect Channels VI or t

### NI PXI/PXIe-2543 Dual 4×1 Terminated Multiplexer (Dual SP4T) Topology

The following figure represents the NI PXI/PXIe-2543 in the dual 4×1 terminated
 multiplexer topology.

|  |
| --- |

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

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between CH 1A and COM A and the other between CH 2B and
 COM B:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch1A and comA .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 ch1A and comA .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch2B and comB .

When scanning the NI PXI/PXIe-2543, a typical scan list entry might be
 ch1A->comA;. This entry routes the signal connected to CH 1A
 to COM A.

Parent topic:

NI PXI/PXIe-2543

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2543-front-panel.html language=enus -->
## TOPIC 00472: NI PXI/PXIe-2543 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2543-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2543-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI/PXIe-2543 front panel.

### NI PXI/PXIe-2543 Front Panel

The following figure illustrates the NI PXI/PXIe-2543 front panel.

[IMAGE alt='image' src='GUID-C5EBAE0D-6E02-4D3A-B76E-A99CA0757A2B-a5.gif']

Parent topic:

NI PXI/PXIe-2543

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2543-hardware-diagram.html language=enus -->
## TOPIC 00473: NI PXI/PXIe-2543 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2543-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2543-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2543.

### NI PXI/PXIe-2543 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI/PXIe-2543.

[IMAGE alt='image' src='GUID-18477387-E81F-4055-87BA-9E4BBFAB4060-a5.gif']

Parent topic:

NI PXI/PXIe-2543

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2543-triggering.html language=enus -->
## TOPIC 00474: NI PXI/PXIe-2543 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2543-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2543-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI/PXIe-2543. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2) PXI trig

### NI PXI/PXIe-2543 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI/PXIe-2543.

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

The following table lists valid scan advanced outputs for the NI PXI/PXIe-2543.

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

NI PXI/PXIe-2543

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2543.html language=enus -->
## TOPIC 00475: NI PXI/PXIe-2543

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2543.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2543.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2543 (NI 2543) is a terminated multiplexer switch module for the PXI bus that can carry 50 Ω RF signals up to 6.6 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2543 and possible operation modes. Topology Software Name Immediate Scanning Dual 4×1

### NI PXI/PXIe-2543

The NI PXI/PXIe-2543 (NI 2543) is a terminated multiplexer switch module for the PXI bus
 that can carry 50 Ω RF signals up to 6.6 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2543 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| Dual 4×1 Terminated Multiplexer | 2543/Dual 4x1 Terminated Mux(NISWITCH_TOPOLOGY_2543_DUAL_4X1_TERMINATED_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- RF Switching Considerations
- Topologies
- Operation Modes
- NI PXI/PXIe-2543 Dual 4×1 Terminated Multiplexer (Dual SP4T) Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2544-8-1-terminated-multiplexer-d.html language=enus -->
## TOPIC 00476: NI PXI/PXIe-2544 8×1 Terminated Multiplexer (Dual SP8T) Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2544-8-1-terminated-multiplexer-d.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2544-8-1-terminated-multiplexer-d.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2544 (NI 2544) in the 8×1 terminated multiplexer topology. Making a Connection Call the niSwitch Connect Channels VI or the niSwitch_Connect function to connect channels in this topology. If applicable, you must call the niSwitch Disconnect Channels VI

### NI PXI/PXIe-2544 8×1 Terminated Multiplexer (Dual SP8T) Topology

The following figure represents the NI PXI/PXIe-2544 (NI 2544) in the 8×1 terminated
 multiplexer topology.

|  |
| --- |

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

The following sequence of tasks illustrates the VI/function calls necessary to make
 consecutive connections—one between CH 1 and COM and the other between CH 2 and
 COM:

1. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch1 and com .
2. Call the niSwitch Disconnect Channels VI or the
 niSwitch_Disconnect function with parameters
 ch1 and com .
3. Call the niSwitch Connect Channels VI or the niSwitch_Connect 
 function with parameters ch2 and com .

When scanning the NI 2544, a typical scan list entry might be
 ch1->com;. This entry routes the signal connected to CH 1 to
 COM.

Parent topic:

NI PXI/PXIe-2544

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2544-front-panel.html language=enus -->
## TOPIC 00477: NI PXI/PXIe-2544 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2544-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2544-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI/PXIe-2544 front panel.

### NI PXI/PXIe-2544 Front Panel

The following figure illustrates the NI PXI/PXIe-2544 front panel.

[IMAGE alt='image' src='GUID-0CFD728C-E0A0-41AE-9026-F58A3C334410-a5.gif']

Parent topic:

NI PXI/PXIe-2544

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2544-hardware-diagram.html language=enus -->
## TOPIC 00478: NI PXI/PXIe-2544 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2544-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2544-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2544.

### NI PXI/PXIe-2544 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI/PXIe-2544.

[IMAGE alt='image' src='GUID-F492BDB8-8EC2-4CC8-AEEB-CF661E3742DA-a5.gif']

Parent topic:

NI PXI/PXIe-2544

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2544-triggering.html language=enus -->
## TOPIC 00479: NI PXI/PXIe-2544 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2544-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2544-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: Trigger Input The following table lists valid trigger inputs for the NI PXI/PXIe-2544 (NI 2544). Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0) PXI trigger line 0 TTL1 TTL1(NISWITCH_VAL_TTL1) PXI trigger line 1 TTL2 TTL2(NISWITCH_VAL_TTL2

### NI PXI/PXIe-2544 Triggering

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI/PXIe-2544
 (NI 2544).

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

The following table lists valid scan advanced outputs for the NI 2544.

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

NI PXI/PXIe-2544

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2544.html language=enus -->
## TOPIC 00480: NI PXI/PXIe-2544

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2544.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2544.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2544 (NI 2544) is a terminated multiplexer switch module for the PXI bus that can carry 50 Ω RF signals up to 6.6 GHz. Operation Modes The following table lists the supported topology of the NI PXI-2544 and possible operation modes. Topology Software Name Immediate Scanning 8×1 Termi

### NI PXI/PXIe-2544

The NI PXI/PXIe-2544 (NI 2544) is a terminated multiplexer switch module for the PXI bus
 that can carry 50 Ω RF signals up to 6.6 GHz.

#### Operation Modes

The following table lists the supported topology of the NI PXI-2544 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 8×1 Terminated Multiplexer | 2544/8x1 Terminated Mux(NISWITCH_TOPOLOGY_2544_8X1_TERMINATED_MUX) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- RF Switching Considerations
- Topologies
- Operation Modes
- NI PXI/PXIe-2544 8×1 Terminated Multiplexer (Dual SP8T) Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2569-100-spst-topology.html language=enus -->
## TOPIC 00481: NI PXI/PXIe-2569 100-SPST Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2569-100-spst-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2569-100-spst-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2569 (NI 2569) in the 100-SPST topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to close the relay of channel 2, call niSwitch_Connect(vi, "ch2", "com2"). T

### NI PXI/PXIe-2569 100-SPST Topology

The following figure represents the NI PXI/PXIe-2569 (NI 2569) in the 100-SPST topology.

[IMAGE alt='image' src='GUID-93938E2A-2358-439C-BA75-242F37D52039-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to close the relay of channel 2, call niSwitch_Connect(vi, "ch2",
 "com2"). To open the relay of channel 2, call niSwitch_Disconnect(vi,
 "ch2", "com2").

When scanning the NI 2569, a typical scan list entry could be
 ch2->com2;. This entry closes the relay between CH2 and COM2.

#### Pinout

The following figure identifies the pins for the NI 2569 in the 100-SPST topology.

[IMAGE alt='image' src='GUID-7131335D-88E5-4163-B6D7-E0965301BEBA-a5.gif']

Parent topic:

NI PXI/PXIe-2569

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2569-50-dpst-topology.html language=enus -->
## TOPIC 00482: NI PXI/PXIe-2569 50-DPST Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2569-50-dpst-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2569-50-dpst-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2569 (NI 2569) in the 50-DPST topology. Making a Connection Both the scanning command, ch2->com2;, and the immediate operation, niSwitch Connect Channels VI or the niSwitch_Connect function with parameters ch2 and com2, result in the following connecti

### NI PXI/PXIe-2569 50-DPST Topology

The following figure represents the NI PXI/PXIe-2569 (NI 2569) in the 50-DPST topology.

[IMAGE alt='image' src='GUID-54DE1E7D-990D-48CC-8266-17E8D978A2AC-a5.gif']

#### Making a Connection

Both the scanning command, ch2->com2;, and the immediate operation,
 niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function with parameters ch2 and com2, result in the
 following connections:

signal connected to CH2W0 is routed to COM2W0

signal connected to CH2W1 is routed to COM2W1

#### Pinout

The following figure identifies the pins for the NI 2569 in the 50-DPST topology.

[IMAGE alt='image' src='GUID-B966116F-4E2F-422D-94AF-65D335B64184-a5.gif']

Parent topic:

NI PXI/PXIe-2569

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2569-hardware-diagram.html language=enus -->
## TOPIC 00483: NI PXI/PXIe-2569 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2569-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2569-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2569.

### NI PXI/PXIe-2569 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI/PXIe-2569.

[IMAGE alt='image' src='GUID-83F00484-2249-49CA-B1D2-D58B185917BB-a5.gif']

Parent topic:

NI PXI/PXIe-2569

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2569-relay-replacement.html language=enus -->
## TOPIC 00484: NI PXI/PXIe-2569 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2569-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2569-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2569 uses electromechanical armature relays. Refer to the following table for information about ordering replacement relays. Relay Manufacturer Part Number AXICOM (Tyco Electronics) IM42GR (3-1462037-1) Relay Kit Part Number National Instruments (10 relays) 779356-01 Complete the fol

### NI PXI/PXIe-2569 Relay Replacement

The NI PXI/PXIe-2569 uses electromechanical armature relays.

Refer to the following table for information about ordering replacement relays.

| Relay Manufacturer | Part Number |
| --- | --- |
| AXICOM (Tyco Electronics) | IM42GR (3-1462037-1) |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays) | 779356-01 |

Complete the following sets of steps to disassemble your module, replace a failed relay,
 and reassemble your module.

#### Disassemble the Module

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your module from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figures and table
 for relay locations. Base Board 
 [IMAGE alt='image' src='GUID-F48ECD75-FB9B-407E-96F4-F4C37C2E2417-a5.gif'] 
 Mezzanine Board 
 [IMAGE alt='image' src='GUID-935A3DCC-2358-4F8E-97D9-534AFB20A33B-a5.gif'] 
 ChannelName
 RelayName
 ChannelName
 RelayName
 Channelname
 RelayName
 ChannelName
 RelayNameCH0
 K0
 CH25
 K25
 CH50
 K50
 CH75
 K75CH1
 K1
 CH26
 K26
 CH51
 K51
 CH76
 K76CH2
 K2
 CH27
 K27
 CH52
 K52
 CH77
 K77CH3
 K3
 CH28
 K28
 CH53
 K53
 CH78
 K78Cp
 K4
 CH29
 K29
 CH54
 K54
 CH79
 K79CH5
 K5
 CH30
 K30
 CH55
 K55
 CH80
 K80CH6
 K6
 CH31
 K31
 CH56
 K56
 CH81
 K81CH7
 K7
 CH32
 K32
 CH57
 K57
 CH82
 K82CH8
 K8
 CH33
 K33
 CH58
 K58
 CH83
 K83CH9
 K9
 CH34
 K34
 CH59
 K59
 CH84
 K84CH10
 K10
 CH35
 K35
 CH60
 K60
 CH85
 K85CH11
 K11
 CH36
 K36
 CH61
 K61
 CH86
 K86CH12
 K12
 CH37
 K37
 CH62
 K62
 CH87
 K87CH13
 K13
 CH38
 K38
 CH63
 K63
 CH88
 K88CH14
 K14
 CH38
 K38
 CH64
 K64
 CH89
 K89CH15
 K15
 Cp0
 K40
 CH65
 K65
 CH90
 K90CH16
 K16
 Cp1
 K41
 CH66
 K66
 CH91
 K91CH17
 K17
 Cp2
 K42
 CH67
 K67
 CH92
 K92CH18
 K18
 Cp3
 K43
 CH68
 K68
 CH93
 K93CH19
 K19
 Cp4
 K44
 CH69
 K69
 CH94
 K94CH20
 K20
 Cp5
 K45
 CH70
 K70
 CH95
 K95CH21
 K21
 Cp6
 K46
 CH71
 K71
 CH96
 K96CH22
 K22
 Cp7
 K47
 CH72
 K72
 CH97
 K97CH23
 K23
 Cp8
 K48
 CH73
 K73
 CH98
 K98CH24
 K24
 Cp9
 K49
 CH74
 K74
 CH99
 K99
3. Remove the four screws and washers, and two lead covers (if present), that
 secure the mezzanine board to the base board. Do not remove the hex standoffs or
 the base board. Note Older versions of this module might have
 adhesive plastic lead covers that you must remove. The module retains full
 specifications even if these covers are not reinstalled. 
 1
 Screws2
 Washers3
 Lead covers (if present)4
 Hex standoff5
 Base board
4. Separate the mezzanine board from the base board.
5. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. The different label types are shown in the following figure.
 [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']

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

If you have a surface mount rework station, replace the relay as you would any other
 surface mount part. Otherwise, complete the following steps to replace the
 relay:

1. Use the soldering iron and solder wick to remove as much solder from the relay
 pads as possible. Do not leave the soldering iron on any lead for more than 5
 seconds. Note If it is necessary to reapply the soldering iron
 to the pad, allow the connection to cool completely before reapplying the
 soldering iron.
2. Apply heat to the pads one at a time, and use the pick to gently pry the relay
 pins from the pads. Make sure that the solder is molten before prying. Caution Using excessive force on a soldered pad can result in
 lifting the PCB trace and ruining the board.
3. Remove the relay.
4. Clean the pads with isopropyl alcohol and cotton swabs.
5. Place the new relay on the PCB pads and solder.
6. Remove the excess flux with isopropyl alcohol and cotton swabs. Caution Do not use flux remover to clean the
 board after relay replacement.

#### Reassemble the Module

Complete the Disassemble the Module steps in reverse order to reassemble your
 module.

Tip

Switch Soft Front Panel Help

Parent topic:

NI PXI/PXIe-2569

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2569-triggering.html language=enus -->
## TOPIC 00485: NI PXI/PXIe-2569 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2569-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2569-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: This module can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI PXI/PXIe-2569 (NI 2569). Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0

### NI PXI/PXIe-2569 Triggering

This module can recognize trigger pulse widths less than 150 ns by disabling digital
 filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI PXI/PXIe-2569
 (NI 2569).

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

The following table lists valid scan advanced outputs for the NI 2569.

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

NI PXI/PXIe-2569

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2569.html language=enus -->
## TOPIC 00486: NI PXI/PXIe-2569

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2569.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2569.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2569 (NI 2569) is a 100-channel general-purpose relay module for the PXI or PXI Express platform. The NI 2569 is composed of 100 armature latching SPST relays. For certain applications, you may need to increase the default settling time. Refer to Adding Additional Settling Time for m

### NI PXI/PXIe-2569

The NI PXI/PXIe-2569 (NI 2569) is a 100-channel general-purpose relay module for the PXI
 or PXI Express platform. The NI 2569 is composed of 100 armature latching SPST relays.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2569 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 100-SPST | 2569/100-SPST(NISWITCH_TOPOLOGY_2569_100_SPST) |  |  |
| 50-DPST | 2569/50-DPST(NISWITCH_TOPOLOGY_2569_50_DPST) |  |  |

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- General-Purpose Topologies
- Armature Relays
- Relay Forms
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI/PXIe-2569 100-SPST Topology
- NI PXI/PXIe-2569 50-DPST Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2575-1-wire-196-1-multiplexer-top.html language=enus -->
## TOPIC 00487: NI PXI/PXIe-2575 1-Wire 196×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2575-1-wire-196-1-multiplexer-top.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2575-1-wire-196-1-multiplexer-top.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2575 (NI 2575) in the 1-wire 196×1 multiplexer topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to close the relay of channel 1, call niSwitch_Connect(vi, "

### NI PXI/PXIe-2575 1-Wire 196×1 Multiplexer Topology

The following figure represents the NI PXI/PXIe-2575 (NI 2575) in the 1-wire 196×1
 multiplexer topology.

[IMAGE alt='image' src='GUID-E0094ECF-98A0-47B4-8F96-7B465F5EB7A6-a5.gif']

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to close the relay of channel 1, call niSwitch_Connect(vi, "ch1",
 "com"). To open the relay of channel 1, call niSwitch_Disconnect(vi,
 "ch1", "com").

When scanning the NI 2575, a typical scan list entry could be
 ch1->com;. This entry closes the relay between CH1 and COM.

#### Pinout

The following figure identifies the pins for the NI 2575 in the 1-wire 196×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-18C75B3C-C351-41EE-8B15-14F5411F54A2-a5.gif']

Parent topic:

NI PXI/PXIe-2575

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2575-2-wire-95-1-multiplexer-topo.html language=enus -->
## TOPIC 00488: NI PXI/PXIe-2575 2-Wire 95×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2575-2-wire-95-1-multiplexer-topo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2575-2-wire-95-1-multiplexer-topo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2575 (NI 2575) in the 2-wire 95×1 multiplexer topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to close the relay of channel 1, call niSwitch_Connect(vi, "c

### NI PXI/PXIe-2575 2-Wire 95×1 Multiplexer Topology

The following figure represents the NI PXI/PXIe-2575 (NI 2575) in the 2-wire 95×1 multiplexer
 topology.

|  |
| --- |
|  |

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to close the relay of channel 1, call niSwitch_Connect(vi, "ch1",
 "com"). To open the relay of channel 1, call niSwitch_Disconnect(vi,
 "ch1", "com").

When scanning the NI 2575, a typical scan list entry could be
 ch1->com;. This entry closes the relay between CH1 and COM.

#### Pinout

The following figure identifies the pins for the NI 2575 in the 2-wire 95×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-B2E56F0F-303C-40E2-B64E-8B0C7FD6A4F1-a5.gif']

Parent topic:

NI PXI/PXIe-2575

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2575-2-wire-98-1-multiplexer-topo.html language=enus -->
## TOPIC 00489: NI PXI/PXIe-2575 2-Wire 98×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2575-2-wire-98-1-multiplexer-topo.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2575-2-wire-98-1-multiplexer-topo.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2575 (NI 2575) in the 2-wire 98×1 multiplexer topology. Making a Connection You can control the channels using the niSwitch Connect Channels VI or the niSwitch_Connect function. For example, to close the relay of channel 1, call niSwitch_Connect(vi, "c

### NI PXI/PXIe-2575 2-Wire 98×1 Multiplexer Topology

The following figure represents the NI PXI/PXIe-2575 (NI 2575) in the 2-wire 98×1 multiplexer
 topology.

|  |
| --- |
|  |

#### Making a Connection

You can control the channels using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function.

For example, to close the relay of channel 1, call niSwitch_Connect(vi, "ch1",
 "com"). To open the relay of channel 1, call niSwitch_Disconnect(vi,
 "ch1", "com").

When scanning the NI 2575, a typical scan list entry could be
 ch1->com;. This entry closes the relay between CH1 and COM.

#### Pinout

The following figure identifies the pins for the NI 2575 in the 2-wire 98×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-0497DD21-7D9F-4FC0-A893-331C4A0CBBF7-a5.gif']

Parent topic:

NI PXI/PXIe-2575

Related concepts:

- Operation Modes
- Scan Lists

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2575-hardware-diagram.html language=enus -->
## TOPIC 00490: NI PXI/PXIe-2575 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2575-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2575-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2575 (NI 2575). The following table lists channel pairings and relay assignments for the NI 2575. 1-Wire 196×1 Channel Name 2-Wire 95×1 Channel Name 2-Wire 98×1 Channel Name Relay Number CH0 CH95 CH0 CH0 K97 CH1 CH96 CH1 CH1 K93 CH2

### NI PXI/PXIe-2575 Hardware Diagram

The following figure shows the hardware diagram for the NI PXI/PXIe-2575 (NI 2575).

[IMAGE alt='image' src='GUID-6A3BCA84-84C6-4131-AC26-9DBFEF512317-a5.gif']

The following table lists channel pairings and relay assignments for the NI 2575.

| 1-Wire 196×1 Channel Name |  | 2-Wire 95×1 Channel Name | 2-Wire 98×1 Channel Name | Relay Number |
| --- | --- | --- | --- | --- |
| CH0 | CH95 | CH0 | CH0 | K97 |
| CH1 | CH96 | CH1 | CH1 | K93 |
| CH2 | CH97 | CH2 | CH2 | K89 |
| CH3 | CH98 | CH3 | CH3 | K85 |
| CH4 | CH99 | CH4 | CH4 | K81 |
| CH5 | CH100 | CH5 | CH5 | K77 |
| CH6 | CH101 | CH6 | CH6 | K73 |
| CH7 | CH102 | CH7 | CH7 | K69 |
| CH8 | CH103 | CH8 | CH8 | K65 |
| CH9 | CH104 | CH9 | CH9 | K61 |
| CH10 | CH105 | CH10 | CH10 | K57 |
| CH11 | CH106 | CH11 | CH11 | K53 |
| CH12 | CH107 | CH12 | CH12 | K47 |
| CH13 | CH108 | CH13 | CH13 | K44 |
| CH14 | CH109 | CH14 | CH14 | K40 |
| CH15 | CH110 | CH15 | CH15 | K39 |
| CH16 | CH111 | CH16 | CH16 | K32 |
| CH17 | CH112 | CH17 | CH17 | K28 |
| CH18 | CH113 | CH18 | CH18 | K24 |
| CH19 | CH114 | CH19 | CH19 | K20 |
| CH20 | CH115 | CH20 | CH20 | K16 |
| CH21 | CH116 | CH21 | CH21 | K11 |
| CH22 | CH117 | CH22 | CH22 | K7 |
| CH23 | CH118 | CH23 | CH23 | K3 |
| CH24 | CH119 | CH24 | CH24 | K52 |
| CH25 | CH120 | CH25 | CH25 | K56 |
| CH26 | CH121 | CH26 | CH26 | K60 |
| CH27 | CH122 | CH27 | CH27 | K64 |
| CH28 | CH123 | CH28 | CH28 | K68 |
| CH29 | CH124 | CH29 | CH29 | K72 |
| CH30 | CH125 | CH30 | CH30 | K76 |
| CH31 | CH126 | CH31 | CH31 | K80 |
| CH32 | CH127 | CH32 | CH32 | K84 |
| CH33 | CH128 | CH33 | CH33 | K87 |
| CH34 | CH129 | CH34 | CH34 | K91 |
| CH35 | CH130 | CH35 | CH35 | K95 |
| CH36 | CH131 | CH36 | CH36 | K2 |
| CH37 | CH132 | CH37 | CH37 | K6 |
| CH38 | CH133 | CH38 | CH38 | K10 |
| CH39 | CH134 | CH39 | CH39 | K14 |
| CH40 | CH135 | CH40 | CH40 | K19 |
| CH41 | CH136 | CH41 | CH41 | K23 |
| CH42 | CH137 | CH42 | CH42 | K27 |
| CH43 | CH138 | CH43 | CH43 | K31 |
| CH44 | CH139 | CH44 | CH44 | K35 |
| CH45 | CH140 | CH45 | CH45 | K38 |
| CH46 | CH141 | CH46 | CH46 | K43 |
| CH47 | CH142 | CH47 | CH47 | K46 |
| CH48 | CH143 | CH48 | CH48 | K96 |
| CH49 | CH144 | CH49 | CH49 | K92 |
| CH50 | CH145 | CH50 | CH50 | K88 |
| CH51 | CH146 | CH51 | CH51 | K83 |
| CH52 | CH147 | CH52 | CH52 | K79 |
| CH53 | CH148 | CH53 | CH53 | K75 |
| CH54 | CH149 | CH54 | CH54 | K71 |
| CH55 | CH150 | CH55 | CH55 | K67 |
| CH56 | CH151 | CH56 | CH56 | K63 |
| CH57 | CH152 | CH57 | CH57 | K59 |
| CH58 | CH153 | CH58 | CH58 | K55 |
| CH59 | CH154 | CH59 | CH59 | K51 |
| CH60 | CH155 | CH60 | CH60 | K45 |
| CH61 | CH156 | CH61 | CH61 | K42 |
| CH62 | CH157 | CH62 | CH62 | K37 |
| CH63 | CH158 | CH63 | CH63 | K34 |
| CH64 | CH159 | CH64 | CH64 | K30 |
| CH65 | CH160 | CH65 | CH65 | K26 |
| CH66 | CH161 | CH66 | CH66 | K22 |
| CH67 | CH162 | CH67 | CH67 | K18 |
| CH68 | CH163 | CH68 | CH68 | K13 |
| CH69 | CH164 | CH69 | CH69 | K9 |
| CH70 | CH165 | CH70 | CH70 | K5 |
| CH71 | CH166 | CH71 | CH71 | K1 |
| CH72 | CH167 | CH72 | CH72 | K50 |
| CH73 | CH168 | CH73 | CH73 | K54 |
| CH74 | CH169 | CH74 | CH74 | K58 |
| CH75 | CH170 | CH75 | CH75 | K62 |
| CH76 | CH171 | CH76 | CH76 | K66 |
| CH77 | CH172 | CH77 | CH77 | K70 |
| CH78 | CH173 | CH78 | CH78 | K74 |
| CH79 | CH174 | CH79 | CH79 | K78 |
| CH80 | CH175 | CH80 | CH80 | K82 |
| CH81 | CH176 | CH81 | CH81 | K86 |
| CH82 | CH177 | CH82 | CH82 | K90 |
| CH83 | CH178 | CH83 | CH83 | K94 |
| CH84 | CH179 | CH84 | CH84 | K0 |
| CH85 | CH180 | CH85 | CH85 | K4 |
| CH86 | CH181 | CH86 | CH86 | K8 |
| CH87 | CH182 | CH87 | CH87 | K12 |
| CH88 | CH183 | CH88 | CH88 | K17 |
| CH89 | CH184 | CH89 | CH89 | K21 |
| CH90 | CH185 | CH90 | CH90 | K25 |
| CH91 | CH186 | CH91 | CH91 | K29 |
| CH92 | CH187 | CH92 | CH92 | K33 |
| CH93 | CH188 | CH93 | CH93 | K36 |
| CH94 | CH189 | CH94 | CH94 | K41 |
| CH190 | CH193 | — | CH95 | K48 |
| CH191 | CH194 | — | CH96 | K49 |
| CH192 | CH195 | — | CH97 | K98 |
| COM Relay |  |  |  | K15 |

Parent topic:

NI PXI/PXIe-2575

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2575-relay-replacement.html language=enus -->
## TOPIC 00491: NI PXI/PXIe-2575 Relay Replacement

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2575-relay-replacement.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2575-relay-replacement.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2575 uses electromechanical armature relays. Refer to the following tables for information about ordering replacement relays. Use relays of the same brand that you are replacing. Relay Manufacturer Part Number OMRON G6KU-2F-Y Tyco 5-1462039-7 Relay Kit Part Number National Instrument

### NI PXI/PXIe-2575 Relay Replacement

The NI PXI/PXIe-2575 uses electromechanical armature relays.

Refer to the following tables for information about ordering replacement relays. Use
 relays of the same brand that you are replacing.

| Relay Manufacturer | Part Number |
| --- | --- |
| OMRON | G6KU-2F-Y |
| Tyco | 5-1462039-7 |

| Relay Kit | Part Number |
| --- | --- |
| National Instruments (10 relays, OMRON) | 780386-01 |
| National Instruments (10 relays, Tyco) | 782051-01 |

Complete the following sets of steps to disassemble your module, replace a failed relay,
 and reassemble your module.

#### Disassemble the Module

1. Ground yourself using a grounding strap or a ground connected to your PXI
 chassis. Note Properly grounding yourself prevents damage to
 your module from electrostatic discharge.
2. Locate the relay you want to replace. Refer to the following figures and table
 for relay locations. Base Board 191700D and Earlier 
 [IMAGE alt='image' src='GUID-F48ECD75-FB9B-407E-96F4-F4C37C2E2417-a5.gif'] 
 Base Board 151664A and Later (PXI-2575 only) 
 [IMAGE alt='image' src='GUID-BAC6455B-3E00-46A8-A450-8F68A3D3AF15-a5.gif'] 
 Mezzanine Board 
 [IMAGE alt='image' src='GUID-935A3DCC-2358-4F8E-97D9-534AFB20A33B-a5.gif'] 
 1-Wire 196×1 Channel
 Name
 2-Wire 95×1 Channel Name
 2-Wire 98×1 Channel Name
 Software Relay Name
 Reference Designator (Base Board 191700D
 and earlier)
 Reference Designator (Base Board 151664A and later) (PXI-2575 only)CH0
 CH95
 CH0
 CH0
 k97
 K97 (mezzanine)
 K97 (mezzanine)
 CH1
 CH96
 CH1
 CH1
 k93
 K93 (mezzanine)
 K93 (mezzanine)
 CH2
 CH97
 CH2
 CH2
 k89
 K89 (mezzanine)
 K89 (mezzanine)
 CH3
 CH98
 CH3
 CH3
 k85
 K85 (mezzanine)
 K85 (mezzanine)
 CH4
 CH99
 CH4
 CH4
 k81
 K81 (mezzanine)
 K81 (mezzanine)
 CH5
 CH100
 CH5
 CH5
 k77
 K77 (mezzanine)
 K77 (mezzanine)
 CH6
 CH101
 CH6
 CH6
 k73
 K73 (mezzanine)
 K73 (mezzanine)
 CH7
 CH102
 CH7
 CH7
 k69
 K69 (mezzanine)
 K69 (mezzanine)
 CH8
 CH103
 CH8
 CH8
 k65
 K65 (mezzanine)
 K65 (mezzanine)
 CH9
 CH104
 CH9
 CH9
 k61
 K61 (mezzanine)
 K61 (mezzanine)
 CH10
 CH105
 CH10
 CH10
 k57
 K57 (mezzanine)
 K57 (mezzanine)
 CH11
 CH106
 CH11
 CH11
 k53
 K53 (mezzanine)
 K53 (mezzanine)
 CH12
 CH107
 CH12
 CH12
 k47
 K47 (mezzanine)
 K47 (mezzanine)
 CH13
 CH108
 CH13
 CH13
 k44
 K44 (mezzanine)
 K44 (mezzanine)
 CH14
 CH109
 CH14
 CH14
 k40
 K40 (mezzanine)
 K40 (mezzanine)
 CH15
 CH110
 CH15
 CH15
 k39
 K39 (base board)
 K40 (base board)
 CH16
 CH111
 CH16
 CH16
 k32
 K32 (base board)
 K33 (base board)
 CH17
 CH112
 CH17
 CH17
 k28
 K28 (base board)
 K29 (base board)
 CH18
 CH113
 CH18
 CH18
 k24
 K24 (base board)
 K25 (base board)
 CH19
 CH114
 CH19
 CH19
 k20
 K20 (base board)
 K21 (base board)
 CH20
 CH115
 CH20
 CH20
 k16
 K16 (base board)
 K17 (base board)
 CH21
 CH116
 CH21
 CH21
 k11
 K11 (base board)
 K12 (base board)
 CH22
 CH117
 CH22
 CH22
 k7
 K7 (base board)
 K8 (base board)
 CH23
 CH118
 CH23
 CH23
 k3
 K3 (base board)
 K4 (base board)
 CH24
 CH119
 CH24
 CH24
 k52
 K52 (mezzanine)
 K52 (mezzanine)
 CH25
 CH120
 CH25
 CH25
 k56
 K56 (mezzanine)
 K56 (mezzanine)
 CH26
 CH121
 CH26
 CH26
 k60
 K60 (mezzanine)
 K60 (mezzanine)
 CH27
 CH122
 CH27
 CH27
 k64
 K64 (mezzanine)
 K64 (mezzanine)
 CH28
 CH123
 CH28
 CH28
 k68
 K68 (mezzanine)
 K68 (mezzanine)
 CH29
 CH124
 CH29
 CH29
 k72
 K72 (mezzanine)
 K72 (mezzanine)
 CH30
 CH125
 CH30
 CH30
 k76
 K76 (mezzanine)
 K76 (mezzanine)
 CH31
 CH126
 CH31
 CH31
 k80
 K80 (mezzanine)
 K80 (mezzanine)
 CH32
 CH127
 CH32
 CH32
 k84
 K84 (mezzanine)
 K84 (mezzanine)
 CH33
 CH128
 CH33
 CH33
 k87
 K87 (mezzanine)
 K87 (mezzanine)
 CH34
 CH129
 CH34
 CH34
 k91
 K91 (mezzanine)
 K91 (mezzanine)
 CH35
 CH130
 CH35
 CH35
 k95
 K95 (mezzanine)
 K95 (mezzanine)
 CH36
 CH131
 CH36
 CH36
 k2
 K2 (base board)
 K3 (base board)
 CH37
 CH132
 CH37
 CH37
 k6
 K6 (base board)
 K7 (base board)
 CH38
 CH133
 CH38
 CH38
 k10
 K10 (base board)
 K11 (base board)
 CH39
 CH134
 CH39
 CH39
 k14
 K14 (base board)
 K15 (base board)
 CH40
 CH135
 CH40
 CH40
 k19
 K19 (base board)
 K20 (base board)
 CH41
 CH136
 CH41
 CH41
 k23
 K23 (base board)
 K24 (base board)
 CH42
 CH137
 CH42
 CH42
 k27
 K27 (base board)
 K28 (base board)
 CH43
 CH138
 CH43
 CH43
 k31
 K31 (base board)
 K32 (base board)
 CH44
 CH139
 CH44
 CH44
 k35
 K35 (base board)
 K36 (base board)
 CH45
 CH140
 CH45
 CH45
 k38
 K38 (base board)
 K39 (base board)
 CH46
 CH141
 CH46
 CH46
 k43
 K43 (mezzanine)
 K43 (mezzanine)
 CH47
 CH142
 CH47
 CH47
 k46
 K46 (mezzanine)
 K46 (mezzanine)
 CH48
 CH143
 CH48
 CH48
 k96
 K96 (mezzanine)
 K96 (mezzanine)
 CH49
 CH144
 CH49
 CH49
 k92
 K92 (mezzanine)
 K92 (mezzanine)
 CH50
 CH145
 CH50
 CH50
 k88
 K88 (mezzanine)
 K88 (mezzanine)
 CH51
 CH146
 CH51
 CH51
 k83
 K83 (mezzanine)
 K83 (mezzanine)
 CH52
 CH147
 CH52
 CH52
 k79
 K79 (mezzanine)
 K79 (mezzanine)
 CH53
 CH148
 CH53
 CH53
 k75
 K75 (mezzanine)
 K75 (mezzanine)
 CH54
 CH149
 CH54
 CH54
 k71
 K71 (mezzanine)
 K71 (mezzanine)
 CH55
 CH150
 CH55
 CH55
 k67
 K67 (mezzanine)
 K67 (mezzanine)
 CH56
 CH151
 CH56
 CH56
 k63
 K63 (mezzanine)
 K63 (mezzanine)
 CH57
 CH152
 CH57
 CH57
 k59
 K59 (mezzanine)
 K59 (mezzanine)
 CH58
 CH153
 CH58
 CH58
 k55
 K55 (mezzanine)
 K55 (mezzanine)
 CH59
 CH154
 CH59
 CH59
 k51
 K51 (mezzanine)
 K51 (mezzanine)
 CH60
 CH155
 CH60
 CH60
 k45
 K45 (mezzanine)
 K45 (mezzanine)
 CH61
 CH156
 CH61
 CH61
 k42
 K42 (mezzanine)
 K42 (mezzanine)
 CH62
 CH157
 CH62
 CH62
 k37
 K37 (base board)
 K38 (base board)
 CH63
 CH158
 CH63
 CH63
 k34
 K34 (base board)
 K35 (base board)
 CH64
 CH159
 CH64
 CH64
 k30
 K30 (base board)
 K31 (base board)
 CH65
 CH160
 CH65
 CH65
 k26
 K26 (base board)
 K27 (base board)
 CH66
 CH161
 CH66
 CH66
 k22
 K22 (base board)
 K23 (base board)
 CH67
 CH162
 CH67
 CH67
 k18
 K18 (base board)
 K19 (base board)
 CH68
 CH163
 CH68
 CH68
 k13
 K13 (base board)
 K14 (base board)
 CH69
 CH164
 CH69
 CH69
 k9
 K9 (base board)
 K10 (base board)
 CH70
 CH165
 CH70
 CH70
 k5
 K5 (base board)
 K6 (base board)
 CH71
 CH166
 CH71
 CH71
 k1
 K1 (base board)
 K2 (base board)
 CH72
 CH167
 CH72
 CH72
 k50
 K50 (mezzanine)
 K50 (mezzanine)
 CH73
 CH168
 CH73
 CH73
 k54
 K54 (mezzanine)
 K54 (mezzanine)
 CH74
 CH169
 CH74
 CH74
 k58
 K58 (mezzanine)
 K58 (mezzanine)
 CH75
 CH170
 CH75
 CH75
 k62
 K62 (mezzanine)
 K62 (mezzanine)
 CH76
 CH170
 CH76
 CH76
 k66
 K66 (mezzanine)
 K66 (mezzanine)
 CH77
 CH172
 CH77
 CH77
 k70
 K70 (mezzanine)
 K70 (mezzanine)
 CH78
 CH173
 CH78
 CH78
 k74
 K74 (mezzanine)
 K74 (mezzanine)
 CH79
 CH174
 CH79
 CH79
 k78
 K78 (mezzanine)
 K78 (mezzanine)
 CH80
 CH175
 CH80
 CH80
 k82
 K82 (mezzanine)
 K82 (mezzanine)
 CH81
 CH176
 CH81
 CH81
 k86
 K86 (mezzanine)
 K86 (mezzanine)
 CH82
 CH177
 CH82
 CH82
 k90
 K90 (mezzanine)
 K90 (mezzanine)
 CH83
 CH178
 CH83
 CH83
 k94
 K94 (mezzanine)
 K94 (mezzanine)
 CH84
 CH179
 CH84
 CH84
 k0
 K0 (base board)
 K1 (base board)
 CH85
 CH180
 CH85
 CH85
 k4
 K4 (base board)
 K5 (base board)
 CH86
 CH181
 CH86
 CH86
 k8
 K8 (base board)
 K9 (base board)
 CH87
 CH182
 CH87
 CH87
 k12
 K12 (base board)
 K13 (base board)
 CH88
 CH183
 CH88
 CH88
 k17
 K17 (base board)
 K18 (base board)
 CH89
 CH184
 CH89
 CH89
 k21
 K21 (base board)
 K22 (base board)
 CH90
 CH185
 CH90
 CH90
 k25
 K25 (base board)
 K26 (base board)
 CH91
 CH186
 CH91
 CH91
 k29
 K29 (base board)
 K30 (base board)
 CH92
 CH187
 CH92
 CH92
 k33
 K33 (base board)
 K34 (base board)
 CH93
 CH188
 CH93
 CH93
 k36
 K36 (base board)
 K37 (base board)
 CH94
 CH189
 CH94
 CH94
 k41
 K41 (mezzanine)
 K41 (mezzanine)
 CH190
 CH193
 —
 CH95
 k48
 K48 (mezzanine)
 K48 (mezzanine)
 CH191
 CH194
 —
 CH96
 k49
 K49 (mezzanine)
 K49 (mezzanine)
 CH192
 CH195
 —
 CH97
 k98
 K98 (mezzanine)
 K98 (mezzanine)
 COM Relay
 k15
 K15 (base board)
 K16 (base board)
3. Remove the parts that secure the mezzanine board to the base board.
  - Disassembly of Base Board 191700D and
 Earlier —Remove the four screws and washers that secure the
 mezzanine board to the base board. Do not remove the
 hex standoffs or the base board. Note Older versions of
 this module might have adhesive plastic lead covers that you must
 remove. The module retains full specifications even if these covers
 are not reinstalled. 
 1
 Screws
 2
 Washers
 3
 Lead covers (if present)
 4
 Hex standoff
 5
 Base board
  - Disassembly of Base Board 151664A and Later (PXI-2575
 only) —Remove the four screws that secure the mezzanine
 board to the base board. Do not remove the hex
 standoffs. 1
 Screws
 2
 Mezzanine board
 3
 Hex standoff
 4
 Base board
 5
 Screws
4. Separate the mezzanine board from the base board.
5. Locate the assembly and serial number labels on the board with the relay you
 want to replace. White labels indicate the board was assembled using lead solder
 (Sn 63 Pb 37). Green labels indicate the board was assembled using lead-free
 solder (Sn 96.5 Ag 3.0 Cu 0.5). Lead-free assemblies have assembly numbers
 ending in L. [IMAGE alt='image' src='GUID-28BECD1D-452B-46FF-A81E-1B8F2C8BBBCE-a5.gif']

#### Replace the Relay

Note

Notice

Notice

- Temperature-regulated soldering iron set to 316 °C (600 °F) for lead solder
 rework or 371 °C (700 °F) for lead-free solder rework
- 63/37 Tin/Lead solder (flux core) for lead solder rework
- 96.5/3.0/0.5 Tin/Silver/Copper solder (flux core) for lead-free solder
 rework
- Solder wick
- Fine pick
- Isopropyl alcohol
- Cotton swabs

If you have a surface mount rework station, replace the relay as you would any other
 surface mount part. Otherwise, complete the following steps to replace the
 relay:

1. Use the soldering iron and solder wick to remove as much solder from the relay
 pads as possible. Do not leave the soldering iron on any lead for more than 5
 seconds. Note If
 it is necessary to reapply the soldering iron to the pad, allow the
 connection to cool completely before reapplying the soldering
 iron.
2. Apply heat to the pads one at a time, and use the pick to gently pry the relay
 pins from the pads. Make sure that the solder is molten before prying. Notice Using
 excessive force on a soldered pad can result in lifting the PCB trace and
 ruining the board.
3. Remove the relay.
4. Clean the pads with isopropyl alcohol and cotton swabs.
5. Place the new relay on the PCB pads and solder.
6. Remove the excess flux with isopropyl alcohol and cotton swabs. Notice Do not use flux
 remover to clean the board after relay replacement.

#### Reassemble the Module

Complete the *Disassemble the Module* steps in reverse order to reassemble
 your module.

Tip

Switch Soft Front Panel

Resetting a
 Relay Count

NI-SWITCH Switch Soft Front Panel User
 Manual

Parent topic:

NI PXI/PXIe-2575

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2575-triggering.html language=enus -->
## TOPIC 00492: NI PXI/PXIe-2575 Triggering

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2575-triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2575-triggering.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2575 (NI 2575) can recognize trigger pulse widths less than 150 ns by disabling digital filtering. Trigger Input The following table lists valid trigger inputs for the NI 2575. Trigger Input Software Hardware Immediate Immediate(NISWITCH_VAL_IMMEDIATE) N/A TTL0 TTL0(NISWITCH_VAL_TTL0

### NI PXI/PXIe-2575 Triggering

The NI PXI/PXIe-2575 (NI 2575) can recognize trigger pulse widths less than 150 ns by
 disabling digital filtering.

#### Trigger Input

The following table lists valid trigger inputs for the NI 2575.

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

The following table lists valid scan advanced outputs for the NI 2575.

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

NI PXI/PXIe-2575

Related concepts:

- Disabling Digital Filtering

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2575.html language=enus -->
## TOPIC 00493: NI PXI/PXIe-2575

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2575.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2575.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2575 (NI 2575) is a 196×1 multiplexer relay module for the PXI or PXI Express platform. The NI 2575 is composed of 99 DPDT relays. These relays are configured in hardware as 98 DPST relays and one DPDT relay. For certain applications, you may need to increase the default settling tim

### NI PXI/PXIe-2575

The NI PXI/PXIe-2575 (NI 2575) is a 196×1 multiplexer relay module for the PXI or PXI
 Express platform. The NI 2575 is composed of 99 DPDT relays. These relays are configured
 in hardware as 98 DPST relays and one DPDT relay.

Note

#### Operation Modes

The following table lists the supported topology of the NI 2575 and possible
 operation modes.

| Topology | Software Name | Immediate | Scanning |
| --- | --- | --- | --- |
| 1-Wire 196×1 Multiplexer | 2575/1-Wire 196x1 Mux(NISWITCH_TOPOLOGY_2575_1_WIRE_196X1_MUX) |  |  |
| 2-Wire 98×1 Multiplexer | 2575/2-Wire 98x1 Mux(NISWITCH_TOPOLOGY_2575_2_WIRE_98X1_MUX) |  |  |
| 2-Wire 95×1 Multiplexer | 2575/2-Wire 95x1 Mux(NISWITCH_TOPOLOGY_2575_2_WIRE_95X1_MUX) |  |  |

Note

#### Related Information

- Integration and System Considerations

Parent topic:

NI-SWITCH Switches

Related concepts:

- Multiplexer
- Relay Forms
- Settling Time
- Adding Additional Settling Time
- Protecting NI Switch Products when Switching Inductive Loads
- Operation Modes
- NI PXI/PXIe-2575 1-Wire 196×1 Multiplexer Topology
- NI PXI/PXIe-2575 2-Wire 98×1 Multiplexer Topology
- NI PXI/PXIe-2575 2-Wire 95×1 Multiplexer Topology
- Integration and System Considerations

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2593-16-1-multiplexer-topology.html language=enus -->
## TOPIC 00494: NI PXI/PXIe-2593 16×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2593-16-1-multiplexer-topology.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2593-16-1-multiplexer-topology.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2593 (NI 2593) 16×1 multiplexer topology. The following figure shows the reset position of the NI 2593 in the 16×1 multiplexer topology. The NI 2593 in this topology contains 16 channels connected to a common channel. These channels are referred to as

### NI PXI/PXIe-2593 16×1 Multiplexer Topology

The following figure represents the NI PXI/PXIe-2593 (NI 2593) 16×1 multiplexer topology.

|  |
| --- |
|  |

The following figure shows the reset position of the NI 2593 in the 16×1 multiplexer
 topology.

[IMAGE alt='image' src='GUID-56D5184C-5BD1-47AB-B4F3-90A92B4BF5CE-a5.gif']

The NI 2593 in this topology contains 16 channels connected to a common channel. These
 channels are referred to as ch<0..15>, and the common channel is referred to as
 com0. You can connect any channel to com0 in this topology.

#### Making a Connection

You can connect the channels of the NI 2593 using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function. For example, to connect channel 15 to common 0, call the niSwitch Connect
 Channels VI or the niSwitch_Connect function with the
 channel 1 parameter set to ch15 and the
 channel 2 parameter set to com0.

When scanning the NI 2593, a typical scan list entry could be
 ch2->com0;. This entry routes the signal from ch2 to
 com0.

Parent topic:

NI PXI/PXIe-2593

Related concepts:

- Multiplexer
- Operation Modes

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2593-3-1-multiplexers.html language=enus -->
## TOPIC 00495: NI PXI/PXIe-2593 3×1 Multiplexers

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2593-3-1-multiplexers.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2593-3-1-multiplexers.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI PXI/PXIe-2593 can be configured as a 3×1 Multiplexer. Refer to the following text, table, and figures for configuration instructions, and use the following links for module-specific implementations of this configuration. Each group of four channels (0:3, 4:7, 8:11, etc.) can be configured as

### NI PXI/PXIe-2593 3×1 Multiplexers

The NI PXI/PXIe-2593 can be configured as a 3×1 Multiplexer. Refer to the following text,
 table, and figures for configuration instructions, and use the following links for
 module-specific implementations of this configuration.

Each group of four channels (0:3, 4:7, 8:11, etc.) can be configured as independent,
 unterminated 3×1 multiplexers. Choose one channel as the "common," and route it to the
 other three channels.

For example, choosing CH0 as a 3×1 common, route CH1, CH2, and CH3 to it with the command
 options described in the following table and figure.

| Route | Connect / Disconnect Calls Connection List | Individual Relay Control |
| --- | --- | --- |
| CH0-> CH1 | CH0->A0B0, A0B0->B0B1, B0B1->A1B1, A1B1->CH1 | Close KA0, KA1 Open KB0, KB1 |
| CH0-> CH2 | CH0->A0B0, A0B0->B0B1C0, B0B1C0->C0C1, C0C1->B2B3C1, B2B3C1->A2B2, A2B2->CH2 | Close KA0, KB0, KA2, KB2Open KB1*, KB3*, KC0, KC1 |
| CH0-> CH3 | CH0->A0B0, A0B0->B0B1C0, B0B1C0->C0C1, C0C1->B2B3C1, B2B3C1->A3B3, A3B3->CH3 | Close KA0, KB0, KA3, KB3 Open KB1*, KB2* KC0, KC1 |

| *Switch unused relays away from the signal path to improve high-frequency performance. |
| --- |

Refer to the following figure for an example of a 3×1 configuration using CH0-CH3 on the
 NI PXI/PXIe-2593.

|  |
| --- |
|  |
|  |

The NI PXI/PXIe-2593 can be configured as quad 3×1 multiplexers using its 16 channels.
 The COM terminals are unused.

Parent topic:

NI PXI/PXIe-2593

Related concepts:

- Multiplexer

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2593-8-1-terminated-multiplexer-t.html language=enus -->
## TOPIC 00496: NI PXI/PXIe-2593 8×1 Terminated Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2593-8-1-terminated-multiplexer-t.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2593-8-1-terminated-multiplexer-t.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2593 (NI 2593) 8×1 terminated multiplexer topology. The following figure shows the reset position of the NI 2593 in the 8×1 terminated multiplexer topology. For proper termination, connect an external terminator, such as the NI 50 Ω MCX terminator (778

### NI PXI/PXIe-2593 8×1 Terminated Multiplexer Topology

The following figure represents the NI PXI/PXIe-2593 (NI 2593) 8×1 terminated multiplexer
 topology.

|  |
| --- |
|  |

The following figure shows the reset position of the NI 2593 in the 8×1 terminated
 multiplexer topology.

[IMAGE alt='image' src='GUID-DDC45AFA-59C1-4110-9BDE-C832B644C782-a5.gif']

For proper termination, connect an external terminator, such as the NI 50 Ω MCX
 terminator (778831-01), to every odd channel. Any input channel not connected to the COM
 is routed back to its associated termination channel.

The NI 2593 in this topology contains 8 channels connected to a common channel. These
 channels are referred to as ch<0..14>, and the common channel is referred to as
 com0. You can connect any even input channel to com0 in this topology.

#### Making a Connection

You can connect the channels of the NI 2593 using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function. For example, to connect channel 14 to common 0, call the niSwitch Connect
 Channels VI or the niSwitch_Connect function with the
 channel 1 parameter set to ch14 and the
 channel 2 parameter set to com0.

When scanning the NI 2593, a typical scan list entry could be
 ch2->com0;. This entry routes signal connected to ch2 to
 com0.

Parent topic:

NI PXI/PXIe-2593

Related concepts:

- Multiplexer
- Operation Modes

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2593-dual-4-1-terminated-multiple.html language=enus -->
## TOPIC 00497: NI PXI/PXIe-2593 Dual 4×1 Terminated Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2593-dual-4-1-terminated-multiple.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2593-dual-4-1-terminated-multiple.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2593 (NI 2593) dual 4×1 terminated multiplexer topology. The following figure shows the reset position of the NI 2593 in the dual 4×1 terminated multiplexer topology. Making a Connection For proper termination, connect an external terminator, such as t

### NI PXI/PXIe-2593 Dual 4×1 Terminated Multiplexer Topology

The following figure represents the NI PXI/PXIe-2593 (NI 2593) dual 4×1 terminated
 multiplexer topology.

|  |
| --- |
|  |

The following figure shows the reset position of the NI 2593 in the dual 4×1 terminated
 multiplexer topology.

[IMAGE alt='image' src='GUID-1621FED7-1509-41D0-AE33-C12441FF9193-a5.gif']

#### Making a Connection

For proper termination, connect an external terminator, such as the NI 50 Ω MCX
 terminator (778831-01), to every odd channel. Any input channel not connected to the
 COM is routed back to its associated termination channel.

The NI 2593 in this topology contains two banks of four input channels connected to a
 common channel. These input channels are the even channels from channel 0 to channel
 14. The two common channels are referred to as com0 and com1. You can only connect
 to the common channel that is in the same bank. The banks are organized as follows:

| Input Channels | Common Channel |
| --- | --- |
| ch0, ch2, ch4, ch6, | com0 |
| ch8, ch10, ch12, ch14 | com1 |

For example, you can connect ch6 to com0; however, you cannot connect ch6 to com1 in
 this topology.

You can connect the channels of the NI 2593 using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function. For example, to connect channel 14 to common 1, call the niSwitch Connect
 Channels VI or the niSwitch_Connect function with the
 channel 1 parameter set to ch14 and the
 channel 2 parameter set to com1.

When scanning the NI 2593, a typical scan list entry could be
 ch2->com0;. This disconnects ch2 from its termination and
 route it to com0.

Parent topic:

NI PXI/PXIe-2593

Related concepts:

- Multiplexer
- Operation Modes

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2593-dual-8-1-multiplexer-topolog.html language=enus -->
## TOPIC 00498: NI PXI/PXIe-2593 Dual 8×1 Multiplexer Topology

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2593-dual-8-1-multiplexer-topolog.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2593-dual-8-1-multiplexer-topolog.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure represents the NI PXI/PXIe-2593 (NI 2593) dual 8×1 multiplexer topology. The following figure shows the reset position of the NI 2593 in the dual 8×1 multiplexer topology. The reset position is the power-on configuration of the module. Making a Connection The NI 2593 in this top

### NI PXI/PXIe-2593 Dual 8×1 Multiplexer Topology

The following figure represents the NI PXI/PXIe-2593 (NI 2593) dual 8×1 multiplexer
 topology.

|  |
| --- |
|  |

The following figure shows the reset position of the NI 2593 in the dual 8×1 multiplexer
 topology. The reset position is the power-on configuration of the module.

[IMAGE alt='image' src='GUID-E271F39D-C278-422F-B7FE-ADAD9B2D38E1-a5.gif']

#### Making a Connection

The NI 2593 in this topology contains two banks of eight input channels connected to
 a common channel. These input channels are referred to as ch<0..15>, and the
 two common channels are referred to as com0 and com1. You can only connect to the
 common channel that is in the same bank. The banks are organized as follows:

| Input Channels | Common Channel |
| --- | --- |
| ch0, ch1, ch2, ch3, ch4, ch5, ch6, ch7 | com0 |
| ch8, ch9, ch10, ch11, ch12, ch13, ch14, ch15 | com1 |

For example, you can connect ch7 to com0; however, you cannot connect ch7 to com1 in
 this topology.

You can connect the channels of the NI 2593 using the niSwitch Connect
 Channels
 VI or the
 niSwitch_Connect
 function. For example, to connect channel 15 to common 1, call the niSwitch Connect
 Channels VI or the niSwitch_Connect function with the
 channel 1 parameter set to ch15 and the
 Channel2 parameter set to com1.

When scanning the NI 2593, a typical scan list entry could be
 ch2->com0;. This entry routes the signal from ch2 to
 com0.

Parent topic:

NI PXI/PXIe-2593

Related concepts:

- Multiplexer
- Operation Modes

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2593-front-panel.html language=enus -->
## TOPIC 00499: NI PXI/PXIe-2593 Front Panel

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2593-front-panel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2593-front-panel.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure illustrates the NI PXI/PXIe-2593 front panel.

### NI PXI/PXIe-2593 Front Panel

The following figure illustrates the NI PXI/PXIe-2593 front panel.

[IMAGE alt='image' src='GUID-1428403C-2046-4749-93A9-C78C4185BD38-a5.gif']

Parent topic:

NI PXI/PXIe-2593

<!--NI_TOPIC bundle=ni-switch path=ni-pxi-pxie-2593-hardware-diagram.html language=enus -->
## TOPIC 00500: NI PXI/PXIe-2593 Hardware Diagram

- bundle_id: `ni-switch`
- source_path: `ni-pxi-pxie-2593-hardware-diagram.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch/raw/resource/enus/ni-pxi-pxie-2593-hardware-diagram.html
- document_id: `ni-switch`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows the hardware diagram for the NI PXI/PXIe-2593. Relay names are the same for every topology.

### NI PXI/PXIe-2593 Hardware Diagram

Note

[IMAGE alt='image' src='GUID-E271F39D-C278-422F-B7FE-ADAD9B2D38E1-a5.gif']

Parent topic:

NI PXI/PXIe-2593
