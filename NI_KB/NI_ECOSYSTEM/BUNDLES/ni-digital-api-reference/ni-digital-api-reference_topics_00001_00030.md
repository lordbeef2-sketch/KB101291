# NI DOCUMENT BUNDLE: ni-digital-api-reference

<!--NI_BUNDLE_CHUNK bundle=ni-digital-api-reference start=1 end=30 -->
<!--NI_TOPIC bundle=ni-digital-api-reference path=abort-keep-alive.html language=enus -->
## TOPIC 00001: Abort Keep Alive

- bundle_id: `ni-digital-api-reference`
- source_path: `abort-keep-alive.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/abort-keep-alive.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the keep alive pattern if it is currently running. If a pattern burst is in progress, the node aborts the pattern burst. If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs to the last keep alive vector, and the new pattern burst starts on the ne

Abort Keep Alive

Stops the keep alive pattern if it is currently running.

If a pattern burst is in progress, the node aborts the pattern burst. If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs to the last keep alive vector, and the new pattern burst starts on the next cycle.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-api-reference path=abort.html language=enus -->
## TOPIC 00002: Abort

- bundle_id: `ni-digital-api-reference`
- source_path: `abort.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/abort.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops bursting the pattern. session in Instrument session obtained from the niDigital Initialize with Optionsnode. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session

Abort

Stops bursting the pattern.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-api-reference path=action.html language=enus -->
## TOPIC 00003: Action

- bundle_id: `ni-digital-api-reference`
- source_path: `action.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/action.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Action nodes to perform tasks with a digital pattern instrument.

Action

Use the Action nodes to perform tasks with a digital pattern instrument.

NI-Digital Pattern Driver Nodes

nodes

Burst Pattern

start label

Source and Capture

nodes

Sequencer Flags and Registers

nodes

Static

nodes

PPMU

nodes

Frequency Count

nodes

Clock Generator

nodes

History RAM

nodes

Low Level

nodes

Parent topic:

NI-Digital Pattern Driver Nodes

<!--NI_TOPIC bundle=ni-digital-api-reference path=burst-pattern-synchronized.html language=enus -->
## TOPIC 00004: Burst Pattern (Synchronized)

- bundle_id: `ni-digital-api-reference`
- source_path: `burst-pattern-synchronized.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/burst-pattern-synchronized.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uses the start label you specify to burst a pattern on the sites you specify. Use this node to burst a pattern on digital pattern instruments that you have previously synchronized using NI-TClk. wait until done A Boolean that indicates whether to wait until the bursting is complete. True Waits until

Burst Pattern (Synchronized)

Uses the start label you specify to burst a pattern on the sites you specify.

Use this node to burst a pattern on digital pattern instruments that you have previously synchronized using NI-TClk.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### wait until done

A Boolean that indicates whether to wait until the bursting is complete.

| True | Waits until the bursting is complete. |
| --- | --- |
| False | Does not wait until the bursting is complete. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### select digital function

A Boolean that specifies whether to select the digital function for the pins in the pattern prior to bursting.

| True | Selects the digital function for the pins in the pattern prior to bursting. |
| --- | --- |
| False | Does not select the digital function for the pins in the pattern prior to bursting. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### start label

Pattern name or exported pattern label from which to start bursting the pattern.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### sessions in

Instrument sessions obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### site list

The sites on which to burst the pattern as a comma-delimited list of strings in the form 
siteN, where 
N is the site number.

If you specify an empty string, the pattern is burst on all sites.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The maximum time allowed for this node to complete, in seconds.

If this node does not complete within this time interval, the node returns an error if wait until done is True.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### sessions out

Handle that identifies the sessions in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Multi-Instrument Synchronization

<!--NI_TOPIC bundle=ni-digital-api-reference path=clock-generator-generate-clock.html language=enus -->
## TOPIC 00005: Clock Generator Generate Clock

