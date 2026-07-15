# NI DOCUMENT BUNDLE: flexrio-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=flexrio-labview-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=flexrio-labview-api-ref path=clock-selections-page.html language=enus -->
## TOPIC 00001: Clock Selections Page (DRAM Properties Dialog Box)

- bundle_id: `flexrio-labview-api-ref`
- source_path: `clock-selections-page.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/clock-selections-page.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: FPGA Module In the DRAM Bank x Properties dialog box, select Clock Selections from the Category list to display this page. Use this page to link each clock port defined by the CLIP to a clock on the FPGA target. You must add the FPGA clock to the LabVIEW project before you can link to the

### Clock Selections Page (DRAM Properties Dialog Box)

**Requires: FPGA Module**

In the DRAM Bank x Properties dialog box, select Clock Selections from the Category list to display this page.

Use this page to link each clock port defined by the CLIP to a clock on the FPGA target. You must add the FPGA clock to the LabVIEW project before you can link to the FPGA clock.

This page includes the following components:

- Component-Level IP Clock —Lists clock(s) defined in the CLIP declaration XML file.
- Connection —Lists clocks available on the FPGA target.

Parent topic:

DRAM Properties Dialog Box

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=dram-properties-dialog-box.html language=enus -->
## TOPIC 00002: DRAM Properties Dialog Box

- bundle_id: `flexrio-labview-api-ref`
- source_path: `dram-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/dram-properties-dialog-box.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click a DRAM Bank x item in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Check the Enable DRAM checkbox if it is not already selected to display the following pages in the Category list: General Clock Selections

### DRAM Properties Dialog Box

Right-click a DRAM Bank x item in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Check the Enable DRAM checkbox if it is not already selected to display the following pages in the Category list:

- General
- Clock Selections

- [General Page (DRAM Properties Dialog Box)](general-page.html)
- [Clock Selections Page (DRAM Properties Dialog Box)](clock-selections-page.html)

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=flexrio-host-interface-attributes-bool.html language=enus -->
## TOPIC 00003: FlexRIO Host Interface Bool Attributes

- bundle_id: `flexrio-labview-api-ref`
- source_path: `flexrio-host-interface-attributes-bool.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/flexrio-host-interface-attributes-bool.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table describes the Bool attributes available through the FlexRIO Host Interface. Attribute Description IO Module Present TRUE if an adapter module is detected by the FlexRIO device. IO Module Power Good Displays the status of TB_Power_Good signal from the adapter module. Vcco Programm

### FlexRIO Host Interface Bool Attributes

The following table describes the Bool attributes available through the FlexRIO Host Interface.

| Attribute | Description |
| --- | --- |
| IO Module Present | TRUE if an adapter module is detected by the FlexRIO device. |
| IO Module Power Good | Displays the status of TB_Power_Good signal from the adapter module. |
| Vcco Programmed Successfully | TRUE if Vcco was programmed successfully. |
| PXI_CLK10 Present (NI PXI-795xR only) | TRUE if the FlexRIO device can detect the PXI_CLK10 clock. |
| IO Module I/O Enabled | TRUE if the adapter module I/O is enabled. |
| IO Module Power Enabled | TRUE if the adapter module power is enabled. |
| EEPROM Power Enabled | TRUE if the power is enabled to the EEPROM on the adapter module. |
| IO Module Power Good Timed Out | TRUE if the adapter module did not drive the TB_Power_Good pin within the time the FlexRIO device expected. |
| IO Module ID Mismatch | TRUE if the IO Module ID expected by the current VI downloaded to the FPGA is different from the ID of the adapter module that is currently connected to the FlexRIO device. |
| IO Module ID Read Timeout | TRUE if the IO Module ID expected by the current VI downloaded to the FPGA was not received within the time the FlexRIO device expected. |
| Inserted IO Module Has EEPROM | Returns TRUE if the inserted adapter module has an EEPROM that can be detected, or FALSE if no EEPROM is detected. |
| Expected IO Module Has EEPROM | Returns TRUE if the expected adapter module has an EEPROM, or FALSE if no EEPROM is expected. |
| Is IO Module Supported | Returns TRUE if adapter modules are supported by the selected FlexRIO device. |
| PXIe_CLK100 Locked? (NI PXIe-796xR and NI PXIe-797xR only) | Returns TRUE if the base clock PLL is locked to the PXIe 100 MHz Clock. |

Parent topic:

FlexRIO_Host_QueryAttribute_Bool VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=flexrio-host-interface-attributes-u32.html language=enus -->
## TOPIC 00004: FlexRIO Host Interface U32 Attributes

- bundle_id: `flexrio-labview-api-ref`
- source_path: `flexrio-host-interface-attributes-u32.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/flexrio-host-interface-attributes-u32.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table describes the U32 attributes available through the FlexRIO Host Interface. Attribute Description Inserted IO Module ID Returns the IO Module ID of the adapter module that is currently connected to the FlexRIO device. Expected IO Module ID Returns the I/O Module ID that the curren

### FlexRIO Host Interface U32 Attributes

The following table describes the U32 attributes available through the FlexRIO Host Interface.

| Attribute | Description |
| --- | --- |
| Inserted IO Module ID | Returns the IO Module ID of the adapter module that is currently connected to the FlexRIO device. |
| Expected IO Module ID | Returns the I/O Module ID that the current VI downloaded to the FPGA is configured to use. |
| Current Temperature | Returns the current temperature of the PCB temperature sensor in units of 0.25 °. |
| Vcco A Value (raw) (NI PXI-795xR and NI PXIe-796xR only) | Returns the Vcco A raw DAC value. |
| Vcco B Value (raw) (NI PXI-795xR and NI PXIe-796xR only) | Returns the Vcco B raw DAC value. |
| Signature | Returns the 32-bit signature for the FlexRIO device. |
| Revision | Returns the present FPGA revision in YYMMDDHH format. |
| Oldest Compatible Revision | Contains the latest date at which a modification was performed on this FPGA which would break software compatibility, in YYMMDDHH format. Software built for a date after this value is considered to be compatible. |
| IO Module State | Returns the current state of the IO Module manager. |
| I2CMux | Returns the current owner of the I2C Bus. Possible values are: None, Hardware, Software, and LVFPGA. |
| Serial Number | Returns the serial number of the FlexRIO FPGA module. |
| IO Module Serial Number | Returns the serial number of the FlexRIO adapter module. |
| Fan Speed (NI-793xR only) | Returns the speed of the device fan in RPM. |
| FAN PWM (NI-793xR only) | Returns the PWM (pulse width modulation) duty cycle, in units of percentage, of the device fan. |

Parent topic:

FlexRIO_Host_QueryAttribute_U32 VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=flexrio-labview-host-vis.html language=enus -->
## TOPIC 00005: FlexRIO LabVIEW Host VIs

- bundle_id: `flexrio-labview-api-ref`
- source_path: `flexrio-labview-host-vis.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/flexrio-labview-host-vis.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: All FlexRIO Host VIs are found in the following LLB: C:\Program Files\National Instruments\LabVIEW\vi.lib\FlexRIO\FlexRIO_HostInterface.llb NI recommends using the System Configuration API in all cases where you are querying an attribute. The Host VIs provide low-level access to the FlexRIO device.

### FlexRIO LabVIEW Host VIs

All FlexRIO Host VIs are found in the following LLB:

C:\Program Files\National Instruments\LabVIEW\vi.lib\FlexRIO\FlexRIO_HostInterface.llb

NI recommends using the [System Configuration API](/csh?context=flexrio_flexriomodularmerge_sysconfigapi) in all cases where you are querying an attribute.

Caution

- [FlexRIO_Host_ControlIOModPower VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-controliomodpower-vi.html) Enables or disables power to the attached FlexRIO adapter module.
- [FlexRIO_Host_CustomAttributeRead VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-customattributeread-vi.html) Queries the current value of the specified attribute.
- [FlexRIO_Host_CustomAttributeWrite VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-customattributewrite-vi.html) Writes a value to the specified custom attribute.
- [FlexRIO_Host_EEPROMRead32 VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromread32-vi.html) Reads an unsigned 32-bit number from the adapter module EEPROM at the specified address.
- [FlexRIO_Host_EEPROMReadByteArray VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromreadbytearray-vi.html) Reads an array of bytes from the adapter module EEPROM, starting at the specified address.
- [FlexRIO_Host_EEPROMWrite32 VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromwrite32-vi.html) Writes an unsigned 32-bit number to the adapter module EEPROM at the specified address.
- [FlexRIO_Host_EEPROMWriteByteArray VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-eepromwritebytearray-vi.html) Writes an array of bytes to the adapter module EEPROM, starting at the specified address.
- [FlexRIO_Host_GetDeviceShutdownLimit VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-getdeviceshutdownlimit-vi.html) This VI returns the device's thermal shutdown limit.
- [FlexRIO_Host_GetDeviceStatus VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-getdevicestatus-vi.html) Queries the current status of the specified hardware device.
- [FlexRIO_Host_I2CAccessControl VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-i2caccesscontrol-vi.html) Use this VI to acquire or release software access to the adapter module I2C bus. NI FlexRIO firmware has an arbiter that controls access to the I2C bus on the adapter module interface. Before issuing any I2C bus commands to the adapter module, software must first acquire access to the I2C bus. The FlexRIO host interface gives users the ability to perform raw I2C bus cycles by using the FlexRIO_Host_I2CIssueBusCycle VI. Because this VI makes no assumptions about I2C command composition, you must use the FlexRIO_Host_I2C_AccessControl VI to acquire and release access to the bus before and after issuing your I2C command. Note that it is not necessary to use this VI with the FlexRIO EEPROM host interface VIs. The EEPROM host interface VIs will all automatically acquire and release access to the bus internally.
- [FlexRIO_Host_I2CIssueBusCycle VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-i2cissuebuscycle-vi.html) Use this VI to issue a single cycle on the adapter module I2C bus. By chaining multiple instances of this VI together, you are able to issue custom I2C commands to the adapter module interface. This is useful for accessing custom I2C circuitry that may exist on custom adapter modules. Note that prior to using this VI, you must first acquire software access to the I2C bus by calling the FlexRIO_Host_I2CAccessControl VI.
- [FlexRIO_Host_ProgramIOModID VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-programiomodid-vi.html) Programs the IO Module ID to the EEPROM on the adapter module that is currently connected. Note: Use this VI to program the IO Module ID on custom adapter modules only. Do not use this VI to reprogram the IO Module ID on an adapter module that you did not manufacturer.
- [FlexRIO_Host_QueryAttribute_Bool VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryattribute-bool-vi.html) Queries the current value of the selected attribute.
- [FlexRIO_Host_QueryAttribute_U32 VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryattribute-u32-vi.html) Queries the current value of the selected attribute.
- [FlexRIO_Host_QueryAttribute VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryattribute-vi.html) Use this VI to query the current value of the selected attribute.
- [FlexRIO_Host_QueryIOModID VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryiomodid-vi.html) Reads the IO Module ID from the EEPROM of the adapter module that is currently connected.
- [FlexRIO_Host_QueryIOModMgrState VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-queryiomodmgrstate-vi.html) Queries the current state of the adapter module manager.
- [FlexRIO_Host_RedetectIOMod VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-redetectiomod-vi.html) Redetects the adapter module that is currently connected to the selected FlexRIO device.
- [FlexRIO_Host_SetDeviceShutdownLimit VI](vi-lib/flexrio/flexrio-hostinterface-llb/flexrio-host-setdeviceshutdownlimit-vi.html) Use this VI to set the device's thermal shutdown limit.

Parent topic:

FlexRIO with Modular I/O

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=flexrio-properties.html language=enus -->
## TOPIC 00006: FlexRIO Properties

- bundle_id: `flexrio-labview-api-ref`
- source_path: `flexrio-properties.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/flexrio-properties.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### FlexRIO Properties

- [System Config](resource/objmgr/niflexriosae-rc.html)

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=flexrio-with-integrated-io.html language=enus -->
## TOPIC 00007: FlexRIO with Integrated I/O

- bundle_id: `flexrio-labview-api-ref`
- source_path: `flexrio-with-integrated-io.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/flexrio-with-integrated-io.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### FlexRIO with Integrated I/O

- [NI FlexRIO API v1](instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1-mnu.html) FlexRIO VIs provide common functionality including streaming, synchronization, clocking configuration, and I/O configuration. You can use the FlexRIO API with the default FPGA image to acquire data with your FlexRIO device without programming to the FPGA.
- [FlexRIO API FPGA v1](instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1-mnu.html) Find here the FlexRIO API FPGA VIs.

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=flexrio-with-modular-io.html language=enus -->
## TOPIC 00008: FlexRIO with Modular I/O

- bundle_id: `flexrio-labview-api-ref`
- source_path: `flexrio-with-modular-io.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/flexrio-with-modular-io.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### FlexRIO with Modular I/O

- [FlexRIO LabVIEW Host VIs](flexrio-labview-host-vis.html)

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=general-page.html language=enus -->
## TOPIC 00009: General Page (DRAM Properties Dialog Box)

