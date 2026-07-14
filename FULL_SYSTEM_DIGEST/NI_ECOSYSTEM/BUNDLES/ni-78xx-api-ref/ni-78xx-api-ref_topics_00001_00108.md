# NI DOCUMENT BUNDLE: ni-78xx-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-78xx-api-ref start=1 end=108 -->
<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/configuring_dram.html language=enus -->
## TOPIC 00001: NI R Series Multifunction RIO DRAM Interface

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/configuring_dram.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/configuring_dram.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### NI R Series Multifunction RIO DRAM Interface

Several NI R Series Multifunction RIO targets contain onboard DRAM that is directly accessible from the LabVIEW FPGA VI. LabVIEW allows DRAM to be accessible as an [FPGA Memory Item](dram_mem_item.html). Refer to the specifications document for your R Series device to determine the available amount of onboard DRAM.

#### Related Topics

[Configuring DRAM with FPGA Memory Items](dram_mem_item.html)
 

[Using DRAM Effectively with NI R Series](use_dram_effectively.html)

|  | Note The following devices do not contain onboard DRAM: NI PCIe-7820R NI PCIe-7846 NI PCIe-7856 NI PXIe-7820R NI PXIe-7846R NI PXIe-7856R |
| --- | --- |

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/configuring_triggers.html language=enus -->
## TOPIC 00002: Configuring Trigger Pulses

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/configuring_triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/configuring_triggers.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### Configuring Trigger Pulses

To ensure compatibility with other NI R Series devices, configure trigger pulses on an NI PXI R Series device to last for at least two clock cycles of the clock on the receiving device. For example, if the clock on the receiving device is 80 MHz, which is a clock period of 12.5 nanoseconds, the trigger line must be constant for at least 25 nanoseconds, which is two cycles of an 80 MHz clock.

|  | Note Regardless of the clock speed, pulses on the trigger line must be constant for at least 18 nanoseconds. Refer to the PXI Specification for more information about trigger timing parameters. |
| --- | --- |

The clocks between a PXI R Series device and another PXI device might not be perfectly synchronized. If you assert a trigger line on a PXI R Series device, you cannot determine at what point in the clock period the trigger registers in the receiving flip-flop. If the trigger arrives during the setup or hold time of the receiving flip-flop, you cannot determine the state of the line for that clock period. Asserting the trigger pulse for two clock cycles ensures that at least one clock cycle on the receiving flip-flop registers as a rising edge and transfers as a trigger.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_7821r_pcie_digital_port_assignments.html language=enus -->
## TOPIC 00003: PCIe-7821R Digital Port Assignments

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_7821r_pcie_digital_port_assignments.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_7821r_pcie_digital_port_assignments.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7821R Digital Port Assignments

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with the PCIe-7821R. Use the following digital port assignments when you configure digital port functions.

| Connector | Digital Port | Digital Lines |
| --- | --- | --- |
| Connector 0 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 0 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 0 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 0 | DIOPORT 3 | 24 (LSB) through 31 |
| Connector 1 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 1 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 1 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 1 | DIOPORT 3 | 24 (LSB) through 31 |
| Connector 2 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 2 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 2 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 2 | DIOPORT 3 | 24 (LSB) through 31 |
| Connector 3 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 3 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 3 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 3 | DIOPORT 3 | 24 (LSB) through 31 |

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_7822r_digital_port_assignments.html language=enus -->
## TOPIC 00004: PXIe-7822R Digital Port Assignments

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_7822r_digital_port_assignments.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_7822r_digital_port_assignments.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7822R Digital Port Assignments

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with the PXIe-7822R. Use the following digital port assignments when you configure digital port functions.

| Connector | Digital Port | Digital Lines |
| --- | --- | --- |
| Connector 0 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 0 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 0 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 0 | DIOPORT 3 | 24 (LSB) through 31 |
| Connector 1 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 1 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 1 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 1 | DIOPORT 3 | 24 (LSB) through 31 |
| Connector 2 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 2 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 2 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 2 | DIOPORT 3 | 24 (LSB) through 31 |
| Connector 3 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 3 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 3 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 3 | DIOPORT 3 | 24 (LSB) through 31 |

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_7822r_pcie_digital_port_assignments.html language=enus -->
## TOPIC 00005: PCIe-7822R Digital Port Assignments

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_7822r_pcie_digital_port_assignments.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_7822r_pcie_digital_port_assignments.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7822R Digital Port Assignments

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with the PCIe-7822R. Use the following digital port assignments when you configure digital port functions.

| Connector | Digital Port | Digital Lines |
| --- | --- | --- |
| Connector 0 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 0 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 0 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 0 | DIOPORT 3 | 24 (LSB) through 31 |
| Connector 1 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 1 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 1 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 1 | DIOPORT 3 | 24 (LSB) through 31 |
| Connector 2 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 2 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 2 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 2 | DIOPORT 3 | 24 (LSB) through 31 |
| Connector 3 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 3 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 3 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 3 | DIOPORT 3 | 24 (LSB) through 31 |

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_782xr_pcie_rtsi.html language=enus -->
## TOPIC 00006: PCIe-782xR RTSI Pinout

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_782xr_pcie_rtsi.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_782xr_pcie_rtsi.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-782xR RTSI Pinout

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with the PCIe-782*x*R. Use the following terminal assignments when you configure RTSI bus signal functions.

[IMAGE alt='text' src='pcie-782x_rtsi.png']

#### Related Topics

[PCIe-7820R Reference](ni_pcie-7820r.html)
 
[PCIe-7821R Reference](ni_pcie-7821r.html)
 
[PCIe-7822R Reference](ni_pcie-7822r.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_7841r_digital_port_assignments.html language=enus -->
## TOPIC 00007: PCIe/PXI-7841R Digital Port Assignments

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_7841r_digital_port_assignments.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_7841r_digital_port_assignments.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe/PXI-7841R Digital Port Assignments

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with the PCIe/PXI-7841R. Use the following digital port assignments when you configure digital port functions.

| Connector | Digital Port | Digital Lines |
| --- | --- | --- |
| Connector 0 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 0 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 1 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 1 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 1 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 1 | DIOPORT 3 | 24 (LSB) through 31 |
| Connector 1 | DIOPORT 4 | 32 (LSB) through 39 |
| Connector 2 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 2 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 2 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 2 | DIOPORT 3 | 24 (LSB) through 31 |
| Connector 2 | DIOPORT 4 | 32 (LSB) through 39 |

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_7842r_digital_port_assignments.html language=enus -->
## TOPIC 00008: PCIe/PXI-7842R Digital Port Assignments

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_7842r_digital_port_assignments.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_7842r_digital_port_assignments.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe/PXI-7842R Digital Port Assignments

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with the PCIe/PXI-7842R. Use the following digital port assignments when you configure digital port functions.

| Connector | Digital Port | Digital Lines |
| --- | --- | --- |
| Connector 0 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 0 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 1 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 1 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 1 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 1 | DIOPORT 3 | 24 (LSB) through 31 |
| Connector 1 | DIOPORT 4 | 32 (LSB) through 39 |
| Connector 2 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 2 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 2 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 2 | DIOPORT 3 | 24 (LSB) through 31 |
| Connector 2 | DIOPORT 4 | 32 (LSB) through 39 |

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_7856_pcie_digital_port_assignments.html language=enus -->
## TOPIC 00009: PCIe-7856 Digital Port Assignments

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_7856_pcie_digital_port_assignments.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_7856_pcie_digital_port_assignments.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7856 Digital Port Assignments

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with the PCIe-7856. Use the following digital port assignments when you configure digital port functions.

| Connector | Digital Port | Digital Lines |
| --- | --- | --- |
| Connector 0 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 0 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 1 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 1 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 1 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 1 | DIOPORT 3 | 24 (LSB) through 31 |

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_7866_digital_port_assignments.html language=enus -->
## TOPIC 00010: PXIe-7866 Digital Port Assignments

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_7866_digital_port_assignments.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_7866_digital_port_assignments.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7866 Digital Port Assignments

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with the PXIe-7866. Use the following digital port assignments when you configure digital port functions.

| Connector | Digital Port | Digital Lines |
| --- | --- | --- |
| Connector 1 | DIOPORT 0 | 0 (LSB) through 7 |
| Connector 1 | DIOPORT 1 | 8 (LSB) through 15 |
| Connector 1 | DIOPORT 2 | 16 (LSB) through 23 |
| Connector 1 | DIOPORT 3 | 24 (LSB) through 31 |

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pci-7813r.html language=enus -->
## TOPIC 00011: PCI-7813R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pci-7813r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pci-7813r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCI-7813R Reference

R Series Reconfigurable I/O for PCI (DIO)

160 DIO lines, 3 million gate FPGA

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

|  | Note In LabVIEW 8.6.1 and earlier, some terminal names appear differently. Refer to Terminal Name Conversion for R Series Devices for a list of affected terminal names. |
| --- | --- |

| Terminal | Description |
| --- | --- |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| RTSI/RTSIx | Trigger channel x, where x is the channel number <0..6>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| RTSI/RTSI7 | RTSI oscillator channel. You can use this channel as an additional trigger channel. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pcie-7820r.html language=enus -->
## TOPIC 00012: PCIe-7820R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pcie-7820r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pcie-7820r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7820R Reference

R Series Digital I/O Module for PCI Express, 128 DIO, Kintex-7 160T FPGA

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| RTSI/RTSIx | Trigger channel x, where x is the channel number <0..6>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| RTSI/RTSI7 | RTSI oscillator channel. You can use this channel as an additional trigger channel. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html).

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pcie-7821r.html language=enus -->
## TOPIC 00013: PCIe-7821R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pcie-7821r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pcie-7821r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7821R Reference

R Series Digital I/O Module for PCI Express, 128 DIO, 512 MB DRAM, Kintex-7 160T FPGA

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| RTSI/RTSIx | Trigger channel x, where x is the channel number <0..6>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| RTSI/RTSI7 | RTSI oscillator channel. You can use this channel as an additional trigger channel. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html).

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pcie-7822r.html language=enus -->
## TOPIC 00014: PCIe-7822R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pcie-7822r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pcie-7822r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7822R Reference

R Series Digital I/O Module for PCI Express, 128 DIO, 512 MB DRAM, Kintex-7 325T FPGA

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| RTSI/RTSIx | Trigger channel x, where x is the channel number <0..6>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| RTSI/RTSI7 | RTSI oscillator channel. You can use this channel as an additional trigger channel. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html).

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pcie-7841r.html language=enus -->
## TOPIC 00015: PCIe-7841R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pcie-7841r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pcie-7841r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7841R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 96 DIO lines, LX30, 200 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

|  | Note In LabVIEW 8.6.1 and earlier, some terminal names appear differently. Refer to Terminal Name Conversion for R Series Devices for a list of affected terminal names. |
| --- | --- |

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| RTSI/RTSIx | Trigger channel x, where x is the channel number <0..6>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| RTSI/RTSI7 | RTSI oscillator channel. You can use this channel as an additional trigger channel. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA.In this format, device temperature = (Returned Device Temperature decimal value) ´ 0.25 °C. For example, a returned Device Temperature decimal value of 120 would indicate a device temperature of 30 °C. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pcie-7842r.html language=enus -->
## TOPIC 00016: PCIe-7842R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pcie-7842r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pcie-7842r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7842R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 96 DIO lines, LX50, 200 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

|  | Note In LabVIEW 8.6.1 and earlier, some terminal names appear differently. Refer to Terminal Name Conversion for R Series Devices for a list of affected terminal names. |
| --- | --- |

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| RTSI/RTSIx | Trigger channel x, where x is the channel number <0..6>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| RTSI/RTSI7 | RTSI oscillator channel. You can use this channel as an additional trigger channel. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA.In this format, device temperature = (Returned Device Temperature decimal value) ´ 0.25 °C. For example, a returned Device Temperature decimal value of 120 would indicate a device temperature of 30 °C. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pcie-7846.html language=enus -->
## TOPIC 00017: PCIe-7846 Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pcie-7846.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pcie-7846.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7846 Reference

