# NI DOCUMENT BUNDLE: ni-usrp-lvnxg-host-fpga-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-usrp-lvnxg-host-fpga-api-ref start=1 end=41 -->
<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=advanced-configure-active-antenna.html language=enus -->
## TOPIC 00001: Advanced Configure Active Antenna

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `advanced-configure-active-antenna.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/advanced-configure-active-antenna.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates a specified ATR register state for advanced daughterboard antenna configuration. scope The channel to operate on. Valid options are rx/RF 0, rx/RF 1, tx/RF 0, and tx/RF 1. For this node, scope is used to determine which daughterboard to update the ATR state of. atr register The specific ATR

Advanced Configure Active Antenna

Updates a specified ATR register state for advanced daughterboard antenna configuration.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

The channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1. For this node, scope is used to determine which daughterboard to update the ATR state of.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### atr register

The specific ATR register to write to.

The registers correspond to the four states each daughterboard supports. The daughterboard state is set based on whether Rx and Tx are enabled or disabled, using the Enable Front End node. It is safe to call the Enable Front End node after writing to the ATR registers.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### antenna configuration

The antenna state of the daughterboard.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

Parent topic:

Advanced Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=advanced-configure-adc-gain.html language=enus -->
## TOPIC 00002: Advanced Configure ADC Gain

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `advanced-configure-adc-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/advanced-configure-adc-gain.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates a specified ATR Register state for advanced daughterboard ADC gain configuration. ADC Gain has a range of 0 dB to 6 dB with a 0.5 step. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. adc gain Gain setting of the daughterboard ADC.

Advanced Configure ADC Gain

Updates a specified ATR Register state for advanced daughterboard ADC gain configuration.
 ADC Gain has a range of 0 dB to 6 dB with a 0.5 step.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### adc gain

Gain setting of the daughterboard ADC. This has a range of 0 dB to 6 dB with a 0.5 step.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

The channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1. For this node, scope is used to determine which daughterboard to update the ATR state of.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Advanced Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=advanced-configure-atr-gain.html language=enus -->
## TOPIC 00003: Advanced Configure ATR Gain

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `advanced-configure-atr-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/advanced-configure-atr-gain.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates a specified ATR register state for advanced ATR gain configuration. scope is the channel to operate on. Valid options are rx/RF 0, rx/RF 1, tx/RF 0, and tx/RF 1. For this node, scope is used to determine which daughterboard to update the ATR state of and whether to update the gain of Rx or T

Advanced Configure ATR Gain

Updates a specified ATR register state for advanced ATR gain configuration.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

is the channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1. For this node, scope is used to determine which daughterboard to update the ATR state of and whether to update the gain of Rx or Tx.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### atr register

The specific ATR register to write to.

The registers correspond to the four states each daughterboard supports. The daughterboard state is set based on whether Rx and Tx are enabled or disabled, using the Enable Front End node. It is safe to call the Enable Front End node after writing to the ATR registers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### gain

The gain of the Rx or Tx signal. This gain is not coerced. Verify the input is in the daughterboard gain range.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Advanced Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=advanced-configure-lpf.html language=enus -->
## TOPIC 00004: Advanced Configure LPF

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `advanced-configure-lpf.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/advanced-configure-lpf.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates a specified ATR register state for advanced LO Low Pass Filter configuration. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. atr register The specific ATR register to write to. The registers correspond to the four states each daugh

Advanced Configure LPF

Updates a specified ATR register state for advanced LO Low Pass Filter configuration.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### atr register

The specific ATR register to write to.

The registers correspond to the four states each daughterboard supports. The daughterboard state is set based on whether Rx and Tx are enabled or disabled, using the Enable Front End node. It is safe to call the Enable Front End node after writing to the ATR registers.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### lo lpf enable

LO LPF state of the daughterboard.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

