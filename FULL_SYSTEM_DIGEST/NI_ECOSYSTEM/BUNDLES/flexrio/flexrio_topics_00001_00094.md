# NI DOCUMENT BUNDLE: flexrio

<!--NI_BUNDLE_CHUNK bundle=flexrio start=1 end=94 -->
<!--NI_TOPIC bundle=flexrio path=accessing-data-sequentially.html language=enus -->
## TOPIC 00001: Accessing Data Sequentially

- bundle_id: `flexrio`
- source_path: `accessing-data-sequentially.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/accessing-data-sequentially.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: DRAM is optimized for high storage density and high bandwidth. DRAM accesses data sequentially and in large blocks. For example, you have to read the data in address 0x1 after you have read the data in address 0x0 and the processor reads large blocks of memory into cache, even if the program being e

### Accessing Data Sequentially

DRAM is optimized for high storage density and high bandwidth. DRAM accesses data sequentially and in large blocks. For example, you have to read the data in address 0x1 after you have read the data in address 0x0 and the processor reads large blocks of memory into cache, even if the program being executed requests a single byte.

To maximize performance, avoid switching between reading and writing, accessing noncontiguous addresses, or writing to memory in decrementing-address fashion. The most efficient access strategy is to perform only one type of access, either reading or writing, on a large number of sequential addresses. Although this is optimal, it is not practical for most applications. A more practical approach is to maximize the amount of sequential data being accessed and minimizing changes in access modes.

The Process VI in the Memory IDL has an arbiter configuration input that allows you to dynamically alter the number of sequential reads and writes (write grant time and read grant time). Use this functionality to dedicate 100% of DRAM bandwidth to reading only, writing only, or equally sharing bandwidth between reads and writes.

Parent topic:

Using DRAM Effectively with FlexRIO

Related concepts:

- Memory Overview

<!--NI_TOPIC bundle=flexrio path=adapter-module-interface-protocol.html language=enus -->
## TOPIC 00002: Adapter Module Interface Protocol

- bundle_id: `flexrio`
- source_path: `adapter-module-interface-protocol.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/adapter-module-interface-protocol.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FlexRIO FPGA modules can interface to a wide variety of adapter modules. These modules may have different V[cco]/V[ccoA]/V[ccoB] power requirements, as well as a variety of GPIO I/O standards and signal directions. FlexRIO devices also allow users to change I/O personalities with each different adap

### Adapter Module Interface Protocol

FlexRIO FPGA modules can interface to a wide variety of adapter modules. These modules may have different V<sub>cco</sub>/V<sub>ccoA</sub>/V<sub>ccoB</sub> power requirements, as well as a variety of GPIO I/O standards and signal directions. FlexRIO devices also allow users to change I/O personalities with each different adapter module. Consequently, NI recommends that each adapter module design contain an EEPROM for identification and protection.

This identification EEPROM is connected to dedicated pins and designated at a specific
 I<sup>2</sup>C, allowing the FlexRIO driver to identify the adapter module you
 insert. Include an EEPROM in your design to allow for improved electrical protection for
 the adapter module and the FlexRIO FPGA module. Using an identification EEPROM prevents
 the use of incompatible adapter module settings, such as using incorrect power rails and
 double-driving digital interface pins. Refer to the *EEPROM Overview* section
 for additional information about adding an ID EEPROM to your adapter module design.

The FlexRIO device employs the following adapter module identification, power up, and removal processes to prevent applying improper voltages or double-driving signals.

#### Adapter Module Insertion
 Protocol

The following figure shows the process that the FlexRIO system performs when you
 insert a new adapter module into the FlexRIO FPGA module.

Note

[IMAGE alt='image' src='GUID-93CC8F23-54C0-4E3E-80E8-7F4688C8645D-a5.gif']

Note

FlexRIO Adapter Module
 Development Kit

Note

Project Explorer

IO Module

Properties

IO Module
 Properties

Status

Status

#### Adapter Module Removal
 Protocol

To properly remove an adapter module from the FlexRIO FPGA module, you must disable
 the adapter module within the LabVIEW FPGA user interface. To disable the adapter
 module within LabVIEW, complete the following steps:

1. In your LabVIEW Project Explorer window, right-click the
 IO Module item under the FPGA Target and select
 Properties to display the IO Module
 Properties dialog box.
2. Click the Status category to view the adapter module
 Status dialog.
3. Deselect the checkbox for Enable IO Module Power . When
 you deselect this option, firmware tristates the FlexRIO I/O and disables all
 adapter module power rails.
4. Click OK .

FlexRIO driver software allows users to enable and disable adapter modules, as well
 as EEPROM access, within the LabVIEW interface. Refer to the *FlexRIO Adapter
 Module Development Kit* for more information about programming your
 adapter module EEPROM.

#### EEPROM Overview

NI strongly recommends that you add an EEPROM to your adapter module for
 identification purposes. Adding an EEPROM to you adapter module helps provide better
 electrical protection for both the adapter module and the FlexRIO FPGA module. It
 also helps to improve the software configuration experience within LabVIEW FPGA.

The adapter module identification EEPROM included in your design must be an
 I<sup>2</sup>C-capable 2 Kbit device (256 × 8). These parts are widely available
 from electronics manufacturers and are often identified as 24C02. Manufacturers
 typically place a prefix to identify their version. For example, the ST
 Microelectronics EEPROM part number is M24C02.

The following figure shows a complete FlexRIO EEPROM connection circuit. This circuit
 shows the connections to the EEPROM (U<sub>1</sub>) and two additional connections
 required for proper adapter module configuration. The supporting parts required for
 the EEPROM are a bypass capacitor (C<sub>1</sub>) on the line from
 V<sub>eeprom</sub>, a pull-up resistor (R<sub>1</sub>) on address line A1 to
 V<sub>eeprom</sub>, and a pull-down resistor (R<sub>2</sub>) on the WP line.
 C<sub>1</sub> is a 0.1 μF ceramic capacitor with a voltage rating of 6.3 V or
 higher. For best performance, use a capacitor with an X7R dielectric. Use 4.7 kΩ
 resistors, which can be any resistor type rated for at least 25 V and 10% tolerance
 or better. You can find other details regarding this interface in the EEPROM
 datasheet. For more information about EEPROM use and programming in your
 application, refer to the *FlexRIO Adapter Module Development Kit*.

Note

2

2

| 1 | 0 | 1 | 0 | 0 | 1 | 0 | R/W |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EEPROM Device Type Identifier | Chip Enable | Operation1 = R0 = W |  |  |  |  |  |
| A2 | A1 | A0 |  |  |  |  |  |

Parent topic:

Configuring Your Adapter Module Using LabVIEW FPGA

Related information:

- FlexRIO Adapter Module Development Kit

<!--NI_TOPIC bundle=flexrio path=adding-custom-clip-to-your-labview-project.html language=enus -->
## TOPIC 00003: Adding Custom CLIP to Your LabVIEW Project

- bundle_id: `flexrio`
- source_path: `adding-custom-clip-to-your-labview-project.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/adding-custom-clip-to-your-labview-project.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: In software, FlexRIO adapter modules are referred to as IO Modules. For convenience, LabVIEW also supports storing your adapter module socketed component-level IP in a location external to the IO Modules directory. For example, you may wish to store your adapter module CLIP in the same location as y

### Adding Custom CLIP to Your LabVIEW Project

Note

IO Modules

For convenience, LabVIEW also supports storing your adapter module socketed component-level IP in a location external to the IO Modules directory. For example, you may wish to store your adapter module CLIP in the same location as your LabVIEW FPGA project files. In this situation, your adapter module CLIP is not automatically discovered by LabVIEW and must be manually added to your LabVIEW project. To manually add your adapter module CLIP to the LabVIEW project, complete the following steps:

1. Create a new LabVIEW project.
2. Add your FPGA target to the
 project.
 The FlexRIO FPGA module appears in the Project Explorer 
 window with an unconfigured adapter module.
3. Right-click the FPGA target and select Properties from the shortcut menu to display the FPGA Target Properties dialog box.
4. Select Component Level IP from the Category list to display the Component Level IP FPGA Target Properties page.
5. Click the Add button. A file browser window
 launches, prompting you for the location of your CLIP XML file. Browse to the XML
 file location, select it, and click OK .
6. Click OK on the FPGA Target Properties dialog box. Your adapter module CLIP has now been added to your FPGA target and is available for selection from within the IO Module Properties dialog box.

Parent topic:

Configuring a Custom Adapter Module in LabVIEW

Related information:

- Creating a LabVIEW Project
- General Page (FPGA Target Properties Dialog Box)
- Component-Level IP Page (FPGA Target Properties Dialog
 Box)

<!--NI_TOPIC bundle=flexrio path=adding-your-custom-adapter-module-and-module.html language=enus -->
## TOPIC 00004: Adding Your Custom Adapter Module and Module I/O in LabVIEW

- bundle_id: `flexrio`
- source_path: `adding-your-custom-adapter-module-and-module.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/adding-your-custom-adapter-module-and-module.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: In software, FlexRIO adapter modules are referred to as IO Modules. To use your adapter module with LabVIEW, complete the following steps: Create a new LabVIEW project. Add your FPGA target to the project. The FlexRIO FPGA module appears in the Project Explorer window with an unconfigured adapter mo

### Adding Your Custom Adapter Module and Module I/O in LabVIEW

Note

IO Modules

To use your adapter module with LabVIEW, complete the following steps:

1. Create a new LabVIEW project.
2. Add your FPGA target to the
 project.
 The FlexRIO FPGA module appears in the Project Explorer 
 window with an unconfigured adapter module.
3. To configure your adapter module, right-click the IO Module item under the FPGA Target and select Properties to display the IO Module Properties dialog box.
4. Select the Enable IO Module checkbox to enable the adapter module, and select your adapter module from the IO Modules list.
5. The adapter module socketed CLIP you created should appear in the Component Level
 IP list. Select your adapter module CLIP from the
 Component Level IP list. The adapter module and CLIP
 descriptions display in the Details box. If there were errors
 with your .tbc file or the CLIP XML file, syntax errors are
 displayed and must be corrected for the items to appear correctly.
6. In the Clock Selections category, configure any CLIP clock
 signals
 as necessary.
7. Click OK . Your custom I/O now appears underneath the IO Module in the project, and your adapter module is ready for use.

Parent topic:

Configuring a Custom Adapter Module in LabVIEW

Related information:

- Creating a LabVIEW Project
- Adding FPGA Targets to a LabVIEW Project (FPGA Module)
- Using CLIP Clocks (FPGA Module)

<!--NI_TOPIC bundle=flexrio path=avoiding-multipe-memory-items-per-bank.html language=enus -->
## TOPIC 00005: Avoiding Multiple Memory Items Per Bank

- bundle_id: `flexrio`
- source_path: `avoiding-multipe-memory-items-per-bank.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/avoiding-multipe-memory-items-per-bank.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Memory items that are assigned to the same bank cannot access the DRAM simultaneously. Access to the DRAM is controlled by a grant time that dictates when a memory item can read or write to the DRAM bank, and for how long. By default, a DRAM bank assigns grant times of 50 cycles per memory item. You

### Avoiding Multiple Memory Items Per
 Bank

Note

The ideal number of memory items per bank is 1. Having more than one memory item per bank prevents either item from accessing the DRAM with the most efficient bandwidth and latency, since memory items have to share access to the DRAM as dictated by the grant time.

Parent topic:

Using DRAM Effectively with FlexRIO

<!--NI_TOPIC bundle=flexrio path=basic-elements-overview.html language=enus -->
## TOPIC 00006: Basic Elements Overview

- bundle_id: `flexrio`
- source_path: `basic-elements-overview.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/basic-elements-overview.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This instrument design library contains several low-level elements, such as edge detectors, latches, and FIFOs. Using this library can be beneficial when developing new FPGA logic for your software-designed instrument. These basic elements are used in other instrument design libraries and the samp

### Basic Elements Overview

This instrument design library contains several low-level elements, such as edge detectors, latches, and FIFOs.  Using this library can be beneficial when developing new FPGA logic for your software-designed instrument.  These basic elements are used in other instrument design libraries and the sample projects for your device.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=basic-elements-overview_2.html language=enus -->
## TOPIC 00007: Basic Elements Overview

- bundle_id: `flexrio`
- source_path: `basic-elements-overview_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/basic-elements-overview_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This instrument design library contains several low-level elements, such as edge detectors, latches, and FIFOs. Using this library can be beneficial when developing new FPGA logic for your software-designed instrument. These basic elements are used in other instrument design libraries and the samp

### Basic Elements Overview

This instrument design library contains several low-level elements, such as edge detectors, latches, and FIFOs.  Using this library can be beneficial when developing new FPGA logic for your software-designed instrument.  These basic elements are used in other instrument design libraries and the sample projects for your device.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=channel-overview.html language=enus -->
## TOPIC 00008: Channel Overview

- bundle_id: `flexrio`
- source_path: `channel-overview.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/channel-overview.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this instrument design library to manipulate channel data for use by other instrument design libraries or LabVIEW FPGA primitives. This library contains IP for interleaving channel waveforms into a single array. You can use this library to dynamically choose which channels to interleave while al

### Channel Overview

Use this instrument design library to manipulate channel data for use by other instrument design libraries or LabVIEW FPGA primitives. This library contains IP for interleaving channel waveforms into a single array. You can use this library to dynamically choose which channels to interleave while also maintaining a constant output array size.

This instrument design library is particularly useful when used with the Multirecord Acquisition instrument design library for dynamically selecting the channels to be stored into memory. The library can also be used to stream a single array of interleaved data.

This library supports variations in data type, number of channels, and samples per cycle.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=channel-overview_2.html language=enus -->
## TOPIC 00009: Channel Overview

- bundle_id: `flexrio`
- source_path: `channel-overview_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/channel-overview_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this instrument design library to manipulate channel data for use by other instrument design libraries or LabVIEW FPGA primitives. This library contains IP for interleaving channel waveforms into a single array. You can use this library to dynamically choose which channels to interleave while al

### Channel Overview

Use this instrument design library to manipulate channel data for use by other instrument design libraries or LabVIEW FPGA primitives. This library contains IP for interleaving channel waveforms into a single array. You can use this library to dynamically choose which channels to interleave while also maintaining a constant output array size.

This instrument design library is particularly useful when used with the Multirecord Acquisition instrument design library for dynamically selecting the channels to be stored into memory. The library can also be used to stream a single array of interleaved data.

This library supports variations in data type, number of channels, and samples per cycle.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=clip-adapters-overview.html language=enus -->
## TOPIC 00010: CLIP Adapters Overview

- bundle_id: `flexrio`
- source_path: `clip-adapters-overview.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/clip-adapters-overview.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CLIP Adapters instrument design library includes AXI4-Lite and AXI4-Stream wrappers. These wrappers implement protocol timing and signaling into simple reader or writer endpoints that present 4-wire handshaking to the diagram. This handshaking allows for easier transition to many FPGA features w

### CLIP Adapters Overview

The CLIP Adapters instrument design library includes AXI4-Lite and AXI4-Stream wrappers. These wrappers implement protocol timing and signaling into simple reader or writer endpoints that present 4-wire handshaking to the diagram. This handshaking allows for easier transition to many FPGA features without the need to implement this state logic on your own.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=clip-adapters-overview_2.html language=enus -->
## TOPIC 00011: CLIP Adapters Overview

- bundle_id: `flexrio`
- source_path: `clip-adapters-overview_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/clip-adapters-overview_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CLIP Adapters instrument design library includes AXI4-Lite and AXI4-Stream wrappers. These wrappers implement protocol timing and signaling into simple reader or writer endpoints that present 4-wire handshaking to the diagram. This handshaking allows for easier transition to many FPGA features w

### CLIP Adapters Overview

The CLIP Adapters instrument design library includes AXI4-Lite and AXI4-Stream wrappers. These wrappers implement protocol timing and signaling into simple reader or writer endpoints that present 4-wire handshaking to the diagram. This handshaking allows for easier transition to many FPGA features without the need to implement this state logic on your own.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=configuring-a-custom-adapter-module-in-labvie.html language=enus -->
## TOPIC 00012: Configuring a Custom Adapter Module in LabVIEW

- bundle_id: `flexrio`
- source_path: `configuring-a-custom-adapter-module-in-labvie.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/configuring-a-custom-adapter-module-in-labvie.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can customize the I/O for your FlexRIO device by using socketed component-level IP (CLIP). Socketed CLIP allows you to add your own VHDL code to a LabVIEW FPGA project to program the FPGA to interface with your custom adapter module circuitry. Custom adapter module configuration requires you to

### Configuring a Custom Adapter Module in LabVIEW

You can customize the I/O for your FlexRIO device by using socketed component-level IP (CLIP). Socketed CLIP allows you to add your own VHDL code to a LabVIEW FPGA project to program the FPGA to interface with your custom adapter module circuitry.

Custom adapter module configuration requires you to create additional software interface elements
 and socketed CLIP. Refer to the *FlexRIO Adapter Module Development Kit User
 Manual*, shipped with FlexRIO Custom Adapter Module Development kit, for
 complete information about custom I/O creation and use with the LabVIEW FPGA Module.

#### Creating A LabVIEW Project with
 Custom Component-Level IP (CLIP)

Note

IO Modules

Before creating a new LabVIEW project that uses your custom CLIP, first ensure that
 your CLIP is stored within the IO Modules directory on disk, inside
 your manufacturer-specific subfolder. NI recommends that you store your socketed
 CLIP in the same directory as your adapter module .tbc file.

Storing your CLIP in the IO Modules directory on disk assists in
 integrating your adapter module support files in the LabVIEW development
 environment. LabVIEW automatically discovers any CLIP items stored in the IO
 Modules directory and makes them selectable in your project. Using the
 IO Modules directory to store your CLIP also enables you to
 develop a custom adapter module installer package that automatically installs
 support for your adapter module.

The following topics contain information about adding your custom adapter module and
 CLIP to your LabVIEW FPGA project.

- Adding Your Custom Adapter Module and Module I/O in LabVIEW
- Adding Custom CLIP to Your LabVIEW Project

Parent topic:

Configuring Your Adapter Module Using LabVIEW FPGA

Related concepts:

- Adding Your Custom Adapter Module and Module I/O in LabVIEW
- Adding Custom CLIP to Your LabVIEW Project

Related information:

- Using CLIP in an FPGA Application

<!--NI_TOPIC bundle=flexrio path=configuring-a-flexrio-adapter-module-in-labvi.html language=enus -->
## TOPIC 00013: Configuring a FlexRIO Adapter Module in LabVIEW

