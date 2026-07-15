# NI DOCUMENT BUNDLE: ni-usrp-lvnxg-fpga-rio-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-usrp-lvnxg-fpga-rio-api-ref start=1 end=22 -->
<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=cdl-gps-nodes.html language=enus -->
## TOPIC 00001: GPS Nodes

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `cdl-gps-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/cdl-gps-nodes.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`

GPS Nodes

USRP RIO Nodes (CDL)

Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

GPS Registers

Makes the Nmea data available to the host by capturing, processing, and sending the data to the Register Bus on request.

Parent topic:

USRP RIO Nodes (CDL)

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=cdl-usrp-rio-nodes.html language=enus -->
## TOPIC 00002: USRP RIO Nodes (CDL)

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `cdl-usrp-rio-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/cdl-usrp-rio-nodes.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

USRP RIO Nodes (CDL)

Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

Configuration Nodes

GPS Nodes

Synchronization Nodes

Time Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=config-registers.html language=enus -->
## TOPIC 00003: Registers

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `config-registers.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/config-registers.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets/gets the configuration values for the Configuration nodes by connecting it to the Register Bus. register instruction Specifies a read or write register instruction. This parameter is usually obtained from the register instruction parameter of the Process node in the Register Bus FPGA library. T

Registers

Sets/gets the configuration values for the Configuration nodes by connecting it to the Register Bus.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### register instruction

Specifies a read or write register instruction.

register instruction

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### resources

Configuration instance. resources is obtained from the Create node.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### ready for input

Boolean that indicates whether the node is ready to accept new input data in the next cycle. Use a Feedback Node to wire this parameter to the 
ready for output input of an upstream node.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### read completion

Indicates whether the register read operation is complete and returns the data from the register read.

Feedback Node

read completion

Process

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=configuration-nodes.html language=enus -->
## TOPIC 00004: Configuration Nodes

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `configuration-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/configuration-nodes.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`

Configuration Nodes

USRP RIO Nodes (CDL)

Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

Registers

Sets/gets the configuration values for the Configuration nodes by connecting it to the Register Bus.

Parent topic:

USRP RIO Nodes (CDL)

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=fpga-align.html language=enus -->
## TOPIC 00005: FPGA Align

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `fpga-align.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/fpga-align.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aligns the targets participating in synchronization before synchronizing a signal without using an FPGA I/O line. sync.resources in Synchronization instance. sync.resources is obtained from the Create node. common reference The "start" signal used by the measurement logic. When you use FPGA Align, t

FPGA Align

Aligns the targets participating in synchronization before synchronizing a signal without using an FPGA I/O line.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources in

Synchronization instance. sync.resources is obtained from the Create node.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### common reference

The "start" signal used by the measurement logic.

FPGA Align

common reference

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### clock x2

Measurement clock used by the measurement logic.

This clock must run at twice the rate of the FPGA Clock, which is the clock that drives the clock-driven loop (CDL) that this node is in. This clock must also derive from the FPGA Clock so that it has a fixed phase relationship. This clock is commonly Data Clock x2.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### sync.resources out

The same instance that was passed in for sync.resources.

#### Choose Host Align or FPGA Align

FPGA Align

sync.common reference

FPGA Align

FPGA Align

Host Align

Host Align

#### Two Physical Connection Topologies

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=fpga-io-out-for-star.html language=enus -->
## TOPIC 00006: FPGA IO Out for Star

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `fpga-io-out-for-star.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/fpga-io-out-for-star.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends out the synchronization signals as needed for the star-topology-based synchronization. sync.fpga io out The FPGA I/O line to send the signal out on. sync.fpga io signal out Signal needed for the synchronization library from Host Align Star or Synchronize Signal Star. Only one sync.fpga io sign

FPGA IO Out for Star

Sends out the synchronization signals as needed for the star-topology-based synchronization.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### sync.fpga io out

The FPGA I/O line to send the signal out on.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### sync.fpga io signal out

Signal needed for the synchronization library from Host Align Star or Synchronize Signal Star.

sync.fpga io signal out

##### sync.fpga io signal out