is the channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1. Use this parameter to determine which daughterboard to update the ATR register state of.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Advanced Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=advanced-configure-power-and-mixer.html language=enus -->
## TOPIC 00005: Advanced Configure Power and Mixer

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `advanced-configure-power-and-mixer.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/advanced-configure-power-and-mixer.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates a specified ATR register state for advanced daughterboard power and mixer enable configuration. If you power the device off, you must reconfigure the LO using the Configure LO node. scope is the channel to operate on. Valid options are rx/RF 0, rx/RF 1, tx/RF 0, and tx/RF 1. For this node, s

Advanced Configure Power and Mixer

Updates a specified ATR register state for advanced daughterboard power and mixer enable configuration. If you power the device off, you must reconfigure the LO using the Configure LO node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

is the channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1. For this node, scope is used to determine which daughterboard to update the ATR state of and whether to update the power and mixer of Rx or Tx.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### atr register

The specific ATR register to write to.

The registers correspond to the four states each daughterboard supports. The daughterboard state is set based on whether Rx and Tx are enabled or disabled, using the Enable Front End node. It is safe to call the Enable Front End node after writing to the ATR registers.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### power enable

The power state of Rx or Tx of the daughterboard.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### mixer enable

The mixer enable for Rx or Tx of the daughterboard.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

Parent topic:

Advanced Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=advanced-nodes.html language=enus -->
## TOPIC 00006: Advanced Nodes

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `advanced-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/advanced-nodes.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`

Advanced Nodes

USRP RIO Nodes (Host)

Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

Advanced Configure Active Antenna

Updates a specified ATR register state for advanced daughterboard antenna configuration.

Advanced Configure ADC Gain

Updates a specified ATR Register state for advanced daughterboard ADC gain configuration.

Advanced Configure ATR Gain

Updates a specified ATR register state for advanced ATR gain configuration.

Advanced Configure LPF

Updates a specified ATR register state for advanced LO Low Pass Filter configuration.

Advanced Configure Power and Mixer

Updates a specified ATR register state for advanced daughterboard power and mixer enable configuration. If you power the device off, you must reconfigure the LO using the Configure LO node.

Construct ATR

Constructs the value that the Write ATR Register node uses to write to an ATR register for advanced daughterboard configuration.

Write ATR Register

Writes to the ATR register of a daughterboard.

Parent topic:

USRP RIO Nodes (Host)

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=calculate-level-range.html language=enus -->
## TOPIC 00007: Calculate Level Range

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `calculate-level-range.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/calculate-level-range.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates the minimum and maximum level, in dBm, for a given frequency and scope based on the characterization data of the device. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. frequency The frequency for which to calculate the valid lev

Calculate Level Range

Calculates the minimum and maximum level, in dBm, for a given frequency and scope based on the characterization data of the device.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency

The frequency for which to calculate the valid level range.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### min level

Smallest value, in dBm, this scope can be configured for.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### max level

Largest value, in dBm, this scope can be configured for.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=clear-future-event.html language=enus -->
## TOPIC 00008: Clear Future Event

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `clear-future-event.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/clear-future-event.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all future events from a given future event instance. The Initialize node must execute before the Clear Future Event node. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. error in Error conditions that occur before this node runs. Th

Clear Future Event

Clears all future events from a given future event instance.
 The Initialize node must execute before the Clear Future Event node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### instance

indicates that the future event time is valid.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Time Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=clocking-nodes.html language=enus -->
## TOPIC 00009: Clocking Nodes

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `clocking-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/clocking-nodes.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`

Clocking Nodes

USRP RIO Nodes (Host)

Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

Configure Reference Out

Controls the output of the reference frequency source output on REF OUT.

Parent topic:

USRP RIO Nodes (Host)

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=close.html language=enus -->
## TOPIC 00010: Close

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `close.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/close.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session to the USRP RIO nodes. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behav

Close

Closes the session to the USRP RIO nodes.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### fpga ref

Reference to the FPGA bitfile on the device.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Error Conditions

error in

Parent topic:

USRP RIO Nodes (Host)

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=configure-cptr-common-reference-edge.html language=enus -->
## TOPIC 00011: Configure CPTR Common Reference Edge

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `configure-cptr-common-reference-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/configure-cptr-common-reference-edge.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures which edge of the common reference is used to generate the CPTR. Configuring the common reference edge is used to account for wiring delays between devices. You must configure the common reference before Set Time executes. niusrprio session in Object created by the Open node and used as t

Configure CPTR Common Reference Edge

Configures which edge of the common reference is used to generate the CPTR.
 Configuring the common reference edge is used to account for wiring delays between devices. You must configure the common reference before Set Time executes.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### cptr common reference edge

Configures which edge of the common reference the PPS identifies for the CPTR.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

The Initialize node must execute before this node.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=configure-cptr-pps-period.html language=enus -->
## TOPIC 00012: Configure CPTR PPS Period

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `configure-cptr-pps-period.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/configure-cptr-pps-period.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the period of the internal PPS, in seconds. Configure the internal PPS period before you configure Set Time. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. pps period Configures the internal PPS period. Specify the pps period in