- bundle_id: `ni-digital-api-reference`
- source_path: `clock-generator-generate-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/clock-generator-generate-clock.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures clock generator frequency and initiates clock generation on the specified channel(s) or pin(s) and pin group(s). session in Instrument session obtained from the niDigital Initialize with Optionsnode. error in Error conditions that occur before this node runs. The node responds to this inp

Clock Generator Generate Clock

Configures clock generator frequency and initiates clock generation on the specified channel(s) or pin(s) and pin group(s).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

List of channel names or list of pins. Do not pass a mix of channel names and pin names.

An empty string denotes all digital pattern instrument channels.

Specify channel names using the form 
 PXI1Slot3/0,2-3 or 
 PXI1Slot3/0,PXI1Slot3/2-3, where 
 PXI1Slot3 is the instrument resource name and 
 0, 
 2, 
 3 are channel names.

To specify channels from multiple instruments, use the form 
 PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis.

##### Site Considerations and Syntax

Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form 
 siteN/pinName, where 
 N is the site number. This node ignores pins that are not mapped to the digital pattern instrument.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency

The frequency of the clock generation, in Hz.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### select digital function?

A Boolean that specifies whether to select the digital function for the pins in the pattern prior to bursting.

| True | Selects the digital function for the pins in the pattern prior to bursting. |
| --- | --- |
| False | Does not select the digital function for the pins in the pattern prior to bursting. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Clock Generator

<!--NI_TOPIC bundle=ni-digital-api-reference path=clock-generator-initiate.html language=enus -->
## TOPIC 00006: Clock Generator Initiate

- bundle_id: `ni-digital-api-reference`
- source_path: `clock-generator-initiate.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/clock-generator-initiate.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates clock generation on the specified channel(s) or pin(s) and pin group(s). session in Instrument session obtained from the niDigital Initialize with Optionsnode. channel list List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all

Clock Generator Initiate

Initiates clock generation on the specified channel(s) or pin(s) and pin group(s).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

List of channel names or list of pins. Do not pass a mix of channel names and pin names.

An empty string denotes all digital pattern instrument channels.

Specify channel names using the form 
 PXI1Slot3/0,2-3 or 
 PXI1Slot3/0,PXI1Slot3/2-3, where 
 PXI1Slot3 is the instrument resource name and 
 0, 
 2, 
 3 are channel names.

To specify channels from multiple instruments, use the form 
 PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis.

##### Site Considerations and Syntax

Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form 
 siteN/pinName, where 
 N is the site number. This node ignores pins that are not mapped to the digital pattern instrument.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-api-reference path=clock-generator.html language=enus -->
## TOPIC 00007: Clock Generator

- bundle_id: `ni-digital-api-reference`
- source_path: `clock-generator.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/clock-generator.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Clock Generator nodes to drive a free-running clock at a specified frequency from a digital pin.

Clock Generator

Use the Clock Generator nodes to drive a free-running clock at a specified frequency from a digital pin.

Action

nodes

Clock Generator Generate Clock

Configures clock generator frequency and initiates clock generation on the specified channel(s) or pin(s) and pin group(s).

Clock Generator Abort

Stops clock generation on the specified channel(s) or pin(s) and pin group(s).

Low Level

nodes

Parent topic:

Action

<!--NI_TOPIC bundle=ni-digital-api-reference path=close.html language=enus -->
## TOPIC 00008: Close

- bundle_id: `ni-digital-api-reference`
- source_path: `close.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/close.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the specified instrument session to a digital pattern instrument, aborts pattern execution, and unloads pattern memory. The channels on a digital pattern instrument remain in their current state. session in Instrument session obtained from the niDigital Initialize with Optionsnode. error in E

Close

Closes the specified instrument session to a digital pattern instrument, aborts pattern execution, and unloads pattern memory.

The channels on a digital pattern instrument remain in their current state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

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

NI-Digital Pattern Driver Nodes

<!--NI_TOPIC bundle=ni-digital-api-reference path=commit.html language=enus -->
## TOPIC 00009: Commit

