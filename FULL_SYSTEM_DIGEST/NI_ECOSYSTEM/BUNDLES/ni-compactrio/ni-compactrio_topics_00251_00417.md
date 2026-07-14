# NI DOCUMENT BUNDLE: ni-compactrio

<!--NI_BUNDLE_CHUNK bundle=ni-compactrio start=251 end=417 -->
<!--NI_TOPIC bundle=ni-compactrio path=ni-9234-scan-interface.html language=enus -->
## TOPIC 00251: NI 9234 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9234-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9234-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O VariablesTo use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts. Module Channels The NI 9234 has the following channels. 237 Module

### NI 9234 (Scan Interface)

#### Module I/O Variables

To use I/O from this
 module in a VI, drag and drop I/O variables from the Project
 Explorer window to the block diagram of the VI. The I/O variables
 for the channels return calibrated floating-point data in volts.

#### Module Channels

The NI 9234 has the
 following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9234, x is 0 to 3. |

#### C Series Module Properties Dialog Box

Use this dialog box to configure the NI 9234. Right-click the NI 9234 in
 the Project Explorer window and select
 Properties to display this dialog box. You can configure
 the following options.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Channels —Specifies the channel(s) for which you want to
 select the input configuration.
- Input Configuration —Specifies the input configuration for
 the selected channel(s). You can select one of three modes: AC coupled, DC
 coupled, or IEPE AC coupled.

Parent topic:

NI 9234

<!--NI_TOPIC bundle=ni-compactrio path=ni-9234.html language=enus -->
## TOPIC 00252: NI 9234

- bundle_id: `ni-compactrio`
- source_path: `ni-9234.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9234.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, ±5 V, 51.2 KS/s, 24-Bit Software Selectable IEPE and AC/DC Analog Input Module NI 9234 Pinout 56 NI 9234 Pinout

### NI 9234

CompactRIO 4-Channel, ±5 V, 51.2 KS/s, 24-Bit Software Selectable IEPE and AC/DC Analog Input Module

#### NI 9234 Pinout

Figure 56.

[IMAGE alt='image' src='GUID-64A20CCC-0A61-491E-9C47-A17B1CFDEF7B-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9235-fpga-interface.html language=enus -->
## TOPIC 00253: NI 9235 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9235-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9235-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. You can synchronize the NI 9235 with other modules that have a selectable timebase source. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 238 Terminals in Software Terminal De

### NI 9235 (FPGA Interface)

#### FPGA
 I/O Node

reading

Note

#### Terminals in Software

Use the FPGA I/O
 Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9235 has AI channels 0 to 7. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | 12.8 MHz internal clock of the NI 9235. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9235 to access this channel. |
| Start | Channel that controls when the NI 9235 starts acquiring data. If TRUE is written to the Start channel, the NI 9235 starts acquiring data. When the NI 9235 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Start channel, no operation is performed. |
| Stop | Channel that controls when the NI 9235 stops acquiring data. If TRUE is written to the Stop channel, the NI 9235 stops acquiring data. When the NI 9235 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Stop channel, no operation is performed. |

Note

Start

Stop

labview\examples\CompactRIO\Module
 Specific\NI 9235\NI 9235 Getting Started\NI 9235 Getting
 Started.lvproj

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any
 methods.

#### I/O Properties

Use the FPGA I/O Property
 Node to access the following I/O properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in units of 100 fV/V per LSB for the channel. 100 fV is equal to 10-13 volts. Use this value to convert and calibrate NI 9235 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in units of 100 nV/V for the channel. Use this value to convert and calibrate NI 9235 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Shunt Cal Enable | Controls the shunt calibration switch for each channel. Refer to the NI 9235 Getting Started VI in the labview\\examples\\CompactRIO\\Module Specific\\NI 9235\\NI 9235 Getting Started\\NI 9235 Getting Started.lvproj for an example of using the Shunt Cal Enable property. |

#### Module Properties

Use the FPGA I/O
 Property Node to access the following module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the NI 9235 acquires data. |
| Module ID | Returns the module ID, 0x732A. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

Use the Onboard Clock
 channel in the single-cycle Timed Loop. You cannot use the other channels on the
 NI 9235 with the single-cycle Timed Loop. For information about loop timing for this
 module, refer to *Understanding Loop Timing (FPGA Interface)*.

Parent topic:

NI 9235

Related concepts:

- Understanding Loop Timing (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9235-scan-interface.html language=enus -->
## TOPIC 00254: NI 9235 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9235-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9235-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts/volts (channel voltage/excitation voltage). Module ChannelsThe NI 9

### NI 9235 (Scan Interface)

#### Module I/O Variables

To use I/O from
 this module in a VI, drag and drop I/O variables from the Project
 Explorer window to the block diagram of the VI. The I/O variables
 for the channels return calibrated floating-point data in volts/volts (channel
 voltage/excitation voltage).

#### Module Channels

The NI 9235 has the
 following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9235, x is 0 to 7. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. Right-click the NI 9235 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9235

<!--NI_TOPIC bundle=ni-compactrio path=ni-9235.html language=enus -->
## TOPIC 00255: NI 9235

- bundle_id: `ni-compactrio`
- source_path: `ni-9235.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9235.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8-Channel, 24-Bit Quarter-Bridge Analog Input Module NI 9235 Pinout 57 NI 9235 Pinout

### NI 9235

CompactRIO 8-Channel, 24-Bit Quarter-Bridge Analog Input Module

#### NI 9235 Pinout

Figure 57.