Configure CPTR PPS Period

Configures the period of the internal PPS, in seconds.
 Configure the internal PPS period before you configure Set Time.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### pps period

Configures the internal PPS period. Specify the pps period in units of seconds.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

The Initialize node must execute before this node.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=configure-cptr-pps-source.html language=enus -->
## TOPIC 00013: Configure CPTR PPS Source

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `configure-cptr-pps-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/configure-cptr-pps-source.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures which PPS is used to generate the CPTR. Configure the internal PPS period before you configure Set Time. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. pps source Configures which PPS to use for the CPTR. Options for pps source

Configure CPTR PPS Source

Configures which PPS is used to generate the CPTR.
 Configure the internal PPS period before you configure Set Time.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### pps source

Configures which PPS to use for the CPTR. Options for pps source include 
External PPS, 
GPS PPS, and 
Internal PPS.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

The Initialize node must execute before this node.

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=configure-gain.html language=enus -->
## TOPIC 00014: Configure Gain

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `configure-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/configure-gain.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the amount of gain for the channel. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. gain The amount of gain, in dB, requested. error in Error conditions that occur before this node runs. The node responds to this input according

Configure Gain

Configures the amount of gain for the channel.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### gain

The amount of gain, in dB, requested.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced gain

The amount of gain, in dB, applied.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

RF Front End Configuration Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=configure-lo.html language=enus -->
## TOPIC 00015: Configure LO

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `configure-lo.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/configure-lo.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency of the local oscillator. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. frequency Requested frequency, in hertz, to tune the local oscillator to. error in Error conditions that occur before this node runs. The node

Configure LO

Configures the frequency of the local oscillator.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency

Requested frequency, in hertz, to tune the local oscillator to.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced frequency

Actual frequency, in hertz, of the local oscillator.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

RF Front End Configuration Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=configure-reference-out.html language=enus -->
## TOPIC 00016: Configure Reference Out

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `configure-reference-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/configure-reference-out.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls the output of the reference frequency source output on REF OUT. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. enable A Boolean that controls the reference frequency source output. error in Error conditions that occur before this

Configure Reference Out

Controls the output of the reference frequency source output on REF OUT.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable

A Boolean that controls the reference frequency source output.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Clocking Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=construct-atr.html language=enus -->
## TOPIC 00017: Construct ATR

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `construct-atr.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/construct-atr.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Constructs the value that the Write ATR Register node uses to write to an ATR register for advanced daughterboard configuration. daughterboard Daughterboard type to construct the register value for. antenna configuration The antenna state of the daughterboard. lo lpf enable LO LPF state of the daugh

Construct ATR

Constructs the value that the Write ATR Register node uses to write to an ATR register for advanced daughterboard configuration.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### daughterboard

Daughterboard type to construct the register value for.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### antenna configuration

The antenna state of the daughterboard.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### lo lpf enable

LO LPF state of the daughterboard.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### rx.configuration

The settings to use for the Rx side of the daughterboard, including power enable, mixer enable, and gain.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### tx.configuration

The settings to use for the Tx side of the daughterboard, including power enable, mixer enable, and gain.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### spi address

Specifies the destination for configuration packets sent to the daughterboard. Valid only for USRP-29x4 devices.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### cpld enable

Specifies the CPLD power state on the daughterboard. Valid only for USRP-29x4 devices.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### atr register value

32-bit value to program an ATR register with.

Parent topic:

Advanced Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=enable-front-end.html language=enus -->
## TOPIC 00018: Enable Front End

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `enable-front-end.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/enable-front-end.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the RF front end for the given channel. Use this node to toggle the active ATR state. Rx Tx ATR State disable disable Idle disable enable Tx only enable disable Rx only enable enable Full duplex niusrprio session in Object created by the Open node and used as the session handle for the USRP