- bundle_id: `ni-digital-api-reference`
- source_path: `commit.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/commit.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument. If you do not call the niDigital Commit node, then the niDigital Initiate node or the niDigital Burst Pattern node will implicitly call this node for you. Calling th

Commit

Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument.

If you do not call the niDigital Commitnode, then the niDigital Initiatenode or the niDigital Burst Patternnode will implicitly call this node for you. Calling this node moves the session from the Uncommitted state to the Committed state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-api-reference path=config-time-set-compare-edge-strobe.html language=enus -->
## TOPIC 00010: Configure Time Set Compare Edges (Strobe)

- bundle_id: `ni-digital-api-reference`
- source_path: `config-time-set-compare-edge-strobe.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/config-time-set-compare-edge-strobe.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the strobe edge time for the specified pins. session in Instrument session obtained from the niDigital Initialize with Optionsnode. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Def

Configure Time Set Compare Edges (Strobe)

Configures the strobe edge time for the specified pins.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### pin list

List of pin and pin group names for which to configure the time set edges.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### time set

Specifies the time set you want to configure.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### compare strobe

Time when the comparison happens within a vector period.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configure Time Set Compare Edges

<!--NI_TOPIC bundle=ni-digital-api-reference path=configuration.html language=enus -->
## TOPIC 00011: Configuration

- bundle_id: `ni-digital-api-reference`
- source_path: `configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/configuration.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these nodes to configure a digital pattern instrument.

Configuration

Use these nodes to configure a digital pattern instrument.

NI-Digital Pattern Driver Nodes

nodes

Pin Map

nodes

Low Level

nodes

node

Select Function

Specifies whether digital pattern instrument channels are controlled by the PPMU, Digital, disconnected, or off. Changes take effect immediately.

Levels and Timing

nodes

Levels

nodes

Time Set

nodes

TDR

nodes

Pattern

nodes

Trigger

nodes

PPMU

nodes

DC Voltage

nodes

DC Current

nodes

Frequency Count

node

History RAM

nodes

Parent topic:

NI-Digital Pattern Driver Nodes

<!--NI_TOPIC bundle=ni-digital-api-reference path=configure-active-load-levels.html language=enus -->
## TOPIC 00012: Configure Active Load Levels

- bundle_id: `ni-digital-api-reference`
- source_path: `configure-active-load-levels.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/configure-active-load-levels.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures I[OL], I[OH], and V[COM] levels for the active load on the pins you specify. The DUT sources or sinks current based on the level values. To enable active load, set the termination mode to Active Load. To disable active load, set the termination mode of the instrument to High Z or V[TERM].

Configure Active Load Levels

Configures I<sub>OL</sub>, I<sub>OH</sub>, and V<sub>COM</sub> levels for the active load on the pins you specify.

The DUT sources or sinks current based on the level values. To enable active load, set the termination mode to Active Load. To disable active load, set the termination mode of the instrument to High Z or V<sub>TERM</sub>.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

List of channel names or list of pins. Do not pass a mix of channel names and pin names.

An empty string denotes all digital pattern instrument channels.

Specify channel names using the form 
 PXI1Slot3/0,2-3 or 
 PXI1Slot3/0,PXI1Slot3/2-3, where 
 PXI1Slot3 is the instrument resource name and 
 0, 
 2, 
 3 are channel names.

To specify channels from multiple instruments, use the form 
 PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis.

##### Site Considerations and Syntax

Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form 
 siteN/pinName, where 
 N is the site number. This node ignores pins that are not mapped to the digital pattern instrument.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### iol

Maximum current that the DUT sinks while outputting a voltage below V<sub>COM</sub>.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### ioh

Maximum current that the DUT sources while outputting a voltage above V<sub>COM</sub>.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### vcom

Commutating voltage level at which the active load circuit switches between sourcing current and sinking current.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Levels

<!--NI_TOPIC bundle=ni-digital-api-reference path=select-function.html language=enus -->
## TOPIC 00013: Select Function