- bundle_id: `flexrio`
- source_path: `configuring-a-flexrio-adapter-module-in-labvi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/configuring-a-flexrio-adapter-module-in-labvi.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each FlexRIO adapter module ships with socketed component-level (CLIP) items that determine the module I/O available for use in the LabVIEW project. Refer to the specific CLIP reference topic for your adapter module for a list of available socketed CLIP items and provided signals. In software, FlexR

### Configuring a FlexRIO Adapter Module in LabVIEW

Note

IO
 Modules

To add a socketed CLIP item to your LabVIEW project, complete the following steps:

1. Right-click the IO Module item in the Project
 Explorer window and select Properties .The
 Properties dialog box allows you to configure which
 adapter module to compile support for, as well as which CLIP item should be used to
 access the adapter module signals.
2. Check the Enable IO Module box.
3. In the IO Modules window, select National
 Instruments : NI [your module number] .
4. Select the Component Level IP item that contains the I/O you
 wish to add to your project.
5. Click OK .

Project Explorer

```text
(<IO Module Name> : <Component Level IP Name>)
```

The following figure shows a properly configured adapter module in the LabVIEW
 Project Explorer window. The module number and available I/O
 signals that appear vary depending on the FlexRIO adapter module and CLIP option you
 use.

[IMAGE alt='image' src='GUID-8CE7AEFE-6D88-4271-9635-19861C73773A-a5.gif']

Project Explorer

Note

0

Advanced Code Generation
 Page

Parent topic:

Configuring Your Adapter Module Using LabVIEW FPGA

<!--NI_TOPIC bundle=flexrio path=configuring-a-flexrio-adapter-module.html language=enus -->
## TOPIC 00014: Configuring a FlexRIO Adapter Module

- bundle_id: `flexrio`
- source_path: `configuring-a-flexrio-adapter-module.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/configuring-a-flexrio-adapter-module.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: If your FlexRIO project includes a FlexRIO adapter module (optional), refer to Configuring Your Adapter Module Using LabVIEW FPGA for information about configuring your adapter module using LabVIEW FPGA.

### Configuring a FlexRIO Adapter Module

If your FlexRIO project includes a FlexRIO adapter module (optional), refer to *Configuring
 Your Adapter Module Using LabVIEW FPGA* for information about configuring your
 adapter module using LabVIEW FPGA.

Parent topic:

Creating an FPGA FlexRIO Project

Related concepts:

- Configuring Your Adapter Module Using LabVIEW FPGA

<!--NI_TOPIC bundle=flexrio path=configuring-a-flexrio-adapter-module_2.html language=enus -->
## TOPIC 00015: Configuring a FlexRIO Adapter Module

- bundle_id: `flexrio`
- source_path: `configuring-a-flexrio-adapter-module_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/configuring-a-flexrio-adapter-module_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: If your FlexRIO project includes a FlexRIO adapter module (optional), refer to Configuring Your Adapter Module Using LabVIEW FPGA for information about configuring your adapter module using LabVIEW FPGA.

### Configuring a FlexRIO Adapter Module

If your FlexRIO project includes a FlexRIO adapter module (optional), refer to *Configuring
 Your Adapter Module Using LabVIEW FPGA* for information about configuring your
 adapter module using LabVIEW FPGA.

Parent topic:

Creating a Real-Time FlexRIO Project

<!--NI_TOPIC bundle=flexrio path=configuring-dram-with-fpga-memory-items.html language=enus -->
## TOPIC 00016: Configuring DRAM with FPGA Memory Items

- bundle_id: `flexrio`
- source_path: `configuring-dram-with-fpga-memory-items.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/configuring-dram-with-fpga-memory-items.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the FPGA memory item interface to use DRAM in the same way that you use block memory and look-up tables (LUT). DRAM memory items appear in the Project Explorer window under the FPGA target. The FPGA memory item interface allows you to partition the physical DRAM banks into multiple memory items.

### Configuring DRAM with FPGA Memory Items

Use the FPGA memory item interface to use DRAM in the same way that you use block memory and look-up tables (LUT). DRAM memory items appear in the Project Explorer window under the FPGA target. The FPGA memory item interface allows you to partition the physical DRAM banks into multiple memory items. You can create target-scoped or VI-defined memory items. For more information about these different memory items, refer to the Using FPGA Memory topic.

Complete the following steps to configure DRAM with FPGA memory items.

1. Determine whether you want to create a target-scoped memory item or a VI-defined memory item.
 
 Note A memory item
 targets a single DRAM bank. If you only select one memory item, this memory item
 can be as large as the entire bank. You can use memory items to divide the full
 DRAM space into smaller memories that you can access independently from
 different sections of the LabVIEW FPGA code. The figure below shows the logic
 that LabVIEW generates to provide access to a DRAM bank.
  - To create a target-scoped memory item, which you can access in the entire
 FPGA VI hierarchy, right-click the FPGA target in the Project
 Explorer window and select New»Memory 
 from the shortcut menu. The Memory
 Properties
 dialog box appears.
  - To create a VI-defined memory item, place a VI-defined Memory
 Configuration
 node on the block diagram, right-click the node, and select
 Configure from the shortcut menu. The Memory
 Properties
 dialog box appears.
2. Configure the memory item in the Memory
 Properties
 dialog box. Click OK . The memory item is now populated in the
 Project Explorer window under the target. Note If you use a Memory
 Method
 Node in
 a single-cycle Timed Loop, make sure the corresponding
 arbitration
 option is Arbitrate if Multiple Requester Only or
 Never Arbitrate.
3. Use the memory
 item
 in an FPGA VI.

For more information about optimizing DRAM access with FlexRIO, refer to *Using DRAM
 Effectively with FlexRIO*.

Parent topic:

DRAM Interfaces

Related concepts:

- Using DRAM Effectively with FlexRIO

<!--NI_TOPIC bundle=flexrio path=configuring-dram-with-socketed-clip.html language=enus -->
## TOPIC 00017: Configuring DRAM with Socketed CLIP

- bundle_id: `flexrio`
- source_path: `configuring-dram-with-socketed-clip.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/configuring-dram-with-socketed-clip.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the socketed CLIP interface to communicate directly with the onboard DRAM. Socketed CLIP lists all memory interfaces that are compatible with the selected DRAM bank item. Complete the following steps to configure DRAM with socketed CLIP. Right-click an FPGA target in the Project Explorer window

### Configuring DRAM with Socketed CLIP

Use the socketed CLIP interface to communicate directly with the onboard DRAM. Socketed CLIP lists all memory interfaces that are compatible with the selected DRAM bank item.

Complete the following steps to configure DRAM with socketed CLIP.

1. Right-click an FPGA target in the Project Explorer window and select Properties from the shortcut menu to display the FPGA Target Properties dialog box.
2. Select DRAM Properties to display the DRAM Properties page.
3. In the Mode drop-down list, select Socketed CLIP .
4. Click OK . The new DRAM Bank is populated in the Project Explorer window under the target.
5. Right-click DRAM Bank x and select Properties to display the DRAM Bank x Properties dialog box.
6. Select Enable DRAM if it is not already selected to display the DRAM configuration options.
7. Configure the DRAM bank in the DRAM Bank x Properties dialog box and click OK when you are done. The DRAM signals are populated in the Project Explorer window under DRAM Bank x .

Note

Parent topic:

DRAM Interfaces

<!--NI_TOPIC bundle=flexrio path=configuring-trigger-pulses.html language=enus -->
## TOPIC 00018: Configuring Trigger Pulses

- bundle_id: `flexrio`
- source_path: `configuring-trigger-pulses.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/configuring-trigger-pulses.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To ensure compatibility with other FlexRIO devices, configure trigger pulses on a FlexRIO PXI device to last for at least two clock cycles of the clock on the receiving device. For example, if the clock on the receiving device is 80 MHz, which is a clock period of 12.5 nanoseconds, the trigger line

### Configuring Trigger Pulses

Note

The clocks between a FlexRIO PXI device and another PXI device might not be perfectly synchronized. If you assert a trigger line on a FlexRIO PXI device, you cannot determine at what point in the clock period the trigger registers in the receiving flip-flop. If the trigger arrives during the setup or hold time of the receiving flip-flop, you cannot determine the state of the line for that clock period. Asserting the trigger pulse for two clock cycles ensures that at least one clock cycle on the receiving flip-flop registers as a rising edge and transfers as a trigger.

Parent topic:

PXI Triggers

<!--NI_TOPIC bundle=flexrio path=configuring-your-adapter-module-using-labview.html language=enus -->
## TOPIC 00019: Configuring Your Adapter Module Using LabVIEW FPGA

- bundle_id: `flexrio`
- source_path: `configuring-your-adapter-module-using-labview.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/configuring-your-adapter-module-using-labview.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW FPGA Module includes a feature for HDL IP integration called component-level IP (CLIP). FlexRIO devices support two types of CLIP: user-defined CLIP and socketed CLIP. User-defined CLIP—Allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FP

### Configuring Your Adapter Module Using LabVIEW FPGA

The LabVIEW FPGA Module includes a feature for HDL IP integration called component-level IP (CLIP).

FlexRIO devices support two types of CLIP: user-defined CLIP and socketed CLIP.

- User-defined CLIP —Allows you to insert HDL IP into an FPGA target, enabling VHDL code to communicate directly with an FPGA VI.
- Socketed CLIP —Provides the same IP integration functionality of the user-defined CLIP, while also allowing the CLIP to communicate directly with circuitry external to the FPGA. Adapter module socketed CLIP allows your IP to communicate directly with both the FPGA VI and the external adapter module connector interface or the FlexRIO FPGA module onboard DRAM.

The following illustration shows the relationship between an FPGA VI and CLIP. [IMAGE alt='image' src='GUID-098AE767-8031-4E73-A41E-84452F53E232-a5.gif']

To configure your adapter module using the LabVIEW FPGA module, you can do one of the following things:

- Configure a FlexRIO Adapter Module in LabVIEW.
- Configure a Custom Adapter Module in LabVIEW.

For information about using LabVIEW FPGA to access the onboard DRAM, refer to the DRAM Interfaces.

Parent topic:

FlexRIO Adapter Module Support

Related concepts:

- DRAM Interfaces
- Configuring a FlexRIO Adapter Module in LabVIEW
- Configuring a Custom Adapter Module in LabVIEW

Related information:

- Using CLIP in an FPGA Application
- FPGA I/O Node
- Advanced Code Generation Page

<!--NI_TOPIC bundle=flexrio path=configuring-your-flexrio-fpga-target.html language=enus -->
## TOPIC 00020: Configuring Your FlexRIO FPGA Target

- bundle_id: `flexrio`
- source_path: `configuring-your-flexrio-fpga-target.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/configuring-your-flexrio-fpga-target.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure FlexRIO FPGA targets from the Project Explorer window. Complete the following steps to configure your FlexRIO FPGA target. Create a new FlexRIO project or open an existing project. Add an FPGA target to the project. Right-click the FPGA target in the Project Explorer window and sel

### Configuring Your FlexRIO FPGA Target

You can configure FlexRIO FPGA targets from the Project Explorer window. Complete the following steps to configure your FlexRIO FPGA target.

1. Create a new FlexRIO project or open an existing project.
2. Add an FPGA target to the project.
3. Right-click the FPGA target in the Project Explorer window and select Properties from the shortcut menu. The FPGA Target Properties Dialog Box appears.
4. Select General from the Category list.
5. Enter a Name for the FPGA target. The Name identifies the FPGA target in the Project Explorer window.
6. (Optional) If you did not select an existing target when you added the FPGA target to the project, enter a Resource for the FPGA target, which can be found in Measurement & Automation Explorer (MAX). The Resource associates the FPGA target in the Project Explorer window with a specific FPGA target connected to the development computer, network computer, or RT target.
7. (Optional) Specify the execution mode you want to use to debug an FPGA VI on the Execution Mode page.

 Note 
 LabVIEW displays only the options that the current FPGA target supports.
8. (Optional) Specify the top-level clock on the Top-Level Clock page.
9. (Optional) Add, create, or modify component-level IP declaration XML files on the Component-Level IP page.
10. (Optional) Configure target-scoped properties for accessing DRAM on the DRAM Properties page.
11. (Optional) Configure conditional disable symbols on the Conditional Disable Symbols page.
12. Click OK .

Parent topic:

Creating an FPGA FlexRIO Project

Related concepts:

- Creating an FPGA FlexRIO Project

<!--NI_TOPIC bundle=flexrio path=creating-a-real-time-flexrio-project.html language=enus -->
## TOPIC 00021: Creating a Real-Time FlexRIO Project

- bundle_id: `flexrio`
- source_path: `creating-a-real-time-flexrio-project.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/creating-a-real-time-flexrio-project.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to create a Real-Time FlexRIO project in LabVIEW. In LabVIEW, select New Project. Select Real-Time Project and click OK. In the Create New LabVIEW Real-Time Project window, select the project type in the Project type drop-down menu, create a name for the project in the P

### Creating a Real-Time FlexRIO Project

Complete the following steps to create a Real-Time FlexRIO project in LabVIEW.

1. In LabVIEW, select New Project .
2. Select Real-Time Project and click OK .
3. In the Create New LabVIEW Real-Time Project window, select the project type in the Project type drop-down menu, create a name for the project in the Project name field, and select a location to save the project in the Project folder field.
4. Click Next .
5. Add VIs to your project. You can either add blank VIs or import existing VIs to the host and the target.
6. Click Next .
7. In the Browse targets window, select Browse... to search for targets.
8. The Add Targets and Devices on <target name> window appears. select one of the following options.
  - Discover existing system - select this option if your FlexRIO FPGA target is installed in your computer.
  - Create new system - select this option if your hardware is not available or not connected.
9. Click OK .
10. Click Next .
11. Click Finish .
12. The project appears in the Project Explorer window.
13. Right-click the target and select New»FPGA Target . The FPGA target appears in the project under the Real-Time target.

For more information about using LabVIEW Real-Time, refer to the *LabVIEW Real-Time Module
 User Manual* on ni.com/docs. For information about advanced design
 considerations that use LabVIEW Real-Time and NI-793xR modules, refer to the
 *NI-7931R/7932R/7935R User Manual*.

Parent topic:

Getting Started with FlexRIO

Related information:

- LabVIEW Real-Time Module User Manual
- NI-7931R/7932R/7935R User Manual

<!--NI_TOPIC bundle=flexrio path=creating-an-fpga-flexrio-project.html language=enus -->
## TOPIC 00022: Creating an FPGA FlexRIO Project

- bundle_id: `flexrio`
- source_path: `creating-an-fpga-flexrio-project.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/creating-an-fpga-flexrio-project.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to create an FPGA FlexRIO project in LabVIEW. In LabVIEW, select Create Project. Select LabVIEW FPGA Project and click Finish. In the Create New LabVIEW FPGA Project window, select FlexRIO on My Computer and click Next. Under System Setup, select one of the following opt

### Creating an FPGA FlexRIO Project

Complete the following steps to create an FPGA FlexRIO project in LabVIEW.

1. In LabVIEW, select Create Project .
2. Select LabVIEW FPGA Project and click Finish .
3. In the Create New LabVIEW FPGA Project window, select FlexRIO on My Computer and click Next .
4. Under System Setup, select one of the following options.
  1. Discover existing system - select this option if your FlexRIO FPGA target is installed in your computer.
  2. Create new system - select this option if your hardware is not available or not connected.
5. Click Next .
6. Select your FlexRIO FPGA target from the drop-down menu. When you select a target, the wizard provides information about the target's FPGA type and DRAM, if applicable.
7. Click Next .
8. Click Finish .
9. The project appears in the Project Explorer window.
  - For information about configuring your FlexRIO FPGA module, refer to Configuring Your
 FlexRIO FPGA Target .
  - For information about configuring your project to use DRAM, refer to DRAM
 Interfaces .
  - For information about programming your device with FlexRIO VIs, refer to the FlexRIO LabVIEW API
 documentation.
  - For information about accessing advanced configuration options for FlexRIO devices and
 applications, refer to the FlexRIO LabVIEW API documentation.

Parent topic:

Getting Started with FlexRIO

Related concepts:

- Configuring Your FlexRIO FPGA Target
- DRAM Interfaces

<!--NI_TOPIC bundle=flexrio path=cycle-accurate-simulation.html language=enus -->
## TOPIC 00023: Cycle-Accurate Simulation

- bundle_id: `flexrio`
- source_path: `cycle-accurate-simulation.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/cycle-accurate-simulation.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FlexRIO devices support cycle-accurate simulation to aid in debugging your FPGA. Cycle-accurate simulation means that timing is precise, which allows for clock-by-clock analysis before the LabVIEW FPGA design is compiled to a bitstream. Cycle-accurate simulation can improve design quality and save d

### Cycle-Accurate Simulation

FlexRIO devices support cycle-accurate simulation to aid in debugging your FPGA. Cycle-accurate simulation means that timing is precise, which allows for clock-by-clock analysis before the LabVIEW FPGA design is compiled to a bitstream. Cycle-accurate simulation can improve design quality and save development time. This topic describes the aspects of cycle-accurate simulation that are specific to FlexRIO devices.

To decrease cycle-accurate simulation compilation and execution times, FlexRIO devices use cycle-accurate simulation as their model fidelity. Cycle-accurate simulation timing is exactly the same as hardware timing, but the VHDL code is different than the code that the driver software implements on the target. For example, the onboard DRAM and corresponding DRAM controller on a FlexRIO device are both abstracted into a simulation model for cycle-accurate simulation. This abstraction means that the absolute delays may not match between simulation and actual execution, but the functional behavior is identical.

#### FPGA I/O Items

Cycle-accurate simulation can simulate all the FPGA I/O items for your FlexRIO device
 including PXI/PXI Express items, IO Module Status items, and Board IO items. In
 simulation, static values are provided as defaults for some FPGA I/O items. All
 other FPGA I/O items do not have default values. The following table lists the
 default values of some FPGA I/O items used in simulation.

| FPGA I/O Item | Default Value |
| --- | --- |
| IO Module Present | TRUE |
| IO Module Power Good | TRUE |
| IO Module Power Enabled | TRUE |
| EEPROM Power Enabled | TRUE |
| IO Module IO Enabled | TRUE |
| Expected IO Module ID | Matches expected ID of the currently configured FlexRIO adapter module |
| Inserted IO Module ID | Matches expected ID of the currently configured FlexRIO adapter module |
| Device Temperature | 25 °C (b0000000001100100, 1 LSB = 0.25 °C) |
| Clock100 PLL Unlocked | FALSE (PXI Express devices only) |

If you want to simulate something other than the default value, you can override
 these values by connecting your own stimulus inside the test bench.

Note

Clock100 PLL Unlocked

#### Adapter Module Signals

To communicate with your adapter module, your FlexRIO FPGA module provides 66
 general-purpose I/O (GPIO) signals and four clock signals (two Global clocks and IO
 Module Clock 0/1). You can configure these signals as you normally would in LabVIEW
 FPGA or with a stimulus model. If you configure these signals normally, refer to
 your adapter module documentation for information about how these signals and clocks
 work in your FlexRIO system. If you have a stimulus model for your FlexRIO adapter
 module, you can instantiate it in your test bench to imitate the functionality of
 your FlexRIO adapter module.

Note

Note

2

#### DRAM

Cycle-accurate simulation supports DRAM functionality for FlexRIO devices that have onboard DRAM, but it limits the DRAM to a maximum of 1 MB. The following devices do not have onboard DRAM:

- NI PXI-7951R
- NI PXIe-7961R
- NI PXIe-7971R

Parent topic:

Programming with FlexRIO

Related information:

- Debugging FPGA VIs Using a Third-Party Simulator (FPGA
 Module)
- Model Fidelity Page (Simulation Export Properties Dialog
 Box)

<!--NI_TOPIC bundle=flexrio path=cycle-accurate-simulation_2.html language=enus -->
## TOPIC 00024: Cycle-Accurate Simulation

- bundle_id: `flexrio`
- source_path: `cycle-accurate-simulation_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/cycle-accurate-simulation_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FlexRIO devices support cycle-accurate simulation to aid in debugging your FPGA. Cycle-accurate simulation means that timing is precise, which allows for clock-by-clock analysis before the LabVIEW FPGA design is compiled to a bitstream. Cycle-accurate simulation can improve design quality and save d