R Series Reconfigurable I/O Module (AI, AO, DIO) for PCI Express, 8 AI, 8 AO, 48 DIO, 500 kS/s AI, Kintex-7 160T FPGA

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| RTSI/RTSIx | Trigger channel x, where x is the channel number <0..6>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| RTSI/RTSI7 | RTSI oscillator channel. You can use this channel as an additional trigger channel. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pcie-7851r.html language=enus -->
## TOPIC 00018: PCIe-7851R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pcie-7851r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pcie-7851r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7851R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 96 DIO lines, LX30, 750 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

|  | Note In LabVIEW 8.6.1 and earlier, some terminal names appear differently. Refer to Terminal Name Conversion for R Series Devices for a list of affected terminal names. |
| --- | --- |

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| RTSI/RTSIx | Trigger channel x, where x is the channel number <0..6>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| RTSI/RTSI7 | RTSI oscillator channel. You can use this channel as an additional trigger channel. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA.In this format, device temperature = (Returned Device Temperature decimal value) ´ 0.25 °C. For example, a returned Device Temperature decimal value of 120 would indicate a device temperature of 30 °C. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pcie-7852r.html language=enus -->
## TOPIC 00019: PCIe-7852R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pcie-7852r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pcie-7852r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7852R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 96 DIO lines, LX50, 750 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

|  | Note In LabVIEW 8.6.1 and earlier, some terminal names appear differently. Refer to Terminal Name Conversion for R Series Devices for a list of affected terminal names. |
| --- | --- |

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| RTSI/RTSIx | Trigger channel x, where x is the channel number <0..6>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| RTSI/RTSI7 | RTSI oscillator channel. You can use this channel as an additional trigger channel. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA.In this format, device temperature = (Returned Device Temperature decimal value) ´ 0.25 °C. For example, a returned Device Temperature decimal value of 120 would indicate a device temperature of 30 °C. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pcie-7856.html language=enus -->
## TOPIC 00020: PCIe-7856 Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pcie-7856.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pcie-7856.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7856 Reference

R Series Reconfigurable I/O Module (AI, AO, DIO) for PCI Express, 8 AI, 8 AO, 48 DIO, 1 MS/s AI, Kintex-7 160T FPGA

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| RTSI/RTSIx | Trigger channel x, where x is the channel number <0..6>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| RTSI/RTSI7 | RTSI oscillator channel. You can use this channel as an additional trigger channel. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pcie-7857.html language=enus -->
## TOPIC 00021: PCIe-7857 Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pcie-7857.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pcie-7857.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7857 Reference

R Series Reconfigurable I/O Module (AI, AO, DIO) for PCI Express, 8 AI, 8 AO, 48 DIO, 1 MS/s AI, 512 MB DRAM, Kintex-7 160T FPGA

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| RTSI/RTSIx | Trigger channel x, where x is the channel number <0..6>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| RTSI/RTSI7 | RTSI oscillator channel. You can use this channel as an additional trigger channel. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pcie-7858.html language=enus -->
## TOPIC 00022: PCIe-7858 Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pcie-7858.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pcie-7858.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7858 Reference

R Series Reconfigurable I/O Module (AI, AO, DIO) for PCI Express, 8 AI, 8 AO, 48 DIO, 1 MS/s AI, 512 MB DRAM, Kintex-7 325T FPGA

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| RTSI/RTSIx | Trigger channel x, where x is the channel number <0..6>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| RTSI/RTSI7 | RTSI oscillator channel. You can use this channel as an additional trigger channel. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxi-7841r.html language=enus -->
## TOPIC 00023: PXI-7841R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxi-7841r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxi-7841r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXI-7841R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 96 DIO lines, LX30, 200 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

|  | Note In LabVIEW 8.6.1 and earlier, some terminal names appear differently. Refer to Terminal Name Conversion for R Series Devices for a list of affected terminal names. |
| --- | --- |

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| PXI/PXI_Clk10 | 10 MHz clock in the PXI chassis that you can use to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. Note You can phase-lock the FPGA device clock to the 10 MHz clock of the PXI chassis. Select Start»All Programs»NI»RIO Device Setup to launch the RIO Device Setup utility, which you can use to synchronize the FPGA clock to the 10 MHz clock of the PXI chassis. The FPGA clock itself does not change to 10 MHz even though you synchronize it. |
|  | Note You can phase-lock the FPGA device clock to the 10 MHz clock of the PXI chassis. Select Start»All Programs»NI»RIO Device Setup to launch the RIO Device Setup utility, which you can use to synchronize the FPGA clock to the 10 MHz clock of the PXI chassis. The FPGA clock itself does not change to 10 MHz even though you synchronize it. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Caution Do not use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable to access the PXI/PXI_Star channel if the FPGA device is in Slot 2 of the PXI chassis. Writing to the PXI/PXI_Star channel when the FPGA device is in Slot 2 affects the accuracy of the 10 MHz clock and can cause the PXI system to malfunction. |
|  | Caution Do not use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable to access the PXI/PXI_Star channel if the FPGA device is in Slot 2 of the PXI chassis. Writing to the PXI/PXI_Star channel when the FPGA device is in Slot 2 affects the accuracy of the 10 MHz clock and can cause the PXI system to malfunction. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA.In this format, device temperature = (Returned Device Temperature decimal value) ´ 0.25 °C. For example, a returned Device Temperature decimal value of 120 would indicate a device temperature of 30 °C. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxi-7842r.html language=enus -->
## TOPIC 00024: PXI-7842R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxi-7842r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxi-7842r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXI-7842R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 96 DIO lines, LX50, 200 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

|  | Note In LabVIEW 8.6.1 and earlier, some terminal names appear differently. Refer to Terminal Name Conversion for R Series Devices for a list of affected terminal names. |
| --- | --- |

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| PXI/PXI_Clk10 | 10 MHz clock in the PXI chassis that you can use to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. Note You can phase-lock the FPGA device clock to the 10 MHz clock of the PXI chassis. Select Start»All Programs»NI»RIO Device Setup to launch the RIO Device Setup utility, which you can use to synchronize the FPGA clock to the 10 MHz clock of the PXI chassis. The FPGA clock itself does not change to 10 MHz even though you synchronize it. |
|  | Note You can phase-lock the FPGA device clock to the 10 MHz clock of the PXI chassis. Select Start»All Programs»NI»RIO Device Setup to launch the RIO Device Setup utility, which you can use to synchronize the FPGA clock to the 10 MHz clock of the PXI chassis. The FPGA clock itself does not change to 10 MHz even though you synchronize it. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Caution Do not use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable to access the PXI/PXI_Star channel if the FPGA device is in Slot 2 of the PXI chassis. Writing to the PXI/PXI_Star channel when the FPGA device is in Slot 2 affects the accuracy of the 10 MHz clock and can cause the PXI system to malfunction. |
|  | Caution Do not use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable to access the PXI/PXI_Star channel if the FPGA device is in Slot 2 of the PXI chassis. Writing to the PXI/PXI_Star channel when the FPGA device is in Slot 2 affects the accuracy of the 10 MHz clock and can cause the PXI system to malfunction. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA.In this format, device temperature = (Returned Device Temperature decimal value) ´ 0.25 °C. For example, a returned Device Temperature decimal value of 120 would indicate a device temperature of 30 °C. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxi-7851r.html language=enus -->
## TOPIC 00025: PXI-7851R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxi-7851r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxi-7851r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXI-7851R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 96 DIO lines, LX30, 750 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

|  | Note In LabVIEW 8.6.1 and earlier, some terminal names appear differently. Refer to Terminal Name Conversion for R Series Devices for a list of affected terminal names. |
| --- | --- |

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| PXI/PXI_Clk10 | 10 MHz clock in the PXI chassis that you can use to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. Note You can phase-lock the FPGA device clock to the 10 MHz clock of the PXI chassis. Select Start»All Programs»NI»RIO Device Setup to launch the RIO Device Setup utility, which you can use to synchronize the FPGA clock to the 10 MHz clock of the PXI chassis. The FPGA clock itself does not change to 10 MHz even though you synchronize it. |
|  | Note You can phase-lock the FPGA device clock to the 10 MHz clock of the PXI chassis. Select Start»All Programs»NI»RIO Device Setup to launch the RIO Device Setup utility, which you can use to synchronize the FPGA clock to the 10 MHz clock of the PXI chassis. The FPGA clock itself does not change to 10 MHz even though you synchronize it. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Caution Do not use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable to access the PXI/PXI_Star channel if the FPGA device is in Slot 2 of the PXI chassis. Writing to the PXI/PXI_Star channel when the FPGA device is in Slot 2 affects the accuracy of the 10 MHz clock and can cause the PXI system to malfunction. |
|  | Caution Do not use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable to access the PXI/PXI_Star channel if the FPGA device is in Slot 2 of the PXI chassis. Writing to the PXI/PXI_Star channel when the FPGA device is in Slot 2 affects the accuracy of the 10 MHz clock and can cause the PXI system to malfunction. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA.In this format, device temperature = (Returned Device Temperature decimal value) ´ 0.25 °C. For example, a returned Device Temperature decimal value of 120 would indicate a device temperature of 30 °C. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxi-7852r.html language=enus -->
## TOPIC 00026: PXI-7852R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxi-7852r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxi-7852r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXI-7852R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 96 DIO lines, LX50, 750 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

|  | Note In LabVIEW 8.6.1 and earlier, some terminal names appear differently. Refer to Terminal Name Conversion for R Series Devices for a list of affected terminal names. |
| --- | --- |

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| PXI/PXI_Clk10 | 10 MHz clock in the PXI chassis that you can use to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. Note You can phase-lock the FPGA device clock to the 10 MHz clock of the PXI chassis. Select Start»All Programs»NI»RIO Device Setup to launch the RIO Device Setup utility, which you can use to synchronize the FPGA clock to the 10 MHz clock of the PXI chassis. The FPGA clock itself does not change to 10 MHz even though you synchronize it. |
|  | Note You can phase-lock the FPGA device clock to the 10 MHz clock of the PXI chassis. Select Start»All Programs»NI»RIO Device Setup to launch the RIO Device Setup utility, which you can use to synchronize the FPGA clock to the 10 MHz clock of the PXI chassis. The FPGA clock itself does not change to 10 MHz even though you synchronize it. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Caution Do not use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable to access the PXI/PXI_Star channel if the FPGA device is in Slot 2 of the PXI chassis. Writing to the PXI/PXI_Star channel when the FPGA device is in Slot 2 affects the accuracy of the 10 MHz clock and can cause the PXI system to malfunction. |
|  | Caution Do not use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable to access the PXI/PXI_Star channel if the FPGA device is in Slot 2 of the PXI chassis. Writing to the PXI/PXI_Star channel when the FPGA device is in Slot 2 affects the accuracy of the 10 MHz clock and can cause the PXI system to malfunction. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA.In this format, device temperature = (Returned Device Temperature decimal value) ´ 0.25 °C. For example, a returned Device Temperature decimal value of 120 would indicate a device temperature of 30 °C. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxi-7853r.html language=enus -->
## TOPIC 00027: PXI-7853R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxi-7853r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxi-7853r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXI-7853R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 96 DIO lines, LX85, 750 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