- bundle_id: `ni-digital-api-reference`
- source_path: `select-function.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/select-function.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether digital pattern instrument channels are controlled by the PPMU, Digital, disconnected, or off. Changes take effect immediately. session in Instrument session obtained from the niDigital Initialize with Optionsnode. channel list List of channel names or list of pins. Do not pass a m

Select Function

Specifies whether digital pattern instrument channels are controlled by the PPMU, Digital, disconnected, or off. Changes take effect immediately.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

List of channel names or list of pins. Do not pass a mix of channel names and pin names.

An empty string denotes all digital pattern instrument channels.

Specify channel names using the form 
 PXI1Slot3/0,2-3 or 
 PXI1Slot3/0,PXI1Slot3/2-3, where 
 PXI1Slot3 is the instrument resource name and 
 0, 
 2, 
 3 are channel names.

To specify channels from multiple instruments, use the form 
 PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis.

##### Site Considerations and Syntax

Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form 
 siteN/pinName, where 
 N is the site number. This node ignores pins that are not mapped to the digital pattern instrument.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### function

Value that specifies whether to disconnect the pins, or use the PPMU or pin driver to control the pins.

| Digital | The pin is connected to the driver, comparator, and active load functions. The PPMU is not sourcing, but can make voltage measurements. The state of the digital pin driver when you change the selected function to Digital is determined by the most recent call to the niDigital Write Staticnode or the last vector of the most recently executed pattern burst, whichever happened last. Use the niDigital Write Staticnode to control the state of the digital pin driver through software. Use the niDigital Burst Patternnode to control the state of the digital pin driver through a pattern. Set the select digital function input of the niDigital Burst Patternnode to True to automatically switch the selected function of the pins in the pattern burst to Digital. |
| --- | --- |
| PPMU | The pin is connected to the PPMU. The driver, comparator, and active load are off while this function is selected. Call the niDigital PPMU Sourcenode to source a voltage or current. The niDigital PPMU Sourcenode automatically switches the selected function to the PPMU state and starts sourcing from the PPMU. Changing the selected function to Disconnect, Off, or Digital causes the PPMU to stop sourcing. If you change the selected function to PPMU using the niDigital Select Functionnode, the PPMU is initially not sourcing. Note You can make PPMU voltage measurements using the niDigital PPMU Measurenode from within any selected function. |
| Off | The pin is electrically connected, and the PPMU and digital pin driver are off while this function is selected. |
| Disconnect | The pin is electrically disconnected from instrument functions. Selecting this function causes the PPMU to stop sourcing prior to disconnecting the pin. Caution In the Disconnect state, some I/O protection and sensing circuitry remains exposed. Do not subject the instrument to voltage beyond its operating range. |
| NIDIGITAL_VAL_RIO | Yields control of the specified pin(s) to LabVIEW FPGA. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Alternate Ways to Select
 Function

By default, the niDigital Burst Patternnode automatically changes the function to Digital for
 the pins in the pattern. The niDigital PPMU Sourcenode always changes the function to PPMU for the pins
 in the channel list automatically.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-digital-api-reference path=self-calibrate.html language=enus -->
## TOPIC 00014: Self Calibrate

- bundle_id: `ni-digital-api-reference`
- source_path: `self-calibrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/self-calibrate.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs self-calibration on a digital pattern instrument. session in Instrument session obtained from the niDigital Initialize with Optionsnode. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior

Self Calibrate

Performs self-calibration on a digital pattern instrument.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-digital-api-reference path=self-test.html language=enus -->
## TOPIC 00015: Self Test

- bundle_id: `ni-digital-api-reference`
- source_path: `self-test.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/self-test.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns self test results from a digital pattern instrument. This test requires several minutes to execute. session in Instrument session obtained from the niDigital Initialize with Optionsnode. error in Error conditions that occur before this node runs. The node responds to this input according to

Self Test

Returns self test results from a digital pattern instrument. This test requires several minutes to execute.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### self test message

The returned self test status message.

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### self test result

A parameter that indicates if the self test passed (0) or failed (!=0).

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-digital-api-reference path=send-software-edge-trigger.html language=enus -->
## TOPIC 00016: Send Software Edge Trigger

- bundle_id: `ni-digital-api-reference`
- source_path: `send-software-edge-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/send-software-edge-trigger.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Forces a particular edge-based trigger to occur regardless of how the specified trigger is configured. You can use this node as a software override. session in Instrument session obtained from the niDigital Initialize with Optionsnode. trigger The trigger you want to override. Start trigger 2000 Ove

Send Software Edge Trigger

Forces a particular edge-based trigger to occur regardless of how the specified trigger is configured.

You can use this node as a software override.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### trigger

The trigger you want to override.

