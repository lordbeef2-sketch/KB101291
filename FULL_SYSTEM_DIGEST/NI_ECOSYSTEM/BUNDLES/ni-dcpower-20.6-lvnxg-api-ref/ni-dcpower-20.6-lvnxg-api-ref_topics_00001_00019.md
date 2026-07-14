# NI DOCUMENT BUNDLE: ni-dcpower-20.6-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-dcpower-20.6-lvnxg-api-ref start=1 end=19 -->
<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=abort-with-channels.html language=enus -->
## TOPIC 00001: Abort With Channels

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `abort-with-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/abort-with-channels.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transitions the specified channels from the Running state to the Uncommitted state. If a sequence is running, calling this node stops the sequence. session in Instrument session obtained from the Initialize With Independent Channels node. error in Error conditions that occur before this node runs. W

Abort With Channels

Transitions the specified channels from the Running state to the Uncommitted state.

If a sequence is running, calling this node stops the sequence.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize With Independent
 Channels node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

With the following exception, the node responds to this input according to standard error behavior. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Channel(s) to use.

If you do not wire this parameter, by default all channels in the session
 are used.

##### Channel Name Syntax

Specify the channel(s) using the form
 PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or
 PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where
 PXI1Slot3 and PXI1Slot4 are
 instrument resource names and 0, 2, and 3 are channels.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Disabling Power Output

Use the Configure Output Enabled node or the Reset With
 Channels node to disable power output on a per-channel basis.

#### Sequence of NI-DCPower Nodes

Any configuration nodes called after Abort With Channels are not
 applied until the Initiate With Channels node is called. If power
 output is enabled when you call this node, the output channels remain in their current
 state and continue providing power.

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=adjust-current-limit-calibration.html language=enus -->
## TOPIC 00002: Adjust Current Limit Calibration

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `adjust-current-limit-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/adjust-current-limit-calibration.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates calibration constants for the current limit for the specified output channel and range by comparing requested and measured outputs. This node can only be called from an external calibration session. session in Instrument calibration session obtained from the Initialize External Calibratio

Adjust Current Limit Calibration

Calculates calibration constants for the current limit for the specified output channel and range by comparing requested and measured outputs.

This node can only be called from an external calibration session.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument calibration session obtained from the Initialize External Calibration node.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Output channel to which these calibration settings apply.

Only one channel at a time can be calibrated.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### number of measurements

Number of elements in requested outputs and measured outputs.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### range

Range to calibrate with these settings.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### requested outputs

Array of the output values requested in the Configure Current Limit node.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### measured outputs

Array of the output values measured by an external precision digital multimeter (DMM).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node does not support the following hardware:

- PXIe-4140/4141/4142/4143/4144/4145

#### Calibration Procedure

Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this node.

Parent topic:

External Calibration Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=adjust-current-measurement-calibration.html language=enus -->
## TOPIC 00003: Adjust Current Measurement Calibration

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `adjust-current-measurement-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/adjust-current-measurement-calibration.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates calibration coefficients for the specified current measurement range by comparing reported and measured outputs. This node can only be called in an external calibration session. session in Instrument calibration session obtained from the Initialize External Calibration node. channel name

Adjust Current Measurement Calibration

Calculates calibration coefficients for the specified current measurement range by comparing reported and measured outputs.

This node can only be called in an external calibration session.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument calibration session obtained from the Initialize External Calibration node.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Output channel to which these calibration settings apply.

Only one channel at a time can be calibrated.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### number of measurements

Number of elements in requested outputs and measured outputs.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### range

Range to calibrate with these settings.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### reported outputs

Array of the output values that were returned by the Measure node.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### measured outputs

Array of the output values measured by an external precision digital multimeter (DMM).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node does not support the following hardware:

- PXIe-4135/4136/4137/4138/4139
- PXIe-4147
- PXIe-4162/4163

#### Calibration Procedure

Parent topic:

External Calibration Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=adjust-internal-reference-calibration.html language=enus -->
## TOPIC 00004: Adjust Internal Reference Calibration

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `adjust-internal-reference-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/adjust-internal-reference-calibration.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Programs the adjusted reference value to the device. This node can only be called from an external calibration session. session in Instrument calibration session obtained from the Initialize External Calibration node. error in Error conditions that occur before this node runs. The node responds to t

Adjust Internal Reference Calibration

Programs the adjusted reference value to the device.

This node can only be called from an external calibration session.