Enable Front End

Enables the RF front end for the given channel.
 Use this node to toggle the active ATR state.

| Rx | Tx | ATR State |
| --- | --- | --- |
| disable | disable | Idle |
| disable | enable | Tx only |
| enable | disable | Rx only |
| enable | enable | Full duplex |

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable

Signal that enables the device front end.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Configuring the Daughterboard

scope

Parent topic:

RF Front End Configuration Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=fpga-self-synchronization.html language=enus -->
## TOPIC 00019: FPGA Self Synchronization

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `fpga-self-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/fpga-self-synchronization.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this type of synchronization in conjunction with FPGA Align on the FPGA. Refer to the FPGA nodes for documentation. When this node finishes, the FPGAs are synchronized. niusrprio sessions in Objects created by the Open node and used as the session handles for the USRP RIO nodes. error in Error c

FPGA Self Synchronization

Use this type of synchronization in conjunction with FPGA Align on the FPGA.
 Refer to the FPGA nodes for documentation. When this node finishes, the FPGAs are synchronized.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### niusrprio sessions in

Objects created by the Open node and used as the session handles for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1du16.png']

##### sync.cptr.period

The period (in clocks) of the common periodic time reference (CPTR).

FPGA Align

sync.cptr.period

Align

common reference rate

120 MHz

10 MHz

Host Align

sync.cptr.period

sync.fpga io

50 ns

50 ns

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### niusrprio sessions out

niUsrpRio sessions used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=get-future-event.html language=enus -->
## TOPIC 00020: Get Future Event

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `get-future-event.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/get-future-event.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the future event time on the FPGA for a given future event instance. The future event time is only valid if valid is True. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. error in Error conditions that occur before this node runs. The

Get Future Event

Gets the future event time on the FPGA for a given future event instance.
 The future event time is only valid if valid is True.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### instance

indicates that the future event time is valid.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### future event time

Time used to schedule a future event or the scheduled future event time.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### valid

indicates the future event time is valid.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

The Time node and Initialize node must execute before the Get Future Event node.

Parent topic:

Time Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=get-gps-nmea-strings.html language=enus -->
## TOPIC 00021: Get GPS Nmea Strings

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `get-gps-nmea-strings.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/get-gps-nmea-strings.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Nmea string GPRMC, GPGGA, or both. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. nmea string select The Nmea string(s) that you want. error in Error conditions that occur before this node runs. The node responds to this input acc

Get GPS Nmea Strings

Gets the Nmea string GPRMC, GPGGA, or both.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### nmea string select

The Nmea string(s) that you want.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### nmea string

The requested Nmea string(s).

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

GPS Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=get-time-multi.html language=enus -->
## TOPIC 00022: Get Time (Multi)

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `get-time-multi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/get-time-multi.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time on the FPGA. Reads the time from the previous CPTR, or now. This node cannot read the time from the next CPTR and will cause an error. niusrprio sessions in Objects created by the Open node and used as the session handles for the USRP RIO nodes. error in Error conditions that occur bef

Get Time (Multi)

Gets the time on the FPGA. Reads the time from the previous CPTR, or now.
 This node cannot read the time from the next CPTR and will cause an error.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### niusrprio sessions in

Objects created by the Open node and used as the session handles for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### when

indicates when to get or set the time.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### niusrprio sessions out

niUsrpRio sessions used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### times

indicates the times to set on the devices

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

TheInitialize node must execute before the Get Time node.

Parent topic:

Time Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=get-time-single.html language=enus -->
## TOPIC 00023: Get Time (Single)

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `get-time-single.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/get-time-single.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time on the FPGA. Reads the time from the previous CPTR, or now. This node cannot read the time from the next CPTR and will cause an error. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. error in Error conditions that occur before

Get Time (Single)

Gets the time on the FPGA. Reads the time from the previous CPTR, or now.
 This node cannot read the time from the next CPTR and will cause an error.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### when

indicates when to get or set the time.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### time

Time to set on the devices.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

The Initialize node must execute before the Get Time node.

Parent topic:

Time Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=gps-nodes.html language=enus -->
## TOPIC 00024: GPS Nodes

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `gps-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/gps-nodes.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the GPS in the application.

GPS Nodes

Specifies the behavior of the GPS in the application.