| Start trigger | 2000 | Overrides the Start trigger. You must specify an empty string in the trigger ID parameter. |
| --- | --- | --- |
| Conditional Jump trigger | 2001 | Specifies to route a conditional jump trigger. You must specify a conditional jump trigger in the trigger ID parameter. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### trigger ID

The instance of the specified trigger that you want to override.

| Null | Specifies an empty string. |
| --- | --- |
| conditionalJumpTrigger0 | Specifies conditional jump trigger 0. |
| conditionalJumpTrigger1 | Specifies conditional jump trigger 1. |
| conditionalJumpTrigger2 | Specifies conditional jump trigger 2. |
| conditionalJumpTrigger3 | Specifies conditional jump trigger 3. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-api-reference path=sequencer-flags-and-registers.html language=enus -->
## TOPIC 00017: Sequencer Flags and Registers

- bundle_id: `ni-digital-api-reference`
- source_path: `sequencer-flags-and-registers.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/sequencer-flags-and-registers.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Sequencer Flags and Registers nodes to create and configure sequencer flags and registers.

Sequencer Flags and Registers

Use the Sequencer Flags and Registers nodes to create and configure sequencer flags and registers.

Action

nodes

Write Sequencer Flag

Writes the state of a pattern sequencer flag.

Read Sequencer Flag

Reads the state of a pattern sequencer flag.

Write Sequencer Register

Writes a value to a pattern sequencer register.

Read Sequencer Register

Reads the value of a pattern sequencer register.

Parent topic:

Action

<!--NI_TOPIC bundle=ni-digital-api-reference path=sort-pin-results-by-site-i64.html language=enus -->
## TOPIC 00018: Sort Pin Results By Site (I64)

- bundle_id: `ni-digital-api-reference`
- source_path: `sort-pin-results-by-site-i64.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/sort-pin-results-by-site-i64.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Organizes data read from multiple digital pattern instruments by grouping the data by site number. To use this node, read data from each instrument using the same list of pins and pin groups for the channel list parameter, and combine the data in a two-dimensional array. Each instrument returns data

Sort Pin Results By Site (I64)

Organizes data read from multiple digital pattern instruments by grouping the data by site number.

To use this node, read data from each instrument using the same list of pins and pin groups for the channel list parameter, and combine the data in a two-dimensional array.

Each instrument returns data only for the pins that are mapped to its channels. Pass the data array and the same channel list as parameters to this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### sessions in

Instrument sessions obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

The specified channel list you use to read data in the results array. This node requires that the channel list contain only pin and pin group names.

Specify channel names using the form 
 PXI1Slot3/0,2-3 or 
 PXI1Slot3/0,PXI1Slot3/2-3, where 
 PXI1Slot3 is the instrument resource name and 
 0, 
 2, 
 3 are channel names.

To specify channels from multiple instruments, use the form 
 PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis.

[IMAGE alt='datatype_icon' src='/assets/img/c1di64.png']

##### results

The data read from the digital pattern instruments, combined into a two-dimensional array.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### read pin names

A Boolean that specifies whether the DUT pin names and system pin names are returned.

| True | The DUT pin names and system pin names are returned. |
| --- | --- |
| False | The DUT pin names and system pin names are not returned. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### DUT pin names

The returned list of DUT pin names and site numbers corresponding to the values in DUT pin results. Results for each site are returned in the order specified by the channel list.

[IMAGE alt='datatype_icon' src='/assets/img/ii64.png']

##### system pin results

The returned array containing data for the system pins in the channel list in the order you specify.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### system pin names

The system pin names corresponding to the values in system pin results.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### DUT pin results

An array containing data for the DUT pins in the channel list, grouped by site number and in the order you specify in the channel list.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### sessions out

Handle that identifies the sessions in all subsequent NI-Digital node calls.

Parent topic:

Sort Results

<!--NI_TOPIC bundle=ni-digital-api-reference path=source-and-capture-action.html language=enus -->
## TOPIC 00019: Source and Capture