- bundle_id: `flexrio-labview-api-ref`
- source_path: `general-page.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/general-page.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: FPGA Module In the DRAM Bank x Properties dialog box, select General from the Category list to display this page. Use this page to configure the type of memory interface that should be used when communicating with external DRAM. This page contains the following components: Enable DRAM—Enab

### General Page (DRAM Properties Dialog Box)

**Requires: FPGA Module**

In the DRAM Bank x Properties dialog box, select General from the Category list to display this page.

Use this page to configure the type of memory interface that should be used when communicating with external DRAM.

This page contains the following components:

- Enable DRAM —Enables the DRAM. Unchecking this box disables access to the DRAM for the selected DRAM bank.
- Memory Interface —Lists all memory interfaces that are compatible with the selected DRAM bank item. If multiple versions of a memory interface are available, the version information displays next to the memory interface name.
- Details —Displays general information about the selected DRAM memory interface item.
- Path —Displays the file system path to the XML file for the currently selected memory interface file.
- Reload —Reload the currently selected memory interface in the table. Use the Reload button if you modify a memory interface XML file on disk after you configure it for use with your FPGA target. Reload updates the I/O in the LabVIEW project and Details information, but changes may not be visible in the Memory Interface or Path dialogs.

FlexRIO ships with two memory interface support options which provide access to the external DRAM memory. Refer to the [DRAM Memory Interface](/csh?pubname=flexrio&topicname=dram-memory-interface.html) topic for more information.

Parent topic:

DRAM Properties Dialog Box

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/analog-edge-trigger-vim.html language=enus -->
## TOPIC 00010: Analog Edge Trigger VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/analog-edge-trigger-vim.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/analog-edge-trigger-vim.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements an analog edge trigger according to specified trigger and hysteresis conditions. icon Inputs/Outputs cu8.png internal pipeline stages c1dunkn.png trigger channel data trigger channel data specifies the data to monitor for trigger conditions. cunkn.png requested trigger level requested tri

### Analog Edge Trigger VI

Implements an analog edge trigger according to specified trigger and hysteresis conditions.

[IMAGE alt='icon' src='analog-edge-trigger-vim.png']

#### Inputs/Outputs

| internal pipeline stages — trigger channel data — trigger channel data specifies the data to monitor for trigger conditions. requested trigger level — requested trigger level specifies the level at which to assert triggered. requested hysteresis level — requested hysteresis level specifies the hysteresis level. rising edge — rising edge specifies whether to trigger on a rising edge. Set this parameter to FALSE to trigger on a falling edge. trigger channel data out — trigger channel data out returns a copy of trigger channel data. triggered — triggered returns TRUE if trigger level and hysteresis conditions have been met on trigger channel data. triggered on sample — triggered on sample indicates the samples on which trigger conditions were met. actual trigger level — actual trigger level indicates the actual level at which trigger conditions were met and triggered was asserted. |
| --- |

Parent topic:

FlexRIO API FPGA v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/block-ram-buffer-vim.html language=enus -->
## TOPIC 00011: Block RAM Buffer VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/block-ram-buffer-vim.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/block-ram-buffer-vim.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Implements a FIFO buffer in Block RAM. icon Inputs/Outputs c1di16.png new elements new elements specifies new elements to write to the buffer at write index. ci32.png write index write index specifies the index at which to write to the buffer. This index represents the next index after the index of

### Block RAM Buffer VI

Implements a FIFO buffer in Block RAM.

[IMAGE alt='icon' src='block-ram-buffer-vim.png']

#### Inputs/Outputs

| new elements — new elements specifies new elements to write to the buffer at write index. write index — write index specifies the index at which to write to the buffer. This index represents the next index after the index of the element most recently written to the buffer. read index — read index specifies the index from which to read. This index represents the index of the oldest element written to the buffer. allocation — allocation specifies the size of the buffer in block RAM. read out — read out returns data read from read index. |
| --- |

Parent topic:

Buffering

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/channel-packer-vim.html language=enus -->
## TOPIC 00012: Channel Packer VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/channel-packer-vim.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/channel-packer-vim.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Repackages inbound data into a larger output array. For example, a module that produces 2 samples per clock can be reformatted into one that produces 8 samples per data valid at 1/4 the frequency. In the FlexRIO design libraries, this is used to format the data into words that can be more efficientl

### Channel Packer VI

Repackages inbound data into a larger output array. For example, a module that produces 2 samples per clock can be reformatted into one that produces 8 samples per data valid at 1/4 the frequency. In the FlexRIO design libraries, this is used to format the data into words that can be more efficiently used with DRAM.

[IMAGE alt='icon' src='channel-packer-vim.png']

#### Inputs/Outputs

| output spc — output spc specifies the output samples per clock cycle. Set this parameter to a value that allows this VI to produce a unit that completely fills a DRAM word. For example, if the DRAM interface is 512 bits wide and 16-bit data is stored, set the output to 32 samples (512/16 = 32). Array in — Array in specifies an array of channel data. — data valid — data valid specifies whether input data is valid. Array out — Array out returns the input data repackaged into a larger output array. — full — full indicates when the requested output spc is met. |
| --- |
| — |
| — |

Parent topic:

Host Transfer

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/channel-to-dram-arbiter-vim.html language=enus -->
## TOPIC 00013: Channel to DRAM Arbiter VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/channel-to-dram-arbiter-vim.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/channel-to-dram-arbiter-vim.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Consumes a set of channel data and arbitrates which channel passes on each clock cycle. icon Inputs/Outputs c1dcclst.png channels in channels in specifies the data for a set of channels. c1di16.png cbool.png valid in valid in specifies whether input data is valid. c1dbool.png channels enabled channe

### Channel to DRAM Arbiter VI

Consumes a set of channel data and arbitrates which channel passes on each clock cycle.

[IMAGE alt='icon' src='channel-to-dram-arbiter-vim.png']

#### Inputs/Outputs

| channels in — channels in specifies the data for a set of channels. — valid in — valid in specifies whether input data is valid. channels enabled — channels enabled specifies the bitmask that determines which channels are enabled. ready for output — data — data returns the data from one of the enabled channels on each clock cycle according to the channels enabled bit mask. valid out — valid out informs downstream nodes whether data is valid. ready for input — |
| --- |
| — |

Parent topic:

Host Transfer

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/convert-fxp-to-integer-vim.html language=enus -->
## TOPIC 00014: Convert FXP to Integer VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/convert-fxp-to-integer-vim.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/convert-fxp-to-integer-vim.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an array of fixed point numerical values to an array of integers. icon Inputs/Outputs c1dcclst.png Array in Array in specifies an array of fixed-point numeric values. c1dunkn.png i1dcclst.png Array Array returns an array of integers. i1di16.png

### Convert FXP to Integer VI

Converts an array of fixed point numerical values to an array of integers.

[IMAGE alt='icon' src='convert-fxp-to-integer-vim.png']

#### Inputs/Outputs

| Array in — Array in specifies an array of fixed-point numeric values. — Array — Array returns an array of integers. — |
| --- |
| — |
| — |

Parent topic:

Host Transfer

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/dram-to-channel-arbiter-vi.html language=enus -->
## TOPIC 00015: DRAM to Channel Arbiter VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/dram-to-channel-arbiter-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/dram-to-channel-arbiter-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Identifies the channel contained in the current DRAM word. icon Inputs/Outputs cbool.png reset reset resets the state of this VI. c1dbool.png channels enabled channels enabled specifies the bitmask that determines which channels are enabled. cbool.png input valid input valid indicates whether the in

### DRAM to Channel Arbiter VI

Identifies the channel contained in the current DRAM word.

[IMAGE alt='icon' src='dram-to-channel-arbiter-vi.png']

#### Inputs/Outputs

| reset — reset resets the state of this VI. channels enabled — channels enabled specifies the bitmask that determines which channels are enabled. input valid — input valid indicates whether the input data is valid on the current clock cycle. channel count — channel count specifies the number of channels enabled. valid channel — valid channel outputs a bitmask that indicates which channel is valid. output valid — output valid indicates whether the output data is valid on the current clock cycle. |
| --- |

Parent topic:

Host Transfer

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1-mnu.html language=enus -->
## TOPIC 00016: FlexRIO API FPGA v1

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1-mnu.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Find here the FlexRIO API FPGA VIs. icon

### FlexRIO API FPGA v1

Find here the FlexRIO API FPGA VIs.

[IMAGE alt='icon' src='flexrio-api-fpga-v1-mnu.png']

- [Analog Edge Trigger VI](../../../../../instr-lib/flexrio/api/fpga/v1/analog-edge-trigger-vim.html) Implements an analog edge trigger according to specified trigger and hysteresis conditions.
- [IO State Monitor VI](../../../../../instr-lib/flexrio/api/fpga/v1/io-state-monitor-vi.html) Monitors the state of the I/O and reports errors.
- [Buffering](../../../../../instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1buffering-mnu.html) FPGA VIs related to buffering.
- [Host Transfer](../../../../../instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1host-transfer-mnu.html) FPGA VIs related to host transfer.
- [Synchronization](../../../../../instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1synchronization-mnu.html) FPGA VIs related to synchronisation.

Parent topic:

FlexRIO with Integrated I/O

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1buffering-mnu.html language=enus -->
## TOPIC 00017: Buffering

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1buffering-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1buffering-mnu.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FPGA VIs related to buffering. icon

### Buffering

FPGA VIs related to buffering.

[IMAGE alt='icon' src='flexrio-api-fpga-v1buffering-mnu.png']

- [Block RAM Buffer VI](../../../../../instr-lib/flexrio/api/fpga/v1/block-ram-buffer-vim.html) Implements a FIFO buffer in Block RAM.
- [Variable Delay VI](../../../../../instr-lib/flexrio/api/fpga/v1/variable-delay-vim.html) Applies a specified delay to a set of input data.

Parent topic:

FlexRIO API FPGA v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1host-transfer-mnu.html language=enus -->
## TOPIC 00018: Host Transfer

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1host-transfer-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1host-transfer-mnu.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FPGA VIs related to host transfer. icon

### Host Transfer

FPGA VIs related to host transfer.

[IMAGE alt='icon' src='flexrio-api-fpga-v1host-transfer-mnu.png']

- [Channel Packer VI](../../../../../instr-lib/flexrio/api/fpga/v1/channel-packer-vim.html) Repackages inbound data into a larger output array. For example, a module that produces 2 samples per clock can be reformatted into one that produces 8 samples per data valid at 1/4 the frequency. In the FlexRIO design libraries, this is used to format the data into words that can be more efficiently used with DRAM.
- [Streaming IDL Ready VI](../../../../../instr-lib/flexrio/api/fpga/v1/streaming-idl-ready-vi.html) Monitors the stream state for readiness.
- [Channel to DRAM Arbiter VI](../../../../../instr-lib/flexrio/api/fpga/v1/channel-to-dram-arbiter-vim.html) Consumes a set of channel data and arbitrates which channel passes on each clock cycle.
- [DRAM to Channel Arbiter VI](../../../../../instr-lib/flexrio/api/fpga/v1/dram-to-channel-arbiter-vi.html) Identifies the channel contained in the current DRAM word.
- [Convert FXP to Integer VI](../../../../../instr-lib/flexrio/api/fpga/v1/convert-fxp-to-integer-vim.html) Converts an array of fixed point numerical values to an array of integers.

Parent topic:

FlexRIO API FPGA v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1synchronization-mnu.html language=enus -->
## TOPIC 00019: Synchronization

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1synchronization-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/flexrio-api-fpga-v1synchronization-mnu.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FPGA VIs related to synchronisation. icon

### Synchronization

FPGA VIs related to synchronisation.

[IMAGE alt='icon' src='flexrio-api-fpga-v1synchronization-mnu.png']

- [Start Trigger VI](../../../../../instr-lib/flexrio/api/fpga/v1/start-trigger-vim.html) Conditions a start trigger for inter-device routing and TClk functionality.
- [Pulse Expander VI](../../../../../instr-lib/flexrio/api/fpga/v1/pulse-expander-vi.html) Expands a pulse to respect a specified minimum pulse length.
- [Resync Pulse VI](../../../../../instr-lib/flexrio/api/fpga/v1/resync-pulse-vi.html) Aligns the assertion of a signal to a specified pulse.

Parent topic:

FlexRIO API FPGA v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/io-state-monitor-vi.html language=enus -->
## TOPIC 00020: IO State Monitor VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/io-state-monitor-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/io-state-monitor-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Monitors the state of the I/O and reports errors. icon Inputs/Outputs cgenclassrntag.png io ready resource io ready resource specifies I/O to monitor for a ready state. cgenclassrntag.png io error resource io error resource specifies I/O to monitor for errors. ibool.png flexrio.module.io ready 0 fle

### IO State Monitor VI

Monitors the state of the I/O and reports errors.

[IMAGE alt='icon' src='io-state-monitor-vi.png']

#### Inputs/Outputs

| io ready resource — io ready resource specifies I/O to monitor for a ready state. io error resource — io error resource specifies I/O to monitor for errors. flexrio.module.io ready 0 — flexrio.module.io ready 0 indicates whether io ready resource is in a ready state. flexrio.module.io error 0 — flexrio.module.io error 0 returns errors identified in io error resource. |
| --- |

Parent topic:

FlexRIO API FPGA v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/pulse-expander-vi.html language=enus -->
## TOPIC 00021: Pulse Expander VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/pulse-expander-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/pulse-expander-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Expands a pulse to respect a specified minimum pulse length. icon Inputs/Outputs cunkn.png min pulse length min pulse length specifies a minimum pulse length. cbool.png input pulse input pulse specifies the pulse to expand. ibool.png expanded pulse expanded pulse returns the pulse that results from

### Pulse Expander VI

Expands a pulse to respect a specified minimum pulse length.

[IMAGE alt='icon' src='pulse-expander-vi.png']

#### Inputs/Outputs

| min pulse length — min pulse length specifies a minimum pulse length. input pulse — input pulse specifies the pulse to expand. expanded pulse — expanded pulse returns the pulse that results from expanding input pulse to respect the specified minimum pulse length. |
| --- |

Parent topic:

Synchronization

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/resync-pulse-vi.html language=enus -->
## TOPIC 00022: Resync Pulse VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/resync-pulse-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/resync-pulse-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aligns the assertion of a signal to a specified pulse. icon Inputs/Outputs cbool.png signal signal specifies the signal to align with sync pulse. cbool.png sync pulse sync pulse specifies the pulse with which to align signal. cbool.png clear? clear? clears a signal that is latched pending sync pulse

### Resync Pulse VI

Aligns the assertion of a signal to a specified pulse.

[IMAGE alt='icon' src='resync-pulse-vi.png']

#### Inputs/Outputs

| signal — signal specifies the signal to align with sync pulse. sync pulse — sync pulse specifies the pulse with which to align signal. clear? — clear? clears a signal that is latched pending sync pulse. signalled and sync — signalled and sync returns signal aligned with sync pulse. This parameter is TRUE only when signal and sync pulse are both TRUE or when sync pulse is TRUE and signal is latched into a pending state by a previous clock cycle. |
| --- |

Parent topic:

Synchronization

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/start-trigger-vim.html language=enus -->
## TOPIC 00023: Start Trigger VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/start-trigger-vim.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/start-trigger-vim.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Conditions a start trigger for inter-device routing and TClk functionality. icon Inputs/Outputs cbool.png dio for start export dio for start export specifies the DIO for exporting the start trigger signal. ci32.png dio start dio start specifies the DIO start trigger signal source. cu16.png flexrio.t

### Start Trigger VI

Conditions a start trigger for inter-device routing and TClk functionality.

[IMAGE alt='icon' src='start-trigger-vim.png']

#### Inputs/Outputs

| dio for start export — dio for start export specifies the DIO for exporting the start trigger signal. dio start — dio start specifies the DIO start trigger signal source. flexrio.trigger.start.cfg 0 — flexrio.trigger.start.cfg 0 specifies start trigger configuration information. external analog trigger — analog trigger — analog trigger implements an analog start trigger. user-defined start trigger — user-defined start trigger implements a start trigger using user-defined conditions. ready for start? — ready for start? specifies whether the downstream node is ready to receive the start trigger. trigger io resources — start trigger — started event — start trigger for export — start trigger for tclk — start trigger control — start trigger control contains the start trigger control information. arm start — arm start specifies whether to arm the start trigger. done — done specifies whether the stream is in a non-running state. conditioned start trigger — conditioned start trigger outputs the trigger signal conditioned for TClk and inter-device routing. unconditioned start trigger — unconditioned start trigger outputs the unconditioned start trigger. flexrio.trigger.start.metadata 0 — |
| --- |
| start trigger — started event — start trigger for export — start trigger for tclk — |
| arm start — arm start specifies whether to arm the start trigger. done — done specifies whether the stream is in a non-running state. |

Parent topic:

Synchronization

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/streaming-idl-ready-vi.html language=enus -->
## TOPIC 00024: Streaming IDL Ready VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/streaming-idl-ready-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/streaming-idl-ready-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Monitors the stream state for readiness. icon Inputs/Outputs cenum.png stream.state stream.state specifies the state of the stream. icclst.png start trigger control start trigger control contains start trigger control information. ibool.png arm start arm start indicates to the next node whether to a

### Streaming IDL Ready VI

Monitors the stream state for readiness.

[IMAGE alt='icon' src='streaming-idl-ready-vi.png']

#### Inputs/Outputs

| stream.state — stream.state specifies the state of the stream. start trigger control — start trigger control contains start trigger control information. arm start — arm start indicates to the next node whether to arm the Start trigger. This signal pulses for one clock cycle when the stream enters a running state to allow a single start to occur. done — done indicates whether the stream is in a non-running state. |
| --- |
| arm start — arm start indicates to the next node whether to arm the Start trigger. This signal pulses for one clock cycle when the stream enters a running state to allow a single start to occur. done — done indicates whether the stream is in a non-running state. |

Parent topic:

Host Transfer

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/fpga/v1/variable-delay-vim.html language=enus -->
## TOPIC 00025: Variable Delay VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/fpga/v1/variable-delay-vim.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/fpga/v1/variable-delay-vim.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies a specified delay to a set of input data. icon Inputs/Outputs cbool.png reset reset resets this VI. Set this to TRUE each time you change delay. cu16.png delay delay specifies the delay in clock cycles. cu16.png maximum delay maximum delay specifies the size of the buffer in the FPGA. c1di16

### Variable Delay VI

Applies a specified delay to a set of input data.

[IMAGE alt='icon' src='variable-delay-vim.png']

#### Inputs/Outputs

| reset — reset resets this VI. Set this to TRUE each time you change delay. delay — delay specifies the delay in clock cycles. maximum delay — maximum delay specifies the size of the buffer in the FPGA. Array in — Array in specifies the input data. data valid — data valid specifies whether input data is valid. Array out — Array out returns the data from Array in delayed by the number of clock cycles specified in delay. data valid? — data valid? specifies whether the output data is valid. debug outputs — — — |
| --- |
| — — |

Parent topic:

Buffering

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1-mnu.html language=enus -->
## TOPIC 00026: NI FlexRIO API v1

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1-mnu.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FlexRIO VIs provide common functionality including streaming, synchronization, clocking configuration, and I/O configuration. You can use the FlexRIO API with the default FPGA image to acquire data with your FlexRIO device without programming to the FPGA. icon

### NI FlexRIO API v1

FlexRIO VIs provide common functionality including streaming, synchronization, clocking configuration, and I/O configuration. You can use the FlexRIO API with the default FPGA image to acquire data with your FlexRIO device without programming to the FPGA.

[IMAGE alt='icon' src='ni-flexrio-api-v1-mnu.png']

- [Get Property Reference VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/get-property-reference-vi.html) Converts an NI-FPGA reference to a FlexRIO-specific class to access FlexRIO properties. Wire this reference to the FlexRIO API Property Nodes to get and set the values of FlexRIO properties.
- [Read IO Module Slots Used VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-io-module-slots-used-vi.html) Returns the number of slots used in the chassis by the IO module. The default value is 1.
- [Write IO Module Slots Used VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-io-module-slots-used-vi.html) Writes to the EEPROM the number of slots used in the chassis by the IO module. The default value is 1.
- [Automotive Vision Utility](../../../../../instr-lib/flexrio/automotive-vision-utility/v1/host/automotive-vision-utility-mnu.html) Common utility VIs for automotive vision applications
- [Open VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/open-vi.html) Opens a session to the specified FlexRIO device using the default FPGA image and creates a session reference you can use to identify this session in subsequent FlexRIO API VI calls. Use Close to dispose of the session reference.
- [Configure Stream VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-stream-vi.html) Configures enabled channels and number of samples in the stream.
- [Start Stream VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/start-stream-vi.html) Activates a stream.
- [Read Stream VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-vi.html) Returns data read from the stream.
- [Write Stream VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-stream-vi.html) Writes data to a specified stream.
- [MergeVI Close VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-close-vi.html) Closes the session, destroys the session reference, and deallocates resources associated with the session. Call this VI once for each unique named session that you have created.
- [Utility](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1utility-mnu.html) Use the Utility VIs for tasks such as signal routing and reading and writing configuration data to the FlexRIO device's flash memory.
- [Configuration](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1configuration-mnu.html) Use the Configuration VIs to configure the reference clock and triggering properties.
- [Stream](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1stream-mnu.html) Use the Stream VIs to configure streaming properties such as enabled channels and the number of samples to transfer.
- [Properties](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1properties-mnu.html) Use the FlexRIO properties to access advanced configuration options.
- [Automotive Vision](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1automotive-vision-mnu.html) Automotive Vision Subpalette.

Parent topic:

FlexRIO with Integrated I/O

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1automotive-vision-mnu.html language=enus -->
## TOPIC 00027: Automotive Vision

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1automotive-vision-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1automotive-vision-mnu.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Automotive Vision Subpalette. icon

### Automotive Vision

Automotive Vision Subpalette.

[IMAGE alt='icon' src='ni-flexrio-api-v1automotive-vision-mnu.png']

- [Wait for PoC Safe to Disconnect VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-poc-safe-to-disconnect-vi.html) Waits and blocks until specified channels with power-over-coax are safe to disconnect. For help on each instance of the polymorphic VI, hover on the polymorphic VI selector.

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1configuration-mnu.html language=enus -->
## TOPIC 00028: Configuration

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1configuration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1configuration-mnu.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Configuration VIs to configure the reference clock and triggering properties. icon

### Configuration

Use the Configuration VIs to configure the reference clock and triggering properties.

[IMAGE alt='icon' src='ni-flexrio-api-v1configuration-mnu.png']

- [Configure Start Trigger VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-start-trigger-vi.html) Configures the start trigger.
- [Configure Clock VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-clock-vi.html) Configures reference and external clock sources.
- [Commit VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/commit-vi.html) Commits property settings to the hardware.

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1i2c-mnu.html language=enus -->
## TOPIC 00029: I2C

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1i2c-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1i2c-mnu.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: icon

### I2C

[IMAGE alt='icon' src='ni-flexrio-api-v1i2c-mnu.png']

- [Read I2C VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-i2c-vi.html) Issues an I2C read to the specified I2C bus instance.
- [Write I2C VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-i2c-vi.html) Issues an I2C write to the specified I2C bus instance.
- [Transfer I2C VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/transfer-i2c-vi.html) Issues an I2C write, without a stop condition, before issuing an I2C read.

Parent topic:

Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1properties-mnu.html language=enus -->
## TOPIC 00030: Properties

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1properties-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1properties-mnu.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FlexRIO properties to access advanced configuration options. icon

### Properties

Use the FlexRIO properties to access advanced configuration options.

[IMAGE alt='icon' src='ni-flexrio-api-v1properties-mnu.png']

- [MergeVI Device Property Node VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-device-property-node-vi.html) Reads and writes FlexRIO device properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference.
- [MergeVI Channel Property Node VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-channel-property-node-vi.html) Reads and writes FlexRIO channel properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference.
- [MergeVI Stream Property Node VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-stream-property-node-vi.html) Reads and writes FlexRIO stream properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference.
- [MergeVI Trigger Property Node VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-trigger-property-node-vi.html) Reads and writes FlexRIO trigger properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference.
- [MergeVI Clock Property Node VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-clock-property-node-vi.html) Reads and writes FlexRIO clock properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference.

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1qsfp-mnu.html language=enus -->
## TOPIC 00031: QSFP

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1qsfp-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1qsfp-mnu.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the QSFP VIs to control and communicate with QSFP modules at the ports. icon

### QSFP

Use the QSFP VIs to control and communicate with QSFP modules at the ports.

[IMAGE alt='icon' src='ni-flexrio-api-v1qsfp-mnu.png']

- [Write QSFP VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-qsfp-vi.html) Writes values to the QSFP+ module connected at the specified port. For address and data information, refer to the SFF-8636 specification.
- [Read QSFP VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-qsfp-vi.html) Returns values for the QSFP+ module connected at the specified port. For address and data information, refer to the SFF-8636 specification.
- [Reset QSFP Ports VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/reset-qsfp-ports-vi.html) Resets the QSFP+ modules connected to all ports.
- [Get QSFP Module Present VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/get-qsfp-module-present-vi.html) Gets the QSFP+ module connection status for the specified port.
- [Enable QSFP Low Power Mode VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/enable-qsfp-low-power-mode-vi.html) Enables low power mode for the QSFP+ modules connected to all ports. True enables low power mode. False enables high power mode.

Parent topic:

Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1stream-mnu.html language=enus -->
## TOPIC 00032: Stream

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1stream-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1stream-mnu.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Stream VIs to configure streaming properties such as enabled channels and the number of samples to transfer. icon

### Stream

Use the Stream VIs to configure streaming properties such as enabled channels and the number of samples to transfer.

[IMAGE alt='icon' src='ni-flexrio-api-v1stream-mnu.png']

- [Clear Stream VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/clear-stream-vi.html) Clears samples from the stream.
- [Configure Stream Finite VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-stream-finite-vi.html) Configures a stream to operate in a finite transfer bound by a specified number of samples. Streams configured to operate in a finite transfer will autonomously stop after completing the requested number of samples or in response to an error state.
- [Configure Stream Enabled Channels VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-stream-enabled-channels-vi.html) Configures which channels are enabled for a specified stream.

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1utility-mnu.html language=enus -->
## TOPIC 00033: Utility

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1utility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1utility-mnu.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Utility VIs for tasks such as signal routing and reading and writing configuration data to the FlexRIO device's flash memory. icon

### Utility

Use the Utility VIs for tasks such as signal routing and reading and writing configuration data to the FlexRIO device's flash memory.

[IMAGE alt='icon' src='ni-flexrio-api-v1utility-mnu.png']

- [Route Signal VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/route-signal-vi.html) Routes a signal from a specified source to a specified destination and returns a route ticket that you can use to identify this route in subsequent VI calls.
- [Unroute Signal VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/unroute-signal-vi.html) Unroutes a signal specified by a route ticket.
- [Wait for IO Ready VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-io-ready-vi.html) Waits and blocks the data flow until the FlexRIO module I/O is ready.
- [Get TClk Session Reference VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/get-tclk-session-reference-vi.html) Returns a reference to the NI-TClk session that can be wired to NI-TClk nodes.
- [Read Calibration Data VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-calibration-data-vi.html) Reads calibration data from the FlexRIO device's on-board flash memory.
- [Write Calibration Data VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-calibration-data-vi.html) Writes calibration data to the FlexRIO device's on-board flash memory.
- [Update Verification Information VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/update-verification-information-vi.html) Updates verification time and verification temperature fields in the device's flash memory to current system time and device temperature, respectively. Use the FlexRIO API Property Node to read the values of these fields.
- [Reset DSP Synchronously VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/reset-dsp-synchronously-vi.html) Asserts DSP Reset on the same rising edge of TClk across all sessions. Use this function to synchronously assert a DSP Reset on multiple TClk synchronized boards on a common rising edge of TClk. This assumes that all boards have already been synchronized via a call to niTClk_Synchronize. Use this function in combination with the TClk Synchronized DSP Reset FPGA VI.
- [Start CableSense Signal VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/start-cablesense-signal-vi.html) Generates the CableSense signal on all channels for which the signal is enabled on your compatible FlexRIO module, as configured by the CableSense Mode property.
- [Stop CableSense Signal VI](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/stop-cablesense-signal-vi.html) Disables the CableSense signal on all channels for which the signal is enabled on your compatible FlexRIO module.
- [QSFP](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1qsfp-mnu.html) Use the QSFP VIs to control and communicate with QSFP modules at the ports.
- [I2C](../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio-api-v1i2c-mnu.html)

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/clear-stream-vi.html language=enus -->
## TOPIC 00034: Clear Stream VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/clear-stream-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/clear-stream-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears samples from the stream. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cu32.png stream instance stream instance identifies an instance of a stream. cerrcodeclst.png error in error in describes error con

### Clear Stream VI

Clears samples from the stream.

[IMAGE alt='icon' src='clear-stream-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. stream instance — stream instance identifies an instance of a stream. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. stream instance out — stream instance out returns a copy of stream number. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Stream

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/commit-vi.html language=enus -->
## TOPIC 00035: Commit VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/commit-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/commit-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits property settings to the hardware. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cerrcodeclst.png error in error in describes error conditions that occur before this node runs. This input provides stan

### Commit VI

Commits property settings to the hardware.

[IMAGE alt='icon' src='commit-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-analog-start-trigger-vi.html language=enus -->
## TOPIC 00036: Configure Analog Start Trigger VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-analog-start-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-analog-start-trigger-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start trigger for analog edge triggering. icon Inputs/Outputs cbool.png rising edge? rising edge? specifies whether to trigger on a rising edge. If this value is FALSE, this VI will configure the device to trigger on a falling edge. cdbl.png hysteresis hysteresis specifies the size of

### Configure Analog Start Trigger VI

Configures the Start trigger for analog edge triggering.

[IMAGE alt='icon' src='configure-analog-start-trigger-vi.png']

#### Inputs/Outputs

| rising edge? — rising edge? specifies whether to trigger on a rising edge. If this value is FALSE, this VI will configure the device to trigger on a falling edge. hysteresis — hysteresis specifies the size of the hysteresis window on either side of level in volts. level — level specifies the trigger level in volts. fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. trigger instance — trigger instance specifies an instance of a trigger. channel — channel specifies the channel to monitor for trigger conditions. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. trigger instance out — trigger instance out returns a copy of trigger instance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Start Trigger VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-clock-vi.html language=enus -->
## TOPIC 00037: Configure Clock VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-clock-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-clock-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures reference and external clock sources. icon

### Configure Clock VI

Configures reference and external clock sources.

[IMAGE alt='icon' src='configure-clock-vi.png']

- [Configure Reference Clock VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-reference-clock-vi.html) Configures the Reference Clock source. You can use this VI to set the onboard clock, the PXI backplane clock, or an external clock as the Reference Clock.
- [Configure External Clock VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-external-clock-vi.html) Configures external clock source and frequency.

Parent topic:

Configuration

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-digital-edge-start-trigger-vi.html language=enus -->
## TOPIC 00038: Configure Digital Edge Start Trigger VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-digital-edge-start-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-digital-edge-start-trigger-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start trigger for digital edge triggering. icon Inputs/Outputs cbool.png rising edge? rising edge? specifies whether to trigger on a rising edge. If this value is FALSE, this VI will configure the device to trigger on a falling edge. cgenclassrn.png fpga interface in fpga interface in

### Configure Digital Edge Start Trigger VI

Configures the Start trigger for digital edge triggering.

[IMAGE alt='icon' src='configure-digital-edge-start-trigger-vi.png']

#### Inputs/Outputs

| rising edge? — rising edge? specifies whether to trigger on a rising edge. If this value is FALSE, this VI will configure the device to trigger on a falling edge. fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. trigger instance — trigger instance specifies an instance of a trigger. trigger source — Specifies the trigger source. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. trigger instance out — trigger instance out returns a copy of trigger instance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Start Trigger VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-digital-level-start-trigger-vi.html language=enus -->
## TOPIC 00039: Configure Digital Level Start Trigger VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-digital-level-start-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-digital-level-start-trigger-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to trigger on a high or low level of a digital signal. icon Inputs/Outputs cbool.png high level? high level? specifies whether to trigger on a high level. Set this value to FALSE to trigger on a low level. cgenclassrn.png fpga interface in fpga interface in specifies the refere

### Configure Digital Level Start Trigger VI

Configures the device to trigger on a high or low level of a digital signal.

[IMAGE alt='icon' src='configure-digital-level-start-trigger-vi.png']

#### Inputs/Outputs

| high level? — high level? specifies whether to trigger on a high level. Set this value to FALSE to trigger on a low level. fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. trigger instance — trigger instance specifies an instance of a trigger. trigger source — Specifies the trigger source. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. trigger instance out — trigger instance out returns a copy of trigger instance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Start Trigger VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-external-clock-vi.html language=enus -->
## TOPIC 00040: Configure External Clock VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-external-clock-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-external-clock-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures external clock source and frequency. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. ci32.png clock source clock source identifies the source of the external Sample Clock. cdbl.png frequency frequency

### Configure External Clock VI

Configures external clock source and frequency.

[IMAGE alt='icon' src='configure-external-clock-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. clock source — clock source identifies the source of the external Sample Clock. frequency — frequency specifies the frequency of the external sample clock. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Clock VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-immediate-start-trigger-vi.html language=enus -->
## TOPIC 00041: Configure Immediate Start Trigger VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-immediate-start-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-immediate-start-trigger-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to trigger itself immediately and independently of external signals. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cu32.png trigger instance trigger instance specifies an instance of a tr

### Configure Immediate Start Trigger VI

Configures the device to trigger itself immediately and independently of external signals.

[IMAGE alt='icon' src='configure-immediate-start-trigger-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. trigger instance — trigger instance specifies an instance of a trigger. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. trigger instance out — trigger instance out returns a copy of trigger instance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Start Trigger VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-reference-clock-vi.html language=enus -->
## TOPIC 00042: Configure Reference Clock VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-reference-clock-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-reference-clock-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference Clock source. You can use this VI to set the onboard clock, the PXI backplane clock, or an external clock as the Reference Clock. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. ci32.png

### Configure Reference Clock VI

Configures the Reference Clock source. You can use this VI to set the onboard clock, the PXI backplane clock, or an external clock as the Reference Clock.

[IMAGE alt='icon' src='configure-reference-clock-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. reference clock source — reference clock source specifies the Reference Clock source. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Clock VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-start-trigger-vi.html language=enus -->
## TOPIC 00043: Configure Start Trigger VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-start-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-start-trigger-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the start trigger. icon

### Configure Start Trigger VI

Configures the start trigger.

[IMAGE alt='icon' src='configure-start-trigger-vi.png']

- [Configure Immediate Start Trigger VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-immediate-start-trigger-vi.html) Configures the device to trigger itself immediately and independently of external signals.
- [Configure Analog Start Trigger VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-analog-start-trigger-vi.html) Configures the Start trigger for analog edge triggering.
- [Configure Digital Edge Start Trigger VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-digital-edge-start-trigger-vi.html) Configures the Start trigger for digital edge triggering.
- [Configure Digital Level Start Trigger VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-digital-level-start-trigger-vi.html) Configures the device to trigger on a high or low level of a digital signal.

Parent topic:

Configuration

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-stream-enabled-channels-vi.html language=enus -->
## TOPIC 00044: Configure Stream Enabled Channels VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-stream-enabled-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-stream-enabled-channels-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures which channels are enabled for a specified stream. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cu32.png stream instance stream instance identifies an instance of a stream. cstr.png channels enable

### Configure Stream Enabled Channels VI

Configures which channels are enabled for a specified stream.

[IMAGE alt='icon' src='configure-stream-enabled-channels-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. stream instance — stream instance identifies an instance of a stream. channels enabled — channels enabled specifies the channels to enable for the specified stream. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. stream instance out — stream instance out returns a copy of stream number. channel count — channel count indicates the total number of channels parsed. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Stream

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-stream-finite-vi.html language=enus -->
## TOPIC 00045: Configure Stream Finite VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-stream-finite-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-stream-finite-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a stream to operate in a finite transfer bound by a specified number of samples. Streams configured to operate in a finite transfer will autonomously stop after completing the requested number of samples or in response to an error state. icon Inputs/Outputs cgenclassrn.png fpga interface

### Configure Stream Finite VI

Configures a stream to operate in a finite transfer bound by a specified number of samples. Streams configured to operate in a finite transfer will autonomously stop after completing the requested number of samples or in response to an error state.

[IMAGE alt='icon' src='configure-stream-finite-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. stream instance — stream instance identifies an instance of a stream. num samples — num samples specifies the maximum number of samples to transfer. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. stream instance out — stream instance out returns a copy of stream number. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Stream

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-stream-vi.html language=enus -->
## TOPIC 00046: Configure Stream VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-stream-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/configure-stream-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures enabled channels and number of samples in the stream. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cu32.png stream instance stream instance identifies an instance of a stream. cstr.png channels ena

### Configure Stream VI

Configures enabled channels and number of samples in the stream.

[IMAGE alt='icon' src='configure-stream-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. stream instance — stream instance identifies an instance of a stream. channels enabled — channels enabled specifies the channels to enable for the specified stream. num samples — num samples specifies the maximum number of samples to transfer. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. stream instance out — stream instance out returns a copy of stream number. channel count — channel count indicates the total number of channels parsed. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/enable-qsfp-low-power-mode-vi.html language=enus -->
## TOPIC 00047: Enable QSFP Low Power Mode VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/enable-qsfp-low-power-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/enable-qsfp-low-power-mode-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables low power mode for the QSFP+ modules connected to all ports. True enables low power mode. False enables high power mode. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cbool.png enable enable enables lo

### Enable QSFP Low Power Mode VI

Enables low power mode for the QSFP+ modules connected to all ports. True enables low power mode. False enables high power mode.

[IMAGE alt='icon' src='enable-qsfp-low-power-mode-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. enable — enable enables low power mode for the QSFP+ modules connected to both Port 0 and Port 1. Choose true to enable low power mode. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

QSFP

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/get-property-reference-vi.html language=enus -->
## TOPIC 00048: Get Property Reference VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/get-property-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/get-property-reference-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an NI-FPGA reference to a FlexRIO-specific class to access FlexRIO properties. Wire this reference to the FlexRIO API Property Nodes to get and set the values of FlexRIO properties. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on

### Get Property Reference VI

Converts an NI-FPGA reference to a FlexRIO-specific class to access FlexRIO properties. Wire this reference to the FlexRIO API Property Nodes to get and set the values of FlexRIO properties.

[IMAGE alt='icon' src='get-property-reference-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. property reference — is the reference to the FlexRIO properties. Wire this output into the reference terminal of the FlexRIO property nodes. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/get-qsfp-module-present-vi.html language=enus -->
## TOPIC 00049: Get QSFP Module Present VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/get-qsfp-module-present-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/get-qsfp-module-present-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the QSFP+ module connection status for the specified port. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cu8.png port port specifies the port, 0 or 1, from which the VI reads QSFP+ module data. cerrcodecl

### Get QSFP Module Present VI

Gets the QSFP+ module connection status for the specified port.

[IMAGE alt='icon' src='get-qsfp-module-present-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. port — port specifies the port, 0 or 1, from which the VI reads QSFP+ module data. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. module present — error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

QSFP

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/get-tclk-session-reference-vi.html language=enus -->
## TOPIC 00050: Get TClk Session Reference VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/get-tclk-session-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/get-tclk-session-reference-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a reference to the NI-TClk session that can be wired to NI-TClk nodes. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cerrcodeclst.png error in error in describes error conditions that occur before this

### Get TClk Session Reference VI

Returns a reference to the NI-TClk session that can be wired to NI-TClk nodes.

[IMAGE alt='icon' src='get-tclk-session-reference-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. tclk session reference — returns a reference to the TClk session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-channel-property-node-vi.html language=enus -->
## TOPIC 00051: MergeVI Channel Property Node VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-channel-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-channel-property-node-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads and writes FlexRIO channel properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference. Right-click on the property to select a differen

### MergeVI Channel Property Node VI

Reads and writes FlexRIO channel properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference.

Right-click on the property to select a different property or to switch between reading and writing operations.

[IMAGE alt='icon' src='mergevi-channel-property-node-vi.png']

Parent topic:

Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-clock-property-node-vi.html language=enus -->
## TOPIC 00052: MergeVI Clock Property Node VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-clock-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-clock-property-node-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads and writes FlexRIO clock properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference. Right-click on the property to select a different

### MergeVI Clock Property Node VI

Reads and writes FlexRIO clock properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference.

Right-click on the property to select a different property or to switch between reading and writing operations.

[IMAGE alt='icon' src='mergevi-clock-property-node-vi.png']

Parent topic:

Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-close-vi.html language=enus -->
## TOPIC 00053: MergeVI Close VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-close-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-close-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session, destroys the session reference, and deallocates resources associated with the session. Call this VI once for each unique named session that you have created. icon Inputs/Outputs cpoly.png FPGA VI Reference In cerrcodeclst.png error in error in describes error conditions that occu

### MergeVI Close VI

Closes the session, destroys the session reference, and deallocates resources associated with the session. Call this VI once for each unique named session that you have created.

[IMAGE alt='icon' src='mergevi-close-vi.png']

#### Inputs/Outputs

| FPGA VI Reference In — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-device-property-node-vi.html language=enus -->
## TOPIC 00054: MergeVI Device Property Node VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-device-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-device-property-node-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads and writes FlexRIO device properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference. Right-click on the property to select a different

### MergeVI Device Property Node VI

Reads and writes FlexRIO device properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference.

Right-click on the property to select a different property or to switch between reading and writing operations.

[IMAGE alt='icon' src='mergevi-device-property-node-vi.png']

Parent topic:

Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-stream-property-node-vi.html language=enus -->
## TOPIC 00055: MergeVI Stream Property Node VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-stream-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-stream-property-node-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads and writes FlexRIO stream properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference. Right-click on the property to select a different

### MergeVI Stream Property Node VI

Reads and writes FlexRIO stream properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference.

Right-click on the property to select a different property or to switch between reading and writing operations.

[IMAGE alt='icon' src='mergevi-stream-property-node-vi.png']

Parent topic:

Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-trigger-property-node-vi.html language=enus -->
## TOPIC 00056: MergeVI Trigger Property Node VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-trigger-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/mergevi-trigger-property-node-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads and writes FlexRIO trigger properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference. Right-click on the property to select a differen

### MergeVI Trigger Property Node VI

Reads and writes FlexRIO trigger properties. When placed on the diagram from the FlexRIO API palette, this Property Node is automatically connected to Get Property Reference to facilitate converting an NI-FPGA reference to a FlexRIO session reference.

Right-click on the property to select a different property or to switch between reading and writing operations.

[IMAGE alt='icon' src='mergevi-trigger-property-node-vi.png']

Parent topic:

Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-calibration-data-vi.html language=enus -->
## TOPIC 00057: Read Calibration Data VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-calibration-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-calibration-data-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads calibration data from the FlexRIO device's on-board flash memory. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cu32.png offset offset specifies the byte address in the device's flash memory at which to

### Read Calibration Data VI

Reads calibration data from the FlexRIO device's on-board flash memory.

[IMAGE alt='icon' src='read-calibration-data-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. offset — offset specifies the byte address in the device's flash memory at which to begin the operation. size — size defines the number of bytes to read from the device's flash memory. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. data — data returns the data read from the device's flash memory. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-i2c-vi.html language=enus -->
## TOPIC 00058: Read I2C VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-i2c-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-i2c-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Issues an I2C read to the specified I2C bus instance. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cstr.png bus instance name specifies the I2C bus instance to which the read should be issued. cu16.png slave

### Read I2C VI

Issues an I2C read to the specified I2C bus instance.

[IMAGE alt='icon' src='read-i2c-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. bus instance name — specifies the I2C bus instance to which the read should be issued. slave address — slave address specifies the I2C slave address of the device to which the read should be issued. num bytes to read — num bytes to read specifies the number of bytes to be read. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. repeated start (f) — fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. data — data returns the data read from the I2C bus. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

I2C

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-io-module-slots-used-vi.html language=enus -->
## TOPIC 00059: Read IO Module Slots Used VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-io-module-slots-used-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-io-module-slots-used-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of slots used in the chassis by the IO module. The default value is 1. icon Inputs/Outputs cgenclassrn.png FPGA VI Reference In cerrcodeclst.png error in (no error) error in can accept error information wired from VIs previously called. Use this information to decide if any functi

### Read IO Module Slots Used VI

Returns the number of slots used in the chassis by the IO module. The default value is 1.

[IMAGE alt='icon' src='read-io-module-slots-used-vi.png']

#### Inputs/Outputs

| FPGA VI Reference In — error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FPGA VI Reference Out — slotsUsed — indicates the number of slots used in the chassis by the IO module. The default value is 1. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-qsfp-vi.html language=enus -->
## TOPIC 00060: Read QSFP VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-qsfp-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-qsfp-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns values for the QSFP+ module connected at the specified port. For address and data information, refer to the SFF-8636 specification. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cu8.png port port speci

### Read QSFP VI

Returns values for the QSFP+ module connected at the specified port. For address and data information, refer to the SFF-8636 specification.

[IMAGE alt='icon' src='read-qsfp-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. port — port specifies the port, 0 or 1, from which the VI reads QSFP+ module data. address — address specifies the address on the QSFP+ module. For address and data information, refer to the SFF-8636 specification. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. data — data specifies data read from an address on the QSFP+ module. For address and data information, refer to the SFF-8636 specification. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

QSFP

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-1d-f64-vi.html language=enus -->
## TOPIC 00061: Read Stream 1D F64 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-1d-f64-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-1d-f64-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns data read from a specified stream. icon Inputs/Outputs ci32.png timeout timeout specifies a time limit in milliseconds after which the VI will stop attempting to read data from the stream. cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Inter

### Read Stream 1D F64 VI

Returns data read from a specified stream.

[IMAGE alt='icon' src='read-stream-1d-f64-vi.png']

#### Inputs/Outputs

| timeout — timeout specifies a time limit in milliseconds after which the VI will stop attempting to read data from the stream. fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. stream instance — stream instance identifies an instance of a stream. samples — samples specifies the number of samples to read from the stream. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. stream instance out — stream instance out returns a copy of stream number. read data — read data returns data read from the stream. wfm info — wfm info returns information about waveforms read from the stream. absoluteInitialXUpper — returns the upper 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. absoluteInitialXLower — returns the lower 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. relativeInitialX — returns a timestamp that represents the time offset of the first sample from a reference point. The reference point is typically the start of the waveform. dt — indicates the time between two points. If the driver is unable to determine the dt, this value will be 0. gain — indicates the gain applied to the signal. offset — indicates the offset applied to the signal. reserved 1 — is a reserved field. Do not use. reserved 2 — is a reserved field. Do not use. # of elements — returns the number of elements in the waveform. reserved 3 — is a reserved field. Do not use. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| absoluteInitialXUpper — returns the upper 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. absoluteInitialXLower — returns the lower 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. relativeInitialX — returns a timestamp that represents the time offset of the first sample from a reference point. The reference point is typically the start of the waveform. dt — indicates the time between two points. If the driver is unable to determine the dt, this value will be 0. gain — indicates the gain applied to the signal. offset — indicates the offset applied to the signal. reserved 1 — is a reserved field. Do not use. reserved 2 — is a reserved field. Do not use. # of elements — returns the number of elements in the waveform. reserved 3 — is a reserved field. Do not use. |

Parent topic:

Read Stream VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-1d-i16-vi.html language=enus -->
## TOPIC 00062: Read Stream 1D I16 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-1d-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-1d-i16-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns data read from a specified stream. icon Inputs/Outputs ci32.png timeout timeout specifies a time limit in milliseconds after which the VI will stop attempting to read data from the stream. cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Inter

### Read Stream 1D I16 VI

Returns data read from a specified stream.

[IMAGE alt='icon' src='read-stream-1d-i16-vi.png']

#### Inputs/Outputs

| timeout — timeout specifies a time limit in milliseconds after which the VI will stop attempting to read data from the stream. fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. stream instance — stream instance identifies an instance of a stream. samples — samples specifies the number of samples to read from the stream. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. stream instance out — stream instance out returns a copy of stream number. read data — read data returns data read from the stream. wfm info — wfm info returns information about waveforms read from the stream. absoluteInitialXUpper — returns the upper 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. absoluteInitialXLower — returns the lower 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. relativeInitialX — returns a timestamp that represents the time offset of the first sample from a reference point. The reference point is typically the start of the waveform. dt — indicates the time between two points. If the driver is unable to determine the dt, this value will be 0. gain — indicates the gain applied to the signal. offset — indicates the offset applied to the signal. reserved 1 — is a reserved field. Do not use. reserved 2 — is a reserved field. Do not use. # of elements — returns the number of elements in the waveform. reserved 3 — is a reserved field. Do not use. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| absoluteInitialXUpper — returns the upper 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. absoluteInitialXLower — returns the lower 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. relativeInitialX — returns a timestamp that represents the time offset of the first sample from a reference point. The reference point is typically the start of the waveform. dt — indicates the time between two points. If the driver is unable to determine the dt, this value will be 0. gain — indicates the gain applied to the signal. offset — indicates the offset applied to the signal. reserved 1 — is a reserved field. Do not use. reserved 2 — is a reserved field. Do not use. # of elements — returns the number of elements in the waveform. reserved 3 — is a reserved field. Do not use. |

Parent topic:

Read Stream VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-1d-wdt-vi.html language=enus -->
## TOPIC 00063: Read Stream 1D WDT VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-1d-wdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-1d-wdt-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns data read from a specified stream. icon Inputs/Outputs ci32.png timeout timeout specifies a time limit in milliseconds after which the VI will stop attempting to read data from the stream. cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Inter

### Read Stream 1D WDT VI

Returns data read from a specified stream.

[IMAGE alt='icon' src='read-stream-1d-wdt-vi.png']

#### Inputs/Outputs

| timeout — timeout specifies a time limit in milliseconds after which the VI will stop attempting to read data from the stream. fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. stream instance — stream instance identifies an instance of a stream. samples — samples specifies the number of samples to read from the stream. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. stream instance out — stream instance out returns a copy of stream number. read data — read data returns data read from the stream. wfm info — wfm info returns information about waveforms read from the stream. absoluteInitialXUpper — returns the upper 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. absoluteInitialXLower — returns the lower 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. relativeInitialX — returns a timestamp that represents the time offset of the first sample from a reference point. The reference point is typically the start of the waveform. dt — indicates the time between two points. If the driver is unable to determine the dt, this value will be 0. gain — indicates the gain applied to the signal. offset — indicates the offset applied to the signal. reserved 1 — is a reserved field. Do not use. reserved 2 — is a reserved field. Do not use. # of elements — returns the number of elements in the waveform. reserved 3 — is a reserved field. Do not use. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| absoluteInitialXUpper — returns the upper 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. absoluteInitialXLower — returns the lower 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. relativeInitialX — returns a timestamp that represents the time offset of the first sample from a reference point. The reference point is typically the start of the waveform. dt — indicates the time between two points. If the driver is unable to determine the dt, this value will be 0. gain — indicates the gain applied to the signal. offset — indicates the offset applied to the signal. reserved 1 — is a reserved field. Do not use. reserved 2 — is a reserved field. Do not use. # of elements — returns the number of elements in the waveform. reserved 3 — is a reserved field. Do not use. |

Parent topic:

Read Stream VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-2d-f64-vi.html language=enus -->
## TOPIC 00064: Read Stream 2D F64 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-2d-f64-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-2d-f64-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns data read from a specified stream. icon Inputs/Outputs ci32.png timeout timeout specifies a time limit in milliseconds after which the VI will stop attempting to read data from the stream. cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Inter

### Read Stream 2D F64 VI

Returns data read from a specified stream.

[IMAGE alt='icon' src='read-stream-2d-f64-vi.png']

#### Inputs/Outputs

| timeout — timeout specifies a time limit in milliseconds after which the VI will stop attempting to read data from the stream. fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. stream instance — stream instance identifies an instance of a stream. samples — samples specifies the number of samples to read from the stream. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. stream instance out — stream instance out returns a copy of stream number. read data — read data returns data read from the stream. wfm info — wfm info returns information about waveforms read from the stream. absoluteInitialXUpper — returns the upper 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. absoluteInitialXLower — returns the lower 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. relativeInitialX — returns a timestamp that represents the time offset of the first sample from a reference point. The reference point is typically the start of the waveform. dt — indicates the time between two points. If the driver is unable to determine the dt, this value will be 0. gain — indicates the gain applied to the signal. offset — indicates the offset applied to the signal. reserved 1 — is a reserved field. Do not use. reserved 2 — is a reserved field. Do not use. # of elements — returns the number of elements in the waveform. reserved 3 — is a reserved field. Do not use. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| absoluteInitialXUpper — returns the upper 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. absoluteInitialXLower — returns the lower 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. relativeInitialX — returns a timestamp that represents the time offset of the first sample from a reference point. The reference point is typically the start of the waveform. dt — indicates the time between two points. If the driver is unable to determine the dt, this value will be 0. gain — indicates the gain applied to the signal. offset — indicates the offset applied to the signal. reserved 1 — is a reserved field. Do not use. reserved 2 — is a reserved field. Do not use. # of elements — returns the number of elements in the waveform. reserved 3 — is a reserved field. Do not use. |

Parent topic:

Read Stream VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-2d-i16-vi.html language=enus -->
## TOPIC 00065: Read Stream 2D I16 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-2d-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-2d-i16-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns data read from a specified stream. icon Inputs/Outputs ci32.png timeout timeout specifies a time limit in milliseconds after which the VI will stop attempting to read data from the stream. cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Inter

### Read Stream 2D I16 VI

Returns data read from a specified stream.

[IMAGE alt='icon' src='read-stream-2d-i16-vi.png']

#### Inputs/Outputs

| timeout — timeout specifies a time limit in milliseconds after which the VI will stop attempting to read data from the stream. fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. stream instance — stream instance identifies an instance of a stream. samples — samples specifies the number of samples to read from the stream. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. stream instance out — stream instance out returns a copy of stream number. read data — read data returns data read from the stream. wfm info — wfm info returns information about waveforms read from the stream. absoluteInitialXUpper — returns the upper 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. absoluteInitialXLower — returns the lower 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. relativeInitialX — returns a timestamp that represents the time offset of the first sample from a reference point. The reference point is typically the start of the waveform. dt — indicates the time between two points. If the driver is unable to determine the dt, this value will be 0. gain — indicates the gain applied to the signal. offset — indicates the offset applied to the signal. reserved 1 — is a reserved field. Do not use. reserved 2 — is a reserved field. Do not use. # of elements — returns the number of elements in the waveform. reserved 3 — is a reserved field. Do not use. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| absoluteInitialXUpper — returns the upper 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. absoluteInitialXLower — returns the lower 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. relativeInitialX — returns a timestamp that represents the time offset of the first sample from a reference point. The reference point is typically the start of the waveform. dt — indicates the time between two points. If the driver is unable to determine the dt, this value will be 0. gain — indicates the gain applied to the signal. offset — indicates the offset applied to the signal. reserved 1 — is a reserved field. Do not use. reserved 2 — is a reserved field. Do not use. # of elements — returns the number of elements in the waveform. reserved 3 — is a reserved field. Do not use. |

Parent topic:

Read Stream VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-vi.html language=enus -->
## TOPIC 00066: Read Stream VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns data read from the stream. icon

### Read Stream VI

Returns data read from the stream.

[IMAGE alt='icon' src='read-stream-vi.png']

- [Read Stream 1D I16 VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-1d-i16-vi.html) Returns data read from a specified stream.
- [Read Stream 1D F64 VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-1d-f64-vi.html) Returns data read from a specified stream.
- [Read Stream WDT VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-wdt-vi.html) Returns data read from a specified stream.
- [Read Stream 2D I16 VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-2d-i16-vi.html) Returns data read from a specified stream.
- [Read Stream 2D F64 VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-2d-f64-vi.html) Returns data read from a specified stream.
- [Read Stream 1D WDT VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-1d-wdt-vi.html) Returns data read from a specified stream.

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-wdt-vi.html language=enus -->
## TOPIC 00067: Read Stream WDT VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-wdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/read-stream-wdt-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns data read from a specified stream. icon Inputs/Outputs ci32.png timeout timeout specifies a time limit in milliseconds after which the VI will stop attempting to read data from the stream. cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Inter

### Read Stream WDT VI

Returns data read from a specified stream.

[IMAGE alt='icon' src='read-stream-wdt-vi.png']

#### Inputs/Outputs

| timeout — timeout specifies a time limit in milliseconds after which the VI will stop attempting to read data from the stream. fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. stream instance — stream instance identifies an instance of a stream. samples — samples specifies the number of samples to read from the stream. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. stream instance out — stream instance out returns a copy of stream number. read data — read data returns data read from the stream. wfm info — wfm info returns information about waveforms read from the stream. absoluteInitialXUpper — returns the upper 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. absoluteInitialXLower — returns the lower 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. relativeInitialX — returns a timestamp that represents the time offset of the first sample from a reference point. The reference point is typically the start of the waveform. dt — indicates the time between two points. If the driver is unable to determine the dt, this value will be 0. gain — indicates the gain applied to the signal. offset — indicates the offset applied to the signal. reserved 1 — is a reserved field. Do not use. reserved 2 — is a reserved field. Do not use. # of elements — returns the number of elements in the waveform. reserved 3 — is a reserved field. Do not use. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| absoluteInitialXUpper — returns the upper 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. absoluteInitialXLower — returns the lower 64 bits of a timestamp that represents the time offset of the first sample from an arbitrary starting point. The actual time is the sum of absoluteInitialXUpper and absoluteInitialXLower. This timestamp can be used to compare times across streaming acquisitions as long as the clock is not reconfigured between acquisitions. relativeInitialX — returns a timestamp that represents the time offset of the first sample from a reference point. The reference point is typically the start of the waveform. dt — indicates the time between two points. If the driver is unable to determine the dt, this value will be 0. gain — indicates the gain applied to the signal. offset — indicates the offset applied to the signal. reserved 1 — is a reserved field. Do not use. reserved 2 — is a reserved field. Do not use. # of elements — returns the number of elements in the waveform. reserved 3 — is a reserved field. Do not use. |

Parent topic:

Read Stream VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/reset-dsp-synchronously-vi.html language=enus -->
## TOPIC 00068: Reset DSP Synchronously VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/reset-dsp-synchronously-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/reset-dsp-synchronously-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asserts DSP Reset on the same rising edge of TClk across all sessions. Use this function to synchronously assert a DSP Reset on multiple TClk synchronized boards on a common rising edge of TClk. This assumes that all boards have already been synchronized via a call to niTClk_Synchronize. Use this fu

### Reset DSP Synchronously VI

Asserts DSP Reset on the same rising edge of TClk across all sessions. Use this function to synchronously assert a DSP Reset on multiple TClk synchronized boards on a common rising edge of TClk. This assumes that all boards have already been synchronized via a call to niTClk_Synchronize. Use this function in combination with the TClk Synchronized DSP Reset FPGA VI.

[IMAGE alt='icon' src='reset-dsp-synchronously-vi.png']

#### Inputs/Outputs

| fpga interfaces in — fpga interfaces in instance — instance error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interfaces out — error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/reset-qsfp-ports-vi.html language=enus -->
## TOPIC 00069: Reset QSFP Ports VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/reset-qsfp-ports-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/reset-qsfp-ports-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the QSFP+ modules connected to all ports. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cerrcodeclst.png error in error in describes error conditions that occur before this node runs. This input provide

### Reset QSFP Ports VI

Resets the QSFP+ modules connected to all ports.

[IMAGE alt='icon' src='reset-qsfp-ports-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

QSFP

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/route-signal-vi.html language=enus -->
## TOPIC 00070: Route Signal VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/route-signal-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/route-signal-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes a signal from a specified source to a specified destination and returns a route ticket that you can use to identify this route in subsequent VI calls. Routes created by this VI exist until the session that created the route is closed, Unroute Signal is called on the route's route ticket, or a

### Route Signal VI

Routes a signal from a specified source to a specified destination and returns a route ticket that you can use to identify this route in subsequent VI calls.

Routes created by this VI exist until the session that created the route is closed, Unroute Signal is called on the route's route ticket, or a device involved in the route is reset.

[IMAGE alt='icon' src='route-signal-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. source — source specifies the source of the signal to route. destination — destination specifies the destination to which to route the signal. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. route ticket — route ticket identifies a signal route. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/start-cablesense-signal-vi.html language=enus -->
## TOPIC 00071: Start CableSense Signal VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/start-cablesense-signal-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/start-cablesense-signal-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates the CableSense signal on all channels for which the signal is enabled on your compatible FlexRIO module, as configured by the CableSense Mode property. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. c

### Start CableSense Signal VI

Generates the CableSense signal on all channels for which the signal is enabled on your compatible FlexRIO module, as configured by the CableSense Mode property.

[IMAGE alt='icon' src='start-cablesense-signal-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — returns a reference to the VI on the FPGA Interface palette. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/start-stream-vi.html language=enus -->
## TOPIC 00072: Start Stream VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/start-stream-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/start-stream-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Activates a stream. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cu32.png stream instance stream instance identifies an instance of a stream. cerrcodeclst.png error in error in describes error conditions that

### Start Stream VI

Activates a stream.

[IMAGE alt='icon' src='start-stream-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. stream instance — stream instance identifies an instance of a stream. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. stream instance out — stream instance out returns a copy of stream number. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/stop-cablesense-signal-vi.html language=enus -->
## TOPIC 00073: Stop CableSense Signal VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/stop-cablesense-signal-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/stop-cablesense-signal-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the CableSense signal on all channels for which the signal is enabled on your compatible FlexRIO module. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cerrcodeclst.png error in error in describes erro

### Stop CableSense Signal VI

Disables the CableSense signal on all channels for which the signal is enabled on your compatible FlexRIO module.

[IMAGE alt='icon' src='stop-cablesense-signal-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — returns a reference to the VI on the FPGA Interface palette. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/transfer-i2c-vi.html language=enus -->
## TOPIC 00074: Transfer I2C VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/transfer-i2c-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/transfer-i2c-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Issues an I2C write, without a stop condition, before issuing an I2C read. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cstr.png bus instance name specifies the I2C bus instance to which the read should be is

### Transfer I2C VI

Issues an I2C write, without a stop condition, before issuing an I2C read.

[IMAGE alt='icon' src='transfer-i2c-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. bus instance name — specifies the I2C bus instance to which the read should be issued. slave address — slave address specifies the I2C slave address of the device to which the read should be issued. write data — write data specifies the data to write to the I2C bus. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. num bytes to read — num bytes to read specifies the number of bytes to be read. repeated start (f) — fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. read data — read data returns the data read from the I2C bus. num bytes written — num bytes written returns the number of bytes written. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

I2C

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/unroute-signal-vi.html language=enus -->
## TOPIC 00075: Unroute Signal VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/unroute-signal-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/unroute-signal-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unroutes a signal specified by a route ticket. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cu32.png route ticket route ticket identifies a signal route. The route ticket originates from Route Signal. cerrcod

### Unroute Signal VI

Unroutes a signal specified by a route ticket.

[IMAGE alt='icon' src='unroute-signal-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. route ticket — route ticket identifies a signal route. The route ticket originates from Route Signal. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/update-verification-information-vi.html language=enus -->
## TOPIC 00076: Update Verification Information VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/update-verification-information-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/update-verification-information-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates verification time and verification temperature fields in the device's flash memory to current system time and device temperature, respectively. Use the FlexRIO API Property Node to read the values of these fields. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specif

### Update Verification Information VI

Updates verification time and verification temperature fields in the device's flash memory to current system time and device temperature, respectively. Use the FlexRIO API Property Node to read the values of these fields.

[IMAGE alt='icon' src='update-verification-information-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-io-ready-vi.html language=enus -->
## TOPIC 00077: Wait for IO Ready VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-io-ready-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-io-ready-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks the data flow until the FlexRIO module I/O is ready. icon Inputs/Outputs ci32.png timeout timeout specifies a time limit in milliseconds after which the VI will stop attempting to read data from the stream. cgenclassrn.png fpga interface in fpga interface in specifies the reference

### Wait for IO Ready VI

Waits and blocks the data flow until the FlexRIO module I/O is ready.

[IMAGE alt='icon' src='wait-for-io-ready-vi.png']

#### Inputs/Outputs

| timeout — timeout specifies a time limit in milliseconds after which the VI will stop attempting to read data from the stream. fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. io error — io error outputs error codes that indicate why the I/O module is not ready. io ready — io ready informs the next node that the I/O is ready. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-poc-safe-to-disconnect-channels-array-vi.html language=enus -->
## TOPIC 00078: Wait for PoC Safe to Disconnect Channels Array VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-poc-safe-to-disconnect-channels-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-poc-safe-to-disconnect-channels-array-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks until specified channels with power-over-coax are safe to disconnect. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. c1dstr.png Channels Channels specifies the channels to wait until safe to di

### Wait for PoC Safe to Disconnect Channels Array VI

Waits and blocks until specified channels with power-over-coax are safe to disconnect.

[IMAGE alt='icon' src='wait-for-poc-safe-to-disconnect-channels-array-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. Channels — Channels specifies the channels to wait until safe to disconnect. Each element of the array is a single channel such as "SI0", "SO2", etc. Timeout (ms) — Timeout (ms) specifies a time limit in milliseconds to wait until safe to disconnect. A value of -1 indicates to wait indefinitely error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Wait for PoC Safe to Disconnect VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-poc-safe-to-disconnect-channels-string-vi.html language=enus -->
## TOPIC 00079: Wait for PoC Safe to Disconnect Channels String VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-poc-safe-to-disconnect-channels-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-poc-safe-to-disconnect-channels-string-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks until specified channels with power-over-coax are safe to disconnect. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cstr.png Channels Channels specifies the channels to wait until safe to disc

### Wait for PoC Safe to Disconnect Channels String VI

Waits and blocks until specified channels with power-over-coax are safe to disconnect.

[IMAGE alt='icon' src='wait-for-poc-safe-to-disconnect-channels-string-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. Channels — Channels specifies the channels to wait until safe to disconnect. The channels specification can be a single channel such as "SI0", a range such as "SI0-SI3" or a list such as "SI0,SI3". Timeout (ms) — Timeout (ms) specifies a time limit in milliseconds to wait until safe to disconnect. A value of -1 indicates to wait indefinitely error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Wait for PoC Safe to Disconnect VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-poc-safe-to-disconnect-vi.html language=enus -->
## TOPIC 00080: Wait for PoC Safe to Disconnect VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-poc-safe-to-disconnect-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-poc-safe-to-disconnect-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks until specified channels with power-over-coax are safe to disconnect. For help on each instance of the polymorphic VI, hover on the polymorphic VI selector. icon

### Wait for PoC Safe to Disconnect VI

Waits and blocks until specified channels with power-over-coax are safe to disconnect. For help on each instance of the polymorphic VI, hover on the polymorphic VI selector.

[IMAGE alt='icon' src='wait-for-poc-safe-to-disconnect-vi.png']

- [Wait for PoC Safe to Disconnect Channels Array VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-poc-safe-to-disconnect-channels-array-vi.html) Waits and blocks until specified channels with power-over-coax are safe to disconnect.
- [Wait for PoC Safe to Disconnect Channels String VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/wait-for-poc-safe-to-disconnect-channels-string-vi.html) Waits and blocks until specified channels with power-over-coax are safe to disconnect.

Parent topic:

Automotive Vision

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-calibration-data-vi.html language=enus -->
## TOPIC 00081: Write Calibration Data VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-calibration-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-calibration-data-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes calibration data to the FlexRIO device's on-board flash memory. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cu32.png offset offset specifies the byte address in the device's flash memory at which to b

### Write Calibration Data VI

Writes calibration data to the FlexRIO device's on-board flash memory.

[IMAGE alt='icon' src='write-calibration-data-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. offset — offset specifies the byte address in the device's flash memory at which to begin the operation. data — data specifies the data to write to the device's flash memory. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-i2c-vi.html language=enus -->
## TOPIC 00082: Write I2C VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-i2c-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-i2c-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Issues an I2C write to the specified I2C bus instance. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cstr.png bus instance name specifies the I2C bus instance to which the read should be issued. cu16.png slave

### Write I2C VI

Issues an I2C write to the specified I2C bus instance.

[IMAGE alt='icon' src='write-i2c-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. bus instance name — specifies the I2C bus instance to which the read should be issued. slave address — slave address specifies the I2C slave address of the device to which the read should be issued. data — data specifies the data to write to the I2C bus. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. repeated start (f) — fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. numBytesWritten — error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

I2C

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-io-module-slots-used-vi.html language=enus -->
## TOPIC 00083: Write IO Module Slots Used VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-io-module-slots-used-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-io-module-slots-used-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes to the EEPROM the number of slots used in the chassis by the IO module. The default value is 1. icon Inputs/Outputs cgenclassrn.png FPGA VI Reference In cu8.png slotsUsed indicates the number of slots used in the chassis by the IO module. The default value is 1. cerrcodeclst.png error in (no

### Write IO Module Slots Used VI

Writes to the EEPROM the number of slots used in the chassis by the IO module. The default value is 1.

[IMAGE alt='icon' src='write-io-module-slots-used-vi.png']

#### Inputs/Outputs

| FPGA VI Reference In — slotsUsed — indicates the number of slots used in the chassis by the IO module. The default value is 1. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FPGA VI Reference Out — error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-qsfp-vi.html language=enus -->
## TOPIC 00084: Write QSFP VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-qsfp-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-qsfp-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes values to the QSFP+ module connected at the specified port. For address and data information, refer to the SFF-8636 specification. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cu8.png port port specifi

### Write QSFP VI

Writes values to the QSFP+ module connected at the specified port. For address and data information, refer to the SFF-8636 specification.

[IMAGE alt='icon' src='write-qsfp-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. port — port specifies the port, 0 or 1, from which the VI reads QSFP+ module data. address — address specifies the address on the QSFP+ module. For address and data information, refer to the SFF-8636 specification. data — data specifies data to be written to an address on the QSFP+ module. For address and data information, refer to the SFF-8636 specification. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

QSFP

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-stream-1d-i16-vi.html language=enus -->
## TOPIC 00085: Write Stream 1D I16 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-stream-1d-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-stream-1d-i16-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to a specified stream. icon Inputs/Outputs ci32.png timeout timeout specifies a time limit in milliseconds after which the VI will stop attempting to write data to the stream. cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface pale

### Write Stream 1D I16 VI

Writes data to a specified stream.

[IMAGE alt='icon' src='write-stream-1d-i16-vi.png']

#### Inputs/Outputs

| timeout — timeout specifies a time limit in milliseconds after which the VI will stop attempting to write data to the stream. fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. stream instance — stream instance identifies an instance of a stream. read data — error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. stream instance out — stream instance out returns a copy of stream number. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Write Stream VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-stream-vi.html language=enus -->
## TOPIC 00086: Write Stream VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-stream-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-stream-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to a specified stream. icon

### Write Stream VI

Writes data to a specified stream.

[IMAGE alt='icon' src='write-stream-vi.png']

- [Write Stream 1D I16 VI](../../../../../../../instr-lib/flexrio/api/host/v1/ni-flexrio/api/write-stream-1d-i16-vi.html) Writes data to a specified stream.

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/api/host/v1/ni-flexrio/open-vi.html language=enus -->
## TOPIC 00087: Open VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/api/host/v1/ni-flexrio/open-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/api/host/v1/ni-flexrio/open-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a session to the specified FlexRIO device using the default FPGA image and creates a session reference you can use to identify this session in subsequent FlexRIO API VI calls. Use Close to dispose of the session reference. icon Inputs/Outputs cdaqmxscale.png RIO Device RIO Device specifies the

### Open VI

Opens a session to the specified FlexRIO device using the default FPGA image and creates a session reference you can use to identify this session in subsequent FlexRIO API VI calls. Use Close to dispose of the session reference.

[IMAGE alt='icon' src='open-vi.png']

#### Inputs/Outputs

| RIO Device — RIO Device specifies the resource name of the FlexRIO device. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/automotive-vision-utility/v1/host/automotive-vision-utility-mnu.html language=enus -->
## TOPIC 00088: Automotive Vision Utility

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/automotive-vision-utility/v1/host/automotive-vision-utility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/automotive-vision-utility/v1/host/automotive-vision-utility-mnu.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Common utility VIs for automotive vision applications icon

### Automotive Vision Utility

Common utility VIs for automotive vision applications

[IMAGE alt='icon' src='automotive-vision-utility-mnu.png']

- [Launch SerDes Configuration Utility Server VI](../../../../../instr-lib/flexrio/automotive-vision-utility/v1/host/launch-serdes-configuration-utility-server-vi.html) Launches the SerDes configuration utility server and establishes a TCP socket client connection to the server.
- [Run Script In SerDes Configuration Utility VI](../../../../../instr-lib/flexrio/automotive-vision-utility/v1/host/run-script-in-serdes-configuration-utility-vi.html) Runs a SerDes configuration script in the SerDes configuration utility server.
- [Parse SerDes Configuration Script VI](../../../../../instr-lib/flexrio/automotive-vision-utility/v1/host/parse-serdes-configuration-script-vi.html) Parses a SerDes configuration script into an array of SerDes Configuration Commands if the script file type is supported.
- [Run SerDes Configuration Commands VI](../../../../../instr-lib/flexrio/automotive-vision-utility/v1/host/run-serdes-configuration-commands-vi.html) Runs the SerDes configuration commands specified in the SerDes config commands array input in sequential order.

Parent topic:

NI FlexRIO API v1

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/automotive-vision-utility/v1/host/launch-serdes-configuration-utility-server-vi.html language=enus -->
## TOPIC 00089: Launch SerDes Configuration Utility Server VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/automotive-vision-utility/v1/host/launch-serdes-configuration-utility-server-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/automotive-vision-utility/v1/host/launch-serdes-configuration-utility-server-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launches the SerDes configuration utility server and establishes a TCP socket client connection to the server. icon Inputs/Outputs cbool.png run minimized? (T) run minimized? (T) specifies whether the command line utility runs minimized. cgenclassrn.png fpga interface in fpga interface in specifies

### Launch SerDes Configuration Utility Server VI

Launches the SerDes configuration utility server and establishes a TCP socket client connection to the server.

[IMAGE alt='icon' src='launch-serdes-configuration-utility-server-vi.png']

#### Inputs/Outputs

| run minimized? (T) — run minimized? (T) specifies whether the command line utility runs minimized. fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. tcp socket config — tcp socket config specifies the TCP socket configuration parameters for the SerDes configuration utility. host — host identifies the socket hostname in internet domain notation or an IPv4 address. port — port identifies the socket port number. timeout — timeout identifies the socket timeout in seconds to wait for a client connection. verbose (F) — verbose (F) specifies whether to increase the output verbosity in the command line utility. output file — output file redirects the command line utility stdout to the output file if specified. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. socket connection id out — socket connection id out returns a reference to the SerDes configuration utility TCP socket. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| host — host identifies the socket hostname in internet domain notation or an IPv4 address. port — port identifies the socket port number. timeout — timeout identifies the socket timeout in seconds to wait for a client connection. |

Parent topic:

Automotive Vision Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/automotive-vision-utility/v1/host/parse-serdes-configuration-script-vi.html language=enus -->
## TOPIC 00090: Parse SerDes Configuration Script VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/automotive-vision-utility/v1/host/parse-serdes-configuration-script-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/automotive-vision-utility/v1/host/parse-serdes-configuration-script-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parses a SerDes configuration script into an array of SerDes Configuration Commands if the script file type is supported. icon Inputs/Outputs cpath.png configuration script configuration script specifies the file path of the configuration script. cerrcodeclst.png error in error in describes error co

### Parse SerDes Configuration Script VI

Parses a SerDes configuration script into an array of SerDes Configuration Commands if the script file type is supported.

[IMAGE alt='icon' src='parse-serdes-configuration-script-vi.png']

#### Inputs/Outputs

| configuration script — configuration script specifies the file path of the configuration script. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. configuration script out — configuration script out returns the file path of the configuration script. file type supported? — file type supported? returns true if the file type is supported, otherwise false. serdes config commands — serdes config commands contains information for SerDes configuration commands. command type — command type specifies the SerDes configuration command type. address — address specifies the I2C address. write data — write data specifies the data bytes to write. num bytes to read — num bytes to read specifies the number of bytes to read. milliseconds to wait — milliseconds to wait specifies the wait time in milliseconds. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| command type — command type specifies the SerDes configuration command type. address — address specifies the I2C address. write data — write data specifies the data bytes to write. num bytes to read — num bytes to read specifies the number of bytes to read. milliseconds to wait — milliseconds to wait specifies the wait time in milliseconds. |

Parent topic:

Automotive Vision Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/automotive-vision-utility/v1/host/run-script-in-serdes-configuration-utility-vi.html language=enus -->
## TOPIC 00091: Run Script In SerDes Configuration Utility VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/automotive-vision-utility/v1/host/run-script-in-serdes-configuration-utility-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/automotive-vision-utility/v1/host/run-script-in-serdes-configuration-utility-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs a SerDes configuration script in the SerDes configuration utility server. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. cncrn.png socket connection id in socket connection id in specifies a reference to t

### Run Script In SerDes Configuration Utility VI

Runs a SerDes configuration script in the SerDes configuration utility server.

[IMAGE alt='icon' src='run-script-in-serdes-configuration-utility-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. socket connection id in — socket connection id in specifies a reference to the SerDes configuration utility TCP socket. serial channels — serial channels specifies the serial channels on which to run the configuration script. configuration script — configuration script specifies the file path of the configuration script. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. socket connection id out — socket connection id out returns a reference to the SerDes configuration utility TCP socket. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Automotive Vision Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/automotive-vision-utility/v1/host/run-serdes-configuration-commands-vi.html language=enus -->
## TOPIC 00092: Run SerDes Configuration Commands VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/automotive-vision-utility/v1/host/run-serdes-configuration-commands-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/automotive-vision-utility/v1/host/run-serdes-configuration-commands-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs the SerDes configuration commands specified in the SerDes config commands array input in sequential order. icon Inputs/Outputs cgenclassrn.png fpga interface in fpga interface in specifies the reference to the VI on the FPGA Interface palette. c1dstr.png serial channels serial channels specifie

### Run SerDes Configuration Commands VI

Runs the SerDes configuration commands specified in the SerDes config commands array input in sequential order.

[IMAGE alt='icon' src='run-serdes-configuration-commands-vi.png']

#### Inputs/Outputs

| fpga interface in — fpga interface in specifies the reference to the VI on the FPGA Interface palette. serial channels — serial channels specifies the serial channels on which to run the configuration script. serdes config commands — serdes config commands contains information for SerDes configuration commands. command type — command type specifies the SerDes configuration command type. address — address specifies the I2C address. write data — write data specifies the data bytes to write. num bytes to read — num bytes to read specifies the number of bytes to read. milliseconds to wait — milliseconds to wait specifies the wait time in milliseconds. enable debug output (F) — enable debug output (F) specifies if debug output is enabled. Set to True to enable. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. fpga interface out — fpga interface out returns a reference to the VI on the FPGA Interface palette. debug output — debug output returns a debug output string for each I2C bus instance if debug output is enabled. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| command type — command type specifies the SerDes configuration command type. address — address specifies the I2C address. write data — write data specifies the data bytes to write. num bytes to read — num bytes to read specifies the number of bytes to read. milliseconds to wait — milliseconds to wait specifies the wait time in milliseconds. |

Parent topic:

Automotive Vision Utility

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo-mnu.html language=enus -->
## TOPIC 00093: DRAM FIFO

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo-mnu.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides a deep buffer that streams data through DRAM. icon

### DRAM FIFO

Provides a deep buffer that streams data through DRAM.

[IMAGE alt='icon' src='dram-fifo-mnu.png']

- [Create Resource VI](../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/create-resource-vi.html) Creates a reference to a DRAM FIFO. Select the instance that corresponds to the data width of the DRAM being accessed.
- [Process VI](../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/process-vi.html) Manages the transfer of enqueued elements to and from the DRAM.
- [Read VI](../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/read-vi.html) Dequeues a Boolean array from the From DRAM queue.
- [Write VI](../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/write-vi.html) Enqueues a Boolean array to the To DRAM queue.
- [Packer VI](../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/packer-vi.html) Packs an array of elements into a Boolean array equal in size to the data width of the DRAM.
- [Unpacker VI](../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpacker-vi.html) Unpacks a Boolean array into an array of elements of specified size and data type.

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/create-resource-vi.html language=enus -->
## TOPIC 00094: Create Resource VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/create-resource-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/create-resource-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a reference to a DRAM FIFO. Select the instance that corresponds to the data width of the DRAM being accessed. icon

### Create Resource VI

Creates a reference to a DRAM FIFO. Select the instance that corresponds to the data width of the DRAM being accessed.

[IMAGE alt='icon' src='create-resource-vi.png']

- [Create 64x1 DRAM FIFO VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u64/create-64x1-dram-fifo-vi.html) Creates a reference to a DRAM FIFO.
- [Create 64x2 DRAM FIFO VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u64x2/create-64x2-dram-fifo-vi.html) Creates a reference to a DRAM FIFO.
- [Create 128x1 DRAM FIFO VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u128/create-128x1-dram-fifo-vi.html) Creates a reference to a DRAM FIFO.
- [Create 128x2 DRAM FIFO VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u128x2/create-128x2-dram-fifo-vi.html) Creates a reference to a DRAM FIFO.
- [Create 256x1 DRAM FIFO VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u256/create-256x1-dram-fifo-vi.html) Creates a reference to a DRAM FIFO.
- [Create 256x2 DRAM FIFO VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u256x2/create-256x2-dram-fifo-vi.html) Creates a reference to a DRAM FIFO.
- [Create 384x1 DRAM FIFO VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u384/create-384x1-dram-fifo-vi.html) Creates a reference to a DRAM FIFO.
- [Create 384x2 DRAM FIFO VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u384x2/create-384x2-dram-fifo-vi.html) Creates a reference to a DRAM FIFO.
- [Create 512x1 DRAM FIFO VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u512/create-512x1-dram-fifo-vi.html) Creates a reference to a DRAM FIFO.
- [Create 512x2 DRAM FIFO VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u512x2/create-512x2-dram-fifo-vi.html) Creates a reference to a DRAM FIFO.

Parent topic:

DRAM FIFO

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-boolean-array-vi.html language=enus -->
## TOPIC 00095: Pack Boolean Array VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-boolean-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-boolean-array-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Packs an array of elements into a Boolean array equal in size to the data width of the DRAM. icon Inputs/Outputs cDRAM_FIFO_v2_FPGAlvclass.png DRAM FIFO in cbool.png reset reset clears data that has not yet been packed and sent out as valid. c1dbool.png data in data in specifies the data elements to

### Pack Boolean Array VI

Packs an array of elements into a Boolean array equal in size to the data width of the DRAM.

[IMAGE alt='icon' src='pack-boolean-array-vi.png']

#### Inputs/Outputs

| DRAM FIFO in — reset — reset clears data that has not yet been packed and sent out as valid. data in — data in specifies the data elements to pack. flush data — flush data specifies whether to flush data from the DRAM FIFO. input valid — input valid informs this VI whether the next data point has arrived for processing. Wire the output valid terminal of an upstream VI to this input. elements per valid output — elements per valid output specifies how many input elements this VI packed into data out. data out — data out returns a Boolean array of packed data equal in size to the DRAM width specified by the Create Resource VI. output valid — output valid returns TRUE if element contains a valid value. Wire this output to the input valid terminal of a downstream VI. |
| --- |

Parent topic:

Packer VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u16-vi.html language=enus -->
## TOPIC 00096: Pack U16 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u16-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u16-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Packs an array of elements into a Boolean array equal in size to the data width of the DRAM. icon Inputs/Outputs cDRAM_FIFO_v2_FPGAlvclass.png DRAM FIFO in cbool.png reset reset clears data that has not yet been packed and sent out as valid. c1du16.png data in data in specifies the data elements to

### Pack U16 VI

Packs an array of elements into a Boolean array equal in size to the data width of the DRAM.

[IMAGE alt='icon' src='pack-u16-vi.png']

#### Inputs/Outputs

| DRAM FIFO in — reset — reset clears data that has not yet been packed and sent out as valid. data in — data in specifies the data elements to pack. flush data — flush data specifies whether to flush data from the DRAM FIFO. input valid — input valid informs this VI whether the next data point has arrived for processing. Wire the output valid terminal of an upstream VI to this input. elements per valid output — elements per valid output specifies how many input elements this VI packed into data out. data out — data out returns a Boolean array of packed data equal in size to the DRAM width specified by the Create Resource VI. output valid — output valid returns TRUE if element contains a valid value. Wire this output to the input valid terminal of a downstream VI. |
| --- |

Parent topic:

Packer VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u32-vi.html language=enus -->
## TOPIC 00097: Pack U32 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u32-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Packs an array of elements into a Boolean array equal in size to the data width of the DRAM. icon Inputs/Outputs cDRAM_FIFO_v2_FPGAlvclass.png DRAM FIFO in cbool.png reset reset clears data that has not yet been packed and sent out as valid. c1du32.png data in data in specifies the data elements to

### Pack U32 VI

Packs an array of elements into a Boolean array equal in size to the data width of the DRAM.

[IMAGE alt='icon' src='pack-u32-vi.png']

#### Inputs/Outputs

| DRAM FIFO in — reset — reset clears data that has not yet been packed and sent out as valid. data in — data in specifies the data elements to pack. flush data — flush data specifies whether to flush data from the DRAM FIFO. input valid — input valid informs this VI whether the next data point has arrived for processing. Wire the output valid terminal of an upstream VI to this input. elements per valid output — elements per valid output specifies how many input elements this VI packed into data out. data out — data out returns a Boolean array of packed data equal in size to the DRAM width specified by the Create Resource VI. output valid — output valid returns TRUE if element contains a valid value. Wire this output to the input valid terminal of a downstream VI. |
| --- |

Parent topic:

Packer VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u64-vi.html language=enus -->
## TOPIC 00098: Pack U64 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u64-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u64-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Packs an array of elements into a Boolean array equal in size to the data width of the DRAM. icon Inputs/Outputs cDRAM_FIFO_v2_FPGAlvclass.png DRAM FIFO in cbool.png reset reset clears data that has not yet been packed and sent out as valid. c1du64.png data in data in specifies the data elements to

### Pack U64 VI

Packs an array of elements into a Boolean array equal in size to the data width of the DRAM.

[IMAGE alt='icon' src='pack-u64-vi.png']

#### Inputs/Outputs

| DRAM FIFO in — reset — reset clears data that has not yet been packed and sent out as valid. data in — data in specifies the data elements to pack. flush data — flush data specifies whether to flush data from the DRAM FIFO. input valid — input valid informs this VI whether the next data point has arrived for processing. Wire the output valid terminal of an upstream VI to this input. elements per valid output — elements per valid output specifies how many input elements this VI packed into data out. data out — data out returns a Boolean array of packed data equal in size to the DRAM width specified by the Create Resource VI. output valid — output valid returns TRUE if element contains a valid value. Wire this output to the input valid terminal of a downstream VI. |
| --- |

Parent topic:

Packer VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u8-vi.html language=enus -->
## TOPIC 00099: Pack U8 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u8-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u8-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Packs an array of elements into a Boolean array equal in size to the data width of the DRAM. icon Inputs/Outputs cDRAM_FIFO_v2_FPGAlvclass.png DRAM FIFO in cbool.png reset reset clears data that has not yet been packed and sent out as valid. c1du8.png data in data in specifies the data elements to p

### Pack U8 VI

Packs an array of elements into a Boolean array equal in size to the data width of the DRAM.

[IMAGE alt='icon' src='pack-u8-vi.png']

#### Inputs/Outputs

| DRAM FIFO in — reset — reset clears data that has not yet been packed and sent out as valid. data in — data in specifies the data elements to pack. flush data — flush data specifies whether to flush data from the DRAM FIFO. input valid — input valid informs this VI whether the next data point has arrived for processing. Wire the output valid terminal of an upstream VI to this input. elements per valid output — elements per valid output specifies how many input elements this VI packed into data out. data out — data out returns a Boolean array of packed data equal in size to the DRAM width specified by the Create Resource VI. output valid — output valid returns TRUE if element contains a valid value. Wire this output to the input valid terminal of a downstream VI. |
| --- |

Parent topic:

Packer VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/packer-vi.html language=enus -->
## TOPIC 00100: Packer VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/packer-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/packer-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Packs an array of elements into a Boolean array equal in size to the data width of the DRAM. icon

### Packer VI

Packs an array of elements into a Boolean array equal in size to the data width of the DRAM.

[IMAGE alt='icon' src='packer-vi.png']

- [Pack U8 VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u8-vi.html) Packs an array of elements into a Boolean array equal in size to the data width of the DRAM.
- [Pack U16 VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u16-vi.html) Packs an array of elements into a Boolean array equal in size to the data width of the DRAM.
- [Pack U32 VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u32-vi.html) Packs an array of elements into a Boolean array equal in size to the data width of the DRAM.
- [Pack U64 VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-u64-vi.html) Packs an array of elements into a Boolean array equal in size to the data width of the DRAM.
- [Pack Boolean Array VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/pack-boolean-array-vi.html) Packs an array of elements into a Boolean array equal in size to the data width of the DRAM.

Parent topic:

DRAM FIFO

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u128/create-128x1-dram-fifo-vi.html language=enus -->
## TOPIC 00101: Create 128x1 DRAM FIFO VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u128/create-128x1-dram-fifo-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u128/create-128x1-dram-fifo-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a reference to a DRAM FIFO. icon Inputs/Outputs cgenclassrntag.png memory refnum memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U128 custom control at instr.lib\_niInstr\Memory\v1\FPGA\Memory\Public as the data type when configuring the me

### Create 128x1 DRAM FIFO VI

Creates a reference to a DRAM FIFO.

[IMAGE alt='icon' src='create-128x1-dram-fifo-vi.png']

#### Inputs/Outputs

| memory refnum — memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U128 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. actual # of DRAM elements — actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements according to the properties page of the memory item. DRAM FIFO ref out — DRAM FIFO ref out returns the reference to the DRAM FIFO. |
| --- |

Parent topic:

Create Resource VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u128x2/create-128x2-dram-fifo-vi.html language=enus -->
## TOPIC 00102: Create 128x2 DRAM FIFO VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u128x2/create-128x2-dram-fifo-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u128x2/create-128x2-dram-fifo-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a reference to a DRAM FIFO. icon Inputs/Outputs cgenclassrntag.png memory refnum memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U128 custom control at instr.lib\_niInstr\Memory\v1\FPGA\Memory\Public as the data type when configuring the me

### Create 128x2 DRAM FIFO VI

Creates a reference to a DRAM FIFO.

[IMAGE alt='icon' src='create-128x2-dram-fifo-vi.png']

#### Inputs/Outputs

| memory refnum — memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U128 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. memory refnum 2 — memory refnum 2 identifies a second memory item implemented using DRAM through which to stream data. Use the U128 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. actual # of DRAM elements — actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements according to the properties page of the memory item. The address length does not double with the x2 implementation. The DRAM data width doubles in size. DRAM FIFO ref out — DRAM FIFO ref out returns the reference to the DRAM FIFO. |
| --- |

Parent topic:

Create Resource VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u256/create-256x1-dram-fifo-vi.html language=enus -->
## TOPIC 00103: Create 256x1 DRAM FIFO VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u256/create-256x1-dram-fifo-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u256/create-256x1-dram-fifo-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a reference to a DRAM FIFO. icon Inputs/Outputs cgenclassrntag.png memory refnum memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U256 custom control at instr.lib\_niInstr\Memory\v1\FPGA\Memory\Public as the data type when configuring the me

### Create 256x1 DRAM FIFO VI

Creates a reference to a DRAM FIFO.

[IMAGE alt='icon' src='create-256x1-dram-fifo-vi.png']

#### Inputs/Outputs

| memory refnum — memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U256 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. actual # of DRAM elements — actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements according to the properties page of the memory item. DRAM FIFO ref out — DRAM FIFO ref out returns the reference to the DRAM FIFO. |
| --- |

Parent topic:

Create Resource VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u256x2/create-256x2-dram-fifo-vi.html language=enus -->
## TOPIC 00104: Create 256x2 DRAM FIFO VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u256x2/create-256x2-dram-fifo-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u256x2/create-256x2-dram-fifo-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a reference to a DRAM FIFO. icon Inputs/Outputs cgenclassrntag.png memory refnum memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U256 custom control at instr.lib\_niInstr\Memory\v1\FPGA\Memory\Public as the data type when configuring the me

### Create 256x2 DRAM FIFO VI

Creates a reference to a DRAM FIFO.

[IMAGE alt='icon' src='create-256x2-dram-fifo-vi.png']

#### Inputs/Outputs

| memory refnum — memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U256 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. memory refnum 2 — memory refnum 2 identifies a second memory item implemented using DRAM through which to stream data. Use the U256 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. actual # of DRAM elements — actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements according to the properties page of the memory item. The address length does not double with the x2 implementation. The DRAM data width doubles in size. DRAM FIFO ref out — DRAM FIFO ref out returns the reference to the DRAM FIFO. |
| --- |

Parent topic:

Create Resource VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u384/create-384x1-dram-fifo-vi.html language=enus -->
## TOPIC 00105: Create 384x1 DRAM FIFO VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u384/create-384x1-dram-fifo-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u384/create-384x1-dram-fifo-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a reference to a DRAM FIFO. icon Inputs/Outputs cgenclassrntag.png memory refnum memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U384 custom control at instr.lib\_niInstr\Memory\v1\FPGA\Memory\Public as the data type when configuring the me

### Create 384x1 DRAM FIFO VI

Creates a reference to a DRAM FIFO.

[IMAGE alt='icon' src='create-384x1-dram-fifo-vi.png']

#### Inputs/Outputs

| memory refnum — memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U384 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. actual # of DRAM elements — actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements according to the properties page of the memory item. DRAM FIFO ref out — DRAM FIFO ref out returns the reference to the DRAM FIFO. |
| --- |

Parent topic:

Create Resource VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u384x2/create-384x2-dram-fifo-vi.html language=enus -->
## TOPIC 00106: Create 384x2 DRAM FIFO VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u384x2/create-384x2-dram-fifo-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u384x2/create-384x2-dram-fifo-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a reference to a DRAM FIFO. icon Inputs/Outputs cgenclassrntag.png memory refnum memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U384 custom control at instr.lib\_niInstr\Memory\v1\FPGA\Memory\Public as the data type when configuring the me

### Create 384x2 DRAM FIFO VI

Creates a reference to a DRAM FIFO.

[IMAGE alt='icon' src='create-384x2-dram-fifo-vi.png']

#### Inputs/Outputs

| memory refnum — memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U384 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. memory refnum 2 — memory refnum 2 identifies a second memory item implemented using DRAM through which to stream data. Use the U384 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. actual # of DRAM elements — actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements according to the properties page of the memory item. The address length does not double with the x2 implementation. The DRAM data width doubles in size. DRAM FIFO ref out — DRAM FIFO ref out returns the reference to the DRAM FIFO. |
| --- |

Parent topic:

Create Resource VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u512/create-512x1-dram-fifo-vi.html language=enus -->
## TOPIC 00107: Create 512x1 DRAM FIFO VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u512/create-512x1-dram-fifo-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u512/create-512x1-dram-fifo-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a reference to a DRAM FIFO. icon Inputs/Outputs cgenclassrntag.png memory refnum memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U512 custom control at instr.lib\_niInstr\Memory\v1\FPGA\Memory\Public as the data type when configuring the me

### Create 512x1 DRAM FIFO VI

Creates a reference to a DRAM FIFO.

[IMAGE alt='icon' src='create-512x1-dram-fifo-vi.png']

#### Inputs/Outputs

| memory refnum — memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U512 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. actual # of DRAM elements — actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements according to the properties page of the memory item. DRAM FIFO ref out — DRAM FIFO ref out returns the reference to the DRAM FIFO. |
| --- |

Parent topic:

Create Resource VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u512x2/create-512x2-dram-fifo-vi.html language=enus -->
## TOPIC 00108: Create 512x2 DRAM FIFO VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u512x2/create-512x2-dram-fifo-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u512x2/create-512x2-dram-fifo-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a reference to a DRAM FIFO. icon Inputs/Outputs cgenclassrntag.png memory refnum memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U512 custom control at instr.lib\_niInstr\Memory\v1\FPGA\Memory\Public as the data type when configuring the me

### Create 512x2 DRAM FIFO VI

Creates a reference to a DRAM FIFO.

[IMAGE alt='icon' src='create-512x2-dram-fifo-vi.png']

#### Inputs/Outputs

| memory refnum — memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U512 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. memory refnum 2 — memory refnum 2 identifies a second memory item implemented using DRAM through which to stream data. Use the U512 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. actual # of DRAM elements — actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements according to the properties page of the memory item. The address length does not double with the x2 implementation. The DRAM data width doubles in size. DRAM FIFO ref out — DRAM FIFO ref out returns the reference to the DRAM FIFO. |
| --- |

Parent topic:

Create Resource VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u64/create-64x1-dram-fifo-vi.html language=enus -->
## TOPIC 00109: Create 64x1 DRAM FIFO VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u64/create-64x1-dram-fifo-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u64/create-64x1-dram-fifo-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a reference to a DRAM FIFO. icon Inputs/Outputs cgenclassrntag.png memory refnum memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U64 custom control at instr.lib\_niInstr\Memory\v1\FPGA\Memory\Public as the data type when configuring the mem

### Create 64x1 DRAM FIFO VI

Creates a reference to a DRAM FIFO.

[IMAGE alt='icon' src='create-64x1-dram-fifo-vi.png']

#### Inputs/Outputs

| memory refnum — memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U64 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. actual # of DRAM elements — actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements according to the properties page of the memory item. DRAM FIFO ref out — DRAM FIFO ref out returns the reference to the DRAM FIFO. |
| --- |

Parent topic:

Create Resource VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u64x2/create-64x2-dram-fifo-vi.html language=enus -->
## TOPIC 00110: Create 64x2 DRAM FIFO VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u64x2/create-64x2-dram-fifo-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/private/dram-fifo-u64x2/create-64x2-dram-fifo-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a reference to a DRAM FIFO. icon Inputs/Outputs cgenclassrntag.png memory refnum memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U64 custom control at instr.lib\_niInstr\Memory\v1\FPGA\Memory\Public as the data type when configuring the mem

### Create 64x2 DRAM FIFO VI

Creates a reference to a DRAM FIFO.

[IMAGE alt='icon' src='create-64x2-dram-fifo-vi.png']

#### Inputs/Outputs

| memory refnum — memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U64 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. memory refnum 2 — memory refnum 2 identifies a second memory item implemented using DRAM through which to stream data. Use the U64 custom control at instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. actual # of DRAM elements — actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements according to the properties page of the memory item. The address length does not double with the x2 implementation. The DRAM data width doubles in size. DRAM FIFO ref out — DRAM FIFO ref out returns the reference to the DRAM FIFO. |
| --- |

Parent topic:

Create Resource VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/process-vi.html language=enus -->
## TOPIC 00111: Process VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/process-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/process-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Manages the transfer of enqueued elements to and from the DRAM. Place this VI inside a single cycle timed loop that uses a DRAM clock with a speed as close as possible to the DRAM clock speed that is optimal for the device. See the help for your FPGA target to identify which clock is optimal for its

### Process VI

Manages the transfer of enqueued elements to and from the DRAM.

Place this VI inside a single cycle timed loop that uses a DRAM clock with a speed as close as possible to the DRAM clock speed that is optimal for the device. See the help for your FPGA target to identify which clock is optimal for its DRAM.

[IMAGE alt='icon' src='process-vi.png']

#### Inputs/Outputs

| DRAM FIFO ref in — DRAM FIFO Ref In specifies the reference to the DRAM FIFO. reset DRAM — write grant time (clock ticks) — write grant time (clock ticks) specifies the number of consecutive writes to perform to DRAM before switching back to reads. Longer grant times reduce the number of switches between reads and writes and are more efficient than shorter grant times. read grant time (clock ticks) — read grant time (clock ticks) specifies the number of consecutive reads to perform from DRAM before switching back to writes. Longer grant times reduce the number of switches between reads and writes and are more efficient than shorter grant times. dynamic arbitration — dynamic arbitration specifies how to dynamically assign throughput to reads and writes. reset in progress? — reset in progress? indicates whether a reset is in progress. status — status provides information on how full the DRAM is as well as how many elements are waiting to be read from the To DRAM queue and From DRAM queue. elements in 'to DRAM queue' — elements in 'to DRAM queue' indicates the number of elements in the To DRAM queue. elements in 'from DRAM queue' — elements in 'from DRAM queue' indicates how many elements are in the From DRAM queue. elements in DRAM — elements in DRAM indicates how many elements are in the DRAM. DRAM full — DRAM full indicates whether the DRAM is full. DRAM empty — DRAM empty indicates whether the DRAM is empty. |
| --- |
| elements in 'to DRAM queue' — elements in 'to DRAM queue' indicates the number of elements in the To DRAM queue. elements in 'from DRAM queue' — elements in 'from DRAM queue' indicates how many elements are in the From DRAM queue. elements in DRAM — elements in DRAM indicates how many elements are in the DRAM. DRAM full — DRAM full indicates whether the DRAM is full. DRAM empty — DRAM empty indicates whether the DRAM is empty. |

Parent topic:

DRAM FIFO

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/read-vi.html language=enus -->
## TOPIC 00112: Read VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/read-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/read-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Dequeues a Boolean array from the From DRAM queue. icon Inputs/Outputs cDRAM_FIFO_v2_FPGAlvclass.png DRAM FIFO ref in DRAM FIFO Ref In specifies the reference to the DRAM FIFO. cbool.png ready for output ready for output informs this VI whether downstream VIs are ready for this VI to return a new va

### Read VI

Dequeues a Boolean array from the From DRAM queue.

[IMAGE alt='icon' src='read-vi.png']

#### Inputs/Outputs

| DRAM FIFO ref in — DRAM FIFO Ref In specifies the reference to the DRAM FIFO. ready for output — ready for output informs this VI whether downstream VIs are ready for this VI to return a new value. The default value is TRUE. Use a Feedback Node to wire the ready for input terminal of a downstream VI to this input. element — element returns the oldest data element in the FIFO. Use Unpacker to convert the data back to its original type. output valid — output valid returns TRUE if element contains a valid value. Wire this output to the input valid terminal of a downstream VI. |
| --- |

Parent topic:

DRAM FIFO

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-boolean-array-vi.html language=enus -->
## TOPIC 00113: Unpack Boolean Array VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-boolean-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-boolean-array-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unpacks a Boolean array into a Boolean array. icon Inputs/Outputs cu16.png output data size (bits) cbool.png reset reset clears data that has not yet been unpacked and sent out as valid. c1dbool.png packed data in packed data in specifies the array of packed data to unpack. cbool.png input valid inp

### Unpack Boolean Array VI

Unpacks a Boolean array into a Boolean array.

[IMAGE alt='icon' src='unpack-boolean-array-vi.png']

#### Inputs/Outputs

| output data size (bits) — reset — reset clears data that has not yet been unpacked and sent out as valid. packed data in — packed data in specifies the array of packed data to unpack. input valid — input valid informs this VI whether the next data point has arrived for processing. Wire the output valid terminal of an upstream VI to this input. ready for output — ready for output informs this VI whether downstream VIs are ready for this VI to return a new value. The default value is TRUE. Use a Feedback Node to wire the ready for input terminal of a downstream VI to this input. unpacked data out — unpacked data out returns an array of data equal in size to the value provided in output data size. output valid — output valid returns TRUE if element contains a valid value. Wire this output to the input valid terminal of a downstream VI. ready for input — ready for input indicates whether this VI is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output terminal of an upstream VI. A value of FALSE indicates that the To DRAM queue is full. A full DRAM queue can result from either insufficient write grant time or a full DRAM FIFO. Use Process to get information about the state of the FIFO. |
| --- |

Parent topic:

Unpacker VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u16-vi.html language=enus -->
## TOPIC 00114: Unpack U16 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u16-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u16-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unpacks a Boolean array into an array of unsigned 16-bit integers. icon Inputs/Outputs cu16.png output data size (elements) output data size (elements) specifies the number of elements to return in the unpacked data out array. This value must be a constant. cbool.png reset reset clears data that has

### Unpack U16 VI

Unpacks a Boolean array into an array of unsigned 16-bit integers.

[IMAGE alt='icon' src='unpack-u16-vi.png']

#### Inputs/Outputs

| output data size (elements) — output data size (elements) specifies the number of elements to return in the unpacked data out array. This value must be a constant. reset — reset clears data that has not yet been unpacked and sent out as valid. packed data in — packed data in specifies the array of packed data to unpack. input valid — input valid informs this VI whether the next data point has arrived for processing. Wire the output valid terminal of an upstream VI to this input. ready for output — ready for output informs this VI whether downstream VIs are ready for this VI to return a new value. The default value is TRUE. Use a Feedback Node to wire the ready for input terminal of a downstream VI to this input. unpacked data out — unpacked data out returns an array of data equal in size to the value provided in output data size. output valid — output valid returns TRUE if element contains a valid value. Wire this output to the input valid terminal of a downstream VI. ready for input — ready for input indicates whether this VI is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output terminal of an upstream VI. A value of FALSE indicates that the To DRAM queue is full. A full DRAM queue can result from either insufficient write grant time or a full DRAM FIFO. Use Process to get information about the state of the FIFO. |
| --- |

Parent topic:

Unpacker VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u32-vi.html language=enus -->
## TOPIC 00115: Unpack U32 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u32-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unpacks a Boolean array into an array of unsigned 32-bit integers. icon Inputs/Outputs cu16.png output data size (elements) output data size (elements) specifies the number of elements to return in the unpacked data out array. This value must be a constant. cbool.png reset reset clears data that has

### Unpack U32 VI

Unpacks a Boolean array into an array of unsigned 32-bit integers.

[IMAGE alt='icon' src='unpack-u32-vi.png']

#### Inputs/Outputs

| output data size (elements) — output data size (elements) specifies the number of elements to return in the unpacked data out array. This value must be a constant. reset — reset clears data that has not yet been unpacked and sent out as valid. packed data in — packed data in specifies the array of packed data to unpack. input valid — input valid informs this VI whether the next data point has arrived for processing. Wire the output valid terminal of an upstream VI to this input. ready for output — ready for output informs this VI whether downstream VIs are ready for this VI to return a new value. The default value is TRUE. Use a Feedback Node to wire the ready for input terminal of a downstream VI to this input. unpacked data out — unpacked data out returns an array of data equal in size to the value provided in output data size. output valid — output valid returns TRUE if element contains a valid value. Wire this output to the input valid terminal of a downstream VI. ready for input — ready for input indicates whether this VI is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output terminal of an upstream VI. A value of FALSE indicates that the To DRAM queue is full. A full DRAM queue can result from either insufficient write grant time or a full DRAM FIFO. Use Process to get information about the state of the FIFO. |
| --- |

Parent topic:

Unpacker VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u64-vi.html language=enus -->
## TOPIC 00116: Unpack U64 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u64-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u64-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unpacks a Boolean array into an array of unsigned 64-bit integers. icon Inputs/Outputs cu16.png output data size (elements) output data size (elements) specifies the number of elements to return in the unpacked data out array. This value must be a constant. cbool.png reset reset clears data that has

### Unpack U64 VI

Unpacks a Boolean array into an array of unsigned 64-bit integers.

[IMAGE alt='icon' src='unpack-u64-vi.png']

#### Inputs/Outputs

| output data size (elements) — output data size (elements) specifies the number of elements to return in the unpacked data out array. This value must be a constant. reset — reset clears data that has not yet been unpacked and sent out as valid. packed data in — packed data in specifies the array of packed data to unpack. input valid — input valid informs this VI whether the next data point has arrived for processing. Wire the output valid terminal of an upstream VI to this input. ready for output — ready for output informs this VI whether downstream VIs are ready for this VI to return a new value. The default value is TRUE. Use a Feedback Node to wire the ready for input terminal of a downstream VI to this input. unpacked data out — unpacked data out returns an array of data equal in size to the value provided in output data size. output valid — output valid returns TRUE if element contains a valid value. Wire this output to the input valid terminal of a downstream VI. ready for input — ready for input indicates whether this VI is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output terminal of an upstream VI. A value of FALSE indicates that the To DRAM queue is full. A full DRAM queue can result from either insufficient write grant time or a full DRAM FIFO. Use Process to get information about the state of the FIFO. |
| --- |

Parent topic:

Unpacker VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u8-vi.html language=enus -->
## TOPIC 00117: Unpack U8 VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u8-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u8-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unpacks a Boolean array into an array of unsigned 8-bit integers. icon Inputs/Outputs cu16.png output data size (elements) output data size (elements) specifies the number of elements to return in the unpacked data out array. This value must be a constant. cbool.png reset reset clears data that has

### Unpack U8 VI

Unpacks a Boolean array into an array of unsigned 8-bit integers.

[IMAGE alt='icon' src='unpack-u8-vi.png']

#### Inputs/Outputs

| output data size (elements) — output data size (elements) specifies the number of elements to return in the unpacked data out array. This value must be a constant. reset — reset clears data that has not yet been unpacked and sent out as valid. packed data in — packed data in specifies the array of packed data to unpack. input valid — input valid informs this VI whether the next data point has arrived for processing. Wire the output valid terminal of an upstream VI to this input. ready for output — ready for output informs this VI whether downstream VIs are ready for this VI to return a new value. The default value is TRUE. Use a Feedback Node to wire the ready for input terminal of a downstream VI to this input. unpacked data out — unpacked data out returns an array of data equal in size to the value provided in output data size. output valid — output valid returns TRUE if element contains a valid value. Wire this output to the input valid terminal of a downstream VI. ready for input — ready for input indicates whether this VI is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output terminal of an upstream VI. A value of FALSE indicates that the To DRAM queue is full. A full DRAM queue can result from either insufficient write grant time or a full DRAM FIFO. Use Process to get information about the state of the FIFO. |
| --- |

Parent topic:

Unpacker VI

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpacker-vi.html language=enus -->
## TOPIC 00118: Unpacker VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpacker-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpacker-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unpacks a Boolean array into an array of elements of specified size and data type. icon

### Unpacker VI

Unpacks a Boolean array into an array of elements of specified size and data type.

[IMAGE alt='icon' src='unpacker-vi.png']

- [Unpack U8 VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u8-vi.html) Unpacks a Boolean array into an array of unsigned 8-bit integers.
- [Unpack U16 VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u16-vi.html) Unpacks a Boolean array into an array of unsigned 16-bit integers.
- [Unpack U32 VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u32-vi.html) Unpacks a Boolean array into an array of unsigned 32-bit integers.
- [Unpack U64 VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-u64-vi.html) Unpacks a Boolean array into an array of unsigned 64-bit integers.
- [Unpack Boolean Array VI](../../../../../../instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/unpack-boolean-array-vi.html) Unpacks a Boolean array into a Boolean array.

Parent topic:

DRAM FIFO

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/write-vi.html language=enus -->
## TOPIC 00119: Write VI

- bundle_id: `flexrio-labview-api-ref`
- source_path: `instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/write-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/instr-lib/flexrio/dram-fifo/v2/fpga/dram-fifo/write-vi.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enqueues a Boolean array to the To DRAM queue. icon Inputs/Outputs cDRAM_FIFO_v2_FPGAlvclass.png DRAM FIFO ref in DRAM FIFO Ref In specifies the reference to the DRAM FIFO. c1dbool.png element element specifies the Boolean array data element to store in the FIFO. For writing numerical array data, fi