### Cycle-Accurate Simulation

FlexRIO devices support cycle-accurate simulation to aid in debugging your FPGA. Cycle-accurate simulation means that timing is precise, which allows for clock-by-clock analysis before the LabVIEW FPGA design is compiled to a bitstream. Cycle-accurate simulation can improve design quality and save development time. This topic describes the aspects of cycle-accurate simulation that are specific to FlexRIO devices.

To decrease cycle-accurate simulation compilation and execution times, FlexRIO devices use cycle-accurate simulation as their model fidelity. Cycle-accurate simulation timing is exactly the same as hardware timing, but the VHDL code is different than the code that the driver software implements on the target. For example, the onboard DRAM and corresponding DRAM controller on a FlexRIO device are both abstracted into a simulation model for cycle-accurate simulation. This abstraction means that the absolute delays may not match between simulation and actual execution, but the functional behavior is identical.

#### FPGA I/O Items

Cycle-accurate simulation can simulate all the FPGA I/O items for your FlexRIO device
 including PXI/PXI Express items, IO Module Status items, and Board IO items. In
 simulation, static values are provided as defaults for some FPGA I/O items. All
 other FPGA I/O items do not have default values. The following table lists the
 default values of some FPGA I/O items used in simulation.

| FPGA I/O Item | Default Value |
| --- | --- |
| IO Module Present | TRUE |
| IO Module Power Good | TRUE |
| IO Module Power Enabled | TRUE |
| EEPROM Power Enabled | TRUE |
| IO Module IO Enabled | TRUE |
| Expected IO Module ID | Matches expected ID of the currently configured FlexRIO adapter module |
| Inserted IO Module ID | Matches expected ID of the currently configured FlexRIO adapter module |
| Device Temperature | 25 °C (b0000000001100100, 1 LSB = 0.25 °C) |
| Clock100 PLL Unlocked | FALSE (PXI Express devices only) |

If you want to simulate something other than the default value, you can override
 these values by connecting your own stimulus inside the test bench.

Note

Clock100 PLL Unlocked

#### Adapter Module Signals

To communicate with your adapter module, your FlexRIO FPGA module provides 66
 general-purpose I/O (GPIO) signals and four clock signals (two Global clocks and IO
 Module Clock 0/1). You can configure these signals as you normally would in LabVIEW
 FPGA or with a stimulus model. If you configure these signals normally, refer to
 your adapter module documentation for information about how these signals and clocks
 work in your FlexRIO system. If you have a stimulus model for your FlexRIO adapter
 module, you can instantiate it in your test bench to imitate the functionality of
 your FlexRIO adapter module.

Note

Note

2

#### DRAM

Cycle-accurate simulation supports DRAM functionality for FlexRIO devices that have onboard DRAM, but it limits the DRAM to a maximum of 1 MB. The following devices do not have onboard DRAM:

- NI PXI-7951R
- NI PXIe-7961R
- NI PXIe-7971R

Parent topic:

Programming with FlexRIO

<!--NI_TOPIC bundle=flexrio path=data-manipulation-overview.html language=enus -->
## TOPIC 00025: Data Manipulation Overview

- bundle_id: `flexrio`
- source_path: `data-manipulation-overview.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/data-manipulation-overview.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this instrument design library to manipulate and allocate arrays on the host. This library contains IP for deinterleaving, scaling, and copying arrays, and can optionally perform these operations after typecasting the input array to a larger data type. This typecast functionality can be useful w

### Data Manipulation Overview

Use this instrument design library to manipulate and allocate arrays on the host. This library contains IP for deinterleaving, scaling, and copying arrays, and can optionally perform these operations after typecasting the input array to a larger data type. This typecast functionality can be useful when transferring different data types through a single Target to Host FIFO type. For example, some applications will stream 16-bit or 32-bit integer array data through an 8-bit integer target to the host FIFO and use this library to typecast and scale the data to a floating point array. The implementation of this library is optimized to reduce data copies and maximize throughput.

This instrument design library is particularly useful in streaming applications that require high performance and efficient use of host memory.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=data-manipulation-overview_2.html language=enus -->
## TOPIC 00026: Data Manipulation Overview

- bundle_id: `flexrio`
- source_path: `data-manipulation-overview_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/data-manipulation-overview_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this instrument design library to manipulate and allocate arrays on the host. This library contains IP for deinterleaving, scaling, and copying arrays, and can optionally perform these operations after typecasting the input array to a larger data type. This typecast functionality can be useful w

### Data Manipulation Overview

Use this instrument design library to manipulate and allocate arrays on the host. This library contains IP for deinterleaving, scaling, and copying arrays, and can optionally perform these operations after typecasting the input array to a larger data type. This typecast functionality can be useful when transferring different data types through a single Target to Host FIFO type. For example, some applications will stream 16-bit or 32-bit integer array data through an 8-bit integer target to the host FIFO and use this library to typecast and scale the data to a floating point array. The implementation of this library is optimized to reduce data copies and maximize throughput.

This instrument design library is particularly useful in streaming applications that require high performance and efficient use of host memory.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=data-trigger-overview.html language=enus -->
## TOPIC 00027: Data Trigger Overview

- bundle_id: `flexrio`
- source_path: `data-trigger-overview.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/data-trigger-overview.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This instrument design library can be used to generate a trigger on an input signal under various conditions. The triggers produced by this library are typically consumed by the acquisition block in order to determine when to start and stop acquiring data. This library supports multiple trigger type

### Data Trigger Overview

This instrument design library can be used to generate a trigger on an input signal under various conditions. The triggers produced by this library are typically consumed by the acquisition block in order to determine when to start and stop acquiring data.

This library supports multiple trigger types. For more information on supported triggers and their use, refer to the LabVIEW context help for the Data Trigger VIs or to Data Trigger FPGA VIs.

This library supports various data types and samples per cycle.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=data-trigger-overview_2.html language=enus -->
## TOPIC 00028: Data Trigger Overview

- bundle_id: `flexrio`
- source_path: `data-trigger-overview_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/data-trigger-overview_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This instrument design library can be used to generate a trigger on an input signal under various conditions. The triggers produced by this library are typically consumed by the acquisition block in order to determine when to start and stop acquiring data. This library supports multiple trigger type

### Data Trigger Overview

This instrument design library can be used to generate a trigger on an input signal under various conditions. The triggers produced by this library are typically consumed by the acquisition block in order to determine when to start and stop acquiring data.

This library supports multiple trigger types. For more information on supported triggers and their use, refer to the LabVIEW context help for the Data Trigger VIs or to Data Trigger FPGA VIs.

This library supports various data types and samples per cycle.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=determining-which-version-of-flexrio-adapter.html language=enus -->
## TOPIC 00029: Determining Which Version of FlexRIO Adapter Module Support Is Installed On Your Computer

- bundle_id: `flexrio`
- source_path: `determining-which-version-of-flexrio-adapter.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/determining-which-version-of-flexrio-adapter.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To check the version of FlexRIO Adapter Module Support installed on your computer, select Start»Control Panel»Programs and Features»National Instruments Software. The version of FlexRIO Adapter Module Support installed on your computer is listed under the Products tab.

### Determining Which Version of FlexRIO Adapter Module Support Is Installed On Your Computer

To check the version of FlexRIO Adapter Module Support installed on your computer, select Start»Control Panel»Programs and Features»National Instruments Software. The version of FlexRIO Adapter Module Support installed on your computer is listed under the Products tab.

Parent topic:

FlexRIO Adapter Module Support

<!--NI_TOPIC bundle=flexrio path=determining-which-version-of-flexrio-support.html language=enus -->
## TOPIC 00030: Determining Which Version of FlexRIO Support Is Installed On Your Computer

- bundle_id: `flexrio`
- source_path: `determining-which-version-of-flexrio-support.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/determining-which-version-of-flexrio-support.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To check the version of FlexRIO Support installed on your computer, select Start»Control Panel»Programs and Features»National Instruments Software. The version of FlexRIO Support installed on your computer is listed under the Products tab.

### Determining Which Version of FlexRIO Support Is Installed On Your Computer

To check the version of FlexRIO Support installed on your computer, select Start»Control Panel»Programs and Features»National Instruments Software. The version of FlexRIO Support installed on your computer is listed under the Products tab.

Parent topic:

Getting Started with FlexRIO

<!--NI_TOPIC bundle=flexrio path=digital-signal-processing-dsp-overview.html language=enus -->
## TOPIC 00031: Digital Signal Processing (DSP) Overview

- bundle_id: `flexrio`
- source_path: `digital-signal-processing-dsp-overview.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/digital-signal-processing-dsp-overview.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this instrument design library to digitally process I/Q data. This instrument design library contains LabVIEW FPGA VIs. These VIs contain functionality that is typically found in digital downconverters (DDCs) and digital upconverters (DUCs). These VIs also perform DSP for the digital correction

### Digital Signal Processing (DSP) Overview

Use this instrument design library to digitally process I/Q data. This instrument design library contains LabVIEW FPGA VIs. These VIs contain functionality that is typically found in digital downconverters (DDCs) and digital upconverters (DUCs). These VIs also perform DSP for the digital correction of analog imperfections in the system. For devices that support two samples per cycle, you can configure this instrument design library to process two I/Q data samples per cycle. You can use this instrument design library to perform the following functions:

#### DDC and DUC Functionality

- Fractional Decimation —Decimates the I/Q data rate with a high frequency and phase resolution, using an FIR filter.
- Fractional Interpolation —Interpolates the I/Q data with a high frequency and phase resolution, using an FIR filter.
- Frequency Shift —Applies a digital frequency shift to the I/Q data.

#### Digital Correction Functionality

- Digital Gain —Digitally controls the I and Q signal amplitudes.
- Digital Offset —Digitally controls the I and Q signal offsets.
- Equalization —Filters the I/Q data to equalize the analog response of a device.
- I/Q Impairments —Modifies the I/Q data to correct or apply I/Q impairments, such as gain imbalance, quadrature skew, or DC offset.

This instrument design library also includes the Power Level Trigger VI and several data type conversion VIs. Data type conversion VIs simplify the interfacing between instrument design VIs and FPGA I/O nodes. Refer to the LabVIEW context help of the DSP VIs for more detailed information about the library interface.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=digital-signal-processing-dsp-overview_2.html language=enus -->
## TOPIC 00032: Digital Signal Processing (DSP) Overview

- bundle_id: `flexrio`
- source_path: `digital-signal-processing-dsp-overview_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/digital-signal-processing-dsp-overview_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this instrument design library to digitally process I/Q data. This instrument design library contains LabVIEW FPGA VIs. These VIs contain functionality that is typically found in digital downconverters (DDCs) and digital upconverters (DUCs). These VIs also perform DSP for the digital correction

### Digital Signal Processing (DSP) Overview

Use this instrument design library to digitally process I/Q data. This instrument design library contains LabVIEW FPGA VIs. These VIs contain functionality that is typically found in digital downconverters (DDCs) and digital upconverters (DUCs). These VIs also perform DSP for the digital correction of analog imperfections in the system. For devices that support two samples per cycle, you can configure this instrument design library to process two I/Q data samples per cycle. You can use this instrument design library to perform the following functions:

#### DDC and DUC Functionality

- Fractional Decimation —Decimates the I/Q data rate with a high frequency and phase resolution, using an FIR filter.
- Fractional Interpolation —Interpolates the I/Q data with a high frequency and phase resolution, using an FIR filter.
- Frequency Shift —Applies a digital frequency shift to the I/Q data.

#### Digital Correction Functionality

- Digital Gain —Digitally controls the I and Q signal amplitudes.
- Digital Offset —Digitally controls the I and Q signal offsets.
- Equalization —Filters the I/Q data to equalize the analog response of a device.
- I/Q Impairments —Modifies the I/Q data to correct or apply I/Q impairments, such as gain imbalance, quadrature skew, or DC offset.

This instrument design library also includes the Power Level Trigger VI and several data type conversion VIs. Data type conversion VIs simplify the interfacing between instrument design VIs and FPGA I/O nodes. Refer to the LabVIEW context help of the DSP VIs for more detailed information about the library interface.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=dma-streaming.html language=enus -->
## TOPIC 00033: DMA Streaming

- bundle_id: `flexrio`
- source_path: `dma-streaming.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/dma-streaming.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FlexRIO with Integrated I/O modules support both host-to-target streaming and target-to-host streaming through DMA channels that connect the host to your target. Use DMA streaming to allow the maximum throughput of data from your host application to be streamed to the target at high rates of spe

### DMA Streaming

The FlexRIO with Integrated I/O modules support both host-to-target streaming and target-to-host streaming
through DMA channels that connect the host to your target. Use DMA streaming to allow the
maximum throughput of data from your host application to be streamed to the target at high rates
of speed.

The PXI FlexRIO Integrated I/O modules provide up to 60 DMA channels that can be accessed by your
host. These channels can be used in a variety of ways to meet the needs of your application. The total
overall bandwidth of the module limits your DMA use, whether you use 1 DMA channel or 60.

The maximum width of a DMA channel is 256 bits. To use the full width of the DMA channel
to achieve maximum throughput, you can write an array of U64 elements into the DMA FIFO
and configure the FIFO for multi-element read/write (four elements per read/write) to satisfy the
256 bit width. You can also write up to 1024 bits at a time from LabVIEW FPGA, and the Ready
for Input connection throttles the connection to the FIFO to prevent overflow.

Theoretically, DMA throughput is maximized and is most consistent when the DMA FIFO
buffer is sized as large as possible to absorb variations in the readiness of the host memory.
However, sizing the FIFO larger consumes block RAM resources on the FPGA and increases
the timing pressure on the FIFO. In order to sustain throughput through the PCIe bus to and from
host memory, make the FIFO as large as you can
successfully compile with. You can change the size of the FIFO by configuring the Requested Number of
Elements for the FIFO in the project properties. You can validate the DMA sizing through
benchmarking, and you can use VIs in the Streaming Design Library to monitor the health
of a FIFO.

For more detailed information about using DMA, DMA best practices, and how to make design decisions on how to implement DMA in your application, refer to the Transferring Data Using Direct Memory Access topic in the *LabVIEW FPGA Module User Manual*.

Parent topic:

LabVIEW and System Integration

Related information:

- LabVIEW FPGA Module User Manual

<!--NI_TOPIC bundle=flexrio path=dma-throughput.html language=enus -->
## TOPIC 00034: DMA Throughput

- bundle_id: `flexrio`
- source_path: `dma-throughput.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/dma-throughput.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Total throughput depends on the SCTL rate from the FPGA that is reading or writing the DMA channels. The data throughput is calculated by the following equation: (Data Width × Samples per Cycle) × Number of DMA FIFOs × SCTL Clock Rate = Data Throughput The total data throughput cannot exceed the max

### DMA Throughput

Total throughput depends on the SCTL rate from the FPGA that is reading or writing the DMA
channels. The data throughput is calculated by the following equation:

(Data Width × Samples per Cycle) × Number of DMA FIFOs × SCTL Clock Rate
= Data Throughput

The total data throughput cannot exceed the maximum data specification for
your module. Refer to the specifications document for your module for information
about data throughput limits.

Some remote controlling PCs and PXI Express chassis have slot bandwidth
restrictions that may limit the maximum throughput of your application. Refer to the
controller and chassis specifications for more information.

The number of array elements fed into the DMA FIFO from the Host can limit
the maximum throughput for your application. Use large array subsets and set your
FIFO depths to be deep enough to sustain high throughput.

For more detailed information about using DMA, DMA best practices, and how to make design
 decisions on how to implement DMA in your application, refer to the *Transferring
 Data Using Direct Memory
 Access*
 topic in the *LabVIEW FPGA Module User Manual*.

Parent topic:

LabVIEW and System Integration

Related information:

- Transferring Data Using Direct Memory Access (FPGA
 Module)

<!--NI_TOPIC bundle=flexrio path=download-reset-and-run-side-effects-in-the-la.html language=enus -->
## TOPIC 00035: Download, Reset, and Run Side Effects in the LabVIEW FPGA Host Interface

- bundle_id: `flexrio`
- source_path: `download-reset-and-run-side-effects-in-the-la.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/download-reset-and-run-side-effects-in-the-la.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: When the FPGA on your FlexRIO module loads, it performs a power-on self-configuration sequence that configures various on-board hardware. This configuration occurs at the following times: At device power-up after the bitfile loads. At the first time Run.vi is called after a new bitfile is downloaded

### Download, Reset, and Run Side Effects in the LabVIEW FPGA Host Interface

When the FPGA on your FlexRIO module loads, it performs a power-on self-configuration
sequence that configures various on-board hardware. This configuration occurs at the following
times:

- At device power-up after the bitfile loads.
- At the first time Run.vi is called after a new bitfile is downloaded and the bitfile is not set to
 Run on Load .
- When Run.vi is called after Reset.vi .

When self-configuration executes, the clocking configuration enters an
 indeterminate state. When the clocking configuration is in an indeterminate state,
 you cannot rely on clocking stability from the clocking and routing hardware on your module.

For more information about Run, Reset, and other Invoke methods, refer to the *LabVIEW FPGA
 Module User Manual*.

Parent topic:

LabVIEW and System Integration

Related information:

- LabVIEW FPGA Module User Manual

<!--NI_TOPIC bundle=flexrio path=dram-fifo-overview.html language=enus -->
## TOPIC 00036: DRAM FIFO Overview

- bundle_id: `flexrio`
- source_path: `dram-fifo-overview.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/dram-fifo-overview.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This Instrument Design Library contains elements useful for implementing a FIFO using DRAM. VI Description Create Resource Creates a reference to a DRAM FIFO. Select the instance that corresponds to the data width of the DRAM being accessed. Write Enqueues a Boolean array in the To DRAM Queue. Read

### DRAM FIFO Overview

This Instrument Design Library contains elements useful for implementing a FIFO using DRAM.

[IMAGE alt='image' src='GUID-ADAC7827-007E-4201-8AE2-79C367D1602C-a5.gif']

| VI | Description |
| --- | --- |
| Create Resource | Creates a reference to a DRAM FIFO. Select the instance that corresponds to the data width of the DRAM being accessed. |
| Write | Enqueues a Boolean array in the To DRAM Queue. |
| Read | Dequeues an element from the From DRAM Queue. |
| Process | Manages the transfer of enqueued elements to and from the DRAM. |
| Packer | Accepts an array of elements and packs them into a Boolean array equal in size to the data width of the DRAM. |
| Unpacker | Accepts a Boolean array and unpacks them into an array of elements of specified size and data type. |

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=dram-fifo-overview_2.html language=enus -->
## TOPIC 00037: DRAM FIFO Overview