|  | Note In LabVIEW 8.6.1 and earlier, some terminal names appear differently. Refer to Terminal Name Conversion for R Series Devices for a list of affected terminal names. |
| --- | --- |

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| PXI/PXI_Clk10 | 10 MHz clock in the PXI chassis that you can use to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. Note You can phase-lock the FPGA device clock to the 10 MHz clock of the PXI chassis. Select Start»All Programs»NI»RIO Device Setup to launch the RIO Device Setup utility, which you can use to synchronize the FPGA clock to the 10 MHz clock of the PXI chassis. The FPGA clock itself does not change to 10 MHz even though you synchronize it. |
|  | Note You can phase-lock the FPGA device clock to the 10 MHz clock of the PXI chassis. Select Start»All Programs»NI»RIO Device Setup to launch the RIO Device Setup utility, which you can use to synchronize the FPGA clock to the 10 MHz clock of the PXI chassis. The FPGA clock itself does not change to 10 MHz even though you synchronize it. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Caution Do not use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable to access the PXI/PXI_Star channel if the FPGA device is in Slot 2 of the PXI chassis. Writing to the PXI/PXI_Star channel when the FPGA device is in Slot 2 affects the accuracy of the 10 MHz clock and can cause the PXI system to malfunction. |
|  | Caution Do not use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable to access the PXI/PXI_Star channel if the FPGA device is in Slot 2 of the PXI chassis. Writing to the PXI/PXI_Star channel when the FPGA device is in Slot 2 affects the accuracy of the 10 MHz clock and can cause the PXI system to malfunction. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA.In this format, device temperature = (Returned Device Temperature decimal value) ´ 0.25 °C. For example, a returned Device Temperature decimal value of 120 would indicate a device temperature of 30 °C. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxi-7854r.html language=enus -->
## TOPIC 00028: PXI-7854R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxi-7854r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxi-7854r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXI-7854R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 96 DIO lines, LX110, 750 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

|  | Note In LabVIEW 8.6.1 and earlier, some terminal names appear differently. Refer to Terminal Name Conversion for R Series Devices for a list of affected terminal names. |
| --- | --- |

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| PXI/PXI_Clk10 | 10 MHz clock in the PXI chassis that you can use to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. Note You can phase-lock the FPGA device clock to the 10 MHz clock of the PXI chassis. Select Start»All Programs»NI»RIO Device Setup to launch the RIO Device Setup utility, which you can use to synchronize the FPGA clock to the 10 MHz clock of the PXI chassis. The FPGA clock itself does not change to 10 MHz even though you synchronize it. |
|  | Note You can phase-lock the FPGA device clock to the 10 MHz clock of the PXI chassis. Select Start»All Programs»NI»RIO Device Setup to launch the RIO Device Setup utility, which you can use to synchronize the FPGA clock to the 10 MHz clock of the PXI chassis. The FPGA clock itself does not change to 10 MHz even though you synchronize it. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Caution Do not use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable to access the PXI/PXI_Star channel if the FPGA device is in Slot 2 of the PXI chassis. Writing to the PXI/PXI_Star channel when the FPGA device is in Slot 2 affects the accuracy of the 10 MHz clock and can cause the PXI system to malfunction. |
|  | Caution Do not use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable to access the PXI/PXI_Star channel if the FPGA device is in Slot 2 of the PXI chassis. Writing to the PXI/PXI_Star channel when the FPGA device is in Slot 2 affects the accuracy of the 10 MHz clock and can cause the PXI system to malfunction. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA.In this format, device temperature = (Returned Device Temperature decimal value) ´ 0.25 °C. For example, a returned Device Temperature decimal value of 120 would indicate a device temperature of 30 °C. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxie-7820r.html language=enus -->
## TOPIC 00029: PXIe-7820R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxie-7820r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxie-7820r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7820R Reference

R Series for PXI Express Digital RIO with Kintex-7 160T FPGA

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| PXI/PXI_Clk10 | Controls the 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarB | Controls the differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarC | Controls the differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXI/PXIe_Sync100 | Controls the reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html).

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxie-7821r.html language=enus -->
## TOPIC 00030: PXIe-7821R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxie-7821r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxie-7821r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7821R Reference

R Series for PXI Express Digital RIO with Kintex-7 160T FPGA

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| PXI/PXI_Clk10 | Controls the 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarB | Controls the differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarC | Controls the differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXI/PXIe_Sync100 | Controls the reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html).

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxie-7822r.html language=enus -->
## TOPIC 00031: PXIe-7822R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxie-7822r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxie-7822r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7822R Reference

R Series for PXI Express Digital RIO with Kintex-7 325T FPGA

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| PXI/PXI_Clk10 | Controls the 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarB | Controls the differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarC | Controls the differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXI/PXIe_Sync100 | Controls the reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html).

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxie-7846r.html language=enus -->
## TOPIC 00032: PXIe-7846R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxie-7846r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxie-7846r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7846R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 160T FPGA, 500 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| PXI/PXI_Clk10 | 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarB | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarC | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXI/PXIe_Sync100 | Reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxie-7847r.html language=enus -->
## TOPIC 00033: PXIe-7847R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxie-7847r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxie-7847r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7847R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 160T FPGA, 500 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| PXI/PXI_Clk10 | 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarB | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarC | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXI/PXIe_Sync100 | Reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxie-7856r.html language=enus -->
## TOPIC 00034: PXIe-7856R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxie-7856r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxie-7856r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7856R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 160T FPGA, 1 MS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| PXI/PXI_Clk10 | 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarB | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarC | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXI/PXIe_Sync100 | Reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxie-7857r.html language=enus -->
## TOPIC 00035: PXIe-7857R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxie-7857r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxie-7857r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7857R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 160T FPGA, 1 MS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| PXI/PXI_Clk10 | 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarB | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarC | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXI/PXIe_Sync100 | Reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxie-7858r.html language=enus -->
## TOPIC 00036: PXIe-7858R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxie-7858r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxie-7858r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7858R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 325T FPGA, 1 MS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| PXI/PXI_Clk10 | 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarB | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarC | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXI/PXIe_Sync100 | Reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxie-7861.html language=enus -->
## TOPIC 00037: PXIe-7861 Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxie-7861.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxie-7861.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7861 Reference

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 16 AI channels, 8 AO channels, 32 DIO channels, Kintex-7 160T FPGA, 1 MS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| PXI/PXI_Clk10 | 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarB | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarC | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXI/PXIe_Sync100 | Reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxie-7862.html language=enus -->
## TOPIC 00038: PXIe-7862 Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxie-7862.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxie-7862.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7862 Reference

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 16 AI channels, 8 AO channels, 32 DIO channels, Kintex-7 325T FPGA, 1 MS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| PXI/PXI_Clk10 | 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarB | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarC | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXI/PXIe_Sync100 | Reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxie-7865.html language=enus -->
## TOPIC 00039: PXIe-7865 Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxie-7865.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxie-7865.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7865 Reference

R Series Reconfigurable I/O Module (AI, AO, TTL-compatible DIO) for PXI Express, 2 AI, 24 AO, 32 TTL-compatible DIO, 1 MS/s AIO, 512 MB DRAM, Kintex-7 160T FPGA

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| PXI/PXI_Clk10 | 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarB | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarC | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXI/PXIe_Sync100 | Reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxie-7866.html language=enus -->
## TOPIC 00040: PXIe-7866 Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxie-7866.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxie-7866.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7866 Reference

R Series Reconfigurable I/O Module (AI, AO, TTL-compatible DIO) for PXI Express, 2 AI, 24 AO, 32 TTL-compatible DIO, 1 MS/s AIO, 512 MB DRAM, Kintex-7 325T FPGA

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| PXI/PXI_Clk10 | 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarB | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarC | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXI/PXIe_Sync100 | Reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxie-7867r.html language=enus -->
## TOPIC 00041: PXIe-7867R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxie-7867r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxie-7867r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7867R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 6 AI channels, 18 AO channels, 48 DIO channels, Kintex-7 160T FPGA, 1 MS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| PXI/PXI_Clk10 | 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarB | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarC | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXI/PXIe_Sync100 | Reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_pxie-7868r.html language=enus -->
## TOPIC 00042: PXIe-7868R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_pxie-7868r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_pxie-7868r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7868R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 6 AI channels, 18 AO channels, 48 DIO channels, Kintex-7 325T FPGA, 1 MS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| PXI/PXI_Clk10 | 10 MHz clock on the PXI backplane. You can use this clock to synchronize multiple PXI modules. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Star | Star trigger bus. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarB | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarB distributes trigger signals from the system timing slot to the peripherals (input). Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXIe_DStarC | Differential star trigger that creates connections between a PXI Express system timing module and a peripheral device. PXIe_DStarC sends trigger or clock signals from the peripherals to the system timing slot (output). Use an FPGA I/O Node configured for writing to access this channel. |
| PXI/PXIe_Sync100 | Reference signal that is synchronous to the rising edge of PXIe_CLK100. Use PXIe_Sync100 to synchronize multiple modules in a PXI Express system. Use an FPGA I/O Node configured for reading to access this channel. |
| PXI/PXI_Trigx | Trigger channel x, where x is the channel number <0..7>. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. Follow the guidelines for using PXI triggers with the LabVIEW FPGA Module. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_usb-7845r.html language=enus -->
## TOPIC 00043: USB-7845R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_usb-7845r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_usb-7845r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7845R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K70T FPGA, 500 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| Board IO/FPGA Temperature | Returns the current temperature of the FPGA, in degrees Celsius. |
| Board IO/UserLED1 | Controls the User LED1 on the module. Set the User LED1 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED2 | Controls the User LED2 on the module. Set the User LED2 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED3 | Controls the User LED3 on the module. Set the User LED3 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector0 DIO Logic Family | Sets the logic family for the DIO on connector0 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector1 DIO Logic Family | Sets the logic family for the DIO on connector1 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_usb-7845r_oem.html language=enus -->
## TOPIC 00044: USB-7845R OEM Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_usb-7845r_oem.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_usb-7845r_oem.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7845R OEM Reference

R Series Reconfigurable OEM I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K70T FPGA, 500 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| Board IO/FPGA Temperature | Returns the current temperature of the FPGA, in degrees Celsius. |
| Board IO/UserLED1 | Controls the User LED1 on the module. Set the User LED1 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED2 | Controls the User LED2 on the module. Set the User LED2 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED3 | Controls the User LED3 on the module. Set the User LED3 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector1:2 DIO Logic Family | Sets the logic family for the DIO on connector1 and connector2 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector3 DIO Logic Family | Sets the logic family for the DIO on connector3 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_usb-7846r.html language=enus -->
## TOPIC 00045: USB-7846R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_usb-7846r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_usb-7846r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7846R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K160T FPGA, 500 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| Board IO/FPGA Temperature | Returns the current temperature of the FPGA, in degrees Celsius. |
| Board IO/UserLED1 | Controls the User LED1 on the module. Set the User LED1 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED2 | Controls the User LED2 on the module. Set the User LED2 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED3 | Controls the User LED3 on the module. Set the User LED3 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector0 DIO Logic Family | Sets the logic family for the DIO on connector0 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector1 DIO Logic Family | Sets the logic family for the DIO on connector1 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_usb-7846r_oem.html language=enus -->
## TOPIC 00046: USB-7846R OEM Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_usb-7846r_oem.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_usb-7846r_oem.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7846R OEM Reference