### Write VI

Enqueues a Boolean array to the To DRAM queue.

[IMAGE alt='icon' src='write-vi.png']

#### Inputs/Outputs

| DRAM FIFO ref in — DRAM FIFO Ref In specifies the reference to the DRAM FIFO. element — element specifies the Boolean array data element to store in the FIFO. For writing numerical array data, first use Packer to convert the array to a Boolean array. input valid — input valid informs this VI whether the next data point has arrived for processing. Wire the output valid terminal of an upstream VI to this input. ready for input — ready for input indicates whether this VI is ready to accept new input data. Use a Feedback Node to wire this output to the ready for output terminal of an upstream VI. A value of FALSE indicates that the To DRAM queue is full. A full DRAM queue can result from either insufficient write grant time or a full DRAM FIFO. Use Process to get information about the state of the FIFO. |
| --- |

Parent topic:

DRAM FIFO

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=io-module-clock-selections-properties.html language=enus -->
## TOPIC 00120: IO Module Clock Selections Properties Page

- bundle_id: `flexrio-labview-api-ref`
- source_path: `io-module-clock-selections-properties.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/io-module-clock-selections-properties.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Component-Level IP Properties dialog box, select Clock Selections from the Category list to display this page. Use this page to link each clock port defined by the CLIP to a clock on the FPGA target. You must add the FPGA clock to the LabVIEW project before you can link to the FPGA clock. Thi

### IO Module Clock Selections Properties Page

In the Component-Level IP Properties dialog box, select Clock Selections from the Category list to display this page.

Use this page to link each clock port defined by the CLIP to a clock on the FPGA target. You must add the FPGA clock to the LabVIEW project before you can link to the FPGA clock.

This page includes the following components:

- Component-Level IP Clock —Lists clock(s) you defined in the CLIP declaration XML file.
- Connection —Lists clocks available on the FPGA target.

Parent topic:

IO Module Properties Dialog Box

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=io-module-details-properties.html language=enus -->
## TOPIC 00121: IO Module Details Properties Page

- bundle_id: `flexrio-labview-api-ref`
- source_path: `io-module-details-properties.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/io-module-details-properties.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the IO Module Properties dialog box, select Details from the Category list to display this page. Use this page to view detailed information about the adapter module that is currently selected in the IO Module General Properties page. This information is populated in the LabVIEW project from the a