- bundle_id: `ni-digital-api-reference`
- source_path: `source-and-capture-action.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/source-and-capture-action.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Source and Capture nodes to create, configure, write, and fetch source and capture waveforms with the NI-Digital Pattern Driver.

Source and Capture

Use the Source and Capture nodes to create, configure, write, and fetch source and capture waveforms with the NI-Digital Pattern Driver.

Action

nodes

Create Capture Waveform

Creates waveforms to acquire data during a pattern burst.

Create Source Waveform

Creates a source waveform.

Write Source Waveform

Writes a source waveform after a waveform is created.

Fetch Capture Waveform (U32)

Fetches a defined number of samples for a specific list of sites.

Parent topic:

Action

<!--NI_TOPIC bundle=ni-digital-api-reference path=static.html language=enus -->
## TOPIC 00020: Static

- bundle_id: `ni-digital-api-reference`
- source_path: `static.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/static.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Static nodes to program read and write static states for the pin driver.

Static

Use the Static nodes to program read and write static states for the pin driver.

Action

nodes

Write Static

node

Read Static

channel list

Parent topic:

Action

<!--NI_TOPIC bundle=ni-digital-api-reference path=tdr-node.html language=enus -->
## TOPIC 00021: TDR

- bundle_id: `ni-digital-api-reference`
- source_path: `tdr-node.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/tdr-node.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measures propagation delays through cables, connectors, and load boards using Time-Domain Reflectometry (TDR). Ensure that the channels and pins you select are connected to an open circuit. apply offsets A Boolean that specifies whether to apply the measured TDR offsets. True TDR offsets are applied

TDR

Measures propagation delays through cables, connectors, and load boards using Time-Domain Reflectometry (TDR).

Ensure that the channels and pins you select are connected to an open circuit.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### apply offsets

A Boolean that specifies whether to apply the measured TDR offsets.

| True | TDR offsets are applied. |
| --- | --- |
| False | TDR offsets are not applied. |

If you need to adjust the measured offsets prior to applying, set this input to False, and call the niDigital Apply TDR Offsetsnode to specify the adjusted TDR offsets values.

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

List of channel names or list of pins. Do not pass a mix of channel names and pin names.

An empty string denotes all digital pattern instrument channels.

Specify channel names using the form 
 PXI1Slot3/0,2-3 or 
 PXI1Slot3/0,PXI1Slot3/2-3, where 
 PXI1Slot3 is the instrument resource name and 
 0, 
 2, 
 3 are channel names.

To specify channels from multiple instruments, use the form 
 PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis.

##### Site Considerations and Syntax

Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form 
 siteN/pinName, where 
 N is the site number. This node ignores pins that are not mapped to the digital pattern instrument.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### offsets

Measured TDR offsets specified in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

TDR

<!--NI_TOPIC bundle=ni-digital-api-reference path=tdr.html language=enus -->
## TOPIC 00022: TDR

- bundle_id: `ni-digital-api-reference`
- source_path: `tdr.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/tdr.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these nodes to measure pin propagation delay using Time-Domain Reflectometry (TDR) and to apply delay values to the pins of a digital pattern instrument.

TDR

Use these nodes to measure pin propagation delay using Time-Domain Reflectometry (TDR) and to apply delay values to the pins of a digital pattern instrument.

Configuration

nodes

TDR

Measures propagation delays through cables, connectors, and load boards using Time-Domain Reflectometry (TDR).

Apply TDR Offsets

Applies the correction for propagation delay offsets to a digital pattern instrument.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-digital-api-reference path=wait-until-done.html language=enus -->
## TOPIC 00023: Wait Until Done

- bundle_id: `ni-digital-api-reference`
- source_path: `wait-until-done.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/wait-until-done.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the pattern burst has completed or the timeout has expired. session in Instrument session obtained from the niDigital Initialize with Optionsnode. timeout Maximum time (in seconds) allowed for this node to complete. If this node does not complete within this time interval, this node retu

Wait Until Done

Waits until the pattern burst has completed or the timeout has expired.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Maximum time (in seconds) allowed for this node to complete.

If this node does not complete within this time interval, this node returns an error.

Default value: 10 s

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-api-reference path=write-sequencer-flag-synchronized.html language=enus -->
## TOPIC 00024: Write Sequencer Flag (Synchronized)

- bundle_id: `ni-digital-api-reference`
- source_path: `write-sequencer-flag-synchronized.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/write-sequencer-flag-synchronized.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a Boolean value to the pattern sequencer flag for synchronized digital pattern instruments. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime program. sessions in Instrument sessions obtained from the niDigital Initialize with Options node. error