- bundle_id: `flexrio`
- source_path: `dram-fifo-overview_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/dram-fifo-overview_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This Instrument Design Library contains elements useful for implementing a FIFO using DRAM. VI Description Create Resource Creates a reference to a DRAM FIFO. Select the instance that corresponds to the data width of the DRAM being accessed. Write Enqueues a Boolean array in the To DRAM Queue. Read

### DRAM FIFO Overview

This Instrument Design Library contains elements useful for implementing a FIFO using DRAM.

[IMAGE alt='image' src='GUID-ADAC7827-007E-4201-8AE2-79C367D1602C-a5.gif']

| VI | Description |
| --- | --- |
| Create Resource | Creates a reference to a DRAM FIFO. Select the instance that corresponds to the data width of the DRAM being accessed. |
| Write | Enqueues a Boolean array in the To DRAM Queue. |
| Read | Dequeues an element from the From DRAM Queue. |
| Process | Manages the transfer of enqueued elements to and from the DRAM. |
| Packer | Accepts an array of elements and packs them into a Boolean array equal in size to the data width of the DRAM. |
| Unpacker | Accepts a Boolean array and unpacks them into an array of elements of specified size and data type. |

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=dram-interfaces.html language=enus -->
## TOPIC 00038: DRAM Interfaces

- bundle_id: `flexrio`
- source_path: `dram-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/dram-interfaces.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some FlexRIO devices contain onboard DRAM that is directly accessible from the FPGA VI. LabVIEW supports two types of DRAM interfaces: FPGA memory items and socketed CLIP. You cannot use both FPGA memory items and socketed CLIP to access the same DRAM bank in an FPGA VI. Refer to your FPGA device's

### DRAM Interfaces

Some FlexRIO devices contain onboard DRAM that is directly accessible from the FPGA VI. LabVIEW supports two types of DRAM interfaces: FPGA memory items and socketed CLIP. You cannot use both FPGA memory items and socketed CLIP to access the same DRAM bank in an FPGA VI. Refer to your FPGA device's Specifications document to determine the available amount of onboard DRAM for your device.

#### Configuring DRAM

Refer to the following topics for information about configuring the DRAM for your
 FlexRIO device.

- Configuring DRAM with FPGA Memory Items
- Configuring DRAM with Socketed CLIP

For tips on how to use DRAM effectively in FlexRIO, refer to the *Using DRAM
 Effectively with FlexRIO* tutorial.

#### Disabling Synchronization
 Registers

The DRAM interface signals are synchronous to the DRAM interface clock.
 Synchronization registers cause a delay in sending and receiving data or commands to
 and from the DRAM interface. For proper device operation, you must disable all
 synchronization
 registers
 for all DRAM interface signals and all input signals.

Note

Right-click a DRAM interface signal and select Properties from
 the shortcut menu to open the FPGA I/O Properties dialog box.
 Select Advanced Code Generation in the
 Category list to open the Advanced Code
 Generation page. Select 0 in the
 Number of Synchronizing Registers for Output Data box to
 disable all synchronization registers for that signal. Always disable
 synchronization registers for synchronous interfaces when proper operation depends
 on no latency.

Related concepts:

- Configuring DRAM with FPGA Memory Items
- Configuring DRAM with Socketed CLIP
- Using DRAM Effectively with FlexRIO

<!--NI_TOPIC bundle=flexrio path=dram-memory-interface.html language=enus -->
## TOPIC 00039: DRAM Memory Interface

- bundle_id: `flexrio`
- source_path: `dram-memory-interface.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/dram-memory-interface.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FlexRIO devices have different memory interfaces that provide access to the external DRAM memory. When you enable the DRAM memory bank in the DRAM General Properties dialog box, any compatible memory interfaces are automatically displayed in the Memory Interface window. The following table lists all

### DRAM Memory Interface

FlexRIO devices have different memory interfaces that provide access to the external DRAM memory. When you enable the DRAM memory bank in the DRAM General Properties dialog box, any compatible memory interfaces are automatically displayed in the Memory Interface window.

The following table lists all the NI-developed memory interfaces that are compatible with the external DRAM memory banks on FlexRIO devices, and it also gives a basic overview of their functionality.

| Memory Interface Name | Memory Interface Description |
| --- | --- |
| Random Access - 64 Bit | Provides a high-performance random access interface to external memory. Use this interface for maximum performance or if you require a random access-based memory interface. The data port is 64 bits wide. This memory interface is supported only on FlexRIO PXI devices (NI PXI-795x). |
| FIFO - 64 Bit | Provides a FIFO-based interface to external memory. When using this memory interface, the entire memory bank is treated as a large FIFO. Use this interface if your throughput application requires a straightforward, FIFO-based memory interface. The data port is 64 bits wide. This memory interface is supported only on FlexRIO PXI devices (NI PXI-795x). |
| Random Access - 128 Bit | Provides a high-performance random access interface to external memory. Use this for maximum performance or if you require a random access-based memory interface. The data port is 128 bits wide. This memory interface is supported only on FlexRIO PXI Express devices (NI PXIe-796x and NI 797xR). |
| FIFO - 128 Bit | Provides a FIFO-based interface to external memory. When using this memory interface, the entire memory bank is treated as a large FIFO. Use this interface if your throughput application requires a straightforward, FIFO-based memory interface. The data port is 128 bits wide. This memory interface is supported only on FlexRIO PXI Express devices (NI PXIe-796x and NI 797xR). |

Parent topic:

Configuring DRAM with Socketed CLIP

Related concepts:

- Random Access - 64 Bit Memory Interface
- FIFO - 64 Bit Memory Interface
- Random Access - 128 Bit Memory Interface
- FIFO - 128 Bit Memory Interface

<!--NI_TOPIC bundle=flexrio path=fifo-128-bit-memory-interface.html language=enus -->
## TOPIC 00040: FIFO - 128 Bit Memory Interface

- bundle_id: `flexrio`
- source_path: `fifo-128-bit-memory-interface.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/fifo-128-bit-memory-interface.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This memory interface provides the easiest-to-use FIFO interface to external DRAM. The FIFO is exposed as separate read and write interfaces. Both the write-side and read-side data ports are 128-bit data words. Signals for Writing to the FIFO The following table lists the write-side I/O provided by

### FIFO - 128 Bit Memory Interface

This memory interface provides the easiest-to-use FIFO interface to external DRAM. The FIFO is exposed as separate read and write interfaces. Both the write-side and read-side data ports are 128-bit data words.

#### Signals for Writing to the FIFO

The following table lists the write-side I/O provided by the FIFO - 128 Bit memory interface.

| Memory Interface I/O | Data Type | To Memory/From Memory | Description |
| --- | --- | --- | --- |
| Full | Bool | From memory | TRUE = Indicates that the FIFO is full and that no data can be written to it. FALSE = Indicates that the FIFO is not full and that data can written to it. |
| Write_Data_Upper | U64 | To memory | Sets the upper 64 bits of the data to write into the FIFO. |
| Write_Data_Lower | U64 | To memory | Sets the lower 64 bits of the data to write into the FIFO. |
| Write | Bool | To memory | TRUE = Transfers data from the Write_Data_Upper and Write_Data_Lower signals into the FIFO. FALSE = Transfers no data to the FIFO. Note Do not set the Write signal to TRUE when the Full signal is TRUE. |

#### Signals for Reading from the
 FIFO

The following table lists the read-side I/O provided by the FIFO - 128 Bit memory
 interface.

| Memory Interface I/O | Data Type | To Memory/From Memory | Description |
| --- | --- | --- | --- |
| Data_Available | Bool | From memory | TRUE = Indicates that the values in the Read_Data_Upper and Read_Data_Lower signals are valid and may be read. FALSE = Indicates that the values in the Read_Data_Upper and Read_Data_Lower signals are invalid and may not be read yet. |
| Read_Data_Upper | U64 | From memory | Displays the upper 64 bits of the data to read from the FIFO. This signal is valid only when the Data_Available signal is TRUE. |
| Read_Data_Lower | U64 | From memory | Displays the lower 64 bits of the data to read from the FIFO. This signal is valid only when the Data_Available signal is TRUE. |
| Read | Bool | To memory | TRUE = Reads data from the Read_Data_Upper and Read_Data_Lower signals out of the FIFO. FALSE = Does not read any data from the FIFO. Note Do not set the Read signal to TRUE when the Data_Available signal is FALSE. |

The write-side interface Full signal is TRUE when data cannot be
 added into the FIFO. If the Full signal is low, you can write data
 into the FIFO by driving the Write_Data_Upper and
 Write_Data_Lower signals with your data and setting the
 Write signal to TRUE. Do not set the Write
 signal to TRUE when Full is TRUE because this condition leads to
 undefined behavior.

When read-side data on the Read_Data_Upper and
 Read_Data_Lower lines is available to be read, the
 Data_Available signal is TRUE. After this data is read, set the
 Read signal to TRUE. Do not set the Read
 signal to TRUE when Data_Available is FALSE because this condition
 leads to undefined behavior.

The FIFO - 128 Bit memory interface requires you to define the clock domains of the
 single-cycle Timed Loop from which the read-side and write-side interfaces are
 accessed. Configure these interfaces using the Clock
 Selections property page for the corresponding DRAM bank item in the
 LabVIEW project. Configure the Input_Clock signal to be driven with
 the LabVIEW FPGA clock resource which you are using to clock the single-cycle Timed
 Loop
 that is accessing the write-side interface. Likewise, configure the
 Output_Clock signal to be driven with the LabVIEW FPGA clock
 resource that you are using to clock the single-cycle Timed Loop that is accessing
 the read-side interface.

Note

Note

must

0

Note

The FIFO - 128 Bit memory interface is designed to simultaneously read and write data
 at speeds up to 40 MHz. It is possible to run the interface up to 200 MHz. However,
 at speeds greater than 40 MHz, the Full and
 Data_Available signals may temporarily become TRUE and FALSE,
 respectively.

LabVIEW contains example VIs that read and write to the FIFO - 128 Bit memory
 interface. To access the NI Example Finder, open LabVIEW and select
 Help»Find Examples, then select Hardware Input
 and Output»FlexRIO. You can also access device-specific examples by
 selecting Add device from the Hardware
 pull-down menu in the NI Example Finder.

Parent topic:

DRAM Memory Interface

<!--NI_TOPIC bundle=flexrio path=fifo-64-bit-memory-interface.html language=enus -->
## TOPIC 00041: FIFO - 64 Bit Memory Interface

- bundle_id: `flexrio`
- source_path: `fifo-64-bit-memory-interface.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/fifo-64-bit-memory-interface.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This memory interface provides the easiest-to-use FIFO interface to external DRAM. The FIFO is exposed as separate read and write interfaces. Both the write-side and read-side data ports are 64-bit data words. Signals for Writing to the FIFO The following table lists the write-side I/O provided by t

### FIFO - 64 Bit Memory Interface

This memory interface provides the easiest-to-use FIFO interface to external DRAM. The FIFO is exposed as separate read and write interfaces. Both the write-side and read-side data ports are 64-bit data words.

#### Signals for Writing to the FIFO

The following table lists the write-side I/O provided by the FIFO - 64 Bit memory interface.

| Memory Interface I/O | Data Type | To Memory/From Memory | Description |
| --- | --- | --- | --- |
| Full | Bool | From memory | TRUE = Indicates that the FIFO is full and that no data can be written to it. FALSE = Indicates that the FIFO is not full and that data can written to it. |
| Write_Data_Upper | U32 | To memory | Sets the upper 32 bits of the data to write into the FIFO. |
| Write_Data_Lower | U32 | To memory | Sets the lower 32 bits of the data to write into the FIFO. |
| Write | Bool | To memory | TRUE = Transfers data from the Write_Data_Upper and Write_Data_Lower signals into the FIFO. FALSE = Transfers no data to the FIFO. Note Do not set the Write signal to TRUE when the Full signal is TRUE. |

#### Signals for Reading from the
 FIFO

The following table lists the read-side I/O provided by the FIFO - 64 Bit memory
 interface.

| Memory Interface I/O | Data Type | To Memory/From Memory | Description |
| --- | --- | --- | --- |
| Data_Available | Bool | From memory | TRUE = Indicates that the values in the Read_Data_Upper and Read_Data_Lower signals are valid and may be read. FALSE = Indicates that the values in the Read_Data_Upper and Read_Data_Lower signals are invalid and may not be read yet. |
| Read_Data_Upper | U32 | From memory | Displays the upper 32 bits of the data to read from the FIFO. This signal is valid only when the Data_Available signal is TRUE. |
| Read_Data_Lower | U32 | From memory | Displays the lower 32 bits of the data to read from the FIFO. This signal is valid only when the Data_Available signal is TRUE. |
| Read | Bool | To memory | TRUE = Reads data from the Read_Data_Upper and Read_Data_Lower signals out of the FIFO. FALSE = Does not read any data from the FIFO. Note Do not set the Read signal to TRUE when the Data_Available signal is FALSE. |

The write-side interface Full signal is TRUE when data cannot be
 added into the FIFO. If the Full signal is low, you can write data
 into the FIFO by driving the Write_Data_Upper and
 Write_Data_Lower signals with your data and setting the
 Write signal to TRUE. Do not set the Write
 signal to TRUE when Full is TRUE because this condition leads to
 undefined behavior.

When read-side data on the Read_Data_Upper and
 Read_Data_Lower lines is available to be read, the
 Data_Available signal is TRUE. After this data is read, set the
 Read signal to TRUE. Do not set the Read
 signal to TRUE when Data_Available is FALSE because this condition
 leads to undefined behavior.

The FIFO - 64 Bit memory interface requires you to define the clock domains of the
 single-cycle Timed Loop from which the read-side and write-side interfaces are
 accessed. Configure these interfaces using the Clock
 Selections property page for the corresponding DRAM bank item in the
 LabVIEW project. Configure the Input_Clock signal to be driven with
 the LabVIEW FPGA clock resource which you are using to clock the single-cycle Timed
 Loop
 that is accessing the write-side interface. Likewise, configure the
 Output_Clock signal to be driven with the LabVIEW FPGA clock
 resource that you are using to clock the single-cycle Timed Loop that is accessing
 the read-side interface.

Note

Note

must

0

Note

The FIFO - 64 Bit memory interface is designed to simultaneously read and write data
 at speeds up to 40 MHz. It is possible to run the interface up to 200 MHz. However,
 at speeds greater than 40 MHz, the Full and
 Data_Available signals may temporarily become TRUE and FALSE,
 respectively.

LabVIEW contains example VIs that read and write to the FIFO - 64 Bit memory
 interface. To access the NI Example Finder, open LabVIEW and select
 Help»Find Examples, then select Hardware Input
 and Output»FlexRIO. You can also access device-specific examples by
 selecting Add device from the Hardware
 pull-down menu in the NI Example Finder.

Parent topic:

DRAM Memory Interface

<!--NI_TOPIC bundle=flexrio path=fifo-register-bus-overview.html language=enus -->
## TOPIC 00042: FIFO Register Bus Overview

- bundle_id: `flexrio`
- source_path: `fifo-register-bus-overview.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/fifo-register-bus-overview.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the FIFO Register Bus instrument design library to send register read and write instructions from your application on the host to the Instruction Framework FPGA Network. Other instrument design libraries on the FPGA can define a set of registers, which can be added as an Address Space in the Ins

### FIFO Register Bus Overview

Use the FIFO Register Bus instrument design library to send register read and write instructions from your application on the host to the Instruction Framework FPGA Network. Other instrument design libraries on the FPGA can define a set of registers, which can be added as an Address Space in the Instruction Framework FPGA Network. By using DMA to transfer data, the FIFO Register Bus library provides a significant performance benefit when you need to quickly issue a large number of register writes.

You can use multiple instances of the FIFO Register Bus instrument design library in your FPGA application. Using multiple instances of the FIFO Register Bus is useful in applications where independent components each send register instructions to the FPGA because each FIFO Register Bus instance has a separate DMA FIFO for data transfer. Different instances of the FIFO Register Bus can send register instructions to the same instrument design library on the FPGA. The Instruction Framework FPGA Network will automatically arbitrate among register instructions with the same destination and then route a completed read instruction to the instance of the FIFO Register Bus that issued it.

This instrument design library includes host VIs and FPGA VIs. For each instance of the FIFO Register Bus, the host writes register instructions into a Host to Target DMA FIFO. The FPGA reads a register instruction from the DMA FIFO, decodes it, and sends it to the Instruction Framework FPGA Network. The FPGA waits for the current register instruction to be processed before decoding and sending the next register instruction.

#### Thread Safety

#### Unsupported

[IMAGE alt='image' src='GUID-C3F9262D-66B1-4111-AA70-568602DA7864-a5.gif']

The FIFO Register Bus does not support opening multiple sessions to the same instance.

#### Supported

[IMAGE alt='image' src='GUID-B2CF5E03-C25E-47C1-86DF-03EE25750E22-a5.gif']

You may branch the wire of a FIFO Register Bus session, and calls to the session will be thread-safe.

#### Supported

[IMAGE alt='image' src='GUID-672EBBE5-FBAB-4400-BE6C-23C53332EEA2-a5.gif']

You may open multiple sessions if they are targeted towards different bus
 instances.

For more detailed information about the library interface, refer to the LabVIEW
 context help of the FIFO Register Bus LabVIEW VIs.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

Related concepts:

- Instruction Framework Overview

<!--NI_TOPIC bundle=flexrio path=fifo-register-bus-overview_2.html language=enus -->
## TOPIC 00043: FIFO Register Bus Overview

- bundle_id: `flexrio`
- source_path: `fifo-register-bus-overview_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/fifo-register-bus-overview_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the FIFO Register Bus instrument design library to send register read and write instructions from your application on the host to the Instruction Framework FPGA Network. Other instrument design libraries on the FPGA can define a set of registers, which can be added as an Address Space in the Ins

### FIFO Register Bus Overview

Use the FIFO Register Bus instrument design library to send register read and write instructions from your application on the host to the Instruction Framework FPGA Network. Other instrument design libraries on the FPGA can define a set of registers, which can be added as an Address Space in the Instruction Framework FPGA Network. By using DMA to transfer data, the FIFO Register Bus library provides a significant performance benefit when you need to quickly issue a large number of register writes.

You can use multiple instances of the FIFO Register Bus instrument design library in your FPGA application. Using multiple instances of the FIFO Register Bus is useful in applications where independent components each send register instructions to the FPGA because each FIFO Register Bus instance has a separate DMA FIFO for data transfer. Different instances of the FIFO Register Bus can send register instructions to the same instrument design library on the FPGA. The Instruction Framework FPGA Network will automatically arbitrate among register instructions with the same destination and then route a completed read instruction to the instance of the FIFO Register Bus that issued it.

This instrument design library includes host VIs and FPGA VIs. For each instance of the FIFO Register Bus, the host writes register instructions into a Host to Target DMA FIFO. The FPGA reads a register instruction from the DMA FIFO, decodes it, and sends it to the Instruction Framework FPGA Network. The FPGA waits for the current register instruction to be processed before decoding and sending the next register instruction.

#### Thread Safety

#### Unsupported

[IMAGE alt='image' src='GUID-C3F9262D-66B1-4111-AA70-568602DA7864-a5.gif']

The FIFO Register Bus does not support opening multiple sessions to the same instance.

#### Supported

[IMAGE alt='image' src='GUID-B2CF5E03-C25E-47C1-86DF-03EE25750E22-a5.gif']

You may branch the wire of a FIFO Register Bus session, and calls to the session will be thread-safe.

#### Supported

[IMAGE alt='image' src='GUID-672EBBE5-FBAB-4400-BE6C-23C53332EEA2-a5.gif']

You may open multiple sessions if they are targeted towards different bus
 instances.

For more detailed information about the library interface, refer to the LabVIEW
 context help of the FIFO Register Bus LabVIEW VIs.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=flexrio-adapter-module-support.html language=enus -->
## TOPIC 00044: FlexRIO Adapter Module Support

- bundle_id: `flexrio`
- source_path: `flexrio-adapter-module-support.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/flexrio-adapter-module-support.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FlexRIO Adapter Module Support software provides NI-developed component-level intellectual property (CLIP) items as well as CLIP examples for use with your FlexRIO adapter module hardware. Learn how to configure your FlexRIO adapter module and its related CLIP items and how to use LabVIEW and th