Signal needed for the synchronization library from Host Align Star or Synchronize Signal Star. Only one sync.fpga io signal out should be True at a time (all the inputs are Red).

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=future-event-register-bus.html language=enus -->
## TOPIC 00007: Future Event Register Bus

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `future-event-register-bus.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/future-event-register-bus.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects a future event instance to the Register Bus. future event.resources The LabVIEW FPGA resources used by this future event instance, obtained from the Create Future Event node. register instruction specifies a read or write register instruction. This parameter is usually obtained from the reg

Future Event Register Bus

Connects a future event instance to the Register Bus.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### future event.resources

The LabVIEW FPGA resources used by this future event instance, obtained from the Create Future Event node.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### register instruction

specifies a read or write register instruction. This parameter is usually obtained from the register instruction parameter of the Process node. The source of this parameter defines the instances of the Register Bus library to which the Synchronization library instance is wired, and is communicated from the host.

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### instance

indicates that the future event time is valid.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### read completion

Indicates whether the register read operation is complete and returns the data from the register read.

Feedback Node

read completion

Process

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### ready for input

Indicates whether the node is ready to accept new input data in the next cycle. Use a Feedback Node to wire this parameter to the ready for output terminal of an upstream node.

Parent topic:

Time Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=future-event.html language=enus -->
## TOPIC 00008: Future Event

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `future-event.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/future-event.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures future events and identifies when events occur. future event.resources The LabVIEW FPGA resources used by this future event instance, obtained from the Create Future Event node. time.resources LabVIEW FPGA resources used by Time, obtained from the Create Time node. event.occurred Boolean

Future Event

Configures future events and identifies when events occur.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### future event.resources

The LabVIEW FPGA resources used by this future event instance, obtained from the Create Future Event node.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### time.resources

LabVIEW FPGA resources used by Time, obtained from the Create Time node.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### event.occurred

Boolean which is TRUE on the cycle when the future event occurs.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### event.time

The actual time when the future event occurred.

Parent topic:

Time Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=gps-registers.html language=enus -->
## TOPIC 00009: GPS Registers

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `gps-registers.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/gps-registers.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Makes the Nmea data available to the host by capturing, processing, and sending the data to the Register Bus on request. register instruction specifies a read or write register instruction. This parameter is usually obtained from the register instruction parameter of the Process node in the Register

GPS Registers

Makes the Nmea data available to the host by capturing, processing, and sending the data to the Register Bus on request.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### register instruction

specifies a read or write register instruction.

register instruction

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### ready for input

A Boolean that indicates whether the register read operation is complete.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### read completion

Indicates whether the register read operation is complete and returns the data from the register read.

Feedback Node

read completion

Process

Parent topic:

GPS Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=host-align-bus.html language=enus -->
## TOPIC 00010: Host Align Bus

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `host-align-bus.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/host-align-bus.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aligns the participating targets connected to a common bus, typically AUX I/O, before synchronizing a signal. sync.resources in Synchronization instance. sync.resources is obtained from the Create node. common reference The "start" signal used by the measurement logic. When you use the FPGA Align no

Host Align Bus

Aligns the participating targets connected to a common bus, typically AUX I/O, before synchronizing a signal.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources in

Synchronization instance. sync.resources is obtained from the Create node.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### common reference

The "start" signal used by the measurement logic.

When you use the FPGA Align node, the common reference must be the same clock to which the FPGA clock of the target is locked.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### clock x2

Measurement clock used by the measurement logic.

This clock must run at twice the rate of the FPGA Clock, which is the clock that drives the clock-driven loop (CDL) that this node is in. This clock must also derive from the FPGA Clock so that it has a fixed phase relationship. This clock is commonly Data Clock x2.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### sync.meas.fpga io

The FPGA I/O line to send and receive the measurement signals on. This line is commonly an AUX I/O line.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### sync.resources out

The same instance that was passed in for sync.resources.

#### Choose Host Align or FPGA Align

FPGA Align

sync.common reference

FPGA Align

FPGA Align

Host Align

Host Align