Write Sequencer Flag (Synchronized)

Writes a Boolean value to the pattern sequencer flag for synchronized digital pattern instruments.

Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime program.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### sessions in

Instrument sessions obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### sequencer flag

The pattern sequencer flag to write.

| seqflag0 | Writes pattern sequencer flag 0. |
| --- | --- |
| seqflag1 | Writes pattern sequencer flag 1. |
| seqflag2 | Writes pattern sequencer flag 2. |
| seqflag3 | Writes pattern sequencer flag 3. |

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### state

A Boolean that assigns a state to the pattern sequencer flag you specify.

| True | Assigns True to the pattern sequencer flag you specify. |
| --- | --- |
| False | Assigns False to the pattern sequencer flag you specify. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### sessions out

Handle that identifies the sessions in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Multi-Instrument Synchronization

<!--NI_TOPIC bundle=ni-digital-api-reference path=write-sequencer-flag.html language=enus -->
## TOPIC 00025: Write Sequencer Flag

- bundle_id: `ni-digital-api-reference`
- source_path: `write-sequencer-flag.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/write-sequencer-flag.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program. session in Instrument session obtained from the niDigital Initialize with Optionsnode. error in Error conditions that occur before this node run

Write Sequencer Flag

Writes the state of a pattern sequencer flag.

Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### sequencer flag

The pattern sequencer flag to write.

| seqflag0 | Writes pattern sequencer flag 0. |
| --- | --- |
| seqflag1 | Writes pattern sequencer flag 1. |
| seqflag2 | Writes pattern sequencer flag 2. |
| seqflag3 | Writes pattern sequencer flag 3. |

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### state

A Boolean that assigns a state to the pattern sequencer flag you specify.

| True | Assigns True to the pattern sequencer flag you specify. |
| --- | --- |
| False | Assigns False to the pattern sequencer flag you specify. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Sequencer Flags and Registers

<!--NI_TOPIC bundle=ni-digital-api-reference path=write-sequencer-register.html language=enus -->
## TOPIC 00026: Write Sequencer Register

- bundle_id: `ni-digital-api-reference`
- source_path: `write-sequencer-register.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/write-sequencer-register.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a value to a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program. session in Instrument session obtained from the niDigital Initialize with Optionsnode. sequencer register The sequencer register you want t

Write Sequencer Register

Writes a value to a pattern sequencer register.

Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### sequencer register

The sequencer register you want to write to.

| reg0 | Reads sequencer register 0. |
| --- | --- |
| reg1 | Reads sequencer register 1. |
| reg2 | Reads sequencer register 2. |
| reg3 | Reads sequencer register 3. |
| reg4 | Reads sequencer register 4. |
| reg5 | Reads sequencer register 5. |
| reg6 | Reads sequencer register 6. |
| reg7 | Reads sequencer register 7. |
| reg8 | Reads sequencer register 8. |
| reg9 | Reads sequencer register 9. |
| reg10 | Reads sequencer register 10. |
| reg11 | Reads sequencer register 11. |
| reg12 | Reads sequencer register 12. |
| reg13 | Reads sequencer register 13. |
| reg14 | Reads sequencer register 14. |
| reg15 | Reads sequencer register 15. |

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### value

The value you want to write to the register.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Sequencer Flags and Registers

<!--NI_TOPIC bundle=ni-digital-api-reference path=write-source-waveform-broadcast.html language=enus -->
## TOPIC 00027: Write Source Waveform (Broadcast U32)