### FlexRIO Adapter Module Support

The FlexRIO Adapter Module Support software provides NI-developed component-level intellectual property (CLIP) items as well as CLIP examples for use with your FlexRIO adapter module hardware.

Learn how to configure your FlexRIO adapter module and its related CLIP items and how to use
 LabVIEW and the LabVIEW FPGA Module with FlexRIO devices.

Parent topic:

FlexRIO with Modular I/O

<!--NI_TOPIC bundle=flexrio path=flexrio-fpga-invoke-methods.html language=enus -->
## TOPIC 00045: FlexRIO FPGA Invoke Methods

- bundle_id: `flexrio`
- source_path: `flexrio-fpga-invoke-methods.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/flexrio-fpga-invoke-methods.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to the standard invoke methods supported by the LabVIEW FPGA Module, FlexRIO targets also support custom FPGA invoke methods. Refer to the help topics in the API Reference for your device for more information about that device's custom invoke methods. NI-7931R NI-7932R NI-7935R PXI-7951R

### FlexRIO FPGA Invoke Methods

In addition to the standard invoke methods supported by the LabVIEW FPGA Module, FlexRIO targets also support custom FPGA invoke methods.

Refer to the help topics in the API Reference for your device for more information about that
 device's custom invoke methods.

- NI-7931R
- NI-7932R
- NI-7935R
- PXI-7951R
- PXI-7952R
- PXI-7953R
- PXI-7954R
- PXI-7961R
- PXI-7962R
- PXI-7965R
- PXI-7966R
- PXIe-7971R
- PXIe-7972R
- PXIe-7975R
- PXIe-7976R

FlexRIO devices also support custom invoke methods for reserving trigger lines on PXI devices.
 Refer to *Reserving Trigger Lines for FlexRIO PXI Devices* for more
 information about using custom invoke methods for reserving trigger lines.

Parent topic:

Programming with FlexRIO

Related concepts:

- Reserving Trigger Lines for FlexRIO PXI Devices

<!--NI_TOPIC bundle=flexrio path=flexrio-help.html language=enus -->
## TOPIC 00046: FlexRIO with Integrated I/O

- bundle_id: `flexrio`
- source_path: `flexrio-help.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/flexrio-help.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn the fundamental and advanced concepts necessary for using FlexRIO with Integrated I/O hardware with the FlexRIO instrument driver. In addition to device-specific information, this help file contains getting started steps for configuring FlexRIO devices in LabVIEW and LabVIEW FPGA Module and in

### FlexRIO with Integrated I/O

Learn the fundamental and advanced concepts necessary for using FlexRIO with Integrated I/O
 hardware with the FlexRIO instrument driver. In addition to device-specific information,
 this help file contains getting started steps for configuring FlexRIO devices in LabVIEW
 and LabVIEW FPGA Module and includes LabVIEW programming references.

<!--NI_TOPIC bundle=flexrio path=flexrio-with-modular-i-o-help.html language=enus -->
## TOPIC 00047: FlexRIO with Modular I/O

- bundle_id: `flexrio`
- source_path: `flexrio-with-modular-i-o-help.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/flexrio-with-modular-i-o-help.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about the fundamental and advanced concepts necessary for using FlexRIO with Modular I/O hardware with the FlexRIO instrument driver. In addition to device-specific information, this help file contains getting started steps for configuring FlexRIO devices in LabVIEW and LabVIEW FPGA Module and

### FlexRIO with Modular I/O

Learn about the fundamental and advanced concepts necessary for using FlexRIO with Modular I/O
 hardware with the FlexRIO instrument driver. In addition to device-specific information,
 this help file contains getting started steps for configuring FlexRIO devices in LabVIEW
 and LabVIEW FPGA Module and includes LabVIEW programming references.

<!--NI_TOPIC bundle=flexrio path=getting-started-with-flexrio.html language=enus -->
## TOPIC 00048: Getting Started with FlexRIO

- bundle_id: `flexrio`
- source_path: `getting-started-with-flexrio.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/getting-started-with-flexrio.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To get started using your FlexRIO device and software, refer to the getting started guide for your device, adapter module, or controller. The getting started guide explains how to complete the following tasks: Installing the software and hardware Installing the adapter module Configuring the hardwar

### Getting Started with FlexRIO

To get started using your FlexRIO device and software, refer to the getting started guide for your device, adapter module, or controller. The getting started guide explains how to complete the following tasks:

- Installing the software and hardware
- Installing the adapter module
- Configuring the hardware in MAX
- Programming the hardware

Tip

Related concepts:

- Configuring a FlexRIO Adapter Module
- Installed Examples

<!--NI_TOPIC bundle=flexrio path=installed-examples.html language=enus -->
## TOPIC 00049: Installed Examples

- bundle_id: `flexrio`
- source_path: `installed-examples.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/installed-examples.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FlexRIO includes several example applications for LabVIEW. These examples serve as interactive tools, programming models, and as building blocks in your own applications. LabVIEW users can use the Example Finder to search or browse examples. FlexRIO examples are classified by keyword, so you can sea

### Installed Examples

FlexRIO includes several example applications for LabVIEW. These examples serve as interactive tools, programming models, and as building blocks in your own applications.

LabVIEW users can use the Example Finder to search or browse examples. FlexRIO examples are classified by keyword, so you can search for a particular device or measurements function. With LabVIEW running, select Help»Find Examples to launch the NI Example Finder. The NI Example Finder offers two ways to access all installed LabVIEW example VIs and their descriptions.

- Click the Browse tab to locate FlexRIO examples by task at Hardware Input and Output » FlexRIO .
- Click the Search tab to search all installed examples by keyword. For example, search for " FlexRIO " to locate all FlexRIO examples.

Note

NI Example Finder

Requirements

Examples also are available online that demonstrate FlexRIO basics, such as using DRAM, acquiring data from adapter modules, and performing high throughput streaming. Refer to ni.com/examples for these examples and for more information.

Parent topic:

Getting Started with FlexRIO

<!--NI_TOPIC bundle=flexrio path=instruction-framework-overview.html language=enus -->
## TOPIC 00050: Instruction Framework Overview

- bundle_id: `flexrio`
- source_path: `instruction-framework-overview.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/instruction-framework-overview.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Instruction Framework instrument design library to build a communication network in LabVIEW FPGA. The network has two types of endpoints: Instruction Producers and Address Spaces. Instruction Producers issue read and write instructions that are targeted for a particular Address Space. When t

### Instruction Framework Overview

Use the Instruction Framework instrument design library to build a communication network in LabVIEW FPGA. The network has two types of endpoints: Instruction Producers and Address Spaces. Instruction Producers issue read and write instructions that are targeted for a particular Address Space. When the destination Address Space completes an instruction, it provides a response which is routed back to the Instruction Producer that issued the instruction, as shown in the following diagram:

[IMAGE alt='image' src='GUID-36867198-0850-404E-A6AF-FE8E1530F619-a5.gif']

The Instruction Framework instrument design library includes some host VIs, to help with communication between host libraries, and FPGA address spaces. The Subsystem Map class provides a way to look-up the location of an Address Space on the host, using the Address Space's unique identifier (UID). A context object is returned from this lookup function, which can be used to specify the destination for a read or write operation.

The Instruction Target class is intended to be used as an abstract interface for the mechanism used to communicate with the Instruction Framework FPGA Network. The FIFO Register Bus instrument design library provides an Instruction Target implementation on the host, which is coupled to an Instruction Producer implementation on the FPGA. This allows a host controller to send instructions to Address Spaces on the FPGA, and read the resulting responses. The instructions are sent to the FPGA using a uniquely named DMA FIFO, and the responses are received using a uniquely named indicator.

Some instrument design libraries use the Instruction Framework as a configuration mechanism. These libraries require a Subsystem Map object to look-up the location of corresponding Address Spaces on the FPGA. These libraries will also require an Instruction Target to provide the communication mechanism from the host controller to an Instruction Producer on the Instruction Framework FPGA Network. The corresponding Address Spaces must be added to the Instruction Framework FPGA Network in order for the host library to communicate properly with the FPGA library. This Address Space implementation provides register access through an Instruction Producer, such as the FIFO Register Bus library, instead of using controls and indicators on the top level of the FPGA diagram.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=instruction-framework-overview_2.html language=enus -->
## TOPIC 00051: Instruction Framework Overview

- bundle_id: `flexrio`
- source_path: `instruction-framework-overview_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/instruction-framework-overview_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Instruction Framework instrument design library to build a communication network in LabVIEW FPGA. The network has two types of endpoints: Instruction Producers and Address Spaces. Instruction Producers issue read and write instructions that are targeted for a particular Address Space. When t

### Instruction Framework Overview

Use the Instruction Framework instrument design library to build a communication network in LabVIEW FPGA. The network has two types of endpoints: Instruction Producers and Address Spaces. Instruction Producers issue read and write instructions that are targeted for a particular Address Space. When the destination Address Space completes an instruction, it provides a response which is routed back to the Instruction Producer that issued the instruction, as shown in the following diagram:

[IMAGE alt='image' src='GUID-36867198-0850-404E-A6AF-FE8E1530F619-a5.gif']

The Instruction Framework instrument design library includes some host VIs, to help with communication between host libraries, and FPGA address spaces. The Subsystem Map class provides a way to look-up the location of an Address Space on the host, using the Address Space's unique identifier (UID). A context object is returned from this lookup function, which can be used to specify the destination for a read or write operation.

The Instruction Target class is intended to be used as an abstract interface for the mechanism used to communicate with the Instruction Framework FPGA Network. The FIFO Register Bus instrument design library provides an Instruction Target implementation on the host, which is coupled to an Instruction Producer implementation on the FPGA. This allows a host controller to send instructions to Address Spaces on the FPGA, and read the resulting responses. The instructions are sent to the FPGA using a uniquely named DMA FIFO, and the responses are received using a uniquely named indicator.

Some instrument design libraries use the Instruction Framework as a configuration mechanism. These libraries require a Subsystem Map object to look-up the location of corresponding Address Spaces on the FPGA. These libraries will also require an Instruction Target to provide the communication mechanism from the host controller to an Instruction Producer on the Instruction Framework FPGA Network. The corresponding Address Spaces must be added to the Instruction Framework FPGA Network in order for the host library to communicate properly with the FPGA library. This Address Space implementation provides register access through an Instruction Producer, such as the FIFO Register Bus library, instead of using controls and indicators on the top level of the FPGA diagram.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=labview-and-system-integration.html language=enus -->
## TOPIC 00052: LabVIEW and System Integration

- bundle_id: `flexrio`
- source_path: `labview-and-system-integration.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/labview-and-system-integration.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about how to integrate your FlexRIO Integrated I/O system in the LabVIEW application development environment.

### LabVIEW and System Integration

This section contains information about how to integrate your FlexRIO Integrated I/O system
in the LabVIEW application development environment.

Parent topic:

FlexRIO with Integrated I/O

<!--NI_TOPIC bundle=flexrio path=labview-system-configuration.html language=enus -->
## TOPIC 00053: LabVIEW System Configuration

- bundle_id: `flexrio`
- source_path: `labview-system-configuration.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/labview-system-configuration.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW System Configuration API allows you to gather information and perform tasks programmatically on both local and remote systems. The System Configuration palette is located on the functions palette in LabVIEW under Measurement I/O. If Measurement I/O does not appear on the functions palett

### LabVIEW System Configuration

Measurement
 I/O

Note

Measurement I/O

Customize»Change Visible
 Palette

Complete the following steps to use the LabVIEW System Configuration API with your FlexRIO device.

1. Open a session and point to your target using its IP address.
2. Enter your user name and password, if applicable.
3. Open the System Configuration palette in LabVIEW.
4. Open the Property Node (Hardware) to obtain information such as the device temperature and device model name.

#### FlexRIO System Experts

FlexRIO System Experts are compatible with the LabVIEW System Configuration API. Use
 the programmatic expert name for your device according to the following table.

| FlexRIO Device | Programmatic Name |
| --- | --- |
| FlexRIO with Modular I/O | niflexrio |
| FlexRIO Coprocessors, FlexRIO with Integrated I/O | niflexrio2 |

Refer to the *NI System Configuration API Help* topic of the *LabVIEW
 Help* for more information about using the LabVIEW System Configuration
 API.

Parent topic:

Programming with FlexRIO

<!--NI_TOPIC bundle=flexrio path=labview-system-configuration_2.html language=enus -->
## TOPIC 00054: LabVIEW System Configuration

- bundle_id: `flexrio`
- source_path: `labview-system-configuration_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/labview-system-configuration_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW System Configuration API allows you to gather information and perform tasks programmatically on both local and remote systems. The System Configuration palette is located on the functions palette in LabVIEW under Measurement I/O. If Measurement I/O does not appear on the functions palett

### LabVIEW System Configuration

Measurement
 I/O

Note

Measurement I/O

Customize»Change Visible
 Palette

Complete the following steps to use the LabVIEW System Configuration API with your FlexRIO device.

1. Open a session and point to your target using its IP address.
2. Enter your user name and password, if applicable.
3. Open the System Configuration palette in LabVIEW.
4. Open the Property Node (Hardware) to obtain information such as the device temperature and device model name.

#### FlexRIO System Experts

FlexRIO System Experts are compatible with the LabVIEW System Configuration API. Use
 the programmatic expert name for your device according to the following table.

| FlexRIO Device | Programmatic Name |
| --- | --- |
| FlexRIO with Modular I/O | niflexrio |
| FlexRIO Coprocessors, FlexRIO with Integrated I/O | niflexrio2 |

Refer to the *NI System Configuration API Help* topic of the *LabVIEW
 Help* for more information about using the LabVIEW System Configuration
 API.

Parent topic:

Programming with FlexRIO

<!--NI_TOPIC bundle=flexrio path=memory-overview.html language=enus -->
## TOPIC 00055: Memory Overview

- bundle_id: `flexrio`
- source_path: `memory-overview.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/memory-overview.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Memory instrument design library to access DRAM and BRAM on the device in a consistent manner. This library provides a basic read and write interface to DRAM and BRAM. This library supports LabVIEW FPGA data widths that are 128 bits and 64 bits wide for DRAM and BRAM, respectively. This inst

### Memory Overview

Use the Memory instrument design library to access DRAM and BRAM on the device in a consistent manner. This library provides a basic read and write interface to DRAM and BRAM. This library supports LabVIEW FPGA data widths that are 128 bits and 64 bits wide for DRAM and BRAM, respectively. This instrument design library contains LabVIEW FPGA VIs.

In addition to the basic memory interface, you can use this instrument design library to reset the DRAM or BRAM. When memory read operations are posted to memory, there is some amount of latency before the associated data is retrieved from memory and presented to the FPGA diagram. Furthermore, multiple read operations can be queued up at once. You can use the Memory instrument design library to reset those queued memory operations.

This instrument design library also adds support for arbitration between the read and write ports of DRAM. Because the physical DRAM interface has a single port for read and write operations, the FPGA must arbitrate between reads and writes when accessing DRAM. This instrument design library implements a simple timeslice arbiter that provides for configurable bandwidth between the read and write ports. You can use this arbitration to achieve improved throughput with your DRAM read and write operations.

Refer to the LabVIEW context help of the Memory Design VIs for more information about the library interface.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=memory-overview_2.html language=enus -->
## TOPIC 00056: Memory Overview

- bundle_id: `flexrio`
- source_path: `memory-overview_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/memory-overview_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Memory instrument design library to access DRAM and BRAM on the device in a consistent manner. This library provides a basic read and write interface to DRAM and BRAM. This library supports LabVIEW FPGA data widths that are 128 bits and 64 bits wide for DRAM and BRAM, respectively. This inst

### Memory Overview

Use the Memory instrument design library to access DRAM and BRAM on the device in a consistent manner. This library provides a basic read and write interface to DRAM and BRAM. This library supports LabVIEW FPGA data widths that are 128 bits and 64 bits wide for DRAM and BRAM, respectively. This instrument design library contains LabVIEW FPGA VIs.

In addition to the basic memory interface, you can use this instrument design library to reset the DRAM or BRAM. When memory read operations are posted to memory, there is some amount of latency before the associated data is retrieved from memory and presented to the FPGA diagram. Furthermore, multiple read operations can be queued up at once. You can use the Memory instrument design library to reset those queued memory operations.

This instrument design library also adds support for arbitration between the read and write ports of DRAM. Because the physical DRAM interface has a single port for read and write operations, the FPGA must arbitrate between reads and writes when accessing DRAM. This instrument design library implements a simple timeslice arbiter that provides for configurable bandwidth between the read and write ports. You can use this arbitration to achieve improved throughput with your DRAM read and write operations.

Refer to the LabVIEW context help of the Memory Design VIs for more information about the library interface.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=multirecord-acquisition-overview.html language=enus -->
## TOPIC 00057: Multirecord Acquisition Overview