USRP RIO Nodes (Host)

Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

Get GPS Nmea Strings

Gets the Nmea string GPRMC, GPGGA, or both.

Parent topic:

USRP RIO Nodes (Host)

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=host-driven-synchronization.html language=enus -->
## TOPIC 00025: Host Driven Synchronization

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `host-driven-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/host-driven-synchronization.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this flavor of synchronization in conjunction with Host Align on the FPGA. When this node finishes, the FPGAs are synchronized. niusrprio sessions in Objects created by the Open node and used as the session handles for the USRP RIO nodes. error in Error conditions that occur before this node run

Host Driven Synchronization

Use this flavor of synchronization in conjunction with Host Align on the FPGA.
 When this node finishes, the FPGAs are synchronized.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### niusrprio sessions in

Objects created by the Open node and used as the session handles for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### sync.cptr.period

The period (in clocks) of the common periodic time reference (CPTR). The default value automatically sets the CPTR period to 10 MHz.

FPGA Align

sync.cptr.period

Align

common reference

10 MHz

120 MHz

10 MHz

Host Align

sync.cptr.period

sync.fpga io

50 ns

120 MHz

8.333 ns

50 ns

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### niusrprio sessions out

niUsrpRio sessions used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=initialize-multi.html language=enus -->
## TOPIC 00026: Initialize (Multi)

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `initialize-multi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/initialize-multi.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes the Time library. This node must execute before any other Time nodes execute. niusrprio sessions in Objects created by the Open node and used as the session handles for the USRP RIO nodes. error in Error conditions that occur before this node runs. The node responds to this input accordi

Initialize (Multi)

Initializes the Time library.
 This node must execute before any other Time nodes execute.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### niusrprio sessions in

Objects created by the Open node and used as the session handles for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### niusrprio sessions out

niUsrpRio sessions used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

The Open node must execute before this node.

Parent topic:

Time Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=initialize-single.html language=enus -->
## TOPIC 00027: Initialize (Single)

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `initialize-single.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/initialize-single.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes the Time library. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default

Initialize (Single)

Initializes the Time library.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

This node must execute before any other Time nodes execute. Open must execute before this node.

Parent topic:

Time Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=open.html language=enus -->
## TOPIC 00028: Open 2

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `open.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/open.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a session to the USRP RIO design library, creates the necessary connections to the hardware, and initializes the device. fpga ref Reference to the FPGA bitfile on the device. reference frequency source Reference source to use for the clocks of the device. The reference frequency must be 10 MHz

Open 2

Opens a session to the USRP RIO design library, creates the necessary connections to the hardware, and initializes the device.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### fpga ref

Reference to the FPGA bitfile on the device.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### reference frequency source

Reference source to use for the clocks of the device. The reference frequency must be 10 MHz.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### GPSDO Power Enable

Turns on the power for the GPSDO.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

How long, in seconds, to keep retrying before giving up.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

USRP RIO Nodes (Host)

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=query-status.html language=enus -->
## TOPIC 00029: Query Status

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `query-status.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/query-status.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries an attribute for its current status. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. what to query for Attribute to query. error in Error conditions that occur before this node runs. The node responds to this input according to stan

Query Status

Queries an attribute for its current status.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### what to query for

Attribute to query.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### status

Boolean that returns the current value of the attribute.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=repeat-host-driven-synchronization.html language=enus -->
## TOPIC 00030: Repeat Host Driven Synchronization

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `repeat-host-driven-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/repeat-host-driven-synchronization.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this flavor of synchronization in conjunction with Host Align on the FPGA. When this node finishes, the FPGAs are synchronized. Use this version of synchronization to return to a known synchronization state from a previous run. It is possible for the FPGAs to not be synchronized if the synchroni

Repeat Host Driven Synchronization

Use this flavor of synchronization in conjunction with Host Align on the FPGA.
 When this node finishes, the FPGAs are synchronized. Use this version of synchronization to return to a known synchronization state from a previous run. It is possible for the FPGAs to not be synchronized if the synchronization data in is incorrect. Synchronization data is also valid only for a given system configuration. If the location of the USRP RIO device, chassis, or slot changes, synchronization data may not be valid.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### niusrprio sessions in

Objects created by the Open node and used as the session handles for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### synchronization data in valid