### IO Module Details Properties Page

In the IO Module Properties dialog box, select Details from the Category list to display this page.

Use this page to view detailed information about the adapter module that is currently selected in the IO Module General Properties page. This information is populated in the LabVIEW project from the associated adapter module configuration file (.fam).

#### Adapter Module Configuration (.fam) Values

The following sections contain detailed descriptions of each of the supported configuration values contained with the .fam file.

- Manufacturer —Specifies the manufacturer of the currently configured adapter module.
- Model —Specifies the model name of the configured adapter module. This name displays in the LabVIEW project with the adapter module.
- VccoA/VccoB —Specifies the voltage level that the VccoA and VccoB banks, respectively, are configured to use when you download an application compiled for use with the adapter module to the FPGA. Use this component with the NI PXI-795xR and NI PXIe-796xR devices only.
- Vcco —Specifies the voltage level that the Vcco bank is configured to use when you download an adapter module application to the FPGA. Use this component with the NI PXIe-797xR devices only.
- IOModuleID —If the selected adapter module has an EEPROM, this indicator displays the stored 32-bit IO Module ID. If the selected adapter module does not have an EEPROM, this indicator displays <No EEPROM>.
- Default Component Level IP —Specifies the declaration name of the component-level IP (CLIP). This CLIP is automatically configured for use when you create a new LabVIEW project and MAX recognizes the FlexRIO device and the attached adapter module.
- GPIO Constraints —Specifies the FPGA pin constraint that the FPGA compilation uses for this adapter module. The Constraints section of the adapter module configuration (.fam) file defines this information. Use the Constraints section to constrain the I/O Standard for each FPGA pin that is used by a GPIO line to the adapter module connector. These constaints should match the I/O Standard that the adapter module is designed to use.
- Sync Clock —Configures the IoModSyncClk signal supplied to the adapter module. The default setting for Sync Clock is the value specified in the adapter module configuration (.fam) file. Note You must recompile the VI after changing the Sync Clock value.
- Power Rail Sequence —Specifies the power-up sequence that the power rails use when you download an adapter module application to the FPGA. Note Use this component with the NI PXIe-797xR devices only.
- IO Module Configuration File Path —Specifies the path to the adapter module configuration file (.fam) for the currently selected adapter module.