#### Two Physical Connection Topologies

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=host-align-star.html language=enus -->
## TOPIC 00011: Host Align Star

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `host-align-star.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/host-align-star.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aligns the participating targets in a star topology, typically connected using PPS Trig, before synchronizing a signal. sync.resources in Synchronization instance. sync.resources is obtained from the Create node. common reference The "start" signal used by the measurement logic. When you use the FPG

Host Align Star

Aligns the participating targets in a star topology, typically connected using PPS Trig, before synchronizing a signal.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources in

Synchronization instance. sync.resources is obtained from the Create node.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### common reference

The "start" signal used by the measurement logic.

When you use the FPGA Align node, the common reference must be the same clock to which the FPGA clock of the target is locked.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### clock x2

Measurement clock used by the measurement logic.

This clock must run at twice the rate of the FPGA Clock, which is the clock that drives the clock-driven loop (CDL) that this node is in. This clock must also derive from the FPGA Clock so that it has a fixed phase relationship. This clock is commonly Data Clock x2.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### sync.fpga io in

The FPGA I/O line to receive the measurement signals on. This line is commonly the PPS TRIG IN line.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### sync.resources out

The same instance that was passed in for sync.resources.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### sync.fpga io signal out

The signal to send out over an FPGA I/O line. This line is commonly the PPS TRIG OUT line. Wire this output into an input of the FPGA IO Out for Star node.

#### Choose Host Align or FPGA Align

FPGA Align

sync.common reference

FPGA Align

FPGA Align

Host Align

Host Align

#### Two Physical Connection Topologies

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=registers.html language=enus -->
## TOPIC 00012: Registers

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `registers.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/registers.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets/gets the configuration values for the Synchronization nodes by connecting it to the Register Bus. register instruction A read or write register instruction. This parameter is usually obtained from the register instruction parameter of the Process node. The source of this parameter defines the R

Registers

Sets/gets the configuration values for the Synchronization nodes by connecting it to the Register Bus.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### register instruction

A read or write register instruction. This parameter is usually obtained from the register instruction parameter of the Process node. The source of this parameter defines the Register Bus objects to which the Synchronization node is wired, and it is communicated from the host.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources

Synchronization instance. sync.resources is obtained from the Create node.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### ready for input

Boolean that indicates whether the node is ready to accept new input data in the next cycle. Use a Feedback Node to wire this parameter to the 
ready for output input of an upstream node.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### read completion

Indicates whether the register read operation is complete and returns the data from the register read.

Feedback Node

read completion

Process

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=sync-advanced.html language=enus -->
## TOPIC 00013: Advanced

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `sync-advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/sync-advanced.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`

Advanced

Synchronization Nodes

FPGA Align

Aligns the targets participating in synchronization before synchronizing a signal without using an FPGA I/O line.

FPGA IO Out for Star

Sends out the synchronization signals as needed for the star-topology-based synchronization.

Host Align Bus

Aligns the participating targets connected to a common bus, typically AUX I/O, before synchronizing a signal.

Host Align Star

Aligns the participating targets in a star topology, typically connected using PPS Trig, before synchronizing a signal.

Synchronize Signal Bus

Synchronously realizes a signal over a bus topology typically using AUX I/O.

Synchronize Signal Star

Synchronously realizes a signal over a star topology typically using PPS Trig.

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=synchronization-nodes.html language=enus -->
## TOPIC 00014: Synchronization Nodes

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `synchronization-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/synchronization-nodes.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`

Synchronization Nodes

USRP RIO Nodes (CDL)

Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

Advanced

Registers

Sets/gets the configuration values for the Synchronization nodes by connecting it to the Register Bus.

Synchronization

Synchronizes USRP RIO devices over the AUX I/O or PPS TRIG lines.

Parent topic:

USRP RIO Nodes (CDL)

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=synchronization.html language=enus -->
## TOPIC 00015: Synchronization

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/synchronization.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronizes USRP RIO devices over the AUX I/O or PPS TRIG lines.

Synchronization

Synchronizes USRP RIO devices over the AUX I/O or PPS TRIG lines.

Synchronization Nodes

Synchronize over AUX IO

Synchronizes USRP RIO devices over the AUX I/O lines.

Synchronize over PPS Trig

