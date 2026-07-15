# NI DOCUMENT BUNDLE: ni-579x-cdl-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-579x-cdl-api-ref start=1 end=7 -->
<!--NI_TOPIC bundle=ni-579x-cdl-api-ref path=fam-registers.html language=enus -->
## TOPIC 00001: FAM Registers

- bundle_id: `ni-579x-cdl-api-ref`
- source_path: `fam-registers.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-cdl-api-ref/raw/resource/enus/fam-registers.html
- document_id: `ni-579x-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Processes the FAM register operations sent from the host using the register bus. register instruction A read or write register instruction. This parameter is usually obtained from the register instruction parameter of the Process node. The source of this parameter defines the Register Bus objects to

FAM Registers

Processes the FAM register operations sent from the host using the register bus.

[IMAGE alt='1378' src='FAM_Registers.gcdl.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### register instruction

A read or write register instruction. This parameter is usually obtained from the register instruction parameter of the Process node. The source of this parameter defines the Register Bus objects to which the Synchronization node is wired, and it is communicated from the host.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### read completion

Indicates whether the register read operation is complete, and returns the data from the register read.

read completion

Process

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### ready for input

Boolean value that indicates whether this node is ready to accept new input data.

Use Feedback Node to wire this output to the ready for
 output output of an upstream node.

| True | The node is ready to accept new input data. |
| --- | --- |
| False | The node is not ready to accept new input data. |

Note

input valid

[IMAGE alt='datatype_icon' src='/assets/img/cvoid.png']

##### IO Module\Register Bus Idle

Indicates when the FAM Registers interface is being accessed. To use the Register Bus signals, you must wait for this signal to be TRUE.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### Register Bus Address

Configures the FAM Registers interface address for read or write data.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### Register Bus Idle

Indicates when the FAM Registers interface is being accessed.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### Register Bus Read

Executes a Register Bus Read.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### Register Bus Read Data

Returns the FAM Registers interface data to read from a Register Bus address.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### Register Bus Write

Executes a Register Bus Write.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### Register Bus Write Data

Configures the FAM Registers interface data to write to a Register Bus address.

<!--NI_TOPIC bundle=ni-579x-cdl-api-ref path=ni-579x-nodes.html language=enus -->
## TOPIC 00002: NI-579x FPGA API for LabVIEW NXG FPGA Module

- bundle_id: `ni-579x-cdl-api-ref`
- source_path: `ni-579x-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-cdl-api-ref/raw/resource/enus/ni-579x-nodes.html
- document_id: `ni-579x-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`

NI-579x FPGA API for LabVIEW NXG FPGA Module

<!--NI_TOPIC bundle=ni-579x-cdl-api-ref path=ni579x-fpga-align.html language=enus -->
## TOPIC 00003: ni579x FPGA Align

- bundle_id: `ni-579x-cdl-api-ref`
- source_path: `ni579x-fpga-align.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-cdl-api-ref/raw/resource/enus/ni579x-fpga-align.html
- document_id: `ni-579x-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aligns the synchronization targets. You must align the synchronization targets before synchronizing a signal. ni579 Host Align and ni579 FPGA Align provide the same quality of synchronization, but differ in requirements and versatility of operation. When using ni579x FPGA Align, the clock-driven loo

ni579x FPGA Align

Aligns the synchronization targets.

You must align the synchronization targets before synchronizing a signal.

ni579 Host Align and ni579 FPGA Align provide the same quality of synchronization, but differ in requirements and versatility of operation. When using ni579x FPGA Align, the clock-driven loop (CDL) rate containing this node must be an integer multiple of the sync.cptr.Reference Clock rate, and the CDL clock must have a fixed phase relationship to the Reference Clock.

Each target performs its alignment independently, so FPGA Align does not require an FPGA I/O line. You can also use FPGA Align without host interaction. FPGA Align has 100% repeatability if-and-only-if the target-to-target phase relationship is low and does not change. When using ni579x Host Align, the CDL rate may be arbitrary, but still must have a fixed phase relationship to the other targets. The CPTR period may also be arbitrary. This alignment process is coordinated by the host, and requires an FPGA I/O line for orchestration. FPGA Align has 100% repeatability; if the hardware configuration remains constant, the level of synchronization remains constant as well.

[IMAGE alt='1378' src='ni579x_FPGA_Align.gcdl.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources

Identifies the Synchronization instance. Sync.resources is obtained from ni579x Create.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### sync.meas.Reference.Clock

The start signal. When using ni579x FPGA Align, the sync.meas.Reference Clock must be the same clock that the target's FPGA Clock is locked to. This is commonly 
PXI_Clk10.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources 2

The synchronization instance is obtained from the create node.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### FPGA Clock x2

Measurement clock used by the measurement logic.

This clock must run at twice the rate of the FPGA Clock (the clock that drives the Single Cycle Timed Loop (SCTL) which this node is in). This clock must also be derived from the FPGA Clock, so that it has a fixed phase relationship. This is commonly IO Module\Sample Clock x2.

<!--NI_TOPIC bundle=ni-579x-cdl-api-ref path=ni579x-host-align.html language=enus -->
## TOPIC 00004: ni579x Host Align

- bundle_id: `ni-579x-cdl-api-ref`
- source_path: `ni579x-host-align.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-cdl-api-ref/raw/resource/enus/ni579x-host-align.html
- document_id: `ni-579x-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aligns the synchronization targets. You must align the synchronization targets before synchronizing a signal. ni579x Host Align and ni579x FPGA Align provide the same quality of synchronization, but differ in requirements and versatility of operation. When using ni579x FPGA Align, the clock-driven l

ni579x Host Align

Aligns the synchronization targets. You must align the synchronization targets before synchronizing a signal.

ni579x Host Align and ni579x FPGA Align provide the same quality of synchronization, but differ in requirements and versatility of operation. When using ni579x FPGA Align, the clock-driven loop (CDL) rate containing this node must be an integer multiple of the sync.cptr.Reference Clock rate, and the CDL clock must have a fixed phase relationship to the Reference Clock.

Each target performs its alignment independently, so ni579x FPGA Align does not require an FPGA I/O line. You can also use ni579x FPGA Align without host interaction. ni579x FPGA Align has 100% repeatability if-and-only-if the target-to-target phase relationship is low and does not change. When using ni579x Host Align, the CDL rate may be arbitrary, but still must have a fixed phase relationship to the other targets. The CPTR period may also be arbitrary. This alignment process is coordinated by the host, and requires an FPGA I/O line for orchestration. ni579x FPGA Align has 100% repeatability; if the hardware configuration remains constant, the level of synchronization remains constant as well.

[IMAGE alt='1378' src='ni579x_Host_Align.gcdl.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources

Identifies the Synchronization instance. Sync.resources is obtained from ni579x Create.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### sync.meas.Reference.Clock

The start signal. When using ni579x FPGA Align, the sync.meas.Reference Clock must be the same clock that the target's FPGA Clock is locked to. This is commonly 
PXI_Clk10.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### sync.meas.FPGA I/O

The FPGA I/O line that starts the alignment process. The FPGA I/O line used is usually a PXI trigger line.

Note

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources 2

The synchronization instance is obtained from the create node.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### FPGA Clock x2

Measurement clock used by the measurement logic.

This clock must run at twice the rate of the FPGA Clock (the clock that drives the Single Cycle Timed Loop (SCTL) which this node is in). This clock must also be derived from the FPGA Clock, so that it has a fixed phase relationship. This is commonly IO Module\Sample Clock x2.

<!--NI_TOPIC bundle=ni-579x-cdl-api-ref path=ni579x-synchronization-registers.html language=enus -->
## TOPIC 00005: ni579x Synchronization Registers

- bundle_id: `ni-579x-cdl-api-ref`
- source_path: `ni579x-synchronization-registers.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-cdl-api-ref/raw/resource/enus/ni579x-synchronization-registers.html
- document_id: `ni-579x-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets/gets the configuration values for the Synchronization library by connecting to the Register Bus. register instruction Specifies a read or write register instruction. This parameter is usually obtained from the register instruction parameter of the Process node in the Register Bus FPGA library.

ni579x Synchronization Registers

Sets/gets the configuration values for the Synchronization library by connecting to the Register Bus.

[IMAGE alt='1378' src='ni579x_Synchronization_Registers.gcdl.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### register instruction

Specifies a read or write register instruction.

register instruction

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources

Identifies the Synchronization instance. Sync.resources is obtained from ni579x Create.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### read completion

Indicates whether the register read operation is complete, and returns the data from the register read.

read completion

Process

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### ready for input

A Boolean that indicates whether this node is ready to write new data to the FIFO in the next clock cycle.

| TRUE | Indicates that this node is ready to write new data to the FIFO. |
| --- | --- |
| FALSE | Indicates that this node is not ready to write new data to the FIFO. |

<!--NI_TOPIC bundle=ni-579x-cdl-api-ref path=ni579x-synchronize-signal.html language=enus -->
## TOPIC 00006: ni579x Synchronize Signal

- bundle_id: `ni-579x-cdl-api-ref`
- source_path: `ni579x-synchronize-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-cdl-api-ref/raw/resource/enus/ni579x-synchronize-signal.html
- document_id: `ni-579x-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronously realizes a signal. If this target is the master, it distributes edge on the specified FPGA I/O line on the next falling edge of the CPTR when edge is high. If this target is not the master, it ignores edge. All targets also read the FPGA I/O line. The synchronized edge output goes high

ni579x Synchronize Signal

Synchronously realizes a signal.

edge

edge

edge

synchronized edge

Note

edge

edge

[IMAGE alt='1378' src='ni579x_Synchronize_Signal.gcdl.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources

Identifies the Synchronization instance. Sync.resources is obtained from ni579x Create.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### sync.cptr.FPGA I/O

The FPGA I/O line that distributes/reads the edge for synchronization. This signal is commonly a PXI trigger line.

Note

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable

Specifies whether to synchronize the input edge.

Note

sync.cptr.FPGA I/O

enable

synchronized edge

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### edge

The input being synchronized. The first block this input encounters is a rising edge detector, so the input signal, edge, is treated as a pulse.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### synchronization delay

Returns the number of clock cycles of delay that were added by synchronizing the input edge.

enable

enable

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### synchronized edge

Returns the synchronized input edge if enable is set to True.

Note

enable

synchronized edge

enable

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources 2

The synchronization instance is obtained from the create node.

<!--NI_TOPIC bundle=ni-579x-cdl-api-ref path=user-command-registers.html language=enus -->
## TOPIC 00007: User Command Registers

- bundle_id: `ni-579x-cdl-api-ref`
- source_path: `user-command-registers.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-cdl-api-ref/raw/resource/enus/user-command-registers.html
- document_id: `ni-579x-cdl-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Processes the user commands sent from the host using the register bus. register instruction A read or write register instruction. This parameter is usually obtained from the register instruction parameter of the Process node. The source of this parameter defines the Register Bus objects to which the

User Command Registers

Processes the user commands sent from the host using the register bus.

[IMAGE alt='1378' src='User_Command_Registers.gcdl.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### register instruction

A read or write register instruction. This parameter is usually obtained from the register instruction parameter of the Process node. The source of this parameter defines the Register Bus objects to which the Synchronization node is wired, and it is communicated from the host.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### read completion

Indicates whether the register read operation is complete, and returns the data from the register read.

read completion

Process

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### ready for input

Boolean value that indicates whether this node is ready to accept new input data.

Use Feedback Node to wire this output to the ready for
 output output of an upstream node.

| True | The node is ready to accept new input data. |
| --- | --- |
| False | The node is not ready to accept new input data. |

Note

input valid

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### IO Module\User Command Idle

A TRUE value indicates that the device is prepared to accept more commands from the User Command signal.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### IO Module\User Error

Indicates that an error occurred and that you must reinitialize the device.

0 = no error

Nonzero = error

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### User Command Idle

A TRUE value indicates that the device is prepared to accept more commands from the User Command signal.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### User Error

Indicates that an error occurred and that you must reinitialize the device.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### User Return

Returns data configured by User Command.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### User Command Status

Indicates whether the previous command completed successfully.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### User Command Commit

A low-to-high transition applies the settings that you configured with the User Command signal.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### User Command

Configures the clocking, ADC, DAC, attenuators, filters, and other settings for your device. Use this signal with the User Data 0 and User Data 1 signals to select values for these settings. Apply these settings by selecting the User Command Commit signal.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### User Data 0

Use this signal in conjunction with the User Data 1 and User Command signals to configure your device.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### User Data 1

Use this signal in conjunction with the User Data 0 and User Command signals to configure your device.