A flag to use the values from a previous synchronization run (synchronization data in) to return the FPGAs to that synchronization state.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### synchronize data in

Returns the FPGAs to the previous synchronization state using synchronization data from that synchronization run.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### sync.cptr.period

The period (in clocks) of the common periodic time reference (CPTR). The default value automatically sets the CPTR period to 10 MHz.

FPGA Align

sync.cptr.period

Align

common reference

120 MHz

10 MHz

Host Align

sync.cptr.period

sync.fpga io

50 ns

120 MHz

~8.333 ns

50 ns

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### niusrprio sessions out

niUsrpRio sessions used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/i1du16.png']

##### synchronization data out

Synchronization data from the completed synchronization run that can be used to return the FPGAs to that synchronization state.

The data is valid only if the FPGAs were successfully synchronized with no output error.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=rf-and-front-end-config-nodes.html language=enus -->
## TOPIC 00031: RF Front End Configuration Nodes

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `rf-and-front-end-config-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/rf-and-front-end-config-nodes.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`

RF Front End Configuration Nodes

USRP RIO Nodes (Host)

Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

Configure Gain

Configures the amount of gain for the channel.

Configure LO

Configures the frequency of the local oscillator.

Enable Front End

Enables the RF front end for the given channel.

Parent topic:

USRP RIO Nodes (Host)

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=set-future-event.html language=enus -->
## TOPIC 00032: Set Future Event

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `set-future-event.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/set-future-event.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Programs a future event for a given future event instance. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. future event time The time used to schedule a future event or the scheduled future event time. force is the future event to set the n

Set Future Event

Programs a future event for a given future event instance.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### future event time

The time used to schedule a future event or the scheduled future event time.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### force

is the future event to set the new time.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### instance

indicates that the future event time is valid.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

The Initialize node must execute before the Set Future Event node.

Parent topic:

Time Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=set-time-multi.html language=enus -->
## TOPIC 00033: Set Time (Multi)

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `set-time-multi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/set-time-multi.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time on the FPGA. Set the time at the next CPTR, or now. This node cannot set the time at the previous CPTR and will cause an error. niusrprio sessions in Objects created by the Open node and used as the session handles for the USRP RIO nodes. time Time to set on the devices. error in Error

Set Time (Multi)

Sets the time on the FPGA. Set the time at the next CPTR, or now.
 This node cannot set the time at the previous CPTR and will cause an error.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dcclst.png']

##### niusrprio sessions in

Objects created by the Open node and used as the session handles for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### time

Time to set on the devices.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### when

indicates when to get or set the time.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### niusrprio sessions out

niUsrpRio sessions used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

Initialize must execute before this node.

Parent topic:

Time Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=set-time-single.html language=enus -->
## TOPIC 00034: Set Time (Single)

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `set-time-single.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/set-time-single.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time on the FPGA. Set the time at the next CPTR, or now. This node cannot set the time at the previous CPTR and will cause an error. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. time Time to set on the devices. error in Error co

Set Time (Single)

Sets the time on the FPGA. Set the time at the next CPTR, or now.
 This node cannot set the time at the previous CPTR and will cause an error.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### time

Time to set on the devices.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### when

indicates when to get or set the time.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

Initialize must execute before this node.

Parent topic:

Time Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=synchronization-nodes.html language=enus -->
## TOPIC 00035: Synchronization Nodes

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `synchronization-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/synchronization-nodes.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`

Synchronization Nodes

USRP RIO Nodes (Host)

Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

FPGA Self Synchronization

Use this type of synchronization in conjunction with FPGA Align on the FPGA.

Host Driven Synchronization

Use this flavor of synchronization in conjunction with Host Align on the FPGA.

Repeat Host Driven Synchronization

Use this flavor of synchronization in conjunction with Host Align on the FPGA.

Parent topic:

USRP RIO Nodes (Host)

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=time-advanced.html language=enus -->
## TOPIC 00036: Advanced

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `time-advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/time-advanced.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`

Advanced

Time Nodes

Configure CPTR Common Reference Edge

Configures which edge of the common reference is used to generate the CPTR.

Configure CPTR PPS Period

Configures the period of the internal PPS, in seconds.

Configure CPTR PPS Source

Configures which PPS is used to generate the CPTR.

Parent topic:

Time Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=time-nodes.html language=enus -->
## TOPIC 00037: Time Nodes

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `time-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/time-nodes.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`

Time Nodes

USRP RIO Nodes (Host)

Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

Advanced

Clear Future Event

Clears all future events from a given future event instance.

Initialize (Multi)

Initializes the Time library.

Initialize (Single)

Initializes the Time library.

Get Future Event

Gets the future event time on the FPGA for a given future event instance.

Get Time (Multi)

Gets the time on the FPGA. Reads the time from the previous CPTR, or now.

Get Time (Single)

Gets the time on the FPGA. Reads the time from the previous CPTR, or now.

Set Future Event

Programs a future event for a given future event instance.

Set Time (Multi)

Sets the time on the FPGA. Set the time at the next CPTR, or now.

Set Time (Single)

Sets the time on the FPGA. Set the time at the next CPTR, or now.

Parent topic:

USRP RIO Nodes (Host)

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=usrp-rio-nodes.html language=enus -->
## TOPIC 00038: USRP RIO Nodes (Host)

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `usrp-rio-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/usrp-rio-nodes.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