Synchronizes USRP RIO devices over the PPS Trig lines.

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=synchronize-over-aux-io.html language=enus -->
## TOPIC 00016: Synchronize over AUX IO

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `synchronize-over-aux-io.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/synchronize-over-aux-io.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronizes USRP RIO devices over the AUX I/O lines. sync.resources in Synchronization instance. sync.resources is obtained from the Create node. enable A Boolean that specifies whether to synchronize the input edge or not. The sync.fpga io may be floating until a target is specified as the master.

Synchronize over AUX IO

Synchronizes USRP RIO devices over the AUX I/O lines.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources in

Synchronization instance. sync.resources is obtained from the Create node.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable

A Boolean that specifies whether to synchronize the input edge or not.

Note

sync.fpga io

enable

synchronized edge

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### edge

Signal being synchronized. Because the first block this input encounters is a rising edge detector, the input signal edge is treated as a pulse.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### common reference

The "start" signal used by the measurement logic.

When you use the FPGA Align node, the common reference must be the same clock to which the FPGA clock of the target is locked.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### clock x2

Measurement clock used by the measurement logic.

This clock must run at twice the rate of the FPGA Clock, which is the clock that drives the clock-driven loop (CDL) that this node is in. This clock must also derive from the FPGA Clock so that it has a fixed phase relationship. This clock is commonly Data Clock x2.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### sync.meas.fpga io

The FPGA I/O line to send and receive the measurement signals on. This line is commonly an AUX I/O line.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### sync.fpga io

The FPGA I/O lines to send and receive the synchronization signals on.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### sync.resources out

The same instance that was passed in for sync.resources.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### synchronization delay

The number of clock cycles of delay that were added by synchronizing the input edge. This value is zero if enable is FALSE. If enable is TRUE, this value is valid only on the master target.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### synchronized edge

The synchronized input edge if enable is TRUE.

Parent topic:

Synchronization

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=synchronize-over-pps-trig.html language=enus -->
## TOPIC 00017: Synchronize over PPS Trig

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `synchronize-over-pps-trig.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/synchronize-over-pps-trig.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronizes USRP RIO devices over the PPS Trig lines. sync.resources in Synchronization instance. sync.resources is obtained from the Create node. enable A Boolean that specifies whether to synchronize the input edge or not. The sync.fpga io may be floating until a target is specified as the master

Synchronize over PPS Trig

Synchronizes USRP RIO devices over the PPS Trig lines.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources in

Synchronization instance. sync.resources is obtained from the Create node.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable

A Boolean that specifies whether to synchronize the input edge or not.

Note

sync.fpga io

enable

synchronized edge

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### edge

Signal being synchronized. Because the first block this input encounters is a rising edge detector, the input signal edge is treated as a pulse.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### common reference

The "start" signal used by the measurement logic.

When you use the FPGA Align node, the common reference must be the same clock to which the FPGA clock of the target is locked.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### clock x2

Measurement clock used by the measurement logic.

This clock must run at twice the rate of the FPGA Clock, which is the clock that drives the clock-driven loop (CDL) that this node is in. This clock must also derive from the FPGA Clock so that it has a fixed phase relationship. This clock is commonly Data Clock x2.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### sync.fpga io in

The FPGA I/O line to receive the measurement signals on. This line is commonly the PPS TRIG IN line.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### sync.fpga io out

The FPGA I/O line to send the signal out on.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### sync.resources out

The same instance that was passed in for sync.resources.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### synchronization delay

The number of clock cycles of delay that were added by synchronizing the input edge. This value is zero if enable is FALSE. If enable is TRUE, this value is valid only on the master target.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### synchronized edge

The synchronized input edge if enable is TRUE.

Parent topic:

Synchronization

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=synchronize-signal-bus.html language=enus -->
## TOPIC 00018: Synchronize Signal Bus

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `synchronize-signal-bus.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/synchronize-signal-bus.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronously realizes a signal over a bus topology typically using AUX I/O. If this target is the master, it distributes edge on the specified FPGA I/O line on the next falling edge of the CPTR when edge is high. If this target is not the master, it will ignore edge. All targets, master or otherwis

Synchronize Signal Bus

Synchronously realizes a signal over a bus topology typically using AUX I/O.
 If this target is the master, it distributes edge on the specified FPGA I/O line on the next falling edge of the CPTR when edge is high. If this target is not the master, it will ignore edge. All targets, master or otherwise, also read the FPGA I/O line. The synchronized edge output goes high on the next CPTR edge after the edge is read from the FPGA I/O line.

Note

edge

edge

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources in

Synchronization instance. sync.resources is obtained from the Create node.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable

A Boolean that specifies whether to synchronize the input edge or not.

Note

sync.fpga io

enable

synchronized edge

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### edge

Signal being synchronized. Because the first block this input encounters is a rising edge detector, the input signal edge is treated as a pulse.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### sync.fpga io

The FPGA I/O line to send and receive the synchronization signals on.

This line is commonly an AUX I/O line.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### sync.resources out

The same instance that was passed in for sync.resources.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### synchronization delay

The number of clock cycles of delay that were added by synchronizing the input edge. This value is zero if enable is FALSE. If enable is TRUE, this value is valid only on the master target.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### synchronized edge

The synchronized input edge if enable is TRUE.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=synchronize-signal-star.html language=enus -->
## TOPIC 00019: Synchronize Signal Star

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `synchronize-signal-star.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/synchronize-signal-star.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronously realizes a signal over a star topology typically using PPS Trig. If this target is the master, it distributes edge on the specified FPGA I/O line on the next falling edge of the CPTR (when edge is high). If this target is not the master, it ignores edge. All targets, master or otherwis