[IMAGE alt='1378' src='Adjust_Internal_Reference_Calibration.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument calibration session obtained from the Initialize External Calibration node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### internal reference

Value that specifies the internal reference to be adjusted.

| 5K Reference | 1054 | Calibration pin connected to 5 V internal reference. |
| --- | --- | --- |
| 100kOhm Reference | 1055 | Calibration pin connected to 100 kΩ internal reference. |

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### adjusted internal reference value

Updated value of the internal reference that will be programmed to the device.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-4162/4163

#### Calibration Procedure

Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this node.

Parent topic:

External Calibration Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=adjust-output-resistance-calibration.html language=enus -->
## TOPIC 00005: Adjust Output Resistance Calibration

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `adjust-output-resistance-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/adjust-output-resistance-calibration.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates the calibration constants for the output resistance of the specified channel by comparing requested and measured outputs. This node can only be called from an external calibration session. session in Instrument calibration session obtained from the Initialize External Calibration node. ch

Adjust Output Resistance Calibration

Calculates the calibration constants for the output resistance of the specified channel by comparing requested and measured outputs.

This node can only be called from an external calibration session.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument calibration session obtained from the Initialize External Calibration node.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Output channel to which these calibration settings apply.

Only one channel at a time can be calibrated.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### number of measurements

Number of elements in requested outputs and measured outputs.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### requested outputs

Array of the output values requested in the Configure Current Limit node.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### measured outputs

Array of the output values measured by an external precision digital multimeter (DMM).

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-4154

#### Calibration Procedure

Parent topic:

External Calibration Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=adjust-residual-current-offset-calibration.html language=enus -->
## TOPIC 00006: Adjust Residual Current Offset Calibration

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `adjust-residual-current-offset-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/adjust-residual-current-offset-calibration.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates the calibration constants for the residual current offsets for the specified output channel. This node can be called only in an external calibration session. The node requires that the output be open prior to it being invoked. session in Instrument calibration session obtained from the In

Adjust Residual Current Offset Calibration

Calculates the calibration constants for the residual current offsets for the specified output channel.

This node can be called only in an external calibration session. The node requires that the output be open prior to it being invoked.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument calibration session obtained from the Initialize External Calibration node.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Output channel to which these calibration settings apply.

Only one channel at a time can be calibrated.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node does not support the following hardware:

- PXI-4110
- PXIe-4112/4113
- PXI-4130
- PXI-4132
- PXIe-4154

#### Residual Current Offsets

#### Calibration Procedure

Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this node.

Parent topic:

External Calibration Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=clear-interchange-warnings.html language=enus -->
## TOPIC 00007: Clear Interchange Warnings

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `clear-interchange-warnings.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/clear-interchange-warnings.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the list of current interchange warnings. session in Instrument session obtained from the Initialize With Independent Channels node. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Defaul

Clear Interchange Warnings

Clears the list of current interchange warnings.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize With Independent
 Channels node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

IVI Utilities Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=close-external-calibration.html language=enus -->
## TOPIC 00008: Close External Calibration

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `close-external-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/close-external-calibration.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the specified calibration session and deallocates the resources that NI-DCPower reserved for calibration. session in Instrument calibration session obtained from the Initialize External Calibration node. calibration close action Action specified for the calibration values from the session as

Close External Calibration

Closes the specified calibration session and deallocates the resources that NI-DCPower reserved for calibration.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument calibration session obtained from the Initialize External Calibration node.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### calibration close action

Action specified for the calibration values from the session as it is closed.

| Cancel | 1001 | The old calibration constants are kept, and the new ones are discarded. |
| --- | --- | --- |
| Commit | 1002 | The new calibration constants are stored in the EEPROM. |

Default value: Cancel (1001)

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

#### Calibration Procedure

Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this node.

Parent topic:

External Calibration Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=close.html language=enus -->
## TOPIC 00009: Close

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `close.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/close.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the specified session and deallocates the resources that NI-DCPower reserved. session in Instrument session obtained from the Initialize With Independent Channels node. error in Error conditions that occur before this node runs. With the following exception, the node responds to this input ac

Close

Closes the specified session and deallocates the resources that NI-DCPower reserved.

[IMAGE alt='1378' src='Close.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize With Independent
 Channels node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

With the following exception, the node responds to this input according to standard error behavior. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Power output

If power output is enabled when you call this node, the output channels remain in their existing state and continue providing power. Use the Configure Output Enabled node to disable power output on a per channel basis. Use the Reset node to disable power on all output channels.

Parent topic:

NI-DCPower Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=commit-with-channels.html language=enus -->
## TOPIC 00010: Commit With Channels

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `commit-with-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/commit-with-channels.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies previously configured settings to the specified channels and moves the channels from the Uncommitted state into the Committed state. session in Instrument session obtained from the Initialize With Independent Channels node. error in Error conditions that occur before this node runs. The node

Commit With Channels

Applies previously configured settings to the specified channels and moves the channels
 from the Uncommitted state into the Committed state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize With Independent
 Channels node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Channel(s) to use.

If you do not wire this parameter, by default all channels in the session
 are used.

##### Channel Name Syntax

Specify the channel(s) using the form
 PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or
 PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where
 PXI1Slot3 and PXI1Slot4 are
 instrument resource names and 0, 2, and 3 are channels.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

After calling this node, modifying any property reverts the channels to
 the Uncommitted state. Use the Initiate With Channels node to
 transition to the Running state.

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=query-maximum-voltage-level.html language=enus -->
## TOPIC 00011: Query Maximum Voltage Level

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `query-maximum-voltage-level.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/query-maximum-voltage-level.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the maximum voltage level on an output channel if the output channel is set to the specified current limit. session in Instrument session obtained from the Initialize With Independent Channels node. channel name Output channel to query. The maximum voltage level can be queried for only one c

Query Maximum Voltage Level

Queries the maximum voltage level on an output channel if the output channel is set to the specified current limit.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize With Independent
 Channels node.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Output channel to query.

The maximum voltage level can be queried for only one channel at a time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### current limit

Current limit to use when calculating the max voltage level.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### maximum voltage level

Maximum voltage level that can be set on an output channel with the specified current limit.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configuration Information Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=reset-node.html language=enus -->
## TOPIC 00012: Reset

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `reset-node.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/reset-node.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the device to a known state.

Reset

Resets the device to a known state.

Utility Nodes

Use the NI-DCPower Utility nodes for miscellaneous functionality.

Reset

Resets the device to a known state.

Reset Device

Resets the device to a known state and performs a hard reset on the device and driver software.

Reset with Defaults

Resets the device to a known state and assigns user-defined default values for configurable properties from the IVI configuration.

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=reset-with-defaults.html language=enus -->
## TOPIC 00013: Reset with Defaults

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `reset-with-defaults.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/reset-with-defaults.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the device to a known state and assigns user-defined default values for configurable properties from the IVI configuration. This node disables power generation, resets session properties to their default values, commits the session properties, and leaves the session in the Running state. In a

Reset with Defaults

Resets the device to a known state and assigns user-defined default values for configurable properties from the IVI configuration.

This node disables power generation, resets session properties to their default values, commits the session properties, and leaves the session in the Running state. In addition to exhibiting the behavior of Reset, Reset with Defaults can assign user-defined default values for configurable properties from the IVI configuration.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize With Independent
 Channels node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

With the following exception, the node responds to this input according to standard error behavior. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Reset

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=revision-query.html language=enus -->
## TOPIC 00014: Revision Query

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `revision-query.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/revision-query.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision information of NI-DCPower and the device firmware. session in Instrument session obtained from the Initialize With Independent Channels node. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standar

Revision Query

Returns the revision information of NI-DCPower and the device firmware.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize With Independent
 Channels node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### firmware revision

Information about the firmware revision for the device.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### instr driver revision

Information about the instrument driver revision for NI-DCPower.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=self-calibrate.html language=enus -->
## TOPIC 00015: Self Calibrate

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `self-calibrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/self-calibrate.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a self-calibration upon the specified channel(s). This node disables the output, performs several internal calculations, and updates calibration values. This node calls the Reset With Channels node, which puts the device configuration into the default state. session in Instrument session ob

Self Calibrate

Performs a self-calibration upon the specified channel(s).

This node disables the output, performs several internal calculations, and updates calibration
 values. This node calls the Reset With Channels node, which puts the
 device configuration into the default state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize With Independent
 Channels node.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Output channel(s) to which to apply this configuration value.

If you do not wire this parameter, by default all channels in the
 session are used.

##### Channel Name Syntax

Specify the channel(s) using the form
 PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or
 PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where
 PXI1Slot3 and PXI1Slot4 are
 instrument resource names and 0, 2, and 3 are channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node does not support the following hardware:

- PXI-4110
- PXIe-4112/4113
- PXI-4130
- PXIe-4154

#### Writing Updated Calibration Values to Hardware

Self Calibration Persistence

Write to EEPROM

#### Self-Calibrate All Channels for Certain
 Devices

For the PXIe-4147, PXIe-4162, and PXIe-4163, you
 must specify all channels of the device with the channel name
 input. You cannot self-calibrate a subset of channels for these devices.

Parent topic:

Calibration Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=self-test.html language=enus -->
## TOPIC 00016: Self Test

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `self-test.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/self-test.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the device self-test routine and returns the test result(s). Calling this node implicitly calls the Reset With Channels node. session in Instrument session obtained from the Initialize With Independent Channels node. error in Error conditions that occur before this node runs. The node respo

Self Test

Performs the device self-test routine and returns the test result(s).

Calling this node implicitly calls the Reset With Channels node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize With Independent
 Channels node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### self test result

Value result from the device self test.

A value of 0 indicates success. Other values indicate the error code
 corresponding to the self test result message.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### self test message

Result message for self test.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Self
 Test All Channels for Certain Devices

For the PXIe-4162 and PXIe-4163, you
 must specify all channels of the device with the resource name
 input of the Initialize With Independent Channels node. You cannot
 self test a subset of channels for these devices.

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=send-software-edge-trigger-with-channels.html language=enus -->
## TOPIC 00017: Send Software Edge Trigger With Channels

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `send-software-edge-trigger-with-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/send-software-edge-trigger-with-channels.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asserts the specified trigger. This node can override an external edge trigger. session in Instrument session obtained from the Initialize With Independent Channels node. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior.

Send Software Edge Trigger With
 Channels

Asserts the specified trigger.

This node can override an external edge trigger.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize With Independent
 Channels node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Channel(s) to use.

If you do not wire this parameter, by default all channels in the session
 are used.

##### Channel Name Syntax

Specify the channel(s) using the form
 PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or
 PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where
 PXI1Slot3 and PXI1Slot4 are
 instrument resource names and 0, 2, and 3 are channels.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### signal

Trigger to override.

| Start Trigger | 1034 | Overrides the Start trigger. |
| --- | --- | --- |
| Source Trigger | 1035 | Overrides the Source trigger. |
| Measure Trigger | 1036 | Overrides the Measure trigger. |
| Sequence Advance Trigger | 1037 | Overrides the Sequence Advance trigger. |
| Pulse Trigger | 1053 | Overrides the Pulse trigger. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node does not support the following hardware:

- PXI-4110
- PXI-4130

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=sequence-nodes.html language=enus -->
## TOPIC 00018: Sequence Nodes

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `sequence-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/sequence-nodes.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower Sequence and Advanced Sequence nodes for configuring the SMU with a series of property or attribute values. You must set the source mode to Sequence.

Sequence Nodes

Use the NI-DCPower Sequence and Advanced Sequence nodes for configuring the SMU with a series of property or attribute values. You must set the source mode to Sequence.

Configuration Nodes

Use the NI-DCPower Configuration nodes to configure the power supply or source measure unit.

Create Advanced Sequence Step With Channels

Creates a new step for an advanced sequence.

Create Advanced Sequence With Channels

Creates an empty advanced sequence.

Delete Advanced Sequence

Deletes a previously created advanced sequence and all the advanced sequence steps in it.

Set Sequence

Configures a series of voltage or current outputs and corresponding source delays.

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-dcpower-20.6-lvnxg-api-ref path=wait-for-event-with-channels.html language=enus -->
## TOPIC 00019: Wait For Event With Channels

- bundle_id: `ni-dcpower-20.6-lvnxg-api-ref`
- source_path: `wait-for-event-with-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-20.6-lvnxg-api-ref/raw/resource/enus/wait-for-event-with-channels.html
- document_id: `ni-dcpower-20.6-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the specified channels have generated the specified event. The session monitors whether each type of event has occurred at least once for the specified channels since the last time this node or the Initiate With Channels node were called. If an event has only been generated once and you

Wait For Event With Channels

Waits until the specified channels have generated the specified event.

The session monitors whether each type of event has occurred at least once for the specified
 channels since the last time this node or the Initiate With Channels node
 were called. If an event has only been generated once and you call this node successively, the
 node times out. Individual events must be generated between separate calls of this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize With Independent
 Channels node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Channel(s) to use.

If you do not wire this parameter, by default all channels in the session
 are used.

##### Channel Name Syntax

Specify the channel(s) using the form
 PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or
 PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where
 PXI1Slot3 and PXI1Slot4 are
 instrument resource names and 0, 2, and 3 are channels.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### event

Event to wait for.

| Source Complete Event | 1030 | Waits for the Source Complete event. |
| --- | --- | --- |
| Measure Complete Event | 1031 | Waits for the Measure Complete event. |
| Sequence Iteration Complete Event | 1032 | Waits for the Sequence Iteration Complete event. |
| Sequence Engine Done Event | 1033 | Waits for the Sequence Engine Done event. |
| Pulse Complete Event | 1051 | Waits for the Pulse Complete event. |
| Ready for Pulse Trigger Event | 1052 | Waits for the Ready for Pulse Trigger event. |

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout (s)

Maximum time allowed for this node to complete, in seconds.

If the node does not complete within this time interval, NI-DCPower returns an error.

Note

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle used to identify the session in all subsequent NI-DCPower node calls.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node provides limited support for the following devices:

- PXI-4110 (Source Complete event only)
- PXI-4130 (Source Complete event only)

#### Programming Patterns

This node should only be called when the specified channels are in the
 Running state.

Parent topic:

Action Nodes