- bundle_id: `flexrio`
- source_path: `multirecord-acquisition-overview.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/multirecord-acquisition-overview.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Multirecord Acquisition instrument design library to acquire a series of waveforms that are aligned with various triggering conditions. The FPGA uses triggering conditions to determine when to start and stop acquiring each waveform. Each acquired waveform is stored in DRAM on the device in a

### Multirecord Acquisition Overview

Use the Multirecord Acquisition instrument design library to acquire a series of waveforms that are aligned with various triggering conditions. The FPGA uses triggering conditions to determine when to start and stop acquiring each waveform. Each acquired waveform is stored in DRAM on the device in a region of memory called a record. Your application can retrieve those records from DRAM for further processing and analysis. You can perform this custom processing on the FPGA or host. Each data sample of a record is 32 bits wide. For devices that receive two samples per cycle, you can configure this instrument design library to acquire two samples per cycle.

This instrument design library is particularly useful when you need to capture a finite amount of data that is correlated with external events. For example, you can use this instrument design library in RF applications to capture multiple bursts of RF data and align those acquisitions to the start of each burst signal. Each RF burst might be stored in a single record. However, this is one specific example, and there are many other kinds of applications in which you can use this library.

In general, records are denoted by the assertion of a Reference Trigger. After the FPGA starts acquiring a record, the FPGA continues acquiring data into that record until the Reference Trigger asserts. After the Reference Trigger asserts, the FPGA acquires the specified number of post-trigger samples into that record before marking the record as complete and advancing to the next record. This behavior allows you to capture a specified number of samples both before and after the assertion of the Reference Trigger.

This library supports the following types of triggers:

- Start Trigger —Starts the acquisition of the first record. This trigger is only valid for the first record.
- Reference Trigger —Identifies a point of interest in the stream of acquired data samples. The FPGA uses this trigger to help decide when to stop acquiring a record. After the Reference Trigger asserts, the FPGA begins counting samples. After the FPGA acquires the specified number of post-trigger samples, the FPGA stops acquiring data into that record. The trigger is only evaluated when a record acquisition is in progress.
- Advance Trigger —Starts the acquisition of additional records after the first record. The FPGA evaluates this trigger only after a record is done being acquired.

You can also use this instrument design library to store one or more 64-bit timestamps that are correlated with each record. For example, you could store the time when the Reference Trigger asserts for each record. This technique can be useful if your application needs to track when each record was acquired.

This instrument design library includes host VIs and FPGA VIs. The following figure is a high-level block diagram of the LabVIEW FPGA design of the Multirecord Acquisition library.

[IMAGE alt='image' src='GUID-AB2CAEE6-8011-40C1-9D32-0429E2C1829C-a5.gif']

The FPGA writes sample data into this instrument design library from the Sample Clock domain. You can retrieve the acquired records from memory and transfer them to the host through the Fetch DMA FIFO VI. You can insert custom FPGA processing code either before samples are written to memory or after you retrieve records from memory. Where you decide to perform the processing generally depends on the nature of the signal processing algorithm.

Refer to the LabVIEW context help for the Multirecord Acquisition LabVIEW VIs for more detailed information about the library interface.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=multirecord-acquisition-overview_2.html language=enus -->
## TOPIC 00058: Multirecord Acquisition Overview

- bundle_id: `flexrio`
- source_path: `multirecord-acquisition-overview_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/multirecord-acquisition-overview_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Multirecord Acquisition instrument design library to acquire a series of waveforms that are aligned with various triggering conditions. The FPGA uses triggering conditions to determine when to start and stop acquiring each waveform. Each acquired waveform is stored in DRAM on the device in a

### Multirecord Acquisition Overview

Use the Multirecord Acquisition instrument design library to acquire a series of waveforms that are aligned with various triggering conditions. The FPGA uses triggering conditions to determine when to start and stop acquiring each waveform. Each acquired waveform is stored in DRAM on the device in a region of memory called a record. Your application can retrieve those records from DRAM for further processing and analysis. You can perform this custom processing on the FPGA or host. Each data sample of a record is 32 bits wide. For devices that receive two samples per cycle, you can configure this instrument design library to acquire two samples per cycle.

This instrument design library is particularly useful when you need to capture a finite amount of data that is correlated with external events. For example, you can use this instrument design library in RF applications to capture multiple bursts of RF data and align those acquisitions to the start of each burst signal. Each RF burst might be stored in a single record. However, this is one specific example, and there are many other kinds of applications in which you can use this library.

In general, records are denoted by the assertion of a Reference Trigger. After the FPGA starts acquiring a record, the FPGA continues acquiring data into that record until the Reference Trigger asserts. After the Reference Trigger asserts, the FPGA acquires the specified number of post-trigger samples into that record before marking the record as complete and advancing to the next record. This behavior allows you to capture a specified number of samples both before and after the assertion of the Reference Trigger.

This library supports the following types of triggers:

- Start Trigger —Starts the acquisition of the first record. This trigger is only valid for the first record.
- Reference Trigger —Identifies a point of interest in the stream of acquired data samples. The FPGA uses this trigger to help decide when to stop acquiring a record. After the Reference Trigger asserts, the FPGA begins counting samples. After the FPGA acquires the specified number of post-trigger samples, the FPGA stops acquiring data into that record. The trigger is only evaluated when a record acquisition is in progress.
- Advance Trigger —Starts the acquisition of additional records after the first record. The FPGA evaluates this trigger only after a record is done being acquired.

You can also use this instrument design library to store one or more 64-bit timestamps that are correlated with each record. For example, you could store the time when the Reference Trigger asserts for each record. This technique can be useful if your application needs to track when each record was acquired.

This instrument design library includes host VIs and FPGA VIs. The following figure is a high-level block diagram of the LabVIEW FPGA design of the Multirecord Acquisition library.

[IMAGE alt='image' src='GUID-AB2CAEE6-8011-40C1-9D32-0429E2C1829C-a5.gif']

The FPGA writes sample data into this instrument design library from the Sample Clock domain. You can retrieve the acquired records from memory and transfer them to the host through the Fetch DMA FIFO VI. You can insert custom FPGA processing code either before samples are written to memory or after you retrieve records from memory. Where you decide to perform the processing generally depends on the nature of the signal processing algorithm.

Refer to the LabVIEW context help for the Multirecord Acquisition LabVIEW VIs for more detailed information about the library interface.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=new-features-and-changes.html language=enus -->
## TOPIC 00059: FlexRIO New Features and Changes

- bundle_id: `flexrio`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/new-features-and-changes.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of FlexRIO. Discover what is new in the latest releases of FlexRIO.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might include

### FlexRIO
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of FlexRIO.

FlexRIO

Note

Release Notes

Related information:

- Software and Driver Downloads

#### FlexRIO
 2026 Q2 Changes

FlexRIO 2026 Q2 includes bug fixes.

##### New
 Features

This version of FlexRIO adds support
 for the following features:

- Bug fixes and improvements.

#### FlexRIO
 2025 Q4 Changes

Learn about new features, behavior changes, and other updates in FlexRIO 2025 Q4.

##### New
 Features and Changes

This version of FlexRIO
 provides support for the following features:

- Added support for Red Hat Enterprise Linux 9.6.
- Ended support for Red Hat Enterprise Linux 9.4.
- Ended support for Windows Server 2019.

<!--NI_TOPIC bundle=flexrio path=ni-labview-instrument-design-libraries-for-fl.html language=enus -->
## TOPIC 00060: NI LabVIEW Instrument Design Libraries for FlexRIO

- bundle_id: `flexrio`
- source_path: `ni-labview-instrument-design-libraries-for-fl.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/ni-labview-instrument-design-libraries-for-fl.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the instrument design libraries that you can use to create application-specific instrumentation. For more information about using instrument design libraries with FlexRIO devices, refer to the following web pages: Getting Started With Your Software-Designed Instrument An Intro

### NI LabVIEW Instrument Design Libraries for FlexRIO

This section describes the instrument design libraries that you can use to create application-specific instrumentation.

For more information about using instrument design libraries with FlexRIO devices, refer to the following web pages:

- Getting Started With Your Software-Designed Instrument
- An Introduction to Instrument Design Libraries for NI Software-Designed Instruments

Parent topic:

Programming with FlexRIO

<!--NI_TOPIC bundle=flexrio path=ni-labview-instrument-design-libraries-for-fl_2.html language=enus -->
## TOPIC 00061: NI LabVIEW Instrument Design Libraries for FlexRIO

- bundle_id: `flexrio`
- source_path: `ni-labview-instrument-design-libraries-for-fl_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/ni-labview-instrument-design-libraries-for-fl_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section describes the instrument design libraries that you can use to create application-specific instrumentation. For more information about using instrument design libraries with FlexRIO devices, refer to the following web pages: Getting Started With Your Software-Designed Instrument An Intro

### NI LabVIEW Instrument Design Libraries for FlexRIO

This section describes the instrument design libraries that you can use to create application-specific instrumentation.

For more information about using instrument design libraries with FlexRIO devices, refer to the following web pages:

- Getting Started With Your Software-Designed Instrument
- An Introduction to Instrument Design Libraries for NI Software-Designed Instruments

Parent topic:

Programming with FlexRIO

<!--NI_TOPIC bundle=flexrio path=power-monitoring-and-shutdown.html language=enus -->
## TOPIC 00062: Power Monitoring and Shutdown

- bundle_id: `flexrio`
- source_path: `power-monitoring-and-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/power-monitoring-and-shutdown.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To stay within PXI Express power and cooling requirements, there are limitations on the size and activity factor of the logic loaded to the FPGA.If power consumed by the device exceeds a factory-programmed limit, the device driver attempts to abort the VI running on the FPGA and reconfigure to a coo

### Power Monitoring and Shutdown

To stay within PXI Express power and cooling requirements, there are limitations on the size and activity factor of the logic loaded to the FPGA.

If power consumed by the device exceeds a factory-programmed limit, the device driver attempts to abort the VI running on the FPGA and reconfigure to a cooldown image. The host VI reports an error and recovery instructions. MAX also displays an error message with recovery instructions.

Note

Property Node

#### Re-enabling the Device After Power Shutdown

To re-enable your device after power shutdown, download a bitfile to the FPGA or open a new session to download the default bitfile to the FPGA.

Parent topic:

System Monitoring and Shutdown

<!--NI_TOPIC bundle=flexrio path=programming.html language=enus -->
## TOPIC 00063: Programming with FlexRIO

- bundle_id: `flexrio`
- source_path: `programming.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/programming.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section provides overview information about programming FlexRIO devices. Refer to the FlexRIO API Reference detailed descriptions of functions, methods, properties, and dialog boxes.NI recommends that you have 8 GB or more of system memory and requires a 64-bit operating system for compiling La

### Programming with FlexRIO

FlexRIO API Reference

Note

Parent topic:

FlexRIO with Modular I/O

Related information:

- FlexRIO API Reference

<!--NI_TOPIC bundle=flexrio path=programming_2.html language=enus -->
## TOPIC 00064: Programming with FlexRIO

- bundle_id: `flexrio`
- source_path: `programming_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/programming_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section provides overview information about programming FlexRIO devices. Refer to the FlexRIO API Reference detailed descriptions of functions, methods, properties, and dialog boxes.NI recommends that you have 8 GB or more of system memory and requires a 64-bit operating system for compiling La

### Programming with FlexRIO

FlexRIO API Reference

Note

Parent topic:

FlexRIO with Integrated I/O

<!--NI_TOPIC bundle=flexrio path=pxi-express-modules.html language=enus -->
## TOPIC 00065: PXI Express Modules

- bundle_id: `flexrio`
- source_path: `pxi-express-modules.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/pxi-express-modules.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXI Express Specification integrates PCI Express signaling into the PXI standard, which increases backplane bandwidth and enhances PXI timing and synchronization features by incorporating a 100 MHz differential reference clock and differential triggers. The PXI Express Specification adds these f

### PXI Express Modules

The PXI Express Specification integrates PCI Express signaling into the PXI standard, 
which increases backplane bandwidth and enhances PXI timing and synchronization features by 
incorporating a 100 MHz differential reference clock and differential triggers. The PXI Express 
Specification adds these features to PXI while maintaining backward compatibility. 
For an overview of the PXI Express specification, refer to PXI Express Specification Tutorial.

The following figure shows a typical PXI Express chassis installation.

[IMAGE alt='image' src='GUID-A6368F92-6284-4488-A3F1-9D2FF606F036-a5.gif']

#### Chassis Guidelines

NI PXI Express modules can be installed in the following PXI Express chassis
 slots:

- PXI hybrid slots —Accepts all PXI modules that are hybrid
 slot-compatible or PXI Express modules
- PXI Express slots —Accepts PXI Express modules

Note

Parent topic:

PXI System Considerations

<!--NI_TOPIC bundle=flexrio path=pxi-modules.html language=enus -->
## TOPIC 00066: PXI Modules

- bundle_id: `flexrio`
- source_path: `pxi-modules.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/pxi-modules.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: PCI eXtensions for Instrumentation (PXI) modular instrumentation delivers a PC-based, standardized, high-performance measurement and automation system. PXI combines the high-speed PCI bus with integrated timing and triggering designed specifically for measurement and automation applications to deliv

### PXI Modules

PCI eXtensions for Instrumentation (PXI) modular instrumentation delivers a PC-based, standardized, high-performance measurement and automation system. PXI combines the high-speed PCI bus with integrated timing and triggering designed specifically for measurement and automation applications to
deliver significant performance improvements over older architectures. For an overview of the PXI Specification, refer to PXI Specification Tutorial.

The following figure shows a typical PXI chassis installation.

[IMAGE alt='image' src='GUID-74EEB724-664E-455C-85F5-E7C86BA1785A-a5.gif']

#### Chassis Guidelines

FlexRIO devices can be installed in the following chassis and slots:

- PXI chassis —PXI modules can be installed in any peripheral slot of a PXI chassis.
- PXI Express chassis —PXI devices can be installed in the following PXI Express chassis slots:
  - PXI-1 slots —Accepts all PXI modules
  - PXI hybrid slots —Accepts all PXI modules that are hybrid slot-compatible or PXI Express modules
  - PXI Express slots —Accepts PXI Express modules

#### Using PXI-Compatible Products with Standard CompactPCI Products

The ability to use PXI-compatible products with standard CompactPCI products is an important feature provided by the PXI Specification, revision 2.1. If you use a PXI-compatible plug-in device in a standard CompactPCI chassis, you cannot use PXI-specific functions, but you can still use the basic plug-in device functions. For example, the PXI trigger bus on NI signal generators is available in a PXI chassis but not in a CompactPCI chassis. The CompactPCI specification permits vendors to develop sub-buses that co-exist with the basic PCI interface on the CompactPCI bus. Compatible operation is not guaranteed between CompactPCI devices with different sub-buses nor between CompactPCI devices with sub-buses and PXI. The standard implementation for CompactPCI does not include these sub-buses. NI signal generators work in any standard CompactPCI chassis. PXI-specific features, such as PXI_Trig bus and PXI_CLK10 reference are implemented on the J2 connector of the CompactPCI bus.

Parent topic:

PXI System Considerations

Related concepts:

- PXI Star Trigger Line

<!--NI_TOPIC bundle=flexrio path=pxi-pxie-chassis-cooling.html language=enus -->
## TOPIC 00067: PXI/PXIe Chassis Cooling

- bundle_id: `flexrio`
- source_path: `pxi-pxie-chassis-cooling.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/pxi-pxie-chassis-cooling.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Not all PXI or PXI Express chassis provide the same cooling. When selecting a PXI or PXI Express chassis, consideration should be given to providing adequate airflow. NI PXI and PXI Express devices are high-precision instruments and may be sensitive to interference from other electronic devices. To

### PXI/PXIe Chassis Cooling

Not all PXI or PXI Express chassis provide the same cooling. When selecting a PXI or 
PXI Express chassis, consideration should be given to providing adequate airflow.

NI PXI and PXI Express devices are high-precision instruments and may be sensitive to 
interference from other electronic devices. To optimize the accuracy and performance of the device,
 you may need to locate the device in a slot away from devices with power supplies and other noisy circuitry. The device may also be sensitive to heat generated by high-power products in neighboring slots. When possible, consider locating the device away 
 from high-power devices to optimize cooling.

For more information on cooling, refer to *Maintain Forced-Air Cooling* on
 ni.com/docs.

Parent topic:

PXI System Considerations

Related information:

- Maintain Forced-Air Cooling Note to Users

<!--NI_TOPIC bundle=flexrio path=pxi-star-trigger-line.html language=enus -->
## TOPIC 00068: PXI Star Trigger Line

- bundle_id: `flexrio`
- source_path: `pxi-star-trigger-line.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/pxi-star-trigger-line.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The PXI star trigger is a feature implemented on National Instruments PXI chassis. PXI chassis have a PXI trigger bus that is linked to all slots in the chassis. In addition, PXI chassis have a star trigger that is linked to Slot 2. The star trigger is a high-performance trigger signal that you can

### PXI Star Trigger Line

The PXI star trigger is a feature implemented on National Instruments PXI chassis. PXI chassis have a PXI trigger bus that is linked to all slots in the chassis. In addition, PXI chassis have a star trigger that is linked to Slot 2. The star trigger is a high-performance trigger signal that you can use to synchronize all the modules in a chassis. You can also do this using the normal PXI trigger bus, but the star trigger offers increased performance, specifically a propagation delay of no more than 5 ns and an intermodule delay of no more than 1 ns.

[IMAGE alt='image' src='GUID-40CACB84-67BF-4D98-976B-2315DC12BF1A-a5.svg']

Slot 2 of the PXI chassis is optimized for a star trigger controller. If the star trigger is not required, you can use Slot 2 as a standard peripheral slot. The trigger signal generated by a controller can then be accessed by the other modules through the backplane. The star trigger controller in Slot 2 of the PXI chassis can route triggers among peripheral slots with very low skew (within 1 nanosecond).

To use a star trigger, the module must be in a PXI form factor.

All FlexRIO FPGA modules can receive triggers from the PXI star trigger line, which means that if another instrument is driving the PXI star trigger from Slot 2 of the PXI chassis, the FlexRIO FPGA module can receive this trigger signal from another slot. FlexRIO FPGA modules cannot drive the PXI star trigger line from Slot 2. Therefore, if you want to generate a trigger on the star trigger line with a master in Slot 2, this master cannot be a FlexRIO FPGA module.

Parent topic:

PXI System Considerations

<!--NI_TOPIC bundle=flexrio path=pxi-system-considerations.html language=enus -->
## TOPIC 00069: PXI System Considerations

- bundle_id: `flexrio`
- source_path: `pxi-system-considerations.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/pxi-system-considerations.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about integrating FlexRIO modules into a PXI/PXIe based measurement system.

### PXI System Considerations

This section contains information about integrating FlexRIO modules into a PXI/PXIe based measurement system.

<!--NI_TOPIC bundle=flexrio path=pxi-trigger-lines.html language=enus -->
## TOPIC 00070: PXI Trigger Lines

- bundle_id: `flexrio`
- source_path: `pxi-trigger-lines.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/pxi-trigger-lines.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Eight PXI bused trigger lines are highly flexible and can be used in a variety of ways. For example, triggers can be used to synchronize the operation of several different PXI peripheral modules. In other applications, one module can control carefully timed sequences of operations performed on other

### PXI Trigger Lines

Eight PXI bused trigger lines are highly flexible and can be used in a variety of ways. For example, triggers can be used to synchronize the operation of several different PXI peripheral modules. In other applications, one module can control carefully timed sequences of operations performed on other modules in the system. Triggers may be passed from one module to another, allowing precisely timed responses to asynchronous external events that are being monitored or controlled. The number of triggers that a particular application requires varies with the complexity and number of events involved.

[IMAGE alt='image' src='GUID-A420B0C2-6BA3-48E1-A9C1-B7CB6C6FC483-a5.gif']

The PXI Specification is implemented with the RTSI bus through the PXI trigger lines. PXI
 Specification requires 8 lines, PXI_TRIGGER[0:7], on the P2/J2 connector of the PXI
 chassis for the trigger lines. The RTSI features of the NI Source hardware is
 implemented on this sub-bus. The RTSI trigger [0..6] is implemented on PXI_TRIGGER[0:6],
 and the RTSI clock is routed on PXI_TRIGGER(7).

Parent topic:

PXI System Considerations

<!--NI_TOPIC bundle=flexrio path=pxi-triggers.html language=enus -->
## TOPIC 00071: PXI Triggers

- bundle_id: `flexrio`
- source_path: `pxi-triggers.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/pxi-triggers.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the FPGA I/O Node to access the trigger lines on FlexRIO PXI devices. When developing an FPGA VI that uses triggers, be sure to reserve the trigger lines you are using and, to ensure compatibility with other FlexRIO devices, configure trigger pulses on FlexRIO PXI devices to last for at

### PXI Triggers