[IMAGE alt='image' src='GUID-AC36A075-118C-4960-9F32-52F7BEFDE058-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9236-fpga-interface.html language=enus -->
## TOPIC 00256: NI 9236 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9236-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9236-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. You can synchronize the NI 9236 with other modules that have a selectable timebase source. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 242 Terminals in Software Terminal Desc

### NI 9236 (FPGA Interface)

#### FPGA
 I/O Node

reading

Note

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9236 has AI channels 0 to 7. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | 12.8 MHz internal clock of the NI 9236. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9236 to access this channel. |
| Start | Channel that controls when the NI 9236 starts acquiring data. If TRUE is written to the Start channel, the NI 9236 starts acquiring data. When the NI 9236 is acquiring data, write TRUE to the Stop channel before you can access properties or TEDS information for the module. If FALSE is written to the Start channel, no operation is performed. |
| Stop | Channel that controls when the NI 9236 stops acquiring data. If TRUE is written to the Stop channel, the NI 9236 stops acquiring data. When the NI 9236 is acquiring data, write TRUE to the Stop channel before you can access properties or TEDS information for the module. If FALSE is written to the Stop channel, no operation is performed. |

Note

Start

Stop

labview\examples\CompactRIO\Module
 Specific\NI 9236\NI 9236 Getting Started\NI 9236 Getting
 Started.lvproj

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

Use the FPGA I/O Property Node to access the following I/O
 properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in units of 100 fV/V per LSB for the channel. 100 fV is equal to 10-13 volts. Use this value to convert and calibrate NI 9236 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in units of 100 nV/V for the channel. Use this value to convert and calibrate NI 9236 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Shunt Cal Enable | Controls the shunt calibration switch for each channel. Refer to the NI 9236 Getting Started VI in the labview\\examples\\CompactRIO\\Module Specific\\NI 9236\\NI 9236 Getting Started\\NI 9236 Getting Started.lvproj for an example of using the Shunt Cal Enable property. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the NI 9236 acquires data. |
| Module ID | Returns the module ID, 0x732B. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

Use the Onboard Clock
 channel in the single-cycle Timed Loop. You cannot use the other channels on the
 NI 9236 with the single-cycle Timed Loop. For information about loop timing for this
 module, refer to *Understanding Loop Timing (FPGA Interface)*.

Parent topic:

NI 9236

Related concepts:

- Understanding Loop Timing (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9236-scan-interface.html language=enus -->
## TOPIC 00257: NI 9236 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9236-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9236-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O VariablesTo use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts/volts (channel voltage/excitation voltage). Module Channels The NI 9

### NI 9236 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in volts/volts (channel voltage/excitation
 voltage).

#### Module Channels

The NI 9236 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9236, x is 0 to 7. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9236. Right-click the NI 9236 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9236

<!--NI_TOPIC bundle=ni-compactrio path=ni-9236.html language=enus -->
## TOPIC 00258: NI 9236

- bundle_id: `ni-compactrio`
- source_path: `ni-9236.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9236.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8-Channel, 24-Bit Quarter-Bridge Analog Input Module NI 9236 Pinout 58 NI 9236 pinout

### NI 9236

CompactRIO 8-Channel, 24-Bit Quarter-Bridge Analog Input Module

#### NI 9236 Pinout

Figure 58.

[IMAGE alt='image' src='GUID-AC36A075-118C-4960-9F32-52F7BEFDE058-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9237-fpga-interface.html language=enus -->
## TOPIC 00259: NI 9237 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9237-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9237-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. You can synchronize the NI 9237 with other modules that have a selectable timebase source. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 246 Terminals in Software Terminal Desc

### NI 9237 (FPGA Interface)

#### FPGA
 I/O Node

reading

Note

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9237 has AI channels 0 to 3. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | 12.8 MHz internal clock of the NI 9237. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9237 to access this channel. |
| Start | Channel that controls when the NI 9237 starts acquiring data. If TRUE is written to the Start channel, the NI 9237 starts acquiring data. When the NI 9237 is acquiring data, write TRUE to the Stop channel before you can access properties or TEDS information for the module. If FALSE is written to the Start channel, no operation is performed. |
| Stop | Channel that controls when the NI 9237 stops acquiring data.If TRUE is written to the Stop channel, the NI 9237 stops acquiring data. When the NI 9237 is acquiring data, write TRUE to the Stop channel before you can access properties or TEDS information for the module.If FALSE is written to the Stop channel, no operation is performed. |

Note

Start

Stop

labview\examples\CompactRIO\Module
 Specific\NI 9237\NI 9237 Getting Started\NI 9234 Getting
 Started.lvproj

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O Properties

Use the FPGA I/O Property
 Node to access the following I/O properties for this device.

| Property | Description |
| --- | --- |
| Half-Bridge Enable | Controls the half-bridge completion option for each channel. |
| LSB Weight | Returns the LSB weight in units of 100 fV/V per LSB for the channel. 100 fV is equal to 10-13 volts. Use this value to convert and calibrate NI 9237 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in units of 10 nV/V for the channel. Use this value to convert and calibrate NI 9237 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset Cal Enable | Enables offset calibration. This disconnects both signal input pins and forces the channel inputs to zero. |
| Shunt Cal Enable | Controls the shunt calibration switch for each channel. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the NI 9237 acquires data. |
| Excitation Voltage | Sets the excitation voltage level. All channels share the same excitation voltage. |
| Module ID | Returns the module ID, 0x73A4 (NI 9237 with DSUB) or 0x71C3 (NI 9237 with RJ-50). |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

Use the Onboard Clock
 channel in the single-cycle Timed Loop. You cannot use the other channels on the
 NI 9237 with the single-cycle Timed Loop. For information about loop timing for this
 module, refer to *Understanding Loop Timing (FPGA Interface)*.

Parent topic:

NI 9237

Related concepts:

- Understanding Loop Timing (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9237-scan-interface.html language=enus -->
## TOPIC 00260: NI 9237 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9237-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9237-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O VariablesTo use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts/volts (channel voltage/excitation voltage). Module Channels The NI 9

### NI 9237 (Scan Interface)

#### Module I/O Variables

To use I/O from this
 module in a VI, drag and drop I/O variables from the Project
 Explorer window to the block diagram of the VI. The I/O variables
 for the channels return calibrated floating-point data in volts/volts (channel
 voltage/excitation voltage).

#### Module Channels

The NI 9237 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9236, x is 0 to 3. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9237. Right-click the NI 9237 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Excitation Voltage —Specifies the excitation voltage for
 the module to output to bridges, or specifies external excitation.
- Enable Half-Bridge Completion —Enables half-bridge
 completion for individual channels.

Parent topic:

NI 9237

<!--NI_TOPIC bundle=ni-compactrio path=ni-9237.html language=enus -->
## TOPIC 00261: NI 9237

- bundle_id: `ni-compactrio`
- source_path: `ni-9237.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9237.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, 24-Bit Half/Full-Bridge Analog Input Module NI 9237 Pinout 59 NI 9237 pinout

### NI 9237

CompactRIO 4-Channel, 24-Bit Half/Full-Bridge Analog Input Module

#### NI 9237 Pinout

Figure 59.

[IMAGE alt='image' src='GUID-4AE43C13-2298-44A0-A73D-DE6E2FE28421-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9238-fpga-interface.html language=enus -->
## TOPIC 00262: NI 9238 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9238-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9238-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. You can simultaneously read from or write to multiple channels on the NI 9238. You can also synchronize an NI 9238 module with other modules that have a selectable timebase source. Terminals in SoftwareUse the FPGA I/O Nod

### NI 9238 (FPGA Interface)

#### FPGA
 I/O Node

reading

Note

selectable timebase source

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9238 has AI channels 0 to 3. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is 12.8 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9238 to access this channel. |
| Start | Channel that controls when the NI 9238 starts acquiring data. If TRUE is written to the Start channel, the NI 9238 starts acquiring data. When the NI 9238 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Start channel, no operation is performed. |
| Stop | Channel that controls when the NI 9238 stops acquiring data. If TRUE is written to the Stop channel, the NI 9238 stops acquiring data. When the NI 9238 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Stop channel, no operation is performed. |

Note

Start

Stop

labview\examples\CompactRIO\Module
 Specific\NI 9238\NI 9238 Getting Started\NI 9234 Getting
 Started.lvproj

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

Use the FPGA I/O Property Node to access the following I/O
 properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in fV/LSB for the channel. Use this value to convert and calibrate NI 9238 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in units of 100 nV/V for the channel. Use this value to convert and calibrate NI 9238 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the NI 9238 acquires data. |
| Module ID | Returns the module ID, 0x7750. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

Use the Onboard Clock
 channel in the single-cycle Timed Loop. You cannot use the other channels on the
 NI 9238 with the single-cycle Timed Loop. For information about loop timing for this
 module, refer to *Understanding Loop Timing (FPGA Interface)*.

Parent topic:

NI 9238

Related concepts:

- Understanding Loop Timing (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9238.html language=enus -->
## TOPIC 00263: NI 9238

- bundle_id: `ni-compactrio`
- source_path: `ni-9238.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9238.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, ±0.5 V, 24-Bit Simultaneous Analog Input Module NI 9238 Pinout 60 NI 9238 Pinout NI-9238 Pinouts

### NI 9238

CompactRIO 4-Channel, ±0.5 V, 24-Bit Simultaneous Analog Input Module

#### NI 9238 Pinout

Figure 60.

[IMAGE alt='NI-9238 Pinouts' src='GUID-D17534D5-234D-4909-A0E1-A56E450ECD00-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9239-fpga-interface.html language=enus -->
## TOPIC 00264: NI 9239 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9239-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9239-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. You can simultaneously read from or write to multiple channels on the NI 9239. You also can synchronize the NI 9239 module with other modules that have a selectable timebase source. Terminals in SoftwareUse the FPGA I/O Node

### NI 9239 (FPGA Interface)

#### FPGA
 I/O Node

reading

Note

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9239 has AI channels 0 to 3. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is 12.8 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9239 to access this channel. |
| Start | Channel that controls when the NI 9239 starts acquiring data. If TRUE is written to the Start channel, the NI 9239 starts acquiring data. When the NI 9239 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Start channel, no operation is performed. |
| Stop | Channel that controls when the NI 9239 stops acquiring data. If TRUE is written to the Stop channel, the NI 9239 stops acquiring data. When the NI 9239 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Stop channel, no operation is performed. |

Note

Start

Stop

labview\examples\CompactRIO\Module
 Specific\NI 9239\NI 9239 Getting Started\NI 9239 Getting
 Started.lvproj

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

Use the FPGA I/O Property Node to access the following I/O
 properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in pV/LSB for the channel. Use this value to convert and calibrate NI 9239 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in units of 100 nV/V for the channel. Use this value to convert and calibrate NI 9239 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the NI 9239 acquires data. |
| Module ID | Returns the module ID, 0x71C2. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

Use the Onboard Clock
 channel in the single-cycle Timed Loop. You cannot use the other channels on the
 NI 9239 with the single-cycle Timed Loop. For information about loop timing for this
 module, refer to *Understanding Loop Timing (FPGA Interface)*.

Parent topic:

NI 9239

Related concepts:

- Understanding Loop Timing (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9239-scan-interface.html language=enus -->
## TOPIC 00265: NI 9239 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9239-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9239-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O VariablesTo use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts. Module Channels The NI 9239 has the following channels. 256 Module

### NI 9239 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in volts.

#### Module Channels

The NI 9239 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9239, x is 0 to 3. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9239. Right-click the NI 9239 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9239

<!--NI_TOPIC bundle=ni-compactrio path=ni-9239.html language=enus -->
## TOPIC 00266: NI 9239

- bundle_id: `ni-compactrio`
- source_path: `ni-9239.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9239.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, ±10 V, 24-Bit Simultaneous Analog Input Module NI 9239 Pinout 61 NI 9239 pinout NI-9229 Pinouts

### NI 9239

CompactRIO 4-Channel, ±10 V, 24-Bit Simultaneous Analog Input Module

#### NI 9239 Pinout

Figure 61.

[IMAGE alt='NI-9229 Pinouts' src='GUID-A513F836-0E9D-4BB4-B551-7D52B84E88D2-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9242-fpga-interface.html language=enus -->
## TOPIC 00267: NI 9242 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9242-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9242-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. You can simultaneously read from or write to multiple channels on the NI 9242. You can also synchronize an NI 9242 module with other modules that have a selectable timebase source. Terminals in SoftwareUse the FPGA I/O Node

### NI 9242 (FPGA Interface)

#### FPGA
 I/O Node

reading

Note

selectable timebase source

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9242 has AI channels 0 to 2. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Neutral | Neutral input channel. Do not access Neutral channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is 12.8 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9242 to access this channel. |
| Start | Channel that controls when the NI 9242 starts acquiring data. If TRUE is written to the Start channel, the NI 9242 starts acquiring data. When the NI 9242 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Start channel, no operation is performed. |
| Stop | Channel that controls when the NI 9242 stops acquiring data. If TRUE is written to the Stop channel, the NI 9242 stops acquiring data. When the NI 9242 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Stop channel, no operation is performed. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

This device does not support any I/O 0roperties.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the NI 9242 acquires data. |
| Module ID | Returns the module ID, 0x772A. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

Use the Onboard Clock
 channel in the single-cycle Timed Loop. You cannot use the other channels on the
 NI 9242 with the single-cycle Timed Loop. For information about loop timing for this
 module, refer to *Understanding Loop Timing (FPGA Interface)*.

Parent topic:

NI 9242

Related concepts:

- Understanding Loop Timing (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9242-scan-interface.html language=enus -->
## TOPIC 00268: NI 9242 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9242-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9242-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O VariablesTo use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts. Module Channels The NI 9242 has the following channels. 259 Module

### NI 9242 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in volts.

#### Module Channels

The NI 9242 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9242, x is 0 to 2. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9242. Right-click the NI 9242 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Data Rate —Specifies the rate at which the NI 9242
 acquires and returns data. The data rate must remain within the appropriate data
 rate range listed in NI 9242 hardware documentation on
 ni.com/manuals .

Parent topic:

NI 9242

<!--NI_TOPIC bundle=ni-compactrio path=ni-9242.html language=enus -->
## TOPIC 00269: NI 9242

- bundle_id: `ni-compactrio`
- source_path: `ni-9242.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9242.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, 250 V[rms], 24-Bit Simultaneous Analog Input Module NI 9242 Pinout 62 NI 9242 pinout

### NI 9242

CompactRIO 4-Channel, 250 V<sub>rms</sub>, 24-Bit Simultaneous Analog Input Module

#### NI 9242 Pinout

Figure 62.

[IMAGE alt='image' src='GUID-ED9A6198-C438-4E20-9211-7D824EB8AA72-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9244-fpga-interface.html language=enus -->
## TOPIC 00270: NI 9244 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9244-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9244-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. You can simultaneously read from or write to multiple channels on the NI 9244. You can also synchronize an NI 9244 module with other modules that have a selectable timebase source. Terminals in SoftwareUse the FPGA I/O Node

### NI 9244 (FPGA Interface)

#### FPGA
 I/O Node

reading

Note

selectable timebase source

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9244 has AI channels 0 to 2. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Neutral | Neutral input channel. Do not access Neutral channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is 12.8 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9244 to access this channel. |
| Start | Channel that controls when the NI 9244 starts acquiring data. If TRUE is written to the Start channel, the NI 9244 starts acquiring data. When the NI 9244 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Start channel, no operation is performed. |
| Stop | Channel that controls when the NI 9244 stops acquiring data. If TRUE is written to the Stop channel, the NI 9244 stops acquiring data. When the NI 9244 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Stop channel, no operation is performed. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

This device does not support any I/O 0roperties.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the NI 9244 acquires data. |
| Module ID | Returns the module ID, 0x76E8. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

Use the Onboard Clock
 channel in the single-cycle Timed Loop. You cannot use the other channels on the
 NI 9244 with the single-cycle Timed Loop. For information about loop timing for this
 module, refer to *Understanding Loop Timing (FPGA Interface)*.

Parent topic:

NI 9244

Related concepts:

- Understanding Loop Timing (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9244-max-rate-synch.html language=enus -->
## TOPIC 00271: NI 9244

- bundle_id: `ni-compactrio`
- source_path: `ni-9244-max-rate-synch.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9244-max-rate-synch.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 9244 derives its sample rate from the internal master timebase. 76 NI 9244 internal master timebase and sample rate Internal master timebase 12.8 MHz Maximum sample rate when using the internal master timebase 50 kS/s (12.8 MHz/256) When the module uses the internal master timebase, it can no

### NI 9244

The NI 9244 derives its sample rate from the internal
 master timebase.

| Internal master timebase | 12.8 MHz |
| --- | --- |
| Maximum sample rate when using the internal master timebase | 50 kS/s (12.8 MHz/256) |

When the module uses the internal master timebase, it can not be sourced to different
 model types for synchronization.

When synchronizing multiple modules, the maximum sample rate of the slave module depends
 on the frequency of the master module's internal master timebase. The maximum sample
 rate of the system is the lowest sample rate of all the modules being synchronized.

The following table lists the NI 9244 maximum sample rate
 when it is configured to use the master timebase source.

| Master module | Slave NI 9244 maximum sample rate |
| --- | --- |
| NI 9202 NI 9225 NI 9227 NI 9229 NI 9233 NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 NI 9242 NI 9244 NI 9252 NI 9253 NI 9470 NI 9775 | 50 kS/s |
| NI 9218 NI 9230 NI 9231 NI 9232 NI 9234 NI 9246 NI 9247 NI 9250 NI 9251 NI 9260 | 51.2 kS/s |

Parent topic:

Understanding the Maximum Sample Rate When Synchronizing Multiple Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9244-scan-interface.html language=enus -->
## TOPIC 00272: NI 9244 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9244-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9244-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O VariablesTo use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts. Module Channels The NI 9244 has the following channels. 262 Module

### NI 9244 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in volts.

#### Module Channels

The NI 9244 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9244, x is 0 to 2. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9244. Right-click the NI 9244 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Data Rate —Specifies the rate at which the NI 9244
 acquires and returns data. The data rate must remain within the appropriate data
 rate range listed in NI 9244 hardware documentation on
 ni.com/manuals .

Parent topic:

NI 9244

<!--NI_TOPIC bundle=ni-compactrio path=ni-9244.html language=enus -->
## TOPIC 00273: NI 9244

- bundle_id: `ni-compactrio`
- source_path: `ni-9244.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9244.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, 400 V[rms] L-N, 800 V[rms] L-L, 24-Bit Simultaneous Analog Input Module NI 9244 Pinout 63 NI 9244 pinout

### NI 9244

CompactRIO 4-Channel, 400 V<sub>rms</sub> L-N, 800 V<sub>rms</sub> L-L, 24-Bit Simultaneous Analog Input Module

#### NI 9244 Pinout

Figure 63.

[IMAGE alt='image' src='GUID-ED9A6198-C438-4E20-9211-7D824EB8AA72-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9246-fpga-interface.html language=enus -->
## TOPIC 00274: NI 9246 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9246-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9246-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. You can simultaneously read from or write to multiple channels on the NI 9246. You can also synchronize an NI 9246 module with other modules that have a selectable timebase source. Terminals in SoftwareUse the FPGA I/O Node

### NI 9246 (FPGA Interface)

#### FPGA
 I/O Node

reading

Note

selectable timebase source

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9246 has AI channels 0 to 2. Do not access AI channels on multiple modules in the same FPGA I/O Node if the modules are not synchronized or do not use the same data rate. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is 13.1 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9246 to access this channel. |
| Start | Channel that controls when the NI 9246 starts acquiring data. If TRUE is written to the Start channel, the NI 9246 starts acquiring data. When the NI 9246 is acquiring data, write TRUE to the Stop channel before you can access properties information for the module. If FALSE is written to the Start channel, no operation is performed. |
| Stop | Channel that controls when the NI 9246 stops acquiring data. If TRUE is written to the Stop channel, the NI 9246 stops acquiring data. When the NI 9246 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Stop channel, no operation is performed. |

Note

Start

Stop

labview\examples\CompactRIO\Module
 Specific\NI 9246\NI 9246 Getting Started\NI 9234 Getting
 Started.lvproj

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Methods

This device does not support any methods.

#### I/O
 Properties

Use the FPGA I/O Property Node to access the following I/O
 properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in pV/LSB for the channel. Use this value to convert and calibrate NI 9246 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in µV for the channel. Use this value to convert and calibrate NI 9246 data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the NI 9246 acquires data. |
| Module ID | Returns the module ID, 0x77E3. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

Use the Onboard Clock
 channel in the single-cycle Timed Loop. You cannot use the other channels on the
 NI 9246 with the single-cycle Timed Loop. For information about loop timing for this
 module, refer to *Understanding Loop Timing (FPGA Interface)*.

Parent topic:

NI 9246

Related concepts:

- Understanding Loop Timing (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9247-max-rate-synch.html language=enus -->
## TOPIC 00275: NI 9247

- bundle_id: `ni-compactrio`
- source_path: `ni-9247-max-rate-synch.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9247-max-rate-synch.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 9247 derives its sample rate from the internal master timebase. 80 NI 9247 internal master timebase and sample rate Internal master timebase 13.1072 MHz Maximum sample rate when using the internal master timebase 51.2 kS/s (13.1072 MHz/256) When the module uses the internal master timebase, i

### NI 9247

The NI 9247 derives its sample rate from the internal
 master timebase.

| Internal master timebase | 13.1072 MHz |
| --- | --- |
| Maximum sample rate when using the internal master timebase | 51.2 kS/s (13.1072 MHz/256) |

When the module uses the internal master timebase, it can not be sourced to different
 model types for synchronization.

When synchronizing multiple modules, the maximum sample rate of the slave module depends
 on the frequency of the master module's internal master timebase. The maximum sample
 rate of the system is the lowest sample rate of all the modules being synchronized.

The following table lists the NI 9247 maximum sample rate
 when it is configured to use the master timebase source.

| Master module | Slave NI 9247 maximum sample rate |
| --- | --- |
| NI 9202 NI 9225 NI 9227 NI 9229 NI 9233 NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 NI 9242 NI 9244 NI 9252 NI 9253 NI 9470 NI 9775 | 50 kS/s |
| NI 9218 NI 9230 NI 9231 NI 9232 NI 9234 NI 9246 NI 9247 NI 9250 NI 9251 NI 9260 | 51.2 kS/s |

Parent topic:

Understanding the Maximum Sample Rate When Synchronizing Multiple Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9250-fpga-interface.html language=enus -->
## TOPIC 00276: NI 9250 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9250-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9250-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. You can synchronize the NI 9250 module with other modules that have a selectable timebase source. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 272 Terminals in Software Termin

### NI 9250 (FPGA Interface)

#### FPGA
 I/O Node

reading

Note

#### Terminals in Software

Use the FPGA I/O
 Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9250 has AI channels 0 to 1. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is 13.1072 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9250 to access this channel. |
| Start | Channel that controls when the NI 9250 starts acquiring data. If TRUE is written to the Start channel, the NI 9250 starts acquiring data. When the NI 9250 is acquiring data, write TRUE to the Stop channel before you can access properties information for the module. If FALSE is written to the Start channel, no operation is performed. |
| Stop | Channel that controls when the NI 9250 stops acquiring data. If TRUE is written to the Stop channel, the NI 9250 stops acquiring data. When the NI 9250 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Stop channel, no operation is performed. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### I/O
 Properties

Use the FPGA I/O Property Node to access the following I/O
 properties for this device.

| Property | Description |
| --- | --- |
| Input Configuration | Sets the input configuration of the corresponding channel to one of three modes: AC Coupled, DC Coupled, IEPE AC Coupled. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the NI 9250 acquires data. |
| Module ID | Returns the module ID, 0x77EA. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9250

<!--NI_TOPIC bundle=ni-compactrio path=ni-9250-max-rate-synch.html language=enus -->
## TOPIC 00277: NI 9250

- bundle_id: `ni-compactrio`
- source_path: `ni-9250-max-rate-synch.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9250-max-rate-synch.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 9250 derives its sample rate from the internal master timebase. 82 NI 9250 internal master timebase and sample rate Internal master timebase 13.1072 MHz Maximum sample rate when using the internal master timebase 102.4 kS/s (13.1072 MHz/128) When the module uses the internal master timebase,

### NI 9250

The NI 9250 derives its sample rate from the internal
 master timebase.

| Internal master timebase | 13.1072 MHz |
| --- | --- |
| Maximum sample rate when using the internal master timebase | 102.4 kS/s (13.1072 MHz/128) |

When the module uses the internal master timebase, it can not be sourced to different
 model types for synchronization.

When synchronizing multiple modules, the maximum sample rate of the slave module depends
 on the frequency of the master module's internal master timebase. The maximum sample
 rate of the system is the lowest sample rate of all the modules being synchronized.

The following table lists the NI 9250 maximum sample rate
 when it is configured to use the master timebase source.

| Master module | Slave NI 9250 maximum sample rate |
| --- | --- |
| NI 9202 NI 9225 NI 9227 NI 9229 NI 9233 NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 NI 9242 NI 9244 NI 9252 NI 9253 NI 9470 NI 9775 | 100 kS/s |
| NI 9218 NI 9230 NI 9231 NI 9232 NI 9234 NI 9246 NI 9247 NI 9250 NI 9251 NI 9260 | 102.4 kS/s |

Parent topic:

Understanding the Maximum Sample Rate When Synchronizing Multiple Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9251-max-rate-synch.html language=enus -->
## TOPIC 00278: NI 9251

- bundle_id: `ni-compactrio`
- source_path: `ni-9251-max-rate-synch.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9251-max-rate-synch.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 9251 derives its sample rate from the internal master timebase. 84 NI 9251 internal master timebase and sample rate Internal master timebase 13.1072 MHz Maximum sample rate when using the internal master timebase 102.4 kS/s (13.1072 MHz/128) When the module uses the internal master timebase,

### NI 9251

The NI 9251 derives its sample rate from the internal
 master timebase.

| Internal master timebase | 13.1072 MHz |
| --- | --- |
| Maximum sample rate when using the internal master timebase | 102.4 kS/s (13.1072 MHz/128) |

When the module uses the internal master timebase, it can not be sourced to different
 model types for synchronization.

When synchronizing multiple modules, the maximum sample rate of the slave module depends
 on the frequency of the master module's internal master timebase. The maximum sample
 rate of the system is the lowest sample rate of all the modules being synchronized.

The following table lists the NI 9251 maximum sample rate
 when it is configured to use the master timebase source.

| Master module | Slave NI 9251 maximum sample rate |
| --- | --- |
| NI 9202 NI 9225 NI 9227 NI 9229 NI 9233 NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 NI 9242 NI 9244 NI 9252 NI 9253 NI 9470 NI 9775 | 100 kS/s |
| NI 9218 NI 9230 NI 9231 NI 9232 NI 9234 NI 9246 NI 9247 NI 9250 NI 9251 NI 9260 | 102.4 kS/s |

Parent topic:

Understanding the Maximum Sample Rate When Synchronizing Multiple Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9251.html language=enus -->
## TOPIC 00279: NI 9251

- bundle_id: `ni-compactrio`
- source_path: `ni-9251.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9251.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 2-Channel, 3 Vrms, 24-Bit Differential Analog Input Module NI 9251 Pinout 67 NI 9251 pinout

### NI 9251

CompactRIO 2-Channel, 3 Vrms, 24-Bit Differential Analog Input Module

#### NI 9251 Pinout

Figure 67.

[IMAGE alt='image' src='GUID-E70E3106-7BA4-4472-9D1E-D8AA1AC0468A-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9252-fpga-interface.html language=enus -->
## TOPIC 00280: NI 9252 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9252-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9252-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 278 Terminals in Software Terminal Description AIx Analog input channel x, where x is the number of the channel. The NI 9252 has c

### NI 9252 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for reading
 with this device.

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9252 has channels 0 to 7. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is 12.8 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9252 to access this channel. |
| Start | Channel that controls when the NI 9252 starts acquiring data. If TRUE is written to the Start channel, the NI 9252 starts acquiring data. When the NI 9252 is acquiring data, write TRUE to the Stop channel before you can access properties information for the module. If FALSE is written to the Start channel, no operation is performed. |
| Stop | Channel that controls when the NI 9252 stops acquiring data. If TRUE is written to the Stop channel, the NI 9252 stops acquiring data. When the NI 9252 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Stop channel, no operation is performed. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the NI 9252 acquires data. |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |
| Filter Response | Sets the AI filter types supported by the device. The filters supported by this module are the Comb (default) and Butterworth filter. |
| Filter Order | Sets the Filter Order for the Butterworth filter. This setting would only take effect if the module is currently configured to the Butterworth filter. |
| Filter Frequency | Sets the AI filter's cutoff frequency. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9252

<!--NI_TOPIC bundle=ni-compactrio path=ni-9252-max-rate-synch.html language=enus -->
## TOPIC 00281: NI 9252

- bundle_id: `ni-compactrio`
- source_path: `ni-9252-max-rate-synch.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9252-max-rate-synch.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 9252 derives its sample rate from the internal master timebase. 86 NI 9252 internal master timebase and sample rate Internal master timebase 12.8 MHz Maximum sample rate when using the internal master timebase 50 kS/s (12.8 MHz/256) When the module uses the internal master timebase, it can no

### NI 9252

The NI 9252 derives its sample rate from the internal
 master timebase.

| Internal master timebase | 12.8 MHz |
| --- | --- |
| Maximum sample rate when using the internal master timebase | 50 kS/s (12.8 MHz/256) |

When the module uses the internal master timebase, it can not be sourced to different
 model types for synchronization.

When synchronizing multiple modules, the maximum sample rate of the slave module depends
 on the frequency of the master module's internal master timebase. The maximum sample
 rate of the system is the lowest sample rate of all the modules being synchronized.

The following table lists the NI 9252 maximum sample rate
 when it is configured to use the master timebase source.

| Master module | Slave NI 9252 maximum sample rate |
| --- | --- |
| NI 9202 NI 9225 NI 9227 NI 9229 NI 9233 NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 NI 9242 NI 9244 NI 9252 NI 9253 NI 9470 NI 9775 | 50 kS/s |
| NI 9218 NI 9230 NI 9231 NI 9232 NI 9234 NI 9246 NI 9247 NI 9250 NI 9251 NI 9260 | 51.2 kS/s |

Parent topic:

Understanding the Maximum Sample Rate When Synchronizing Multiple Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9252.html language=enus -->
## TOPIC 00282: NI 9252

- bundle_id: `ni-compactrio`
- source_path: `ni-9252.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9252.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8-Channel, ±10 V, 24-Bit Differential Analog Input Module NI 9252 Pinout 68 NI 9252 Pinout

### NI 9252

CompactRIO 8-Channel, ±10 V, 24-Bit Differential Analog Input Module

#### NI 9252 Pinout

Figure 68.

[IMAGE alt='image' src='GUID-70CDD891-04B0-43B3-8364-4299FEF40B46-a5.svg']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9253-fpga-interface.html language=enus -->
## TOPIC 00283: NI 9253 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9253-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9253-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 280 Terminals in Software Terminal Description AIx Analog input channel x, where x is the number of the channel. The NI 9253 has c

### NI 9253 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for reading
 with this device.

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9253 has channels 0 to 7. |
| Onboard Clock | Gives access to the onboard clock in the LabVIEW block diagram. The Onboard Clock frequency is 12.8 MHz. Use the FPGA I/O Node in a single-cycle Timed Loop to access this channel. Export the Onboard Clock of the NI 9253 to access this channel. |
| Start | Channel that controls when the NI 9253 starts acquiring data. If TRUE is written to the Start channel, the NI 9253 starts acquiring data. When the NI 9253 is acquiring data, write TRUE to the Stop channel before you can access properties information for the module. If FALSE is written to the Start channel, no operation is performed. |
| Stop | Channel that controls when the NI 9253 stops acquiring data. If TRUE is written to the Stop channel, the NI 9253 stops acquiring data. When the NI 9253 is acquiring data, write TRUE to the Stop channel before you can access properties for the module. If FALSE is written to the Stop channel, no operation is performed. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### Module Methods

Use the FPGA I/O Method
 Node to access the following module method for this device.

| Method | Description |
| --- | --- |
| Check Cached Status | Returns Booleans for each channel that indicate whether there was a input limits fault, overcurrent, or field side power fault on the channel since the last execution of the Check Cached Status method. When the FPGA I/O Node reads the channels, the FPGA VI determines the state of the channels and caches any TRUE value until the Check Cached Status method executes. Channel Input Limits Fault—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index detected the channel input is out of range of Lower Fault Detection Limit and Upper Fault Detection Limit on the channel at some point after the last time that the Check Cached Status method executed. Channel Overcurrent—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index detected an overcurrent on the channel at some point after the last time that the Check Cached Status method executed. Field-Side Power Fault—Returns a single Boolean value. A value of TRUE indicates that the module detected Field-Side Power Fault on the module at some point after the last time that the Check Cached Status method executed. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Data Rate | Sets the rate at which the NI 9253 acquires data. |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |
| Filter Response | Sets the AI filter types supported by the device. The filters supported by this module are the Comb (default) and Butterworth filter. |
| Filter Order | Sets the Filter Order for the Butterworth filter. This setting would only take effect if the module is currently configured to the Butterworth filter. |
| Filter Frequency | Sets the AI filter's cutoff frequency. |
| Field-Side Power Fault Detection Enable | Enables the module to detect Field-Side Power Supplied to the module. Set the input to TRUE to enable Field-Side Power Fault Detection. Set the input to FALSE (default) to disable Field-Side Power Fault Detection. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9253

<!--NI_TOPIC bundle=ni-compactrio path=ni-9253-max-rate-synch.html language=enus -->
## TOPIC 00284: NI 9253

- bundle_id: `ni-compactrio`
- source_path: `ni-9253-max-rate-synch.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9253-max-rate-synch.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI 9253 derives its sample rate from the internal master timebase. 88 NI 9253 internal master timebase and sample rate Internal master timebase 12.8 MHz Maximum sample rate when using the internal master timebase 50 kS/s (12.8 MHz/256) When the module uses the internal master timebase, it can no

### NI 9253

The NI 9253 derives its sample rate from the internal
 master timebase.

| Internal master timebase | 12.8 MHz |
| --- | --- |
| Maximum sample rate when using the internal master timebase | 50 kS/s (12.8 MHz/256) |

When the module uses the internal master timebase, it can not be sourced to different
 model types for synchronization.

When synchronizing multiple modules, the maximum sample rate of the slave module depends
 on the frequency of the master module's internal master timebase. The maximum sample
 rate of the system is the lowest sample rate of all the modules being synchronized.

The following table lists the NI 9253 maximum sample rate
 when it is configured to use the master timebase source.

| Master module | Slave NI 9253 maximum sample rate |
| --- | --- |
| NI 9202 NI 9225 NI 9227 NI 9229 NI 9233 NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 NI 9242 NI 9244 NI 9252 NI 9253 NI 9470 NI 9775 | 50 kS/s |
| NI 9218 NI 9230 NI 9231 NI 9232 NI 9234 NI 9246 NI 9247 NI 9250 NI 9251 NI 9260 | 51.2 kS/s |

Parent topic:

Understanding the Maximum Sample Rate When Synchronizing Multiple Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9253-scan-interface.html language=enus -->
## TOPIC 00285: NI 9253 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9253-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9253-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O VariablesTo use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in amps. Module Channels The NI 9253 has the following channels. 283 Module C

### NI 9253 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in amps.

#### Module Channels

The NI 9253 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9253, x is 0 to 7. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9253. Right-click the NI 9253 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Data Rate —Sets the rate at which the module acquires
 data.
- Filter Response —Sets the AI filter types supported by the
 device. The filters supported by this module are the Comb 
 filter (default) and Butterworth filter.
- Filter Order —Sets the Filter Order for the Butterworth
 filter. This setting takes effect when the module is configured to the
 Butterworth filter.
- Filter Frequency —Sets the AI filter's cutoff
 frequency.
- Diagnostic Settings —You can set the following diagnostic
 functions for the module.
  - Module Settings
    - Field-side Power Fault Detection
 Enable —Enable the module to detect
 Field-Side Power Supplied to the module.
 Select the checkbox to enable Field-Side Power Fault Detection.
 Uncheck the checkbox to disable (default) Field-Side Power Fault
 Detection.
  - Channel Configuration
    - Input Limits Fault Detection
 Enable —Enable the module to detect an Input Limit
 Fault on the corresponding channel. Select the checkbox to
 enable Input Limits Fault Detection. Unselect (default) to
 disable Input Limits Fault Detection.
    - Lower Fault Detection Limit —Sets the
 Channel's Lower Fault Detection Limit of the corresponding
 channel. The range of valid current limit values is 0—0.0219 A
 (default value is 0.0 A).
    - Upper Fault Detection Limit —Sets the
 Channel's Upper Fault Detection Limit of the corresponding
 channel. The range of valid current limit values is 0—0.0219 A
 (default value is 0.0219 A).

#### Module Methods

Use the Invoke Node to
 access the following module properties for this device.

| Method | Description |
| --- | --- |
| Check Cached Status | Returns Booleans for each channel that indicate whether there was an input limits fault, overcurrent, or field side power fault on the channel since the last execution of the Check Cached Status method. When I/O variables or shared variables read the channels, the scan driver determines the state of the channels and caches any TRUE value until the Check Cached Status method executes. Channel Input Limits Fault—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index detected the channel input is out of range of Lower Fault Detection Limit and Upper Fault Detection Limit on the channel at some point after the last time that the Check Cached Status method executed. Channel Overcurrent—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index detected an overcurrent on the channel at some point after the last time that the Check Cached Status method executed. Field-Side Power Fault—Returns a single Boolean value. A value of TRUE indicates that the module detected Field-Side Power Fault on the module at some point after the last time that the Check Cached Status method executed. |

Parent topic:

NI 9253

<!--NI_TOPIC bundle=ni-compactrio path=ni-9266-fpga-interface.html language=enus -->
## TOPIC 00286: NI 9266 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9266-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9266-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for writing with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 320 Terminals in Software Terminal Description AOx Analog output channel x, where x is the number of the channel. The NI 9266 has

### NI 9266 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for writing
 with this device.

#### Terminals in Software

Use the FPGA I/O
 Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AOx | Analog output channel x, where x is the number of the channel. The NI 9266 has AO channels 0 to 7. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### I/O
 Methods

This device does not support any I/O methods.

#### Module Methods

Use the FPGA I/O Method Node to access the following
 module methods for this device.

Refer to the NI 9266 Getting Started
 VI in the labview\examples\CompactRIO\Module Specific\NI
 9266\NI 9266 Getting Started\NI 9266 Getting Started.lvproj for an
 example of using the Check Output Status methods.

Update

Wait for Update

Write
 Data

- The Write Data method stores data values before writing
 the data to a channel,
- The Update method writes the stored data values to the
 output channel.
- The Wait for Update method waits until the
 Update method updates the output channels.

Refer to the NI 9264 Advanced Write Methods VI in the
 labview\examples\CompactRIO\Module Specific\NI 9264\NI 9264 Advanced
 Write Methods\NI 9264 Advanced Write Methods.lvproj for an example of
 using the Update, Wait for Update, and
 Write Data methods.

| Method | Description |
| --- | --- |
| Check Cached Output Status | Returns Booleans that indicate whether the module or channels reported a power supply fault or an open current loop since the last execution of the Check Cached Output Status method. When the FPGA I/O Node communicates with the module, the FPGA VI samples the states of the module and channels and caches any TRUE value until the Check Cached Output Status method executes. Force Status Read—When the value of this input is FALSE, the method returns the cached status information since the last time that the Check Cached Output Status method executed. When the value is TRUE, the method forces the FPGA I/O Node to communicate with the module and update the status information. Forcing a status read can introduce jitter into an analog output loop. Any Fault—Returns a Boolean value. A value of TRUE indicates that the module has a power supply fault or at least one channel has an open current loop. Power Supply Fault—Returns a Boolean value. A value of TRUE indicates that the external power supply is out of the expected range. Open Current Loop—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index has an open current loop and is configured to output a nonzero current value. |
| Check Output Status | Returns Booleans that indicate whether the module or channels reported a power supply fault or an open current loop during the last time the FPGA I/O Node communicated with the module. When the FPGA I/O Node communicates with the module, the FPGA VI samples the states of the module and channels and overwrites the previous output status with the latest state of the module and channels. Force Status Read—When the value of this input is FALSE, the method returns the status information from the last time the FPGA I/O Node communicated with the module. When the value is TRUE, the method forces the FPGA I/O Node to communicate with the module and update the status information. Forcing a status read can introduce jitter into an analog output loop. Any Fault—Returns a Boolean value. A value of TRUE indicates that the module has a power supply fault or at least one channel has an open current loop. Power Supply Fault—Returns a Boolean value. A value of TRUE indicates that the external power supply is out of the expected range. Open Current Loop—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index has an open current loop and is configured to output a nonzero current value. |
| Update | Writes stored data values to the output channel. Overrun—Returns a Boolean value. A value of TRUE indicates an overrun warning. The overrun warning means that the Update method is trying to run while the Write Data method is running, typically in a different loop. Either the Write Data method is writing data to the module too quickly or the Update method is running too slowly. Underflow—Returns a Boolean value. A value of TRUE indicates an underflow warning. The underflow warning means that the Write Data method has not written new data to the module since the last time the Update method ran. Either the Write Data method is writing data to the module too slowly or the Update method is running too quickly. |
| Wait for Update | Waits until the Update method updates the output channels. Timeout (Ticks)—Specifies in FPGA clock ticks how long the Wait for Update method waits for the Update method to update the output channels. A value of 0 causes the Wait for Update method to time out immediately. A negative value causes the Wait for Update method to wait indefinitely. A positive value causes the Wait for Update method to wait for that number of clock ticks before timing out. Timeout Occurred?—Returns a Boolean value. A value of TRUE indicates that a timeout occurred. |
| Write Data | Stores data values before writing the data to a channel. Channel—Specifies the channel to which you want to write data. Data—Specifies the data you want to write to the channel. |

#### I/O
 Properties

Use the FPGA I/O Property Node to access the following I/O
 properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in pA/LSB for the channel. Use this value to convert module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in pA for the channel. Use this value to convert module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9266

Related concepts:

- Converting Current Values to Binary Values for the NI 9266 (FPGA Interface)
- Writing to C Series Channels

<!--NI_TOPIC bundle=ni-compactrio path=ni-9266-scan-interface.html language=enus -->
## TOPIC 00287: NI 9266 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9266-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9266-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables write floating-point values to the channels in volts. Module ChannelsThe NI 9266 has the following channels. 324 Module Channels Ch

### NI 9266 (Scan Interface)

#### Module I/O Variables

To
 use I/O from this module in a VI, drag and drop I/O variables from the
 Project Explorer window to the block diagram of the VI.
 The I/O variables write floating-point values to the channels in volts.

#### Module Channels

The NI 9266 has the following channels.

| Channel | Description |
| --- | --- |
| AOx | Analog output channel x, where x is the number of the channel. For the NI 9266, x is 0 to 7. |

#### Module-Specific Errors

The NI 9266 can return the following
 module-specific errors.

| Error Code | Description |
| --- | --- |
| 65542 | One or more channels have detected an open current loop. Check the module connections. |
| 65543 | The power supply voltage level is out of range. Check the supply voltage and the module connections. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. Right-click the module in the Project Explorer window
 and select Properties to display this dialog box. You can
 configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9266

<!--NI_TOPIC bundle=ni-compactrio path=ni-9266.html language=enus -->
## TOPIC 00288: NI 9266

- bundle_id: `ni-compactrio`
- source_path: `ni-9266.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9266.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8 AO, 0-20 mA, 16-Bit Simultaneous Analog Current Output Module NI 9266 Pinout 77 NI 9266 Pinout

### NI 9266

CompactRIO 8 AO, 0-20 mA, 16-Bit Simultaneous Analog Current Output Module

#### NI 9266 Pinout

Figure 77.

[IMAGE alt='image' src='GUID-236E65DF-4FF4-4792-89B7-291F2DEEC96C-a5.svg']

Parent topic:

Analog Output Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9269-fpga-interface.html language=enus -->
## TOPIC 00289: NI 9269 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9269-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9269-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for writing with this device. You can simultaneously write to multiple channels on the NI 9269. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 326 Terminals in Software Terminal Description AOx Analog outp

### NI 9269 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for writing
 with this device.

Note

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| AOx | Analog output channel x, where x is the number of the channel. The NI 9269 has AO channels 0 to 3. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### I/O
 Methods

This device does not support any I/O methods.

#### Module Methods

Use the FPGA I/O Method Node to access the following
 module methods for this device.

Refer to the NI 9269 Getting Started
 VI in the labview\examples\CompactRIO\Module Specific\NI
 9269\NI 9269 Getting Started\NI 9269 Getting Started.lvproj for an
 example of using the Check Output Status methods.

Update

Wait for Update

Write
 Data

- The Write Data method stores data values before writing
 the data to a channel,
- The Update method writes the stored data values to the
 output channel.
- The Wait for Update method waits until the
 Update method updates the output channels.

Refer to the NI 9264 Advanced Write Methods VI in the
 labview\examples\CompactRIO\Module Specific\NI 9264\NI 9264 Advanced
 Write Methods\NI 9264 Advanced Write Methods.lvproj for an example of
 using the Update, Wait for Update, and
 Write Data methods.

| Method | Description |
| --- | --- |
| Check Cached Output Status | Returns Booleans that indicate whether the module or channels reported a power supply fault or an open current loop since the last execution of the Check Cached Output Status method. When the FPGA I/O Node communicates with the module, the FPGA VI samples the states of the module and channels and caches any TRUE value until the Check Cached Output Status method executes. Force Status Read—When the value of this input is FALSE, the method returns the cached status information since the last time that the Check Cached Output Status method executed. When the value is TRUE, the method forces the FPGA I/O Node to communicate with the module and update the status information. Forcing a status read can introduce jitter into an analog output loop. Any Fault—Returns a Boolean value. A value of TRUE indicates that the module has a power supply fault or at least one channel has an open current loop. Power Supply Fault—Returns a Boolean value. A value of TRUE indicates that the external power supply is out of the expected range. Open Current Loop—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index has an open current loop and is configured to output a nonzero current value. |
| Check Output Status | Returns Booleans that indicate whether the module or channels reported a power supply fault or an open current loop during the last time the FPGA I/O Node communicated with the module. When the FPGA I/O Node communicates with the module, the FPGA VI samples the states of the module and channels and overwrites the previous output status with the latest state of the module and channels. Force Status Read—When the value of this input is FALSE, the method returns the status information from the last time the FPGA I/O Node communicated with the module. When the value is TRUE, the method forces the FPGA I/O Node to communicate with the module and update the status information. Forcing a status read can introduce jitter into an analog output loop. Any Fault—Returns a Boolean value. A value of TRUE indicates that the module has a power supply fault or at least one channel has an open current loop. Power Supply Fault—Returns a Boolean value. A value of TRUE indicates that the external power supply is out of the expected range. Open Current Loop—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index has an open current loop and is configured to output a nonzero current value. |
| Update | Writes stored data values to the output channel. Overrun—Returns a Boolean value. A value of TRUE indicates an overrun warning. The overrun warning means that the Update method is trying to run while the Write Data method is running, typically in a different loop. Either the Write Data method is writing data to the module too quickly or the Update method is running too slowly. Underflow—Returns a Boolean value. A value of TRUE indicates an underflow warning. The underflow warning means that the Write Data method has not written new data to the module since the last time the Update method ran. Either the Write Data method is writing data to the module too slowly or the Update method is running too quickly. |
| Wait for Update | Waits until the Update method updates the output channels. Timeout (Ticks)—Specifies in FPGA clock ticks how long the Wait for Update method waits for the Update method to update the output channels. A value of 0 causes the Wait for Update method to time out immediately. A negative value causes the Wait for Update method to wait indefinitely. A positive value causes the Wait for Update method to wait for that number of clock ticks before timing out. Timeout Occurred?—Returns a Boolean value. A value of TRUE indicates that a timeout occurred. |
| Write Data | Stores data values before writing the data to a channel. Channel—Specifies the channel to which you want to write data. Data—Specifies the data you want to write to the channel. |

#### I/O
 Properties

Use the FPGA I/O Property Node to access the following I/O
 properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight | Returns the LSB weight in nV/LSB for the channel. Use this value to convert module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |
| Offset | Returns the calibration offset in nV for the channel. Use this value to convert module data if you set the Calibration Mode to Raw in the C Series Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9269

Related concepts:

- Converting Voltage Values to Binary Values for the NI 9262/9263/9264/9269 (FPGA Interface)
- Writing to C Series Channels
- Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9269-scan-interface.html language=enus -->
## TOPIC 00290: NI 9269 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9269-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9269-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables write floating-point values to the channels in volts. Module ChannelsThe NI 9269 has the following channels. 330 Module Channels Ch

### NI 9269 (Scan Interface)

#### Module I/O Variables

To
 use I/O from this module in a VI, drag and drop I/O variables from the
 Project Explorer window to the block diagram of the VI.
 The I/O variables write floating-point values to the channels in volts.

#### Module Channels

The NI 9269 has the following channels.

| Channel | Description |
| --- | --- |
| AOx | Analog output channel x, where x is the number of the channel. For the NI 9269, x is 0 to 3. |

#### Module-Specific Errors

The NI 9269 can return the following
 module-specific errors.

| Error Code | Description |
| --- | --- |
| 65548 | One or more channels are in overcurrent or overvoltage protection mode. Check the terminals for any fault condition that could be causing an out-of-range voltage or current on the channels. |
| 65579 | The module is in overcurrent protection mode. Check the terminals for any fault condition that could be causing an out-of-range current. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 module. Right-click the module in the Project Explorer window
 and select Properties to display this dialog box. You can
 configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9269

<!--NI_TOPIC bundle=ni-compactrio path=ni-9269.html language=enus -->
## TOPIC 00291: NI 9269

- bundle_id: `ni-compactrio`
- source_path: `ni-9269.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9269.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, ±10 V, 16-Bit Simultaneous Isolated Analog Output Module NI 9269 Pinout 78 NI 9269 Pinout NI-9269 Pinouts

### NI 9269

CompactRIO 4-Channel, ±10 V, 16-Bit Simultaneous Isolated Analog Output Module

#### NI 9269 Pinout

Figure 78.

[IMAGE alt='NI-9269 Pinouts' src='GUID-1657312E-CBF5-48A4-BC8F-23C49DD37608-a5.svg']

Parent topic:

Analog Output Modules

Related concepts:

- Understanding Power-On and Startup Output States for CompactRIO Output Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9320-fpga-interface.html language=enus -->
## TOPIC 00292: NI 9320 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9320-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9320-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node configured for reading with this device. You can simultaneously read from multiple channels on the NI 9320. Refer to Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface). User-Controlled I/O Sampling You can use the following User-

### NI 9320 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for reading with
 this device.

Note

Simultaneously Reading From or Writing to Multiple CompactRIO Channels
 (FPGA Interface)

#### User-Controlled I/O Sampling

You can use the following
 User-Controlled I/O Sampling functions to perform I/O with
 more specific control over the I/O hardware on the FPGA.

| Function | Type |
| --- | --- |
| Generate I/O Sample Pulse Method | Module function |
| Get I/O Read Status Method | I/O function |
| Read I/O Method | I/O function |
| Reset I/O Method | Module function |

Note

Reset I/O

#### Terminals in Software

Use the FPGA I/O Node or User-Controlled
 I/O Sampling functions to access the following terminals for this
 device.

| Terminal | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. The NI 9320 has AI channels 0 to 15. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### I/O
 Methods

This device does not support any I/O methods.

#### Module Methods

Use the FPGA I/O Method Node
 to access the following module methods for this device.

| Method | Description |
| --- | --- |
| Read Module Temperature | Reads the module temperature, represented as -40 °C to 125 °C. |

#### I/O
 Properties

This device does not support any I/O properties.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9320

Related concepts:

- Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9320.html language=enus -->
## TOPIC 00293: NI 9320

- bundle_id: `ni-compactrio`
- source_path: `ni-9320.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9320.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 16-Channel, ±10 V, 16-Bit Simultaneous Analog Input Module NI 9320 Pinout 70 NI 9320 Pinout

### NI 9320

CompactRIO 16-Channel, ±10 V, 16-Bit Simultaneous Analog Input Module

#### NI 9320 Pinout

Figure 70.

[IMAGE alt='image' src='GUID-E67981BD-7425-4357-A648-2DA6686EC3ED-a5.png']

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9326-fpga-interface.html language=enus -->
## TOPIC 00294: NI 9326 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9326-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9326-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 339 Terminals in Software Terminal Description CTRx Counter input channel x, where x is the number of the channel. The counter I/O

### NI 9326 (FPGA Interface)

#### FPGA I/O Node

Use an FPGA I/O Node
 configured for reading with this device.

#### Terminals in Software

Use the FPGA I/O
 Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| CTRx | Counter input channel x, where x is the number of the channel. The counter I/O node returns a cluster of three items, consisting of two unsigned 32-bit integers called A and B as well as the counter status enum. The Start input I/O node must be executed before counter or DI data can be read. The NI 9326 has counters 0 through 5. |
| DIx | Digital input channel x, where x is the number of the channel. The NI 9326 has DI channels 0 through 5. Supported in Digital Input Mode. |
| Start | Channel that controls when the counters begin monitoring their input terminals. If TRUE is written to the Start channel, the NI 9326 counters are reset, armed, and begin monitoring their input terminals to perform the currently configured measurement (such as Edge Counting). Once the NI 9326 counters are armed, execute the CTRx and DIx I/O nodes to read the counter data. You may not execute any NI 9326 I/O Method or Property nodes while the counters are armed.To disarm the counters, use the Stop channel. If FALSE is written to the Start channel, no operation is performed. The Start channel is also used to synchronize multiple NI 9326 modules. |
| Stop | Channel that controls when the counters are disarmed. If TRUE is written to the Stop channel, the counters are stopped. When the counters are stopped, you may change the counter configuration by executing I/O Method and Property nodes. If FALSE is written to the Stop channel, no operation is performed. |

The definition of A and B
 values vary according to the selected measurement mode . The following table defines
 the A and B values for each
 measurement mode option.

| Measurement Mode | A | B | Status |
| --- | --- | --- | --- |
| Edge Counting | Number of edges. | Unused. Always returns 0. | Not applicable. |
| Period | Amount of time elapsed during B signal periods, measured in units of counter timebase ticks. | Scaling factor for A value. Divide A by B to calculate the measured period. | Applicable. |

Period measurements are returned based on ticks of the module's 100 MHz
 timebase. Each tick corresponds to 10 ns. The actual measured period is calculated
 using the following equation:

Measured Period = (Number of Ticks *
 Timebase)/Scaling Factor = (A * 10
 ns)/B

- A = 3,200,000
- B = 32

Measured Period = (3,200,000 * 10 ns)/32 = 1 ms

Counter statuses are applicable for selected measurement modes. The
 following table describes the different statuses.

| Status | Description |
| --- | --- |
| No Sample | The first measurement data is not ready yet for this CTRx channel. This occurs as a result of the following factors: the amount of time elapsed since the counter was armed via the Start channel, the current counter settings, and the input signal behavior. In this case, the A and B values will each return a default value of 0. |
| New | A new, valid measurement for this CTRx channel. |
| Repeated | The same measurement returned the last time a read was performed on this CTRx channel. This measurement is valid, and occurs when the CTRx I/O Node reads are performed faster than the counter can produce new measurements. |
| Timeout | A timeout has occurred. |
| New and Missed | A new, valid measurement for this CTRx channel. The counter also produced one or more new measurements that were never read. This occurs when the counter produces measurements faster than the CTRx I/O Node reads are performed. |
| Timeout and Missed | A timeout has occurred. In addition, the counter produced one or more new measurements that were never read. |

Timeout is applicable for period measurement mode only. The
 definition of Timeout varies according to the setting of the Butterworth filter. The
 following table defines Timeout for each option.

| Measurement Mode | Timeout Definition |
| --- | --- |
| Period (Butterworth filter enabled) | Timeout occurs when the actual input signal period is greater than the internal counter limit at 232 x 10 ns and the counter returns a value of 0. |
| Period (Butterworth filter disabled) | Timeout occurs when the actual input signal period is greater than the maximum measurable period and the counter returns a value of 0. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### I/O Methods

Use the FPGA I/O Method Node
 to access the following I/O methods for this device. You can also use the properties
 dialog box to configure the measurement modes for this device.

Configure Edge Counting

| Parameters | Description |
| --- | --- |
| Terminal | Source input terminal of the counter. |
| Initial Count | Initial counter value once the counter is armed. |
| Direction | Sets the count direction to either count up, count down or to be externally controlled. |
| Direction Terminal | Configures the terminal that is used to control the count direction. This needs to be set when Direction is configured to "Externally Controlled". If not set, the parameter value defaults to DI0 terminal. |
| Reset Enable | Enables or disables Hardware Reset. |
| Reset Terminal | Configures the terminal that is used to reset the counter. This needs to be set when Hardware Reset is enabled. If not set, the parameter value defaults to DI0 terminal. |
| Reset Count | Sets the count value to load to the counter upon reset. If not set, the parameter value defaults to zero. |
| Pause Enable | Enables or disables the pause trigger. |
| Pause Terminal | Configures the terminal that is used to pause the counter. This needs to be set when pause trigger is enabled. If not set, the parameter value defaults to DI0 terminal. |

Configure Edge Counting Simple

| Parameters | Description |
| --- | --- |
| Terminal | Source input terminal of the counter. |
| Initial Count | Initial counter value once the counter is armed. |

Configure Period

| Parameters | Description |
| --- | --- |
| Terminal | Source input terminal of the counter. |
| Enable Butterworth Filter | Enables or disables Butterworth filter. If Butterworth Filter is enabled, set the Filter Frequency parameter accordingly to filter out the higher frequency noise. If disabled, configure the counter settings based on Divisor, Measurement Time and Maximum Measurable Period before the start of an acquisition. |
| Filter Frequency | Configures the Butterworth filter's cut-off frequency to filter out variations in the period measurements. |
| Measurement Time | Configures the amount of time over which to measure and average to determine the input signal period. This value is specified in units of counter timebase ticks. Set to 0 to disable the Measurement Time, in which case the measurement will be completed using only the Divisor setting. |
| Divisor | Configures the number of periods of the input signal to measure and average to determine the input signal period. Set to 0 to disable the Divisor, in which case the measurement will be completed using only the Measurement Time setting. |
| Maximum Measurable Period | Configures the maximum (slowest) period of the input signal that can be measured. If the actual input signal period is longer than this value, the measurement will timeout and the counter returns a value of 0. This value is specified in units of counter timebase ticks. Set this value to 0 to disable enforcing the maximum period. |

Note

Measurement Time

Divisor

Configure Period Simple

| Parameters | Description |
| --- | --- |
| Terminal | Source input terminal of the counter. |
| Filter Frequency | Configures the Butterworth filter's cut-off frequency to filter out variations in the period measurements. |

#### Module Methods

Use the FPGA I/O Method
 Node to access the following module methods for this device.

| Method | Description |
| --- | --- |
| Check Status | Returns a Boolean value that indicates whether the module is ready. Supported in Digital Input Mode. |

#### I/O Properties

Use the FPGA I/O Property
 Node to access the following I/O properties for this device.

| Property | Description |
| --- | --- |
| Digital Filter Enable | Enables the digital glitch filter for the corresponding digital line. |
| Digital Filter Minimum Pulse Width[1]1 Unit in ticks. 1 tick = 80 ns. For example, the Minimum Pulse Width = 1 ms. Therefore, input to the Digital Filter Minimum Pulse Width property node is 1 ms / 80 ns = 12500 ticks. | Configures the minimum pulse width for the digital glitch filter of the corresponding digital line in increments of 80 ns, up to 5.24 ms. |
| Digital Logic Threshold | Configures the digital logic threshold for the channel. |
| Hysteresis Value | Configures the hysteresis value for the channel. |
| Active Edge | Configures the triggering edge of the input signal. |

Note

| Measurement Mode | Active Edge Description |
| --- | --- |
| Edge Counting | Input Terminal: Configures the triggering edge of the input signal. Rising indicates the counter would count on every rising edge and vice versa. Direction Terminal: Configures the terminal that is used to control the count direction. When set to rising edge, the counter counts up when signal on the direction terminal is high. This applies only when the Direction parameter is set to Externally Controlled. If the Direction Terminal is not set and the Direction parameter is set to Externally Controlled, the default setting is to count up when signal is high. Reset Terminal: Configures the triggering edge of the reset signal. This applies only when the Reset Enable parameter is set to true. If the Reset Terminal is not set and the Reset Enable parameter is set to true, the default setting is to reset on the rising edge of the signal. Pause Terminal: Configures the terminal that is used to pause the counter. When set to rising edge, the counter pauses when the signal on the pause terminal is high. This applies only when the Pause Enable parameter is set to true. If the Pause Terminal is not set and the Pause Enable parameter is set to true, the default setting is to pause when signal is high. |
| Period (Butterworth filter enabled) | Input Terminal: Configures the triggering edge of the input signal. |
| Period (Butterworth filter disabled) | Input Terminal: Configures the triggering edge of the input signal. |

#### Module Properties

Use the FPGA I/O
 Property Node to access the following module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID, 0x7A5E. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device supports the single-cycle Timed Loop
 when Digital InputMode is set in the properties dialog box. The
 input channels of this device are synchronized with two synchronizing registers.

When the module is within a single-cycle Timed Loop, it must be ready to
 perform digital input before a loop containing digital input starts. Poll the
 Ready output of the Check Status
 method to determine whether the module is ready. Digital input operations return
 null data if the module is not ready.

#### FPGA Target Clock Support

- 40 MHz
- 80 MHz
- 120 MHz
- 160 MHz.

Parent topic:

NI 9326

Related concepts:

- Reading from C Series Channels

[<sup>1</sup>](#note_ref-d39309e914) Unit in ticks. 1 tick = 80
 ns. For example, the Minimum Pulse Width = 1 ms. Therefore,
 input to the Digital Filter Minimum Pulse Width property node is
 1 ms / 80 ns = 12500 ticks.

<!--NI_TOPIC bundle=ni-compactrio path=ni-9350-scan-interface.html language=enus -->
## TOPIC 00295: NI 9350 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9350-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9350-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O VariablesTo use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. Digital input reads the Boolean state of that channel. Digital output reads the Boolean state of that channel. When the User Program sets the channel

### NI 9350 (Scan Interface)

#### Module I/O Variables

To use I/O from this
 module in a VI, drag and drop I/O variables from the Project Explorer
 window to the block diagram of the VI.

Digital input

Digital output

State machine variable

User LED0

#### Module Channels

The NI 9350 has the following
 channels.

| Channel | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. For the NI 9350, x is 0 to 7. |
| DOx | Digital output channel x, where x is the number of the channel. For the NI 9350, x is 0 to 7. |
| Varx | State machine variable x, where x is the number of the variable. For the NI 9350, x is 0 to 23. |
| User LED0 | User-configurable LED |

#### C Series Module Properties Dialog Box

Use
 this dialog box to configure the NI 9350. Right-click the NI 9350 in the Project
 Explorer window and select Properties to display this
 dialog box. You can configure the following options.

- Name —Indicates the name of the C Series module, which appears in
 the Project Explorer window. LabVIEW assigns a default name to the
 module based on the slot number. You can use this field to give the module a descriptive
 name.
- Module Type —Indicates the type of C Series module. You cannot
 change this value.
- Location —Indicates a slot in the chassis for the C Series
 module.
- Read Module Information —Reads the Build Number and Program GUID
 of the current User Program installed on the C Series module.
- Build Number —Indicates the build number of the current User
 Program installed on the C Series module.
- Program GUID —Indicates the program GUID of the current User
 Program installed on the C Series module.
- Mode —Indicates the current operating mode of the C Series module.
  - Power Up —Indicates module is powering up.
  - Unprogrammed —Indicates User Program is not written to the C
 Series module.
  - User Program Download —Indicates the User Program is
 downloading to the C Series module.
  - Module Firmware Download —Indicates firmware is downloading to
 the C Series module.
  - Verification —Indicates User Program has successfully
 downloaded. Requires user verification.
  - Operational —Indicates C Series module is running the User
 Program.
  - Reserved —Indicates C Series module is in Reserved mode.
  - Fail-safe —Indicates User Program has detected a fault that
 triggered Fail-safe mode. User must address fault and cycle power to return the C
 Series module to Operational mode.
- Change Mode to X —Updates C Series module from Verification mode
 to Operational mode or from Operational mode to Verification mode.
- Path to New User Program —Specifies the file path of the User
 Program selected for download.
- Build Number —Indicates the build number of the User Program
 selected for download.
- Program GUID in New Program —Indicates the program GUID of the
 User Program selected for download.
- Download —Downloads the selected User Program to the C Series
 module.

#### Module Methods

Use the Invoke Node to access
 the following module properties for this device.

| Method | Description |
| --- | --- |
| Check Channel Status | Returns Boolean arrays that indicate the channel status, including various faults. The index number in the array corresponds to the channel number on the module, so that index 0 indicates the channel status for DI0 or DO0. The following parameters are available: DO Internal Readback—Indicates whether the DO signal is high or low. DO Channel Overcurrent Fault—Indicates an overcurrent fault has been detected. DO Channel Open Circuit Fault—Indicates an open circuit fault has been detected. DI Channel Discrepancy Fault—Indicates a discrepancy fault has been detected. Channel Test Pulse Fault—Indicates a test pulse fault has been detected. Channel Readback Fault—Indicates a readback fault has been detected. |
| Check Module Status | Returns the module status, including digital output values and various faults. The following parameters are available: Mode—Returns an enum value that reads the operating mode of the NI 9350. Power Up—Indicates module is powering up. Unprogrammed—Indicates User Program is not written to the C Series module. User Program Download—Indicates the User Program is downloading to the C Series module. Module Firmware Download—Indicates firmware is downloading to the C Series module. Verification—Indicates User Program has successfully downloaded. Requires user verification. Operational—Indicates C Series module is running the User Program. Reserved—Indicates C Series module is in Reserved mode. Fail-safe—Indicates the User Program has detected a fault that triggered Fail-safe mode. Address the fault and cycle power to return the module to Operational mode. User Program Running—Returns Boolean value to indicate the status of the User Program. Internal Fault—Returns Boolean value to indicate whether an internal fault has been detected. Temperature Fault—Returns Boolean value to indicate whether a temperature fault has been detected. Power Supply Fault—Returns Boolean value to indicate whether a power supply fault has been detected. |
| Start Program | Starts the User Program. |
| Set Mode | Sets the operating mode for the NI 9350 as an enum value. Valid values are Operational or Verification. |
| Read Current State | Returns an array of U8 values. The array index corresponds to the state machine number in the User Program and the U8 value indicates the current state of that state machine. Refer to the report.log file generated by the Functional Safety Editor to index the state machines and identify the state number. |

#### Module Properties

Use the Property Node to
 access the following module properties for this device.

| Property | Description |
| --- | --- |
| Firmware Version Number | Returns U32 value to indicate the version of the module firmware. |
| User Program GUID | Returns a string to indicate the GUID assigned to the User Program. |
| User Program Version Number | Returns U32 value to indicate the build number of the User Program. |

Parent topic:

NI 9350

<!--NI_TOPIC bundle=ni-compactrio path=ni-9350.html language=enus -->
## TOPIC 00296: NI 9350

- bundle_id: `ni-compactrio`
- source_path: `ni-9350.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9350.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 8-Channel 24 V Sinking DI, 8-Channel 24 V Sourcing DO SIL 3 Capable C Series Functional Safety Module NI 9350 Pinout 113 NI 9350 Pinout

### NI 9350

8-Channel 24 V Sinking DI, 8-Channel 24 V Sourcing DO SIL 3 Capable C Series Functional Safety Module

#### NI 9350 Pinout

Figure 113.

[IMAGE alt='image' src='GUID-5751C477-CCBB-43E4-8117-5CC21840C62B-a5.svg']

Parent topic:

Functional Safety Modules

Related information:

- C Series Functional Safety Manual

<!--NI_TOPIC bundle=ni-compactrio path=ni-9351-scan-interface.html language=enus -->
## TOPIC 00297: NI 9351 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9351-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9351-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O VariablesTo use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. Analog input Reads the analog signal of that channel. Digital input Reads the Boolean state of that channel. Digital output Reads the Boolean state of

### NI 9351 (Scan Interface)

#### Module
 I/O Variables

To use I/O from this module in a VI, drag and drop I/O variables
 from the Project Explorer window to the block diagram of the VI.

Analog input

Digital input

Digital output

State machine variable

User LED0

#### Module
 Channels

The NI 9351 has the following channels.

| Channel | Description |
| --- | --- |
| AIx | Analog input channel x, where x is the number of the channel. For the NI 9351, x is 0 to 3. |
| DIx | Digital input channel x, where x is the number of the channel. For the NI 9351, x is 0 to 3. |
| DOx | Digital output channel x, where x is the number of the channel. For the NI 9351, x is 0 to 3. |
| Varx | State machine variable x, where x is the number of the variable. For the NI 9351, x is 0 to 23. |
| User LED0 | User-configurable LED |

#### C Series
 Module Properties Dialog Box

Use this dialog box to configure the NI 9351.
 Right-click the NI 9351 in the Project Explorer window and select
 Properties to display this dialog box. You can configure the
 following options.

- Name —Indicates the name of the C Series module, which appears in the
 Project Explorer window. LabVIEW assigns a default name to the
 module based on the slot number. You can use this field to give the module a descriptive
 name.
- Module Type —Indicates the type of C Series module. You cannot change
 this value.
- Location —Indicates a slot in the chassis for the C Series module.
- Read Module Information —Reads the Build Number and Program GUID of the
 current User Program installed on the C Series module.
- Build Number —Indicates the build number of the current User Program
 installed on the C Series module.
- Program GUID —Indicates the program GUID of the current User Program
 installed on the C Series module.
- Mode —Indicates the current operating mode of the C Series module.
  - Power Up —Indicates module is powering up.
  - Unprogrammed —Indicates User Program is not written to the C
 Series module.
  - User Program Download —Indicates the User Program is
 downloading to the C Series module.
  - Module Firmware Download —Indicates firmware is downloading to
 the C Series module.
  - Verification —Indicates User Program has successfully
 downloaded. Requires user verification.
  - Operational —Indicates C Series module is running the User
 Program.
  - Reserved —Indicates C Series module is in Reserved mode.
  - Fail-safe —Indicates User Program has detected a fault that
 triggered Fail-safe mode. User must address fault and cycle power to return the C
 Series module to Operational mode.
- Change Mode to X —Updates C Series module from Verification mode to
 Operational mode or from Operational mode to Verification mode.
- Path to New User Program —Specifies the file path of the User Program
 selected for download.
- Build Number —Indicates the build number of the User Program selected
 for download.
- Program GUID in New Program —Indicates the program GUID of the User
 Program selected for download.
- Download —Downloads the selected User Program to the C Series
 module.

#### Module
 Methods

Use the Invoke Node to access the following module properties for this
 device.

| Method | Description |
| --- | --- |
| Check Channel Status | Returns Boolean arrays that indicate the channel status, including various faults. The index number in the array corresponds to the channel number on the module, so that index 0 indicates the channel status for DI0 or DO0. The following parameters are available: DO Internal Readback—Indicates whether the DO signal is high or low. DO Channel Overcurrent Fault—Indicates an overcurrent fault has been detected. DO Channel Open Circuit Fault—Indicates an open circuit fault has been detected. DI Channel Discrepancy Fault—Indicates a discrepancy fault has been detected. Channel Test Pulse Fault—Indicates a test pulse fault has been detected. Channel Readback Fault—Indicates a readback fault has been detected. AI Discrepancy Fault—Indicates a discrepancy fault has been detected. AI Overcurrent Fault—Indicates a overcurrent fault has been detected. AI Discrepancy Warning—Indicates which AI channel in a 2oo3 configuration is out of discrepancy range. |
| Check Module Status | Returns the module status, including digital output values and various faults. The following parameters are available: Mode—Returns an enum value that reads the operating mode of the NI 9351. Power Up—Indicates module is powering up. Unprogrammed—Indicates User Program is not written to the C Series module. User Program Download—Indicates the User Program is downloading to the C Series module. Module Firmware Download—Indicates firmware is downloading to the C Series module. Verification—Indicates User Program has successfully downloaded. Requires user verification. Operational—Indicates C Series module is running the User Program. Reserved—Indicates C Series module is in Reserved mode. Fail-safe—Indicates the User Program has detected a fault that triggered Fail-safe mode. Address the fault and cycle power to return the module to Operational mode. User Program Running—Returns Boolean value to indicate the status of the User Program. Internal Fault—Returns Boolean value to indicate whether an internal fault has been detected. Temperature Fault—Returns Boolean value to indicate whether a temperature fault has been detected. Power Supply Fault—Returns Boolean value to indicate whether a power supply fault has been detected. |
| Start Program | Starts the User Program. |
| Set Mode | Sets the operating mode for the NI 9351 as an enum value. Valid values are Operational or Verification. |
| Read Current State | Returns an array of U8 values. The array index corresponds to the state machine number in the User Program and the U8 value indicates the current state of that state machine. Refer to the report.log file generated by the Functional Safety Editor to index the state machines and identify the state number. |

#### Module
 Properties

Use the Property Node to access the following module properties for
 this device.

| Property | Description |
| --- | --- |
| Firmware Version Number | Returns U32 value to indicate the version of the module firmware. |
| User Program GUID | Returns a string to indicate the GUID assigned to the User Program. |
| User Program Version Number | Returns U32 value to indicate the build number of the User Program. |

Parent topic:

NI 9351

<!--NI_TOPIC bundle=ni-compactrio path=ni-9351.html language=enus -->
## TOPIC 00298: NI 9351

- bundle_id: `ni-compactrio`
- source_path: `ni-9351.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9351.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 4-Channel 0-20 mA 16-bit AI, 4-Channel 24 V Sinking DI, 4-Channel 24 V Sourcing DO SIL 3 Capable C Series Functional Safety Module NI 9351 Pinout 114 NI 9351 Pinout

### NI 9351

4-Channel 0-20 mA 16-bit AI, 4-Channel 24 V Sinking DI, 4-Channel 24 V Sourcing DO SIL 3 Capable C Series Functional Safety Module

#### NI 9351 Pinout

Figure 114.

[IMAGE alt='image' src='GUID-8A71F9AF-E8AA-4988-B948-A115DA5959F5-a5.svg']

Parent topic:

Functional Safety Modules

Related information:

- C Series Functional Safety Manual

<!--NI_TOPIC bundle=ni-compactrio path=ni-9361-fpga-interface.html language=enus -->
## TOPIC 00299: NI 9361 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9361-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9361-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 355 Terminals in Software Terminal Description CTRx Counter input channel x, where x is the number of the channel. The counter I/O

### NI 9361 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for reading
 with this device.

#### Terminals in Software

Use the FPGA I/O
 Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| CTRx | Counter input channel x, where x is the number of the channel. The counter I/O node returns a cluster of three items, consisting of two unsigned 32-bit integers called A and B as well as the counter status enum. The Start input I/O node must be executed before counter or DI data can be read. The NI 9361 has counters 0 through 7. |
| DIx | Digital input channel x, where x is the number of the channel. The NI 9361 has DI channels 0 through 7. |
| DI7:0 | Digital Port consisting of channels 0 through 7. Channel 7 is returned in the Most Significant Bit (MSB), and channel 0 is returned in the Least Significant Bit (LSB). |
| Start | Channel that controls when the counters begin monitoring their input terminals. If TRUE is written to the Start channel, the NI 9361 counters are reset, armed, and begin monitoring their input terminals to perform the currently configured measurement (such as Edge Counting). Once the NI 9361 counters are armed, you may execute the CTRx and DIx I/O nodes to read the counter data. You may not execute any NI 9361 I/O Method or Property nodes while the counters are armed. To disarm the counters, use the Stop channel. If FALSE is written to the Start channel, no operation is performed. The Start channel is also used to synchronize multiple NI 9361 modules. |
| Stop | Channel that controls when the counters are disarmed. If TRUE is written to the Stop channel, the counters are stopped. When the counters are stopped, you may change the counter configuration by executing I/O Method and Property nodes. If FALSE is written to the Stop channel, no operation is performed. |

The definition of A and B
 values vary according to the measurement mode you select. The following table
 defines the A and B values for each
 measurement mode option.

| Measurement Mode | A | B | Status |
| --- | --- | --- | --- |
| Edge Counting | Number of edges. | Unused. Always returns 0. | Not applicable. |
| Period | Amount of time elapsed during B signal periods, measured in units of counter timebase ticks. | Number of signal periods measured. | Applicable. |
| Pulse | Width of High portion of input signal period, measured in units of counter timebase ticks. | Width of Low portion of input signal period, measured in units of counter timebase ticks. | Applicable. |
| Pulse Width | Width of input pulse, measured in units of counter timebase ticks. | Unused. Always returns 0. | Applicable. |
| Two Edge Separation | Amount of time between two input edges, measured in units of counter timebase ticks. | Unused. Always returns 0. | Applicable. |
| Encoder Position | Number of encoder counts. | Unused. Always returns 0. | Not applicable. |
| Encoder Velocity | Amount of time elapsed during B encoder counts, measured in units of counter timebase ticks. | Signed number of counter encoder counts and direction. Positive values indicate counting in the positive direction, and negative values indicate counting in the opposite direction. You must use the To Long Integer function to convert the unsigned B value (U32) to a signed value (I32) when performing an Encoder Velocity measurement. | Applicable. |

All values that are based on ticks use the module's timebase of 100 MHz. Each
 tick corresponds to 10 ns. The actual value is calculated as:

Actual
 = Number of ticks * 10 ns

Examples:

Period Measurement Mode

Measured period = (A * 10 ns)/B = 1 ms

Encoder Velocity Measurement Mode

Measured Encoder Velocity = B/(A * 10 ns) = 1000
 count/s

Pulse Width and Two Edge Separation Measurement Mode

Measured Pulse Width or Two Edge Separation = A * 10 ns = 1
 ms

Pulse Measurement Mode

Measured High Pulse = A * 10 ns = 1 ms. Measured Low Pulse = B * 10
 ns = 1 ms

Counter statuses are applicable for selected measurement modes. The following
 table describes the different statuses.

| Status | Description |
| --- | --- |
| No Sample | The first measurement data is not ready yet for this CTRx channel. This occurs as a result of the following factors: the amount of time elapsed since the counter was armed via the Start channel, the current counter settings, and the input signal behavior. In this case, the A and B values will each return a default value of 0. |
| New | A new, valid measurement for this CTRx channel. |
| Repeated | The same measurement returned the last time a read was performed on this CTRx channel. This measurement is valid, and occurs when the CTRx I/O Node reads are performed faster than the counter can produce new measurements. |
| Timeout | A timeout has occurred. |
| New and Missed | A new, valid measurement for this CTRx channel. The counter also produced one or more new measurements that were never read. This occurs when the counter produces measurements faster than the CTRx I/O Node reads are performed. |
| Timeout and Missed | A timeout has occurred. In addition, the counter produced one or more new measurements that were never read. |

Timeout is applicable for selected measurement modes, and the definition of
 Timeout varies according to the measurement mode you select. The following table
 defines Timeout for each measurement mode option.

| Measurement Mode | Timeout Definition |
| --- | --- |
| Period | Timeout occurs when the actual input signal period is greater than the maximum measurable period and the counter returns a value of 0. |
| Pulse | Timeout occurs when the actual input signal period is greater than the maximum measurable period. If the input signal remains high when timeout occurs, the counter returns a non-zero value for the high pulse and a value of 0 for the low pulse. If the input signal remains low when timeout occurs, the counter returns a non-zero value for the low pulse and a value of 0 for the high pulse. |
| Pulse Width | Timeout occurs when the actual input signal period is greater than the maximum measurable period and the counter returns a value of 0. |
| Two Edge Separation | Timeout occurs when the actual input signal period is greater than the maximum measurable separation and the counter returns a value of 0. |
| Quadrature Encoder Velocity | Timeout occurs when the actual input signal period is greater than the maximum measurable count period and the counter returns a value of 0. |
| Two Pulse Encoder Velocity | Timeout occurs when the actual input signal period is greater than the maximum measurable count period and the counter returns a value of 0. |

#### Arbitration

This device supports only the Arbitrate if
 Multiple Requestors Only option for arbitration. You cannot
 configure arbitration settings for this device.

#### I/O Methods

Use the FPGA I/O Method Node
 to access the following I/O methods for this device. You can also use the properties
 dialog box to configure the measurement modes for this device.

#### Module Methods

This device does not
 support any module methods.

#### I/O
 Properties

Use the FPGA I/O Property Node to access the following I/O
 properties for this device.

| Property | Description |
| --- | --- |
| Digital Filter Enable | Enables the digital filter for the corresponding digital line. |
| Digital Filter Minimum Pulse Width[1]1 Unit in ticks. 1 tick = 80 ns. For example, Minimum Pulse Width = 1 ms. Therefore, input to the Digital Filter Minimum Pulse Width property node is 1 ms / 80 ns = 12500 ticks. | Configures the minimum pulse width for the digital filter of the corresponding digital line in increments of 80 ns, up to 5.24 ms. |
| Terminal Mode | Configures the terminal mode of the corresponding digital line (Differential, Single-ended, and Single-ended with Pull-up). |

#### Module Properties

Use the FPGA I/O
 Property Node to access the following module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID, 0x777E. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |
| Digital Logic Threshold | Configures the digital logic threshold for the module. Does not apply to terminals that are configured as Differential. |

#### Single-Cycle Timed Loop

This device does not support any single-cycled
 timed loop.

#### FPGA
 Target Clock Support

- 40 MHz
- 80 MHz
- 120 MHz
- 160 MHz.

Parent topic:

NI 9361

Related concepts:

- Reading from C Series Channels

[<sup>1</sup>](#note_ref-d11322e674) Unit in ticks. 1 tick = 80
 ns. For example, Minimum Pulse Width = 1 ms. Therefore, input to
 the Digital Filter Minimum Pulse Width property node is 1 ms /
 80 ns = 12500 ticks.

<!--NI_TOPIC bundle=ni-compactrio path=ni-9361-i-o-method-parameters.html language=enus -->
## TOPIC 00300: NI 9361 I/O Method Parameters

- bundle_id: `ni-compactrio`
- source_path: `ni-9361-i-o-method-parameters.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9361-i-o-method-parameters.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the I/O Methods, that includes the following parameters, which you can use to configure the NI 9361 measurement modes. The counters operate based on the module's timebase of 100 MHz. Each timebase tick corresponds to 10 ns. Configure Edge Counting Configures the corresponding counter for a

### NI 9361 I/O Method Parameters

Note

Configure Edge Counting

| Parameters | Description |
| --- | --- |
| Terminal | Source input terminal of the counter. |
| Initial Count | Initial counter value once the counter is armed. |
| Active Edge | Sets the triggering edge of the input signal. Rising indicates the counter would count on every rising edge and vice versa. |
| Direction | Sets the count direction to either count up, count down or to be externally controlled. |
| Direction Terminal | Configures the external terminal that is used to control the count direction. This needs to be set when Direction is configured to "Externally Controlled". If not set, the parameter value defaults to DI0 terminal. |
| External Direction Count Up When | Configures whether the counter would count up when the Direction Terminal is 'HIGH' or to count up when the Direction Terminal is 'LOW'. If not set, the parameter value defaults to count up when high. |
| Reset Enable | Enables or disables Hardware Reset. |
| Reset Terminal | Configures the reset terminal that is used to reset the counter. This needs to be set when Hardware Reset is enabled. If not set, the parameter value defaults to DI0 terminal. |
| Reset Count | Sets the count value to load to the counter upon reset. If not set, the parameter value defaults to zero. |
| Reset Active Edge | Sets the triggering edge of the reset signal. If not set, the parameter value defaults to reset on the rising edge. |
| Pause Enable | Enables or disables the pause trigger. |
| Pause Terminal | Configures the pause terminal that is used to pause the counter. This needs to be set when pause trigger is enabled. If not set, the parameter value defaults to DI0 terminal. |
| Pause When | Configures the pause trigger to either pause the counter when the pause terminal is 'HIGH' or 'LOW'. If not set, the parameter value defaults to pause when high. |

Configure Edge Counting Simple

| Parameters | Description |
| --- | --- |
| Terminal | Source input terminal of the counter. |
| Initial Count | Initial counter value once the counter is armed. |
| Active Edge | Sets the triggering edge of the input signal. Rising indicates the counter would count on every rising edge and vice versa. |

Configure Period

| Parameters | Description |
| --- | --- |
| Terminal | Source input terminal of the counter. |
| Starting Edge | Configures the triggering edge of the input signal. |
| Measurement Time | Configures the amount of time over which to measure and average the period of the input signal. This value is specified in units of counter timebase ticks. Set to 0 to disable the Measurement Time, in which case the measurement will be completed using only the Divisor setting. |
| Divisor | Configures the number of periods of the input signal to measure and average to determine the input signal period. Set to 0 to disable the Divisor, in which case the measurement will be completed using only the Measurement Time setting. |
| Maximum Measurable Period | Configures the maximum (slowest) period input signal that can be measured. If the actual input signal period is longer than this value, the measurement will timeout and the counter returns a value of 0. This value is specified in units of counter timebase ticks. Set this value to 0 to disable enforcing the maximum period. |

Note

Measurement Time

Divisor

Configure Period Simple

Measurement Time

Divisor

| Parameters | Description |
| --- | --- |
| Terminal | Source input terminal of the counter. |
| Starting Edge | Configures the triggering edge of the input signal. |
| Maximum Measurable Period | Configures the maximum (slowest) period input signal that can be measured. If the actual input signal period is longer than this value, the measurement will timeout and the counter returns a value of 0. This value is specified in units of counter timebase ticks. Set this value to 0 to disable enforcing the maximum period. |

Configure Pulse

| Parameters | Description |
| --- | --- |
| Terminal | Source input terminal of the counter. |
| Starting Edge | Configures the triggering edge of the input signal. |
| Maximum Measurable Period | Configures the maximum (slowest) period input signal that can be measured. If the actual input signal period is longer than this value, the measurement will timeout and the counter returns a non-zero value for the high pulse and a value of 0 for the low pulse if the actual signal is high during timeout. The counter returns a non-zero value for the low pulse and a value of 0 for the high pulse if the actual signal is low during timeout. This value is specified in units of counter timebase ticks. Set this value to 0 to disable enforcing the maximum period. |

Configure Pulse Width

| Parameters | Description |
| --- | --- |
| Terminal | Source input terminal of the counter. |
| Starting Edge | Configures the triggering edge of the input signal. |
| Maximum Measurable Period | Configures the maximum (slowest) period input signal that can be measured. If the actual input signal period is longer than this value, the measurement will timeout and the counter returns a value of 0. This value is specified in units of counter timebase ticks. Set this value to 0 to disable enforcing the maximum period. |

Configure Two Edge Separation

| Parameters | Description |
| --- | --- |
| First Terminal | First source input terminal of the counter. |
| First Edge | Configures the triggering edge of the first signal. |
| Second Terminal | Second source input terminal of the counter. |
| Second Edge | Configures the triggering edge of the second signal. |
| Maximum Measurable Separation | Configures the maximum separation between the first input signal and the second input signal that can be measured. If the actual input signal separation is longer than this value, the measurement will timeout and the counter returns a value of 0. This value is specified in units of counter timebase ticks. Set this value to 0 to disable enforcing the maximum separation. |

Configure Quadrature Encoder Position

Z

| Parameters | Description |
| --- | --- |
| A Terminal | A input terminal of the counter. |
| A Invert Polarity | Configures the module to invert the A signal. |
| B Terminal | B input terminal of the counter. |
| B Invert Polarity | Configures the module to invert the B signal. |
| Initial Position | Initial counter value once the counter is armed. |
| Decoding Type | Configures the decoding type to either x1, x2 or x4. |
| Z Index Enable | Enables or disables the Z Index. |
| Z Terminal | Configures the Z terminal for the Z index. This needs to be set when Z Index is enabled. If not set, the parameter value defaults to DI0 terminal. |
| Z Invert Polarity | Configures the module to invert the Z signal. If not set, the parameter value defaults to not inverting the Z signal. |
| Z Index Value | Configures the counter value to be loaded when the Z Index is triggered. If not set, the parameter value defaults to not zero. |
| Z Index Phase | Configures the Z Index phase in which the Z index would be triggered. If not set, the parameter value defaults to trigger when A signal is low and B signal is low. |

Configure Two Pulse Encoder

| Parameters | Description |
| --- | --- |
| A Terminal | A input terminal of the counter. |
| A Invert Polarity | Configures the module to invert the A signal. |
| B Terminal | B input terminal of the counter. |
| B Invert Polarity | Configures the module to invert the B signal. |
| Initial Position | Initial counter value once the counter is armed. |
| Reset Enable | Enables or disables Hardware Reset. |
| Reset Terminal | Configures the reset terminal that is used to reset the counter. This needs to be set when Hardware Reset is enabled. If not set, the parameter value defaults to DI0 terminal |
| Reset Position | Sets the count value that would be loaded to the counter upon reset. If not set, the parameter value defaults to zero. |
| Reset Active Edge | Sets the triggering edge of the reset signal. If not set, the parameter value defaults to reset on rising edge. |

Configure Two Pulse Encoder Simple

| Parameters | Description |
| --- | --- |
| A Terminal | A input terminal of the counter. |
| A Invert Polarity | Configures the module to invert the A signal. |
| B Terminal | B input terminal of the counter. |
| B Invert Polarity | Configures the module to invert the B signal. |
| Initial Position | Initial counter value once the counter is armed. |

Configure Quadrature Encoder Velocity

| Parameters | Description |
| --- | --- |
| A Terminal | A input terminal of the counter. |
| A Invert Polarity | Configures the module to invert the A signal. |
| B Terminal | B input terminal of the counter. |
| B Invert Polarity | Configures the module to invert the B signal. |
| Decoding Type | Configures the decoding type to either x1, x2 or x4. |
| Measurement Time | Configures the amount of time over which to measure and average the period of the input signal. This value is specified in units of counter timebase ticks. Set to 0 to disable the Measurement Time, in which case the measurement will be completed using only the Divisor setting. |
| Divisor | Configures the number of encoder count periods to measure and average to determine the encoder input period (velocity). Set to 0 to disable the Divisor, in which case the measurement will be completed using only the Measurement Time setting. |
| Maximum Measurable Count Period | Configures the maximum (slowest) period between encoder input counts that can be measured. If the actual time between encoder counts is longer than this value, the measurement will timeout and the counter returns a value of 0. This value is specified in units of counter timebase ticks. Set this value to 0 to disable enforcing the maximum period. |

Note

Measurement Time

Divisor

Configure Two Pulse Encoder Velocity

| Parameters | Description |
| --- | --- |
| A Terminal | A input terminal of the counter. |
| A Invert Polarity | Configures the module to invert the A signal. |
| B Terminal | B input terminal of the counter. |
| B Invert Polarity | Configures the module to invert the B signal. |
| Measurement Time | Configures the amount of time over which to measure and average the period of the input signal. This value is specified in units of counter timebase ticks. Set to 0 to disable the Measurement Time, in which case the measurement will be completed using only the Divisor setting. |
| Divisor | Configures the number of encoder count periods to measure and average to determine the encoder input period (velocity). Set to 0 to disable the Divisor, in which case the measurement will be completed using only the Measurement Time setting. |
| Maximum Measurable Count Period | Configures the maximum (slowest) period between encoder input counts that can be measured. If the actual time between encoder counts is longer than this value, the measurement will timeout and the counter returns a value of 0. This value is specified in units of counter timebase ticks. Set this value to 0 to disable enforcing the maximum period. |

Parent topic:

NI 9361 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9421-scan-interface.html language=enus -->
## TOPIC 00301: NI 9421 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9421-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9421-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return data as Boolean values. Module ChannelsThe NI 9421 has the following channels. 406 Module Channels Channel

### NI 9421 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return data as Boolean values.

#### Module Channels

The NI 9421 has the following channels.

| Channel | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. For the NI 9421, x is 0 to 7. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9421. Right-click the NI 9421 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

#### Specialty Digital Configuration

Use the Specialty Digital
 Configuration page of the C Series Module
 Properties dialog box to configure channels of this module for
 counter input or quadrature input.

Parent topic:

NI 9421

Related concepts:

- Configuring Specialty Digital Functions
- Configuring Counters
- Configuring a Module for Quadrature Input

<!--NI_TOPIC bundle=ni-compactrio path=ni-9421.html language=enus -->
## TOPIC 00302: NI 9421

- bundle_id: `ni-compactrio`
- source_path: `ni-9421.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9421.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8-Channel, 24 V, Sinking Digital Input Module NI 9421 Pinout 89 NI 9421 Pinout

### NI 9421

CompactRIO 8-Channel, 24 V, Sinking Digital Input Module

#### NI 9421 Pinout

Figure 89.

[IMAGE alt='image' src='GUID-66A01C3F-559A-42EF-915A-84E67323EE9E-a5.svg']

Parent topic:

Digital Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9422-fpga-interface.html language=enus -->
## TOPIC 00303: NI 9422 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9422-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9422-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 407 Terminals in Software Terminal Description DIx Digital input channel x, where x is the number of the channel. The NI 9422 has

### NI 9422 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for reading
 with this device.

#### Terminals in Software

Use the FPGA I/O
 Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. The NI 9422 has DI channels 0 to 7. |
| DI7:0 | Digital port consisting of channels 0 through 7. Channel 7 is returned in the MSB. Channel 0 is returned in the LSB. |

#### Arbitration

This device supports only the Never
 Arbitrate option for arbitration. You cannot configure arbitration
 settings for this device.

#### I/O Methods

Use the FPGA I/O Method Node
 to access the following I/O methods for this device.

| Method | Description |
| --- | --- |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### Module Methods

| Method | Description |
| --- | --- |
| Check Status | Returns a Boolean value that indicates whether the module is ready. |

Note

Check Status

#### I/O
 properties

This device does not support any I/O properties.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device supports the single-cycle Timed
 Loop. Configure the number of input synchronizing registers for the channels of this
 device in the Advanced Code Generation page of the FPGA I/O Node Properties dialog
 box.

When the module is within a single-cycle Timed Loop, it must be ready to
 perform digital input before a loop containing digital input starts. Poll the
 Ready output of the Check Status method to determine
 whether the module is ready. Digital input operations return invalid data if the
 module is not ready.

While the module is performing digital input within a
 single-cycle Timed Loop, do not perform property reads or remove the module from the
 chassis. Doing either of these actions causes the module to be unable to perform
 digital input and the Ready output of the Check Status method
 to return FALSE.

#### FPGA
 Target Clock Support

This device supports only top-level FPGA target
 clock rates and single-cycle Timed Loop clock rates that are multiples of 40 MHz,
 such as 40 MHz, 80 MHz, 120 MHz, and so on.

Parent topic:

NI 9422

Related concepts:

- Reading from C Series Channels

<!--NI_TOPIC bundle=ni-compactrio path=ni-9422-scan-interface.html language=enus -->
## TOPIC 00304: NI 9422 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9422-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9422-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return data as Boolean values. Module ChannelsThe NI 9422 has the following channels. 411 Module Channels Channel

### NI 9422 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return data as Boolean values.

#### Module Channels

The NI 9422 has the following channels.

| Channel | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. For the NI 9422, x is 0 to 7. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9422. Right-click the NI 9422 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

#### Specialty Digital Configuration

Use the Specialty Digital
 Configuration page of the C Series Module
 Properties dialog box to configure channels of this module for
 counter input or quadrature input.

Parent topic:

NI 9422

Related concepts:

- Configuring Specialty Digital Functions
- Configuring Counters
- Configuring a Module for Quadrature Input

<!--NI_TOPIC bundle=ni-compactrio path=ni-9422.html language=enus -->
## TOPIC 00305: NI 9422

- bundle_id: `ni-compactrio`
- source_path: `ni-9422.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9422.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8-Channel, Differential or TTL Digital Input Module NI 9422 Pinout 90 NI 9422 Pinout

### NI 9422

CompactRIO 8-Channel, Differential or TTL Digital Input Module

#### NI 9422 Pinout

Figure 90.

[IMAGE alt='image' src='GUID-13B58EC6-650C-42B7-80ED-7EFFC10371C3-a5.svg']

Parent topic:

Digital Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9423-fpga-interface.html language=enus -->
## TOPIC 00306: NI 9423 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9423-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9423-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 412 Terminals in Software Terminal Description DIx Digital input channel x, where x is the number of the channel. The NI 9423 has

### NI 9423 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for reading
 with this device.

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. The NI 9423 has DI channels 0 to 7. |
| DI7:0 | Digital port consisting of channels 0 through 7. Channel 7 is returned in the MSB. Channel 0 is returned in the LSB. |

#### Arbitration

This device supports only the Never
 Arbitrate option for arbitration. You cannot configure arbitration
 settings for this device.

#### I/O
 Methods

Use the FPGA I/O Method Node to access the following I/O methods
 for this device.

| Method | Description |
| --- | --- |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### Module Methods

| Method | Description |
| --- | --- |
| Check Status | Returns a Boolean value that indicates whether the module is ready. |

Note

Check Status

#### I/O
 Properties

This device does not support any I/O properties.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device supports the single-cycle Timed
 Loop. Configure the number of input synchronizing registers for the channels of this
 device in the Advanced Code Generation page of the FPGA I/O Node Properties dialog
 box.

When the module is within a single-cycle Timed Loop, it must be ready to
 perform digital input before a loop containing digital input starts. Poll the
 Ready output of the Check Status method to determine
 whether the module is ready. Digital input operations return invalid data if the
 module is not ready.

While the module is performing digital input within a
 single-cycle Timed Loop, do not perform property reads or remove the module from the
 chassis. Doing either of these actions causes the module to be unable to perform
 digital input and the Ready output of the Check Status method
 to return FALSE.

#### FPGA
 Target Clock Support

This device supports only top-level FPGA target
 clock rates and single-cycle Timed Loop clock rates that are multiples of 40 MHz,
 such as 40 MHz, 80 MHz, 120 MHz, and so on.

Parent topic:

NI 9423

Related concepts:

- Reading from C Series Channels

<!--NI_TOPIC bundle=ni-compactrio path=ni-9423-scan-interface.html language=enus -->
## TOPIC 00307: NI 9423 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9423-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9423-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return data as Boolean values. Module ChannelsThe NI 9423 has the following channels. 416 Module Channels Channel

### NI 9423 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return data as Boolean values.

#### Module Channels

The NI 9423 has the following channels.

| Channel | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. For the NI 9423, x is 0 to 7. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9423. Right-click the NI 9423 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

#### Specialty Digital Configuration

Use the Specialty Digital
 Configuration page of the C Series Module
 Properties dialog box to configure channels of this module for
 counter input or quadrature input.

Parent topic:

NI 9423

Related concepts:

- Configuring Specialty Digital Functions
- Configuring Counters
- Configuring a Module for Quadrature Input

<!--NI_TOPIC bundle=ni-compactrio path=ni-9423.html language=enus -->
## TOPIC 00308: NI 9423

- bundle_id: `ni-compactrio`
- source_path: `ni-9423.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9423.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8-Channel, 24 V, High-Speed Digital Input Module NI 9423 Pinout 91 NI 9423 Pinout

### NI 9423

CompactRIO 8-Channel, 24 V, High-Speed Digital Input Module

#### NI 9423 Pinout

Figure 91.

[IMAGE alt='image' src='GUID-66A01C3F-559A-42EF-915A-84E67323EE9E-a5.svg']

Parent topic:

Digital Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9425-fpga-interface.html language=enus -->
## TOPIC 00309: NI 9425 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9425-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9425-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 417 Terminals in Software Terminal Description DIx Digital input channel x, where x is the number of the channel. The NI 9425 has

### NI 9425 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for reading
 with this device.

#### Terminals in Software

Use the FPGA I/O
 Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. The NI 9425 has DI channels 0 to 31. |
| DI7:0 | Digital port consisting of channels 0 through 7. Channel 7 is returned in the MSB. Channel 0 is returned in the LSB. |
| DI15:8 | Digital port consisting of channels 8 through 15. Channel 15 is returned in the MSB. Channel 8 is returned in the LSB. |
| DI23:16 | Digital port consisting of channels 16 through 23. Channel 23 is returned in the MSB. Channel 16 is returned in the LSB. |
| DI31:24 | Digital port consisting of channels 24 through 31. Channel 31 is returned in the MSB. Channel 24 is returned in the LSB. |
| DI31:0 | Digital port consisting of channels 0 through 31. Channel 31 is returned in the MSB. Channel 0 is returned in the LSB. |

#### Arbitration

This device supports only the Arbitrate if Multiple
 Requestors Only option for arbitration. You cannot configure
 arbitration settings for this device.

#### I/O Methods

This device does not support
 any I/O methods.

#### I/O
 Properties

This device does not support any I/O properties.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9425

Related concepts:

- Reading from C Series Channels

<!--NI_TOPIC bundle=ni-compactrio path=ni-9425-scan-interface.html language=enus -->
## TOPIC 00310: NI 9425 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9425-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9425-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return data as Boolean values. Module ChannelsThe NI 9425 has the following channels. 419 Module Channels Channel

### NI 9425 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return data as Boolean values.

#### Module Channels

The NI 9425 has the following channels.

| Channel | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. For the NI 9425, x is 0 to 31. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9425. Right-click the NI 9425 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9425

<!--NI_TOPIC bundle=ni-compactrio path=ni-9425.html language=enus -->
## TOPIC 00311: NI 9425

- bundle_id: `ni-compactrio`
- source_path: `ni-9425.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9425.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 32-Channel, 24 V, Sinking Digital Input Module NI 9425 Pinout 92 NI 9425 Pinout

### NI 9425

CompactRIO 32-Channel, 24 V, Sinking Digital Input Module

#### NI 9425 Pinout

Figure 92.

[IMAGE alt='image' src='GUID-F4F7AB68-F745-4B5F-A952-F1D4D1DD14C6-a5.svg']

Parent topic:

Digital Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9426-fpga-interface.html language=enus -->
## TOPIC 00312: NI 9426 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9426-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9426-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 420 Terminals in Software Terminal Description DIx Digital input channel x, where x is the number of the channel. The NI 9426 has

### NI 9426 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for reading
 with this device.

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. The NI 9426 has DI channels 0 to 31. |
| DI7:0 | Digital port consisting of channels 0 through 7. Channel 7 is returned in the MSB. Channel 0 is returned in the LSB. |
| DI15:8 | Digital port consisting of channels 8 through 15. Channel 15 is returned in the MSB. Channel 8 is returned in the LSB. |
| DI23:16 | Digital port consisting of channels 16 through 23. Channel 23 is returned in the MSB. Channel 16 is returned in the LSB. |
| DI31:24 | Digital port consisting of channels 24 through 31. Channel 31 is returned in the MSB. Channel 24 is returned in the LSB. |
| DI31:0 | Digital port consisting of channels 0 through 31. Channel 31 is returned in the MSB. Channel 0 is returned in the LSB. |

#### Arbitration

This device supports only the Arbitrate if Multiple
 Requestors Only option for arbitration. You cannot configure
 arbitration settings for this device.

#### I/O
 Methods

This device does not support any I/O methods.

#### I/O
 Properties

This device does not support any I/O properties.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9426

Related concepts:

- Reading from C Series Channels

<!--NI_TOPIC bundle=ni-compactrio path=ni-9426-scan-interface.html language=enus -->
## TOPIC 00313: NI 9426 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9426-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9426-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return data as Boolean values. Module ChannelsThe NI 9426 has the following channels. 422 Module Channels Channel

### NI 9426 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return data as Boolean values.

#### Module Channels

The NI 9426 has the following channels.

| Channel | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. For the NI 9426, x is 0 to 31. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9426. Right-click the NI 9426 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9426

<!--NI_TOPIC bundle=ni-compactrio path=ni-9426.html language=enus -->
## TOPIC 00314: NI 9426

- bundle_id: `ni-compactrio`
- source_path: `ni-9426.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9426.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 32-Channel, 24 V, Sourcing Digital Input Module NI 9426 Pinout 93 NI 9426 Pinout

### NI 9426

CompactRIO 32-Channel, 24 V, Sourcing Digital Input Module

#### NI 9426 Pinout

Figure 93.

[IMAGE alt='image' src='GUID-BD0CB3F9-9665-45D1-93C7-4674B150E0CA-a5.svg']

Parent topic:

Digital Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9435-fpga-interface.html language=enus -->
## TOPIC 00315: NI 9435 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9435-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9435-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 423 Terminals in Software Terminal Description DIx Digital input channel x, where x is the number of the channel. The NI 9435 has

### NI 9435 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for reading
 with this device.

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. The NI 9435 has DI channels 0 to 3. |
| DI3:0 | Digital port consisting of channels 0 through 3. and . Channel 3 is returned in bit 3. Channel 0 is returned in bit 0. Bits 4 through 7 return a zero. |

#### Arbitration

This device supports only the Never
 Arbitrate option for arbitration. You cannot configure arbitration
 settings for this device.

#### I/O
 Methods

Use the FPGA I/O Method Node to access the following I/O methods
 for this device.

| Method | Description |
| --- | --- |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### Module Methods

| Method | Description |
| --- | --- |
| Check Status | Returns a Boolean value that indicates whether the module is ready. |

Note

Check Status

#### I/O
 Properties

This device does not support any I/O properties.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device supports the single-cycle Timed
 Loop. Configure the number of input synchronizing registers for the channels of this
 device in the Advanced Code Generation page of the FPGA I/O Node Properties dialog
 box.

When the module is within a single-cycle Timed Loop, it must be ready to
 perform digital input before a loop containing digital input starts. Poll the
 Ready output of the Check Status method to determine
 whether the module is ready. Digital input operations return invalid data if the
 module is not ready.

While the module is performing digital input within a
 single-cycle Timed Loop, do not perform property reads or remove the module from the
 chassis. Doing either of these actions causes the module to be unable to perform
 digital input and the Ready output of the Check Status method
 to return FALSE.

#### FPGA
 Target Clock Support

This device supports only top-level FPGA target
 clock rates and single-cycle Timed Loop clock rates that are multiples of 40 MHz,
 such as 40 MHz, 80 MHz, 120 MHz, and so on.

Parent topic:

NI 9435

Related concepts:

- Reading from C Series Channels

<!--NI_TOPIC bundle=ni-compactrio path=ni-9435-scan-interface.html language=enus -->
## TOPIC 00316: NI 9435 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9435-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9435-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return data as Boolean values. Module ChannelsThe NI 9435 has the following channels. 427 Module Channels Channel

### NI 9435 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return data as Boolean values.

#### Module Channels

The NI 9435 has the following channels.

| Channel | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. For the NI 9435, x is 0 to 3. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9435. Right-click the NI 9435 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

#### Specialty Digital Configuration

Use the Specialty Digital
 Configuration page of the C Series Module
 Properties dialog box to configure channels of this module for
 counter input or quadrature input.

Parent topic:

NI 9435

Related concepts:

- Configuring Specialty Digital Functions
- Configuring Counters
- Configuring a Module for Quadrature Input

<!--NI_TOPIC bundle=ni-compactrio path=ni-9435.html language=enus -->
## TOPIC 00317: NI 9435

- bundle_id: `ni-compactrio`
- source_path: `ni-9435.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9435.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, AC/DC Universal Digital Input Module NI 9435 Pinout 94 NI 9435 Pinout

### NI 9435

CompactRIO 4-Channel, AC/DC Universal Digital Input Module

#### NI 9435 Pinout

Figure 94.

[IMAGE alt='image' src='GUID-97A1819E-8864-4CB5-B12B-0B7E794A5B98-a5.svg']

Parent topic:

Digital Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9436-fpga-interface.html language=enus -->
## TOPIC 00318: NI 9436 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9436-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9436-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 428 Terminals in Software Terminal Description DIx Digital input channel x, where x is the number of the channel. The NI 9436 has

### NI 9436 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for reading
 with this device.

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. The NI 9436 has DI channels 0 to 7. |
| DI7:0 | Digital port consisting of channels 0 through 7. Channel 7 is returned in the MSB. Channel 0 is returned in the LSB. |

#### Arbitration

This device supports only the Never
 Arbitrate option for arbitration. You cannot configure arbitration
 settings for this device.

#### I/O
 Methods

Use the FPGA I/O Method Node to access the following I/O methods
 for this device.

| Method | Description |
| --- | --- |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### Module Methods

| Method | Description |
| --- | --- |
| Check Status | Returns a Boolean value that indicates whether the module is ready. |

Note

Check Status

#### I/O
 Properties

This device does not support any I/O properties.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device supports the single-cycle Timed
 Loop. Configure the number of input synchronizing registers for the channels of this
 device in the Advanced Code Generation page of the FPGA I/O Node Properties dialog
 box.

When the module is within a single-cycle Timed Loop, it must be ready to
 perform digital input before a loop containing digital input starts. Poll the
 Ready output of the Check Status method to determine
 whether the module is ready. Digital input operations return invalid data if the
 module is not ready.

While the module is performing digital input within a
 single-cycle Timed Loop, do not perform property reads or remove the module from the
 chassis. Doing either of these actions causes the module to be unable to perform
 digital input and the Ready output of the Check
 Status method to return FALSE.

#### FPGA
 Target Clock Support

This device supports only top-level FPGA target
 clock rates and single-cycle Timed Loop clock rates that are multiples of 40 MHz,
 such as 40 MHz, 80 MHz, 120 MHz, and so on.

Parent topic:

NI 9436

Related concepts:

- Reading from C Series Channels

<!--NI_TOPIC bundle=ni-compactrio path=ni-9436-scan-interface.html language=enus -->
## TOPIC 00319: NI 9436 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9436-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9436-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels read and write Boolean values. Module ChannelsThe NI 9436 has the following channels. 432 Module Channels Channel

### NI 9436 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels read and write Boolean
 values.

#### Module Channels

The NI 9436 has the following channels.

| Channel | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. For the NI 9436, x is 0 to 7. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9436. Right-click the NI 9436 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

#### Specialty Digital Configuration

Use the Specialty Digital
 Configuration page of the C Series Module
 Properties dialog box to configure channels of this module for
 counter input or quadrature input.

Parent topic:

NI 9436

Related concepts:

- Configuring Specialty Digital Functions
- Configuring Counters
- Configuring a Module for Quadrature Input

<!--NI_TOPIC bundle=ni-compactrio path=ni-9436.html language=enus -->
## TOPIC 00320: NI 9436

- bundle_id: `ni-compactrio`
- source_path: `ni-9436.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9436.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8 DI, ±100 VDC to ±250 VDC/100 VAC to 250 VAC, Sinking/Sourcing, 10 ms Input Module NI 9436 Pinout 95 NI 9436 Pinout

### NI 9436

CompactRIO 8 DI, ±100 VDC to ±250 VDC/100 VAC to 250 VAC, Sinking/Sourcing, 10 ms Input Module

#### NI 9436 Pinout

Figure 95.

[IMAGE alt='image' src='GUID-0E6A5D97-6959-4E5C-B62D-6D19030A5A5F-a5.svg']

Parent topic:

Digital Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9437-fpga-interface.html language=enus -->
## TOPIC 00321: NI 9437 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9437-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9437-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for reading with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 433 Terminals in Software Terminal Description DIx Digital input channel x, where x is the number of the channel. The NI 9437 has

### NI 9437 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for reading
 with this device.

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. The NI 9437 has DI channels 0 to 7. |
| DI7:0 | Digital port consisting of channels 0 through 7. Channel 7 is returned in the MSB. Channel 0 is returned in the LSB. |

#### Arbitration

This device supports only the Never
 Arbitrate option for arbitration. You cannot configure arbitration
 settings for this device.

#### I/O
 Methods

Use the FPGA I/O Method Node to access the following I/O methods
 for this device.

| Method | Description |
| --- | --- |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to time out immediately, a negative value causes the method to wait indefinitely, and a positive value causes the method to wait for that number of clock ticks before timing out. |

#### Module Methods

| Method | Description |
| --- | --- |
| Check Status | Returns a Boolean value that indicates whether the module is ready. |

Note

Check Status

#### I/O
 Properties

This device does not support any I/O properties.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device supports the single-cycle Timed
 Loop. Configure the number of input synchronizing registers for the channels of this
 device in the Advanced Code Generation page of the FPGA I/O Node Properties dialog
 box.

When the module is within a single-cycle Timed Loop, it must be ready to
 perform digital input before a loop containing digital input starts. Poll the
 Ready output of the Check Status method to determine
 whether the module is ready. Digital input operations return invalid data if the
 module is not ready.

While the module is performing digital input within a
 single-cycle Timed Loop, do not perform property reads or remove the module from the
 chassis. Doing either of these actions causes the module to be unable to perform
 digital input and the Ready output of the Check
 Status method to return FALSE.

#### FPGA
 Target Clock Support

This device supports only top-level FPGA target
 clock rates and single-cycle Timed Loop clock rates that are multiples of 40 MHz,
 such as 40 MHz, 80 MHz, 120 MHz, and so on.

Parent topic:

NI 9437

Related concepts:

- Reading from C Series Channels

<!--NI_TOPIC bundle=ni-compactrio path=ni-9437-scan-interface.html language=enus -->
## TOPIC 00322: NI 9437 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9437-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9437-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables for the channels return calibrated floating-point data in volts. Module ChannelsThe NI 9437 has the following channels. 437 Module

### NI 9437 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables for the channels return calibrated
 floating-point data in volts.

#### Module Channels

The NI 9437 has the following channels.

| Channel | Description |
| --- | --- |
| DIx | Digital input channel x, where x is the number of the channel. For the NI 9437, x is 0 to 7. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9437. Right-click the NI 9437 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9437

<!--NI_TOPIC bundle=ni-compactrio path=ni-9437.html language=enus -->
## TOPIC 00323: NI 9437

- bundle_id: `ni-compactrio`
- source_path: `ni-9437.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9437.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8-Channel, 250 V, Sinking Digital Input Module NI 9437 Pinout 96 NI 9437 Pinout

### NI 9437

CompactRIO 8-Channel, 250 V, Sinking Digital Input Module

#### NI 9437 Pinout

Figure 96.

[IMAGE alt='image' src='GUID-398DA7F5-1A40-4199-9492-6F4A992023AA-a5.svg']

Parent topic:

Digital Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=ni-9467-fpga-interface.html language=enus -->
## TOPIC 00324: NI 9467 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9467-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9467-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node This device does not support any FPGA I/O Nodes. Module MethodsUse the FPGA I/O Method Node to access the following I/O methods for this device. 521 Module Methods Method Description Wait for PPS Waits until a new PPS is detected, indicating the start of a new second. The NI 9467 Modul

### NI 9467 (FPGA Interface)

#### FPGA I/O Node

This device does not
 support any FPGA I/O Nodes.

#### Module Methods

Use the FPGA
 I/O Method Node to access the following I/O methods for this device.

| Method | Description |
| --- | --- |
| Wait for PPS | Waits until a new PPS is detected, indicating the start of a new second. The NI 9467 Module does not generate a PPS at start-up. The module begins generating a PPS only after it obtains the first location fix. This takes 30 seconds or more of access to GPS satellite signals with a clear view of the sky. This method has the following parameters: Timeout (Ticks)—Specifies in FPGA clock ticks how long the Wait for PPS method waits for the PPS to occur. A value of 0 causes the Wait for PPS method to time out immediately, a negative value causes the Wait for PPS method to wait indefinitely, and a positive value causes the Wait for PPS method to wait for that number of clock ticks before timing out. Timed Out—Returns a Boolean value. A value of TRUE indicates that a timeout occurred. The timeout counter starts counting only when module startup is complete. |
| Wait for Data Update | Waits until new data is received for the last PPS and the properties are updated. At start-up, when the PPS generation has not started, this method indicates the periodic update of the GPS Status, Antenna Status, and Number of Satellites properties. In the time between the PPS and when this method completes, the properties update at different times. Therefore, do not read properties during this time. Instead, read them after the Wait for Data Update method completes. This method has the following parameters: Timeout (Ticks)—Specifies in FPGA clock ticks how long the Wait for Data Update method waits for the update to occur. A value of 0 causes the Wait for Data Update method to time out immediately, a negative value causes the Wait for Data Update method to wait indefinitely, and a positive value causes the Wait for Data Update method to wait for that number of clock ticks before timing out. Timed Out—Returns a Boolean value. A value of TRUE indicates that a timeout occurred. The timeout counter starts counting only when module startup is complete. |
| Reset Module | This method makes the module reinitialize to its start-up state. When the module is reset, it stops generating a PPS. The module starts generating a PPS again after it obtains the first location fix. This takes 30 seconds or more of access to GPS satellite signals with a clear view of the sky. |

#### Module Properties

FPGA I/O Property Node

Note

| Property | Type | Description |
| --- | --- | --- |
| PPS Timestamp (TAI) | Read | Returns a U64 value representing the TAI timestamp in nanoseconds of the last PPS. |
| UTC Offset | Read | Returns an I8 value representing the current offset between TAI time and UTC time in seconds. To compute UTC time, the UTC Offset must be subtracted from the TAI time (UTC_Time = TAI_Time – UTC_Offset). The GPS satellites transmit the UTC Offset information only once every 12.5 minutes. This property reports invalid values for up to 12.5 minutes after start-up. Use the UTC Offset Valid property to determine when this property starts returning valid values. |
| UTC Offset Valid | Read | Returns a Boolean indicating if the UTC Offset and leap second information has been received from the GPS satellites, making the UTC Offset, Leap Second Pending, Leap Second Direction, and Leap Second Occurred properties valid. |
| GPS Status | Read | Reports the current GPS status: Normal—The module is operating properly. Unable to get fix—The module is unable to compute a location fix and generate a precise PPS. This occurs during start-up and when the satellite signals are obstructed. Initializing—This status is reported at start-up or after a module reset until the module is initialized. |
| Self-Survey Complete | Read | Returns True if the self-survey is complete.Returns False if the self-survey is in progress. |
| Antenna Status | Read | Reports the current antenna status: Normal—Antenna is detected (present) and there is no overcurrent. Absent—Antenna is not detected. Overcurrent—An overcurrent condition has been detected. Unknown—Status reported while the module is initializing. |
| Leap Second Pending | Read | Boolean that returns True for up to 60 seconds before the leap second occurs, and cleared the second after the leap second occurs. The GPS satellites transmit the Leap Second information only once every 12.5 minutes. This property reports invalid values for up to 12.5 minutes after start-up. Use the UTC Offset Valid property to determine when this property starts returning valid values. |
| Leap Second Occurred | Read | Boolean that returns True starting the first second after the leap second occurs and remains True for 24 hours. The GPS satellites transmit the Leap Second information only once every 12.5 minutes. This property reports invalid values for up to 12.5 minutes after start-up. Use the UTC Offset Valid property to determine when this property starts returning valid values. |
| Leap Second Direction | Read | Returns Add or Delete depending on the kind of leap second event. Only valid when Leap Second Pending or Leap Second Occurred Properties are True. Disregard at other times.The GPS satellites transmit the Leap Second information only once every 12.5 minutes. This property reports invalid values for up to 12.5 minutes after start-up. Use the UTC Offset Valid property to determine when this property starts returning valid values. |
| Altitude (m) | Read | Return the current location coordinates in degrees and altitude in meters. The Altitude property reports altitude in meters HAE (height above ellipsoid). When the GPS receiver cannot compute a location fix during the self-survey (as reported by the GPS Status property), the location properties repeat the information obtained in the last successful location fix. When the self-survey is complete, the location properties return the precise location computed during the self-survey. |
| Latitude (°) | Read |  |
| Longitude (°) | Read |  |
| Satellites Available | Read | Returns the number of satellites the GPS receiver currently is tracking. |
| Firmware | Read | Returns the current GPS receiver firmware version. |
| Module ID | Read | Returns the module ID. |
| Serial Number | Read | Returns the unique module serial number. |
| Vendor ID | Read | Returns the National Instruments vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9467

<!--NI_TOPIC bundle=ni-compactrio path=ni-9467-glossary.html language=enus -->
## TOPIC 00325: Glossary

- bundle_id: `ni-compactrio`
- source_path: `ni-9467-glossary.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9467-glossary.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Clear view of the sky There is no strict definition for a clear view of the sky, but a suitable guideline is that the GPS antenna should have a clear line of sight to the sky in all directions (360°) down to an imaginary line making a 30° angle with the ground. Locations far from trees and tall buil

### Glossary

Clear view of the sky

GPS

Leap second

Location fix

PPS

Self-survey

TAI

UTC

Parent topic:

NI 9467

<!--NI_TOPIC bundle=ni-compactrio path=ni-9467.html language=enus -->
## TOPIC 00326: NI 9467

- bundle_id: `ni-compactrio`
- source_path: `ni-9467.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9467.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 117 NI 9467 front panel

### NI 9467

Figure 117.

NI 9467

[IMAGE alt='image' src='GUID-EB39163B-DF2A-48C0-AD68-8CD9505D4671-a5.svg']

Parent topic:

Timing and Synchronization Module Reference

<!--NI_TOPIC bundle=ni-compactrio path=ni-9475-scan-interface.html language=enus -->
## TOPIC 00327: NI 9475 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9475-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9475-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables write Boolean values to the channels. Module Channels The NI 9475 has the following channels. 479 Module Channels Channel Descripti

### NI 9475 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables write Boolean values to the channels.

#### Module Channels

The NI 9475 has the following channels.

| Channel | Description |
| --- | --- |
| DOx | Digital output channel x, where x is the number of the channel. For the NI 9475, x is 0 to 7. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9475. Right-click the NI 9475 in the Project Explorer
 window and select Properties to display this dialog box. You
 can configure the following options.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

#### Specialty Digital Configuration

Use the Specialty Digital
 Configuration page of the C Series Module
 Properties dialog box to configure channels of this module for
 counter-driven output or pulse-width modulation output.

Parent topic:

NI 9475

Related concepts:

- Configuring Specialty Digital Functions
- Configuring Counter-Driven Outputs
- Configuring a Channel for Pulse-Width Modulation

<!--NI_TOPIC bundle=ni-compactrio path=ni-9475.html language=enus -->
## TOPIC 00328: NI 9475

- bundle_id: `ni-compactrio`
- source_path: `ni-9475.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9475.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 8-Channel, 60 V, High-Speed, Sourcing Digital Output Module NI 9475 Pinout 106 NI 9475 Pinout

### NI 9475

CompactRIO 8-Channel, 60 V, High-Speed, Sourcing Digital Output Module

#### NI 9475 Pinout

Figure 106.

[IMAGE alt='image' src='GUID-17CCF524-3187-4F51-8E9A-7F4151554E0B-a5.svg']

Parent topic:

Digital Output Modules

Related concepts:

- Understanding Power-On and Startup Output States for CompactRIO Output Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9476-fpga-interface.html language=enus -->
## TOPIC 00329: NI 9476 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9476-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9476-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for writing with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 480 Terminals in Software Terminal Description DOx Digital output channel x, where x is the number of the channel. The NI 9476 has

### NI 9476 (FPGA Interface)

#### FPGA I/O Node

Use an FPGA I/O Node
 configured for writing with this device.

#### Terminals in Software

Use the FPGA I/O Node
 to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| DOx | Digital output channel x, where x is the number of the channel. The NI 9476 has DO channels 0 to 31. |
| DO7:0 | Digital port consisting of channels 0 through 7. Channel 7 is returned in the MSB, and channel 0 is returned in the LSB. |
| DO15:8 | Digital port consisting of channels 8 through 15. Channel 15 is returned in the MSB, and channel 8 is returned in the LSB. |
| DO23:16 | Digital port consisting of channels 16 through 23. Channel 23 is returned in the MSB, and channel 16 is returned in the LSB. |
| DO31:24 | Digital port consisting of channels 24 through 31. Channel 31 is returned in the MSB, and channel 24 is returned in the LSB. |
| DO31:0 | Digital port consisting of channels 0 through 31. Channel 31 is returned in the MSB, and channel 0 is returned in the LSB. |

#### Arbitration

This device supports only the
 Arbitrate if Multiple Requestors Only and Never
 Arbitrate options for arbitration. The default arbitration setting is
 Arbitrate if Multiple Requestors Only.

If you are sure that the
 design of the FPGA VI will never allow more than one digital function to execute at the same
 time, even on different channels, enable the Disable Arbitration
 checkbox on the *C Series Module Properties* dialog box to disable arbitration
 and reduce the amount of FPGA logic used by VIs. If more than one digital function could
 execute simultaneously in the FPGA VI, leave the box unchecked.

#### I/O Methods

This device does not support
 any I/O methods.

#### Module Methods

Use the FPGA I/O Method Node
 to access the following module method for this device.

| Method | Description |
| --- | --- |
| Check Output Status | Returns Booleans that indicate whether any channel reported an overcurrent fault during the last time the FPGA I/O Node communicated with the module. When the FPGA I/O Node communicates with the module, the FPGA VI samples the states of the channels and overwrites the previous output status with the latest state of the channels. Force Status Read—When the value of this input is FALSE, the method returns the cached status information from the last status read. When the value is TRUE, the method gets the current status information from the module. Forcing a status read can introduce jitter into a digital output loop. Any Overcurrent—Returns a Boolean value. A value of TRUE indicates an overcurrent condition on at least one channel. Channel Overcurrent—Returns an array of Boolean values. A value of TRUE in any index indicates that the channel sharing a number with that index is in an overcurrent condition. |

#### I/O
 properties

This device does not support any I/O properties.

#### Module
 Properties

Use the FPGA I/O Property Node to access the following module
 properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle Timed
 Loop.

Parent topic:

NI 9476

Related concepts:

- Writing to C Series Channels

<!--NI_TOPIC bundle=ni-compactrio path=ni-9476-scan-interface.html language=enus -->
## TOPIC 00330: NI 9476 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9476-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9476-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O VariablesTo use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables write Boolean values to the channels. Module Channels The NI 9476 has the following channels. 483 Module Channels Channel Descriptio

### NI 9476 (Scan Interface)

#### Module I/O Variables

To use I/O from this
 module in a VI, drag and drop I/O variables from the Project
 Explorer window to the block diagram of the VI. The I/O variables
 write Boolean values to the channels.

#### Module Channels

The NI 9476 has the
 following channels.

| Channel | Description |
| --- | --- |
| DOx | Digital output channel x, where x is the number of the channel. For the NI 9476, x is 0 to 31. |

#### Module-Specific Errors

The NI 9476 can
 return the following module-specific errors.

| Error Code | Description |
| --- | --- |
| 65548 | One or more channels are in overcurrent or overvoltage protection mode. Check the terminals for any fault condition that could be causing an out-of-range voltage or current on the channels. |

#### C Series Module Properties Dialog Box

Use this dialog box to configure the NI 9476. Right-click the NI 9476 in
 the Project Explorer window and select
 Properties to display this dialog box. You can configure
 the following options.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9476

<!--NI_TOPIC bundle=ni-compactrio path=ni-9476.html language=enus -->
## TOPIC 00331: NI 9476

- bundle_id: `ni-compactrio`
- source_path: `ni-9476.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9476.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 36 V, 32-Channel (Sourcing Output), 500 µs C Series Digital Module NI 9476 Pinout 107 NI 9476 Pinout

### NI 9476

36 V, 32-Channel (Sourcing Output), 500 µs C Series Digital Module

#### NI 9476 Pinout

Figure 107.

[IMAGE alt='image' src='GUID-BA7B62C8-4494-4408-9E7D-57058DD718C2-a5.svg']

Parent topic:

Digital Output Modules

Related concepts:

- Understanding Power-On and Startup Output States for CompactRIO Output Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9477-fpga-interface.html language=enus -->
## TOPIC 00332: NI 9477 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9477-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9477-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for writing with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 485 Terminals in Software Terminal Description DOx Digital output channel x, where x is the number of the channel. The NI 9477 has

### NI 9477 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for writing
 with this device.

#### Terminals in Software

Use the FPGA I/O Node to access the following
 terminals for this device.

| Terminal | Description |
| --- | --- |
| DOx | Digital output channel x, where x is the number of the channel. The NI 9477 has DO channels 0 to 31. |
| DO7:0 | Digital port consisting of channels 0 through 7. Channel 7 is returned in the MSB, and channel 0 is returned in the LSB. |
| DO15:8 | Digital port consisting of channels 8 through 15. Channel 15 is returned in the MSB, and channel 8 is returned in the LSB. |
| DO23:16 | Digital port consisting of channels 16 through 23. Channel 23 is returned in the MSB, and channel 16 is returned in the LSB. |
| DO31:24 | Digital port consisting of channels 24 through 31. Channel 31 is returned in the MSB, and channel 24 is returned in the LSB. |
| DO31:0 | Digital port consisting of channels 0 through 31. Channel 31 is returned in the MSB, and channel 0 is returned in the LSB. |

#### Arbitration

This device supports only the Arbitrate if Multiple
 Requestors Only and Never Arbitrate options for
 arbitration. The default arbitration setting is Arbitrate if Multiple
 Requestors Only.

If you are sure that the design of the FPGA VI
 will never allow more than one digital function to execute at the same time, even on
 different channels, enable the Disable Arbitration checkbox
 on the C Series Module Properties dialog box to disable
 arbitration and reduce the amount of FPGA logic used by VIs. If more than one
 digital function could execute simultaneously in the FPGA VI, leave the box
 unchecked.

#### Methods

This device does not support any
 methods.

#### I/O
 Properties

This device does not support any I/O properties.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle
 Timed Loop.

Parent topic:

NI 9477

Related concepts:

- Writing to C Series Channels

<!--NI_TOPIC bundle=ni-compactrio path=ni-9477-scan-interface.html language=enus -->
## TOPIC 00333: NI 9477 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9477-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9477-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O VariablesTo use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables write Boolean values to the channels. Module Channels The NI 9477 has the following channels. 487 Module Channels Channel Descriptio

### NI 9477 (Scan Interface)

#### Module I/O Variables

To use I/O from this module in a VI, drag and drop
 I/O variables from the Project Explorer window to the block
 diagram of the VI. The I/O variables write Boolean values to the channels.

#### Module Channels

The NI 9477 has the following channels.

| Channel | Description |
| --- | --- |
| DOx | Digital output channel x, where x is the number of the channel. For the NI 9477, x is 0 to 31. |

#### C
 Series Module Properties Dialog Box

Use this dialog box to configure the
 NI 9477. Right-click the NI 9477 in the Project Explorer window and
 select Properties to display this dialog box. You can configure the
 following options.

- Name —Specifies the name of the C Series module, which appears
 in the Project Explorer window. LabVIEW assigns a default
 name to the module based on the slot number. You can use this field to give the
 module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9477

<!--NI_TOPIC bundle=ni-compactrio path=ni-9477.html language=enus -->
## TOPIC 00334: NI 9477

- bundle_id: `ni-compactrio`
- source_path: `ni-9477.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9477.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 32-Channel, 5–60 V, Sinking Digital Output Module NI 9477 Pinout 108 NI 9477 Pinout

### NI 9477

CompactRIO 32-Channel, 5–60 V, Sinking Digital Output Module

#### NI 9477 Pinout

Figure 108.

[IMAGE alt='image' src='GUID-AABB9A76-B0F7-485A-88B4-5C57DFE2C122-a5.svg']

Parent topic:

Digital Output Modules

Related concepts:

- Understanding Power-On and Startup Output States for CompactRIO Output Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9478-fpga-interface.html language=enus -->
## TOPIC 00335: NI 9478 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9478-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9478-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for writing with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 488 Terminals in Software Terminal Description DOx Digital output channel x, where x is the number of the channel. The NI 9478 has

### NI 9478 (FPGA Interface)

#### FPGA I/O
 Node

Use an FPGA I/O Node configured for writing with this
 device.

#### Terminals in Software

Use the FPGA I/O Node
 to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| DOx | Digital output channel x, where x is the number of the channel. The NI 9478 has DO channels 0 to 15. |
| DO7:0 | Digital port consisting of channels 0 through 7. Channel 7 is returned in the MSB, and channel 0 is returned in the LSB. |
| DO15:8 | Digital port consisting of channels 8 through 15. Channel 15 is returned in the MSB, and channel 8 is returned in the LSB. |
| DO15:0 | Digital port consisting of channels 0 through 15. Channel 15 is returned in the MSB, and channel 0 is returned in the LSB. |

#### Arbitration

This device supports only the Arbitrate if Multiple
 Requestors Only option for arbitration. You cannot configure arbitration settings
 for this device.

#### I/O
 Methods

This device does not support any I/O methods.

#### Module Methods

Use the FPGA I/O Method Node
 to access the following module method for this device.

| Method | Description |
| --- | --- |
| Check Output Status | Returns Booleans that indicate whether the module reported an overtemp fault or any channel reported an overcurrent fault during the last time the FPGA I/O Node communicated with the module. When the FPGA I/O Node communicates with the module, the FPGA VI samples the states of the module and channels and overwrites the previous output status with the latest state of the module and channels. Limit Selection—Specifies which current limit status information the module reads. Select Active Limit when you want the Channel Overcurrent output to return TRUE for any channel that exceeds the current limit threshold specified for the active current limit set for that channel. Select Limit A to return TRUE for any channel that exceeds the current limit threshold specified for Current Limit A. Select Limit B to return TRUE for any channel that exceeds the current limit threshold specified for Current Limit B. Module Overtemp—Returns a Boolean value. Returns TRUE when the module exceeds its temperature rating. Channel Overcurrent—Returns an array of Boolean values. Returns TRUE in any index when the channel sharing a number with that index exceeded the current limit specified by the Limit Selection input after the last status read. Returns FALSE when the channel did not exceed the current limit after the last status read. |

#### I/O
 properties

This device does not support any I/O properties.

#### Module
 Properties

Use the FPGA I/O Property Node to access the following module
 properties for this device.

| Property | Description |
| --- | --- |
| Active Current Limit | Sets the active current limit for each channel. The value in an index of the input array controls the active current limit for the channel sharing a number with that index. Select No Change to leave the active current limit unchanged for the channel at run time. Select Limit A to set the active current limit for the channel to Current Limit A. Select Limit B to set the active current limit for the channel to Current Limit B. Select No Limit when you want the channel to have no current limit. |
| Current Limit A | Sets the current limit threshold for Current Limit A in binary values. Use the following equation to calculate the binary value from amperes: Binary Value = (Current Value / 5.12 A) × 256 The range of valid current limit values is 0–5.1 A, which corresponds to binary values 0–255. |
| Current Limit B | Sets the current limit threshold for Current Limit B in binary values. Use the following equation to calculate the binary value from amperes: Binary Value = (Current Value / 5.12 A) × 256The range of valid current limit values is 0–5.1 A, which corresponds to binary values 0–255. |
| Module ID | Returns the module ID. |
| Overcurrent Refresh Period | Sets the time in µs it takes a channel to automatically recover if the channel exceeds its active current limit threshold. Values 2 to 255 enable overcurrent refresh and specify the time in tens of µs. For example, a value of 3 sets an overcurrent refresh period of 30 µs. A value of 0 disables overcurrent refresh so the channel remains disabled after exceeding its active current limit until you write to the channel using an FPGA I/O Node. A value of 1 is not supported and sets an overcurrent refresh period of 20 µs. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device does not support the single-cycle Timed
 Loop.

Parent topic:

NI 9478

Related concepts:

- Writing to C Series Channels
- Configuring Current Limits for the NI 9478 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9478-scan-interface.html language=enus -->
## TOPIC 00336: NI 9478 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9478-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9478-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O Variables To use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables write Boolean values to the channels. Module Channels Module Channels The NI 9478 has the following channels. 491 Module Channels C

### NI 9478 (Scan Interface)

#### Module I/O Variables

To use I/O from
 this module in a VI, drag and drop I/O variables from the Project
 Explorer window to the block diagram of the VI. The I/O variables
 write Boolean values to the channels. Module Channels

#### Module Channels

The NI 9478 has the
 following channels.

| Channel | Description |
| --- | --- |
| DOx | Digital output channel x, where x is the number of the channel. For the NI 9478, x is 0 to 15. |

#### Module-Specific Errors

The NI 9478 can
 return the following module-specific errors.

| Error Code | Description |
| --- | --- |
| 65548 | One or more channels are in overcurrent or overvoltage protection mode. Check the terminals for any fault condition that could be causing an out-of-range voltage or current on the channels. |
| 65571 | Serial module over-temperature error: An over-temperature error has occurred since the last time the module was accessed. Check for fault conditions or extraneous voltages on the I/O port. |

#### C Series Module Properties Dialog Box

Use this dialog box to configure the NI 9478. Right-click the NI 9478 in
 the Project Explorer window and select
 Properties to display this dialog box. You can configure
 the following options.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You cannot
 change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Channels —Specifies the channels for which you want to configure
 an active current limit.
- Active Limit —Specifies the current limit for the selected
 channel(s). You can select Limit A , Limit
 B , or No Limit .
- Current Limit A —Specifies one of two current limit values in
 amps for channels on the module. You can enter a value from 0 to 5.1.
- Current Limit B —Specifies one of two current limit values in
 amps for channels on the module. You can enter a value from 0 to 5.1.
- Enable Overcurrent Refresh —If you check this box, a channel
 that exceeds the current limit automatically recovers after a specified amount
 of time, the overcurrent refresh period. If you leave this box unchecked, a
 channel that exceeds the current limit remains disabled until you write to
 it.
- Overcurrent Refresh Period —Specifies the time in µs it takes a
 channel to automatically recover after exceeding the current limit. You can
 enter a value from 20 to 2,550.

Parent topic:

NI 9478

<!--NI_TOPIC bundle=ni-compactrio path=ni-9478.html language=enus -->
## TOPIC 00337: NI 9478

- bundle_id: `ni-compactrio`
- source_path: `ni-9478.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9478.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 16-Channel, 0–50 V Sinking Digital Output Module with Programmable Current Limits NI 9478 Pinout 109 NI 9478 Pinout

### NI 9478

CompactRIO 16-Channel, 0–50 V Sinking Digital Output Module with Programmable Current Limits

#### NI 9478 Pinout

Figure 109.

[IMAGE alt='image' src='GUID-3F0FE6B2-C2E4-4D60-A787-6A02016763C7-a5.svg']

Parent topic:

Digital Output Modules

Related concepts:

- Understanding Power-On and Startup Output States for CompactRIO Output Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9481-fpga-interface.html language=enus -->
## TOPIC 00338: NI 9481 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9481-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9481-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O Node Use an FPGA I/O Node configured for writing with this device. Terminals in SoftwareUse the FPGA I/O Node to access the following terminals for this device. 493 Terminals in Software Terminal Description CHx channel x, where x is the number of the channel. The NI 9481 has channels 0 to

### NI 9481 (FPGA Interface)

#### FPGA
 I/O Node

Use an FPGA I/O Node configured for writing
 with this device.

#### Terminals in Software

Use the FPGA I/O
 Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| CHx | channel x, where x is the number of the channel. The NI 9481 has channels 0 to 3. |
| CH3:0 | Digital port consisting of channels 0 through 3. Channel 3 is returned in bit 3. Channel 0 is returned in bit 0. |

#### Arbitration

Configure the arbitration settings for the channels of this
 device in the Advanced Code Generation page of the FPGA
 I/O Properties dialog box. The default arbitration setting is
 Never Arbitrate.

#### I/O Methods

This device does not support
 any I/O methods.

#### Module Methods

Use the FPGA I/O Method
 Node to access the following module method for this device.

| Method | Description |
| --- | --- |
| Check Status | Returns a Boolean value that indicates whether the module is ready. |

Note

Check Status

#### I/O
 Properties

This device does not support any I/O properties.

#### Module Properties

Use the FPGA I/O Property Node to access the following
 module properties for this device.

| Property | Description |
| --- | --- |
| Module ID | Returns the module ID. |
| Serial Number | Returns the unique serial number of the module. |
| Vendor ID | Returns the NI vendor ID, 0x1093. |

#### Single-Cycle Timed Loop

This device
 supports the single-cycle Timed Loop. Configure the number of output synchronizing
 registers for the channels of this device in the Advanced
 Configuration dialog box.

When the module is within a
 single-cycle Timed Loop, it must be ready to perform digital output before a loop
 containing digital output starts. Poll the Ready output of
 the Check Status method to determine whether the module is ready.
 The module might ignore or delay digital output operations if it is not ready.

While the module is performing digital output within a single-cycle Timed
 Loop, do not perform property reads or remove the module from the chassis. Doing
 either of these actions causes the module to be unable to perform digital output and
 the Ready output of the Check Status method to return FALSE.

#### FPGA Target Clock Support

This device
 supports only top-level FPGA target clock rates and single-cycle Timed Loop clock
 rates that are multiples of 40 MHz, such as 40 MHz, 80 MHz, 120 MHz, and so on.

Parent topic:

NI 9481

Related concepts:

- Writing to C Series Channels

<!--NI_TOPIC bundle=ni-compactrio path=ni-9481-scan-interface.html language=enus -->
## TOPIC 00339: NI 9481 (Scan Interface)

- bundle_id: `ni-compactrio`
- source_path: `ni-9481-scan-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9481-scan-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Module I/O VariablesTo use I/O from this module in a VI, drag and drop I/O variables from the Project Explorer window to the block diagram of the VI. The I/O variables write Boolean values to the channels. Module Channels The NI 9481 has the following channels. 496 Module Channels Channel Descriptio

### NI 9481 (Scan Interface)

#### Module I/O Variables

To use I/O from this
 module in a VI, drag and drop I/O variables from the Project
 Explorer window to the block diagram of the VI. The I/O variables
 write Boolean values to the channels.

#### Module Channels

The NI 9481 has the
 following channels.

| Channel | Description |
| --- | --- |
| DOx | Digital output channel x, where x is the number of the channel. For the NI 9481, x is 0 to 3. |

#### C Series Module Properties Dialog Box

Use this dialog box to configure the NI 9481. Right-click the NI 9481 in
 the Project Explorer window and select
 Properties to display this dialog box. You can configure
 the following options.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this value.
- Location —Specifies a slot in the chassis for the C Series
 module.

Parent topic:

NI 9481

<!--NI_TOPIC bundle=ni-compactrio path=ni-9481.html language=enus -->
## TOPIC 00340: NI 9481

- bundle_id: `ni-compactrio`
- source_path: `ni-9481.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9481.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: CompactRIO 4-Channel, Form A Electromechanical Relay Module NI 9481 Pinout 110 NI 9481 Pinout

### NI 9481

CompactRIO 4-Channel, Form A Electromechanical Relay Module

#### NI 9481 Pinout

Figure 110.

[IMAGE alt='image' src='GUID-CBFA1C0F-7F5E-40A3-A918-C55A9F66378B-a5.svg']

Parent topic:

Digital Output Modules

Related concepts:

- Understanding Power-On and Startup Output States for CompactRIO Output Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=ni-9870-9871-connectors.html language=enus -->
## TOPIC 00341: Connector Pinouts

- bundle_id: `ni-compactrio`
- source_path: `ni-9870-9871-connectors.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/ni-9870-9871-connectors.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following connectors are used with C Series serial modules.The included cables (NI part number 182845-01) act as adapters between the two connector types. For more information about serial interface devices, visit ni.com/serial. DB-9 Connector Pinout120 DB-9 Male Connector Pinout 567 Signal Desc

### Connector Pinouts

The following connectors are used with C Series serial modules.

The included cables (NI part number 182845-01) act as adapters between the two connector types.
 For more information about serial interface devices, visit
 ni.com/serial.

Parent topic:

C Series Serial Interface Modules

#### DB-9 Connector Pinout

Figure 120.

[IMAGE alt='image' src='GUID-591E3582-E833-487D-924C-2D867C9B8F76-a5.svg']

| Pin | 232 Signal DTE | 485 Signal |
| --- | --- | --- |
| 1 | DCD | GND |
| 2 | RXD | CTS+ (HSI+) |
| 3 | TXD | RTS+ (HSO+) |
| 4 | DTR | RXD+ |
| 5 | GND | RXD– |
| 6 | DSR | CTS– (HSI–) |
| 7 | RTS | RTS– (HSO–) |
| 8 | CTS | TXD+ |
| 9 | RI | TXD– |

#### External Power Connector Pinout

Figure 121.

[IMAGE alt='image' src='GUID-DA09AAAF-77E3-481C-90CD-9E55CF336FD3-a5.svg']

| Pin | Signal |
| --- | --- |
| 1 | Power (8–28 VSUP) |
| 2 | COM |
| 3 | Power (8–28 VSUP) |
| 4 | COM |

Note

SUP

#### Modular Jack Connector (RJ50) Pinout

Figure 122.

[IMAGE alt='image' src='GUID-72690ED5-AEA2-4F8B-8AEF-9BC155943A79-a5.svg']

| Pin | 232 Signal | 485 Signal |
| --- | --- | --- |
| 10 | DCD | GND |
| 9 | RXD | CTS+ (HSI+) |
| 8 | TXD | RTS+ (HSO+) |
| 7 | DTR | RXD+ |
| 6 | GND | RXD– |
| 5 | DSR | CTS– (HSI–) |
| 4 | RTS | RTS– (HSO–) |
| 3 | CTS | TXD+ |
| 2 | RI | TXD– |
| 1 | No Connect | No Connect |

<!--NI_TOPIC bundle=ni-compactrio path=programming-modes.html language=enus -->
## TOPIC 00342: Programming Modes

- bundle_id: `ni-compactrio`
- source_path: `programming-modes.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/programming-modes.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure the programming mode for each slot on a chassis.There are three programming modes. The default mode is only set after a fresh install and is determined by what is installed on the controller.7 Programming ModesProgramming ModeResource ItemUsageReal-TimeReal-Time Resources cRIO-904x and cRI

### Programming Modes

Configure the programming mode for each slot on a chassis.

There are three programming modes.

The default mode is only set after a fresh install and is determined by what is installed
 on the controller.

| Programming Mode | Resource Item | Usage |
| --- | --- | --- |
| Real-Time | Real-Time Resources | cRIO-904x and cRIO-905x controllers. Real Time Driver API support such as NI-DAQmx and NI-XNET support. |
| Real-Time Scan | Real-Time Scan Resources | IO Variables and Scan Engine support |
| LabVIEW FPGA | FPGA Target | IO Nodes on FPGA |

Parent topic:

Getting Started with a CompactRIO System in LabVIEW

#### Configuring a Program Mode

Complete the following steps to configure a programming mode. Programming modes can also
 be configured by using the NI System Configuration API.

1. Drag and drop the C Series Module IO Item into the
 resource item for the mode that you want. Refer to the *Programming
 Modes* table above for the resource item to use for each mode.
2. Right-click the Controller Target Item and select
 Deploy All or right-click the Module IO Item and select
 Deploy Module Modes.

#### Dynamic Mode Switching

Note

You can change the programming mode of a cRIO-904x or cRIO-905x controller at any time
 regardless of deployed chassis slot operations. To execute a mode switch safely, the
 module will be put into a safe state. Modules have different behaviors when this occurs.

<!--NI_TOPIC bundle=ni-compactrio path=rs485-termination.html language=enus -->
## TOPIC 00343: RS485 Termination

- bundle_id: `ni-compactrio`
- source_path: `rs485-termination.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/rs485-termination.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each differential pair of wires is a transmission line. You must properly terminate the line to prevent reflections.A common method of terminating a two-wire multidrop RS485 network is to install terminating resistors at each end of the multidrop network. If you daisy-chained multiple instruments to

### RS485 Termination

Each differential pair of wires is a transmission line. You must properly terminate the
 line to prevent reflections.

A common method of terminating a two-wire multidrop RS485 network is to install terminating
 resistors at each end of the multidrop network. If you daisy-chained multiple
 instruments together, you need a terminating resistor at only the first and last
 instruments. The terminating resistor should match the characteristic impedance of the
 transmission line (typically 100 Ω to 120 Ω).

You can order an optional DB-9 RS485 termination connector (NI part number 182844-01)
 that contains embedded terminating resistors for easy termination from
 ni.com/serial.

The following figure shows a multidrop network using terminating resistors.

Figure 127.

[IMAGE alt='Multidrop Network Using Terminating Resistors' src='GUID-972D69B0-0107-4355-87B9-33D08AB5DCB2-a5.svg']

The following figure shows a full-duplex network using terminating resistors.

Figure 128.

[IMAGE alt='Full-Duplex Network Using Terminating Resistors' src='GUID-F4E7E29F-E850-42B8-941F-324620A16A6B-a5.svg']

Parent topic:

Serial Communication

<!--NI_TOPIC bundle=ni-compactrio path=rs485-transceiver-control.html language=enus -->
## TOPIC 00344: RS485 Transceiver Control Modes

- bundle_id: `ni-compactrio`
- source_path: `rs485-transceiver-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/rs485-transceiver-control.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: RS485 hardware supports four transceiver control modes: Four-wire mode. Two-wire mode: DTR controlled with echo. Data terminal ready (DTR) is a control signal indicating a device is ready to communicate. Two-wire mode: DTR controlled. Two-wire mode: auto control. Use hardware transceiver control to

### RS485 Transceiver Control Modes

- Four-wire mode.
- Two-wire mode: DTR controlled with echo. [[1]](#note-d20904e30) [<sup>1</sup>](#fnsrc_1-d20904e30) Data terminal ready (DTR) is a
 control signal indicating a device is ready to communicate.
- Two-wire mode: DTR controlled.
- Two-wire mode: auto control.

Use hardware transceiver control to enable and disable transmitters and receivers so that
 they function on different bus topologies.

The following table lists the status of the transmitters and receivers under each
 transceiver control mode.

| Mode | Transmitter State | Receiver State |
| --- | --- | --- |
| Four-wire mode (default) | Always enabled | Always enabled |
| Two-wire mode: DTR controlled with echo | Enabled when DTR asserted | Always enabled |
| Two-wire mode: DTR controlled | Enabled when DTR asserted | Enabled when DTR unasserted |
| Two-wire mode: Auto Control | Enabled when transmitting data | Enabled when not transmitting data |

#### Four-Wire Mode

Use the four-wire mode for
 most full-duplex systems. In the four-wire mode, the transmitter and receiver are
 always enabled. Four-wire mode is the default mode.

#### Two-Wire Mode: DTR Controlled with Echo

Use two-wire mode in half-duplex systems where you need to control the
 transmitter programmatically. In the DTR-with-echo mode, the transmitter is
 tri-stated when the DTR signal of the UART (Universal Asynchronous
 Receiver/Transmitter) is unasserted.

To transmit, the application first must
 enable the transmitter by asserting DTR. After the data is fully transmitted, your
 application unasserts DTR to disable the transmitter. Because the receiver is always
 enabled in this mode, you receive packets not only from other devices, but also your
 transmitter. Thus, your receiver echoes all data you transmit.

#### Two-Wire Mode: DTR Controlled

This mode
 is similar to the two-wire, DTR-with-echo mode.

Although this mode uses the
 same method as the DTR-with-echo mode to control the transmitter, the hardware
 automatically disables the receiver whenever the transmitter is enabled. You do not
 receive the packets sent from your transmitter.

#### Two-Wire Mode: Auto Control

In the
 two-wire auto control mode, serial hardware transparently enables the transmitter
 and receiver in a two-wire system.

Use this mode to remove the burden of
 transceiver control from your application. The hardware automatically enables the
 transmitter for each byte to be transmitted. The hardware also disables the receiver
 whenever the transmitter is enabled. You do not receive the packets sent from your
 transmitter.

Handshaking lines (RTS/CTS) are disabled in the two-wire auto
 control mode mode.

Note

Serial Communication
 Issues

Parent topic:

RS485

[<sup>1</sup>](#note_ref-d20904e30) Data terminal ready (DTR) is a
 control signal indicating a device is ready to communicate.

<!--NI_TOPIC bundle=ni-compactrio path=rs485.html language=enus -->
## TOPIC 00345: RS485

- bundle_id: `ni-compactrio`
- source_path: `rs485.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/rs485.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: As specified in the EIA-485 Standard, Standard for Electrical Characteristics of Generators and Receivers for Use in Balanced Digital Multipoint Systems, RS485 expands on the RS422 standard by increasing the number of devices you can use from 10 to 32 and by working with half-duplex bus architecture

### RS485

As specified in the EIA-485 Standard, Standard for Electrical Characteristics of
 Generators and Receivers for Use in Balanced Digital Multipoint Systems,
 RS485 expands on the RS422 standard by increasing the number of devices you can use from
 10 to 32 and by working with half-duplex bus architectures.

Unlike the RS422 standard, RS485 addresses the issue of using multiple transmitters on
 the same line. RS485 defines the electrical characteristics necessary to ensure adequate
 signal voltages under maximum load, as well as short-circuit protection.

RS485 can also withstand multiple drivers driving conflicting signals at the same time.

Parent topic:

Communication Standards

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9603-9608-9609-9628-9638-9629-can-api.html language=enus -->
## TOPIC 00346: sbRIO-9603/9608/9609/9628/9638/9629 CAN API

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9603-9608-9609-9628-9638-9629-can-api.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9603-9608-9609-9628-9638-9629-can-api.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: FPGA I/O NodeUse an FPGA I/O Node for CAN Input or CAN Output.You can select the following terminals for this device. 601 Terminals in Software Terminal Description CAN0 CAN Port 0 I/O MethodsUse the following I/O methods on the sbRIO-9603/9608/9609/9628/9638/9629. 602 I/O Methods Method Description

### sbRIO-9603/9608/9609/9628/9638/9629 CAN API

#### FPGA I/O Node

Use an FPGA I/O Node for
 CAN Input or CAN Output.

You can select the following terminals for this
 device.

| Terminal | Description |
| --- | --- |
| CAN0 | CAN Port 0 |

#### I/O Methods

Use the following I/O methods
 on the sbRIO-9603/9608/9609/9628/9638/9629.

| Method | Description |
| --- | --- |
| Abort Transmit | Abort a pending CAN frame transmission. |
| Reset | Reset the CAN port to the same state as when the FPGA VI started running. |
| Start | Start communication. |
| Stop | Stop communication. |
| Wait on Comm State Change | Wait for a change in the communication state of the CAN port (Comm State property). |
| Wait on Transceiver Wakeup | Wait for the Transceiver Mode property to change from Sleep to Normal mode due to a remote wakeup (bus activity) or local wakeup. |
| Wait on Transmit Complete | Wait for all frames written to CAN Output to complete transmission. |

#### I/O Properties

Use the FPGA I/O Property
 Node to access the following properties with the
 sbRIO-9603/9608/9609/9628/9638/9629.

| Property | Description | Read While Stopped? | Read While Running? | Write While Stopped? | Write While Running? |
| --- | --- | --- | --- | --- | --- |
| Baud Rate | Specifies the baud rate and default sample point for CAN bus. | No | No | Yes | No |
| Baud Rate Advanced | Specifies custom baud rate and sample point for CAN bus. | No | No | Yes | No |
| FD Baud Rate | Specifies the baud rate and default sample point for CAN bus with flexible data rate. | No | No | Yes | No |
| FD Baud Rate Advanced | Specifies custom baud rate and sample point for CAN bus with flexible data rate. | No | No | Yes | No |
| Comm State | Describes the current communication state of the CAN controller. | Yes | Yes | N/A | N/A |
| Listen Only | Controls listen-only mode for passive monitoring/logging. | No | No | Yes | No |
| I/O Mode | Sets the CAN operating mode to CAN(default), CAN FD or CAN FD + BRS. | No | No | Yes | No |
| Input Timeout (ms) | Specifies the time to wait for the reading of CAN frame using CAN Input. The resolution is in milliseconds. | No | No | Yes | No |
| Output Timeout (ms) | Specifies the time to wait for the writing of CAN frame using CAN Output. The resolution is in milliseconds. | No | No | Yes | No |
| Log Bus Errors | Enables the logging of bus errors as frames that can be read using the CAN Input node. | No | No | Yes | Yes |
| Log Transceiver Faults | Enables the logging of transceiver faults as frames that can be read using the CAN Input node. | No | No | Yes | Yes |
| Self Reception | Specifies whether to echo successfully transmitted CAN frames to be read using CAN Input. | No | No | Yes | Yes |
| Single Shot Transmit | Specifies whether to retry failed CAN frame transmissions. | No | No | Yes | No |
| Receive Error Counter | Provides access to the CAN controller Receive Error Counter. | Yes | Yes | N/A | N/A |
| Transmit Error Counter | Provides access to the CAN controller Transmit Error Counter. | Yes | Yes | N/A | N/A |
| Transceiver Mode | Sets the mode for the CAN transceiver and the associated mode in the TCAN4550 CAN controller. | No | Yes | No | Yes |

Parent topic:

Single-Board RIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9603.html language=enus -->
## TOPIC 00347: sbRIO-9603

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9603.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9603.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: sbRIO-9603 Pinouts 150 Connector J3, CAN Port 151 Connector J4, Serial Port

### sbRIO-9603

#### sbRIO-9603 Pinouts

Figure 150.

[IMAGE alt='image' src='GUID-D6DCFD08-AC48-4E73-8B16-1D66C32E1BD2-a5.svg']

Figure 151.

[IMAGE alt='image' src='GUID-9BAA4C6A-AEC7-4E0E-A695-33051B877AFE-a5.svg']

Parent topic:

Single-Board RIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9607.html language=enus -->
## TOPIC 00348: sbRIO-9607

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9607.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9607.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: sbRIO-9607 Pinouts 152 Connector W500, CAN Port 153 Connector W501, Serial Port

### sbRIO-9607

#### sbRIO-9607 Pinouts

Figure 152.

[IMAGE alt='image' src='GUID-D08260CD-F780-42D6-8345-143C38BA042E-a5.svg']

Figure 153.

[IMAGE alt='image' src='GUID-5D098CBE-53B8-4570-A501-1FEB5365F39D-a5.svg']

Parent topic:

Single-Board RIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9608.html language=enus -->
## TOPIC 00349: sbRIO-9608

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9608.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9608.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: sbRIO-9608 Pinouts 154 Connector J3, CAN Port 155 Connector J4, Serial Port

### sbRIO-9608

#### sbRIO-9608 Pinouts

Figure 154.

[IMAGE alt='image' src='GUID-D6DCFD08-AC48-4E73-8B16-1D66C32E1BD2-a5.svg']

Figure 155.

[IMAGE alt='image' src='GUID-9BAA4C6A-AEC7-4E0E-A695-33051B877AFE-a5.svg']

Parent topic:

Single-Board RIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9609.html language=enus -->
## TOPIC 00350: sbRIO-9609

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9609.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9609.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: sbRIO-9609 Pinouts 156 Connector J3, CAN Port 157 Connector J4, Serial Port

### sbRIO-9609

#### sbRIO-9609 Pinouts

Figure 156.

[IMAGE alt='image' src='GUID-D6DCFD08-AC48-4E73-8B16-1D66C32E1BD2-a5.svg']

Figure 157.

[IMAGE alt='image' src='GUID-9BAA4C6A-AEC7-4E0E-A695-33051B877AFE-a5.svg']

Parent topic:

Single-Board RIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9627-fpga-interface.html language=enus -->
## TOPIC 00351: sbRIO-9627 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9627-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9627-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use an FPGA I/O Node configured for reading and writing with this device. Use the FPGA I/O Node to access the following terminals for this device.630 Terminals in Software Terminal Description Connector0/AIx Analog input channel x, where x is the number of the channel. The sbRIO-9627 has AI channels

### sbRIO-9627 (FPGA Interface)

Use an FPGA I/O Node configured for reading and writing
 with this device.

Use the FPGA I/O Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| Connector0/AIx | Analog input channel x, where x is the number of the channel. The sbRIO-9627 has AI channels 0 to 15. |
| Connector0/AOx | Analog output channel x, where x is the number of the channel. The sbRIO-9627 has AO channels 0 to 3. |
| Connector0/DIOx | Digital input/output channel x, where x is the number of the channel. The sbRIO-9627 has channels 0 to 3. Use the FPGA I/O Node, the Set Output Data method or Set Output Enable method to access this channel. |

#### Arbitration

Configure the arbitration
 settings for the DIO channels of this device in the Advanced Code
 Generation page of the FPGA I/O Properties
 dialog box. The default arbitration setting is Never Arbitrate.

#### I/O Methods

Use the FPGA I/O Method Node
 to access the following I/O methods for this device.

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |

#### Module Methods

This device does not
 support any module methods.

#### Module Properties

Use the FPGA I/O
 Property Node to access the following properties for this device.

| Property | Description |
| --- | --- |
| Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended) or DIFF (differential). This property overwrites the value you configure in the FPGA I/O Properties dialog box. |
| Voltage Range | Sets the input range for a channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the FPGA I/O Properties dialog box. |

#### Single-Cycle Timed Loop

This device supports the single-cycle Timed Loop
 for digital I/O only. To configure the number of output synchronizing registers or
 input synchronizing registers for the channels on this device, use the
 Advanced Code Generation page of the FPGA I/O
 Properties dialog box.

Parent topic:

sbRIO-9627

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9627.html language=enus -->
## TOPIC 00352: sbRIO-9627

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9627.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9627.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: sbRIO-9627 Pinouts 158 Connector J5, MIO 159 Connector W1, CAN Port 160 Connectors W2 and W4, RS-232 Serial Ports 161 Connector W3, RS-485 Serial Port

### sbRIO-9627

#### sbRIO-9627 Pinouts

Figure 158.

[IMAGE alt='image' src='GUID-C1299541-FF76-4576-9703-CA9F5B908E38-a5.svg']

Figure 159.

[IMAGE alt='image' src='GUID-A216FEC0-D22A-4C9A-99B6-2751C2D97030-a5.svg']

Figure 160.

[IMAGE alt='image' src='GUID-4BB7D9B0-514B-45D4-860D-CDEC6C07C9E9-a5.svg']

Figure 161.

[IMAGE alt='image' src='GUID-06AFF367-3834-4CE9-9CF1-A557E94C7633-a5.svg']

Parent topic:

Single-Board RIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9628-fpga-interface.html language=enus -->
## TOPIC 00353: sbRIO-9628 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9628-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9628-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use an FPGA I/O Node configured for reading and writing with this device. Use the FPGA I/O Node to access the following terminals for this device.633 Terminals in Software Terminal Description Conn0_AI/AIx Analog input channel x, where x is the number of the channel. The sbRIO-9628 has AI channels 0

### sbRIO-9628 (FPGA Interface)

Use an FPGA I/O Node configured for reading and writing
 with this device.

Use the FPGA I/O Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| Conn0_AI/AIx | Analog input channel x, where x is the number of the channel. The sbRIO-9628 has AI channels 0 to 15. |
| Conn0_AO/AOx | Analog output channel x, where x is the number of the channel. The sbRIO-9628 has AO channels 0 to 3. |
| Conn0_DIO0-3/DIOx | Digital input/output channel x, where x is the channel number. The sbRIO-9628 has DIO channels 0 to 3. |
| Conn0_DIO0-3/DIO3:0 | Digital port consisting of channels 0 through 3. Channel 3 signifies the MSB and channel 0 signifies the LSB. |

#### Arbitration

You cannot configure
 arbitration settings for analog input and analog output channels of this device.
 Analog input and analog output channels on this device only support the
 Arbitrate if Multiple Requestors Only option for arbitration.

Configure the arbitration settings for digital output channels on this device
 in the Advanced Code Generation page on the FPGA I/O
 Properties dialog box. The default arbitration setting is
 Never Arbitrate.

Digital input channels on this device
 only support the Never Arbitrate option for arbitration. You cannot
 configure arbitration settings for digital input channels on this device.

#### I/O Methods

Use the FPGA I/O Method Node
 to access the following I/O methods for this device.

| Method | I/O Type | Description |
| --- | --- | --- |
| Set Output Data | DIO | Refer to the FPGA I/O Method Node topic for a description of this method. |
| Set Output Enable | DIO | Sets the line direction of the digital channel or the digital port. Refer to the FPGA I/O Method Node topic for a description of this method. |

#### Module Methods

Use the FPGA I/O Method
 Node to access the following I/O methods for this device.

| Method | I/O Type | Description |
| --- | --- | --- |
| Check Status | DIO | Returns a Boolean value that indicates whether the DIO module is ready for I/O operations. |

#### I/O Properties

Use the FPGA I/O Property
 Node to access the following properties for this device.

| Property | I/O Type | Description |
| --- | --- | --- |
| Terminal Mode | AI | Sets the terminal mode for a channel as RSE (referenced single-ended) or DIFF (differential). This property overwrites the value you configure in the Module Properties dialog box. You cannot configure channels 8 through 15 to DIFF mode. |
| Voltage Range | AI | Sets the input range for a channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Module Properties dialog box. |
| LSB Weight | AO | Returns the LSB weight in nV/LSB for the channel. Use this value to convert AO data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset | AO | Returns the calibration offset in nV for the channel. Use this value to convert AO data if you set the Calibration Mode to Raw in the Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O
 Property Node to access the following properties for this device.

| Property | I/O Type | Description |
| --- | --- | --- |
| LSB Weight (±10 V range) | AI | Returns the LSB weight in pV/LSB for the ±10 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| LSB Weight (±5 V range) | AI | Returns the LSB weight in pV/LSB for the ±5 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| LSB Weight (±2 V range) | AI | Returns the LSB weight in pV/LSB for the ±2 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| LSB Weight (±1 V range) | AI | Returns the LSB weight in pV/LSB for the ±1 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset (±10 V range) | AI | Returns the calibration offset in nV for the ±10 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset (±5 V range) | AI | Returns the calibration offset in nV for the ±5 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset (±2 V range) | AI | Returns the calibration offset in nV for the ±2 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset (±1 V range) | AI | Returns the calibration offset in nV for the ±1 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |

#### Single-Cycle Timed Loop

This device
 supports the single-cycle Timed Loop for digital I/O only. To configure the number
 of output synchronizing registers or input synchronizing registers for the channels
 on this device, use the Advanced Code Generation page of the
 FPGA I/O Properties dialog box

The Set
 Output Enable method node is not supported in the single-cycle Timed
 Loop. When writing to a DIO I/O node in a single-cycle Timed Loop, the I/O node will
 not change the DIO line directions. To set the line directions to output when
 writing to the DIO channels in a single-cycle Timed Loop, either configure the
 default line directions to output in the Module Properties
 dialog box, or use the Set Output Enable method node outside a
 single-cycle Timed Loop.

This device supports the Number of
 Synchronizing Registers for Output Data synchronizing register option
 when used in SCTL output. This option supports the same functionality as the
 Number of Synchronizing Registers for Output Data option
 described in the Advanced Code Generation FPGA I/O Properties Page (FPGA Module)
 topic, with the exception that you can use this option only in a single-cycle Timed
 Loop. Implement either 0 or 1 synchronizing registers inside the single-cycle Timed
 Loop. Note that if you configure 0 synchronizing registers outside of the
 single-cycle Timed Loop, the FPGA VI implements 1 synchronizing register by default.

When the device is within a single-cycle Timed Loop, it must be ready to
 perform digital I/O before a loop containing digital I/O starts. Poll the
 Ready output of the Check Status
 method to determine whether the module is ready. Digital input operations return
 invalid data if the module is not ready. The module also might ignore or delay
 digital output operations if it is not ready.

Parent topic:

sbRIO-9628

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9628.html language=enus -->
## TOPIC 00354: sbRIO-9628

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9628.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9628.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: sbRIO-9628 Pinouts 162 Connector J2, MIO 163 Connector J3, CAN Port 164 Connectors J4 and J6, RS-232 Serial Ports 165 Connector J5, RS-485 Serial Port

### sbRIO-9628

#### sbRIO-9628 Pinouts

Figure 162.

[IMAGE alt='image' src='GUID-34E29D02-C389-4000-A1D6-826D707A9B36-a5.svg']

Figure 163.

[IMAGE alt='image' src='GUID-27E8F471-3C75-4658-9BC6-DD7D35639E3D-a5.svg']

Figure 164.

[IMAGE alt='image' src='GUID-E825334A-F9C2-4BFD-879D-7C2851AA4D4D-a5.svg']

Figure 165.

[IMAGE alt='image' src='GUID-3C1FE9F5-8032-417F-B653-B656D4BCF902-a5.svg']

Parent topic:

Single-Board RIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9629-fpga-interface.html language=enus -->
## TOPIC 00355: sbRIO-9629 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9629-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9629-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use an FPGA I/O Node configured for reading and writing with this device. Use the FPGA I/O Node to access the following terminals for this device. 639 Terminals in Software Terminal Description Conn0_AI/AIx Analog input channel x, where x is the number of the channel. The sbRIO-9629 has AI channels

### sbRIO-9629 (FPGA Interface)

Use an FPGA I/O Node configured for reading and writing
 with this device.

Use the FPGA I/O Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| Conn0_AI/AIx | Analog input channel x, where x is the number of the channel. The sbRIO-9629 has AI channels 0 to 15. |
| Conn0_AO/AOx | Analog output channel x, where x is the number of the channel. The sbRIO-9629 has AO channels 0 to 3. |
| Conn0_DIO0-3/DIOx | Digital input/output channel x, where x is the channel number. The sbRIO-9629 has DIO channels 0 to 3. |
| Conn0_DIO0-3/DIO3:0 | Digital port consisting of channels 0 through 3. Channel 3 signifies the MSB and channel 0 signifies the LSB. |

#### Arbitration

You cannot configure
 arbitration settings for analog input and analog output channels of this device.
 Analog input and analog output channels on this device only support the
 Arbitrate if Multiple Requestors Only option for arbitration.

Configure the arbitration settings for digital output channels on this device
 in the Advanced Code Generation page on the FPGA I/O
 Properties dialog box. The default arbitration setting is
 Never Arbitrate.

Digital input channels on this device
 only support the Never Arbitrate option for arbitration. You cannot
 configure arbitration settings for digital input channels on this device.

#### I/O Methods

Use the FPGA I/O Method Node
 to access the following I/O methods for this device.

| Method | I/O Type | Description |
| --- | --- | --- |
| Set Output Data | DIO | Refer to the FPGA I/O Method Node topic for a description of this method. |
| Set Output Enable | DIO | Sets the line direction of the digital channel or the digital port. Refer to the FPGA I/O Method Node topic for a description of this method. |

#### Module Methods

Use the FPGA I/O Method
 Node to access the following I/O methods for this device.

| Method | I/O Type | Description |
| --- | --- | --- |
| Check Status | DIO | Returns a Boolean value that indicates whether the DIO module is ready for I/O operations. |

#### I/O Properties

Use the FPGA I/O Property
 Node to access the following properties for this device.

| Property | I/O Type | Description |
| --- | --- | --- |
| Terminal Mode | AI | Sets the terminal mode for a channel as RSE (referenced single-ended) or DIFF (differential). This property overwrites the value you configure in the Module Properties dialog box. You cannot configure channels 8 through 15 to DIFF mode. |
| Voltage Range | AI | Sets the input range for a channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Module Properties dialog box. |
| LSB Weight | AO | Returns the LSB weight in nV/LSB for the channel. Use this value to convert AO data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset | AO | Returns the calibration offset in nV for the channel. Use this value to convert AO data if you set the Calibration Mode to Raw in the Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O
 Property Node to access the following properties for this device.

| Property | I/O Type | Description |
| --- | --- | --- |
| LSB Weight (±10 V range) | AI | Returns the LSB weight in pV/LSB for the ±10 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| LSB Weight (±5 V range) | AI | Returns the LSB weight in pV/LSB for the ±5 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| LSB Weight (±2 V range) | AI | Returns the LSB weight in pV/LSB for the ±2 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| LSB Weight (±1 V range) | AI | Returns the LSB weight in pV/LSB for the ±1 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset (±10 V range) | AI | Returns the calibration offset in nV for the ±10 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset (±5 V range) | AI | Returns the calibration offset in nV for the ±5 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset (±2 V range) | AI | Returns the calibration offset in nV for the ±2 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset (±1 V range) | AI | Returns the calibration offset in nV for the ±1 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |

#### Single-Cycle Timed Loop

This device
 supports the single-cycle Timed Loop for digital I/O only. To configure the number
 of output synchronizing registers or input synchronizing registers for the channels
 on this device, use the Advanced Code Generation page of the
 FPGA I/O Properties dialog box

The Set
 Output Enable method node is not supported in the single-cycle Timed
 Loop. When writing to a DIO I/O node in a single-cycle Timed Loop, the I/O node will
 not change the DIO line directions. To set the line directions to output when
 writing to the DIO channels in a single-cycle Timed Loop, either configure the
 default line directions to output in the Module Properties
 dialog box, or use the Set Output Enable method node outside a
 single-cycle Timed Loop.

This device supports the Number of
 Synchronizing Registers for Output Data synchronizing register option
 when used in SCTL output. This option supports the same functionality as the
 Number of Synchronizing Registers for Output Data option
 described in the Advanced Code Generation FPGA I/O Properties Page (FPGA Module)
 topic, with the exception that you can use this option only in a single-cycle Timed
 Loop. Implement either 0 or 1 synchronizing registers inside the single-cycle Timed
 Loop. Note that if you configure 0 synchronizing registers outside of the
 single-cycle Timed Loop, the FPGA VI implements 1 synchronizing register by default.

When the device is within a single-cycle Timed Loop, it must be ready to
 perform digital I/O before a loop containing digital I/O starts. Poll the
 Ready output of the Check Status
 method to determine whether the module is ready. Digital input operations return
 invalid data if the module is not ready. The module also might ignore or delay
 digital output operations if it is not ready.

Parent topic:

sbRIO-9629

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9629.html language=enus -->
## TOPIC 00356: sbRIO-9629

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9629.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9629.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: sbRIO-9629 Pinouts 166 Connector J2, MIO 167 Connector J3, CAN Port 168 Connectors J4 and J6, RS-232 Serial Ports 169 Connector J5, RS-485 Serial Port

### sbRIO-9629

#### sbRIO-9629 Pinouts

Figure 166.

[IMAGE alt='image' src='GUID-34E29D02-C389-4000-A1D6-826D707A9B36-a5.svg']

Figure 167.

[IMAGE alt='image' src='GUID-27E8F471-3C75-4658-9BC6-DD7D35639E3D-a5.svg']

Figure 168.

[IMAGE alt='image' src='GUID-E825334A-F9C2-4BFD-879D-7C2851AA4D4D-a5.svg']

Figure 169.

[IMAGE alt='image' src='GUID-3C1FE9F5-8032-417F-B653-B656D4BCF902-a5.svg']

Parent topic:

Single-Board RIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9637-fpga-interface.html language=enus -->
## TOPIC 00357: sbRIO-9637 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9637-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9637-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use an FPGA I/O Node configured for reading and writing with this device. Use the FPGA I/O Node to access the following terminals for this device. 644 Terminals in Software Terminal Description Connector0/AIx Analog input channel x, where x is the number of the channel. The sbRIO-9637 has AI channel

### sbRIO-9637 (FPGA Interface)

Use an FPGA I/O Node configured for reading and writing
 with this device.

Use the FPGA I/O Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| Connector0/AIx | Analog input channel x, where x is the number of the channel. The sbRIO-9637 has AI channels 0 to 15. |
| Connector0/AOx | Analog output channel x, where x is the number of the channel. The sbRIO-9637 has AO channels 0 to 3. |
| Connectorx/DIOy | Digital input/output channel y on connector x, where y is the channel number and x is the connector number. The sbRIO-9637 has channels 0 to 27. Use the FPGA I/O Node, the Set Output Data method, or the Set Output Enable method to access this channel. |

#### Arbitration

Configure the arbitration
 settings for the DIO channels of this device in the Advanced Code
 Generation page of the FPGA I/O Properties
 dialog box. The default arbitration setting is Never Arbitrate.

#### I/O Methods

Use the FPGA I/O Method Node
 to access the following I/O methods for this device.

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |

#### Module Methods

This device does not
 support any module methods.

#### Module Properties

Use the FPGA I/O
 Property Node to access the following properties for this device.

| Property | Description |
| --- | --- |
| Terminal Mode | Sets the terminal mode for a channel as RSE (referenced single-ended) or DIFF (differential). This property overwrites the value you configure in the FPGA I/O Properties dialog box. |
| Voltage Range | Sets the input range for a channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the FPGA I/O Properties dialog box. |

#### Single-Cycle Timed Loop

This device supports the single-cycle Timed Loop
 for digital I/O only. To configure the number of output synchronizing registers or
 input synchronizing registers for the channels on this device, use the
 Advanced Code Generation page of the FPGA I/O
 Properties dialog box.

Parent topic:

sbRIO-9637

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9637.html language=enus -->
## TOPIC 00358: sbRIO-9637

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9637.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9637.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: sbRIO-9637 Pinouts 170 Connector J4, DIO 171 Connector J5, MIO 172 Connector W1, CAN Port 173 Connectors W2 and W4, RS-232 Serial Ports 174 Connector W3, RS-485 Serial Port

### sbRIO-9637

#### sbRIO-9637 Pinouts

Figure 170.

[IMAGE alt='image' src='GUID-D44FE976-7E9D-491F-BF0D-EC2BE807EE83-a5.svg']

Figure 171.

[IMAGE alt='image' src='GUID-E307BFD9-129B-4E88-9677-EF258833B73F-a5.svg']

Figure 172.

[IMAGE alt='image' src='GUID-9455EAC4-C4B9-4045-B5D1-9A9A61E1AA26-a5.svg']

Figure 173.

[IMAGE alt='image' src='GUID-4203C8F0-3B9E-4CE6-A76A-C2D05967B14F-a5.svg']

Figure 174.

[IMAGE alt='image' src='GUID-9DBD96C5-89D3-4157-8C44-8E5D09550DBC-a5.svg']

Parent topic:

Single-Board RIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9638-fpga-interface.html language=enus -->
## TOPIC 00359: sbRIO-9638 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9638-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9638-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use an FPGA I/O Node configured for reading and writing with this device. Use the FPGA I/O Node to access the following terminals for this device. 647 Terminals in Software Terminal Description Conn0_AI/AIx Analog input channel x, where x is the number of the channel. The sbRIO-9638 has AI channels

### sbRIO-9638 (FPGA Interface)

Use an FPGA I/O Node configured for reading and writing
 with this device.

Use the FPGA I/O Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| Conn0_AI/AIx | Analog input channel x, where x is the number of the channel. The sbRIO-9638 has AI channels 0 to 15. |
| Conn0_AO/AOx | Analog output channel x, where x is the number of the channel. The sbRIO-9638 has AO channels 0 to 3. |
| Connw_DIOx-y/DIOz | Digital input/output channel z on connector w, where z is the channel number, w is the connector number, and x and y specify the module that contains the channel. The sbRIO-9638 has DIO channels 0 to 27 organized into 4 separate modules. |
| Connw_DIOx-y/DIOy:x | Digital port consisting of channels x and y on connector w. Channel y signifies the MSB and channel x signifies the LSB. |

#### Arbitration

You cannot configure
 arbitration settings for analog input and analog output channels of this device.
 Analog input and analog output channels on this device only support the
 Arbitrate if Multiple Requestors Only option for arbitration.

Configure the arbitration settings for digital output channels on this device
 in the Advanced Code Generation page on the FPGA I/O
 Properties dialog box. The default arbitration setting is
 Never Arbitrate.

Digital input channels on this device
 only support the Never Arbitrate option for arbitration. You cannot
 configure arbitration settings for digital input channels on this device.

#### I/O Methods

Use the FPGA I/O Method Node
 to access the following I/O methods for this device.

| Method | I/O Type | Description |
| --- | --- | --- |
| Set Output Data | DIO | Refer to the FPGA I/O Method Node topic for a description of this method. |
| Set Output Enable | DIO | Sets the line direction of the digital channel or the digital port. Refer to the FPGA I/O Method Node topic for a description of this method. |

#### Module Methods

Use the FPGA I/O Method
 Node to access the following I/O methods for this device.

| Method | I/O Type | Description |
| --- | --- | --- |
| Check Status | DIO | Returns a Boolean value that indicates whether the DIO module is ready for I/O operations. |

#### I/O Properties

Use the FPGA I/O Property
 Node to access the following properties for this device.

| Property | I/O Type | Description |
| --- | --- | --- |
| Terminal Mode | AI | Sets the terminal mode for a channel as RSE (referenced single-ended) or DIFF (differential). This property overwrites the value you configure in the Module Properties dialog box. You cannot configure channels 8 through 15 to DIFF mode. |
| Voltage Range | AI | Sets the input range for a channel as ±10 V, ±5 V, ±2 V, or ±1 V. This property overwrites the value you configure in the Module Properties dialog box. |
| LSB Weight | AO | Returns the LSB weight in nV/LSB for the channel. Use this value to convert AO data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset | AO | Returns the calibration offset in nV for the channel. Use this value to convert AO data if you set the Calibration Mode to Raw in the Module Properties dialog box. |

#### Module Properties

Use the FPGA I/O
 Property Node to access the following properties for this device.

| Property | I/O Type | Description |
| --- | --- | --- |
| LSB Weight (±10 V range) | AI | Returns the LSB weight in pV/LSB for the ±10 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| LSB Weight (±5 V range) | AI | Returns the LSB weight in pV/LSB for the ±5 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| LSB Weight (±2 V range) | AI | Returns the LSB weight in pV/LSB for the ±2 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| LSB Weight (±1 V range) | AI | Returns the LSB weight in pV/LSB for the ±1 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset (±10 V range) | AI | Returns the calibration offset in nV for the ±10 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset (±5 V range) | AI | Returns the calibration offset in nV for the ±5 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset (±2 V range) | AI | Returns the calibration offset in nV for the ±2 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |
| Offset (±1 V range) | AI | Returns the calibration offset in nV for the ±1 V range. Use this value to convert AI data if you set the Calibration Mode to Raw in the Module Properties dialog box. |

#### Single-Cycle Timed Loop

This device
 supports the single-cycle Timed Loop for digital I/O only. To configure the number
 of output synchronizing registers or input synchronizing registers for the channels
 on this device, use the Advanced Code Generation page of the
 FPGA I/O Properties dialog box

The Set
 Output Enable method node is not supported in the single-cycle Timed
 Loop. When writing to a DIO I/O node in a single-cycle Timed Loop, the I/O node will
 not change the DIO line directions. To set the line directions to output when
 writing to the DIO channels in a single-cycle Timed Loop, either configure the
 default line directions to output in the Module Properties
 dialog box, or use the Set Output Enable method node outside a
 single-cycle Timed Loop.

This device supports the Number of
 Synchronizing Registers for Output Data synchronizing register option
 when used in SCTL output. This option supports the same functionality as the
 Number of Synchronizing Registers for Output Data option
 described in the Advanced Code Generation FPGA I/O Properties Page (FPGA Module)
 topic, with the exception that you can use this option only in a single-cycle Timed
 Loop. Implement either 0 or 1 synchronizing registers inside the single-cycle Timed
 Loop. Note that if you configure 0 synchronizing registers outside of the
 single-cycle Timed Loop, the FPGA VI implements 1 synchronizing register by default.

When the device is within a single-cycle Timed Loop, it must be ready to
 perform digital I/O before a loop containing digital I/O starts. Poll the
 Ready output of the Check Status
 method to determine whether the module is ready. Digital input operations return
 invalid data if the module is not ready. The module also might ignore or delay
 digital output operations if it is not ready.

Parent topic:

sbRIO-9638

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9683.html language=enus -->
## TOPIC 00360: sbRIO-9683

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9683.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9683.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the sbRIO-9683 with only sbRIO-9605/9606/9607 devices. The sbRIO-9683 is not electrically or mechanically compatible with other NI sbRIO devices.sbRIO-9683 Pinout 181 sbRIO-9683 Pinout

### sbRIO-9683

Caution

#### sbRIO-9683 Pinout

Figure 181.

[IMAGE alt='image' src='GUID-886D487C-6D80-479F-8FB1-971971E623F8-a5.svg']

Parent topic:

RIO Mezzanine Cards

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9684-fpga-interface.html language=enus -->
## TOPIC 00361: sbRIO-9684 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9684-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9684-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use an FPGA I/O Node configured for reading and writing with this device. Use the FPGA I/O Node to access the following terminals for this device. 659 Terminals in Software Terminal Description AOx Analog output channel where x is the number of the channel. The sbRIO-9684 has AO channels 0 to 7 that

### sbRIO-9684 (FPGA Interface)

Use an FPGA I/O Node configured for reading and writing
 with this device.

Use the FPGA I/O Node to access the following terminals for this device.

| Terminal | Description |
| --- | --- |
| AOx | Analog output channel where x is the number of the channel. The sbRIO-9684 has AO channels 0 to 7 that you can add to a project. |
| Half-Bridge DOx | Half-bridge digital output channel where x is the number of the channel. The sbRIO-9684 has Half-bridge DO channels 0 to 13 that you can add to a project. |
| Half-Bridge DO13:0 | Digital port consisting of Half-bridge DO channels 0 through 13. Channel 13 is returned in the MSB, and channel 0 is returned in the LSB. |
| Half-Bridge DO7:0 | Digital port consisting of Half-bridge DO channels 0 through 7. Channel 7 is returned in the MSB, and channel 0 is returned in the LSB. |
| Half-Bridge DO13:8 | Digital port consisting of Half-bridge DO channels 8 through 13. Channel 13 is returned in the MSB, and channel 8 is returned in the LSB. |
| LVTTL DIOx | LVTTL digital input/output channel where x is the number of the channel. The sbRIO-9684 has LVTTL DIO channels 0 to 31 that you can add to a project. |
| LVTTL DIO7:0 | Digital port consisting of LVTTL DIO channels 0 through 7. Channel 7 is returned in the MSB, and channel 0 is returned in the LSB. |
| LVTTL DIO15:8 | Digital port consisting of LVTTL DIO channels 8 through 15. Channel 15 is returned in the MSB, and channel 8 is returned in the LSB. |
| LVTTL DIO23:16 | Digital port consisting of LVTTL DIO channels 16 through 23. Channel 23 is returned in the MSB, and channel 16 is returned in the LSB. |
| LVTTL DIO31:24 | Digital port consisting of LVTTL DIO channels 24 through 31. Channel 31 is returned in the MSB, and channel 24 is returned in the LSB. |
| Relay Control DOx | Relay control digital output channel where x is the number of the channel. The sbRIO-9684 has relay control DO channels 0 to 3 that you can add to a project. |
| Relay Control DO3:0 | Digital port consisting of relay control DO channels 0 through 3. Channel 3 is returned in the MSB, and channel 0 is returned in the LSB. |
| Scanned AIx | Scanned analog input channel where x is the number of the channel. The sbRIO-9684 has scanned AI channels 0 to 7 that you can add to a project. |
| Simultaneous AIx | Simultaneous analog input channel where x is the number of the channel. The sbRIO-9684 has simultaneous AI channels 0 to 15 that you can add to a project. |
| Sinking DOx | Sinking digital output channel where x is the number of the channel. The sbRIO-9684 has sinking DO channels 0 to 23 that you can add to a project. |
| Sinking DO23:0 | Digital port consisting of sinking DO channels 0 through 23. Channel 23 is returned in the MSB, and channel 0 is returned in the LSB. |
| Sinking DO7:0 | Digital port consisting of sinking DO channels 0 through 7. Channel 7 is returned in the MSB, and channel 0 is returned in the LSB. |
| Sinking DO15:8 | Digital port consisting of sinking DO channels 8 through 15. Channel 15 is returned in the MSB, and channel 8 is returned in the LSB. |
| Sinking DO23:16 | Digital port consisting of sinking DO channels 16 through 23. Channel 23 is returned in the MSB, and channel 16 is returned in the LSB. |
| Sourcing P0 DIx | Sourcing digital input channel where x is the number of the channel. The sbRIO-9684 has sourcing P0 DI channels 0 to 13 that you can add to a project. |
| Sourcing P0 DI13:0 | Digital port consisting of sourcing DI P0 channels 0 through 13. Channel 13 is returned in the MSB, and channel 0 is returned in the LSB. |
| Sourcing P0 DI7:0 | Digital port consisting of sourcing DI P0 channels 0 through 7. Channel 7 is returned in the MSB, and channel 0 is returned in the LSB. |
| Sourcing P0 DI13:8 | Digital port consisting of sourcing DI P0channels 8 through 13. Channel 13 is returned in the MSB, and channel 8 is returned in the LSB. |
| Sourcing P1 DIx | Sourcing digital input channel where x is the number of the channel. The sbRIO-9684 has sourcing P1 DI channels 0 to 13 that you can add to a project. |
| Sourcing P1 DI13:0 | Digital port consisting of sourcing DI P1 channels 0 through 13. Channel 13 is returned in the MSB, and channel 0 is returned in the LSB. |
| Sourcing P1 DI7:0 | Digital port consisting of sourcing DI P1 channels 0 through 7. Channel 7 is returned in the MSB, and channel 0 is returned in the LSB. |
| Sourcing P1 DI13:8 | Digital port consisting of sourcing DI P1 channels 8 through 13. Channel 13 is returned in the MSB, and channel 8 is returned in the LSB. |

#### Arbitration

You can configure the arbitration settings for the LVTTL DIO,
 half-bridge DO, relay control DO, and sinking DO channels of this device in the
 Advanced Code Generation page of the FPGA I/O
 Properties dialog box. The default arbitration setting is
 Never Arbitrate for the LVTTL DIO, half-bridge DO, and relay
 control DO channels. The default arbitration setting is Arbitrate if
 Multiple Requestors Only for the sinking DO channels.

#### I/O
 Methods

Use the FPGA I/O Method Node to access the following I/O methods
 for LVTTL DIO channels of this device.

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |
| Wait on Any Edge | Pauses the execution of the I/O Method Node until the next falling or rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Any Edge method waits for the next falling or rising edge. A value of 0 causes the method to time out immediately. A negative value causes the method to wait indefinitely. A positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Falling Edge | Pauses the execution of the I/O Method Node until the next falling edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Falling Edge method waits for the next falling edge. A value of 0 causes the method to time out immediately. A negative value causes the method to wait indefinitely. A positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on High Level | Pauses the execution of the I/O Method Node until the digital signal is high. The Timeout input specifies in FPGA clock ticks how long the Wait on High Level method waits for the next high level. A value of 0 causes the method to time out immediately. A negative value causes the method to wait indefinitely. A positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Low Level | Pauses the execution of the I/O Method Node until the digital signal is low. The Timeout input specifies in FPGA clock ticks how long the Wait on Low Level method waits for the next low level. A value of 0 causes the method to time out immediately. A negative value causes the method to wait indefinitely. A positive value causes the method to wait for that number of clock ticks before timing out. |
| Wait on Rising Edge | Pauses the execution of the I/O Method Node until the next rising edge of the digital signal. The Timeout input specifies in FPGA clock ticks how long the Wait on Rising Edge method waits for the next rising edge. A value of 0 causes the method to time out immediately. A negative value causes the method to wait indefinitely. A positive value causes the method to wait for that number of clock ticks before timing out. |

#### RMC
 Methods

Use the FPGA I/O Method Node to access the following RMC methods
 for this device.

| Method | Description |
| --- | --- |
| Check Status | Returns a Boolean value that indicates whether the half-bridge DO on the device is ready. |

#### I/O
 Properties

Use the FPGA I/O Property Node to access the following I/O
 properties for this device.

| Property | Description |
| --- | --- |
| LSB Weight (±10V range) | Returns the LSB weight in V/LSB for the ±10V range. |
| LSB Weight (±5V range) | Returns the LSB weight in V/LSB for the ±5V range. |
| Offset (±10V range) | Returns the calibration offset in V for the ±10V range. |
| Offset (±5V range) | Returns the calibration offset in V for the ±5V range. |
| Voltage Range | Returns the input range for a simultaneous analog input bank. |

#### RMC
 Properties

Use the FPGA I/O Property Node to access the following RMC
 properties for this device.

| Property | Description |
| --- | --- |
| Voltage Range Simultaneous AIx:x | Sets the input range for a simultaneous analog input bank as either ±5 V or ±10 V where x:x is the bank. This method overwrites the value that is configured in the RIO Mezzanine Card Properties dialog box. |

#### Single-Cycle Timed Loop

This device supports the single-cycle Timed
 Loop. Configure the number of output synchronizing registers for the high-speed DO
 channels of this device in the Advanced Code Generation page of the
 FPGA I/O Properties dialog box.

Parent topic:

sbRIO-9684

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9684.html language=enus -->
## TOPIC 00362: sbRIO-9684

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9684.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9684.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the sbRIO-9684 with only NI sbRIO-9603/9605/9606/9607 devices. The sbRIO-9684 is not electrically or mechanically compatible with other NI sbRIO devices.sbRIO-9684 Pinout 182 sbRIO-9684 Pinout

### sbRIO-9684

Caution

#### sbRIO-9684 Pinout

Figure 182.

[IMAGE alt='image' src='GUID-886D487C-6D80-479F-8FB1-971971E623F8-a5.svg']

Parent topic:

RIO Mezzanine Cards

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9694-fpga-interface.html language=enus -->
## TOPIC 00363: sbRIO-9694 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9694-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9694-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use an FPGA I/O Node configured for reading and writing with this device. 669 Terminals in Software Terminal Description DIOx Digital input/output channel where x is the number of the channel. The sbRIO-9694 has DIO channels 0 to 95 that you can add to a project. DIO15:0 Digital port consisting of D

### sbRIO-9694 (FPGA Interface)

Use an FPGA I/O Node configured for reading and writing
 with this device.

| Terminal | Description |
| --- | --- |
| DIOx | Digital input/output channel where x is the number of the channel. The sbRIO-9694 has DIO channels 0 to 95 that you can add to a project. |
| DIO15:0 | Digital port consisting of DIO channels 0 through 15. Channel 15 is returned in the MSB, and channel 0 is returned in the LSB. |
| DIO31:16 | Digital port consisting of DIO channels 16 through 31. Channel 31 is returned in the MSB, and channel 16 is returned in the LSB. |
| DIO47:32 | Digital port consisting of DIO channels 32 through 47. Channel 47 is returned in the MSB, and channel 32 is returned in the LSB. |
| DIO63:48 | Digital port consisting of DIO channels 48 through 63. Channel 63 is returned in the MSB, and channel 48 is returned in the LSB. |
| DIO79:64 | Digital port consisting of DIO channels 64 through 79. Channel 79 is returned in the MSB, and channel 64 is returned in the LSB. |
| DIO95:80 | Digital port consisting of DIO channels 80 through 95. Channel 95 is returned in the MSB, and channel 80 is returned in the LSB. |

#### Arbitration

You can configure the arbitration settings for the DO
 channels of this device in the Advanced Code Generation page of the
 FPGA I/O Properties dialog box. The default arbitration
 setting is Never Arbitrate.

#### I/O
 Methods

Use the FPGA I/O Method Node to access the following I/O methods
 for LVTTL DIO channels of this device.

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |

#### Module Methods

This device does not
 support any module methods.

#### Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the single-cycle Timed
 Loop. Configure the number of output synchronizing registers for the channels of
 this device in the Advanced Code Generation page of the
 FPGA I/O Properties dialog box. Configure the number of
 input synchronizing registers for the channels of this device in the
 Advanced Code Generation page of the FPGA I/O
 Properties dialog box.

Parent topic:

sbRIO-9694

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9694.html language=enus -->
## TOPIC 00364: sbRIO-9694

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9694.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9694.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: sbRIO-9694 Pinout 183 sbRIO-9694 Pinout

### sbRIO-9694

#### sbRIO-9694 Pinout

Figure 183.

[IMAGE alt='image' src='GUID-086A7094-AC3B-4201-9D0B-27F68E043CC9-a5.svg']

Parent topic:

RIO Mezzanine Cards

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9697-fpga-interface.html language=enus -->
## TOPIC 00365: sbRIO-9697 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9697-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9697-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use an FPGA I/O Node configured for reading and writing with this device. 671 Terminals in Software Terminal Description DIOx Digital input/output channel where x is the number of the channel. The sbRIO-9697 has DIO channels 0 to 23 that you can add to a project. DIO15:0 Digital port consisting of D

### sbRIO-9697 (FPGA Interface)

Use an FPGA I/O Node configured for reading and writing
 with this device.

| Terminal | Description |
| --- | --- |
| DIOx | Digital input/output channel where x is the number of the channel. The sbRIO-9697 has DIO channels 0 to 23 that you can add to a project. |
| DIO15:0 | Digital port consisting of DIO channels 0 through 15. Channel 15 is returned in the MSB, and channel 0 is returned in the LSB. |
| DIO23:16 | Digital port consisting of DIO channels 16 through 23. Channel 23 is returned in the MSB, and channel 16 is returned in the LSB. |

#### Arbitration

You can configure the arbitration settings for the DO
 channels of this device in the Advanced Code Generation page of the
 FPGA I/O Properties dialog box. The default arbitration
 setting is Never Arbitrate.

#### I/O
 Methods

Use the FPGA I/O Method Node to access the following I/O methods
 for LVTTL DIO channels of this device.

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |

#### Module Methods

This device does not
 support any module methods.

#### Properties

This device does not support any properties.

#### Single-Cycle Timed Loop

This device supports the single-cycle Timed
 Loop. Configure the number of output synchronizing registers for the channels of
 this device in the Advanced Code Generation page of the
 FPGA I/O Properties dialog box. Configure the number of
 input synchronizing registers for the channels of this device in the
 Advanced Code Generation page of the FPGA I/O
 Properties dialog box.

Parent topic:

sbRIO-9697

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9697.html language=enus -->
## TOPIC 00366: sbRIO-9697

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9697.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9697.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the sbRIO-9697 with only sbRIO-9607/9627 devices.sbRIO-9697 Pinout 184 sbRIO-9697 Pinout

### sbRIO-9697

Note

#### sbRIO-9697 Pinout

Figure 184.

[IMAGE alt='image' src='GUID-FE5FAFDE-B683-4B27-BCA0-C20CAE667111-a5.svg']

Parent topic:

RIO Mezzanine Cards

<!--NI_TOPIC bundle=ni-compactrio path=sbrio-9698-fpga-interface.html language=enus -->
## TOPIC 00367: sbRIO-9698 (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `sbrio-9698-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sbrio-9698-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use an FPGA I/O Node configured for reading and writing with this device. 673 Terminals in Software Terminal Description DIOx Digital input/output channel where x is the number of the channel. The sbRIO-9698 has DIO channels 0 to 23 that you can add to a project. DIO15:0 Digital port consisting of D

### sbRIO-9698 (FPGA Interface)

Use an FPGA I/O Node configured for reading and writing
 with this device.

| Terminal | Description |
| --- | --- |
| DIOx | Digital input/output channel where x is the number of the channel. The sbRIO-9698 has DIO channels 0 to 23 that you can add to a project. |
| DIO15:0 | Digital port consisting of DIO channels 0 through 15. Channel 15 is returned in the MSB, and channel 0 is returned in the LSB. |
| DIO23:16 | Digital port consisting of DIO channels 16 through 23. Channel 23 is returned in the MSB, and channel 16 is returned in the LSB. |

#### Arbitration

You can configure the
 arbitration settings for the DO channels of this device in the Advanced Code
 Generation page of the FPGA I/O Properties dialog
 box. The default arbitration setting is Never
 Arbitrate.

#### I/O Methods

Use the FPGA I/O Method Node
 to access the following I/O methods for LVTTL DIO channels of this device.

| Method | Description |
| --- | --- |
| Set Output Data | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |
| Set Output Enable | Refer to the FPGA I/O Method Node topic in the LabVIEW FPGA Module Programming Reference Manual for a description of this method. |

#### Module Methods

This device does not
 support any module methods.

#### Properties

This device does not support
 any properties.

#### Single-Cycle Timed Loop

This device
 supports the single-cycle Timed Loop. Configure the number of output synchronizing
 registers for the channels of this device in the Advanced Code
 Generation page of the FPGA I/O Properties dialog
 box. Configure the number of input synchronizing registers for the channels of this
 device in the Advanced Code Generation page of the FPGA
 I/O Properties dialog box.

Parent topic:

sbRIO-9698

<!--NI_TOPIC bundle=ni-compactrio path=set-voltage-range-method-fpga-interface.html language=enus -->
## TOPIC 00368: Set Voltage Range Method (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `set-voltage-range-method-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/set-voltage-range-method-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This module method overrides the default setting provided in the C Series Module Properties dialog box. To use this module method, select it in an FPGA I/O Method Node that is configured for the appropriate device and/or channel. AI Channel is the channel you want to set the voltage range for. Volta

### Set Voltage Range Method (FPGA Interface)

This module method overrides the default setting provided in the *C Series Module
 Properties* dialog box. To use this module method, select it in an
 FPGA I/O Method Node that is configured for the appropriate
 device and/or channel.

|  | AI Channel is the channel you want to set the voltage range for. |
| --- | --- |
|  | Voltage Range is an enumeration of the following voltage ranges: ±10 V ±5 V ±1 V ±200 mV |

|  | error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE if an error occurred. If status is TRUE, the VI does not perform any operations. code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source always contains an empty string because strings are not supported in LabVIEW FPGA. |
| --- | --- |
|  | status is TRUE if an error occurred. If status is TRUE, the VI does not perform any operations. |
|  | code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source always contains an empty string because strings are not supported in LabVIEW FPGA. |

|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE if an error occurred. If status is TRUE, the VI does not perform any operations. code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source always contains an empty string because strings are not supported in LabVIEW FPGA. |
| --- | --- |
|  | status is TRUE if an error occurred. If status is TRUE, the VI does not perform any operations. |
|  | code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source always contains an empty string because strings are not supported in LabVIEW FPGA. |

Parent topic:

NI 9204 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=set-voltage-range-method-fpga-interface_2.html language=enus -->
## TOPIC 00369: Set Voltage Range Method (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `set-voltage-range-method-fpga-interface_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/set-voltage-range-method-fpga-interface_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This module method overrides the default setting provided in the C Series Module Properties dialog box. To use this module method, select it in an FPGA I/O Method Node that is configured for the appropriate device and/or channel. AI Channel is the channel you want to set the voltage range for. Volta

### Set Voltage Range Method (FPGA Interface)

This module method overrides the default setting provided in the *C Series Module
 Properties* dialog box. To use this module method, select it in an
 FPGA I/O Method Node that is configured for the appropriate
 device and/or channel.

|  | AI Channel is the channel you want to set the voltage range for. |
| --- | --- |
|  | Voltage Range is an enumeration of the following voltage ranges: ±10 V ±5 V ±1 V ±200 mV |

|  | error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE if an error occurred. If status is TRUE, the VI does not perform any operations. code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source always contains an empty string because strings are not supported in LabVIEW FPGA. |
| --- | --- |
|  | status is TRUE if an error occurred. If status is TRUE, the VI does not perform any operations. |
|  | code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source always contains an empty string because strings are not supported in LabVIEW FPGA. |

|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE if an error occurred. If status is TRUE, the VI does not perform any operations. code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source always contains an empty string because strings are not supported in LabVIEW FPGA. |
| --- | --- |
|  | status is TRUE if an error occurred. If status is TRUE, the VI does not perform any operations. |
|  | code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source always contains an empty string because strings are not supported in LabVIEW FPGA. |

Parent topic:

NI 9205 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=set-voltage-range-method-fpga-interface_3.html language=enus -->
## TOPIC 00370: Set Voltage Range Method (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `set-voltage-range-method-fpga-interface_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/set-voltage-range-method-fpga-interface_3.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: This module method overrides the default setting provided in the C Series Module Properties dialog box. To use this module method, select it in an FPGA I/O Method Node that is configured for the appropriate device and/or channel. AI Channel is the channel you want to set the voltage range for. Volta

### Set Voltage Range Method (FPGA Interface)

This module method overrides the default setting provided in the *C Series Module
 Properties* dialog box. To use this module method, select it in an
 FPGA I/O Method Node that is configured for the appropriate
 device and/or channel.

|  | AI Channel is the channel you want to set the voltage range for. |
| --- | --- |
|  | Voltage Range is an enumeration of the following voltage ranges: ±10 V ±5 V ±1 V ±200 mV |

|  | error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE if an error occurred. If status is TRUE, the VI does not perform any operations. code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source always contains an empty string because strings are not supported in LabVIEW FPGA. |
| --- | --- |
|  | status is TRUE if an error occurred. If status is TRUE, the VI does not perform any operations. |
|  | code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source always contains an empty string because strings are not supported in LabVIEW FPGA. |

|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE if an error occurred. If status is TRUE, the VI does not perform any operations. code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source always contains an empty string because strings are not supported in LabVIEW FPGA. |
| --- | --- |
|  | status is TRUE if an error occurred. If status is TRUE, the VI does not perform any operations. |
|  | code is the error code number identifying an error. The default is 0. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source always contains an empty string because strings are not supported in LabVIEW FPGA. |

Parent topic:

NI 9206 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=simultaneously-reading-from-or-writing-to-mul.html language=enus -->
## TOPIC 00371: Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `simultaneously-reading-from-or-writing-to-mul.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/simultaneously-reading-from-or-writing-to-mul.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure a single FPGA I/O Node with the channels you want to simultaneously sample or update. If you configure a single FPGA I/O Node with channels from different modules, FPGA I/O execution begins at the same time for all the modules, but the actual sampling or update times may differ in the foll

### Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface)

Configure a single FPGA I/O Node with the channels you want to
 simultaneously sample or update.

- Between modules depending on the types of modules
- The number of channels used on each module
- The arbitration settings
- Idle state when the I/O Node begins execution

If you configure an FPGA I/O Node with multiple channels on a non-simultaneous module,
 the function accesses the channels sequentially.

The following table lists the C Series modules that
 support simultaneously reading from or writing to multiple CompactRIO channels.

| C Series Module | Description |
| --- | --- |
| NI 9215 | ±10 V, 100 kS/s/ch, 16-Bit, Simultaneous Input, 4-Channel C Series Voltage Input Module |
| NI 9220 | 16-Channel, ±10 V, 100 kS/s/ch, 16-Bit Simultaneous Analog Input Module |
| NI 9222 | ±10 V, 100 kS/s/ch, 16-Bit, Simultaneous Input, 4-Channel C Series Voltage Input Module |
| NI 9223 | ±10 V, 1 MS/s, 16-Bit, Simultaneous Input, 4-Channel C Series Voltage Input Module |
| NI 9225 | 300 Vrms, 50 kS/s/ch, 24-Bit, Simultaneous Input, 3-Channel C Series Voltage Input Module |
| NI 9227 | 50 kS/s/ch, 5 Arms, 24-Bit, 4-Channel C Series Current Input Module |
| NI 9229 | ±60 V, 50 kS/s/ch, 24-Bit, Simultaneous Input, 4-Channel C Series Voltage Module |
| NI 9239 | ±10 V, 50 kS/s/ch, 24-Bit, Simultaneous Input, 4-Channel C Series Voltage Input Module |
| NI 9263 | 100 kS/s/ch Simultaneous, ±10 V, 4-Channel C Series Voltage Output Module |
| NI 9264 | 25 kS/s/ch Simultaneous, ±10 V, 16-Channel C Series Voltage Output Module |
| NI 9265 | 4-Channel C Series Current Output Module |
| NI 9269 | 100 kS/s/ch Simultaneous, ±10 V, Isolated, 4-Channel C Series Voltage Output Module |
| NI 9320 | 16-Channel, ±10 V, 200 kS/s/ch, 16-Bit Simultaneous Analog Input Module |

Parent topic:

Building and Troubleshooting a CompactRIO Embedded Application

<!--NI_TOPIC bundle=ni-compactrio path=single-board-rio-device-reference.html language=enus -->
## TOPIC 00372: Single-Board RIO (sbRIO) Device Reference

- bundle_id: `ni-compactrio`
- source_path: `single-board-rio-device-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/single-board-rio-device-reference.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Single-Board RIO (sbRIO) devices and RIO Mezzanine cards with NI CompactRIO Device Drivers in LabVIEW. 598 Single-Board RIO Devices sbRIO Device Description sbRIO-9603 Single-Board Reconfigurable I/O (DIO), 1 RS-232 Serial port, 1 CAN port, Artix-7 75T FPGA sbRIO-9607 Single-Board Reconfigurable

### Single-Board RIO (sbRIO) Device
 Reference

Use Single-Board RIO (sbRIO) devices and RIO Mezzanine cards with NI CompactRIO Device
 Drivers in LabVIEW.

| sbRIO Device | Description |
| --- | --- |
| sbRIO-9603 | Single-Board Reconfigurable I/O (DIO), 1 RS-232 Serial port, 1 CAN port, Artix-7 75T FPGA |
| sbRIO-9607 | Single-Board Reconfigurable I/O (DIO), 1 RS-232 Serial port, 1 CAN port, Zynq-7020 FPGA |
| sbRIO-9608 | Single-Board Reconfigurable I/O (DIO), 1 RS-232 Serial port, 1 CAN port, Artix-7 200T FPGA |
| sbRIO-9609 | Single-Board Reconfigurable I/O (DIO), 1 RS-232 Serial port, 1 CAN port, Artix-7 200T FPGA |
| sbRIO-9627 | Single-Board Reconfigurable I/O (MIO), 16 AI channels, 4 AO channels, 4 3.3 V DIO channels, 2 RS-232 Serial ports, 1 RS-485 Serial port, 1 CAN port, RIO mezzanine card connector, Zynq-7020 FPGA |
| sbRIO-9628 | Single-Board Reconfigurable I/O (MIO and DIO), 16 AI channels, 4 AO channels, 4 5 V DIO channels, 2 RS-232 Serial ports, 1 RS-485 Serial port, 1 CAN port, RIO mezzanine card connector, Artix-7 100T FPGA |
| sbRIO-9629 | Single-Board Reconfigurable I/O (MIO and DIO), 16 AI channels, 4 AO channels, 4 5 V DIO channels, 2 RS-232 Serial ports, 1 RS-485 Serial port, 1 CAN port, RIO mezzanine card connector, Artix-7 200T FPGA |
| sbRIO-9637 | Single-Board Reconfigurable I/O (MIO and DIO), 16 AI channels, 4 AO channels, 28 3.3 V DIO channels, 2 RS-232 Serial ports, 1 RS-485 Serial port, 1 CAN port, Zynq-7020 FPGA |
| sbRIO-9638 | Single-Board Reconfigurable I/O (MIO), 16 AI channels, 4 AO channels, 28 5 V DIO channels, 2 RS-232 Serial ports, 1 RS-485 Serial port, 1 CAN port, Artix-7 100T FPGA |
| sbRIO-9651 SOM | Embedded System on Module (SOM) with Real-Time Processor and Reconfigurable FPGA, 160 configurable DIO channels, 85,000 logic cells |

| RIO Mezzanine Card | Description |
| --- | --- |
| sbRIO-9683 | RIO Mezzanine Card, General Purpose Inverter Controller |
| sbRIO-9684 | RIO Mezzanine Card, 16-bit General Purpose Inverter Controller |
| sbRIO-9694 | RIO Mezzanine Card, 96 channel digital I/O breakout board |
| sbRIO-9697 | RIO Mezzanine Card, 2-slot C Series, 24 3.3 V DIO channels |
| sbRIO-9698 | RIO Mezzanine Card, 1-Slot C Series, Secondary Ethernet Port, 24 3.3 V DIO channels |
| NI Digital I/O Mezzanine Card | 96 DIO channels |

- [Single-Board RIO Devices](single-board-rio.html)
- [RIO Mezzanine Cards](rio-mezzanine-cards.html)
- [NI Single-Board RIO CLIP Generator](ni-single-board-rio-clip-generator-help.html)

Related concepts:

- Single-Board RIO System

<!--NI_TOPIC bundle=ni-compactrio path=single-board-rio.html language=enus -->
## TOPIC 00373: Single-Board RIO Devices

- bundle_id: `ni-compactrio`
- source_path: `single-board-rio.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/single-board-rio.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 600 Single-Board RIO Devices sbRIO Device Description sbRIO-9603 Single-Board Reconfigurable I/O (DIO), 1 RS-232 Serial port, 1 CAN port, Artix-7 75T FPGA sbRIO-9607 Single-Board Reconfigurable I/O (DIO), 1 RS-232 Serial port, 1 CAN port, Zynq-7020 FPGA sbRIO-9608 Single-Board Reconfigurable I/O (DI

### Single-Board RIO Devices

| sbRIO Device | Description |
| --- | --- |
| sbRIO-9603 | Single-Board Reconfigurable I/O (DIO), 1 RS-232 Serial port, 1 CAN port, Artix-7 75T FPGA |
| sbRIO-9607 | Single-Board Reconfigurable I/O (DIO), 1 RS-232 Serial port, 1 CAN port, Zynq-7020 FPGA |
| sbRIO-9608 | Single-Board Reconfigurable I/O (DIO), 1 RS-232 Serial port, 1 CAN port, Artix-7 200T FPGA |
| sbRIO-9609 | Single-Board Reconfigurable I/O (DIO), 1 RS-232 Serial port, 1 CAN port, Artix-7 200T FPGA |
| sbRIO-9627 | Single-Board Reconfigurable I/O (MIO), 16 AI channels, 4 AO channels, 4 3.3 V DIO channels, 2 RS-232 Serial ports, 1 RS-485 Serial port, 1 CAN port, RIO mezzanine card connector, Zynq-7020 FPGA |
| sbRIO-9628 | Single-Board Reconfigurable I/O (MIO and DIO), 16 AI channels, 4 AO channels, 4 5 V DIO channels, 2 RS-232 Serial ports, 1 RS-485 Serial port, 1 CAN port, RIO mezzanine card connector, Artix-7 100T FPGA |
| sbRIO-9629 | Single-Board Reconfigurable I/O (MIO and DIO), 16 AI channels, 4 AO channels, 4 5 V DIO channels, 2 RS-232 Serial ports, 1 RS-485 Serial port, 1 CAN port, RIO mezzanine card connector, Artix-7 200T FPGA |
| sbRIO-9637 | Single-Board Reconfigurable I/O (MIO and DIO), 16 AI channels, 4 AO channels, 28 3.3 V DIO channels, 2 RS-232 Serial ports, 1 RS-485 Serial port, 1 CAN port, Zynq-7020 FPGA |
| sbRIO-9638 | Single-Board Reconfigurable I/O (MIO), 16 AI channels, 4 AO channels, 28 5 V DIO channels, 2 RS-232 Serial ports, 1 RS-485 Serial port, 1 CAN port, Artix-7 100T FPGA |
| sbRIO-9651 SOM | Embedded System on Module (SOM) with Real-Time Processor and Reconfigurable FPGA, 160 configurable DIO channels, 85,000 logic cells |

Parent topic:

Single-Board RIO (sbRIO) Device Reference

<!--NI_TOPIC bundle=ni-compactrio path=single-shot-transmit.html language=enus -->
## TOPIC 00374: Single Shot Transmit

- bundle_id: `ni-compactrio`
- source_path: `single-shot-transmit.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/single-shot-transmit.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 553 Single Shot Transmit PropertyData typePermissionsRead While Stopped? Read While Running?Write While Stopped?Write While Running?WriteNo NoYesYesThis property specifies whether to retry failed CAN frame transmissions. FALSE indicates standard CAN behavior. Failed CAN frame transmissions are autom

### Single Shot Transmit

| Data type | Permissions | Read While Stopped? | Read While Running? | Write While Stopped? | Write While Running? |
| --- | --- | --- | --- | --- | --- |
|  | Write | No | No | Yes | Yes |

This property specifies whether to retry failed CAN frame transmissions.

- FALSE indicates standard CAN behavior. Failed CAN frame
 transmissions are automatically retried (default).
- TRUE indicates single-shot. With single-shot enabled, if a CAN
 frame is not transmitted successfully, the CAN controller does not retry.

Parent topic:

I/O Properties for CAN Modules

<!--NI_TOPIC bundle=ni-compactrio path=single-shot-transmit_2.html language=enus -->
## TOPIC 00375: Single Shot Transmit

- bundle_id: `ni-compactrio`
- source_path: `single-shot-transmit_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/single-shot-transmit_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 626 Single Shot Transmit PropertyData typePermissionsRead While Stopped? Read While Running?Write While Stopped?Write While Running?WriteNo NoYesYesThis property specifies whether to retry failed CAN frame transmissions. FALSE indicates standard CAN behavior. Failed CAN frame transmissions are autom

### Single Shot Transmit

| Data type | Permissions | Read While Stopped? | Read While Running? | Write While Stopped? | Write While Running? |
| --- | --- | --- | --- | --- | --- |
|  | Write | No | No | Yes | Yes |

This property specifies whether to retry failed CAN frame transmissions.

- FALSE indicates standard CAN behavior. Failed CAN frame
 transmissions are automatically retried (default).
- TRUE indicates single-shot. With single-shot enabled, if a CAN
 frame is not transmitted successfully, the CAN controller does not retry.

Parent topic:

I/O Properties

<!--NI_TOPIC bundle=ni-compactrio path=sja1000-filter-code.html language=enus -->
## TOPIC 00376: SJA1000 Filter Code

- bundle_id: `ni-compactrio`
- source_path: `sja1000-filter-code.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sja1000-filter-code.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 554 SJA1000 Filter Code PropertyData typePermissionsWrite while stopped?Write while running?WriteYesNoThis property controls the SJA1000 Acceptance Code registers (ACR0 to ACR3). The least significant byte of the property is stored in register offset 3 (ACR3), the next least significant in offset 2

### SJA1000 Filter Code

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | No |

This property controls the SJA1000 Acceptance Code registers (ACR0 to ACR3). The least significant byte of the property is stored in register offset 3 (ACR3), the next least significant in offset 2 (ACR2), and so on.

- The default value comes from the CAN Advanced Port Configuration.
- The mask for the SJA1000 filter is specified using the SJA1000 Filter
 Mask property.
- The filter mode is specified using the SJA1000 Filter Mode 
 property.

For information on the SJA1000 acceptance filter registers (PeliCAN mode), refer to the datasheet
 of the Philips SJA1000 standalone CAN controller. This document is available for
 download on www.nxp.com.

Parent topic:

I/O Properties for CAN Modules

<!--NI_TOPIC bundle=ni-compactrio path=sja1000-filter-mask.html language=enus -->
## TOPIC 00377: SJA1000 Filter Mask

- bundle_id: `ni-compactrio`
- source_path: `sja1000-filter-mask.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sja1000-filter-mask.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 555 SJA1000 Filter Mask PropertyData typePermissionsWrite while stopped?Write while running?WriteYesNoThis property controls the SJA1000 Acceptance Mask registers (AMR0 to AMR3). The least significant byte of the property is stored in register offset 3 (AMR3), the next least significant in offset 2

### SJA1000 Filter Mask

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | No |

This property controls the SJA1000 Acceptance Mask registers (AMR0 to AMR3). The least significant byte of the property is stored in register offset 3 (AMR3), the next least significant in offset 2 (AMR2), and so on.

- The default value comes from the CAN Advanced Port Configuration.
- The code for the SJA1000 filter is specified using the SJA1000 Filter
 Code property.
- The filter mode is specified using the SJA1000 Filter Mode property.

For information on the SJA1000 acceptance filter registers (PeliCAN mode), refer to the
 datasheet of the Philips SJA1000 standalone CAN controller. This document is available
 for download on www.nxp.com.

Parent topic:

I/O Properties for CAN Modules

<!--NI_TOPIC bundle=ni-compactrio path=sja1000-filter-mode.html language=enus -->
## TOPIC 00378: SJA1000 Filter Mode

- bundle_id: `ni-compactrio`
- source_path: `sja1000-filter-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/sja1000-filter-mode.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 556 SJA1000 Filter Mode PropertyData typePermissionsWrite while stopped?Write while running?WriteYesNoThis property controls the SJA1000 Acceptance Mode register. Dual (0) specifies use of two filters. Single (1) specifies use of a single filter. The default value comes from the CAN Advanced Port Co

### SJA1000 Filter Mode

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Write | Yes | No |

This property controls the SJA1000 Acceptance Mode register. Dual (0) specifies use of two
 filters. Single (1) specifies use of a single filter.

- The default value comes from the CAN Advanced Port Configuration.
- The code and mask for the SJA1000 filter is specified using the SJA1000 Filter
 Code property.

For information on the SJA1000 acceptance filter registers (PeliCAN mode), refer to the
 datasheet of the Philips SJA1000 standalone CAN controller. This document is available
 for download on www.nxp.com.

Parent topic:

I/O Properties for CAN Modules

<!--NI_TOPIC bundle=ni-compactrio path=specialty-digital-functions.html language=enus -->
## TOPIC 00379: Configuring Specialty Digital Functions

- bundle_id: `ni-compactrio`
- source_path: `specialty-digital-functions.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/specialty-digital-functions.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure some C Series digital input and output modules for specialty digital functions, including: counter input counter-driven output pulse-width modulation output quadrature input Two methods are available to configure specialty digital functions on C Series DIO modules: Configure specia

### Configuring Specialty Digital
 Functions

C Series

- counter input
- counter-driven output
- pulse-width modulation output
- quadrature input

C Series

- Configure specialty digital functions with the Specialty Digital
 Configuration page of the C Series Module
 Properties dialog box.
- Configure specialty digital functions by wiring a reference to a specialty
 digital module to a generic-class property node in a VI block diagram.

Witing a reference specifies the class of the property node as SD Module and
 provides programmatic access to all the specialty digital functions that the module
 supports.

To configure specialty digital functions for one or two modules, program the chassis for
 Scan Interface mode. To configure more than two modules for
 specialty digital functions, program the chassis to use FPGA
 Interface mode.

The maximum update rate for modules configured for specialty digital functions is approximately
 4 MHz.

Parent topic:

Configuring Devices

Related concepts:

- Using the Scan Interface with Individual Modules

<!--NI_TOPIC bundle=ni-compactrio path=start.html language=enus -->
## TOPIC 00380: Start

- bundle_id: `ni-compactrio`
- source_path: `start.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/start.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Start communication.Cases for using this method, as opposed to enabling Auto Start in Module Configuration: Change configuration properties within the diagram (such as the Listen Only property) Auto-baud algorithms (must Stop/Start to set the baud rate for each attempt) Start CAN communication on a

### Start

Start communication.

Cases for using this method, as opposed to enabling Auto Start in Module
 Configuration:

- Change configuration properties within the diagram (such as the Listen Only property)
- Auto-baud algorithms (must Stop/Start to set the baud rate for each attempt)
- Start CAN communication on a trigger (analog or digital input)

#### Node
 Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error Terminals

#### Node
 Outputs

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error Terminals

Parent topic:

I/O Methods for CAN Modules

Related concepts:

- Error Terminals
- Module Configuration

<!--NI_TOPIC bundle=ni-compactrio path=start_2.html language=enus -->
## TOPIC 00381: Start

- bundle_id: `ni-compactrio`
- source_path: `start_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/start_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Start communication.Cases for using this method, as opposed to enabling Auto Start in Module Configuration: Change configuration properties within the diagram (such as the Listen Only property) Auto-baud algorithms (must Stop/Start to set the baud rate for each attempt) Start CAN communication on a

### Start

Start communication.

Cases for using this method, as opposed to enabling Auto Start in Module
 Configuration:

- Change configuration properties within the diagram (such as the Listen Only property)
- Auto-baud algorithms (must Stop/Start to set the baud rate for each attempt)
- Start CAN communication on a trigger (analog or digital input)

#### Node
 Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error Terminals

#### Node
 Outputs

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error Terminals

Parent topic:

I/O Methods for sbRIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=stop.html language=enus -->
## TOPIC 00382: Stop

- bundle_id: `ni-compactrio`
- source_path: `stop.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/stop.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Stop communication. This method also clears the output FIFO as well as any pending CAN node (including all Wait methods). Node Inputs Error In Optional. Not shown by default. Right-click the node and select Error Terminals to enable. Node Outputs Error Out Optional. Not shown by default. Right-click

### Stop

Stop communication.

This method also clears the output FIFO as well as any pending CAN node (including all
 Wait methods).

#### Node
 Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error Terminals

#### Node
 Outputs

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error Terminals

Parent topic:

I/O Methods for CAN Modules

Related concepts:

- Error Terminals

<!--NI_TOPIC bundle=ni-compactrio path=stop_2.html language=enus -->
## TOPIC 00383: Stop

- bundle_id: `ni-compactrio`
- source_path: `stop_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/stop_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Stop communication. This method also clears the output FIFO as well as any pending CAN node (including all Wait methods). Node Inputs Error In Optional. Not shown by default. Right-click the node and select Error Terminals to enable. Node Outputs Error Out Optional. Not shown by default. Right-click

### Stop

Stop communication.

This method also clears the output FIFO as well as any pending CAN node (including all
 Wait methods).

#### Node
 Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error Terminals

#### Node
 Outputs

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error Terminals

Parent topic:

I/O Methods for sbRIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=supporting-external-data-value-references.html language=enus -->
## TOPIC 00384: Supporting External Data Value References

- bundle_id: `ni-compactrio`
- source_path: `supporting-external-data-value-references.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/supporting-external-data-value-references.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following NI CompactRIO Device Drivers FPGA targets support using an external data value reference to implement DMA FIFOs without a data copy and while making better use of memory resources: cRIO-9030 cRIO-9031 cRIO-9033 cRIO-9034 cRIO-9038 cRIO-9066 cRIO-9067 cRIO-9068 NI 9149 sbRIO-9651 SOM my

### Supporting External Data Value References

The following NI CompactRIO Device Drivers FPGA targets support using an external data value reference to implement DMA FIFOs without a data copy and while making better use of memory resources:

- cRIO-9030
- cRIO-9031
- cRIO-9033
- cRIO-9034
- cRIO-9038
- cRIO-9066
- cRIO-9067
- cRIO-9068
- NI 9149
- sbRIO-9651 SOM
- myRIO-1900
- myRIO-1950
- roboRIO

Parent topic:

Building and Troubleshooting a CompactRIO Embedded Application

<!--NI_TOPIC bundle=ni-compactrio path=synchronizing-fpga-vis-with-the-ni-scan-engin.html language=enus -->
## TOPIC 00385: Synchronizing FPGA VIs with the NI Scan Engine (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `synchronizing-fpga-vis-with-the-ni-scan-engin.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/synchronizing-fpga-vis-with-the-ni-scan-engin.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The CompactRIO reconfigurable embedded chassis, integrated controllers and chassis, Ethernet RIO chassis, and Single-Board RIO (sbRIO) devices have a Scan Clock I/O item. Use the Scan Clock item to monitor when the NI Scan Engine transfers data between the FPGA VI and the RT host VI. Use the Scan Cl

### Synchronizing FPGA VIs with the NI Scan Engine (FPGA Interface)

The CompactRIO reconfigurable embedded chassis, integrated controllers and chassis, Ethernet
 RIO chassis, and Single-Board RIO (sbRIO) devices have a Scan Clock I/O item. Use the
 Scan Clock item to monitor when the NI Scan Engine transfers data between the FPGA VI
 and the RT host VI.

Use the Scan Clock information with user-defined I/O variables to synchronize data
 transfers with the NI Scan Engine. Synchronizing user-defined I/O variable data
 transfers with the Scan Engine ensures the coherency of the data sets you transfer
 between the FPGA VI and the RT host VI.

NI recommends you design the application so that read/write operations occur when the
 Scan Engine is not transferring data between the FPGA VI and the RT host VI. If you read
 from or write to user-defined I/O variables while the Scan Engine is transferring data,
 the Scan Engine cannot guarantee data coherency, and the data transfer gets delayed to
 the next opportunity.

The following image illustrates how the Scan Engine reacts when you read from or write to
 user-defined I/O variables during the Scan Engine high time and when a user-defined I/O
 variable read or write operation misses the falling edge of the Scan Engine.

Figure 2.

[IMAGE alt='Scan Engine Reactions to User-Defined I/O Variable Read/Write Operations' src='GUID-28F809FE-F9F9-4D72-83BE-FDD7AE69371E-a5.svg']

You can also use the Scan Clock information to synchronize the execution of code in the FPGA VI with code in the RT host VI that is synchronized to the Scan Engine.

Use the following Scan Clock I/O item, method, and properties to monitor information from the
 Scan Engine.

#### Scan Clock I/O Item

Use the FPGA I/O Node
 to access the Scan Clock I/O item.

To access the Scan Clock I/O item, drag
 the Scan Clock I/O item from the Chassis I/O folder in the
 project to the block diagram of the FPGA VI. You can also place an FPGA I/O Node on
 the block diagram, click the element section of the FPGA I/O Node, and select
 Chassis I/O»Scan Clock from the shortcut menu.

[IMAGE alt='image' src='GUID-57CBA91C-5B3A-42CC-8079-75BA5B02286E-a5.svg']

Scan Clock

Scan Clock

#### Scan Clock Method: Wait on
 Rising Edge

Use the FPGA I/O Method Node to access the
 Wait on Rising Edge method for the Scan Clock I/O
 item.

The Wait on Rising Edge method pauses the
 execution of the FPGA I/O Method Node until the next rising edge of the Scan Clock
 signal or until the Timeout expires.

[IMAGE alt='image' src='GUID-C23371C7-9839-4697-89F2-D0A635332E12-a5.svg']

Timeout

[IMAGE alt='image' src='GUID-57CBA91C-5B3A-42CC-8079-75BA5B02286E-a5.svg']

Timed Out

[IMAGE alt='image' src='GUID-57CBA91C-5B3A-42CC-8079-75BA5B02286E-a5.svg']

Missed Falling Edge

Missed Falling
 Edge

Missed Falling Edge

Missed
 Rising Edge

[IMAGE alt='image' src='GUID-57CBA91C-5B3A-42CC-8079-75BA5B02286E-a5.svg']

Missed Rising Edge

Missed Rising
 Edge

Missed Falling Edge

Missed
 Rising Edge

[IMAGE alt='image' src='GUID-9C72511A-F427-4372-B973-22C7DE3EF354-a5.svg']

High Time

High
 Time

High Time

#### Scan Clock Properties

Use the FPGA I/O
 Property Node to access the following properties for the Scan Clock I/O item.

[IMAGE alt='image' src='GUID-57CBA91C-5B3A-42CC-8079-75BA5B02286E-a5.svg']

Enabled

Enabled

[IMAGE alt='image' src='GUID-9C72511A-F427-4372-B973-22C7DE3EF354-a5.svg']

High Time

High Time

High Time

#### Example VIs

Refer to the User-Defined IOV
 Synchronized VI in the labview\examples\CompactRIO\NI Scan
 Engine\Advanced\Scan Engine Synchronization\Scan Engine
 Synchronization.lvproj for an example of using the Scan Clock I/O item
 and the Wait for Rising Edge method with user-defined I/O variables.

Refer to
 the User-Defined IOV Advanced Sync VI in the labview\examples\CompactRIO\NI
 Scan Engine\Advanced\Scan Engine Synchronization - Advanced\Scan Engine
 Synchronization - Advanced.lvproj for an example of using the Scan
 Clock I/O item and the Wait for Rising Edge method, including the High
 Time output, with user-defined I/O variables.

Parent topic:

Building and Troubleshooting a CompactRIO Embedded Application

Related concepts:

- Using the Scan Interface with Individual Modules

<!--NI_TOPIC bundle=ni-compactrio path=synchronizing-multiple-c-series-modules-with.html language=enus -->
## TOPIC 00386: Synchronizing Multiple C Series Modules with NI 9469 Modules

- bundle_id: `ni-compactrio`
- source_path: `synchronizing-multiple-c-series-modules-with.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/synchronizing-multiple-c-series-modules-with.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To synchronize multiple C Series modules using NI 9469 modules, complete the following procedure. Configuring the Master NI 9469 ModuleComplete the following steps to configure the master NI 9469 module. Configure the system. Right-click the NI 9469 module you want to configure as the master in the

### Synchronizing Multiple C Series Modules with NI 9469
 Modules

To synchronize multiple C Series modules using NI 9469 modules, complete the following
 procedure.

Parent topic:

Synchronizing Multiple C Series Modules

Related concepts:

- Synchronizing Multiple Modules (FPGA Interface)
- Understanding the Maximum Sample Rate When Synchronizing Multiple Modules (FPGA Interface)

#### Configuring the Master NI 9469 Module

Complete the following steps to configure the master NI 9469 module.

1. Configure the system.
2. Right-click the NI 9469 module you want to configure as the master in the
 Project Explorer window and select
 Properties. 
 The C Series Module Properties dialog box opens.
3. Select Master from the Configuration pull-down menu.
4. Enable the Export Clock checkbox.
5. Click the OK button.

#### Configuring the Slave NI 9469 Modules

Complete the following steps to configure the slave NI 9469 modules.

1. Right-click the NI 9469 module you want to configure as a slave in the
 Project Explorer window and select
 Properties. 
 The C Series Module Properties dialog box opens.
2. Select Slave from the Configuration pull-down menu.
3. Place a checkmark in the Import Clock checkbox.
4. Click the OK button.
5. Repeat Steps 1 through 4 for each additional NI 9469 module you
 want to configure as a slave.
6. Select File»Save All in the Project Explorer window.

<!--NI_TOPIC bundle=ni-compactrio path=synchronizing-multiple-cseriies-mods.html language=enus -->
## TOPIC 00387: Synchronizing Multiple C Series Modules

- bundle_id: `ni-compactrio`
- source_path: `synchronizing-multiple-cseriies-mods.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/synchronizing-multiple-cseriies-mods.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`

### Synchronizing Multiple C Series
 Modules

1. Configuring the Master Module
2. Configuring the Slave Modules
3. Acquiring Data from Synchronized C Series Modules
4. Synchronizing Multiple C Series Modules with NI 9469 Modules

Parent topic:

Building and Troubleshooting a CompactRIO Embedded Application

Related concepts:

- Synchronizing Multiple Modules (FPGA Interface)
- Understanding the Maximum Sample Rate When Synchronizing Multiple Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=synchronizing-multiple-modules-fpga-interface.html language=enus -->
## TOPIC 00388: Synchronizing Multiple Modules (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `synchronizing-multiple-modules-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/synchronizing-multiple-modules-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can synchronize multiple modules that are connected to the same FPGA device when your application meets the following requirements: The modules use the same master timebase source The modules start acquisition mode at the same time A single FPGA I/O Node function reads the synchronous data Creat

### Synchronizing Multiple Modules (FPGA Interface)

You can synchronize multiple modules that are connected to the same FPGA device when your
 application meets the following requirements:

- The modules use the same master timebase source
- The modules start acquisition mode at the same time
- A single FPGA I/O Node function reads the synchronous data

Create FPGA I/O items for the module before you can configure the items using the FPGA I/O Node.
 Develop the FPGA VI to meet the guidelines described in the following table.

For delta-sigma modules, you must synchronize multiple sample rates.

| Guideline | Details |
| --- | --- |
| Share a master timebase source | Configure the modules to share master timebase source. |
| Start the synchronized acquisition | Configure an FPGA I/O Node with Start channels for the module you want to synchronize. Wire a Boolean constant set to TRUE to each Start channel. Ensure that all I/O channels are in the same FPGA I/O Node. Otherwise, the FPGA I/O Node will not return synchronized data. |
| Acquire data from synchronized modules with the same data rate | Configure an FPGA I/O Node with all of the channels from which you want to synchronously sample. Ensure that all I/O channels are in the same FPGA I/O Node. Otherwise, the FPGA I/O Node will not return synchronized data. Refer to the Synchronizing NI 923x Modules (FPGA) VI in labview\\examples\\CompactRIO\\Module Specific\\NI 923x\\Synchronizing NI 923x Modules\\Synchronizing NI 923x Modules.lvproj for an example of synchronizing multiple modules with the same data rate. |
| Acquire data from synchronized modules with different data rates | If you synchronize modules that are configured for different data rates, create a separate loop for each data rate in the FPGA VI. In each loop, configure an FPGA I/O Node with all of the channels that are configured for the data rate of that loop. If you place channels that are configured for different rates in the same loop, LabVIEW returns an overrun warning, error 65539, from the FPGA I/O Node when you run the VI. A delay occurs before the FPGA I/O Node returns the first data point. The length of the delay depends on the data rate and model number of the module. The equation for the delay is provided in the following table. |

| Module | Decimation Rate, m | Clock Divider, n | Time to First Sample (s) |
| --- | --- | --- | --- |
| NI 9231, NI 9250, NI 9251 | 32 | n = 1 | (281.625 * m * n + 5.5) * Master_Timebase_Period ± 1 Master_Timebase_Period |
| 64 | n = 1 | (281.625 * m * n + 8.5) * Master_Timebase_Period ± 1 Master_Timebase_Period |  |
| 128, ..., 1,024 | n = 1 | (281.625 * m * n + 6.5) * Master_Timebase_Period ± 1 Master_Timebase_Period |  |
| 32, ..., 1,024 | n = 2, ..., 12 | (281.625 * m * n + 5.5) * Master_Timebase_Period ± 1 Master_Timebase_Period |  |
| NI 9218, NI 9225, NI 9227, NI 9229, NI 9234, NI 9237, NI 9238, NI 9239, NI 9242, NI 9244, NI 9246, NI 9247 | 256 | n = 1 | (8.5 + n * 34,152) * Master_Timebase_Period |
| n = 2, ..., 31 | (5.5 + n * 34,152) * Master_Timebase_Period |  |  |
| NI 9230, NI 9232 | 64 | n = 1, ..., 31 | 77/Fs + 4-5 Master_Timebase_Period |
| 128 | n = 1, ..., 31 | 72/Fs + 4-5 Master_Timebase_Period |  |
| 256 | n = 1, ..., 31 | 68/Fs + 4-5 Master_Timebase_Period |  |
| NI 9235, NI 9236 | 512 | n = 1, ..., 31 | 39/Fs + 110.5 MClk + 1 OClk + Analog Delay |

The Master_Timebase_Period = period of the internal or external clock that
 the module uses (1/13.1072 MHz, 1/12.8 MHz, or 1/10 MHz). Fs = sample
 rate. The divider and decimation rate depend on which sample rate you select.

Specifications

- For example, the NI-9232 Specifications lists the decimation rate
 as 64 and clock divider as 1 when sampling at 102.4 kHz.
- Using the equation in the NI-9218 Specifications , you can determine
 that the clock divider is 1 when the sample rate is 51.2 kHz.
 n = Master_Timebase_Frequency/256/ fs 
 [[1]](#note-d11670e421) [<sup>1</sup>](#fnsrc_1-d11670e421) This is the equation provided in the NI-9218 Specifications reorganized to
 solve for n.

| Module | Clock Divider, b | Time to First Sample (s) |
| --- | --- | --- |
| NI 9202 | 1 | ((5.40625 + e) * a * b * c * d + 4.5) * Master_Timebase_Period ± 1 Master_Timebase_Period |
| 2, ..., 11 | ((5.40625 + e) * a * b * c * d + 5.5) * Master_Timebase_Period ± 1 Master_Timebase_Period |  |

Master_Timebase_Period

a

b

c

d

e

- 0 for notch at Fs
- 1 for notch at Fs/2
- 3 for notch at Fs/4
- 7 for notch at Fs/8
- 15 for notch at Fs/16

NI-9202 Specifications

a

b

c

d

| Module | Filter | Clock Divider, b | Time to First Sample (s) |
| --- | --- | --- | --- |
| NI 9252, NI 9253 | Comb | 2 | ((5.40625 + b) * 128 * a + 8.5) * Master_Timebase_Period ± 1 Master_Timebase_Period |
| Others | ((5.40625 + b) * 128 * a + 5.5) * Master_Timebase_Period ± 1 Master_Timebase_Period |  |  |
| Butterworth | 2 | (5.40625 * 128 * a + 8.5) * Master_Timebase_Period ± 1 Master_Timebase_Period |  |
| Others | (5.40625 * 128 * a + 5.5) * Master_Timebase_Period ± 1 Master_Timebase_Period |  |  |

Master_Timebase_Period

a

b

- 0 for Filter Frequency—1 (notch at Fs)
- 1 for Filter Frequency—2 (notch at Fs/2)
- 3 for Filter Frequency—3 (notch at Fs/4)
- 7 for Filter Frequency—4 (notch at Fs/8)
- 15 for Filter Frequency—5 and 6 (notch at Fs/16)

a

Parent topic:

Analog Input Modules

Related concepts:

- Configuring the Master Timebase Source for a C Series Module (FPGA Interface)
- Understanding Loop Timing (FPGA Interface)
- Understanding the Maximum Sample Rate When Synchronizing Multiple Modules (FPGA Interface)

[<sup>1</sup>](#note_ref-d11670e421) This is the equation provided in the NI-9218 Specifications reorganized to
 solve for n.

<!--NI_TOPIC bundle=ni-compactrio path=synchronizing-multiple-ni-9326-modules-fpga-i.html language=enus -->
## TOPIC 00389: Synchronizing Multiple NI 9326 Modules (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `synchronizing-multiple-ni-9326-modules-fpga-i.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/synchronizing-multiple-ni-9326-modules-fpga-i.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to synchronize multiple NI 9326 modules that are connected to the same FPGA device. Create the FPGA I/O items with all the I/O channels to be synchronized within a single FPGA I/O Node. Otherwise, the FPGA I/O Node will not return synchronized data. Configure an FPGA I/O

### Synchronizing Multiple NI 9326 Modules (FPGA Interface)

Complete the following steps to synchronize multiple NI 9326 modules that are connected to the same FPGA device.

1. Create the FPGA I/O items with all the I/O
 channels to be synchronized within a single FPGA
 I/O Node. Otherwise, the FPGA I/O Node will not
 return synchronized data.
2. Configure an FPGA I/O Node with Start channels for the NI 9326 modules you want to synchronize.
3. Wire a Boolean constant set to
 TRUE to each
 Start channel.

Parent topic:

NI 9326 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=synchronizing-multiple-ni-9361-modules-fpga-i.html language=enus -->
## TOPIC 00390: Synchronizing Multiple NI 9361 Modules (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `synchronizing-multiple-ni-9361-modules-fpga-i.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/synchronizing-multiple-ni-9361-modules-fpga-i.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to synchronize multiple NI 9361 modules that are connected to the same FPGA device. Create the FPGA I/O items with all the I/O channels to be synchronized, within a single FPGA I/O Node. Otherwise, the FPGA I/O Node will not return synchronized data. Configure an FPGA I/

### Synchronizing Multiple NI 9361 Modules (FPGA Interface)

Complete the following steps to synchronize multiple NI 9361 modules that are connected to the same FPGA device.

1. Create the FPGA I/O items with all the I/O channels to be synchronized, within a single FPGA I/O
 Node. Otherwise, the FPGA I/O Node will not return synchronized data.
2. Configure an FPGA I/O Node with Start channels for the NI 9361 modules you want to synchronize.
3. Wire a Boolean constant set to
 TRUE to each
 Start channel.

Parent topic:

NI 9361

<!--NI_TOPIC bundle=ni-compactrio path=synchronizing-multiple-ni-9770-modules-fpga-i.html language=enus -->
## TOPIC 00391: Synchronizing Multiple NI 9770 Modules (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `synchronizing-multiple-ni-9770-modules-fpga-i.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/synchronizing-multiple-ni-9770-modules-fpga-i.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can synchronize multiple NI 9770 modules that are connected to the same FPGA device if your application meets the following requirements: The modules use the same master timebase source. The modules start acquisition mode at the same time. A single FPGA I/O Node function reads the synchronous da

### Synchronizing Multiple NI 9770 Modules (FPGA Interface)

You can synchronize multiple NI 9770 modules that are connected to the same FPGA device if your application meets the following requirements:

- The modules use the same master timebase source.
- The modules start acquisition mode at the same time.
- A single FPGA I/O Node function reads the synchronous data.

Note

#### Sharing a Master Timebase Source

Configure the modules to share the same master timebase source.

#### Sharing the LO Signal

To enable a
 repeatable phase relationship between the master module and the slave modules, share
 a local oscillator (LO) signal between a master module and one or more slave
 modules.

Complete the following steps to configure the modules to share the
 same LO signal.

1. Designate one module as the master module, which will drive its LO signal to a
 slave module.
2. Connect the LO OUT terminal on the master module to the LO IN terminal on the
 slave module. Note You can add multiple slave modules in a daisy-chain configuration by
 connecting the LO OUT terminal of one slave module to the LO IN terminal of
 the next slave module. Note Add 50 Ω termination to the
 LO OUT terminal of the last slave module in the chain.
3. Configure the master module to export its LO signal on the LO OUT terminal by
 setting the LO Out Enabled property of the master module
 to TRUE.
4. Read the LO Frequency property of the master module. This
 value is used to configure the frequency of the LO IN signal on the slave
 module.
5. Configure the slave module to import its LO signal from the LO IN connector. Use
 the Configure RF In method of the slave module to set the
 following values: Parameter
 ValueLO Source
 LO In
 LO In Frequency
 The value returned by the LO
 Frequency property of the master
 module

#### Starting the Synchronized
 Acquisition

Start

Start

Note

#### Acquiring Data from Synchronized NI 9770 Modules
 with the Same Data Rate

Note

For an example of synchronizing multiple modules with the same data rate, refer
 to the Synchronizing NI 9770 Modules (FPGA) VI in
 labview\examples\CompactRIO\Module Specific\NI 9770\NI 9770 Multi-Module
 Synchronization\NI 9770 Multi-Module Synchronization.lvproj .

#### Acquiring Data from Synchronized NI 9770 Modules
 with Different Data Rates

If you synchronize NI 9770 modules that are
 configured for different data rates, create a separate loop for each data rate in
 the FPGA VI. In each loop, configure an FPGA I/O Node with all of the channels that
 are configured for the data rate of that loop. If you place NI 9770 channels that
 are configured for different data rates in the same loop, LabVIEW returns an overrun
 warning from the FPGA I/O Node (error 65539) when you run the VI. There is a delay
 before the FPGA I/O Node returns the first data point. The length of the delay
 depends on the data rate of the NI 9770.

Parent topic:

NI 9770 (FPGA Interface)

Related concepts:

- Configuring the Master Timebase Source for a C Series Module (FPGA Interface)
- Understanding Loop Timing (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=synchronizing-the-ni-9470-with-other-modules.html language=enus -->
## TOPIC 00392: Synchronizing the NI 9470 with Other Modules (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `synchronizing-the-ni-9470-with-other-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/synchronizing-the-ni-9470-with-other-modules.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can synchronize the NI 9470 with other modules that are connected to the same FPGA device if your application meets the following requirements: The modules must use the same master timebase source The modules must start acquisition mode at the same time Each channel of the NI 9470 must be in its

### Synchronizing the NI 9470 with Other Modules (FPGA Interface)

You can synchronize the NI 9470 with other modules that are connected to the same FPGA device if your application meets the following requirements:

- The modules must use the same master timebase source
- The modules must start acquisition mode at the same time
- Each channel of the NI 9470 must be in its own FPGA I/O Node residing in its own loop.

Create FPGA I/O items for the module before you can configure the items using the FPGA I/O Node.
 Develop the FPGA VI to meet the guidelines described in the following table.

For delta-sigma modules, you will need to synchronize multiple sample rates.

| Guideline | Details |
| --- | --- |
| Share a master timebase source | Configure the modules to share master timebase source. |
| Start the synchronized acquisition | Configure an FPGA I/O Node with Start channels for the module you want to synchronize. Wire a Boolean constant set to TRUE to each Start channel. Ensure that all Start channels are in the same FPGA I/O Node. The data will not be synchronized if they are not. |
| Acquire data from synchronized modules | Create separate loops for each channel of the NI 9470 that runs at a different data rate. Channels that are configured to run at the same data rate can either be in the same loop or be in a separate loop. For channels that are configured to run at different data rates, configure an FPGA I/O Node in each loop. For channels that are configured to run at the same data rate, you can either configure one FPGA I/O Node for the all the channels or configure an FPGA I/O Node for each channel. If you place channels that are configured for different data rates in the same loop, LabVIEW returns an overrun warning, error 65539, from the FPGA I/O Node for the AI channels and an underflow warning, error 65676, from the FPGA I/O Node for the AO channels. A delay occurs before the FPGA I/O Node returns the first data point. The length of the delay depends on the data rate and the PWM Divisor for each NI 9470 channel. Refer to Synchronizing Multiple Modules (FPGA Interface) for how to synchronize other DSA modules that are synchronized with the NI 9470. |
| Understand the maximum sample rate when synchronizing multiple modules | — |

| 12.8 MHz OCLK | 13.1072 MHz OCLK | Time to First Channel Sample(s) |
| --- | --- | --- |
| 3.200 kS/s | 3.277 kS/s | (14,472,838 + 4,000 * n) * (Master Timebase Period ± 1 Master Timebase Period) |
| 3.125 kS/s | 3.200 kS/s | (14,472,838 + 4,096 * n) * (Master Timebase Period ± 1 Master Timebase Period) |
| 2.560 KS/s | 2.621 KS/s | (14,472,838 + 5,000 * n) * (Master Timebase Period ± 1 Master Timebase Period) |
| 2.000 KS/s | 2.048 KS/s | (14,473,006 + 6,400 * n) * (Master Timebase Period ± 1 Master Timebase Period) |

Note

Master Timebase Period

n

PWM Divisor I/O Property

n

synchronizing multiple modules

Parent topic:

NI 9470 (FPGA Interface)

Related concepts:

- Configuring the Master Timebase Source for a C Series Module (FPGA Interface)
- Synchronizing Multiple Modules (FPGA Interface)
- Understanding the Maximum Sample Rate When Synchronizing Multiple Modules (FPGA Interface)
- NI 9470 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=timing-and-synchronization-modules-reference.html language=enus -->
## TOPIC 00393: Timing and Synchronization Module Reference

- bundle_id: `ni-compactrio`
- source_path: `timing-and-synchronization-modules-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/timing-and-synchronization-modules-reference.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 520 C Series Timing and Synchronization Modules Timing and Synchronization Module Description NI-9467 GPS C Series Synchronization Module NI-9469 Chassis C Series Synchronization Module

### Timing and Synchronization Module
 Reference

| Timing and Synchronization Module | Description |
| --- | --- |
| NI-9467 | GPS C Series Synchronization Module |
| NI-9469 | Chassis C Series Synchronization Module |

<!--NI_TOPIC bundle=ni-compactrio path=transceiver-mode-sbrio.html language=enus -->
## TOPIC 00394: Transceiver Mode

- bundle_id: `ni-compactrio`
- source_path: `transceiver-mode-sbrio.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/transceiver-mode-sbrio.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 629 Transceiver Mode PropertyData typePermissionsRead While Stopped? Read While Running?Write While Stopped?Write While Running?Read/WriteNo YesNoYesThis property sets the mode for the CAN transceiver, as well as the associated mode in the TCAN4550 CAN controller. The values are: 0: Normal 1: Sleep

### Transceiver Mode

| Data type | Permissions | Read While Stopped? | Read While Running? | Write While Stopped? | Write While Running? |
| --- | --- | --- | --- | --- | --- |
|  | Read/Write | No | Yes | No | Yes |

This property sets the mode for the CAN transceiver, as well as the associated mode in the TCAN4550 CAN controller.

- 0: Normal
- 1: Sleep

The Sleep mode places the TCAN4550 and the CAN transceiver into a low-power state. This low-power state has no effect on LabVIEW FPGA hardware. The Sleep mode can be set only when the CAN controller is running (not when stopped).

A local wakeup occurs when you set Transceiver Mode from
 Sleep back to Normal.

A remote wakeup occurs when a remote node transmits a CAN frame (referred to
 as the wakeup frame). The wakeup frame wakes up the transceiver and CAN controller chip.
 The wakeup frame is not received or acknowledged by the TCAN4550 CAN controller. When
 the wakeup frame ends, the CAN port enters Normal mode, and again receives and transmits
 CAN frames. If the node that transmitted the wakeup frame did not detect an
 acknowledgment (such as if other nodes were also waking), it retries the transmission,
 and the retry is received by the CAN port.

To determine when a remote wakeup occurs when the transceiver is in Sleep mode, invoke
 the Wait On Transceiver Wakeup method.

Parent topic:

I/O Properties

<!--NI_TOPIC bundle=ni-compactrio path=transceiver-mode.html language=enus -->
## TOPIC 00395: Transceiver Mode

- bundle_id: `ni-compactrio`
- source_path: `transceiver-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/transceiver-mode.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 557 Transceiver Mode PropertyData typePermissionsWrite while stopped?Write while running?Read/WriteNoYesThis property sets the mode for the CAN transceiver, as well as the associated mode in the SJA1000 CAN controller. The values are: 0: Normal 1: Sleep The Sleep mode places the SJA1000 and the CAN

### Transceiver Mode

| Data type | Permissions | Write while stopped? | Write while running? |
| --- | --- | --- | --- |
|  | Read/Write | No | Yes |

This property sets the mode for the CAN transceiver, as well as the associated mode in the SJA1000 CAN controller.

- 0: Normal
- 1: Sleep

The Sleep mode places the SJA1000 and the CAN transceiver into a low-power state. This low-power state has no effect on LabVIEW FPGA hardware. The Sleep mode can be set only when the CAN controller is running (not when stopped).

A local wakeup occurs when you set Transceiver Mode from Sleep back to Normal.

A remote wakeup occurs when a remote node transmits a CAN frame (referred to as the wakeup frame). The wakeup frame wakes up the transceiver and CAN controller chip. The wakeup frame is not received or acknowledged by the SJA1000 CAN controller. When the wakeup frame ends, the CAN port enters Normal mode, and again receives and transmits CAN frames. If the node that transmitted the wakeup frame did not detect an acknowledgement (such as if other nodes were also waking), it will retry the transmission, and the retry will be received by the CAN port.

To determine when a remote wakeup occurs when the transceiver is in Sleep mode, invoke the
 Wait On Transceiver Wakeup method.

After communication starts, the SJA1000 must detect a *bus free condition* (11 bit
 times) before you can change the Transceiver Mode to Sleep. If you set
 the mode to Sleep before bus free, the SJA1000 automatically returns to
 Normal mode. After you start communication (run FPGA with
 Auto Start enabled or invoke Start
 method), wait at least 11 bit times before setting Transceiver Mode to Sleep.

Parent topic:

I/O Properties for CAN Modules

Related concepts:

- Error Terminals
- I/O Properties for CAN Modules
- Wait on Transceiver Wakeup
- Start

<!--NI_TOPIC bundle=ni-compactrio path=transmit-error-counter.html language=enus -->
## TOPIC 00396: Transmit Error Counter

- bundle_id: `ni-compactrio`
- source_path: `transmit-error-counter.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/transmit-error-counter.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 558 Transmit Error Counter PropertyData typePermissionsRead While Stopped? Read While Running?Write While Stopped?Write While Running?ReadYes YesN/AN/AThis property provides access to the CAN controller Transmit Error Counter defined by the CAN standard.

### Transmit Error Counter

| Data type | Permissions | Read While Stopped? | Read While Running? | Write While Stopped? | Write While Running? |
| --- | --- | --- | --- | --- | --- |
|  | Read | Yes | Yes | N/A | N/A |

This property provides access to the CAN controller Transmit Error Counter defined by the CAN standard.

Parent topic:

I/O Properties for CAN Modules

<!--NI_TOPIC bundle=ni-compactrio path=transmit-error-counter_2.html language=enus -->
## TOPIC 00397: Transmit Error Counter

- bundle_id: `ni-compactrio`
- source_path: `transmit-error-counter_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/transmit-error-counter_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 628 Transmit Error Counter PropertyData typePermissionsRead While Stopped? Read While Running?Write While Stopped?Write While Running?ReadYes YesN/AN/AThis property provides access to the CAN controller Transmit Error Counter defined by the CAN standard.

### Transmit Error Counter

| Data type | Permissions | Read While Stopped? | Read While Running? | Write While Stopped? | Write While Running? |
| --- | --- | --- | --- | --- | --- |
|  | Read | Yes | Yes | N/A | N/A |

This property provides access to the CAN controller Transmit Error Counter defined by the CAN standard.

Parent topic:

I/O Properties

<!--NI_TOPIC bundle=ni-compactrio path=understanding-loop-timing-fpga-interface.html language=enus -->
## TOPIC 00398: Understanding Loop Timing (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `understanding-loop-timing-fpga-interface.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/understanding-loop-timing-fpga-interface.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: 97 C Series Modules that have an Internal Master Timebase and are Internally Timed NI 9202 NI 9225 NI 9227 NI 9229 NI 9230 NI 9231 NI 9232 NI 9234 NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 NI 9242 NI 9244 NI 9246 NI 9247 NI 9250 NI 9251 NI 9252 NI 9253 NI 9260 NI 9770 NI 9775 Do not use the Loop Timer

### Understanding Loop Timing (FPGA Interface)

| NI 9202 NI 9225 NI 9227 NI 9229 NI 9230 NI 9231 NI 9232 NI 9234 | NI 9235 NI 9236 NI 9237 NI 9238 NI 9239 NI 9242 NI 9244 NI 9246 | NI 9247 NI 9250 NI 9251 NI 9252 NI 9253 NI 9260 NI 9770 NI 9775 |
| --- | --- | --- |

Do not use the Loop Timer function or the Wait function in
 a loop with an FPGA I/O Node that acquires data from one of these modules.

When you create a loop that reads data from one of these modules, make sure the loop does not
 execute slower than the data rate of the module. If the loop execution time is slower
 than the data rate, the FPGA I/O Node returns an overrun warning and continues to read
 data. The overrun warning means that the data the FPGA I/O Node returns is valid, but
 the function missed one or more data points since the last time it read data from the
 module.

The function returns the overrun warning when all of the following conditions are true:

- The module is in acquisition mode.
- An FPGA I/O Node that is acquiring data from the module executes at least once after you put the module in acquisition mode.
- The FPGA I/O Node did not read one or more data points since the previous time the function executed.

If the application acquires multiple buffers of data from the module and the timing relationship between them is not important, you can ignore the overrun warning returned with the first point of each buffer. 
Avoiding Overrun Warnings

To avoid overrun warnings, develop the FPGA VI to meet the following guidelines:

| Conditions | Guidelines |
| --- | --- |
| Your application acquires multiple buffers of data from a module with an internal master timebase. | If the timing relationship between the buffers is not important, you can ignore the overrun warning returned with the first point of each buffer. |
| You are reading from multiple modules with an internal master timebase in the same loop. | Use one FPGA I/O Node to read the channels. Configure the modules to share a master timebase source and have the same data rate. |
| You are reading from a module with an internal master timebase and another analog input module in the same loop. | If the rate at which you can acquire data from the other module is as fast or faster than the data rate configured for the module with an internal master timebase, you can read from both modules in the same loop. If you use the same FPGA I/O Node to read data from all modules, the FPGA I/O Node does not return data for the other module until the module with an internal master timebase acquires data. If the other module has a slower data rate than the module with an internal master timebase and you read from both modules in the same loop, the FPGA I/O Node for the module with an internal master timebase returns an overrun warning and continues reading data. To avoid missing data, you can either change the data rate of the module with an internal master timebase or read from each module in a different loop. |

Parent topic:

Analog Input Modules

<!--NI_TOPIC bundle=ni-compactrio path=understanding-ni-9201-9221-scanning-fpga-inte.html language=enus -->
## TOPIC 00399: Understanding NI 9201/9221 Scanning (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `understanding-ni-9201-9221-scanning-fpga-inte.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/understanding-ni-9201-9221-scanning-fpga-inte.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To scan the channels of the NI 9201/9221, configure an FPGA I/O Node with the channels you want to acquire from the module. The module implements a pipeline that is automatically managed by the FPGA I/O Node. Channels within the FPGA I/O Node are sampled in numerical order regardless of the order th

### Understanding NI 9201/9221 Scanning (FPGA Interface)

To scan the channels of the NI 9201/9221, configure an FPGA I/O Node with the channels you want
 to acquire from the module.

The module implements a pipeline that is automatically managed by the FPGA I/O Node.
 Channels within the FPGA I/O Node are sampled in numerical order regardless of the order
 they appear in the node.

The first time an FPGA I/O Node configured with channels on an NI 9201/9221 module executes, the module performs two setup conversions before converting the first channel. The two setup conversions prime the pipeline for subsequent FPGA I/O Node reads. The module does not repeat the setup conversions unless the FPGA I/O Node channel configuration changes and the pipeline needs to be primed again.

Parent topic:

NI 9201 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=understanding-ni-9201-9221-scanning-fpga-inte_2.html language=enus -->
## TOPIC 00400: Understanding NI 9201/9221 Scanning (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `understanding-ni-9201-9221-scanning-fpga-inte_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/understanding-ni-9201-9221-scanning-fpga-inte_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To scan the channels of the NI 9201/9221, configure an FPGA I/O Node with the channels you want to acquire from the module. The module implements a pipeline that is automatically managed by the FPGA I/O Node. Channels within the FPGA I/O Node are sampled in numerical order regardless of the order th

### Understanding NI 9201/9221 Scanning (FPGA Interface)

To scan the channels of the NI 9201/9221, configure an FPGA I/O Node with the channels you want
 to acquire from the module.

The module implements a pipeline that is automatically managed by the FPGA I/O Node.
 Channels within the FPGA I/O Node are sampled in numerical order regardless of the order
 they appear in the node.

The first time an FPGA I/O Node configured with channels on an NI 9201/9221 module executes, the module performs two setup conversions before converting the first channel. The two setup conversions prime the pipeline for subsequent FPGA I/O Node reads. The module does not repeat the setup conversions unless the FPGA I/O Node channel configuration changes and the pipeline needs to be primed again.

Parent topic:

NI 9221 (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=understanding-power-on-and-startup-output-sta.html language=enus -->
## TOPIC 00401: Understanding Power-On and Startup Output States for CompactRIO Output Modules (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `understanding-power-on-and-startup-output-sta.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/understanding-power-on-and-startup-output-sta.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The power-on output state is the state that a C Series output module is in when power is applied to the module. You cannot configure the power-on output state. Refer to the module documentation on ni.com/docs for information about the power-on output state for your module. C Series analog output mod

### Understanding Power-On and Startup Output States for CompactRIO Output Modules (FPGA Interface)

Note

C Series analog output modules have a *Hot Swap Behavior* feature that allows you to
 configure the state of the output channels when the module is removed and reinserted.

The startup output state is the state that a CompactRIO channel is in after you load and run an
 FPGA VI that communicates with the output module. You can configure startup output
 states.

#### Configuring Startup Output States

Use
 the FPGA I/O Node analog or digital output options to change startup output states.
 You can develop the FPGA VI so that the output function executes when the FPGA VI
 starts running.

#### Understanding Output States

| Action | State of the Output Channels |
| --- | --- |
| The chassis with the module powers on. | Power-on output state |
| An FPGA VI loads. | Startup output state |
| An Invoke Method function configured with the Abort method executes on the host VI. | Power-on output state |
| A Close FPGA VI Reference function that is configured to Close and Reset executes. Close and Reset is the default action for the Close FPGA VI Reference function. | Power-on output state |
| A Close FPGA VI Reference function that is configured to Close executes. | Last output value |
| You click the Abort button on the host VI or select Operate»Stop while LabVIEW is targeted to an FPGA device and the FPGA VI is running with Interactive Front Panel Communication. | Last output value |
| You remove and reinsert one of the following modules: NI 9476, NI 9477, or NI 9478. | Power-on output state |
| You remove and reinsert one of the following modules and the FPGA VI is not loaded: NI 9263, NI 9264, NI 9265, NI 9269. | Power-on output state |
| You remove and reinsert one of the following modules and the FPGA VI is loaded, but not running: NI-9263, NI-9264, NI-9265, NI-9269. | Power-on output state |
| You remove and reinsert one of the following modules and the FPGA VI is loaded and running: NI-9263, NI-9264, NI-9265, NI-9269. | User-configurable |
| You remove and reinsert one of the following modules: NI-9375, NI-9401, NI-9402, NI-9403, NI-9472, NI-9474, NI-9475, NI-9481 or NI-9485. NI recommends that you do not replace a module that is a different type with one of these modules after the FPGA VI is loaded. Replacing a module that is a different type than the module with which you are replacing it after the FPGA VI is loaded can place the output channels in an undefined or unexpected state. | Last output value |

Parent topic:

Building and Troubleshooting a CompactRIO Embedded Application

Related concepts:

- NI 9263
- NI 9264
- NI 9265
- NI 9269
- NI 9375
- NI 9401
- NI 9402
- NI 9403
- NI 9472
- NI 9474
- NI 9475
- NI 9476
- NI 9477
- NI 9478
- NI 9481
- NI 9485

<!--NI_TOPIC bundle=ni-compactrio path=understanding-the-maximum-sample-rate-when-sy.html language=enus -->
## TOPIC 00402: Understanding the Maximum Sample Rate When Synchronizing Multiple Modules (FPGA Interface)

- bundle_id: `ni-compactrio`
- source_path: `understanding-the-maximum-sample-rate-when-sy.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/understanding-the-maximum-sample-rate-when-sy.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following C Series modules derive their sampling rate from the internal master timebase. To show information about the internal master timebase and maximum sample rate for a specific module, select the module from the following list.

### Understanding the Maximum Sample Rate When
 Synchronizing Multiple Modules (FPGA Interface)

The following C Series modules derive their sampling rate from the internal master timebase.

To show information about the internal master timebase and maximum sample rate for a specific
 module, select the module from the following list.

- [NI 9202](ni-9202-max-rate-synch.html)
- [NI 9218](ni-9218-max-rate-synch.html)
- [NI 9225](ni-9225-max-rate-synch.html)
- [NI 9227](ni-9227-max-rate-synch.html)
- [NI 9229](ni-9229-max-rate-synch.html)
- [NI 9230](ni-9230-max-rate-synch.html)
- [NI 9231](ni-9231-max-rate-synch.html)
- [NI 9232](ni-9232-max-rate-synch.html)
- [NI 9234](ni-9234-max-rate-synch.html)
- [NI 9235](ni-9235-max-rate-synch.html)
- [NI 9236](ni-9236-max-rate-synch.html)
- [NI 9237](ni-9237-max-rate-synch.html)
- [NI 9238](ni-9238-max-rate-synch.html)
- [NI 9239](ni-9239-max-rate-synch.html)
- [NI 9242](ni-9242-max-rate-synch.html)
- [NI 9244](ni-9244-max-rate-synch.html)
- [NI 9246](ni-9246-max-rate-synch.html)
- [NI 9247](ni-9247-max-rate-synch.html)
- [NI 9250](ni-9250-max-rate-synch.html)
- [NI 9251](ni-9251-max-rate-synch.html)
- [NI 9252](ni-9252-max-rate-synch.html)
- [NI 9253](ni-9253-max-rate-synch.html)
- [NI 9260](ni-9260-max-rate-synch.html)
- [NI 9470](ni-9470-max-rate-synch.html)

Parent topic:

Synchronizing Multiple Modules (FPGA Interface)

Related concepts:

- Configuring the Master Timebase Source for a C Series Module (FPGA Interface)
- Synchronizing Multiple Modules (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=user-manual-welcome.html language=enus -->
## TOPIC 00403: NI CompactRIO User Manual

- bundle_id: `ni-compactrio`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/user-manual-welcome.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NI CompactRIO User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### NI CompactRIO
 User Manual

The NI CompactRIO User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- CompactRIO Systems (cRIO)
- CompactRIO Chassis
- Download NI CompactRIO
- Interactive Activation Guide
- NI CompactRIO Release Notes
- NI CompactRIO Waveform Reference Library
- LabVIEW for CompactRIO Developer's Guide
- Developing Embedded Applications using CompactRIO and LabVIEW FPGA
- LabVIEW FPGA Module Programming Reference Manual
- Software Support for CompactRIO, CompactDAQ, Single-Board RIO, R Series, and
 EtherCAT

<!--NI_TOPIC bundle=ni-compactrio path=using-a-vi-to-convert-and-calibrate-9204-5-6-data.html language=enus -->
## TOPIC 00404: Using a VI to Convert and Calibrate Values (NI-9204, NI-9205, and NI-9206)

- bundle_id: `ni-compactrio`
- source_path: `using-a-vi-to-convert-and-calibrate-9204-5-6-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/using-a-vi-to-convert-and-calibrate-9204-5-6-data.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using the NI-9204, NI-9205, and NI-9206, refer to the Binary to Nominal Polynomial (Host) VI in the LabVIEW example program below. This example uses the straight-line conversion algorithm with the NI-MCal linearization correction to convert binary analog input values to calibrated engineering u

### Using a VI to Convert and Calibrate Values
 (NI-9204, NI-9205, and NI-9206)

When using the NI-9204, NI-9205, and NI-9206, refer to the Binary to Nominal
 Polynomial (Host) VI in the LabVIEW example program below. This example
 uses the straight-line conversion algorithm with the NI-MCal linearization correction to
 convert binary analog input values to calibrated engineering units.

Use the Binary to Nominal Polynomial (Host) VI as a subVI in the host
 VI.

#### LabVIEW Example
 Program

labview\examples\CompactRIO\Module Specific\NI
 9204\<module> Linearization Coefficients\NI 9204 Linearization
 Coefficients.lvproj

- <module> is NI 9204 , NI 9205 , or
 NI 9206 .

Parent topic:

Converting and Calibrating CompactRIO Analog Input Values (FPGA Interface)

<!--NI_TOPIC bundle=ni-compactrio path=using-c-series-modules-in-a-labview-project.html language=enus -->
## TOPIC 00405: Using C Series Modules in a LabVIEW Project

- bundle_id: `ni-compactrio`
- source_path: `using-c-series-modules-in-a-labview-project.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/using-c-series-modules-in-a-labview-project.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: To use C Series modules in a LabVIEW project, configure the project with your controller, chassis, and FPGA. The following figure shows a project configured with a controller, chassis, FPGA target, and C Series modules in Scan Interface mode and FPGA Interface mode. Target Chassis Item Real-Time Sc

### Using C Series Modules in a LabVIEW Project

To use C Series modules in a LabVIEW project, configure the project with your controller,
 chassis, and FPGA.

The following figure shows a project configured with a controller, chassis, FPGA target,
 and C Series modules in Scan Interface mode and FPGA
 Interface mode.

[IMAGE alt='image' src='GUID-0BB5D602-3E42-4477-998B-1EDFB4476F8E-a5.svg']

1. Target
2. Chassis Item
3. Real-Time Scan Resources Item
4. C Series Modules (Scan Interface)
5. FPGA Target
6. C Series Module (FPGA Interface)

For an example of a LabVIEW project using C Series I/O, refer to the *Using the Scan
 Interface with FPGA Interface LabVIEW* project in
 labview\examples\CompactRIO\NI Scan Engine\Getting Started\Using Scan
 Interface with FPGA Interface\Using Scan Interface with FPGA
 Interface.lvproj.

#### Target and Chassis Items

| Target Item Icon | Device |
| --- | --- |
|  | CompactRIO Controller |
|  | Ethernet RIO Chassis |
|  | CompactRIO Chassis Ethernet RIO Chassis |

| Chassis Item Icon | Device |
| --- | --- |
|  | CompactRIO Chassis, Ethernet RIO Chassis |
|  | MXIe-RIO Chassis |
|  | R Series Expansion Chassis Single-Board RIO Mezzanine Card |
|  | Single-Board RIO Device |

Parent topic:

Building and Troubleshooting a CompactRIO Embedded Application

Related concepts:

- Configuring a Project
- Programming Interfaces

<!--NI_TOPIC bundle=ni-compactrio path=using-crio-io-device-control.html language=enus -->
## TOPIC 00406: Using the cRIO I/O Device Control

- bundle_id: `ni-compactrio`
- source_path: `using-crio-io-device-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/using-crio-io-device-control.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the cRIO I/O Device to specify a cRIO I/O item on the block diagram. To configure the cRIO I/O Device, right-click the Device and select Configure I/O Type. The Configure I/O Type dialog box opens to determine which methods and properties a cRIO I/O Device supports. To select a cRIO I/O item fro

### Using the cRIO I/O Device Control

Use the cRIO I/O Device to specify a cRIO I/O item on the block diagram.

Configure
 I/O Type

Configure I/O Type

- To select a cRIO I/O item from the shortcut menu on the block diagram, click the
 arrow on the right side of the Device. A shortcut menu opens with items that
 appear in the Project Explorer window under the same target as the active
 VI.
- Specify an I/O item by clicking inside the cRIO I/O Device and typing the name
 of the I/O item.
- To enable the cRIO I/O Device to reference a cRIO I/O resource, add the I/O
 resource under the cRIO target in the Project Explorer window.
- When creating a reusable subVI, use the cRIO I/O control to specify a cRIO I/O
 item on the block diagram.

#### Configure I/O Type Dialog Box

I/O Items

I/O Item Type

Replace All

I/O Item
 Type

I/O Name Control
 Type

I/O Item Type Details

I/O Item Type

I/O Name Control Type

Remove

I/O Name Control Type

I/O Name Control Type Details

I/O Name Control Type

Parent topic:

Using C Series Modules in a LabVIEW Project

<!--NI_TOPIC bundle=ni-compactrio path=using-equation-to-convert-and-calibrate-values.html language=enus -->
## TOPIC 00407: Using an Equation to Convert and Calibrate Values

- bundle_id: `ni-compactrio`
- source_path: `using-equation-to-convert-and-calibrate-values.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/using-equation-to-convert-and-calibrate-values.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following equation in the host VI to convert binary analog input values to calibrated engineering units: Input Engineering Units = (Binary Value × LSB Weight – Offset)When converting and calibrating data acquired from the NI-9203 in ±20 mA range, the equation is <codeph>Input Engineering Uni

### Using an Equation to Convert and Calibrate Values

Use the following equation in the host VI to convert binary analog input values to
 calibrated engineering units:

- Input Engineering Units = (Binary Value × LSB Weight –
 Offset) [[1]](#note-d12231e30) [<sup>1</sup>](#fnsrc_1-d12231e30) When converting and calibrating data acquired from the
 NI-9203 in ±20 mA range, the equation is <codeph>Input Engineering Units =
 ((Binary Value – 32768) × LSB Weight – Offset)</codeph>.

- Binary Value is the signed or unsigned value returned by the
 FPGA I/O Node
- LSB Weight is the value returned by the LSB Weight
 property
- Offset is the value returned by the Offset property.

The LSB Weight and Offset units differ per module.

To convert to calibrated engineering units, use the FPGA I/O Property
 Node to read the *LSB Weight* and *Offset*
 properties. If you do not want to read the LSB Weight and Offset values from the module,
 convert to uncalibrated engineering units. Use the following values for Offset and LSB
 Weight:

Offset = 0<sup>[[2]](#note-d12231e79)</sup>[<sup>2</sup>](#fnsrc_2-d12231e79) When calculating engineering units for the NI-9203 in ±20
 mA range, Offset = 20 mA.

LSB Weight = Typical Input Span ÷ 2<sup>ADC Resolution</sup>

Where

- Typical Input Span value is listed in the following table for each
 module.
- ADC Resolution value is the ADC resolution of the module. Refer to
 module documentation to obtain this value.

| Module | Typical Input Span |
| --- | --- |
| NI-9201 | 21.06 V |
| NI-9203 | 21.56 mA (unipolar), 43.12 mA (bipolar) |
| NI-9205 | 20.8 V |
| NI-9206 | 21.5 V |
| NI-9215 | 20.8 V |
| NI-9216 | 100 Ω RTD |
| NI-9217 | 100 Ω RTD |
| NI-9218 | Varies by mode; refer to the following table NI-9218 Typical Input Span |
| NI-9220 | 20.8 V |
| NI-9221 | 125 V |
| NI-9222 | 21.2 V |
| NI-9223 | 21.2 V |
| NI-9225 | 850 V |
| NI-9226 | 1,000 Ω RTD |
| NI-9227 | 29.954 A |
| NI-9229 | 125.28 V |
| NI-9230 | 63 V |
| NI-9232 | 63 V |
| NI-9234 | 10.2 V |
| NI-9235 | 52.6 mV/V |
| NI-9236 | 52.6 mV/V |
| NI-9237 | 50 mV/V |
| NI-9238 | 1.25 V |
| NI-9239 | 21.04 V |
| NI-9246 | 62.5 A |
| NI-9247 | 294 A |
| NI-9381 | 5 V |

| Channel Mode | Typical Measurement Range |
| --- | --- |
| ±16 V | ±16.3 V |
| ±20 mA | 24.4 mA |
| ±22 mV/V Bridge | 22.1 mV/V |
| ±5 V IEPE | 5.33 V |
| ±60 V | ±62.1 V |
| ±65 mV | 73.5 mV |

Parent topic:

Converting and Calibrating CompactRIO Analog Input Values (FPGA Interface)

[<sup>1</sup>](#note_ref-d12231e30) When converting and calibrating data acquired from the
 NI-9203 in ±20 mA range, the equation is <codeph>Input Engineering Units =
 ((Binary Value – 32768) × LSB Weight – Offset)</codeph>.

[<sup>2</sup>](#note_ref-d12231e79) When calculating engineering units for the NI-9203 in ±20
 mA range, Offset = 20 mA.

<!--NI_TOPIC bundle=ni-compactrio path=using-scan-interface-with-ind-modules.html language=enus -->
## TOPIC 00408: Using the Scan Interface with Individual Modules

- bundle_id: `ni-compactrio`
- source_path: `using-scan-interface-with-ind-modules.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/using-scan-interface-with-ind-modules.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You may be able to use the Scan Interface for supported individual modules even if the chassis you are using is in FPGA Interface programming mode or does not support Scan Interface programming mode. First you must let LabVIEW discover the modules in the chassis and download a compiled bitfile to th

### Using the Scan Interface with Individual Modules

You may be able to use the Scan Interface for supported individual modules even if the chassis
 you are using is in FPGA Interface programming mode or does not
 support Scan Interface programming mode. First you must let
 LabVIEW discover the modules in the chassis and download a compiled bitfile to the
 chassis. Using modules that require the high-speed interface, such as the NI 951x, may
 also require a downloaded compiled bitfile. You must have the LabVIEW FPGA module
 installed to compile bitfiles for the FPGA.

After setting up your project, discovering modules, and downloading the bitfile to the chassis,
 use modules under the FPGA target in FPGA Interface programming mode and use modules
 under the Real-Time Scan Resources item in Scan Interface programming mode.

Note

Tip

Note

Note

Parent topic:

Programming Interfaces

Related concepts:

- Synchronizing FPGA VIs with the NI Scan Engine (FPGA Interface)
- Configuring a Project

#### Creating the LabVIEW Project

Complete the following steps to set up the LabVIEW project:

1. Configure the system.
2. Drag and drop the C Series module(s) that will run in Scan Interface mode under
 the Real-Time Scan Resources item. Leave any modules you plan to write FPGA code
 for under the FPGA target.

The LabVIEW Project Explorer window should look similar to the following figure:

[IMAGE alt='image' src='GUID-7995CE8B-C3AE-499A-BBF3-570BBBFA4E00-a5.svg']

1. Module in Scan Interface Programming Mode
2. Module in FPGA Interface Programming Mode

#### Downloading the Bitfile

Complete the following steps to compile a bitfile and download it to the chassis:

1. Create a new VI under the FPGA target and save it with your project files. You
 will use this FPGA VI from an RT VI to download the module bitfile to the
 chassis.
2. Right-click the FPGA VI and select Create Build
 Specification from the shortcut menu. Under Build
 Specifications , right-click the new build specification for the
 example FPGA VI, select Build , and wait for the build to
 complete.
3. Create a new VI under the RT target and save it with your Project files.
4. Add an Open FPGA VI Reference function to the block
 diagram of the new RT VI.
5. Right-click the Open FPGA VI Reference function and
 select Configure Open FPGA VI Reference from the shortcut
 menu to open the Configure Open FPGA VI Reference dialog
 box.
6. Select the FPGA VI you created in step 1, make sure that the Run the
 FPGA VI checkbox is enabled, and click OK 
 to close the dialog box.
7. Place the code you want to run in the RT VI on the block diagram to the right of
 the Open FPGA VI Reference function. Enclose the code in
 a structure such as a Timed Loop or While Loop.
8. Add a Close FPGA VI Reference function to the block
 diagram to the right of the structure enclosing the code.
9. Connect the Open FPGA VI Reference function to the
 Close FPGA VI Reference function through the
 structure that encloses the code.
10. Run the RT VI.

The LabVIEW Project Explorer window should look similar to the following figure:

[IMAGE alt='image' src='GUID-2864C0B6-C173-46B3-B621-F905B6FAA356-a5.svg']

1. Module in Scan Interface Mode
2. Module in FPGA Interface Mode
3. FPGA VI to Download Bitfile
4. RT VI to Download Bitfile

Note

<!--NI_TOPIC bundle=ni-compactrio path=using-the-rio-device-i-o-control.html language=enus -->
## TOPIC 00409: Using the RIO Device I/O Control

- bundle_id: `ni-compactrio`
- source_path: `using-the-rio-device-i-o-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/using-the-rio-device-i-o-control.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Place the RIO Device I/O control on the front panel of a VI. Use the I/O control pull-down menu to select a RIO device. Selecting a RIO Device in a Project VI Targeted to My Computer If the VI is part of a project and is targeted to My Computer, the I/O control pull-down menu shows the following sec

### Using the RIO Device I/O Control

Place the RIO Device I/O control on the front panel of a VI.

Use the I/O control pull-down menu to select a RIO device.

#### Selecting a RIO Device in a Project VI Targeted to
 My Computer

- RIO devices in the project
- Local RIO devices and local RIO aliases
- Browse , which opens the Browse RIO
 Devices dialog box
- Recently used RIO devices

#### Selecting a RIO Device in a Project VI Targeted to
 an RT Controller

If the VI is part of a project and is targeted to an RT
 controller, the I/O control pull-down menu shows RIO devices local to the
 controller.

#### Selecting a RIO Device in a Non-Project
 VI

If the VI is not part of a project, the I/O control pull-down menu
 shows the following sections from top to bottom.

- Local RIO devices and local RIO aliases
- Browse, which opens the Browse RIO Devices dialog
 box
- Recently used RIO devices

#### Browse RIO Devices Dialog Box

Use this
 dialog box to select from local and remote RIO devices. Click the
 + sign to the left of a device to show the FPGA target
 associated with that device. This dialog box includes the following components:

Add Remote System

Refresh Device List

Parent topic:

Using C Series Modules in a LabVIEW Project

<!--NI_TOPIC bundle=ni-compactrio path=wait-on-comm-state-change.html language=enus -->
## TOPIC 00410: Wait on Comm State Change

- bundle_id: `ni-compactrio`
- source_path: `wait-on-comm-state-change.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/wait-on-comm-state-change.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Wait for a change in the communication state of the CAN port (Comm State property). This enables you to handle CAN communication state changes in a separate loop from your main CAN Input/Output loop. If the Comm State property changes before you call Wait (relative to the previous Wait), the current

### Wait on Comm State Change

Wait for a change in the communication state of the CAN port (Comm State
 property). This enables you to handle CAN communication state changes in a separate loop
 from your main CAN Input/Output loop.

If the Comm State property changes before you call Wait
 (relative to the previous Wait), the current Wait returns immediately. The
 Comm State is not considered to be changed when you first
 Start, and it does not change after Stop.

This method returns an error if invoked while communication is stopped.

#### Node
 Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error Terminals

[IMAGE alt='image' src='GUID-C23371C7-9839-4697-89F2-D0A635332E12-a5.svg']

Timeout

Timeout

Comm State

Timed Out?

FALSE

Comm State

Timed Out?

TRUE

Timeout

–1

#### Node
 Outputs

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error Terminals

Timed Out?

TRUE

[IMAGE alt='image' src='GUID-C85B9DA8-4DC5-4608-AF6B-D53C8D212F1F-a5.svg']

Comm State

Parent topic:

I/O Methods for CAN Modules

<!--NI_TOPIC bundle=ni-compactrio path=wait-on-comm-state-change_2.html language=enus -->
## TOPIC 00411: Wait on Comm State Change

- bundle_id: `ni-compactrio`
- source_path: `wait-on-comm-state-change_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/wait-on-comm-state-change_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Wait for a change in the communication state of the CAN port (Comm State property). This enables you to handle CAN communication state changes in a separate loop from your main CAN Input/Output loop. If the Comm State property changes before you call Wait (relative to the previous Wait), the current

### Wait on Comm State Change

Wait for a change in the communication state of the CAN port (Comm State
 property). This enables you to handle CAN communication state changes in a separate loop
 from your main CAN Input/Output loop.

If the Comm State property changes before you call Wait
 (relative to the previous Wait), the current Wait returns immediately. The
 Comm State is not considered to be changed when you first
 Start, and it does not change after Stop.

This method returns an error if invoked while communication is stopped.

#### Node
 Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error Terminals

[IMAGE alt='image' src='GUID-C23371C7-9839-4697-89F2-D0A635332E12-a5.svg']

Timeout

Timeout

Comm State

Timed Out?

FALSE

Comm State

Timed Out?

TRUE

Timeout

–1

#### Node
 Outputs

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error Terminals

Timed Out?

TRUE

[IMAGE alt='image' src='GUID-C85B9DA8-4DC5-4608-AF6B-D53C8D212F1F-a5.svg']

Comm State

Parent topic:

I/O Methods for sbRIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=wait-on-transceiver-wakeup.html language=enus -->
## TOPIC 00412: Wait on Transceiver Wakeup

- bundle_id: `ni-compactrio`
- source_path: `wait-on-transceiver-wakeup.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/wait-on-transceiver-wakeup.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Wait for the Transceiver Mode property to change from Sleep to Normal mode due to a remote wakeup (bus activity) or local wakeup. A local wakeup occurs if you use the I/O Property node to set Transceiver Mode property back to Normal. If a wakeup occurs before you call Wait (relative to the previous

### Wait on Transceiver Wakeup

Wait for the Transceiver Mode property to change from
 Sleep to Normal mode due to a remote wakeup
 (bus activity) or local wakeup. A local wakeup occurs if you use the I/O Property node
 to set Transceiver Mode property back to Normal.

If a wakeup occurs before you call Wait (relative to the previous Wait), the
 current Wait returns immediately. The wakeup is not considered to have occurred when you
 first Start, and it does not occur after Stop.

This method returns an error if invoked while communication is stopped.

#### Node
 Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error Terminals

[IMAGE alt='image' src='GUID-C23371C7-9839-4697-89F2-D0A635332E12-a5.svg']

Timeout

Timeout

Comm State

Timed Out?

FALSE

Comm State

Timed Out?

TRUE

Timeout

–1

#### Node
 Outputs

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error Terminals

Timed Out?

TRUE

Parent topic:

I/O Methods for CAN Modules

Related concepts:

- Transceiver Mode
- Error Terminals

<!--NI_TOPIC bundle=ni-compactrio path=wait-on-transceiver-wakeup_2.html language=enus -->
## TOPIC 00413: Wait on Transceiver Wakeup

- bundle_id: `ni-compactrio`
- source_path: `wait-on-transceiver-wakeup_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/wait-on-transceiver-wakeup_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Wait for the Transceiver Mode property to change from Sleep to Normal mode due to a remote wakeup (bus activity) or local wakeup. A local wakeup occurs if you use the I/O Property node to set Transceiver Mode property back to Normal. If a wakeup occurs before you call Wait (relative to the previous

### Wait on Transceiver Wakeup

Wait for the Transceiver Mode property to change from
 Sleep to Normal mode due to a remote wakeup
 (bus activity) or local wakeup. A local wakeup occurs if you use the I/O Property node
 to set Transceiver Mode property back to Normal.

If a wakeup occurs before you call Wait (relative to the previous Wait), the
 current Wait returns immediately. The wakeup is not considered to have occurred when you
 first Start, and it does not occur after Stop.

This method returns an error if invoked while communication is stopped.

#### Node
 Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error Terminals

[IMAGE alt='image' src='GUID-C23371C7-9839-4697-89F2-D0A635332E12-a5.svg']

Timeout

Timeout

Comm State

Timed Out?

FALSE

Comm State

Timed Out?

TRUE

Timeout

–1

#### Node
 Outputs

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error Terminals

Timed Out?

TRUE

Parent topic:

I/O Methods for sbRIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=wait-on-transmit-complete.html language=enus -->
## TOPIC 00414: Wait on Transmit Complete

- bundle_id: `ni-compactrio`
- source_path: `wait-on-transmit-complete.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/wait-on-transmit-complete.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Wait for all frames written to CAN Output to complete transmission. You typically use this to determine when all frames have been acknowledged. If all transmits are complete before you call Wait (relative to the previous Wait), the current wait returns immediately. All transmits are considered compl

### Wait on Transmit Complete

Wait for all frames written to CAN Output to complete transmission. You typically use this to
 determine when all frames have been acknowledged.

If all transmits are complete before you call Wait (relative to the previous
 Wait), the current wait returns immediately. All transmits are considered complete after
 you first Start. This method returns an error if invoked while communication is stopped.

#### Node
 Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error Terminals

[IMAGE alt='image' src='GUID-C23371C7-9839-4697-89F2-D0A635332E12-a5.svg']

Timeout

Timeout

Comm State

Timed Out?

FALSE

Comm State

Timed Out?

TRUE

Timeout

–1

#### Node
 Outputs

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error Terminals

Timed Out?

TRUE

Parent topic:

I/O Methods for CAN Modules

Related concepts:

- Transceiver Mode
- Error Terminals

<!--NI_TOPIC bundle=ni-compactrio path=wait-on-transmit-complete_2.html language=enus -->
## TOPIC 00415: Wait on Transmit Complete

- bundle_id: `ni-compactrio`
- source_path: `wait-on-transmit-complete_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/wait-on-transmit-complete_2.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: Wait for all frames written to CAN Output to complete transmission. You typically use this to determine when all frames have been acknowledged. If all transmits are complete before you call Wait (relative to the previous Wait), the current wait returns immediately. All transmits are considered compl

### Wait on Transmit Complete

Wait for all frames written to CAN Output to complete transmission. You typically use this to
 determine when all frames have been acknowledged.

If all transmits are complete before you call Wait (relative to the previous
 Wait), the current wait returns immediately. All transmits are considered complete after
 you first Start. This method returns an error if invoked while communication is stopped.

#### Node
 Inputs

[IMAGE alt='image' src='GUID-2F73BE22-59DC-499C-82DD-01584C207E3F-a5.svg']

Error In

Error Terminals

[IMAGE alt='image' src='GUID-C23371C7-9839-4697-89F2-D0A635332E12-a5.svg']

Timeout

Timeout

Comm State

Timed Out?

FALSE

Comm State

Timed Out?

TRUE

Timeout

–1

#### Node
 Outputs

[IMAGE alt='image' src='GUID-656146DF-DD7C-44A4-90F1-3A2AFD7D00E4-a5.svg']

Error Out

Error Terminals

Timed Out?

TRUE

Parent topic:

I/O Methods for sbRIO Devices

<!--NI_TOPIC bundle=ni-compactrio path=what-is-the-relationship-between-bits-per-sec.html language=enus -->
## TOPIC 00416: What is the relationship between bits per second, throughput, and bus utilization?

- bundle_id: `ni-compactrio`
- source_path: `what-is-the-relationship-between-bits-per-sec.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/what-is-the-relationship-between-bits-per-sec.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: The term bits per second (bps) refers to the bit rate of data transfer, with 1/bps being the length of time required to transmit one bit. Throughput is the actual data transfer measured by the amount of data transmitted ÷ time required to transmit.Bus utilization is the percentage of time that the s

### What is the relationship between bits per second, throughput, and bus utilization?

The term bits per second (bps) refers to the bit rate of data transfer, with 1/bps being the length of time required to transmit one bit.

Throughput is the actual data transfer measured by the amount of data
 transmitted ÷ time required to transmit.

Bus utilization is the percentage of time that the serial bus is actively
 transmitting data. Because a wide range of factors such as flow control, processor
 latency, and device architecture can affect serial performance, bus utilization often is
 not 100 percent.

There is overhead associated with serial communication in the form of start bits, stop
 bits, and parity bits. This overhead reduces the throughput by 20–30 percent.The actual
 data throughput can be considerably less than the bits per second setting.

Parent topic:

Serial Communication

<!--NI_TOPIC bundle=ni-compactrio path=writing-to-c-series-channels.html language=enus -->
## TOPIC 00417: Writing to C Series Channels

- bundle_id: `ni-compactrio`
- source_path: `writing-to-c-series-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio/raw/resource/enus/writing-to-c-series-channels.html
- document_id: `ni-compactrio`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can read from C series channels using the FPGA interface or Scan interface. Write Data using the FPGA Interface Complete the following steps to write data to an output channel in a CompactRIO, Ethernet RIO, MXIe-RIO, or Single-Board RIO system. Configure a project for the system. Make sure the o

### Writing to C Series Channels

You can read from C series channels using the FPGA interface or Scan interface.

Parent topic:

Building and Troubleshooting a CompactRIO Embedded Application

Related concepts:

- CompactRIO Embedded System
- Configuring a Project with Connected Hardware
- Simultaneously Reading From or Writing to Multiple CompactRIO Channels (FPGA Interface)

#### Write Data using the FPGA Interface

Complete the following steps to write data to an output channel in a CompactRIO,
 Ethernet RIO, MXIe-RIO, or Single-Board RIO system.

1. Configure a project for the system.
2. Make sure the output channel is added to the system.
3. Right-click the FPGA target in the Project Explorer
 window and select New»VI to add a new FPGA VI to the
 system.
4. Place an FPGA I/O Node on the block diagram of the FPGA VI.
5. Click the element section of the FPGA I/O Node and select
 Module»Module/Channel
 or Onboard I/O»Port»Port/DIO from the
 shortcut menu, where Module represents a C Series module and
 Module/Channel is the channel to which you want to write. 
 If you configure an FPGA I/O Node for multiple channels, the I/O Node accesses
 the channels simultaneously or sequentially depending on the type of module and
 other factors. 
 Note LabVIEW can
 write to CompactRIO digital output lines as ports for some I/O
 modules.

##### Confirming the State of Digital Output
 Channels

For digital channels, you also can read the digital output channel.

Complete the following steps to read from the digital output channels.

1. Place another FPGA I/O Node function on the block diagram. 
 This FPGA I/O Node must execute after the FPGA I/O Node you added above.
2. Click the element section of the FPGA I/O Node and select
 Module»Module/Channel
 or Onboard I/O»Port»Port/DIO from the
 shortcut menu, where Module represents a C Series module and
 Module/Channel is the channel you want to read.
3. Right-click the new FPGA I/O Node and select Change to
 Read from the shortcut menu.

#### Write Data using the Scan Interface

Complete the following steps to write data to an output channel in a CompactRIO or
 Single-Board RIO system.

1. Configure a project for the system.
2. Make sure the I/O variable for the output channel appears under the module item
 in the Project Explorer window.
3. Right-click the RT target item for the controller or device in the
 Project Explorer window and select
 New»VI from the shortcut menu to add a new LabVIEW
 Real-Time VI to the target.
4. Place a Timed Loop on the block diagram of the VI.
5. Configure the Timed Loop to use the Synchronize to Scan Engine timing
 source.
6. Place the I/O variable for the channel in the Timed Structure.
7. Right-click the input terminal of the I/O variable and select
 Create»Control.
8. Right-click the error out terminal of the I/O variable
 and select Create»Indicator.
9. Run the VI.