For more information about the .fam file, refer to the FlexRIO Adapter Module Development Kit User Manual.

Parent topic:

IO Module Properties Dialog Box

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=io-module-general-properties.html language=enus -->
## TOPIC 00122: IO Module General Properties Page

- bundle_id: `flexrio-labview-api-ref`
- source_path: `io-module-general-properties.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/io-module-general-properties.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the IO Module Properties dialog box, select General from the Category list to display this page. Use this page to enable and select your adapter module. Also use this page to select, view details for, and reload component-level IP (CLIP) declaration XML files. This page contains the following com

### IO Module General Properties Page

In the IO Module Properties dialog box, select General from the Category list to display this page.

Use this page to enable and select your adapter module. Also use this page to select, view details for, and reload component-level IP (CLIP) declaration XML files.

This page contains the following components:

- Enable IO Module —Enables the adapter module if it is compatible with the bitstream currently downloaded to the FPGA. Unchecking this box disables the adapter module and causes no adapter module I/O to be available in the LabVIEW project. Disabling the adapter module also tristates all GPIO pins that are routed to the adapter module connector.
- IO Modules —Provides a list of all adapter modules available for use in your LabVIEW project.
- Component Level IP —Lists all CLIP items that are compatible with the selected adapter module. If multiple versions of a single CLIP are present, version information displays next to each CLIP name.
- Details —Displays general information about the selected adapter module and CLIP. For custom adapter module CLIP, syntax errors from either the associated adapter module configuration file (.fam) or the CLIP XML declaration file are also displayed in the Details dialog box.
- Component Level IP Path —Displays the file system path to the XML file for the currently selected CLIP file.
- Reload —Reload the declaration XML file for the currently selected CLIP. Use the Reload button if you modify a declaration XML file on disk after you configure it for use with your adapter module. Reload updates the I/O in the LabVIEW project, but changes may not be visible in the IO Module General Properties page.

NI provides CLIP support options for the FlexRIO adapter modules. For more information, refer to [Configuring a FlexRIO Adapter Module in LabVIEW](/csh?context=flexrio_frioamshelp_config_fam_in_lv).

Parent topic:

IO Module Properties Dialog Box

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=io-module-properties-dialog-box.html language=enus -->
## TOPIC 00123: IO Module Properties Dialog Box

- bundle_id: `flexrio-labview-api-ref`
- source_path: `io-module-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/io-module-properties-dialog-box.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In software, FlexRIO adapter modules are referred to as IO Modules. Right-click the IO Module item in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to select which adapter module to use in your application. You can also confi

### IO Module Properties Dialog Box

Note

Right-click the IO Module item in the Project Explorer window and select Properties from the shortcut menu to display this dialog box.

Use this dialog box to select which adapter module to use in your application. You can also configure which component-level IP (CLIP) to use as the interface to the adapter module circuitry.

This dialog box includes the following components:

- General
- Clock Selections
- Status
- Details

- [IO Module General Properties Page](io-module-general-properties.html)
- [IO Module Clock Selections Properties Page](io-module-clock-selections-properties.html)
- [IO Module Status Properties Page](io-module-status-properties.html)
- [IO Module Details Properties Page](io-module-details-properties.html)

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=io-module-status-properties.html language=enus -->
## TOPIC 00124: IO Module Status Properties Page