You can use the FPGA I/O Node to access the trigger lines on FlexRIO PXI devices. When developing an FPGA VI that uses triggers, be sure to reserve the trigger lines you are using and, to ensure compatibility with other FlexRIO devices, configure trigger pulses on FlexRIO PXI devices to last for at least two clock cycles of the clock on the receiving device. Refer to the PXI Specifications for more information about trigger bus requirements.

Related concepts:

- Reserving Trigger Lines for FlexRIO PXI Devices
- Configuring Trigger Pulses

<!--NI_TOPIC bundle=flexrio path=random-access-128-bit-memory-interface.html language=enus -->
## TOPIC 00072: Random Access - 128 Bit Memory Interface

- bundle_id: `flexrio`
- source_path: `random-access-128-bit-memory-interface.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/random-access-128-bit-memory-interface.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This memory interface provides the highest performance interface to external DRAM. Both the write-side and read-side data ports are exposed as 128-bit data words. Requests to write to and read from DRAM are satisfied by issuing a write or read command to the Random Access - 128 Bit memory interface.

### Random Access - 128 Bit Memory Interface

This memory interface provides the highest performance interface to external DRAM. Both the write-side and read-side data ports are exposed as 128-bit data words. Requests to write to and read from DRAM are satisfied by issuing a write or read command to the Random Access - 128 Bit memory interface.

The following table lists the I/O provided by the Random Access - 128 Bit memory interface.

| Memory Interface I/O | Data Type | To Memory/From Memory | Description |
| --- | --- | --- | --- |
| Address | U32 | To Memory | Sets the address in external memory for reading or writing. The physical data bus for external memory is 32 bits wide (4 bytes). Each unique address value represents 4 bytes of data. Therefore, the total number of unique addresses in external memory is equal to (Memory Size in bytes)/4. Note The memory interface exposed to LabVIEW FPGA is 128 bits wide. As a result, each memory write or read operation accesses four different address locations in memory. The memory controller latches this signal value only when you issue a new memory write command by asserting the Command_Write_Enable signal. |
| Command | U8 | To Memory | 0 = Performs a memory write. 1 = Perform a memory read. The memory controller latches this signal value only when you issue a new memory write command by asserting the Command_Write_Enable signal. |
| Command_Write_Enable | Bool | To Memory | TRUE = Performs either a memory write or read command, as dictated by the Command signal setting. FALSE = Does not perform any new memory write or read commands. To write or read a single 128-bit data value, assert this signal for only one clock cycle. Each new command is latched in a single clock cycle. |
| Command_FIFO_Full | Bool | From memory | TRUE = The memory controller internal command FIFO is full. FALSE = Space is available in the command FIFO, and the memory controller can accept new commands. Note Never assert the Command_Write_Enable signal when the Command_FIFO_Full signal is TRUE. |
| Read_Data_Upper | U64 | From memory | Displays the upper 64 bits of the 128-bit data value that was read from external memory. When you issue a memory read command, this signal contains the data retrieved from external memory. The signal state is valid only on the clock cycles in which Read_Strobe is TRUE. |
| Read_Data_Lower | U64 | From memory | Displays the lower 64 bits of the 128-bit data value that was read from external memory. When you issue a memory read command, this signal contains the data retrieved from external memory. The signal state is valid only on the clock cycles in which Read_Strobe is TRUE. |
| Read_Strobe | Bool | From memory | TRUE = Indicates that you can latch data onto the Read_Data_Upper and Read_Data_Lower signals. FALSE = Indicates that you cannot latch data onto the Read_Data_Upper and Read_Data_Lower signals yet. When you issue a memory read command, the memory read operation takes more than one clock cycle to complete. When the memory read completes, the Read_Strobe signal asserts TRUE for one clock cycle. Note You must latch the Read_Data_Upper and Read_Data_Lower signals on the same clock cycle that Read_Strobe asserts. The memory controller permits you to queue multiple read commands without waiting for the first read command to complete. All read data returns from the memory controller in the order that the read commands were issued. In this situation, the Read_Strobe signal asserts once for each of the completed queued read commands. |
| Write_Data_Upper | U64 | To memory | Sets the upper 64 bits of the 128-bit data value to be written to external memory. The memory controller latches this signal value only when you issue a new memory write command by asserting the Command_Write_Enable signal. |
| Write_Data_Lower | U64 | To memory | Sets the lower 64 bits of the 128-bit data value to be written to external memory. The memory controller latches this signal value only when you issue a new memory write command by asserting the Command_Write_Enable signal. |
| Data Mask Lower |  |  |  |
| Data Mask Upper |  |  |  |
| Initialization_Done | Bool | From memory | TRUE = Indicates that the memory interface initialization sequence is completed. FALSE = Indicates that the memory interface initialization sequence is not completed. The memory controller performs its initialization sequence each time the FPGA is reprogrammed, and when the Reset Invoke Method function is called in the host VI. Note Never assert Command_Write_Enable when the Initialization_Done signal is FALSE. |

Each command that is written to the Random Access - 128 Bit memory interface is added to an internal command FIFO. This command FIFO can fill up, which drives the Command_FIFO_Full signal to TRUE. Do not issue any new commands to the Random Access - 128 Bit memory interface when the command FIFO is full.

The Random Access - 128 Bit memory interface automatically performs an initialization sequence after the FPGA is first programmed, and when the Reset Invoke Method function is called in the host VI. Do not issue new commands to the Random Access - 128 Bit memory interface before the initialization sequence is completed. The Initialization_Done signal returns to TRUE when the Random Access - 128 Bit memory interface initialization sequence is completed.

Each individual address value accesses 32 bits of data. Each write and read command writes and reads 128 bits of data, respectively. Because of this scheme, writing and reading data at consecutive addresses requires that you increment the address by 4 for each write and read command. Also, because each address value accesses 32 bits of data, the maximum number of valid addresses is equal to (Memory Size in Bytes)/4.

User_Clk

User_Clk

Note

Note

must

0

Complete the following steps to write data into the DRAM:

1. Ensure that the Command_FIFO_Full Boolean is FALSE.
2. Drive the Address signal with the DRAM memory address that you want to write.
3. Drive the Write_Data_Upper with the upper 64 bits of the 128-bit data word.
4. Drive the Write_Data_Lower with the lower 64 bits of the 128-bit data word.
5. Drive the Command signal with 0 . This communicates to the Random Access - 128 Bit memory interface to perform a memory write command.
6. Drive the Command_Write_Enable signal to TRUE for one clock cycle. You must only drive this signal for a single clock cycle if you want to only issue a single memory write command. Each clock cycle that this signal asserts causes a new write command to be issued to the Random Access - 128 Bit memory interface.

Complete the following steps to read data from DRAM:

1. Ensure that the Command_FIFO_Full Boolean is FALSE.
2. Drive the Address signal with the DRAM memory address that you want to read from.
3. Drive the Command signal with 1 . This signal communicates to the Random Access - 128 Bit memory interface to perform a memory read command.
4. Drive the Command_Write_Enable signal to TRUE for one clock cycle. You must only drive this signal for a single clock cycle if you want to only issue a single memory read command. Each clock cycle in which this signal is asserted causes a new read command to be issued to the Random Access - 128 Bit memory interface.
5. Continually monitor the state of the Read_Strobe signal. When this signal reads as TRUE, latch the 128-bit data value on the Read_Data_Upper and Read_Data_Lower signals. This contains the data most recently read from the Random Access - 128 Bit memory interface.

Note

Read_Strobe

Read_Strobe

LabVIEW contains example VIs that read and write to the Random Access - 128 Bit memory interface. To access the NI Example Finder, open LabVIEW and select Help»Find Examples, then select Hardware Input and Output»FlexRIO. You can also access device-specific examples by selecting Add device from the Hardware pull-down menu in the NI Example Finder.

Parent topic:

DRAM Memory Interface

<!--NI_TOPIC bundle=flexrio path=random-access-64-bit-memory-interface.html language=enus -->
## TOPIC 00073: Random Access - 64 Bit Memory Interface

- bundle_id: `flexrio`
- source_path: `random-access-64-bit-memory-interface.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/random-access-64-bit-memory-interface.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This memory interface provides the highest performance interface to external DRAM. Both the write-side and read-side data ports are exposed as 64-bit data words. Requests to write to and read from DRAM are satisfied by issuing a write or read command to the Random Access - 64 Bit memory interface. T

### Random Access - 64 Bit Memory Interface

This memory interface provides the highest performance interface to external DRAM. Both the write-side and read-side data ports are exposed as 64-bit data words. Requests to write to and read from DRAM are satisfied by issuing a write or read command to the Random Access - 64 Bit memory interface.

The following table lists the I/O provided by the Random Access - 64 Bit memory interface.

| Memory Interface I/O | Data Type | To Memory/From Memory | Description |
| --- | --- | --- | --- |
| Address | U32 | To Memory | Sets the address in external memory for reading or writing. The physical data bus for external memory is 16 bits wide (2 bytes). Each unique address value represents 2 bytes of data. Therefore, the total number of unique addresses in external memory is equal to (Memory Size in bytes)/2. Note The memory interface exposed to LabVIEW FPGA is 64 bits wide. As a result, each memory write or read operation accesses four different address locations in memory. The memory controller latches this signal value only when you issue a new memory write command by asserting the Command_Write_Enable signal. |
| Command | U8 | To Memory | 0 = Performs a memory write. 1 = Perform a memory read. The memory controller latches this signal value only when you issue a new memory write command by asserting the Command_Write_Enable signal. |
| Command_Write_Enable | Bool | To Memory | TRUE = Performs either a memory write or read command, as dictated by the Command signal setting. FALSE = Does not perform any new memory write or read commands. To write or read a single 64-bit data value, assert this signal for only one clock cycle. Each new command is latched in a single clock cycle. |
| Command_FIFO_Full | Bool | From memory | TRUE = The memory controller internal command FIFO is full. FALSE = Space is available in the command FIFO, and the memory controller can accept new commands. Note Never assert the Command_Write_Enable signal when the Command_FIFO_Full signal is TRUE. |
| Read_Data_Upper | U32 | From memory | Displays the upper 32 bits of the 64-bit data value that was read from external memory. When you issue a memory read command, this signal contains the data retrieved from external memory. The signal state is valid only on the clock cycles in which Read_Strobe is TRUE. |
| Read_Data_Lower | U32 | From memory | Displays the lower 32 bits of the 64-bit data value that was read from external memory. When you issue a memory read command, this signal contains the data retrieved from external memory. The signal state is valid only on the clock cycles in which Read_Strobe is TRUE. |
| Read_Strobe | Bool | From memory | TRUE = Indicates that you can latch data onto the Read_Data_Upper and Read_Data_Lower signals. FALSE = Indicates that you cannot latch data onto the Read_Data_Upper and Read_Data_Lower signals yet. When you issue a memory read command, the memory read operation takes more than one clock cycle to complete. When the memory read completes, the Read_Strobe signal asserts TRUE for one clock cycle. Note You must latch the Read_Data_Upper and Read_Data_Lower signals on the same clock cycle that Read_Strobe asserts. The memory controller permits you to queue multiple read commands without waiting for the first read command to complete. All read data returns from the memory controller in the order that the read commands were issued. In this situation, the Read_Strobe signal asserts once for each of the completed queued read commands. |
| Write_Data_Upper | U32 | To memory | Sets the upper 32 bits of the 64-bit data value to be written to external memory. The memory controller latches this signal value only when you issue a new memory write command by asserting the Command_Write_Enable signal. |
| Write_Data_Lower | U32 | To memory | Sets the lower 32 bits of the 64-bit data value to be written to external memory. The memory controller latches this signal value only when you issue a new memory write command by asserting the Command_Write_Enable signal. |
| Data Mask |  |  |  |
| Initialization_Done | Bool | From memory | TRUE = Indicates that the memory interface initialization sequence is completed. FALSE = Indicates that the memory interface initialization sequence is not completed. The memory controller performs its initialization sequence each time the FPGA is reprogrammed, and when the Reset Invoke Method function is called in the host VI. Note Never assert Command_Write_Enable when the Initialization_Done signal is FALSE. |

Each command that is written to the Random Access - 64 Bit memory interface is added to an internal command FIFO. This command FIFO can fill up, which drives the Command_FIFO_Full signal to TRUE. Do not issue any new commands to the Random Access - 64 Bit memory interface when the command FIFO is full.

The Random Access - 64 Bit memory interface automatically performs an initialization sequence after the FPGA is first programmed, and when the Reset Invoke Method function is called in the host VI. Do not issue new commands to the Random Access - 64 Bit memory interface before the initialization sequence is completed. The Initialization_Done signal returns to TRUE when the Random Access - 64 Bit memory interface initialization sequence is completed.

Each individual address value accesses 16 bits of data. Each write and read command writes and reads 64 bits of data, respectively. Because of this scheme, writing and reading data at consecutive addresses requires that you increment the address by 4 for each write and read command. Also, because each address value accesses 16 bits of data, the maximum number of valid addresses is equal to (Memory Size in Bytes)/2.

User_Clk

User_Clk

Note

Note

must

0

Complete the following steps to write data into the DRAM:

1. Ensure that the Command_FIFO_Full Boolean is FALSE.
2. Drive the Address signal with the DRAM memory address that you want to write.
3. Drive the Write_Data_Upper with the upper 32 bits of the 64-bit data word.
4. Drive the Write_Data_Lower with the lower 32 bits of the 64-bit data word.
5. Drive the Command signal with 0 . This communicates to the Random Access - 64 Bit memory interface to perform a memory write command.
6. Drive the Command_Write_Enable signal to TRUE for one clock cycle. You must only drive this signal for a single clock cycle if you want to only issue a single memory write command. Each clock cycle that this signal asserts causes a new write command to be issued to the Random Access - 64 Bit memory interface.

Complete the following steps to read data from DRAM:

1. Ensure that the Command_FIFO_Full Boolean is FALSE.
2. Drive the Address signal with the DRAM memory address that you want to read from.
3. Drive the Command signal with 1 . This signal communicates to the Random Access - 64 Bit memory interface to perform a memory read command.
4. Drive the Command_Write_Enable signal to TRUE for one clock cycle. You must only drive this signal for a single clock cycle if you want to only issue a single memory read command. Each clock cycle in which this signal is asserted causes a new read command to be issued to the Random Access - 64 Bit memory interface.
5. Continually monitor the state of the Read_Strobe signal. When this signal reads as TRUE, latch the 64-bit data value on the Read_Data_Upper and Read_Data_Lower signals. This contains the data most recently read from the Random Access - 64 Bit memory interface.

Note

Read_Strobe

Read_Strobe

LabVIEW contains example VIs that read and write to the Random Access - 64 Bit memory interface. To access the NI Example Finder, open LabVIEW and select Help»Find Examples, then select Hardware Input and Output»FlexRIO. You can also access device-specific examples by selecting Add device from the Hardware pull-down menu in the NI Example Finder.

Parent topic:

DRAM Memory Interface

<!--NI_TOPIC bundle=flexrio path=request-pipelining.html language=enus -->
## TOPIC 00074: Request Pipelining

- bundle_id: `flexrio`
- source_path: `request-pipelining.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/request-pipelining.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: There is a long latency between data requests and the execution of the requests due to the pipeline of the DRAM architecture. Therefore, NI recommends creating your design with a “look ahead” approach. Keep requesting the data you wish to read, without waiting for the retrieve method's data valid st

### Request Pipelining

There is a long latency between data requests and the execution of the requests due to the pipeline of the DRAM architecture.

Therefore, NI recommends creating your design with a “look ahead” approach. Keep requesting the data you wish to read, without waiting for the retrieve method's data valid strobe. The requests for reads and writes get stored in a queue inside the memory item and then passed on to the memory, which also has an internal queue where it picks out commands in order. Even though each individual request is still subject to latency and some non-determinism, you now get much higher transfer rates because DRAM can access several pieces of data sequentially instead of treating each request separately.

Parent topic:

Using DRAM Effectively with FlexRIO

<!--NI_TOPIC bundle=flexrio path=reserving-trigger-lines-for-flexrio-pxi-devic.html language=enus -->
## TOPIC 00075: Reserving Trigger Lines for FlexRIO PXI Devices

- bundle_id: `flexrio`
- source_path: `reserving-trigger-lines-for-flexrio-pxi-devic.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/reserving-trigger-lines-for-flexrio-pxi-devic.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: National Instruments recommends that you reserve the trigger lines used by FlexRIO PXI devices. If two PXI devices try to drive the same trigger line in different applications, or if the PXI devices are not programmed to work together, the application does not work and, in some cases, third-party PX

### Reserving Trigger Lines for FlexRIO PXI Devices

National Instruments recommends that you reserve the trigger lines used by FlexRIO PXI devices. If two PXI devices try to drive the same trigger line in different applications, or if the PXI devices are not programmed to work together, the application does not work and, in some cases, third-party PXI devices can be damaged. You can use Measurement & Automation Explorer (MAX) or the host VI to reserve trigger lines.

#### Reserving Trigger Lines in MAX

If you download and run the FPGA VI interactively, configure the PXI triggers in MAX. MAX maintains the trigger reservation for the FlexRIO device even after you cycle power to the PXI chassis.

#### Reserving Trigger Lines in the LabVIEW FPGA Host VI

If you download and run the FPGA VI programmatically, reserve the trigger lines in the host VI. Use the Invoke Method function to reserve the trigger and to release the trigger reservation. LabVIEW releases the trigger reservation for the FlexRIO device automatically when you close the FPGA VI reference. You must run the host VI again to reserve the trigger.

#### Reserving Trigger Lines

Complete the following steps to reserve a trigger line for a FlexRIO PXI device.

1. Place the Open FPGA VI Reference function on the block diagram and configure it for the FPGA device and FPGA VI.
2. Place the Invoke Method function on the block diagram.
3. Wire the FPGA VI Reference Out output of the Open FPGA VI Reference function to the FPGA VI Reference In input of the Invoke Method function.
4. Wire the error out output of the FPGA VI Reference function to the error in input of the Invoke Method function.
5. Click the Invoke Method function and select Reserve PXI Trigger from the shortcut menu.
6. Right-click the Trigger input and select Create»Constant . An enum constant is created to help you select the trigger.

To reserve multiple trigger lines, repeat steps 2 to 6 for each trigger line you want to reserve, wiring the FPGA VI Reference Out output of the existing Invoke Method function to the FPGA VI Reference In input of the Invoke Method node that follows it.

#### Releasing Trigger Lines

Complete the following steps to release a trigger line for a FlexRIO PXI device.

1. Place the Open FPGA VI Reference function on the block diagram and configure it for the FPGA device and FPGA VI.
2. Place the Invoke Method function on the block diagram.
3. Wire the FPGA VI Reference Out output of the Open FPGA VI Reference function to the FPGA VI Reference In input of the Invoke Method function.
4. Wire the error out output of the FPGA VI Reference function to the error in input of the Invoke Method function.
5. Click the Invoke Method function and select Unreserve PXI Trigger from the shortcut menu.
6. Right-click the Trigger input and select Create»Constant . An enum constant is created to help you select the trigger.

To release multiple trigger lines, repeat steps 2 to 6 for each trigger line you want to release, wiring the FPGA VI Reference Out output of the existing Invoke Method function to the FPGA VI Reference In input of the Invoke Method node that follows it.