R Series Reconfigurable OEM I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K160T FPGA, 500 kS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| Board IO/FPGA Temperature | Returns the current temperature of the FPGA, in degrees Celsius. |
| Board IO/UserLED1 | Controls the User LED1 on the module. Set the User LED1 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED2 | Controls the User LED2 on the module. Set the User LED2 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED3 | Controls the User LED3 on the module. Set the User LED3 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector1:2 DIO Logic Family | Sets the logic family for the DIO on connector1 and connector2 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector3 DIO Logic Family | Sets the logic family for the DIO on connector3 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_usb-7855r.html language=enus -->
## TOPIC 00047: USB-7855R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_usb-7855r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_usb-7855r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7855R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K70T FPGA, 1 MS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| Board IO/FPGA Temperature | Returns the current temperature of the FPGA, in degrees Celsius. |
| Board IO/UserLED0 | Controls the User LED0 on the module. Set the User LED0 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED1 | Controls the User LED1 on the module. Set the User LED1 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED2 | Controls the User LED2 on the module. Set the User LED2 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector0 DIO Logic Family | Sets the logic family for the DIO on connector0 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector1 DIO Logic Family | Sets the logic family for the DIO on connector1 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_usb-7855r_oem.html language=enus -->
## TOPIC 00048: USB-7855R OEM Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_usb-7855r_oem.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_usb-7855r_oem.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7855R OEM Reference

R Series Reconfigurable OEM I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K70T FPGA, 1 MS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| Board IO/FPGA Temperature | Returns the current temperature of the FPGA, in degrees Celsius. |
| Board IO/UserLED0 | Controls the User LED0 on the module. Set the User LED0 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED1 | Controls the User LED1 on the module. Set the User LED1 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED2 | Controls the User LED2 on the module. Set the User LED2 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector1:2 DIO Logic Family | Sets the logic family for the DIO on connector1 and connector2 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector3 DIO Logic Family | Sets the logic family for the DIO on connector3 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_usb-7856r.html language=enus -->
## TOPIC 00049: USB-7856R Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_usb-7856r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_usb-7856r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7856R Reference

R Series Reconfigurable I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K160T FPGA, 1 MS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| Board IO/FPGA Temperature | Returns the current temperature of the FPGA, in degrees Celsius. |
| Board IO/UserLED0 | Controls the User LED0 on the module. Set the User LED0 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED1 | Controls the User LED1 on the module. Set the User LED1 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED2 | Controls the User LED2 on the module. Set the User LED2 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector0 DIO Logic Family | Sets the logic family for the DIO on connector0 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector1 DIO Logic Family | Sets the logic family for the DIO on connector1 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/ni_usb-7856r_oem.html language=enus -->
## TOPIC 00050: USB-7856R OEM Reference

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/ni_usb-7856r_oem.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/ni_usb-7856r_oem.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7856R OEM Reference

R Series Reconfigurable OEM I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K160T FPGA, 1 MS/s AI Sample Rate

#### FPGA I/O Node

You can use an [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html), configured for reading and writing, with this device.

|  | Note FPGA I/O Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

#### Terminals in Software

You can select the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the channel number. Use an FPGA I/O Node configured for reading to access this channel. |
| AOx | Analog output channel x, where x is the channel number. Use an FPGA I/O Node configured for writing to access this channel. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this channel. |
| Connectorx/DIOPORTy | Digital input/output port y on connector x, where y is the port number and x is the connector number. A port is made up of eight digital channels. Use an FPGA I/O Node configured for reading or writing, or use the Set Output Data or Set Output Enable method to access this port. |
| Board IO/Device Temperature | Returns the current temperature of the device, in increments of 0.25 °C. The temperature is measured from an onboard temperature sensor on the device PCB, external to the FPGA. |
| Board IO/FPGA Temperature | Returns the current temperature of the FPGA, in degrees Celsius. |
| Board IO/UserLED0 | Controls the User LED0 on the module. Set the User LED0 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED1 | Controls the User LED1 on the module. Set the User LED1 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |
| Board IO/UserLED2 | Controls the User LED2 on the module. Set the User LED2 terminal to TRUE to turn the LED on and FALSE to turn the LED off. |

#### Arbitration

This device supports arbitration. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### I/O Methods

Use the [FPGA I/O Method Node](/csh?topicname=lvfpga/io_method_node.html) to invoke methods. You can use the following methods with this device.

|  | Note FPGA I/O Method Nodes cannot be configured to write to R Series digital output channels as both ports and lines. You must write digital outputs as either a port or a line. |
| --- | --- |

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node (FPGA Module) topic for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to timeout immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### I/O Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the gain calibration coefficient for an analog output channel. |
| LSB Weight (±1 V Range) | Returns the gain calibration coefficient for the ±1 V range of an analog input channel. |
| LSB Weight (±2 V Range) | Returns the gain calibration coefficient for the ±2 V range of an analog input channel. |
| LSB Weight (±5 V Range) | Returns the gain calibration coefficient for the ±5 V range of an analog input channel. |
| LSB Weight (±10 V Range) | Returns the gain calibration coefficient for the ±10 V range of an analog input channel. |
| Offset | Returns the offset calibration coefficient for an analog output channel. |
| Offset (±1 V Range) | Returns the offset calibration coefficient for the ±1 V range of an analog input channel. |
| Offset (±2 V Range) | Returns the offset calibration coefficient for the ±2 V range of an analog input channel. |
| Offset (±5 V Range) | Returns the offset calibration coefficient for the ±5 V range of an analog input channel. |
| Offset (±10 V Range) | Returns the offset calibration coefficient for the ±10 V range of an analog input channel. |
| Voltage Range | Sets the input range for an AI channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Module Properties

Use the [FPGA I/O Property Node](/csh?topicname=lvfpga/io_property_node.html) to access the following module properties for this device.

| Property | Description |
| --- | --- |
| AI Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended), NRSE (non-referenced single-ended ), or DIFF (differential). This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector1:2 DIO Logic Family | Sets the logic family for the DIO on connector1 and connector2 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |
| Connector3 DIO Logic Family | Sets the logic family for the DIO on connector3 as 3.3 V, 2.5 V, 1.8 V, 1.5 V, or 1.2 V. This property overwrites the value you configure in the Configure R Series I/O dialog box. |

#### Single-Cycle Timed Loop

This device supports the [single-cycle Timed Loop](/csh?topicname=lvfpga/fpga_timed_loop.html) for digital I/O only.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pci-7811r.html language=enus -->
## TOPIC 00051: PCI-7811R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pci-7811r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pci-7811r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCI-7811R

R Series Reconfigurable I/O for PCI (DIO) 160 DIO lines, 1 million gate FPGA

##### Software Reference

[PCI-7811R Reference](ni_pci-7811r.html)

#### PCI-7811R Pinout

[IMAGE alt='text' src='pci-7811r_pinout.png']

#### Related Topics