- bundle_id: `flexrio-labview-api-ref`
- source_path: `io-module-status-properties.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/io-module-status-properties.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the IO Module Properties dialog box, select Status from the Category list to display this page. Use this page to see the status information of the installed adapter module. Because this property page communicates directly with hardware, you must have a proper RIO resource name configured for the

### IO Module Status Properties Page

In the IO Module Properties dialog box, select Status from the Category list to display this page.

Use this page to see the status information of the installed adapter module. Because this property page communicates directly with hardware, you must have a proper RIO resource name configured for the FlexRIO device. You can configure the RIO resource name by configuring the Resource property on the FPGA target item.

This page contains the following components:

- Expected IO Module —Displays the manufacturer and model name of the adapter module that the FPGA firmware is currently expecting to use, based upon the current program that is downloaded to the FPGA. This control is only updated each time a new program is downloaded to the FPGA.
- Status —Displays general information about the hardware state, including which adapter module is currently inserted and the state of the adapter module power.
- Enable IO Module Power —This control enables or disables power to the installed adapter module interface. NI highly recommends that you ensure that adapter module power is disabled before swapping out adapter modules. Notice that power can only be enabled if the inserted and expected adapter modules match. Therefore, the Enable IO Module Power control can only be used when the inserted and expected adapter modules are the same.

Parent topic:

IO Module Properties Dialog Box

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession-p.html language=enus -->
## TOPIC 00125: FlexRIO Properties

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession-p.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession-p.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### FlexRIO Properties

- [Channel:Description:AI Channel Count](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-aichannelcount.html) Indicates the number of analog input channels on the device.
- [Channel:Description:AO Channel Count](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-aochannelcount.html) Indicates the number of analog output channels on the device.
- [Channel:Description:DI Channel Count](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dichannelcount.html) Indicates the number of digital input channels on the device.
- [Channel:Description:DIFF PFI Channel Count](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diffpfichannelcount.html) Indicates the number of differential PFI channels on the device.
- [Channel:Description:DIO Channel Count](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diochannelcount.html) Indicates the number of digital I/O channels on the device.
- [Channel:Description:DO Channel Count](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dochannelcount.html) Indicates the number of digital output channels on the device.
- [Channel:Description:PFI Channel Count](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-pfichannelcount.html) Indicates the number of PFI channels on the device.
- [Channel:Description:SI Channel Count](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sichannelcount.html) Indicates the number of serial input channels on the device.
- [Channel:Description:SO Channel Count](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sochannelcount.html) Indicates the number of serial output channels on the device.
- [DIO Voltage](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diovoltage.html) Specifies the DIO voltage. By default, the voltage for the DIO pins is set in the project item under the FPGA target. The voltage can be changed at run-time (immediately) via this property. Valid values are 3.3V, 2.5V, 1.8V, 1.5V, and 1.2V. No coercion is performed, the value must be exact.
- [DSP:ADC Correction:Interleave Offset Correction Enabled](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-iocfilterenable.html) Enables the interleaving offset correction filter for the ADC. For devices with interleaving ADCs, the data stream may require additional processing to remove the interleaving spur caused by offset errors between the ADC cores. Use this property to enable or disable this functionality. This attribute is only present on devices that support this functionality.
- [Description:ADC Resolution](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcresolution.html) Indicates the number of bits of data returned to the FPGA diagram. This property applies only to FlexRIO devices with an ADC.
- [Description:ADC Sample Container](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcsamplecontainer.html) Indicates the number of bits used to represent data to the diagram. This number may be different from the number of bits of resolution. This property applies only to FlexRIO devices with an ADC.
- [Description:Bitfile:Identity](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bitfileidentity.html) Indicates the identity of the bitfile
- [Description:Bitfile:Vendor](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bitfilevendor.html) Indicates the vendor of the bitfile
- [Description:Bitfile:Version](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bitfileversion.html)
- [Description:Bus Type](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bustype.html) Indicates the bus type for the device.
- [Description:DAC Resolution](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dacresolution.html) Indicates the number of bits of data used to represent an output sample in the FPGA diagram. This property applies only to FlexRIO devices with a DAC.
- [Description:Serial Number](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-serialnumber.html) Indicates the device serial number
- [Device:ADC:Interleaving Factor](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcinterleavingfactor.html) Specifies the number of ADC cores to interleave for time-interleaved sampling. When greater than 1, this will configure the ADC to sample the enabled analog input channels with this number of interleaved ADC cores, which results in a higher effective sampling rate.
- [Device:Calibration:Date/Time](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-calibrationdate-time.html) Indicates the time of the last write to calibration storage.
- [Device:Calibration:Storage Size](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-calibrationstoragesize.html) Indicates the size in bytes of available calibration storage.
- [Device:Calibration:Temperature](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-calibrationtemperature.html) Indicates the FPGA temperature at last write to calibration storage in degrees Celsius.
- [Device:Clocking:ADC Clock Divisor](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcclockdivisor.html) Indicates the ratio between the sample clock timebase rate and the ADC sample clock.
- [Device:Clocking:ADC Sample Rate](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcsamplerate.html) Indicates the rate at which the analog-to-digital converter samples and digitizes a signal.
- [Device:Clocking:DAC Clock Divisor](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dacclockdivisor.html) Indicates the ratio between the sample clock timebase rate and the DAC sample clock.
- [Device:Clocking:DAC Sample Rate](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dacsamplerate.html) Indicates the rate at which the digital-to-analog converter outputs samples.
- [Device:Clocking:Data Clock Divisor](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dataclockdivisor.html) Indicates the ratio between the Sample Clock timebase rate and the Data Clock.
- [Device:Clocking:Data Clock Rate](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dataclockrate.html) Indicates the Data Clock rate for the I/O module.
- [Device:Clocking:FPGA TX Clock Select](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-fpgatxclockselect.html) Specifies the name of the user clock to be used as the FPGA generation clock.
- [Device:Clocking:Phase DAC Value](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-phasedacvalue.html) Specifies the value of the clock phase digital-to-analog converter (DAC).
- [Device:Clocking:Reference Clock Rate](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-referenceclockrate.html) Indicates the Reference Clock rate.
- [Device:Clocking:Reference Clock Source](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-referenceclocksource.html) Specifies the Reference Clock source.
- [Device:Clocking:Sample Clock Source](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sampleclocksource.html) Specifies the Sample Clock source.
- [Device:Clocking:Sample Clock Timebase Rate](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sampleclocktimebaserate.html) Specifies the Sample Clock timebase rate.
- [Device:Clocking:User Clock Count](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-userclockcount.html) Specifies the number of user clocks available.
- [Device:DI Equalization Enable](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diequalizationenable.html) Specifies whether equalization is enabled for all digital input channels.
- [Device:DIFF PFI Input Equalization Enable](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diffpfiinputequalizationenable.html) Specifies whether input equalization is enabled for all DIFF PFI channels.
- [Device:DIFF PFI Output Pre-Emphasis Enable](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diffpfioutputpre-emphasisenable.html) Specifies whether output pre-emphasis is enabled for all DIFF PFI channels.
- [Device:DO Pre-Emphasis Enable](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dopre-emphasisenable.html) Specifies whether pre-emphasis is enabled for all digital output channels.
- [Device:Monitoring:12V IO Power](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-12viopower.html) Indicates the power consumed by the 12V rail to the IO in watts.
- [Device:Monitoring:12V Power](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-12vpower.html) Indicates the power consumed by the 12V rail in watts.
- [Device:Monitoring:3V3 Power](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-3v3power.html) Indicates the power consumed by the 3.3V rail in watts.
- [Device:Monitoring:ADC Temperature](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adctemperature.html) Indicates the current ADC temperature in degrees Celsius.
- [Device:Monitoring:FPGA Temperature](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-fpgatemperature.html) Indicates the current FPGA temperature in degrees Celsius.
- [Device:Monitoring:IO Error](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-ioerror.html) Reports error codes when the I/O module enters an error state.
- [Device:Monitoring:IO Ready](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-ioready.html) Indicates whether the I/O is ready.
- [Device:Monitoring:Power Limit](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-powerlimit.html) Indicates the level of total power consumption in watts at which the device will shut down to prevent damage.
- [Device:Monitoring:Temperature Limit](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-temperaturelimit.html) Indicates the temperature in degrees Celsius at which the device will shut down to prevent damage.
- [Device:Monitoring:Total IO Power](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-totaliopower.html) Indicates the total power consumed by the IO module in watts.
- [Device:Monitoring:Total Power](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-totalpower.html) Indicates the total power consumed by the device in watts.
- [Device:PCI:Baseboard Reference Clock Exported](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-baseboardreferenceclockexported.html) Controls whether the baseboard reference clock is exported. When true, the baseboard reference clock is exported to the FlexRIO synchronization cable and RTSI7.
- [Device:PCI:Baseboard Reference Clock Source](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-baseboardreferenceclocksource.html) Specifies the source for the baseboard reference clock.
- [Device:PCI:Baseboard Reference PLL Locked](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-baseboardreferenceclockplllocked.html) Indicates whether the baseboard PLL is locked.
- [Device:Primary TClk Stream Instance](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-primarytclkstreaminstance.html) Specifies which stream instance is the primary stream for TClk when serving as a TClk trigger master. On devices with multiple streams, this selects the stream whose start trigger will be exported to all TClk slaves when serving as the TClk master.
- [Device:Verification:Date/Time](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-verificationdate-time.html) Indicates the time of last verification.
- [Device:Verification:Temperature](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-verificationtemperature.html) Indicates the FPGA temperature at last verification in degrees Celsius.
- [Internal:TClk Session Reference](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-tclksessionreference.html) Internal TClk session reference memory
- [PFI Voltage](../../../resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-pfivoltage.html) Specifies the PFI voltage. Valid values are 3.3V, 2.5V, 1.8V, 1.5V, and 1.2V. No coercion is performed, the value must be exact.

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-12viopower.html language=enus -->
## TOPIC 00126: Device:Monitoring:12V IO Power

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-12viopower.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-12viopower.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the power consumed by the 12V rail to the IO in watts. Remarks The following table lists the characteristics of this property. Short Name 12V IO Power Data type cdbl.png Permissions Read Only

### Device:Monitoring:12V IO Power

Indicates the power consumed by the 12V rail to the IO in watts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | 12V IO Power |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-12vpower.html language=enus -->
## TOPIC 00127: Device:Monitoring:12V Power

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-12vpower.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-12vpower.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the power consumed by the 12V rail in watts. Remarks The following table lists the characteristics of this property. Short Name 12V Power Data type cdbl.png Permissions Read Only

### Device:Monitoring:12V Power

Indicates the power consumed by the 12V rail in watts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | 12V Power |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-3v3power.html language=enus -->
## TOPIC 00128: Device:Monitoring:3V3 Power

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-3v3power.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-3v3power.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the power consumed by the 3.3V rail in watts. Remarks The following table lists the characteristics of this property. Short Name 3V3 Power Data type cdbl.png Permissions Read Only

### Device:Monitoring:3V3 Power

Indicates the power consumed by the 3.3V rail in watts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | 3V3 Power |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcclockdivisor.html language=enus -->
## TOPIC 00129: Device:Clocking:ADC Clock Divisor

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcclockdivisor.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcclockdivisor.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the ratio between the sample clock timebase rate and the ADC sample clock. Remarks The following table lists the characteristics of this property. Short Name ADC Clock Divisor Data type ci32.png Permissions Read Only

### Device:Clocking:ADC Clock Divisor

Indicates the ratio between the sample clock timebase rate and the ADC sample clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ADC Clock Divisor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcinterleavingfactor.html language=enus -->
## TOPIC 00130: Device:ADC:Interleaving Factor

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcinterleavingfactor.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcinterleavingfactor.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of ADC cores to interleave for time-interleaved sampling. When greater than 1, this will configure the ADC to sample the enabled analog input channels with this number of interleaved ADC cores, which results in a higher effective sampling rate. Remarks The following table lists

### Device:ADC:Interleaving Factor

Specifies the number of ADC cores to interleave for time-interleaved sampling. When greater than 1, this will configure the ADC to sample the enabled analog input channels with this number of interleaved ADC cores, which results in a higher effective sampling rate.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ADC Interleaving Factor |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcresolution.html language=enus -->
## TOPIC 00131: Description:ADC Resolution

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcresolution.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcresolution.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of bits of data returned to the FPGA diagram. This property applies only to FlexRIO devices with an ADC. Remarks The following table lists the characteristics of this property. Short Name ADC Resolution Data type ci32.png Permissions Read Only

### Description:ADC Resolution

Indicates the number of bits of data returned to the FPGA diagram. This property applies only to FlexRIO devices with an ADC.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ADC Resolution |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcsamplecontainer.html language=enus -->
## TOPIC 00132: Description:ADC Sample Container

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcsamplecontainer.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcsamplecontainer.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of bits used to represent data to the diagram. This number may be different from the number of bits of resolution. This property applies only to FlexRIO devices with an ADC. Remarks The following table lists the characteristics of this property. Short Name ADC Sample Container D

### Description:ADC Sample Container

Indicates the number of bits used to represent data to the diagram. This number may be different from the number of bits of resolution. This property applies only to FlexRIO devices with an ADC.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ADC Sample Container |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcsamplerate.html language=enus -->
## TOPIC 00133: Device:Clocking:ADC Sample Rate

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcsamplerate.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adcsamplerate.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the rate at which the analog-to-digital converter samples and digitizes a signal. Remarks The following table lists the characteristics of this property. Short Name ADC Sample Rate Data type cdbl.png Permissions Read Only

### Device:Clocking:ADC Sample Rate

Indicates the rate at which the analog-to-digital converter samples and digitizes a signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ADC Sample Rate |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adctemperature.html language=enus -->
## TOPIC 00134: Device:Monitoring:ADC Temperature

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adctemperature.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-adctemperature.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the current ADC temperature in degrees Celsius. Remarks The following table lists the characteristics of this property. Short Name ADC Temperature Data type cdbl.png Permissions Read Only

### Device:Monitoring:ADC Temperature

Indicates the current ADC temperature in degrees Celsius.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ADC Temperature |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-aichannelcount.html language=enus -->
## TOPIC 00135: Channel:Description:AI Channel Count

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-aichannelcount.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-aichannelcount.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of analog input channels on the device. Remarks The following table lists the characteristics of this property. Short Name AI Channel Count Data type ci32.png Permissions Read Only

### Channel:Description:AI Channel Count

Indicates the number of analog input channels on the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI Channel Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-aochannelcount.html language=enus -->
## TOPIC 00136: Channel:Description:AO Channel Count

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-aochannelcount.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-aochannelcount.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of analog output channels on the device. Remarks The following table lists the characteristics of this property. Short Name AO Channel Count Data type ci32.png Permissions Read Only

### Channel:Description:AO Channel Count

Indicates the number of analog output channels on the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO Channel Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-baseboardreferenceclockexported.html language=enus -->
## TOPIC 00137: Device:PCI:Baseboard Reference Clock Exported

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-baseboardreferenceclockexported.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-baseboardreferenceclockexported.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls whether the baseboard reference clock is exported. When true, the baseboard reference clock is exported to the FlexRIO synchronization cable and RTSI7. Remarks The following table lists the characteristics of this property. Short Name Baseboard Reference Clock Exported Data type cbool.png P

### Device:PCI:Baseboard Reference Clock Exported

Controls whether the baseboard reference clock is exported. When true, the baseboard reference clock is exported to the FlexRIO synchronization cable and RTSI7.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Baseboard Reference Clock Exported |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-baseboardreferenceclockplllocked.html language=enus -->
## TOPIC 00138: Device:PCI:Baseboard Reference PLL Locked

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-baseboardreferenceclockplllocked.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-baseboardreferenceclockplllocked.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the baseboard PLL is locked. Remarks The following table lists the characteristics of this property. Short Name Baseboard Reference Clock PLL Locked Data type cbool.png Permissions Read/Write

### Device:PCI:Baseboard Reference PLL Locked

Indicates whether the baseboard PLL is locked.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Baseboard Reference Clock PLL Locked |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-baseboardreferenceclocksource.html language=enus -->
## TOPIC 00139: Device:PCI:Baseboard Reference Clock Source

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-baseboardreferenceclocksource.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-baseboardreferenceclocksource.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source for the baseboard reference clock. Remarks The following table lists the characteristics of this property. Short Name Baseboard Reference Clock Source Data type ci32.png Permissions Read/Write Onboard 0 Synchronization Connector 1

### Device:PCI:Baseboard Reference Clock Source

Specifies the source for the baseboard reference clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Baseboard Reference Clock Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Onboard | 0 |  |
| --- | --- | --- |
| Synchronization Connector | 1 |  |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bitfileidentity.html language=enus -->
## TOPIC 00140: Description:Bitfile:Identity

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bitfileidentity.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bitfileidentity.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the identity of the bitfile Remarks The following table lists the characteristics of this property. Short Name Bitfile Identity Data type cstr.png Permissions Read Only

### Description:Bitfile:Identity

Indicates the identity of the bitfile

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Bitfile Identity |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bitfilevendor.html language=enus -->
## TOPIC 00141: Description:Bitfile:Vendor

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bitfilevendor.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bitfilevendor.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the vendor of the bitfile Remarks The following table lists the characteristics of this property. Short Name Bitfile Vendor Data type cstr.png Permissions Read Only

### Description:Bitfile:Vendor

Indicates the vendor of the bitfile

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Bitfile Vendor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bitfileversion.html language=enus -->
## TOPIC 00142: Description:Bitfile:Version

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bitfileversion.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bitfileversion.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remarks The following table lists the characteristics of this property. Short Name Bitfile Version Data type cstr.png Permissions Read Only

### Description:Bitfile:Version

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Bitfile Version |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bustype.html language=enus -->
## TOPIC 00143: Description:Bus Type

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bustype.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-bustype.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the bus type for the device. Remarks The following table lists the characteristics of this property. Short Name Bus Type Data type ci32.png Permissions Read Only PXIe 0 PCIe 1

### Description:Bus Type

Indicates the bus type for the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Bus Type |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| PXIe | 0 |  |
| --- | --- | --- |
| PCIe | 1 |  |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-calibrationdate-time.html language=enus -->
## TOPIC 00144: Device:Calibration:Date/Time

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-calibrationdate-time.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-calibrationdate-time.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the time of the last write to calibration storage. Remarks The following table lists the characteristics of this property. Short Name Calibration Date/Time Data type catrn.png Permissions Read Only

### Device:Calibration:Date/Time

Indicates the time of the last write to calibration storage.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Calibration Date/Time |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-calibrationstoragesize.html language=enus -->
## TOPIC 00145: Device:Calibration:Storage Size

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-calibrationstoragesize.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-calibrationstoragesize.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the size in bytes of available calibration storage. Remarks The following table lists the characteristics of this property. Short Name Calibration Storage Size Data type ci32.png Permissions Read/Write

### Device:Calibration:Storage Size

Indicates the size in bytes of available calibration storage.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Calibration Storage Size |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-calibrationtemperature.html language=enus -->
## TOPIC 00146: Device:Calibration:Temperature

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-calibrationtemperature.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-calibrationtemperature.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the FPGA temperature at last write to calibration storage in degrees Celsius. Remarks The following table lists the characteristics of this property. Short Name Calibration Temperature Data type cdbl.png Permissions Read Only

### Device:Calibration:Temperature

Indicates the FPGA temperature at last write to calibration storage in degrees Celsius.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Calibration Temperature |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dacclockdivisor.html language=enus -->
## TOPIC 00147: Device:Clocking:DAC Clock Divisor

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dacclockdivisor.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dacclockdivisor.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the ratio between the sample clock timebase rate and the DAC sample clock. Remarks The following table lists the characteristics of this property. Short Name DAC Clock Divisor Data type ci32.png Permissions Read Only

### Device:Clocking:DAC Clock Divisor

Indicates the ratio between the sample clock timebase rate and the DAC sample clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DAC Clock Divisor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dacresolution.html language=enus -->
## TOPIC 00148: Description:DAC Resolution

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dacresolution.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dacresolution.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of bits of data used to represent an output sample in the FPGA diagram. This property applies only to FlexRIO devices with a DAC. Remarks The following table lists the characteristics of this property. Short Name DAC Resolution Data type ci32.png Permissions Read Only

### Description:DAC Resolution

Indicates the number of bits of data used to represent an output sample in the FPGA diagram. This property applies only to FlexRIO devices with a DAC.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DAC Resolution |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dacsamplerate.html language=enus -->
## TOPIC 00149: Device:Clocking:DAC Sample Rate

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dacsamplerate.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dacsamplerate.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the rate at which the digital-to-analog converter outputs samples. Remarks The following table lists the characteristics of this property. Short Name DAC Sample Rate Data type cdbl.png Permissions Read Only

### Device:Clocking:DAC Sample Rate

Indicates the rate at which the digital-to-analog converter outputs samples.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DAC Sample Rate |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dataclockdivisor.html language=enus -->
## TOPIC 00150: Device:Clocking:Data Clock Divisor

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dataclockdivisor.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dataclockdivisor.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the ratio between the Sample Clock timebase rate and the Data Clock. Remarks The following table lists the characteristics of this property. Short Name Data Clock Divisor Data type ci32.png Permissions Read Only

### Device:Clocking:Data Clock Divisor

Indicates the ratio between the Sample Clock timebase rate and the Data Clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Clock Divisor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dataclockrate.html language=enus -->
## TOPIC 00151: Device:Clocking:Data Clock Rate

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dataclockrate.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dataclockrate.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the Data Clock rate for the I/O module. Remarks The following table lists the characteristics of this property. Short Name Data Clock Rate Data type cdbl.png Permissions Read Only

### Device:Clocking:Data Clock Rate

Indicates the Data Clock rate for the I/O module.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Clock Rate |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dichannelcount.html language=enus -->
## TOPIC 00152: Channel:Description:DI Channel Count

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dichannelcount.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dichannelcount.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of digital input channels on the device. Remarks The following table lists the characteristics of this property. Short Name DI Channel Count Data type ci32.png Permissions Read Only

### Channel:Description:DI Channel Count

Indicates the number of digital input channels on the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI Channel Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diequalizationenable.html language=enus -->
## TOPIC 00153: Device:DI Equalization Enable

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diequalizationenable.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diequalizationenable.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether equalization is enabled for all digital input channels. Remarks The following table lists the characteristics of this property. Short Name DI Equalization Enable Data type cbool.png Permissions Read/Write

### Device:DI Equalization Enable

Specifies whether equalization is enabled for all digital input channels.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI Equalization Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diffpfichannelcount.html language=enus -->
## TOPIC 00154: Channel:Description:DIFF PFI Channel Count

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diffpfichannelcount.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diffpfichannelcount.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of differential PFI channels on the device. Remarks The following table lists the characteristics of this property. Short Name DIFF PFI Channel Count Data type ci32.png Permissions Read Only

### Channel:Description:DIFF PFI Channel Count

Indicates the number of differential PFI channels on the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DIFF PFI Channel Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diffpfiinputequalizationenable.html language=enus -->
## TOPIC 00155: Device:DIFF PFI Input Equalization Enable

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diffpfiinputequalizationenable.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diffpfiinputequalizationenable.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether input equalization is enabled for all DIFF PFI channels. Remarks The following table lists the characteristics of this property. Short Name DIFF PFI Input Equalization Enable Data type cbool.png Permissions Read/Write

### Device:DIFF PFI Input Equalization Enable

Specifies whether input equalization is enabled for all DIFF PFI channels.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DIFF PFI Input Equalization Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diffpfioutputpre-emphasisenable.html language=enus -->
## TOPIC 00156: Device:DIFF PFI Output Pre-Emphasis Enable

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diffpfioutputpre-emphasisenable.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diffpfioutputpre-emphasisenable.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether output pre-emphasis is enabled for all DIFF PFI channels. Remarks The following table lists the characteristics of this property. Short Name DIFF PFI Output Pre-Emphasis Enable Data type cbool.png Permissions Read/Write

### Device:DIFF PFI Output Pre-Emphasis Enable

Specifies whether output pre-emphasis is enabled for all DIFF PFI channels.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DIFF PFI Output Pre-Emphasis Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diochannelcount.html language=enus -->
## TOPIC 00157: Channel:Description:DIO Channel Count

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diochannelcount.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diochannelcount.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of digital I/O channels on the device. Remarks The following table lists the characteristics of this property. Short Name DIO Channel Count Data type ci32.png Permissions Read Only

### Channel:Description:DIO Channel Count

Indicates the number of digital I/O channels on the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DIO Channel Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diovoltage.html language=enus -->
## TOPIC 00158: DIO Voltage

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diovoltage.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-diovoltage.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DIO voltage. By default, the voltage for the DIO pins is set in the project item under the FPGA target. The voltage can be changed at run-time (immediately) via this property. Valid values are 3.3V, 2.5V, 1.8V, 1.5V, and 1.2V. No coercion is performed, the value must be exact. Remarks

### DIO Voltage

Specifies the DIO voltage. By default, the voltage for the DIO pins is set in the project item under the FPGA target. The voltage can be changed at run-time (immediately) via this property. Valid values are 3.3V, 2.5V, 1.8V, 1.5V, and 1.2V. No coercion is performed, the value must be exact.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DIO Voltage |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dochannelcount.html language=enus -->
## TOPIC 00159: Channel:Description:DO Channel Count

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dochannelcount.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dochannelcount.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of digital output channels on the device. Remarks The following table lists the characteristics of this property. Short Name DO Channel Count Data type ci32.png Permissions Read Only

### Channel:Description:DO Channel Count

Indicates the number of digital output channels on the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO Channel Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dopre-emphasisenable.html language=enus -->
## TOPIC 00160: Device:DO Pre-Emphasis Enable

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dopre-emphasisenable.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-dopre-emphasisenable.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether pre-emphasis is enabled for all digital output channels. Remarks The following table lists the characteristics of this property. Short Name DO Pre-Emphasis Enable Data type cbool.png Permissions Read/Write

### Device:DO Pre-Emphasis Enable

Specifies whether pre-emphasis is enabled for all digital output channels.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO Pre-Emphasis Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-fpgatemperature.html language=enus -->
## TOPIC 00161: Device:Monitoring:FPGA Temperature

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-fpgatemperature.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-fpgatemperature.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the current FPGA temperature in degrees Celsius. Remarks The following table lists the characteristics of this property. Short Name FPGA Temperature Data type cdbl.png Permissions Read Only

### Device:Monitoring:FPGA Temperature

Indicates the current FPGA temperature in degrees Celsius.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FPGA Temperature |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-fpgatxclockselect.html language=enus -->
## TOPIC 00162: Device:Clocking:FPGA TX Clock Select

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-fpgatxclockselect.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-fpgatxclockselect.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of the user clock to be used as the FPGA generation clock. Remarks The following table lists the characteristics of this property. Short Name FPGA TX Clock Select Data type cstr.png Permissions Read/Write

### Device:Clocking:FPGA TX Clock Select

Specifies the name of the user clock to be used as the FPGA generation clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FPGA TX Clock Select |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-iocfilterenable.html language=enus -->
## TOPIC 00163: DSP:ADC Correction:Interleave Offset Correction Enabled

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-iocfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-iocfilterenable.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the interleaving offset correction filter for the ADC. For devices with interleaving ADCs, the data stream may require additional processing to remove the interleaving spur caused by offset errors between the ADC cores. Use this property to enable or disable this functionality. This attribut

### DSP:ADC Correction:Interleave Offset Correction Enabled

Enables the interleaving offset correction filter for the ADC. For devices with interleaving ADCs, the data stream may require additional processing to remove the interleaving spur caused by offset errors between the ADC cores. Use this property to enable or disable this functionality. This attribute is only present on devices that support this functionality.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IOC Filter Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-ioerror.html language=enus -->
## TOPIC 00164: Device:Monitoring:IO Error

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-ioerror.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-ioerror.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reports error codes when the I/O module enters an error state. Remarks The following table lists the characteristics of this property. Short Name IO Error Data type ci32.png Permissions Read/Write

### Device:Monitoring:IO Error

Reports error codes when the I/O module enters an error state.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IO Error |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-ioready.html language=enus -->
## TOPIC 00165: Device:Monitoring:IO Ready

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-ioready.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-ioready.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the I/O is ready. Remarks The following table lists the characteristics of this property. Short Name IO Ready Data type cbool.png Permissions Read/Write

### Device:Monitoring:IO Ready

Indicates whether the I/O is ready.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IO Ready |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-pfichannelcount.html language=enus -->
## TOPIC 00166: Channel:Description:PFI Channel Count

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-pfichannelcount.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-pfichannelcount.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of PFI channels on the device. Remarks The following table lists the characteristics of this property. Short Name PFI Channel Count Data type ci32.png Permissions Read Only

### Channel:Description:PFI Channel Count

Indicates the number of PFI channels on the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PFI Channel Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-pfivoltage.html language=enus -->
## TOPIC 00167: PFI Voltage

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-pfivoltage.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-pfivoltage.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the PFI voltage. Valid values are 3.3V, 2.5V, 1.8V, 1.5V, and 1.2V. No coercion is performed, the value must be exact. Remarks The following table lists the characteristics of this property. Short Name PFI Voltage Data type cdbl.png Permissions Read/Write

### PFI Voltage

Specifies the PFI voltage. Valid values are 3.3V, 2.5V, 1.8V, 1.5V, and 1.2V. No coercion is performed, the value must be exact.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PFI Voltage |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-phasedacvalue.html language=enus -->
## TOPIC 00168: Device:Clocking:Phase DAC Value

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-phasedacvalue.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-phasedacvalue.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the clock phase digital-to-analog converter (DAC). Remarks The following table lists the characteristics of this property. Short Name Phase DAC Value Data type ci32.png Permissions Read/Write

### Device:Clocking:Phase DAC Value

Specifies the value of the clock phase digital-to-analog converter (DAC).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Phase DAC Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-powerlimit.html language=enus -->
## TOPIC 00169: Device:Monitoring:Power Limit

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-powerlimit.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-powerlimit.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the level of total power consumption in watts at which the device will shut down to prevent damage. Remarks The following table lists the characteristics of this property. Short Name Power Limit Data type cdbl.png Permissions Read Only

### Device:Monitoring:Power Limit

Indicates the level of total power consumption in watts at which the device will shut down to prevent damage.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Power Limit |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-primarytclkstreaminstance.html language=enus -->
## TOPIC 00170: Device:Primary TClk Stream Instance

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-primarytclkstreaminstance.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-primarytclkstreaminstance.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which stream instance is the primary stream for TClk when serving as a TClk trigger master. On devices with multiple streams, this selects the stream whose start trigger will be exported to all TClk slaves when serving as the TClk master. Remarks The following table lists the characteristi

### Device:Primary TClk Stream Instance

Specifies which stream instance is the primary stream for TClk when serving as a TClk trigger master. On devices with multiple streams, this selects the stream whose start trigger will be exported to all TClk slaves when serving as the TClk master.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Primary TClk Stream Instance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-referenceclockrate.html language=enus -->
## TOPIC 00171: Device:Clocking:Reference Clock Rate

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-referenceclockrate.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-referenceclockrate.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the Reference Clock rate. Remarks The following table lists the characteristics of this property. Short Name Reference Clock Rate Data type cdbl.png Permissions Read/Write

### Device:Clocking:Reference Clock Rate

Indicates the Reference Clock rate.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Reference Clock Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-referenceclocksource.html language=enus -->
## TOPIC 00172: Device:Clocking:Reference Clock Source

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-referenceclocksource.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-referenceclocksource.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Reference Clock source. Remarks The following table lists the characteristics of this property. Short Name Reference Clock Source Data type ci32.png Permissions Read/Write Default 0 Onboard 1 PXI_Clk10 2 External 3 None 4 Baseboard Reference 5 PXI_Clk100 6

### Device:Clocking:Reference Clock Source

Specifies the Reference Clock source.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Reference Clock Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Default | 0 |  |
| --- | --- | --- |
| Onboard | 1 |  |
| PXI_Clk10 | 2 |  |
| External | 3 |  |
| None | 4 |  |
| Baseboard Reference | 5 |  |
| PXI_Clk100 | 6 |  |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sampleclocksource.html language=enus -->
## TOPIC 00173: Device:Clocking:Sample Clock Source

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sampleclocksource.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sampleclocksource.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Sample Clock source. Remarks The following table lists the characteristics of this property. Short Name Sample Clock Source Data type ci32.png Permissions Read/Write Internal 0 Front Panel 1

### Device:Clocking:Sample Clock Source

Specifies the Sample Clock source.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample Clock Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Internal | 0 |  |
| --- | --- | --- |
| Front Panel | 1 |  |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sampleclocktimebaserate.html language=enus -->
## TOPIC 00174: Device:Clocking:Sample Clock Timebase Rate

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sampleclocktimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sampleclocktimebaserate.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Sample Clock timebase rate. Remarks The following table lists the characteristics of this property. Short Name Sample Clock Timebase Rate Data type cdbl.png Permissions Read/Write

### Device:Clocking:Sample Clock Timebase Rate

Specifies the Sample Clock timebase rate.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample Clock Timebase Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-serialnumber.html language=enus -->
## TOPIC 00175: Description:Serial Number

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-serialnumber.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-serialnumber.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the device serial number Remarks The following table lists the characteristics of this property. Short Name Serial Number Data type cstr.png Permissions Read Only

### Description:Serial Number

Indicates the device serial number

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Serial Number |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sichannelcount.html language=enus -->
## TOPIC 00176: Channel:Description:SI Channel Count

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sichannelcount.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sichannelcount.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of serial input channels on the device. Remarks The following table lists the characteristics of this property. Short Name SI Channel Count Data type ci32.png Permissions Read Only

### Channel:Description:SI Channel Count

Indicates the number of serial input channels on the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SI Channel Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sochannelcount.html language=enus -->
## TOPIC 00177: Channel:Description:SO Channel Count

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sochannelcount.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-sochannelcount.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of serial output channels on the device. Remarks The following table lists the characteristics of this property. Short Name SO Channel Count Data type ci32.png Permissions Read Only

### Channel:Description:SO Channel Count

Indicates the number of serial output channels on the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SO Channel Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-tclksessionreference.html language=enus -->
## TOPIC 00178: Internal:TClk Session Reference

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-tclksessionreference.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-tclksessionreference.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Internal TClk session reference memory Remarks The following table lists the characteristics of this property. Short Name TClk Session Reference Data type ci32.png Permissions Read/Write

### Internal:TClk Session Reference

Internal TClk session reference memory

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TClk Session Reference |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-temperaturelimit.html language=enus -->
## TOPIC 00179: Device:Monitoring:Temperature Limit

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-temperaturelimit.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-temperaturelimit.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the temperature in degrees Celsius at which the device will shut down to prevent damage. Remarks The following table lists the characteristics of this property. Short Name Temperature Limit Data type cdbl.png Permissions Read Only

### Device:Monitoring:Temperature Limit

Indicates the temperature in degrees Celsius at which the device will shut down to prevent damage.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Temperature Limit |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-totaliopower.html language=enus -->
## TOPIC 00180: Device:Monitoring:Total IO Power

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-totaliopower.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-totaliopower.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the total power consumed by the IO module in watts. Remarks The following table lists the characteristics of this property. Short Name Total IO Power Data type cdbl.png Permissions Read Only

### Device:Monitoring:Total IO Power

Indicates the total power consumed by the IO module in watts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Total IO Power |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-totalpower.html language=enus -->
## TOPIC 00181: Device:Monitoring:Total Power

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-totalpower.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-totalpower.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the total power consumed by the device in watts. Remarks The following table lists the characteristics of this property. Short Name Total Power Data type cdbl.png Permissions Read Only

### Device:Monitoring:Total Power

Indicates the total power consumed by the device in watts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Total Power |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-userclockcount.html language=enus -->
## TOPIC 00182: Device:Clocking:User Clock Count

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-userclockcount.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-userclockcount.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of user clocks available. Remarks The following table lists the characteristics of this property. Short Name User Clock Count Data type ci32.png Permissions Read Only

### Device:Clocking:User Clock Count

Specifies the number of user clocks available.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | User Clock Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-verificationdate-time.html language=enus -->
## TOPIC 00183: Device:Verification:Date/Time

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-verificationdate-time.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-verificationdate-time.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the time of last verification. Remarks The following table lists the characteristics of this property. Short Name Verification Date/Time Data type catrn.png Permissions Read Only

### Device:Verification:Date/Time

Indicates the time of last verification.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Verification Date/Time |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-verificationtemperature.html language=enus -->
## TOPIC 00184: Device:Verification:Temperature

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-verificationtemperature.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapi-rc/niflexrioapisession/pniflexrio-verificationtemperature.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the FPGA temperature at last verification in degrees Celsius. Remarks The following table lists the characteristics of this property. Short Name Verification Temperature Data type cdbl.png Permissions Read Only

### Device:Verification:Temperature

Indicates the FPGA temperature at last verification in degrees Celsius.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Verification Temperature |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel-p.html language=enus -->
## TOPIC 00185: FlexRIO Channel Properties

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel-p.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel-p.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### FlexRIO Channel Properties

- [Active Channel](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-activechannel.html) Specifies the channel name (e.g. 'AI0' or 'AO0') used to access all subsequent properties in this instance of the property node. You must first select this property and then pass the name of the specific channel.
- [Analog Input:Advanced:Decimation Filter Band](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aidecimationfilterband.html) Specifies a highpass or lowpass filter response for the ADC decimation filter. If the signal resides in the first Nyquist zone, use the lowpass filter. If the signal resides in the second Nyquist zone, use the highpass filter. This property is for use in undersampling applications.
- [Analog Input:Advanced:Nyquist Zone](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-ainyquistzone.html) Specifies the Nyquist Zone in which the input signal resides. This property is for use in undersampling applications and is useful for improving interleaving spur performance.
- [Analog Input:CableSense:CableSense Mode](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-cablesensemode.html) Specifies whether the CableSense signal will be generated on the specified channel.
- [Analog Input:Coupling](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aicoupling.html) Specifies the coupling of the channel.
- [Analog Input:Enabled](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aichannelenabled.html) Specifies whether the active channel is enabled.
- [Analog Input:Impedance](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aiimpedance.html) Specifies the impedance of the channel in ohms.
- [Analog Input:Offset](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aioffset.html) Specifies the vertical offset of the channel in volts.
- [Analog Input:Offset DAC](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aioffsetdac.html) Specifies the vertical offset of the channel in DAC codes. Setting this property will cause the value of the AI Offset property to be ignored.
- [Analog Input:Range](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-airange.html) Specifies the vertical range of the channel in volts.
- [Analog Input:Scaling:Gain](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aiscalinggain.html) Specifies the ratio between volts and ADC codes on the channel data.
- [Analog Input:Scaling:Offset](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aiscalingoffset.html) Specifies the offset between volts and ADC codes on the channel data.
- [Analog Output:Advanced:Inverse Sinc Filter Enabled](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoinv-sincfilterenabled.html) Enables the inverse sinc filter for the channel.
- [Analog Output:Channel Status](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aochannelstatus.html) Indicates the status of the channel.
- [Analog Output:DAC Digital Upconverter Enabled](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-dacdigitalupconverterenabled.html) If true, this channel's output will be sourced from the DAC's digital upconverter. The user is expected to provide a complex waveform that will be properly steered to the DAC channels.
- [Analog Output:Impedance](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoimpedance.html) Specifies the impedance of the channel in ohms.
- [Analog Output:Range](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aorange.html) Specifies the vertical range of the channel in volts.
- [Analog Output:Scaling:Gain](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoscalinggain.html) Specifies the ratio between volts and DAC codes on the channel data.
- [Analog Output:Scaling:Offset](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoscalingoffset.html) Specifies the offset between volts and DAC codes on the channel data.
- [DIFF PFI:Line Configuration](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-diffpfilineconfig.html) Specifies the line direction of the active channel.
- [DIO:Line Configuration](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-diolineconfig.html) Specifies the line direction of the active channel.
- [DIO:Line Voltage](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-diolinevoltage.html) Specifies the DIO line voltage.
- [DSP:Frequency Shift:Advanced:Magnitude](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-dspfrequencyshiftmagnitude.html) Directly specifies the magnitude of the frequency shift applied to the signal. This is intended for advanced users who need to directly configure the magnitude without the units of the API.
- [DSP:Frequency Shift:Shift in Hertz](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-dspfrequencyshift.html) When DSP is enabled, this attribute specifies the amount that the frequency spectrum will be shifted. For input streams, this means shifting the frequency spectrum down by the specified frequency. For output streams, this means shifting the spectrum up by the specified frequency.
- [PFI:Line Configuration](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-pfilineconfig.html) Specifies the line direction of the active channel.
- [Serial Input:CSI-2 Interface:Number of Lanes](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sicsi-2lanes.html) Specifies the number of active CSI-2 lanes.
- [Serial Input:Deserializer:I2C Bus Instance Name](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sii2cname.html) Indicates the name of the I2C bus instance associated with the specified serial input channel.
- [Serial Input:Deserializer:Reference Clock Enabled](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sirefclkenabled.html) Specifies whether the reference clock is enabled.
- [Serial Input:Deserializer:Reference Clock Frequency](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sirefclkfrequency.html) Specifies the reference clock associated with the serial input channel.
- [Serial Input:Deserializer:Reference Clock Name](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sirefclkname.html) Indicates the name of the reference clock associated with the specified serial input channel.
- [Serial Input:Power Over Coax:Power Over Coax Current](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipoccurrent.html) Indicates the power over coax current in amps on the specified serial input channel.
- [Serial Input:Power Over Coax:Power Over Coax In Range](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipocinrange.html) Indicates whether power over coax is enabled, above the minimum valid voltage, and not receiving a fault signal on the specified serial input channel.
- [Serial Input:Power Over Coax:Power Over Coax Source](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipocsource.html) Configures the power over coax source on the specified serial input channel.
- [Serial Input:Power Over Coax:Power Over Coax Voltage](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipocvoltage.html) Indicates the power over coax voltage on the specified serial input channel.
- [Serial Output:CSI-2 Interface:Data Rate](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-socsi-2datarate.html) Specifies the CSI-2 data rate.
- [Serial Output:CSI-2 Interface:Data Rate Clock Name](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sodataclkname.html) Indicates the name of the CSI-2 data rate clock associated with the specified serial output channel.
- [Serial Output:CSI-2 Interface:Number of Lanes](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-socsi-2lanes.html) Specifies the number of active CSI-2 lanes.
- [Serial Output:Power Over Coax:Power Over Coax Current](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopoccurrent.html) Indicates the power over coax current in amps on the specified serial output channel.
- [Serial Output:Power Over Coax:Power Over Coax In Range](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopocinrange.html) Indicates whether power over coax is enabled, above the minimum valid voltage, and not receiving a fault signal on the specified serial output channel.
- [Serial Output:Power Over Coax:Power Over Coax Sink](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopocsink.html) Configures the power over coax sink on the specified serial output channel.
- [Serial Output:Power Over Coax:Power Over Coax Voltage](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopocvoltage.html) Indicates the power over coax voltage on the specified serial output channel.
- [Serial Output:Serializer:I2C Bus Instance Name](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-soi2cname.html) Indicates the name of the I2C bus instance associated with the specified serial output channel.
- [Serial Output:Serializer:Reference Clock Enabled](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sorefclkenabled.html) Specifies whether the reference clock is enabled.
- [Serial Output:Serializer:Reference Clock Frequency](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sorefclkfrequency.html) Specifies the reference clock associated with the serial output channel.
- [Serial Output:Serializer:Reference Clock Name](../../../resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sorefclkname.html) Indicates the name of the reference clock associated with the specified serial output channel.

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-activechannel.html language=enus -->
## TOPIC 00186: Active Channel

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-activechannel.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-activechannel.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel name (e.g. 'AI0' or 'AO0') used to access all subsequent properties in this instance of the property node. You must first select this property and then pass the name of the specific channel. Remarks The following table lists the characteristics of this property. Short Name Acti

### Active Channel

Specifies the channel name (e.g. 'AI0' or 'AO0') used to access all subsequent properties in this instance of the property node. You must first select this property and then pass the name of the specific channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Active Channel |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aichannelenabled.html language=enus -->
## TOPIC 00187: Analog Input:Enabled

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aichannelenabled.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aichannelenabled.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the active channel is enabled. Remarks The following table lists the characteristics of this property. Short Name AI Channel Enabled Data type cbool.png Permissions Read/Write

### Analog Input:Enabled

Specifies whether the active channel is enabled.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI Channel Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aicoupling.html language=enus -->
## TOPIC 00188: Analog Input:Coupling

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aicoupling.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aicoupling.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling of the channel. Remarks The following table lists the characteristics of this property. Short Name AI Coupling Data type ci32.png Permissions Read/Write AC 0 DC 1

### Analog Input:Coupling

Specifies the coupling of the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI Coupling |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| AC | 0 |  |
| --- | --- | --- |
| DC | 1 |  |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aidecimationfilterband.html language=enus -->
## TOPIC 00189: Analog Input:Advanced:Decimation Filter Band

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aidecimationfilterband.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aidecimationfilterband.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a highpass or lowpass filter response for the ADC decimation filter. If the signal resides in the first Nyquist zone, use the lowpass filter. If the signal resides in the second Nyquist zone, use the highpass filter. This property is for use in undersampling applications. Remarks The follo

### Analog Input:Advanced:Decimation Filter Band

Specifies a highpass or lowpass filter response for the ADC decimation filter. If the signal resides in the first Nyquist zone, use the lowpass filter. If the signal resides in the second Nyquist zone, use the highpass filter. This property is for use in undersampling applications.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI Decimation Filter Band |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aiimpedance.html language=enus -->
## TOPIC 00190: Analog Input:Impedance

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aiimpedance.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aiimpedance.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the impedance of the channel in ohms. Remarks The following table lists the characteristics of this property. Short Name AI Impedance Data type cdbl.png Permissions Read/Write

### Analog Input:Impedance

Specifies the impedance of the channel in ohms.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI Impedance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-ainyquistzone.html language=enus -->
## TOPIC 00191: Analog Input:Advanced:Nyquist Zone

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-ainyquistzone.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-ainyquistzone.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Nyquist Zone in which the input signal resides. This property is for use in undersampling applications and is useful for improving interleaving spur performance. Remarks The following table lists the characteristics of this property. Short Name AI Nyquist Zone Data type ci32.png Permis

### Analog Input:Advanced:Nyquist Zone

Specifies the Nyquist Zone in which the input signal resides. This property is for use in undersampling applications and is useful for improving interleaving spur performance.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI Nyquist Zone |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aioffset.html language=enus -->
## TOPIC 00192: Analog Input:Offset

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aioffset.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aioffset.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the vertical offset of the channel in volts. Remarks The following table lists the characteristics of this property. Short Name AI Offset Data type cdbl.png Permissions Read/Write

### Analog Input:Offset

Specifies the vertical offset of the channel in volts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aioffsetdac.html language=enus -->
## TOPIC 00193: Analog Input:Offset DAC

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aioffsetdac.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aioffsetdac.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the vertical offset of the channel in DAC codes. Setting this property will cause the value of the AI Offset property to be ignored. Remarks The following table lists the characteristics of this property. Short Name AI Offset DAC Data type ci32.png Permissions Read/Write

### Analog Input:Offset DAC

Specifies the vertical offset of the channel in DAC codes. Setting this property will cause the value of the AI Offset property to be ignored.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI Offset DAC |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-airange.html language=enus -->
## TOPIC 00194: Analog Input:Range

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-airange.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-airange.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the vertical range of the channel in volts. Remarks The following table lists the characteristics of this property. Short Name AI Range Data type cdbl.png Permissions Read/Write

### Analog Input:Range

Specifies the vertical range of the channel in volts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aiscalinggain.html language=enus -->
## TOPIC 00195: Analog Input:Scaling:Gain

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aiscalinggain.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aiscalinggain.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ratio between volts and ADC codes on the channel data. Remarks The following table lists the characteristics of this property. Short Name AI Scaling Gain Data type cdbl.png Permissions Read/Write

### Analog Input:Scaling:Gain

Specifies the ratio between volts and ADC codes on the channel data.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI Scaling Gain |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aiscalingoffset.html language=enus -->
## TOPIC 00196: Analog Input:Scaling:Offset

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aiscalingoffset.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aiscalingoffset.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset between volts and ADC codes on the channel data. Remarks The following table lists the characteristics of this property. Short Name AI Scaling Offset Data type cdbl.png Permissions Read/Write

### Analog Input:Scaling:Offset

Specifies the offset between volts and ADC codes on the channel data.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI Scaling Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aochannelstatus.html language=enus -->
## TOPIC 00197: Analog Output:Channel Status

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aochannelstatus.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aochannelstatus.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the status of the channel. Remarks The following table lists the characteristics of this property. Short Name AO Channel Status Data type ci32.png Permissions Read Only Normal 0 Overpower 1 Overtemperature 2

### Analog Output:Channel Status

Indicates the status of the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO Channel Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

| Normal | 0 |  |
| --- | --- | --- |
| Overpower | 1 |  |
| Overtemperature | 2 |  |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoimpedance.html language=enus -->
## TOPIC 00198: Analog Output:Impedance

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoimpedance.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoimpedance.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the impedance of the channel in ohms. Remarks The following table lists the characteristics of this property. Short Name AO Impedance Data type cdbl.png Permissions Read Only

### Analog Output:Impedance

Specifies the impedance of the channel in ohms.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO Impedance |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoinv-sincfilterenabled.html language=enus -->
## TOPIC 00199: Analog Output:Advanced:Inverse Sinc Filter Enabled

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoinv-sincfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoinv-sincfilterenabled.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the inverse sinc filter for the channel. Remarks The following table lists the characteristics of this property. Short Name AO Inv. Sinc Filter Enabled Data type cbool.png Permissions Read/Write

### Analog Output:Advanced:Inverse Sinc Filter Enabled

Enables the inverse sinc filter for the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO Inv. Sinc Filter Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aorange.html language=enus -->
## TOPIC 00200: Analog Output:Range

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aorange.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aorange.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the vertical range of the channel in volts. Remarks The following table lists the characteristics of this property. Short Name AO Range Data type cdbl.png Permissions Read/Write

### Analog Output:Range

Specifies the vertical range of the channel in volts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoscalinggain.html language=enus -->
## TOPIC 00201: Analog Output:Scaling:Gain

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoscalinggain.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoscalinggain.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ratio between volts and DAC codes on the channel data. Remarks The following table lists the characteristics of this property. Short Name AO Scaling Gain Data type cdbl.png Permissions Read/Write

### Analog Output:Scaling:Gain

Specifies the ratio between volts and DAC codes on the channel data.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO Scaling Gain |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoscalingoffset.html language=enus -->
## TOPIC 00202: Analog Output:Scaling:Offset

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoscalingoffset.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-aoscalingoffset.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset between volts and DAC codes on the channel data. Remarks The following table lists the characteristics of this property. Short Name AO Scaling Offset Data type cdbl.png Permissions Read/Write

### Analog Output:Scaling:Offset

Specifies the offset between volts and DAC codes on the channel data.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO Scaling Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-cablesensemode.html language=enus -->
## TOPIC 00203: Analog Input:CableSense:CableSense Mode

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-cablesensemode.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-cablesensemode.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the CableSense signal will be generated on the specified channel. Remarks The following table lists the characteristics of this property. Short Name CableSense Mode Data type ci32.png Permissions Read/Write Disabled 0 On Demand 1

### Analog Input:CableSense:CableSense Mode

Specifies whether the CableSense signal will be generated on the specified channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CableSense Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Disabled | 0 |  |
| --- | --- | --- |
| On Demand | 1 |  |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-dacdigitalupconverterenabled.html language=enus -->
## TOPIC 00204: Analog Output:DAC Digital Upconverter Enabled

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-dacdigitalupconverterenabled.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-dacdigitalupconverterenabled.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: If true, this channel's output will be sourced from the DAC's digital upconverter. The user is expected to provide a complex waveform that will be properly steered to the DAC channels. Remarks The following table lists the characteristics of this property. Short Name DAC Digital Upconverter Enabled

### Analog Output:DAC Digital Upconverter Enabled

If true, this channel's output will be sourced from the DAC's digital upconverter. The user is expected to provide a complex waveform that will be properly steered to the DAC channels.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DAC Digital Upconverter Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-diffpfilineconfig.html language=enus -->
## TOPIC 00205: DIFF PFI:Line Configuration

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-diffpfilineconfig.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-diffpfilineconfig.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the line direction of the active channel. Remarks The following table lists the characteristics of this property. Short Name DIFF PFI Line Config Data type ci32.png Permissions Read/Write Input 0 Output 1

### DIFF PFI:Line Configuration

Specifies the line direction of the active channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DIFF PFI Line Config |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Input | 0 |  |
| --- | --- | --- |
| Output | 1 |  |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-diolineconfig.html language=enus -->
## TOPIC 00206: DIO:Line Configuration

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-diolineconfig.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-diolineconfig.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the line direction of the active channel. Remarks The following table lists the characteristics of this property. Short Name DIO Line Config Data type ci32.png Permissions Read/Write Input 0 Output 1

### DIO:Line Configuration

Specifies the line direction of the active channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DIO Line Config |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Input | 0 |  |
| --- | --- | --- |
| Output | 1 |  |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-diolinevoltage.html language=enus -->
## TOPIC 00207: DIO:Line Voltage

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-diolinevoltage.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-diolinevoltage.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DIO line voltage. Remarks The following table lists the characteristics of this property. Short Name DIO Line Voltage Data type cdbl.png Permissions Read/Write

### DIO:Line Voltage

Specifies the DIO line voltage.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DIO Line Voltage |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-dspfrequencyshift.html language=enus -->
## TOPIC 00208: DSP:Frequency Shift:Shift in Hertz

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-dspfrequencyshift.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-dspfrequencyshift.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: When DSP is enabled, this attribute specifies the amount that the frequency spectrum will be shifted. For input streams, this means shifting the frequency spectrum down by the specified frequency. For output streams, this means shifting the spectrum up by the specified frequency. Remarks The followi

### DSP:Frequency Shift:Shift in Hertz

When DSP is enabled, this attribute specifies the amount that the frequency spectrum will be shifted. For input streams, this means shifting the frequency spectrum down by the specified frequency. For output streams, this means shifting the spectrum up by the specified frequency.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DSP Frequency Shift |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-dspfrequencyshiftmagnitude.html language=enus -->
## TOPIC 00209: DSP:Frequency Shift:Advanced:Magnitude

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-dspfrequencyshiftmagnitude.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-dspfrequencyshiftmagnitude.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Directly specifies the magnitude of the frequency shift applied to the signal. This is intended for advanced users who need to directly configure the magnitude without the units of the API. Remarks The following table lists the characteristics of this property. Short Name DSP Frequency Shift Magnitu

### DSP:Frequency Shift:Advanced:Magnitude

Directly specifies the magnitude of the frequency shift applied to the signal. This is intended for advanced users who need to directly configure the magnitude without the units of the API.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DSP Frequency Shift Magnitude |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-pfilineconfig.html language=enus -->
## TOPIC 00210: PFI:Line Configuration

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-pfilineconfig.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-pfilineconfig.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the line direction of the active channel. Remarks The following table lists the characteristics of this property. Short Name PFI Line Config Data type ci32.png Permissions Read/Write Input 0 Output 1

### PFI:Line Configuration

Specifies the line direction of the active channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PFI Line Config |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| Input | 0 |  |
| --- | --- | --- |
| Output | 1 |  |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sicsi-2lanes.html language=enus -->
## TOPIC 00211: Serial Input:CSI-2 Interface:Number of Lanes

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sicsi-2lanes.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sicsi-2lanes.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of active CSI-2 lanes. Remarks The following table lists the characteristics of this property. Short Name SI CSI-2 Lanes Data type ci32.png Permissions Read/Write 1 1 2 2 4 4

### Serial Input:CSI-2 Interface:Number of Lanes

Specifies the number of active CSI-2 lanes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SI CSI-2 Lanes |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| 1 | 1 |  |
| --- | --- | --- |
| 2 | 2 |  |
| 4 | 4 |  |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sii2cname.html language=enus -->
## TOPIC 00212: Serial Input:Deserializer:I2C Bus Instance Name

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sii2cname.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sii2cname.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the I2C bus instance associated with the specified serial input channel. Remarks The following table lists the characteristics of this property. Short Name SI I2C Name Data type cstr.png Permissions Read Only

### Serial Input:Deserializer:I2C Bus Instance Name

Indicates the name of the I2C bus instance associated with the specified serial input channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SI I2C Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipoccurrent.html language=enus -->
## TOPIC 00213: Serial Input:Power Over Coax:Power Over Coax Current

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipoccurrent.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipoccurrent.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the power over coax current in amps on the specified serial input channel. Remarks The following table lists the characteristics of this property. Short Name SI PoC Current Data type cdbl.png Permissions Read Only

### Serial Input:Power Over Coax:Power Over Coax Current

Indicates the power over coax current in amps on the specified serial input channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SI PoC Current |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipocinrange.html language=enus -->
## TOPIC 00214: Serial Input:Power Over Coax:Power Over Coax In Range

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipocinrange.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipocinrange.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether power over coax is enabled, above the minimum valid voltage, and not receiving a fault signal on the specified serial input channel. Remarks The following table lists the characteristics of this property. Short Name SI PoC In Range Data type cbool.png Permissions Read Only

### Serial Input:Power Over Coax:Power Over Coax In Range

Indicates whether power over coax is enabled, above the minimum valid voltage, and not receiving a fault signal on the specified serial input channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SI PoC In Range |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipocsource.html language=enus -->
## TOPIC 00215: Serial Input:Power Over Coax:Power Over Coax Source

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipocsource.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipocsource.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the power over coax source on the specified serial input channel. Remarks The following table lists the characteristics of this property. Short Name SI PoC Source Data type ci32.png Permissions Read/Write None 0 Internal 1 Auxiliary 2

### Serial Input:Power Over Coax:Power Over Coax Source

Configures the power over coax source on the specified serial input channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SI PoC Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| None | 0 |  |
| --- | --- | --- |
| Internal | 1 |  |
| Auxiliary | 2 |  |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipocvoltage.html language=enus -->
## TOPIC 00216: Serial Input:Power Over Coax:Power Over Coax Voltage

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipocvoltage.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sipocvoltage.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the power over coax voltage on the specified serial input channel. Remarks The following table lists the characteristics of this property. Short Name SI PoC Voltage Data type cdbl.png Permissions Read Only

### Serial Input:Power Over Coax:Power Over Coax Voltage

Indicates the power over coax voltage on the specified serial input channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SI PoC Voltage |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sirefclkenabled.html language=enus -->
## TOPIC 00217: Serial Input:Deserializer:Reference Clock Enabled

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sirefclkenabled.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sirefclkenabled.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the reference clock is enabled. Remarks The following table lists the characteristics of this property. Short Name SI RefClk Enabled Data type cbool.png Permissions Read/Write

### Serial Input:Deserializer:Reference Clock Enabled

Specifies whether the reference clock is enabled.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SI RefClk Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sirefclkfrequency.html language=enus -->
## TOPIC 00218: Serial Input:Deserializer:Reference Clock Frequency

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sirefclkfrequency.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sirefclkfrequency.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference clock associated with the serial input channel. Remarks The following table lists the characteristics of this property. Short Name SI RefClk Frequency Data type cdbl.png Permissions Read/Write

### Serial Input:Deserializer:Reference Clock Frequency

Specifies the reference clock associated with the serial input channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SI RefClk Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sirefclkname.html language=enus -->
## TOPIC 00219: Serial Input:Deserializer:Reference Clock Name

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sirefclkname.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sirefclkname.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the reference clock associated with the specified serial input channel. Remarks The following table lists the characteristics of this property. Short Name SI RefClk Name Data type cstr.png Permissions Read Only

### Serial Input:Deserializer:Reference Clock Name

Indicates the name of the reference clock associated with the specified serial input channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SI RefClk Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-socsi-2datarate.html language=enus -->
## TOPIC 00220: Serial Output:CSI-2 Interface:Data Rate

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-socsi-2datarate.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-socsi-2datarate.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the CSI-2 data rate. Remarks The following table lists the characteristics of this property. Short Name SO CSI-2 Data Rate Data type cdbl.png Permissions Read/Write

### Serial Output:CSI-2 Interface:Data Rate

Specifies the CSI-2 data rate.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SO CSI-2 Data Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-socsi-2lanes.html language=enus -->
## TOPIC 00221: Serial Output:CSI-2 Interface:Number of Lanes

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-socsi-2lanes.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-socsi-2lanes.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of active CSI-2 lanes. Remarks The following table lists the characteristics of this property. Short Name SO CSI-2 Lanes Data type ci32.png Permissions Read/Write 1 1 2 2 4 4

### Serial Output:CSI-2 Interface:Number of Lanes

Specifies the number of active CSI-2 lanes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SO CSI-2 Lanes |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| 1 | 1 |  |
| --- | --- | --- |
| 2 | 2 |  |
| 4 | 4 |  |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sodataclkname.html language=enus -->
## TOPIC 00222: Serial Output:CSI-2 Interface:Data Rate Clock Name

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sodataclkname.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sodataclkname.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the CSI-2 data rate clock associated with the specified serial output channel. Remarks The following table lists the characteristics of this property. Short Name SO Data Clk Name Data type cstr.png Permissions Read Only

### Serial Output:CSI-2 Interface:Data Rate Clock Name

Indicates the name of the CSI-2 data rate clock associated with the specified serial output channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SO Data Clk Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-soi2cname.html language=enus -->
## TOPIC 00223: Serial Output:Serializer:I2C Bus Instance Name

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-soi2cname.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-soi2cname.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the I2C bus instance associated with the specified serial output channel. Remarks The following table lists the characteristics of this property. Short Name SO I2C Name Data type cstr.png Permissions Read Only

### Serial Output:Serializer:I2C Bus Instance Name

Indicates the name of the I2C bus instance associated with the specified serial output channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SO I2C Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopoccurrent.html language=enus -->
## TOPIC 00224: Serial Output:Power Over Coax:Power Over Coax Current

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopoccurrent.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopoccurrent.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the power over coax current in amps on the specified serial output channel. Remarks The following table lists the characteristics of this property. Short Name SO PoC Current Data type cdbl.png Permissions Read Only

### Serial Output:Power Over Coax:Power Over Coax Current

Indicates the power over coax current in amps on the specified serial output channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SO PoC Current |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopocinrange.html language=enus -->
## TOPIC 00225: Serial Output:Power Over Coax:Power Over Coax In Range

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopocinrange.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopocinrange.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether power over coax is enabled, above the minimum valid voltage, and not receiving a fault signal on the specified serial output channel. Remarks The following table lists the characteristics of this property. Short Name SO PoC In Range Data type cbool.png Permissions Read Only

### Serial Output:Power Over Coax:Power Over Coax In Range

Indicates whether power over coax is enabled, above the minimum valid voltage, and not receiving a fault signal on the specified serial output channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SO PoC In Range |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopocsink.html language=enus -->
## TOPIC 00226: Serial Output:Power Over Coax:Power Over Coax Sink

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopocsink.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopocsink.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the power over coax sink on the specified serial output channel. Remarks The following table lists the characteristics of this property. Short Name SO PoC Sink Data type ci32.png Permissions Read/Write None 0 Auxiliary 2

### Serial Output:Power Over Coax:Power Over Coax Sink

Configures the power over coax sink on the specified serial output channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SO PoC Sink |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

| None | 0 |  |
| --- | --- | --- |
| Auxiliary | 2 |  |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopocvoltage.html language=enus -->
## TOPIC 00227: Serial Output:Power Over Coax:Power Over Coax Voltage

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopocvoltage.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sopocvoltage.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the power over coax voltage on the specified serial output channel. Remarks The following table lists the characteristics of this property. Short Name SO PoC Voltage Data type cdbl.png Permissions Read Only

### Serial Output:Power Over Coax:Power Over Coax Voltage

Indicates the power over coax voltage on the specified serial output channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SO PoC Voltage |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sorefclkenabled.html language=enus -->
## TOPIC 00228: Serial Output:Serializer:Reference Clock Enabled

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sorefclkenabled.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sorefclkenabled.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the reference clock is enabled. Remarks The following table lists the characteristics of this property. Short Name SO RefClk Enabled Data type cbool.png Permissions Read/Write

### Serial Output:Serializer:Reference Clock Enabled

Specifies whether the reference clock is enabled.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SO RefClk Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sorefclkfrequency.html language=enus -->
## TOPIC 00229: Serial Output:Serializer:Reference Clock Frequency

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sorefclkfrequency.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sorefclkfrequency.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference clock associated with the serial output channel. Remarks The following table lists the characteristics of this property. Short Name SO RefClk Frequency Data type cdbl.png Permissions Read/Write

### Serial Output:Serializer:Reference Clock Frequency

Specifies the reference clock associated with the serial output channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SO RefClk Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sorefclkname.html language=enus -->
## TOPIC 00230: Serial Output:Serializer:Reference Clock Name

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sorefclkname.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapichannel-rc/flexrio-channel/pniflexrio-sorefclkname.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the reference clock associated with the specified serial output channel. Remarks The following table lists the characteristics of this property. Short Name SO RefClk Name Data type cstr.png Permissions Read Only

### Serial Output:Serializer:Reference Clock Name

Indicates the name of the reference clock associated with the specified serial output channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SO RefClk Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Channel Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapiclock-rc/flexrio-clock-p.html language=enus -->
## TOPIC 00231: FlexRIO Clock Properties

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapiclock-rc/flexrio-clock-p.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapiclock-rc/flexrio-clock-p.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### FlexRIO Clock Properties

- [Active User Clock](../../../resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-activeuserclock.html) Specifies the user clock used to access all subsequent properties in this instance of the property node. You must first select this property and then pass the name of the specific user clock.
- [User Clock:Bypass PLL](../../../resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-bypasspll.html) Specifies whether the active user clock is a re-exported copy of the reference clock that bypasses the PLL.
- [User Clock:Enabled](../../../resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-userclockenabled.html) Specifies whether the active user clock is enabled.
- [User Clock:Frequency](../../../resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-userclockfrequency.html) Configures the specified user clock to generate the requested frequency.

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-activeuserclock.html language=enus -->
## TOPIC 00232: Active User Clock

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-activeuserclock.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-activeuserclock.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the user clock used to access all subsequent properties in this instance of the property node. You must first select this property and then pass the name of the specific user clock. Remarks The following table lists the characteristics of this property. Short Name Active User Clock Data ty

### Active User Clock

Specifies the user clock used to access all subsequent properties in this instance of the property node. You must first select this property and then pass the name of the specific user clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Active User Clock |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

FlexRIO Clock Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-bypasspll.html language=enus -->
## TOPIC 00233: User Clock:Bypass PLL

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-bypasspll.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-bypasspll.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the active user clock is a re-exported copy of the reference clock that bypasses the PLL. Remarks The following table lists the characteristics of this property. Short Name Bypass PLL Data type cbool.png Permissions Read/Write

### User Clock:Bypass PLL

Specifies whether the active user clock is a re-exported copy of the reference clock that bypasses the PLL.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Bypass PLL |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Clock Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-userclockenabled.html language=enus -->
## TOPIC 00234: User Clock:Enabled

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-userclockenabled.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-userclockenabled.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the active user clock is enabled. Remarks The following table lists the characteristics of this property. Short Name User Clock Enabled Data type cbool.png Permissions Read/Write

### User Clock:Enabled

Specifies whether the active user clock is enabled.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | User Clock Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Clock Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-userclockfrequency.html language=enus -->
## TOPIC 00235: User Clock:Frequency

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-userclockfrequency.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapiclock-rc/flexrio-clock/pniflexrio-userclockfrequency.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the specified user clock to generate the requested frequency. Remarks The following table lists the characteristics of this property. Short Name User Clock Frequency Data type cdbl.png Permissions Read/Write

### User Clock:Frequency

Configures the specified user clock to generate the requested frequency.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | User Clock Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Clock Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream-p.html language=enus -->
## TOPIC 00236: FlexRIO Stream Properties

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream-p.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream-p.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`