Synchronize Signal Star

Synchronously realizes a signal over a star topology typically using PPS Trig.
 If this target is the master, it distributes edge on the specified FPGA I/O line on the next falling edge of the CPTR (when edge is high). If this target is not the master, it ignores edge. All targets, master or otherwise, also read the FPGA I/O line. The 
synchronized edge output goes high on the next CPTR edge after the edge is read from the FPGA I/O line.

Note

edge

edge

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### sync.resources in

Synchronization instance. sync.resources is obtained from the Create node.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable

Specifies whether to synchronize the input edge or not.

Note

sync.fpga io in

enable

synchronized edge

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### edge

Signal being synchronized. Because the first block this input encounters is a rising edge detector, the input signal edge is treated as a pulse.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### sync.fpga io in

The FPGA I/O line to receive the synchronization signals on. This line is commonly the PPS Trig In line.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### sync.resources out

The same instance that was passed in for sync.resources.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### sync.fpga io signal out

The signal to send out over an FPGA I/O line. This line is commonly the PPS Trig Out line. Wire this output into an input of FPGA IO Out for Star.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### synchronization delay

The number of clock cycles of delay that were added by synchronizing the input edge. This value is zero if enable is FALSE. If enable is TRUE, this value is valid only on the master target.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### synchronized edge

The synchronized input edge if enable is TRUE.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=time-nodes.html language=enus -->
## TOPIC 00020: Time Nodes

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `time-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/time-nodes.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`

Time Nodes

USRP RIO Nodes (CDL)

Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

Future Event

Configures future events and identifies when events occur.

Future Event Register Bus

Connects a future event instance to the Register Bus.

Timekeeper

Configures and manages Time on the FPGA.

Time Register Bus

Connects Time to the Register Bus.

Parent topic:

USRP RIO Nodes (CDL)

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=time-register-bus.html language=enus -->
## TOPIC 00021: Time Register Bus

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `time-register-bus.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/time-register-bus.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects Time to the Register Bus. time.resources LabVIEW FPGA resources used by Time, obtained from the Create Time node. register instruction specifies a read or write register instruction. This parameter is usually obtained from the register instruction parameter of the Process node. The source o

Time Register Bus

Connects Time to the Register Bus.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### time.resources

LabVIEW FPGA resources used by Time, obtained from the Create Time node.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### register instruction

specifies a read or write register instruction. This parameter is usually obtained from the register instruction parameter of the Process node. The source of this parameter defines the instances of the Register Bus library to which the Synchronization library instance is wired, and is communicated from the host.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### read completion

Indicates whether the register read operation is complete and returns the data from the register read.

Feedback Node

read completion

Process

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### ready for input

Indicates whether the node is ready to accept new input data in the next cycle. Use a Feedback Node to wire this parameter to the ready for output terminal of an upstream node.

Parent topic:

Time Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-fpga-rio-api-ref path=timekeeper.html language=enus -->
## TOPIC 00022: Timekeeper

- bundle_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- source_path: `timekeeper.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-fpga-rio-api-ref/raw/resource/enus/timekeeper.html
- document_id: `ni-usrp-lvnxg-fpga-rio-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures and manages Time on the FPGA. time.resources LabVIEW FPGA resources used by Time, obtained from the Create Time node. common reference The LabVIEW FPGA I/O for the common reference used by all devices. pps The LabVIEW FPGA I/O for the common PPS used by all the devices. pps out The LabVIE

Timekeeper

Configures and manages Time on the FPGA.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### time.resources

LabVIEW FPGA resources used by Time, obtained from the Create Time node.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### common reference

The LabVIEW FPGA I/O for the common reference used by all devices.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### pps

The LabVIEW FPGA I/O for the common PPS used by all the devices.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### pps out

The LabVIEW FPGA I/O for the PPS output from this device.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### time

The time on the device, or the time to set on the device.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### time.previous cptr

The time at the previous CPTR edge.

Parent topic:

Time Nodes