USRP RIO Nodes (Host)

Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

Close

Closes the session to the USRP RIO nodes.

Open 2

Opens a session to the USRP RIO design library, creates the necessary connections to the hardware, and initializes the device.

Advanced Nodes

Clocking Nodes

GPS Nodes

Specifies the behavior of the GPS in the application.

RF Front End Configuration Nodes

Synchronization Nodes

Time Nodes

Utility Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=utility-nodes.html language=enus -->
## TOPIC 00039: Utility Nodes

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `utility-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/utility-nodes.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`

Utility Nodes

USRP RIO Nodes (Host)

Use USRP RIO nodes to develop applications for USRP Software Defined Radio Reconfigurable Devices.

Calculate Level Range

Calculates the minimum and maximum level, in dBm, for a given frequency and scope based on the characterization data of the device.

Query Status

Queries an attribute for its current status.

Wait until Done

Polls an attribute until that attribute becomes true.

Parent topic:

USRP RIO Nodes (Host)

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=wait-until-done.html language=enus -->
## TOPIC 00040: Wait until Done

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `wait-until-done.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/wait-until-done.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Polls an attribute until that attribute becomes true. niusrprio session in Object created by the Open node and used as the session handle for the USRP RIO nodes. what to wait for The attribute to poll. polling interval How long, in seconds, to wait between retries. timeout How long, in seconds, to k

Wait until Done

Polls an attribute until that attribute becomes true.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### what to wait for

The attribute to poll.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### polling interval

How long, in seconds, to wait between retries.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

How long, in seconds, to keep retrying before giving up.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-usrp-lvnxg-host-fpga-api-ref path=write-atr-register.html language=enus -->
## TOPIC 00041: Write ATR Register

- bundle_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- source_path: `write-atr-register.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-lvnxg-host-fpga-api-ref/raw/resource/enus/write-atr-register.html
- document_id: `ni-usrp-lvnxg-host-fpga-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes to the ATR register of a daughterboard. The ATR register provides advanced configuration for a daughterboard. Do not continue to configure the daughterboard after writing to the ATR registers because the ATR registers may be overwritten and these configurations will be lost. niusrprio session

Write ATR Register

Writes to the ATR register of a daughterboard. The ATR register provides advanced configuration for a daughterboard. Do not continue to configure the daughterboard after writing to the ATR registers because the ATR registers may be overwritten and these configurations will be lost.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### niusrprio session in

Object created by the Open node and used as the session handle for the USRP RIO nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### atr register

The specific ATR register to write to.

The registers correspond to the four states each daughterboard supports. The daughterboard state is set based on whether Rx and Tx are enabled or disabled, using the Enable Front End node. It is safe to call the Enable Front End node after you write to the ATR registers.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### atr register value

32-bit value to program an ATR register with.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

is the channel to operate on. Valid options are 
rx/RF 0, 
rx/RF 1, 
tx/RF 0, and 
tx/RF 1. For this node, scope is used to determine which daughterboard to update the ATR state of and whether to update the power and mixer of Rx or Tx.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### niusrprio session out

The niUsrpRio session used in all subsequent USRP RIO host nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Advanced Nodes