### FlexRIO Stream Properties

- [Active Stream](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-activestream.html) Specifies the stream name (e.g. '0') used to access all subsequent properties in this instance of the property node. You must first select this property and then pass the name of the specific stream.
- [Circular Buffer:Elements Written](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-circularbufferelementswritten.html) Specifies number of elements written into the FPGA's circular buffer.
- [Circular Buffer:Segment Count](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-circularbuffersegments.html) Specifies the number of segments the FPGA-side circular buffer is divided into.
- [Circular Buffer:Size](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-circularbuffersize.html) Specifies the capacity of the FPGA-side circular buffer.
- [Configuration:Finite](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamfinite.html) Specifies whether the stream should be finite. Finite streams are bound by a number of samples specified in Stream Number of Samples.
- [Configuration:TClk API Control Enabled](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-tclkapicontrolenabled.html) Specifies whether the TClk API will control this stream. When this attribute is true for a stream, TClk API calls such as niTClk Configure for Homogeneous Triggers, niTClk Initiate, and niTClk Wait Until Done will apply to this stream.
- [DSP:DDC:FPGA DDC Enabled](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaddcenabled.html) Enables the FPGA DDC chain for the device. Normally this will enable the decimator on modules that support it, as well as enable frequency shifting. However, details of the signal processing chain are dependent on the signal path in the FPGA. This property is detected by discovering flexrio.dsp.ddc.enable N, where N is the stream number connected to this signal path.
- [DSP:DDC:FPGA DDC IQ Enabled](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaddciqenabled.html) When IQ mode is enabled, both the I and Q data will be transferred to the stream. When it is disabled, only the I portions are captured on the device and transferred to the host. This property has no effect if the DDC is disabled.
- [DSP:DUC:FPGA DUC Enabled](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaducenabled.html) Enables the FPGA DUC chain for the device. Normally this will enable the decimator on modules that support it, as well as enable frequency shifting. However, details of the signal processing chain are dependent on the signal path in the FPGA. This property is detected by discovering flexrio.dsp.duc.enable N, where N is the stream number connected to this signal path.
- [DSP:DUC:FPGA DUC IQ Enabled](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaduciqenabled.html) When IQ mode is enabled, both the I and Q data will be transferred to the stream. When it is disabled, only the I portions are captured on the device and transferred to the host. This property has no effect if the DUC is disabled.
- [DSP:Data Path IQ Enabled](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-datapathiqenabled.html) The data path on the FPGA uses complex data. This affects data steering in the FPGA. For a device with upconversion, this will be true when either the FPGA has a DUC operating in IQ mode (see the attribute 'FPGA DUC IQ Enabled'), or the device has an upconverter built into the front end that requires IQ data (see the attribute 'DAC Digital Upconverter Enabled'). In IQ mode, you are required to supply IQ data to WriteStream.
- [Data Delay](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-datadelay.html) Specifies the delay after the sample clock rising edge when the device acquires a new data sample. Data delay is used to capture pre-trigger content digitized by the device. If the FlexRIO Variable Delay block is present, you may shift the data contained in the acquisition using this property. The driver converts this delay into an adjustment on the actual data captured in units of the data clock period. For example, if the data clock period is 100MHz, a 10ns data delay will result in a data phase shift of one data clock period. The timestamps returned reflect this adjustment, excluding the residual adjustment that can not be accounted for using data delay.
- [Description:Channels In Stream](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-channelsinstream.html) Specifies the number of channels available in the named stream.
- [Description:FIFO Name](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamfifoname.html) Returns a semicolon delimited list of the names of the FIFOs used on the stream.
- [Description:Is Input Stream](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-isinputstream.html) Indicates whether the driver considers this stream to be an input stream (device to host). If false, then this is an output stream.
- [Description:Stream Data Format](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamdataformat.html)
- [Metadata:Sample dt](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-sampledt.html) Overrides the dt metadata returned in waveforms. This value is used to populate the waveform infomation during a stream read. This value is normally set by the driver, but can be set manually. Setting this value to 0 allows the driver to override. Note: this does not change the hardware, and is intended to allow a user to set dt in situations where the hardware sample rate is not the sample rate of the data, such as when adding user-defined DSP that may change the effective sample rate.
- [Stream Channels Enabled](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamchannelsenabled.html) Returns a bitmask indicating which channels will be transferred in this stream.
- [Stream FIFO Size](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamfifosize.html) Specifies the number of samples allocated in each stream FIFO. Set this value to 0 to allow the driver to allocate the buffer according to its own heuristics.
- [Stream Number Of Samples](../../../resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamnumberofsamples.html) Specifies the number of samples to transfer in a finite stream.

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-activestream.html language=enus -->
## TOPIC 00237: Active Stream

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-activestream.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-activestream.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the stream name (e.g. '0') used to access all subsequent properties in this instance of the property node. You must first select this property and then pass the name of the specific stream. Remarks The following table lists the characteristics of this property. Short Name Active Stream Dat