- bundle_id: `ni-digital-api-reference`
- source_path: `write-source-waveform-broadcast.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/write-source-waveform-broadcast.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the same waveform data to all sites. Use this instance of the niDigital Write Source Waveform node if you set the data mapping parameter of the niDigital Create Source Waveform node to Broadcast. waveform name The name to assign to the waveform. Use the waveform name with source_start opcode

Write Source Waveform (Broadcast U32)

Writes the same waveform data to all sites.

Use this instance of the niDigital Write Source Waveformnode if you set the data mapping parameter of the niDigital Create Source Waveformnode to 
 Broadcast.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### waveform name

The name to assign to the waveform.

Use the waveform name with source_start opcode in your pattern.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### waveform data

1D array of samples to use as source data to apply to all sites.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Write Source Waveform

<!--NI_TOPIC bundle=ni-digital-api-reference path=write-source-waveform-siteunique.html language=enus -->
## TOPIC 00028: Write Source Waveform (Site Unique U32)

- bundle_id: `ni-digital-api-reference`
- source_path: `write-source-waveform-siteunique.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/write-source-waveform-siteunique.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one waveform per site. Use this instance of the niDigital Write Source Waveform node if you set the parameter of the niDigital Create Source Waveform node to Site Unique. waveform name The name to assign to the waveform. Use the waveform name with source_start opcode in your pattern. session

Write Source Waveform (Site Unique U32)

Writes one waveform per site.

Use this instance of the niDigital Write Source Waveformnode if you set the parameter of the niDigital Create Source Waveformnode to 
 Site Unique.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### waveform name

The name to assign to the waveform.

Use the waveform name with source_start opcode in your pattern.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### site list

Site numbers listed as a comma-delimited list of strings of form 
siteN, where 
N is the site number.

If you enter an empty string, the node fetches data from all sites.

[IMAGE alt='datatype_icon' src='/assets/img/c1du32.png']

##### waveform data

An array of samples to use as source data.
 Each row in the 2D array corresponds to each site in the site list parameter.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Write Source Waveform

<!--NI_TOPIC bundle=ni-digital-api-reference path=write-source-waveform-tdms.html language=enus -->
## TOPIC 00029: Write Source Waveform Data from File (TDMS)

- bundle_id: `ni-digital-api-reference`
- source_path: `write-source-waveform-tdms.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/write-source-waveform-tdms.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a source waveform based on the waveform data and configuration information the file contains. waveform name The name to assign to the waveform. Use the waveform name with source_start opcode in your pattern. session in Instrument session obtained from the niDigital Initialize with Optionsnode

Write Source Waveform Data from File (TDMS)

Writes a source waveform based on the waveform data and configuration information the file contains.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### waveform name

The name to assign to the waveform.

Use the waveform name with source_start opcode in your pattern.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### waveform file

Absolute file path to the load source waveform file (.tdms).

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Write Source Waveform

<!--NI_TOPIC bundle=ni-digital-api-reference path=write-static.html language=enus -->
## TOPIC 00030: Write Static

- bundle_id: `ni-digital-api-reference`
- source_path: `write-static.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-api-reference/raw/resource/enus/write-static.html
- document_id: `ni-digital-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a static state to the specified pins. The selected pins remain in the specified state until the next pattern burst or call to this node. If there are uncommitted changes to levels or the termination mode, this node commits the changes to the pins. This node does not change the selected pin fu

Write Static

Writes a static state to the specified pins. The selected pins remain in the specified state until the next pattern burst or call to this node.

If there are uncommitted changes to levels or the termination mode, this node commits the changes to the pins.

This node does not change the selected pin function. If you write a static state to a pin that does not have the Digital function selected, the new static state is stored by the instrument, and affects the state of the pin the next time you change the selected function to Digital.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the niDigital Initialize with Optionsnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

List of channel names or list of pins. Do not pass a mix of channel names and pin names.

An empty string denotes all digital pattern instrument channels.

Specify channel names using the form 
 PXI1Slot3/0,2-3 or 
 PXI1Slot3/0,PXI1Slot3/2-3, where 
 PXI1Slot3 is the instrument resource name and 
 0, 
 2, 
 3 are channel names.

To specify channels from multiple instruments, use the form 
 PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis.

##### Site Considerations and Syntax

Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form 
 siteN/pinName, where 
 N is the site number. This node ignores pins that are not mapped to the digital pattern instrument.

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### state

Parameter that specifies one of the following digital states to assign to the pin.

| 0 | Specifies to drive low. |
| --- | --- |
| 1 | Specifies to drive high. |
| X | Specifies to not drive. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent NI-Digital node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Static