[NI 7811R Digital Port Assignments](ni_7811_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pci-7813r.html language=enus -->
## TOPIC 00052: PCI-7813R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pci-7813r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pci-7813r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCI-7813R

R Series Reconfigurable I/O for PCI (DIO) 160 DIO lines, 3 million gate FPGA

##### Software Reference

[PCI-7813R Reference](ni_pci-7813r.html)

#### PCI-7813R Pinout

[IMAGE alt='text' src='pci-7813r_pinout.png']

#### Related Topics

[NI 7813R Digital Port Assignments](ni_7813_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie-7820r.html language=enus -->
## TOPIC 00053: PCIe-7820R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie-7820r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie-7820r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7820R

R Series Digital I/O Module for PCI Express, 128 DIO, Kintex-7 160T FPGA

##### Software Reference

[PCIe-7820R Reference](ni_pcie-7820r.html)

#### PCIe-7820R Pinout

[IMAGE alt='text' src='pcie-7820r_pinout.png']

#### Related Topics

[PCIe-7820R Digital Port Assignments](ni_7820r_pcie_digital_port_assignments.html)
 
[PCIe-782xR RTSI Pinout](ni_782xr_pcie_rtsi.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie-7821r.html language=enus -->
## TOPIC 00054: PCIe-7821R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie-7821r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie-7821r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7821R

R Series Digital I/O Module for PCI Express, 128 DIO, 512 MB DRAM, Kintex-7 160T FPGA

##### Software Reference

[PCIe-7821R Reference](ni_pcie-7821r.html)

#### PCIe-7821R Pinout

[IMAGE alt='text' src='pcie-7821r_pinout.png']

#### Related Topics

[PCIe-7821R Digital Port Assignments](ni_7821r_pcie_digital_port_assignments.html)
 
[PCIe-782xR RTSI Pinout](ni_782xr_pcie_rtsi.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie-7822r.html language=enus -->
## TOPIC 00055: PCIe-7822R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie-7822r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie-7822r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7822R

R Series Digital I/O Module for PCI Express, 128 DIO, 512 MB DRAM, Kintex-7 325T FPGA

##### Software Reference

[PCIe-7822R Reference](ni_pcie-7822r.html)

#### PCIe-7822R Pinout

[IMAGE alt='text' src='pcie-7822r_pinout.png']

#### Related Topics

[PCIe-7822R Digital Port Assignments](ni_7822r_pcie_digital_port_assignments.html)
 
[PCIe-782xR RTSI Pinout](ni_782xr_pcie_rtsi.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie-7841r.html language=enus -->
## TOPIC 00056: PCIe-7841R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie-7841r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie-7841r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7841R

R Series Reconfigurable I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 96 DIO lines, LX30, 200 kS/s AI Sample Rate

##### Software Reference

[PCIe-7841R Reference](ni_pcie-7841r.html)

#### PCIe-7841R Pinout

[IMAGE alt='text' src='pcie-7841r_pinout.png']

#### Related Topics

[NI 7841R Digital Port Assignments](ni_7841r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie-7842r.html language=enus -->
## TOPIC 00057: PCIe-7842R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie-7842r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie-7842r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7842R

R Series Reconfigurable I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 96 DIO lines, LX50, 200 kS/s AI Sample Rate

##### Software Reference

[PCIe-7842R Reference](ni_pcie-7842r.html)

#### PCIe-7842R Pinout

[IMAGE alt='text' src='pcie-7842r_pinout.png']

#### Related Topics

[NI 7842R Digital Port Assignments](ni_7842r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie-7846.html language=enus -->
## TOPIC 00058: PCIe-7846

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie-7846.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie-7846.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7846

R Series Reconfigurable I/O Module (AI, AO, DIO) for PCI Express, 8 AI, 8 AO, 48 DIO, 500 kS/s AI, Kintex-7 160T FPGA****

##### Software Reference

[PCIe-7846 Reference](ni_pcie-7846.html)

#### PCIe-7846 Pinout

[IMAGE alt='pinout' src='pcie-7846-56-57-58_pinout.png']

#### Related Topics

[PCIe-7846 Digital Port Assignments](ni_7846_pcie_digital_port_assignments.html)
 
[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)
 
[PCIe-784x RTSI Pinout](ni_784x_pcie_rtsi.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie-7851r.html language=enus -->
## TOPIC 00059: PCIe-7851R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie-7851r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie-7851r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7851R

R Series Reconfigurable I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 96 DIO lines, LX30, 750 kS/s AI Sample Rate

##### Software Reference

[PCIe-7851R Reference](ni_pcie-7851r.html)

#### PCIe-7851R Pinout

[IMAGE alt='text' src='pcie-7851r_pinout.png']

#### Related Topics

[NI 7851R Digital Port Assignments](ni_7851r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie-7852r.html language=enus -->
## TOPIC 00060: PCIe-7852R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie-7852r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie-7852r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7852R

R Series Reconfigurable I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 96 DIO lines, LX50, 750 kS/s AI Sample Rate

##### Software Reference

[PCIe-7852R Reference](ni_pcie-7852r.html)

#### PCIe-7852R Pinout

[IMAGE alt='text' src='pcie-7852r_pinout.png']

#### Related Topics

[NI 7852R Digital Port Assignments](ni_7852r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie-7856.html language=enus -->
## TOPIC 00061: PCIe-7856

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie-7856.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie-7856.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7856

R Series Reconfigurable I/O Module (AI, AO, DIO) for PCI Express, 8 AI, 8 AO, 48 DIO, 1 MS/s AI, Kintex-7 160T FPGA

##### Software Reference

[PCIe-7856 Reference](ni_pcie-7856.html)

#### PCIe-7856 Pinout

[IMAGE alt='pinout' src='pcie-7846-56-57-58_pinout.png']

#### Related Topics

[PCIe-7856 Digital Port Assignments](ni_7856_pcie_digital_port_assignments.html)
 
[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)
 
[PCIe-785x RTSI Pinout](ni_785x_pcie_rtsi.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie-7857.html language=enus -->
## TOPIC 00062: PCIe-7857

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie-7857.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie-7857.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7857

R Series Reconfigurable I/O Module (AI, AO, DIO) for PCI Express, 8 AI, 8 AO, 48 DIO, 1 MS/s AI, 512 MB DRAM, Kintex-7 160T FPGA

##### Software Reference

[PCIe-7857 Reference](ni_pcie-7857.html)

#### PCIe-7857 Pinout

[IMAGE alt='pinout' src='pcie-7846-56-57-58_pinout.png']

#### Related Topics

[PCIe-7857 Digital Port Assignments](ni_7857_pcie_digital_port_assignments.html) 
 
[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)
 
[PCIe-785x RTSI Pinout](ni_785x_pcie_rtsi.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie-7858.html language=enus -->
## TOPIC 00063: PCIe-7858

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie-7858.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie-7858.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7858

R Series Reconfigurable I/O Module (AI, AO, DIO) for PCI Express, 8 AI, 8 AO, 48 DIO, 1 MS/s AI, 512 MB DRAM, Kintex-7 325T FPGA

##### Software Reference

[PCIe-7858 Reference](ni_pcie-7858.html)

#### PCIe-7858 Pinout

[IMAGE alt='pinout' src='pcie-7846-56-57-58_pinout.png']

#### Related Topics

[PCIe-7858 Digital Port Assignments](ni_7858_pcie_digital_port_assignments.html)
 
[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)
 
[PCIe-785x RTSI Pinout](ni_785x_pcie_rtsi.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie_7820_base_clocks.html language=enus -->
## TOPIC 00064: PCIe-7820R Base Clocks

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie_7820_base_clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie_7820_base_clocks.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7820R Base Clocks

A [base clock](/csh?topicname=lvfpgahelp/applying_fpga_clocks_and_timing_title.html) is a digital signal existing in hardware that you can use as a clock for an FPGA application. The following figure shows the clock routing for the PCIe-7820R base clocks.

[IMAGE alt='NI 782xR Base Clock Diagram' src='loc_782xr_pcie_base_clock_diagram.png']

The PCIe-7820R provides several base clock resources that can be used to run a LabVIEW FPGA VI. The 40 MHz onboard clock is generated within the device FPGA using a PLL. The PLL source is the onboard 100 MHz oscillator clock.

The following base clock resources are available for your device.

##### 40 MHz Onboard Clock

The 40 MHz Onboard Clock is the default clock in your LabVIEW FPGA project. This clock can be used as a [top-level clock](/csh?topicname=lvfpgahelp/selecting_toplevel_fpga_clk.html) for running your LabVIEW FPGA VI.

##### External Clock *x*

An External Clock is **input only** and can be used as a clock source for a Single Cycle Timed Loop (SCTL) to run at the frequency of your choice. The recommended input frequency range is 1 MHz to 80 MHz. An External Clock cannot be used as a Top-Level clock. The source for an External Clock input must be from a stable and glitch-free clock source. There is one External Clock per Connector, where *x* is the connector number.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie_782x_base_clocks.html language=enus -->
## TOPIC 00065: PCIe-782xR Base Clocks

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie_782x_base_clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie_782x_base_clocks.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-782*x*R Base Clocks

A [base clock](/csh?topicname=lvfpgahelp/applying_fpga_clocks_and_timing_title.html) is a digital signal existing in hardware that you can use as a clock for an FPGA application. The following figure shows the clock routing for the PCIe-782*x*R base clocks.

[IMAGE alt='NI 782xR Base Clock Diagram' src='loc_782xr_pcie_base_clock_diagram.png']

The PCIe-782*x*R provides several base clock resources that can be used to run a LabVIEW FPGA VI. The 40 MHz onboard clock is generated within the device FPGA using a PLL. The PLL source is the onboard 100 MHz oscillator clock.

The following base clock resources are available for your device.

##### DRAM Clock

DRAM Clock uses the 100 MHz Oscillator as its source. This clock drives the DRAM interface.

##### 40 MHz Onboard Clock

The 40 MHz Onboard Clock is the default clock in your LabVIEW FPGA project. This clock can be used as a [top-level clock](/csh?topicname=lvfpgahelp/selecting_toplevel_fpga_clk.html) for running your LabVIEW FPGA VI.

##### External Clock *x*

An External Clock is **input only** and can be used as a clock source for a Single Cycle Timed Loop (SCTL) to run at the frequency of your choice. The recommended input frequency range is 1 MHz to 80 MHz. An External Clock cannot be used as a Top-Level clock. The source for an External Clock input must be from a stable and glitch-free clock source. There is one External Clock per Connector, where *x* is the connector number.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie_7846_base_clocks.html language=enus -->
## TOPIC 00066: PCIe-7846 Base Clocks

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie_7846_base_clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie_7846_base_clocks.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7846 Base Clocks

A [base clock](/csh?topicname=lvfpgahelp/applying_fpga_clocks_and_timing_title.html) is a digital signal existing in hardware that you can use as a clock for an FPGA application. The following figure shows the clock routing for the PCIe-7846 base clocks.

[IMAGE alt='NI 782xR Base Clock Diagram' src='loc_784x_pcie_base_clock_diagram.png']

The PCIe-7846 provides several base clock resources that can be used to run a LabVIEW FPGA VI. The 40 MHz onboard clock is generated within the device FPGA using a PLL. The PLL source is the onboard 100 MHz oscillator clock.

The following base clock resources are available for your device.

##### 40 MHz Onboard Clock

The 40 MHz Onboard Clock is the default clock in your LabVIEW FPGA project. This clock can be used as a [top-level clock](/csh?topicname=lvfpgahelp/selecting_toplevel_fpga_clk.html) for running your LabVIEW FPGA VI.

##### External Clock *x*

An External Clock is **input only** and can be used as a clock source for a Single Cycle Timed Loop (SCTL) to run at the frequency of your choice. The recommended input frequency range is 1 MHz to 80 MHz. An External Clock cannot be used as a Top-Level clock. The source for an External Clock input must be from a stable and glitch-free clock source. There is one External Clock on Connector 1.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie_7856_base_clocks.html language=enus -->
## TOPIC 00067: PCIe-7856 Base Clocks

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie_7856_base_clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie_7856_base_clocks.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-7856 Base Clocks

A [base clock](/csh?topicname=lvfpgahelp/applying_fpga_clocks_and_timing_title.html) is a digital signal existing in hardware that you can use as a clock for an FPGA application. The following figure shows the clock routing for the PCIe-7856 base clocks.

[IMAGE alt='NI 782xR Base Clock Diagram' src='loc_785x_pcie_base_clock_diagram.png']

The PCIe-7856 provides several base clock resources that can be used to run a LabVIEW FPGA VI. The 40 MHz onboard clock is generated within the device FPGA using a PLL. The PLL source is the onboard 100 MHz oscillator clock.

The following base clock resources are available for your device.

##### 40 MHz Onboard Clock

The 40 MHz Onboard Clock is the default clock in your LabVIEW FPGA project. This clock can be used as a [top-level clock](/csh?topicname=lvfpgahelp/selecting_toplevel_fpga_clk.html) for running your LabVIEW FPGA VI.

##### External Clock *x*

An External Clock is **input only** and can be used as a clock source for a Single Cycle Timed Loop (SCTL) to run at the frequency of your choice. The recommended input frequency range is 1 MHz to 80 MHz. An External Clock cannot be used as a Top-Level clock. The source for an External Clock input must be from a stable and glitch-free clock source. There is one External Clock on Connector 1.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pcie_785x_base_clocks.html language=enus -->
## TOPIC 00068: PCIe-785x Base Clocks

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pcie_785x_base_clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pcie_785x_base_clocks.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PCIe-785*x* Base Clocks

A [base clock](/csh?topicname=lvfpgahelp/applying_fpga_clocks_and_timing_title.html) is a digital signal existing in hardware that you can use as a clock for an FPGA application. The following figure shows the clock routing for the PCIe-785*x* base clocks.

[IMAGE alt='NI 785x Base Clock Diagram' src='loc_785x_pcie_base_clock_diagram.png']

The PCIe-785*x* provides several base clock resources that can be used to run a LabVIEW FPGA VI. The 40 MHz onboard clock is generated within the device FPGA using a PLL. The PLL source is the onboard 100 MHz oscillator clock.

The following base clock resources are available for your device.

##### DRAM Clock

DRAM Clock uses the 100 MHz Oscillator as its source. This clock drives the DRAM interface. This clock is not available on the PCIe-7856.

##### 40 MHz Onboard Clock

The 40 MHz Onboard Clock is the default clock in your LabVIEW FPGA project. This clock can be used as a [top-level clock](/csh?topicname=lvfpgahelp/selecting_toplevel_fpga_clk.html) for running your LabVIEW FPGA VI.

##### External Clock *x*

An External Clock is **input only** and can be used as a clock source for a Single Cycle Timed Loop (SCTL) to run at the frequency of your choice. The recommended input frequency range is 1 MHz to 80 MHz. An External Clock cannot be used as a Top-Level clock. The source for an External Clock input must be from a stable and glitch-free clock source. There is one External Clock on Connector 1.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxi-7841r.html language=enus -->
## TOPIC 00069: PXI-7841R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxi-7841r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxi-7841r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXI-7841R

R Series Reconfigurable I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 96 DIO lines, LX30, 200 kS/s AI Sample Rate

##### Software Reference

[PXI-7841R Reference](ni_pxi-7841r.html)

#### PXI-7841R Pinout

[IMAGE alt='text' src='pxi-7841r_pinout.png']

#### Related Topics

[NI 7841R Digital Port Assignments](ni_7841r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxi-7842r.html language=enus -->
## TOPIC 00070: PXI-7842R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxi-7842r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxi-7842r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXI-7842R

R Series Reconfigurable I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 96 DIO lines, LX50, 200 kS/s AI Sample Rate

##### Software Reference

[PXI-7842R Reference](ni_pxi-7842r.html)

#### PXI-7842R Pinout

[IMAGE alt='text' src='pxi-7842r_pinout.png']

#### Related Topics

[NI 7842R Digital Port Assignments](ni_7842r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxi-7851r.html language=enus -->
## TOPIC 00071: PXI-7851R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxi-7851r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxi-7851r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXI-7851R

R Series Reconfigurable I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 96 DIO lines, LX30, 750 kS/s AI Sample Rate

##### Software Reference

[PXI-7851R Reference](ni_pxi-7851r.html)

#### PXI-7851R Pinout

[IMAGE alt='text' src='pxi-7851r_pinout.png']

#### Related Topics

[NI 7851R Digital Port Assignments](ni_7851r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxi-7853r.html language=enus -->
## TOPIC 00072: PXI-7853R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxi-7853r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxi-7853r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXI-7853R

R Series Reconfigurable I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 96 DIO lines, LX85, 750 kS/s AI Sample Rate

##### Software Reference

[PXI-7853R Reference](ni_pxi-7853r.html)

#### PXI-7853R Pinout

[IMAGE alt='text' src='pxi-7853r_pinout.png']

#### Related Topics

[NI 7853R Digital Port Assignments](ni_7853r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxi-7854r.html language=enus -->
## TOPIC 00073: PXI-7854R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxi-7854r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxi-7854r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXI-7854R

R Series Reconfigurable I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 96 DIO lines, LX110, 750 kS/s AI Sample Rate

##### Software Reference

[PXI-7854R Reference](ni_pxi-7854r.html)

#### PXI-7854R Pinout

[IMAGE alt='text' src='pxi-7854r_pinout.png']

#### Related Topics

[NI 7854R Digital Port Assignments](ni_7854r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxi_triggering.html language=enus -->
## TOPIC 00074: Using PXI Triggers with the LabVIEW FPGA Module

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxi_triggering.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxi_triggering.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### Using PXI Triggers with the LabVIEW FPGA Module

You can use the [FPGA I/O Node](/csh?topicname=lvfpga/fpga_io_node.html) to access the trigger lines on PXI R Series devices. When developing an FPGA VI that uses triggers, be sure to [reserve the trigger lines](reserving_triggers.html) you are using and, to ensure compatibility with other R Series devices, [configure trigger pulses](configuring_triggers.html) on PXI R Series devices to last for at least two clock cycles of the clock on the receiving device. Refer to the PXI Specification for more information about trigger bus requirements.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie-7820r.html language=enus -->
## TOPIC 00075: PXIe-7820R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie-7820r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie-7820r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7820R

R Series for PXI Express Digital RIO with Kintex-7 160T FPGA

##### Software Reference

[PXIe-7820R Reference](ni_pxie-7820r.html)

#### PXIe-7820R Pinout

[IMAGE alt='text' src='pxie-7820r_pinout.gif']

#### Related Topics

[PXIe-7820R Digital Port Assignments](ni_7820r_digital_port_assignments.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie-7821r.html language=enus -->
## TOPIC 00076: PXIe-7821R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie-7821r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie-7821r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7821R

R Series for PXI Express Digital RIO with Kintex-7 160T FPGA

##### Software Reference

[PXIe-7821R Reference](ni_pxie-7821r.html)

#### PXIe-7821R Pinout

[IMAGE alt='text' src='pxie-7821r_pinout.gif']

#### Related Topics

[PXIe-7821R Digital Port Assignments](ni_7821r_digital_port_assignments.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie-7822r.html language=enus -->
## TOPIC 00077: PXIe-7822R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie-7822r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie-7822r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7822R

R Series for PXI Express Digital RIO with Kintex-7 325T FPGA

##### Software Reference

[PXIe-7822R Reference](ni_pxie-7822r.html)

#### PXIe-7822R Pinout

[IMAGE alt='text' src='pxie-7822r_pinout.gif']

#### Related Topics

[PXIe-7822R Digital Port Assignments](ni_7822r_digital_port_assignments.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie-7846r.html language=enus -->
## TOPIC 00078: PXIe-7846R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie-7846r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie-7846r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7846R

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 160T FPGA, 500 kS/s AI Sample Rate

##### Software Reference

[PXIe-7846R Reference](ni_pxie-7846r.html)

#### PXIe-7846R Pinout

[IMAGE alt='pinout' src='pxie-7846r-47r-56r-57r-58r_pinout.png']

#### Related Topics

[PXIe-7846R Digital Port Assignments](ni_7846r_pxie_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie-7847r.html language=enus -->
## TOPIC 00079: PXIe-7847R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie-7847r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie-7847r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7847R

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 160T FPGA, 500 kS/s AI Sample Rate

##### Software Reference

[PXIe-7847R Reference](ni_pxie-7847r.html)

#### PXIe-7847R Pinout

[IMAGE alt='pinout' src='pxie-7846r-47r-56r-57r-58r_pinout.png']

#### Related Topics

[PXIe-7847R Digital Port Assignments](ni_7847r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie-7856r.html language=enus -->
## TOPIC 00080: PXIe-7856R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie-7856r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie-7856r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7856R

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 160T FPGA, 1 MS/s AI Sample Rate

##### Software Reference

[PXIe-7856R Reference](ni_pxie-7856r.html)

#### PXIe-7856R Pinout

[IMAGE alt='pinout' src='pxie-7846r-47r-56r-57r-58r_pinout.png']

#### Related Topics

[PXIe-7856R Digital Port Assignments](ni_7856r_pxie_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie-7857r.html language=enus -->
## TOPIC 00081: PXIe-7857R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie-7857r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie-7857r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7857R

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 160T FPGA, 1 MS/s AI Sample Rate

##### Software Reference

[PXIe-7857R Reference](ni_pxie-7857r.html)

#### PXIe-7857R Pinout

[IMAGE alt='pinout' src='pxie-7846r-47r-56r-57r-58r_pinout.png']

#### Related Topics

[PXIe-7857R Digital Port Assignments](ni_7857r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie-7858r.html language=enus -->
## TOPIC 00082: PXIe-7858R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie-7858r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie-7858r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7858R

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 325T FPGA, 1 MS/s AI Sample Rate

##### Software Reference

[PXIe-7858R Reference](ni_pxie-7858r.html)

#### PXIe-7858R Pinout

[IMAGE alt='pinout' src='pxie-7846r-47r-56r-57r-58r_pinout.png']

#### Related Topics

[PXIe-7858R Digital Port Assignments](ni_7858r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie-7861.html language=enus -->
## TOPIC 00083: PXIe-7861

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie-7861.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie-7861.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7861

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 16 AI channels, 8 AO channels, 32 DIO channels, Kintex-7 160T FPGA, 1 MS/s AI Sample Rate

##### Software Reference

[PXIe-7861 Reference](ni_pxie-7861.html)

#### PXIe-7861 Pinout

[IMAGE alt='pinout' src='pxie-7861-62_pinout.png']

#### Related Topics

[PXIe-7861 Digital Port Assignments](ni_7861_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie-7862.html language=enus -->
## TOPIC 00084: PXIe-7862

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie-7862.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie-7862.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7862

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 16 AI channels, 8 AO channels, 32 DIO channels, Kintex-7 325T FPGA, 1 MS/s AI Sample Rate

##### Software Reference

[PXIe-7862 Reference](ni_pxie-7862.html)

#### PXIe-7862 Pinout

[IMAGE alt='pinout' src='pxie-7861-62_pinout.png']

#### Related Topics

[PXIe-7862 Digital Port Assignments](ni_7862_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie-7866.html language=enus -->
## TOPIC 00085: PXIe-7866

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie-7866.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie-7866.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7866

R Series Reconfigurable I/O Module (AI, AO, TTL-compatible DIO) for PXI Express, 2 AI, 24 AO, 32 TTL-compatible DIO, 1 MS/s AIO, 512 MB DRAM, Kintex-7 325T FPGA

##### Software Reference

[PXIe-7866 Reference](ni_pxie-7866.html)

#### PXIe-7866 Pinout

[IMAGE alt='pinout' src='pxie-7865-66_pinout.png']

#### Related Topics

[PXIe-7866 Digital Port Assignments](ni_7866_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie-7867r.html language=enus -->
## TOPIC 00086: PXIe-7867R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie-7867r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie-7867r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7867R

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 6 AI channels, 18 AO channels, 48 DIO channels, Kintex-7 160T FPGA, 1 MS/s AI Sample Rate

##### Software Reference

[PXIe-7867R Reference](ni_pxie-7867r.html)

#### PXIe-7867R Pinout

[IMAGE alt='pinout' src='pxie-7867r-68r_pinout.png']

#### Related Topics

[PXIe-7867R Digital Port Assignments](ni_7867r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie-7868r.html language=enus -->
## TOPIC 00087: PXIe-7868R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie-7868r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie-7868r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-7868R

R Series Reconfigurable I/O Module (AI, AO, DIO) for PXI Express, 6 AI channels, 18 AO channels, 48 DIO channels, Kintex-7 325T FPGA, 1 MS/s AI Sample Rate

##### Software Reference

[PXIe-7868R Reference](ni_pxie-7868r.html)

#### PXIe-7868R Pinout

[IMAGE alt='pinout' src='pxie-7867r-68r_pinout.png']

#### Related Topics

[PXIe-7868R Digital Port Assignments](ni_7868r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie_784x_5x_base_clocks.html language=enus -->
## TOPIC 00088: PXIe-784x/5x/6xR Base Clocks

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie_784x_5x_base_clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie_784x_5x_base_clocks.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-784*x*/5*x*/6*x*R Base Clocks

A [base clock](/csh?topicname=lvfpgahelp/applying_fpga_clocks_and_timing_title.html) is a digital signal existing in hardware that you can use as a clock for an FPGA application. The following figure shows the clock routing for the PXIe-784*x*/5*x*/6*x*R base clocks.

[IMAGE alt='NI 784x/5xR Base Clock Diagram' src='loc_784x5xr_base_clock_diagram.png']

The PXIe-784*x*/5*x*/6*x*R provides several base clock resources that can be used to run a LabVIEW FPGA VI. The 40 MHz onboard clock and the 100 MHz clock are generated within the device FPGA using a PLL. The PLL source is either the PXI Express Clk100 backplane clock or the onboard 100 MHz oscillator clock. After the VI is downloaded, the FPGA detects whether or not the backplane 100 MHz clock is present, and if so, configures the PLL to lock to the backplane 100 MHz clock. If the PXI Express backplane clock is not present (for example, in a CompactPCI Express chassis), then the device FPGA sets the PLL to lock to the onboard 100 MHz oscillator clock.

The following base clock resources are available for your device.

##### DRAM Clock

DRAM Clock uses the 100 MHz Oscillator as its source. This clock drives the DRAM interface.

##### PXI_CLK10

PXI_CLK10 can be used as a source for running your LabVIEW FPGA VI.

##### PXIe_DStarA

Configure this clock to the frequency of your choice for running your LabVIEW FPGA VI. You can drive the PXIe_DStarA using a timing and synchronization device.

##### 40 MHz Onboard Clock

The 40 MHz Onboard Clock is the default clock in your LabVIEW FPGA project. This clock can be used as a [top-level clock](/csh?topicname=lvfpgahelp/selecting_toplevel_fpga_clk.html) for running your LabVIEW FPGA VI. The 40 MHz Onboard Clock is generated from a PLL which preferentially locks to the PXI Express Clk100 backplane clock.

##### 100 MHz Clock

The 100 MHz Clock can be used as a source for running your LabVIEW FPGA VI. The 100 MHz Clock is generated from a PLL which preferentially locks to the PXI Express Clk100 backplane clock.

##### External Clock *x*

An External Clock is **input only** and can be used as a clock source for a Single Cycle Timed Loop (SCTL) to run at the frequency of your choice. The recommended input frequency range is 1 to 80MHz. An External Clock cannot be used as a Top-Level clock. The source for an External Clock input must be from a stable and glitch-free clock source. There is one External Clock on Connector 1.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie_786x_base_clocks.html language=enus -->
## TOPIC 00089: PXIe-786x Base Clocks

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie_786x_base_clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie_786x_base_clocks.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-786*x* Base Clocks

A [base clock](/csh?topicname=lvfpgahelp/applying_fpga_clocks_and_timing_title.html) is a digital signal existing in hardware that you can use as a clock for an FPGA application. The following figures show the clock routing for the respective PXIe-786*x* base clocks.

[IMAGE alt='NI 784x/5xR Base Clock Diagram' src='loc_786xr_base_clock_diagram.png']

The PXIe-786*x* provides several base clock resources that can be used to run a LabVIEW FPGA VI. The 40 MHz onboard clock and the 100 MHz clock are generated within the device FPGA using a PLL. The PLL source is either the PXI Express Clk100 backplane clock or the onboard 100 MHz oscillator clock. After the VI is downloaded, the FPGA detects whether or not the backplane 100 MHz clock is present, and if so, configures the PLL to lock to the backplane 100 MHz clock. If the PXI Express backplane clock is not present (for example, in a CompactPCI Express chassis), then the device FPGA sets the PLL to lock to the onboard 100 MHz oscillator clock.

The following base clock resources are available for your device.

##### DRAM Clock

DRAM Clock uses the 100 MHz Oscillator as its source. This clock drives the DRAM interface.

##### PXI_CLK10

PXI_CLK10 can be used as a source for running your LabVIEW FPGA VI.

##### PXIe_DStarA

Configure this clock to the frequency of your choice for running your LabVIEW FPGA VI. You can drive the PXIe_DStarA using a timing and synchronization device.

##### 40 MHz Onboard Clock

The 40 MHz Onboard Clock is the default clock in your LabVIEW FPGA project. This clock can be used as a [top-level clock](/csh?topicname=lvfpgahelp/selecting_toplevel_fpga_clk.html) for running your LabVIEW FPGA VI. The 40 MHz Onboard Clock is generated from a PLL which preferentially locks to the PXI Express Clk100 backplane clock.

##### 100 MHz Clock

The 100 MHz Clock can be used as a source for running your LabVIEW FPGA VI. The 100 MHz Clock is generated from a PLL which preferentially locks to the PXI Express Clk100 backplane clock.

##### External Clock *x*

|  | Note Only applicable for the NI PXIe-7865 and NI PXIe-7866. |
| --- | --- |

An External Clock is **input only** and can be used as a clock source for a Single Cycle Timed Loop (SCTL) to run at the frequency of your choice. The recommended input frequency range is 1 to 20 MHz. An External Clock cannot be used as a Top-Level clock. The source for an External Clock input must be from a stable and glitch-free clock source. There is one External Clock on Connector 1.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/pxie_base_clocks.html language=enus -->
## TOPIC 00090: PXIe-782xR Base Clocks

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/pxie_base_clocks.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/pxie_base_clocks.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### PXIe-782*x*R Base Clocks

A [base clock](/csh?topicname=lvfpgahelp/applying_fpga_clocks_and_timing_title.html) is a digital signal existing in hardware that you can use as a clock for an FPGA application. The following figure shows the clock routing for the PXIe-782*x*R base clocks.

[IMAGE alt='NI 782xR Base Clock Diagram' src='loc_782xr_base_clock_diagram.png']

The PXIe-782*x*R provides several base clock resources that can be used to run a LabVIEW FPGA VI. The 40 MHz onboard clock and the 100 MHz clock are generated within the device FPGA using a PLL. The PLL source is either the PXI Express Clk100 backplane clock or the onboard 100 MHz oscillator clock. After the VI is downloaded, the FPGA detects whether or not the backplane 100 MHz clock is present, and if so, configures the PLL to lock to the backplane 100 MHz clock. If the PXI Express backplane clock is not present (for example, in a CompactPCI Express chassis), then the device FPGA sets the PLL to lock to the onboard 100 MHz oscillator clock.

The following base clock resources are available for your device.

##### DRAM Clock

DRAM Clock uses the 100 MHz Oscillator as its source. This clock drives the DRAM interface.

##### PXI_CLK10

PXI_CLK10 can be used as a source for running your LabVIEW FPGA VI.

##### PXIe_DStarA

Configure this clock to the frequency of your choice for running your LabVIEW FPGA VI. You can drive the PXIe_DStarA using a timing and synchronization device.

##### 40 MHz Onboard Clock

The 40 MHz Onboard Clock is the default clock in your LabVIEW FPGA project. This clock can be used as a [top-level clock](/csh?topicname=lvfpgahelp/selecting_toplevel_fpga_clk.html) for running your LabVIEW FPGA VI. The 40 MHz Onboard Clock is generated from a PLL which preferentially locks to the PXI Express Clk100 backplane clock.

##### 100 MHz Clock

The 100 MHz Clock can be used as a source for running your LabVIEW FPGA VI. The 100 MHz Clock is generated from a PLL which preferentially locks to the PXI Express Clk100 backplane clock.

##### External Clock *x*

An External Clock is **input only** and can be used as a clock source for a Single Cycle Timed Loop (SCTL) to run at the frequency of your choice. The recommended input frequency range is 1 to 80MHz. An External Clock cannot be used as a Top-Level clock. The source for an External Clock input must be from a stable and glitch-free clock source. There is one External Clock per Connector, where *x* is the connector number.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/r_series_related_documentation.html language=enus -->
## TOPIC 00091: R Series Related Documentation

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/r_series_related_documentation.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/r_series_related_documentation.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### R Series Related Documentation

Most R Series manuals are available as PDFs at ni.com/manuals.

The following documents contain information that you may find helpful as you use this help file:

- Getting Started with R Series Multifunction RIO —Use this document when installing the software and hardware.
- NI R Series Multifunction RIO User Manual —Use this manual to learn more about your NI 781 x R/783 x R/784 x R/785 x R hardware, such as connecting I/O signals to your device.
- NI R Series Multifunction RIO Specifications —Use this document as a reference for the hardware specifications of the NI 781 x R/783 x R/784 x R/785 x R device.
- For other R Series devices, each model has their respective Getting Started Guide and Specifications documents, searchable by their model.
- NI 78xxR Utilities Help—Use this help file to learn more about the utilities you can use with your NI 78 xx R Multifunction R Series device. This help file is accessible by clicking Help in the NI 78 xx R utility user interface.
- Software Support for CompactRIO, CompactDAQ, Single-Board RIO, R Series, and EtherCAT—The versions of LabVIEW, the LabVIEW FPGA Module, the LabVIEW Real-Time Module, and device driver software you need for the R Series devices in your system.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/reading_rseries_device_temp.html language=enus -->
## TOPIC 00092: Reading the Temperature of an R Series Device

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/reading_rseries_device_temp.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/reading_rseries_device_temp.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### Reading the Temperature of an R Series Device

NI 784*x*R/785*x*R/786*x*R and NI 78xx devices have an onboard temperature sensor. Complete the following steps to read the temperature of the chassis or device.

1. Create a new project or open an existing project.
2. Configure the LabVIEW Project for your NI 784 x R/785 x R /786*x*R and NI 78xx device by completing the following steps:
  1. Right-click My Computer in the Project Explorer window and select New»Targets and Devices from the shortcut menu to display the Add Targets and Devices dialog box.
  2. Select the appropriate device under R Series and click the OK button.
3. Make sure the Device Temperature I/O item is added to the project.
4. Right-click the FPGA target in the Project Explorer window and select New»VI from the shortcut menu to add a new VI to the project.
5. Place an FPGA I/O Node on the block diagram of the VI.
6. Click the element section of the FPGA I/O Node and select Add New FPGA I/O .
7. In the New FPGA I/O dialog box, select Board I/O»Device Temperature from the Available Resources list, and click OK .
8. Right-click the Device Temperature output of the FPGA I/O Node and select Create»Indicator from the shortcut menu.

The **Device Temperature** output returns 16-bit values for the temperature. Refer to your device topic for information on converting this value into meaningful engineering units.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/reading_rseries_fpga_temp.html language=enus -->
## TOPIC 00093: Reading the Temperature of the FPGA on an NI USB R Series Device

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/reading_rseries_fpga_temp.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/reading_rseries_fpga_temp.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### Reading the Temperature of the FPGA on an NI USB R Series Device

You can read the FPGA temperature of an NI USB R Series device. Complete the following steps to read the temperature of the device FPGA.

1. Create a new project or open an existing project.
2. Configure the LabVIEW Project for your NI USB R device by completing the following steps:
  1. Right-click My Computer in the Project Explorer window and select New»Targets and Devices from the shortcut menu to display the Add Targets and Devices dialog box.
  2. Select the appropriate device under R Series and click the OK button.
3. Make sure the FPGA Temperature I/O item is added to the project.
4. Right-click the FPGA target in the Project Explorer window and select New»VI from the shortcut menu to add a new VI to the project.
5. Place an FPGA I/O Node on the block diagram of the VI.
6. Click the element section of the FPGA I/O Node and select Add New FPGA I/O .
7. In the New FPGA I/O dialog box, select Board I/O»FPGA Temperature from the Available Resources list, and click OK .
8. Right-click the FPGA Temperature output of the FPGA I/O Node and select Create»Indicator from the shortcut menu.

The **FPGA Temperature** output returns [fixed-point](/csh?topicname=lvfpgaconcepts/fpgafixedpoint.html) data from the FPGA in degrees Celsius. The fixed-point data is signed, with a word length of 12 bits and an integer word length of 10 bits.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/reserving_triggers.html language=enus -->
## TOPIC 00094: Reserving Trigger Lines for PXI R Series Devices

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/reserving_triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/reserving_triggers.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### Reserving Trigger Lines for PXI R Series Devices

NI recommends that you reserve the trigger lines used by NI PXI R Series devices. If two PXI devices try to drive the same trigger line in different applications, or if the PXI devices are not programmed to work together, the application will not work and, in some cases, third-party PXI devices can be damaged. You can use Measurement & Automation Explorer (MAX) or the host VI to reserve trigger lines.

#### Reserving Trigger Lines in MAX

If you download and run the FPGA VI interactively, configure the PXI triggers in MAX. MAX maintains the trigger reservation for the R Series device even after you cycle power to the PXI chassis.

#### Reserving Trigger Lines in the LabVIEW FPGA Host VI

If you download and run the FPGA VI programmatically, reserve the trigger lines in the host VI. Use the Invoke Method function to reserve the trigger and to release the trigger reservation. LabVIEW releases the trigger reservation for the R Series device automatically when you close the FPGA VI reference. You must run the host VI again to reserve the trigger.

##### Reserving Trigger Lines

Complete the following steps to reserve a trigger line for a PXI R Series device.

1. Place the Open FPGA VI Reference function on the block diagram and configure it for the FPGA device and FPGA VI.
2. Place the Invoke Method function on the block diagram.
3. Wire the FPGA VI Reference Out output of the Open FPGA VI Reference function to the FPGA VI Reference In input of the Invoke Method function.
4. Wire the error out output of the FPGA VI Reference function to the error in input of the Invoke Method function.
5. Click the Invoke Method function and select Reserve PXI Trigger from the shortcut menu.
6. Right-click the Trigger input and select Create»Constant . An enum constant is created to help you select the trigger.

To reserve multiple trigger lines, repeat steps 2 to 6 for each trigger line you want to reserve, wiring the **FPGA VI Reference Out** output of the existing Invoke Method function to the **FPGA VI Reference In** input of the Invoke Method node that follows it.

##### Releasing Trigger Lines

Complete the following steps to release a trigger line for a PXI R Series device.

1. Place the Open FPGA VI Reference function on the block diagram and configure it for the FPGA device and FPGA VI.
2. Place the Invoke Method function on the block diagram.
3. Wire the FPGA VI Reference Out output of the Open FPGA VI Reference function to the FPGA VI Reference In input of the Invoke Method function.
4. Wire the error out output of the FPGA VI Reference function to the error in input of the Invoke Method function.
5. Click the Invoke Method function and select Unreserve PXI Trigger from the shortcut menu.
6. Right-click the Trigger input and select Create»Constant . An enum constant is created to help you select the trigger.

To release multiple trigger lines, repeat steps 2 to 6 for each trigger line you want to release, wiring the **FPGA VI Reference Out** output of the existing Invoke Method function to the **FPGA VI Reference In** input of the Invoke Method node that follows it.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/rseries_help.html language=enus -->
## TOPIC 00095: NI R Series Multifunction RIO Device Drivers

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/rseries_help.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/rseries_help.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### NI R Series Multifunction RIO Device Drivers

January 2020, 371508AA-01

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

© 2012–2020 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/rseries_terminal_name_changes.html language=enus -->
## TOPIC 00096: Terminal Name Conversion for R Series Devices

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/rseries_terminal_name_changes.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/rseries_terminal_name_changes.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### Terminal Name Conversion for R Series Devices

In LabVIEW version 8.6.1 and earlier, some RTSI and PXI terminal names appear differently. The following table lists all affected terminal names.

| Terminal Name(LabVIEW 2009) | Terminal Name(LabVIEW 8.6.1 and earlier) |
| --- | --- |
| PXI/PXI_Trigx | PXI/TRIGx |
| PXI/PXI_Clk10 | PXI/CLK10 |
| PXI/PXI_Star | PXI/STAR |
| PXI/PXI_Lblx | PXI/LBLSTARx |
| PXI/PXI_Lbrx | PXI/LBRx |
| RTSI/RTSIx | RTSI/TRIGx |
| RTSI/RTSI7 | RTSI/OSC |

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/supporting_pci_express_fpga_module_functionality.html language=enus -->
## TOPIC 00097: Supported PCI Express FPGA Module Functionality

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/supporting_pci_express_fpga_module_functionality.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/supporting_pci_express_fpga_module_functionality.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### Supported PCI Express FPGA Module Functionality

#### Arbitration

This device supports [arbitration](/csh?topicname=lvfpgaconcepts/arbitration_options.html) to determine which object can access the resource if multiple objects request access at the same time. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### FPGA Base Clocks

This device supports [FPGA I/O Properties](/csh?topicname=lvfpgahelp/applying_fpga_clocks_and_timing_title.html). For more information about the available base clock resources, refer to the relevant base clocks topic:

- PCIe-782*x*R Base Clocks
- PCIe-784*x* Base Clocks
- PCIe-785*x* Base Clocks

#### Single-Cycle Timed Loop

FPGA I/O Properties

multiple clock domains

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/supporting_pxi_express_fpga_module_functionality.html language=enus -->
## TOPIC 00098: Supported PXI Express FPGA Module Functionality

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/supporting_pxi_express_fpga_module_functionality.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/supporting_pxi_express_fpga_module_functionality.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### Supported PXI Express FPGA Module Functionality

#### Arbitration

This device supports [arbitration](/csh?topicname=lvfpgaconcepts/arbitration_options.html) to determine which object can access the resource if multiple objects request access at the same time. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### FPGA Base Clocks

FPGA I/O Properties

PXIe-782xR Base Clocks

#### Single-Cycle Timed Loop

FPGA I/O Properties

multiple clock domains

#### Peer-to-Peer Streaming

peer-to-peer data streaming

#### NI R Series Peer-to-Peer Resource Availability

Peer to Peer Reader

Peer to Peer Writer

| FIFO Type | Description |
| --- | --- |
| DMA input | Reads data into the FIFO from the VI. |
| DMA output | Writes data from the FIFO into the VI. |
| P2P Writer | Writes data to the peer-to-peer reader device. |
| P2P Reader | Reads data from the peer-to-peer writer device. |

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/supporting_pxi_express_fpga_module_functionality_pxie-784x5x.html language=enus -->
## TOPIC 00099: Supported PXI Express FPGA Module Functionality

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/supporting_pxi_express_fpga_module_functionality_pxie-784x5x.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/supporting_pxi_express_fpga_module_functionality_pxie-784x5x.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### Supported PXI Express FPGA Module Functionality

#### Arbitration

This device supports [arbitration](/csh?topicname=lvfpgaconcepts/arbitration_options.html) to determine which object can access the resource if multiple objects request access at the same time. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### FPGA Base Clocks

FPGA I/O Properties

PXIe-784x/5xR/6xR Base Clocks

#### Single-Cycle Timed Loop

FPGA I/O Properties

multiple clock domains

#### Peer-to-Peer Streaming

peer-to-peer data streaming

#### NI R Series Peer-to-Peer Resource Availability

Peer to Peer Reader

Peer to Peer Writer

| FIFO Type | Description |
| --- | --- |
| DMA input | Writes data into the FIFO from the VI. |
| DMA output | Reads data from the FIFO into the VI. |
| P2P Writer | Writes data to the peer-to-peer reader device. |
| P2P Reader | Reads data from the peer-to-peer writer device. |

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/supporting_pxi_express_fpga_module_functionality_pxie-786x.html language=enus -->
## TOPIC 00100: Supported PXI Express FPGA Module Functionality

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/supporting_pxi_express_fpga_module_functionality_pxie-786x.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/supporting_pxi_express_fpga_module_functionality_pxie-786x.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### Supported PXI Express FPGA Module Functionality

#### Arbitration

This device supports [arbitration](/csh?topicname=lvfpgaconcepts/arbitration_options.html) to determine which object can access the resource if multiple objects request access at the same time. Configure the arbitration settings for the channels of this device in the [FPGA I/O Properties](/csh?topicname=lvfpgadialog/fpga_io_node_properties.html) dialog box for the FPGA I/O item you are using.

#### FPGA Base Clocks

FPGA I/O Properties

PXIe-786x Base Clocks

#### Single-Cycle Timed Loop

FPGA I/O Properties

multiple clock domains

#### Peer-to-Peer Streaming

peer-to-peer data streaming

#### NI R Series Peer-to-Peer Resource Availability

Peer to Peer Reader

Peer to Peer Writer

| FIFO Type | Description |
| --- | --- |
| DMA input | Writes data into the FIFO from the VI. |
| DMA output | Reads data from the FIFO into the VI. |
| P2P Writer | Writes data to the peer-to-peer reader device. |
| P2P Reader | Reads data from the peer-to-peer writer device. |

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/usb-7845r.html language=enus -->
## TOPIC 00101: USB-7845R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/usb-7845r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/usb-7845r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7845R

R Series Reconfigurable I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K70T FPGA, 500 kS/s AI Sample Rate

##### Software Reference

[USB-7845R Reference](ni_usb-7845r.html)

#### USB-7845R Pinout

[IMAGE alt='text' src='loc_usb-7855r_pinout.png']

#### Related Topics

[USB-7845R Digital Port Assignments](ni_7845r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

[Reading the Temperature of an R Series Device FPGA](reading_rseries_fpga_temp.html)

[Removing an USB R Series Device from the Host](usb_hot-swap.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/usb-7845r_oem.html language=enus -->
## TOPIC 00102: USB-7845R OEM

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/usb-7845r_oem.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/usb-7845r_oem.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7845R OEM

R Series Reconfigurable OEM I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K70T FPGA, 500 kS/s AI Sample Rate

##### Software Reference

[USB-7845R OEM Reference](ni_usb-7845r_oem.html)

#### USB-7845R OEM Pinout

[IMAGE alt='text' src='loc_oem_pinout.png']

#### Related Topics

[USB-7845R OEM Digital Port Assignments](ni_7845r_oem_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

[Reading the Temperature of an R Series Device FPGA](reading_rseries_fpga_temp.html)

[Removing an USB R Series Device from the Host](usb_hot-swap.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/usb-7846r.html language=enus -->
## TOPIC 00103: USB-7846R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/usb-7846r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/usb-7846r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7846R

R Series Reconfigurable I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K160T FPGA, 500 kS/s AI Sample Rate

##### Software Reference

[USB-7846R Reference](ni_usb-7846r.html)

#### USB-7846R Pinout

[IMAGE alt='text' src='loc_usb-7856r_pinout.png']

#### Related Topics

[USB-7846R Digital Port Assignments](ni_7846r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

[Reading the Temperature of an R Series Device FPGA](reading_rseries_fpga_temp.html)

[Removing an USB R Series Device from the Host](usb_hot-swap.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/usb-7846r_oem.html language=enus -->
## TOPIC 00104: USB-7846R OEM

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/usb-7846r_oem.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/usb-7846r_oem.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7846R OEM

R Series Reconfigurable OEM I/O Module (AI, AO, DIO)

8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K160T FPGA, 500 kS/s AI Sample Rate

##### Software Reference

[USB-7846R OEM Reference](ni_usb-7846r_oem.html)

#### USB-7846R OEM Pinout

[IMAGE alt='text' src='loc_oem_pinout.png']

#### Related Topics

[USB-7846R OEM Digital Port Assignments](ni_7846r_oem_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

[Reading the Temperature of an R Series Device FPGA](reading_rseries_fpga_temp.html)

[Removing an USB R Series Device from the Host](usb_hot-swap.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/usb-7855r.html language=enus -->
## TOPIC 00105: USB-7855R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/usb-7855r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/usb-7855r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7855R

R Series Reconfigurable I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K70T FPGA, 1 MS/s AI Sample Rate

##### Software Reference

[USB-7855R Reference](ni_usb-7855r.html)

#### USB-7855R Pinout

[IMAGE alt='text' src='loc_usb-7855r_pinout.png']

#### Related Topics

[USB-7855R Digital Port Assignments](ni_7855r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

[Reading the Temperature of an R Series Device FPGA](reading_rseries_fpga_temp.html)

[Removing an USB R Series Device from the Host](usb_hot-swap.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/usb-7855r_oem.html language=enus -->
## TOPIC 00106: USB-7855R OEM

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/usb-7855r_oem.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/usb-7855r_oem.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7855R OEM

R Series Reconfigurable OEM I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K70T FPGA, 1 MS/s AI Sample Rate

##### Software Reference

[USB-7855R OEM Reference](ni_usb-7855r_oem.html)

#### USB-7855R OEM Pinout

[IMAGE alt='text' src='loc_oem_pinout.png']

#### Related Topics

[USB-7855R OEM Digital Port Assignments](ni_7855r_oem_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

[Reading the Temperature of an R Series Device FPGA](reading_rseries_fpga_temp.html)

[Removing an USB R Series Device from the Host](usb_hot-swap.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/usb-7856r.html language=enus -->
## TOPIC 00107: USB-7856R

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/usb-7856r.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/usb-7856r.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7856R

R Series Reconfigurable I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K160T FPGA, 1 MS/s AI Sample Rate

##### Software Reference

[USB-7856R Reference](ni_usb-7856r.html)

#### USB-7856R Pinout

[IMAGE alt='text' src='loc_usb-7856r_pinout.png']

#### Related Topics

[USB-7856R Digital Port Assignments](ni_7856r_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

[Reading the Temperature of an R Series Device FPGA](reading_rseries_fpga_temp.html)

[Removing an USB R Series Device from the Host](usb_hot-swap.html)

<!--NI_TOPIC bundle=ni-78xx-api-ref path=target2devicehelp/usb-7856r_oem.html language=enus -->
## TOPIC 00108: USB-7856R OEM

- bundle_id: `ni-78xx-api-ref`
- source_path: `target2devicehelp/usb-7856r_oem.html`
- source_url: https://docs-be.ni.com/bundle/ni-78xx-api-ref/raw/resource/enus/target2devicehelp/usb-7856r_oem.html
- document_id: `ni-78xx-api-ref`
- page_type: `leaf`
- content_type: ``

### USB-7856R OEM

R Series Reconfigurable OEM I/O Module (AI, AO, DIO) 8 AI channels, 8 AO channels, 48 DIO channels, Kintex-7 K160T FPGA, 1 MS/s AI Sample Rate

##### Software Reference

[USB-7856R OEM Reference](ni_usb-7856r_oem.html)

#### USB-7856R OEM Pinout

[IMAGE alt='text' src='loc_oem_pinout.png']

#### Related Topics

[USB-7856R OEM Digital Port Assignments](ni_7856r_oem_digital_port_assignments.html)

[Reading the Temperature of an R Series Device](reading_rseries_device_temp.html)

[Reading the Temperature of an R Series Device FPGA](reading_rseries_fpga_temp.html)

[Removing an USB R Series Device from the Host](usb_hot-swap.html)