### Active Stream

Specifies the stream name (e.g. '0') used to access all subsequent properties in this instance of the property node. You must first select this property and then pass the name of the specific stream.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Active Stream |
| --- | --- |
| Data type |  |
| Permissions | Write Only |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-channelsinstream.html language=enus -->
## TOPIC 00238: Description:Channels In Stream

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-channelsinstream.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-channelsinstream.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of channels available in the named stream. Remarks The following table lists the characteristics of this property. Short Name Channels In Stream Data type ci32.png Permissions Read/Write

### Description:Channels In Stream

Specifies the number of channels available in the named stream.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Channels In Stream |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-circularbufferelementswritten.html language=enus -->
## TOPIC 00239: Circular Buffer:Elements Written

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-circularbufferelementswritten.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-circularbufferelementswritten.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies number of elements written into the FPGA's circular buffer. Remarks The following table lists the characteristics of this property. Short Name Circular Buffer Elements Written Data type cu64.png Permissions Read Only

### Circular Buffer:Elements Written

Specifies number of elements written into the FPGA's circular buffer.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Circular Buffer Elements Written |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-circularbuffersegments.html language=enus -->
## TOPIC 00240: Circular Buffer:Segment Count

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-circularbuffersegments.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-circularbuffersegments.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of segments the FPGA-side circular buffer is divided into. Remarks The following table lists the characteristics of this property. Short Name Circular Buffer Segments Data type ci32.png Permissions Read Only

### Circular Buffer:Segment Count

Specifies the number of segments the FPGA-side circular buffer is divided into.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Circular Buffer Segments |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-circularbuffersize.html language=enus -->
## TOPIC 00241: Circular Buffer:Size

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-circularbuffersize.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-circularbuffersize.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the capacity of the FPGA-side circular buffer. Remarks The following table lists the characteristics of this property. Short Name Circular Buffer Size Data type cu64.png Permissions Read Only

### Circular Buffer:Size

Specifies the capacity of the FPGA-side circular buffer.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Circular Buffer Size |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-datadelay.html language=enus -->
## TOPIC 00242: Data Delay

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-datadelay.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-datadelay.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the delay after the sample clock rising edge when the device acquires a new data sample. Data delay is used to capture pre-trigger content digitized by the device. If the FlexRIO Variable Delay block is present, you may shift the data contained in the acquisition using this property. The d

### Data Delay

Specifies the delay after the sample clock rising edge when the device acquires a new data sample. Data delay is used to capture pre-trigger content digitized by the device. If the FlexRIO Variable Delay block is present, you may shift the data contained in the acquisition using this property. The driver converts this delay into an adjustment on the actual data captured in units of the data clock period. For example, if the data clock period is 100MHz, a 10ns data delay will result in a data phase shift of one data clock period. The timestamps returned reflect this adjustment, excluding the residual adjustment that can not be accounted for using data delay.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-datapathiqenabled.html language=enus -->
## TOPIC 00243: DSP:Data Path IQ Enabled

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-datapathiqenabled.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-datapathiqenabled.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The data path on the FPGA uses complex data. This affects data steering in the FPGA. For a device with upconversion, this will be true when either the FPGA has a DUC operating in IQ mode (see the attribute 'FPGA DUC IQ Enabled'), or the device has an upconverter built into the front end that require

### DSP:Data Path IQ Enabled

The data path on the FPGA uses complex data. This affects data steering in the FPGA. For a device with upconversion, this will be true when either the FPGA has a DUC operating in IQ mode (see the attribute 'FPGA DUC IQ Enabled'), or the device has an upconverter built into the front end that requires IQ data (see the attribute 'DAC Digital Upconverter Enabled'). In IQ mode, you are required to supply IQ data to WriteStream.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Path IQ Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaddcenabled.html language=enus -->
## TOPIC 00244: DSP:DDC:FPGA DDC Enabled

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaddcenabled.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaddcenabled.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the FPGA DDC chain for the device. Normally this will enable the decimator on modules that support it, as well as enable frequency shifting. However, details of the signal processing chain are dependent on the signal path in the FPGA. This property is detected by discovering flexrio.dsp.ddc.

### DSP:DDC:FPGA DDC Enabled

Enables the FPGA DDC chain for the device. Normally this will enable the decimator on modules that support it, as well as enable frequency shifting. However, details of the signal processing chain are dependent on the signal path in the FPGA. This property is detected by discovering flexrio.dsp.ddc.enable N, where N is the stream number connected to this signal path.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FPGA DDC Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaddciqenabled.html language=enus -->
## TOPIC 00245: DSP:DDC:FPGA DDC IQ Enabled

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaddciqenabled.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaddciqenabled.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: When IQ mode is enabled, both the I and Q data will be transferred to the stream. When it is disabled, only the I portions are captured on the device and transferred to the host. This property has no effect if the DDC is disabled. Remarks The following table lists the characteristics of this propert

### DSP:DDC:FPGA DDC IQ Enabled

When IQ mode is enabled, both the I and Q data will be transferred to the stream. When it is disabled, only the I portions are captured on the device and transferred to the host. This property has no effect if the DDC is disabled.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FPGA DDC IQ Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaducenabled.html language=enus -->
## TOPIC 00246: DSP:DUC:FPGA DUC Enabled

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaducenabled.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaducenabled.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the FPGA DUC chain for the device. Normally this will enable the decimator on modules that support it, as well as enable frequency shifting. However, details of the signal processing chain are dependent on the signal path in the FPGA. This property is detected by discovering flexrio.dsp.duc.

### DSP:DUC:FPGA DUC Enabled

Enables the FPGA DUC chain for the device. Normally this will enable the decimator on modules that support it, as well as enable frequency shifting. However, details of the signal processing chain are dependent on the signal path in the FPGA. This property is detected by discovering flexrio.dsp.duc.enable N, where N is the stream number connected to this signal path.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FPGA DUC Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaduciqenabled.html language=enus -->
## TOPIC 00247: DSP:DUC:FPGA DUC IQ Enabled

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaduciqenabled.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-fpgaduciqenabled.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: When IQ mode is enabled, both the I and Q data will be transferred to the stream. When it is disabled, only the I portions are captured on the device and transferred to the host. This property has no effect if the DUC is disabled. Remarks The following table lists the characteristics of this propert

### DSP:DUC:FPGA DUC IQ Enabled

When IQ mode is enabled, both the I and Q data will be transferred to the stream. When it is disabled, only the I portions are captured on the device and transferred to the host. This property has no effect if the DUC is disabled.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FPGA DUC IQ Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-isinputstream.html language=enus -->
## TOPIC 00248: Description:Is Input Stream

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-isinputstream.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-isinputstream.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the driver considers this stream to be an input stream (device to host). If false, then this is an output stream. Remarks The following table lists the characteristics of this property. Short Name Is Input Stream Data type cbool.png Permissions Read Only

### Description:Is Input Stream

Indicates whether the driver considers this stream to be an input stream (device to host). If false, then this is an output stream.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Is Input Stream |
| --- | --- |
| Data type |  |
| Permissions | Read Only |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-sampledt.html language=enus -->
## TOPIC 00249: Metadata:Sample dt

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-sampledt.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-sampledt.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Overrides the dt metadata returned in waveforms. This value is used to populate the waveform infomation during a stream read. This value is normally set by the driver, but can be set manually. Setting this value to 0 allows the driver to override. Note: this does not change the hardware, and is inte

### Metadata:Sample dt

Overrides the dt metadata returned in waveforms. This value is used to populate the waveform infomation during a stream read. This value is normally set by the driver, but can be set manually. Setting this value to 0 allows the driver to override. Note: this does not change the hardware, and is intended to allow a user to set dt in situations where the hardware sample rate is not the sample rate of the data, such as when adding user-defined DSP that may change the effective sample rate.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample dt |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Stream Properties

<!--NI_TOPIC bundle=flexrio-labview-api-ref path=resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamchannelsenabled.html language=enus -->
## TOPIC 00250: Stream Channels Enabled

- bundle_id: `flexrio-labview-api-ref`
- source_path: `resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamchannelsenabled.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-labview-api-ref/raw/resource/enus/resource/objmgr/niflexrioapistream-rc/flexrio-stream/pniflexrio-streamchannelsenabled.html
- document_id: `flexrio-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a bitmask indicating which channels will be transferred in this stream. Remarks The following table lists the characteristics of this property. Short Name Stream Channels Enabled Data type cu64.png Permissions Read/Write

### Stream Channels Enabled

Returns a bitmask indicating which channels will be transferred in this stream.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Stream Channels Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |

Parent topic:

FlexRIO Stream Properties