Parent topic:

PXI Triggers

<!--NI_TOPIC bundle=flexrio path=streaming-data-to-and-from-disk.html language=enus -->
## TOPIC 00076: Streaming Data To and From Disk

- bundle_id: `flexrio`
- source_path: `streaming-data-to-and-from-disk.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/streaming-data-to-and-from-disk.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following guidelines provide information about how to configure your system to continuously stream data to and from disk with your FlexRIO device. These guidelines are only relevant when performing a direct memory access (DMA) to and from host memory using Host to Target DMA FIFOs and Target to

### Streaming Data To and From Disk

Note

NI Peer-to-Peer Streaming
 Help

NI recommends using the TDMS (technical data management system) API method of streaming to disk.
 Refer to *Streaming External Data to a TDMS
 File*
 in the*LabVIEW Help* for information about using TDMS to stream data to
 disk.

#### Before You Begin

Refer to the following table for a list of recommended equipment to use to achieve maximum streaming rates.

| Recommended Equipment | Description |
| --- | --- |
| 64-bit Windows operating system | A 64-bit Windows operating system allows you to allocate large DMA buffers for multiple devices. Using a 32-bit Windows operating system can cause the kernel address space to become fragmented as processes allocate and free memory. |
| Embedded or remote controller that supports 256-byte PCIe payload sizes | Most NI controllers support 256-byte PCIe payloads. Your computer's BIOS determines the maximum payload size. |
| Matched memory sticks in the embedded controller | Two DIMMs (dual in-line memory modules) provide more memory bandwidth than a single DIMM and reduce jitter on PCIe bus writes. |

#### Configuring Your Computer

Refer to the following list for information about how to configure your computer for
 maximum streaming rates.

- Size the RAID array's volume for the streaming rate you need. Refer to the
 specifications for your RAID storage system for information about throughput as
 a function of capacity. Refer to the following figure for information about the
 RAID volume required for the desired streaming rate.

|  |
| --- |

For example, a streaming rate of 2.0 GB/s requires a RAID array sized for
 approximately 15 TB. Beyond 15 TB, the stream to disk rate falls below 2.0 GB/s.

- When writing multi-terabyte files to disk, manually wait for the TDMS Reserve
 File to complete. Wait 500 ms per terabyte.
- Use TDMS Asynchronous Read and Write (Data Ref) for best performance. Use 4 to 8
 asynchronous reads or writes.
- Disable Windows services such as Application Experience, Windows Updates/Windows
 Module Installer, and Google Update, and close any other unnecessary
 applications.

Caution

#### Configuring the DMA

Refer to the following list for tips about configuring the DMA to reduce streaming rates and prevent device underflow and overflow.

- Use the Invoke Method function on a DMA FIFO to set the DMA buffer to a multiple of the read/write size you are using. The minimum DMA buffer size is 4,096 bytes. Setting the DMA buffer to a size that is not a multiple of the read/write size can drastically reduce streaming rates.
- Set the DMA buffer size to a value between 64 MB to 1 GB, depending on the read/write size and
 data throughput, to prevent device underflow or overflow. Note The DMA buffer size must be
 an exact multiple of the read/write size you are using. The minimum multiple
 size is 4,096 bytes. NI recommends using large reads and writes (for
 example, 8 MB, 16 MB, or 32 MB).

#### Configuring LabVIEW

- To reduce jitter, do not directly update LabVIEW front panel indicators from the same loop performing the DMA FIFO Read/Write. Use a separate loop to update front panel indicators.
- Use a maximum PCIe payload size of 256 bytes.

Parent topic:

Getting Started with FlexRIO

Related information:

- NI Peer-to-Peer Streaming Help
- Streaming External Data to a TDMS File

<!--NI_TOPIC bundle=flexrio path=streaming-overview.html language=enus -->
## TOPIC 00077: Streaming Overview

- bundle_id: `flexrio`
- source_path: `streaming-overview.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/streaming-overview.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Streaming Instrument Design Library provides a consistent mechanism to handle both finite and continuous transfer streams. It provides stream monitoring and handshaking. It contains VIs for both the Host and FPGA.

### Streaming Overview

The Streaming Instrument Design Library provides a consistent mechanism to handle both finite and continuous transfer streams. It provides stream monitoring and handshaking. It contains VIs for both the Host and FPGA.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=streaming-overview_2.html language=enus -->
## TOPIC 00078: Streaming Overview

- bundle_id: `flexrio`
- source_path: `streaming-overview_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/streaming-overview_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Streaming Instrument Design Library provides a consistent mechanism to handle both finite and continuous transfer streams. It provides stream monitoring and handshaking. It contains VIs for both the Host and FPGA.

### Streaming Overview

The Streaming Instrument Design Library provides a consistent mechanism to handle both finite and continuous transfer streams. It provides stream monitoring and handshaking. It contains VIs for both the Host and FPGA.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=synchronization-errors.html language=enus -->
## TOPIC 00079: Synchronization Errors

- bundle_id: `flexrio`
- source_path: `synchronization-errors.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/synchronization-errors.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following list explains the five sources of synchronization error you may encounter when you synchronize two or more devices while acquiring analog signals. Skew - the relative difference in time between when identical aligned samples are taken on synchronized devices. Drift - the amount of time

### Synchronization Errors

The following list explains the five sources of synchronization error you may encounter when you synchronize two or more devices while acquiring analog signals.

- Skew - the relative difference in time between when identical aligned samples are taken on synchronized devices.
- Drift - the amount of time that the sample time moves relative to the clock source. Devices can have low skew and low jitter but still drift.
- Sampler jitter - the amount of variability in timing between two samples on the same channel or between two channels on the same device.
- Trigger jitter - the amount of variability in timing between devices that share a trigger.
- Repeatability - describes the consistency of the errors above when the device is power cycled.

Parent topic:

PXI System Considerations

<!--NI_TOPIC bundle=flexrio path=system-monitoring-and-shutdown.html language=enus -->
## TOPIC 00080: System Monitoring and Shutdown

- bundle_id: `flexrio`
- source_path: `system-monitoring-and-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/system-monitoring-and-shutdown.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FlexRIO with Integrated I/O modules have onboard power and temperature monitoring. You can access the measurements through the FlexRIO API. This section provides information about the protection limits set to prevent device damage in the case of excessive power or temperature..

### System Monitoring and Shutdown

The FlexRIO with Integrated I/O modules have onboard power and temperature monitoring. You can access the measurements through the FlexRIO API. This section provides information about the protection limits set to prevent device damage in the case of excessive power or temperature..

Parent topic:

FlexRIO with Integrated I/O

<!--NI_TOPIC bundle=flexrio path=terminal-name-conversion-for-flexrio-devices.html language=enus -->
## TOPIC 00081: Terminal Name Conversion for FlexRIO Devices

- bundle_id: `flexrio`
- source_path: `terminal-name-conversion-for-flexrio-devices.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/terminal-name-conversion-for-flexrio-devices.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you are using LabVIEW FPGA with NI-RIO 3.1.1 or earlier, some FPGA I/O item names have been modified from their original name. The following table lists all affected terminal names. Terminal Name(NI RIO 3.2)Terminal Name(NI-RIO 3.1.1 and earlier) PXI/PXI_TrigxPXI/TRIGx PXI/PXI_CLK10PXI/CLK10PXI/P

### Terminal Name Conversion for FlexRIO Devices

If you are using LabVIEW FPGA with NI-RIO 3.1.1 or earlier, some FPGA I/O item names have been modified from their original name. The following table lists all affected terminal names.

| Terminal Name(NI RIO 3.2) | Terminal Name(NI-RIO 3.1.1 and earlier) |
| --- | --- |
| PXI/PXI_Trigx | PXI/TRIGx |
| PXI/PXI_CLK10 | PXI/CLK10 |
| PXI/PXI_Star | PXI/STAR |

Parent topic:

PXI System Considerations

<!--NI_TOPIC bundle=flexrio path=thermal-monitoring-and-shutdown.html language=enus -->
## TOPIC 00082: Thermal Monitoring and Shutdown

- bundle_id: `flexrio`
- source_path: `thermal-monitoring-and-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/thermal-monitoring-and-shutdown.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The device is protected against excessive temperatures and shuts down in the presence of excessive heat. The system responds to detected over-temperature conditions at three set levels. You can see the current FPGA temperature in MAX. You can also read temperature limits and monitor the current FP

### Thermal Monitoring and Shutdown

Note

Property Node

| 96 °C | The device driver attempts to abort the VI running on the FPGA and reconfigure the FPGA to a cooldown image. The host VI reports an error and recovery instructions. MAX also displays an error message with recovery instructions. |
| --- | --- |
| 100 °C | The FPGA reconfigures itself without driver involvement to a cooldown image. This may cause the computer connected to the FlexRIO device to crash. |
| 115 °C | Circuitry on the device cuts power to the board to prevent damage. This may cause the computer connected to the FlexRIO device to crash. |

#### Re-enabling the Device After Thermal Shutdown

To re-enable your device after thermal shutdown, download a bitfile to the FPGA or open a new session to download the default bitfile to the FPGA.

Parent topic:

System Monitoring and Shutdown

<!--NI_TOPIC bundle=flexrio path=trigger-routing.html language=enus -->
## TOPIC 00083: Trigger Routing

- bundle_id: `flexrio`
- source_path: `trigger-routing.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/trigger-routing.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Next FlexRIO devices can send and receive signals through the front panel connectors and the PXI trigger bus. The front panel connectors provide connectivity for the input and output signals and for the control lines that send and receive clocks, triggers, and events. You can use the PXI trigger bus

### Trigger Routing

Next FlexRIO devices can send and receive signals through the front panel connectors and the PXI trigger bus. The front panel connectors provide connectivity for the input and output signals and for the control lines that send and receive clocks, triggers, and events. You can use the PXI trigger bus to send and receive events, triggers, and Sample and Reference Clocks. Trigger routes are configured independently of the LabVIEW session. To route a signal, use the FlexRIO API to configure how to route the device.

Parent topic:

PXI Triggers

<!--NI_TOPIC bundle=flexrio path=user-manual-welcome.html language=enus -->
## TOPIC 00084: FlexRIO User Manual

- bundle_id: `flexrio`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/user-manual-welcome.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The FlexRIO User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### FlexRIO
 User Manual

The FlexRIO User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download FlexRIO
- FlexRIO Release Notes
- Interactive Activation Guide
- FlexRIO API Reference
- NI Learning Center

<!--NI_TOPIC bundle=flexrio path=using-dram-effectively-with-flexrio.html language=enus -->
## TOPIC 00085: Using DRAM Effectively with FlexRIO

- bundle_id: `flexrio`
- source_path: `using-dram-effectively-with-flexrio.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/using-dram-effectively-with-flexrio.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Your application design can have a dynamic impact on the throughput and storage capacity obtainable from the dynamic random access memory (DRAM) interface of the FPGA. Follow these DRAM usage recommendations to use FlexRIO DRAM more effectively.

### Using DRAM Effectively with FlexRIO

Your application design can have a dynamic impact on the throughput and storage capacity obtainable from the dynamic random access memory (DRAM) interface of the FPGA. Follow these DRAM usage recommendations to use FlexRIO DRAM more effectively.

- [Using the Correct Access Size and Frequency](using-the-correct-access-size-and-frequency.html)
- [Accessing Data Sequentially](accessing-data-sequentially.html)
- [Avoiding Multiple Memory Items Per Bank](avoiding-multipe-memory-items-per-bank.html)
- [Request Pipelining](request-pipelining.html)

Parent topic:

DRAM Interfaces

<!--NI_TOPIC bundle=flexrio path=using-the-correct-access-size-and-frequency.html language=enus -->
## TOPIC 00086: Using the Correct Access Size and Frequency

- bundle_id: `flexrio`
- source_path: `using-the-correct-access-size-and-frequency.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/using-the-correct-access-size-and-frequency.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The access size is the amount of information stored in one memory address. You can set up memory to use a variety of data types. To achieve the best performance and to utilize the maximum amount of data, use a data type that matches the access size of the device. The access size is the exact number

### Using the Correct Access Size and Frequency

The access size is the amount of information stored in one memory address. You can set up memory to use a variety of data types. To achieve the best performance and to utilize the maximum amount of data, use a data type that matches the access size of the device. The access size is the exact number of bits that are written and read in a given memory access.

The following table shows the specifications for FlexRIO targets that support FPGA-accessible DRAM, including the optimum access size.

| FlexRIO Target | Number of DRAM Banks | Size per Bank | Bandwidth per Bank | Access Size | Optimal Clock Rate |
| --- | --- | --- | --- | --- | --- |
| NI-795xR1 | 2 | 64 MB | 800 MB/s | 64 bits | 100 MHz |
| NI PXI-796xR1 | 2 | 256 MB | 1.6 GB/s | 128 bits | 100 MHz |
| NI PXI-797xR1 | 1 | 2 GB | 10.5 GB/s | 512 bits | 166 MHz |
| NI-793xR | 1 | 2 GB | 10.5 GB/s | 512 bits | 166 MHz |
| PXIe-791x1 | 2 | 2 GB | 10.5 GB/s | 512 bits | 166 MHz |

<sup>1</sup> The NI PXI-7951R, NI PXIe-7961R, NI PXIe-7971R, and PXIe-791x do not have DRAM.

If you use a data type that is smaller than the access size, the remaining bits receive an unknown and invalid value, but still get written and take up both space and bandwidth. For example, if the access size is 128 bits wide and a 32-bit data type is chosen during configuration of the DRAM, there will be 96 bits of unknown and invalid data.

The following figure shows an optimized memory element and a memory element where the data type is smaller than the access size.

[IMAGE alt='image' src='GUID-DFDF9EFB-AB78-49B6-A1CB-8FA70D50AD3B-a5.gif']

NI recommends using a data type that is the same width as the access size of the DRAM to optimize each access. Memory items accept a cluster as a data type and information can be packaged into clusters to achieve data types larger than those native to LabVIEW.

Note

Parent topic:

Using DRAM Effectively with FlexRIO

<!--NI_TOPIC bundle=flexrio path=using-the-fpga-interface-c-api-with-flexrio.html language=enus -->
## TOPIC 00087: Using the FPGA Interface C API with FlexRIO

- bundle_id: `flexrio`
- source_path: `using-the-fpga-interface-c-api-with-flexrio.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/using-the-fpga-interface-c-api-with-flexrio.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can target your FlexRIO hardware Linux Real-Time operating system from text-based development environments such as C and C++. To set up a C/C++ based toolchain, visit ni.com/info and enter the info code NILRTCrossCompile for more information.

### Using the FPGA Interface C API with FlexRIO

You can target your FlexRIO hardware Linux Real-Time operating system from text-based development environments such as C and C++. To set up a C/C++ based toolchain, visit ni.com/info and enter the info code NILRTCrossCompile for more information.

Parent topic:

Programming with FlexRIO

Related information:

- Getting Started with C/C++ Development Tools for NI Linux
 Real-Time, Eclipse Edition

<!--NI_TOPIC bundle=flexrio path=using-the-fpga-interface-c-api-with-flexrio_2.html language=enus -->
## TOPIC 00088: Using the FPGA Interface C API with FlexRIO

- bundle_id: `flexrio`
- source_path: `using-the-fpga-interface-c-api-with-flexrio_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/using-the-fpga-interface-c-api-with-flexrio_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can target your FlexRIO hardware Linux Real-Time operating system from text-based development environments such as C and C++. To set up a C/C++ based toolchain, visit ni.com/info and enter the info code NILRTCrossCompile for more information.

### Using the FPGA Interface C API with FlexRIO

You can target your FlexRIO hardware Linux Real-Time operating system from text-based development environments such as C and C++. To set up a C/C++ based toolchain, visit ni.com/info and enter the info code NILRTCrossCompile for more information.

Parent topic:

Programming with FlexRIO

<!--NI_TOPIC bundle=flexrio path=using-the-standard-functionality-for-error-in.html language=enus -->
## TOPIC 00089: Using the Standard Functionality for error in Parameters

- bundle_id: `flexrio`
- source_path: `using-the-standard-functionality-for-error-in.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/using-the-standard-functionality-for-error-in.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Some nodes, suc

### Using the Standard Functionality for error in Parameters

error in

Note

error in

error
 in

Standard error in behavior is as follows.

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The error in cluster contains the following cluster elements.

|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |

Parent topic:

Programming with FlexRIO

Related concepts:

- Using the Standard Functionality for error out Parameters

<!--NI_TOPIC bundle=flexrio path=using-the-standard-functionality-for-error-in_2.html language=enus -->
## TOPIC 00090: Using the Standard Functionality for error in Parameters

- bundle_id: `flexrio`
- source_path: `using-the-standard-functionality-for-error-in_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/using-the-standard-functionality-for-error-in_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Some nodes, suc

### Using the Standard Functionality for error in Parameters

error in

Note

error in

error
 in

Standard error in behavior is as follows.

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The error in cluster contains the following cluster elements.

|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |

Parent topic:

Programming with FlexRIO

<!--NI_TOPIC bundle=flexrio path=using-the-standard-functionality-for-error-ou.html language=enus -->
## TOPIC 00091: Using the Standard Functionality for error out Parameters

- bundle_id: `flexrio`
- source_path: `using-the-standard-functionality-for-error-ou.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/using-the-standard-functionality-for-error-ou.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard err

### Using the Standard Functionality for error out Parameters

Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

Standard error out functionality is as follows.

|  | error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

The error out cluster contains the following cluster elements.

|  | status is TRUE (X) if an error occurred before this node ran or during the running of this node or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |

Parent topic:

Programming with FlexRIO

Related concepts:

- Using the Standard Functionality for error in Parameters

<!--NI_TOPIC bundle=flexrio path=using-the-standard-functionality-for-error-ou_2.html language=enus -->
## TOPIC 00092: Using the Standard Functionality for error out Parameters

- bundle_id: `flexrio`
- source_path: `using-the-standard-functionality-for-error-ou_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/using-the-standard-functionality-for-error-ou_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard err

### Using the Standard Functionality for error out Parameters

Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

Standard error out functionality is as follows.

|  | error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

The error out cluster contains the following cluster elements.

|  | status is TRUE (X) if an error occurred before this node ran or during the running of this node or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |

Parent topic:

Programming with FlexRIO

<!--NI_TOPIC bundle=flexrio path=waveform-generation-overview.html language=enus -->
## TOPIC 00093: Waveform Generation Overview

- bundle_id: `flexrio`
- source_path: `waveform-generation-overview.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/waveform-generation-overview.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Waveform Generation Instrument Design Library allows you to generate and process waveform data.

### Waveform Generation Overview

The Waveform Generation Instrument Design Library allows you to generate and process waveform data.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO

<!--NI_TOPIC bundle=flexrio path=waveform-generation-overview_2.html language=enus -->
## TOPIC 00094: Waveform Generation Overview

- bundle_id: `flexrio`
- source_path: `waveform-generation-overview_2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio/raw/resource/enus/waveform-generation-overview_2.html
- document_id: `flexrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Waveform Generation Instrument Design Library allows you to generate and process waveform data.

### Waveform Generation Overview

The Waveform Generation Instrument Design Library allows you to generate and process waveform data.

Parent topic:

NI LabVIEW Instrument Design Libraries for FlexRIO
