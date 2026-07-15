# NI DOCUMENT BUNDLE: ni-hsdio-19.5-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-hsdio-19.5-lvnxg-api-ref start=1 end=46 -->
<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=adjust-calibration-dbl.html language=enus -->
## TOPIC 00001: Adjust Calibration (DBL)

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `adjust-calibration-dbl.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/adjust-calibration-dbl.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs internal calculations on a single floating point value and saves the resulting values until the end of the External Calibration session. These values will be stored on the device when Close External Calibration is executed with the action configured to Commit, or discarded if the action is

Adjust Calibration (DBL)

Performs internal calculations on a single floating point value and saves the resulting values until the end of the External Calibration session.

These values will be stored on the device when Close External Calibration is executed with the action configured to 
 Commit, or discarded if the action is configured as Cancel.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel

The channel to adjust.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument handle that identifies your calibration session.

This parameter is obtained from the niHSDIO Initialize External Calibrationnode

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### value

The floating point value used to perform internal calculations.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### calibration type

The section of the external calibration procedure you are trying to execute.

Refer to the calibration procedure document for your device for the correct value to use.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### calibration reference

Parameter that specifies which internal routing path to configure based on the calibration type.

Refer to the calibration procedure document for your device for the correct value to use.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Session handle that passes a reference to your calibration session to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=calibration-utility.html language=enus -->
## TOPIC 00002: Calibration Utility

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `calibration-utility.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/calibration-utility.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Calibration Utility nodes to access calibration utility operations.

Calibration Utility

Use the Calibration Utility nodes to access calibration utility operations.

Calibration

nodes

Change External Calibration Password

Changes the password that is required to initialize an external calibration session. The password may be up to four characters long.

Get Calibration User Defined Info

Returns the user-defined information in the device onboard EEPROM.

Set Calibration User Defined Info

Stores a user-defined string of characters in the device onboard EEPROM.

Get Calibration User Defined Info Maximum Size

Returns the maximum number of characters that can be used to store user-defined information in the device onboard EEPROM.

Get Last External Calibration Date And Time

Returns the date and time of the most recent successful external calibration.

Get Last External Calibration Temperature

Returns the onboard temperature of the device in degrees Celsius during the last successful external calibration.

Get Device Temperature

Returns the current onboard temperature of the device in degrees Celsius.

Get Last Self Calibration Date And Time

Returns the date and time of the most recent successful self-calibration.

Get Last Self Calibration Temperature

Returns the onboard temperature of the device in degrees Celsius during the last successful self-calibration.

Get External Calibration Recommended Interval

Returns the recommended number of months between external calibrations.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=calibration.html language=enus -->
## TOPIC 00003: Calibration

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/calibration.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Calibration nodes to access calibration operations.

Calibration

Use the Calibration nodes to access calibration operations.

NI-HSDIO Nodes

nodes

Self Calibrate

Self calibrates the device.

External Calibration

nodes

Calibration Utility

nodes

Parent topic:

NI-HSDIO Nodes

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=clear-calibration-state.html language=enus -->
## TOPIC 00004: Clear Calibration State

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `clear-calibration-state.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/clear-calibration-state.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Restores the internal routing of the device to the default, unconfigured state. session in Instrument handle that identifies your calibration session. This parameter is obtained from the niHSDIO Initialize External Calibrationnode error in Error conditions that occur before this node runs. The node

Clear Calibration State

Restores the internal routing of the device to the default, unconfigured state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument handle that identifies your calibration session.

This parameter is obtained from the niHSDIO Initialize External Calibrationnode

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Session handle that passes a reference to your calibration session to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=close-child-calibration-session.html language=enus -->
## TOPIC 00005: Close Child Calibration Session

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `close-child-calibration-session.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/close-child-calibration-session.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the child session of the open external calibration session, similar to Closenode. If any open child sessions have not been closed when the Close External Calibrationnode is called, they are closed implicitly. session in Instrument handle that identifies your calibration session. This paramete

Close Child Calibration Session

Closes the child session of the open external calibration session, similar to Closenode.

If any open child sessions have not been closed when the Close External Calibrationnode is called, they are closed implicitly.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument handle that identifies your calibration session.

This parameter is obtained from the niHSDIO Initialize External Calibrationnode

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### child session in

The niHSDIO acquisition or generation session that is created by the calibration session for the purpose of measurement.

You can create one acquisition and/or one generation session at a time within the calibration session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Session handle that passes a reference to your calibration session to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=close-external-calibration.html language=enus -->
## TOPIC 00006: Close External Calibration

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `close-external-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/close-external-calibration.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an NI-HSDIO external calibration session and, if specified, stores the new calibration constants and calibration data in the onboard EEPROM. Whether you commit or cancel, the device is reset and the FPGA is reloaded afterwards. session in Instrument handle that identifies your calibration ses

Close External Calibration

Closes an NI-HSDIO external calibration session and, if specified, stores the new calibration constants and calibration data in the onboard EEPROM.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument handle that identifies your calibration session.

This parameter is obtained from the niHSDIO Initialize External Calibrationnode

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### calibration action

The action to perform at closing.

| Commit | 62 | The new calibration constants and data determined during the external calibration session are stored in the onboard EEPROM, given that the calibration was complete and passed successfully. |
| --- | --- | --- |
| Cancel | 63 | No changes are made to the calibration constants and data in the EEPROM. |

Default value: Commit

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

External Calibration

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=config-multi-pattern-match-ref-trig.html language=enus -->
## TOPIC 00007: Configure Multi-Sample Pattern Match Reference Trigger

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `config-multi-pattern-match-ref-trig.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/config-multi-pattern-match-ref-trig.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference trigger for multi-sample pattern match triggering. You can configure up to 32 channels with patterns of up to 10 samples per channel with this node. For the channels specified in the channel list parameter, the pattern must match each pattern element specified in the pattern

Configure Multi-Sample Pattern Match Reference Trigger

Configures the Reference trigger for multi-sample pattern match triggering.

You can configure up to 32 channels with patterns of up to 10 samples per channel with this node. For the channels specified in the channel list parameter, the pattern must match each pattern element specified in the pattern array parameter on consecutive clock cycles. After the last pattern element in the pattern array parameter is matched, the Reference trigger is asserted.

This node is valid only for acquisition sessions.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

The channels that are configured for pattern matching using the 
pattern array value.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### pattern array

The binary multi-sample pattern that activates the pattern match trigger. The first element in the array corresponds to the first pattern acquired.

This array of strings creates a mask for the multi-sample pattern. Each string is composed of the following characters:

- X or 
 x : Ignore the channel
- 1 : Match on a logic 1
- 0 : Match on a logic 0
- R or 
 r : Match on a rising edge
- F or 
 f : Match on a falling edge
- E or 
 e : Match on either edge

Note

R

F

E

The first character in the expression corresponds to the first channel in 
 channel list. The number of characters in pattern must correspond to the number of channels specified in 
 channel list or an error is returned.

For example, the following two examples are valid and achieve the same results:

- channel list = 
 19-0 and pattern array = 
 0000 0XXX XX11 1111 1111
- channel list = 
 0-19 and pattern array = 
 1111 1111 11XX XXX0 0000

The following example searches for ten consecutive samples on channel 0:

| Sample 0 | x |
| --- | --- |
| Sample 1 | 1 |
| Sample ... | ... |
| Sample 8 | 0 |
| Sample 9 | 1 |

The following example searches for ten consecutive samples on channels 0 to 19:

| Sample 0 | 0000 0000 0000 0000 0000 |
| --- | --- |
| Sample 1 | 1111 1111 1111 1111 0000 |
| Sample ... | ... |
| Sample 8 | 0000 1111 1111 1111 1111 |
| Sample 9 | 1111 1111 11XX XXX0 0000 |

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### pretrigger samples

The number of pretrigger samples the device must receive before the Reference trigger is acknowledged.

Default value: 500

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=config-multi-pattern-match-start-trig.html language=enus -->
## TOPIC 00008: Configure Multi-Sample Pattern Match Start Trigger

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `config-multi-pattern-match-start-trig.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/config-multi-pattern-match-start-trig.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start trigger for multi-sample pattern match triggering. You can configure up to 32 channels with patterns of up to 10 samples per channel with this node. For the channels specified in the channel list parameter, the pattern must match each pattern element specified in the pattern arr

Configure Multi-Sample Pattern Match Start Trigger

Configures the Start trigger for multi-sample pattern match triggering.

You can configure up to 32 channels with patterns of up to 10 samples per channel with this node. For the channels specified in the channel list parameter, the pattern must match each pattern element specified in the pattern array parameter on consecutive clock cycles. After the last pattern element in the pattern array parameter is matched, the Start trigger is asserted.

This node is valid only for acquisition sessions.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

The channels that are configured for pattern matching using the 
pattern array value.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### pattern array

The binary multi-sample pattern that activates the pattern match trigger. The first element in the array corresponds to the first pattern acquired.

This array of strings creates a mask for the multi-sample pattern. Each string is composed of the following characters:

- X or 
 x : Ignore the channel
- 1 : Match on a logic 1
- 0 : Match on a logic 0
- R or 
 r : Match on a rising edge
- F or 
 f : Match on a falling edge
- E or 
 e : Match on either edge

Note

R

F

E

The first character in the expression corresponds to the first channel in 
 channel list. The number of characters in pattern must correspond to the number of channels specified in 
 channel list or an error is returned.

For example, the following two examples are valid and achieve the same results:

- channel list = 
 19-0 and pattern array = 
 0000 0XXX XX11 1111 1111
- channel list = 
 0-19 and pattern array = 
 1111 1111 11XX XXX0 0000

The following example searches for ten consecutive samples on channel 0:

| Sample 0 | x |
| --- | --- |
| Sample 1 | 1 |
| Sample ... | ... |
| Sample 8 | 0 |
| Sample 9 | 1 |

The following example searches for ten consecutive samples on channels 0 to 19:

| Sample 0 | 0000 0000 0000 0000 0000 |
| --- | --- |
| Sample 1 | 1111 1111 1111 1111 0000 |
| Sample ... | ... |
| Sample 8 | 0000 1111 1111 1111 1111 |
| Sample 9 | 1111 1111 11XX XXX0 0000 |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=configure-data-interpretation.html language=enus -->
## TOPIC 00009: Configure Data Interpretation

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `configure-data-interpretation.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/configure-data-interpretation.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects between acquiring high/low data or valid/invalid data during a static or dynamic acquisition operation. PXI/PXIe-654x/656x devices support only the high/low mode of data interpretation. NI-HSDIO returns an error if you select valid/invalid mode for an acquisition with these devices. Select H

Configure Data Interpretation

Selects between acquiring high/low data or valid/invalid data during a static or dynamic acquisition operation.

Note

x

x

Select 
 High or Low to get logic high or logic low values. Select 
 Valid or Invalid to determine if the signal is within the specified voltage range (above Data Voltage Low Level but below Data Voltage High Level) or outside the range (below Data Voltage Low Level or above Data Voltage High Level).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

The channels you want to apply settings to. Leave channel list blank to apply to all channels.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### data interpretation

The specified value for data interpretation.

| High or Low |  | The data read represents logical values (logic high or logic low). |
| --- | --- | --- |
| Valid or Invalid |  | The data read represents whether channel data is within a specified voltage range. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=configure-data-voltage-custom-levels.html language=enus -->
## TOPIC 00010: Configure Data Voltage Custom Levels

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `configure-data-voltage-custom-levels.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/configure-data-voltage-custom-levels.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the voltage levels of the data channels using the specified high and low levels. Refer to the device documentation for possible voltage restrictions. When you use this node, NI-HSDIO coerces the values you specify according to the voltage levels supported by your device. Refer to your dev

Configure Data Voltage Custom Levels

Configures the voltage levels of the data channels using the specified high and low levels.

Refer to the device documentation for possible voltage restrictions.

When you use this node, NI-HSDIO coerces the values you specify according to the voltage levels supported by your device. Refer to your device specifications for more information about the supported voltage levels. After you commit the session, you can read the Data High or Data Low properties to get the actual value of the configured custom levels.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

The channels you want to apply settings to. Leave channel list blank to apply to all channels.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### high level

The voltage that identifies the high level.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### low level

The voltage that identifies the low level.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Using this with the PXI--6541/6542

If you are using a PXI-6541/6542 device for generation sessions, you must set high level to the appropriate logic family value, and you must set low level to 
 0.

For acquisition sessions with the NI 6541/6542, select the same value for high level and low level from the following list: 0.9 V, 1.25 V, or 1.65 V.

#### Using this with the PXIe-6544/6545/6547/6548

If you are using an PXIe-6544/6545/6547/6548 device for generation sessions, you must set low level to 
 0. For acquisition sessions with the PXIe-6544/6545/6547/6548, you must select the same value for high level and low level.

Parent topic:

Configure Voltage

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=configure-generation-mode.html language=enus -->
## TOPIC 00011: Configure Generation Mode

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `configure-generation-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/configure-generation-mode.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to initiate the waveform generation based on a specified script or based on a waveform. Initiation occurs after you call the Initiatenode. session in Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize Ex

Configure Generation Mode

Specifies whether to initiate the waveform generation based on a specified script or based on a waveform.

Initiation occurs after you call the Initiatenode.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### generation mode

The generation mode you want to configure.

| Waveform | The generated waveform is based on a selected waveform. |
| --- | --- |
| Scripted | The generated waveform is based on a selected script. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Scripting

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=configure-idle-state-string.html language=enus -->
## TOPIC 00012: Configure Idle State String

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `configure-idle-state-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/configure-idle-state-string.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the state of the channels when the dynamic generation operation is idle using a string format The operation may be idle when the generation operation completes normally, when the generation operation pauses from an active Pause trigger, or when the generation operation terminates because of an

Configure Idle State String

Sets the state of the channels when the dynamic generation operation is idle using a string format

The operation may be idle when the generation operation completes normally, when the generation operation pauses from an active Pause trigger, or when the generation operation terminates because of an underflow error.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### idle state

The idle state of a dynamic generation operation.

This expression is composed of characters:

- X or 
 x —Retains the previous value.
- 1 —Sets the channel to logic high.
- 0 —Sets the channel to logic low.
- Z or 
 z —Disables the channel (sets it to a high-impedance state).

The first character in idle state corresponds to the first channel in channel list. The number of characters in pattern must equal the number of channels specified in channel list, or the node returns an error. For example, if you are trying to make three channels tristate, the 
 idle state control needs to be "ZZZ" without any commas or spaces.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

The channels being configured.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configure Idle State

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=configure-idle-state-u32.html language=enus -->
## TOPIC 00013: Configure Idle State U32

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `configure-idle-state-u32.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/configure-idle-state-u32.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the state of the channels when the dynamic generation operation is idle using a binary format The operation may be idle when the generation operation completes normally, when the generation operation pauses from an active Pause trigger, or when the generation operation terminates because of an

Configure Idle State U32

Sets the state of the channels when the dynamic generation operation is idle using a binary format

The operation may be idle when the generation operation completes normally, when the generation operation pauses from an active Pause trigger, or when the generation operation terminates because of an underflow error.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### idle state

The idle state across all channels configured for dynamic generation.

idle state defines the bit mask representing the idle state. High is specified with a 1, and low is specified with a 0. If you need to specify values other than high or low, use the niHSDIO Configure Idle State (String) instance of this node.

Each binary digit of this value is applied to the corresponding channel if it is configured for dynamic generation.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configure Idle State

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=configure-initial-state-u32.html language=enus -->
## TOPIC 00014: Configure Initial State (U32)

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `configure-initial-state-u32.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/configure-initial-state-u32.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Initial state for a dynamic generation operation using a binary format. The Initial state of each channel is driven after the operation is initiated using the Initiatenode. Channels remain unchanged until the operation is initiated. The Initial state is active after the session is initiated

Configure Initial State (U32)

Sets the Initial state for a dynamic generation operation using a binary format.

The Initial state of each channel is driven after the operation is initiated using the Initiatenode. Channels remain unchanged until the operation is initiated. The Initial state is active after the session is initiated and until the start trigger generates the first waveform sample.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### initial state

The initial state of a dynamic generation operation.

This parameter defines the bit mask representing the initial state. High is specified with a 1, and low is specified with a 0. If you need to specify values other than high and low, use the niHSDIO Configure Initial State (String) instance of this node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configure Initial State

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=configure-pattern-match-advance-trigger-u32.html language=enus -->
## TOPIC 00015: Configure Pattern Match Advance Trigger (U32)

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `configure-pattern-match-advance-trigger-u32.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/configure-pattern-match-advance-trigger-u32.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Advance trigger for pattern match triggering. This node is valid only for acquisition sessions. channel list The channels that are configured for pattern matching using the pattern array value. session in Instrument session obtained from the Initialize Acquisition Sessionnode, the Ini

Configure Pattern Match Advance Trigger (U32)

Configures the Advance trigger for pattern match triggering. This node is valid only for acquisition sessions.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

The channels that are configured for pattern matching using the 
pattern array value.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### pattern

The binary pattern that activates the pattern match trigger under the conditions specified in trigger when.

Bits on channels not specified in channel list are ignored.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### trigger when

The conditions under which the trigger is sent.

| Pattern matches | The trigger is asserted when the sampled pattern matches the pattern specified in pattern. |
| --- | --- |
| Pattern does not match | The trigger is asserted when the sampled pattern does not match the pattern specified in pattern. |

Default value: Pattern matches

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=configure-pattern-match-advance-trigger.html language=enus -->
## TOPIC 00016: Configure Pattern Match Advance Trigger

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `configure-pattern-match-advance-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/configure-pattern-match-advance-trigger.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Advance trigger for pattern match triggering. This node is valid only for acquisition sessions. channel list The channels that are configured for pattern matching using the pattern array value. session in Instrument session obtained from the Initialize Acquisition Sessionnode, the Ini

Configure Pattern Match Advance Trigger

Configures the Advance trigger for pattern match triggering. This node is valid only for acquisition sessions.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

The channels that are configured for pattern matching using the 
pattern array value.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### pattern

The binary pattern that activates the pattern match trigger under the conditions specified in trigger when.

This string expression creates a mask for the pattern. This expression is composed of characters:

- X or 
 x : Ignore the channel
- 1 : Match on a logic 1
- 0 : Match on a logic 0
- R or 
 r : Match on a rising edge
- F or 
 f : Match on a falling edge
- E or 
 e : Match on either edge

The first character in the expression corresponds to the first channel in channel list. The number of characters in pattern must correspond to the number of channels specified in channel list or an error is returned.

##### Examples of valid expressions

The following two examples are valid and achieve the same results:

- channel list = 
 19-0 and pattern = 
 0000 0XXX XX11 1111 1111
- channel list = 
 0-19 and pattern = 
 1111 1111 11XX XXX0 0000

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### trigger when

The conditions under which the trigger is sent.

| Pattern matches | The trigger is asserted when the sampled pattern matches the pattern specified in pattern. |
| --- | --- |
| Pattern does not match | The trigger is asserted when the sampled pattern does not match the pattern specified in pattern. |

Default value: Pattern matches

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=configure-pattern-match-pause-trigger-u32.html language=enus -->
## TOPIC 00017: Configure Pattern Match Pause Trigger (U32)

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `configure-pattern-match-pause-trigger-u32.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/configure-pattern-match-pause-trigger-u32.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Pause trigger for pattern match triggering. This node is valid only for acquisition sessions. channel list The channels that are configured for pattern matching using the pattern array value. session in Instrument session obtained from the Initialize Acquisition Sessionnode, the Initi

Configure Pattern Match Pause Trigger (U32)

Configures the Pause trigger for pattern match triggering. This node is valid only for acquisition sessions.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

The channels that are configured for pattern matching using the 
pattern array value.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### pattern

The binary pattern that activates the pattern match trigger under the conditions specified in trigger when.

Bits on channels not specified in channel list are ignored.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### trigger when

The conditions under which the trigger is sent.

| Pattern matches | The trigger is asserted when the sampled pattern matches the pattern specified in pattern. |
| --- | --- |
| Pattern does not match | The trigger is asserted when the sampled pattern does not match the pattern specified in pattern. |

Default value: Pattern matches

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=configure-pattern-match-pause-trigger.html language=enus -->
## TOPIC 00018: Configure Pattern Match Pause Trigger

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `configure-pattern-match-pause-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/configure-pattern-match-pause-trigger.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Pause trigger for pattern match triggering. This node is valid only for acquisition sessions. channel list The channels that are configured for pattern matching using the pattern array value. session in Instrument session obtained from the Initialize Acquisition Sessionnode, the Initi

Configure Pattern Match Pause Trigger

Configures the Pause trigger for pattern match triggering. This node is valid only for acquisition sessions.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

The channels that are configured for pattern matching using the 
pattern array value.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### pattern

The binary pattern that activates the pattern match trigger under the conditions specified in trigger when.

This string expression creates a mask for the pattern. This expression is composed of characters:

- X or 
 x : Ignore the channel
- 1 : Match on a logic 1
- 0 : Match on a logic 0
- R or 
 r : Match on a rising edge
- F or 
 f : Match on a falling edge
- E or 
 e : Match on either edge

The first character in the expression corresponds to the first channel in channel list. The number of characters in pattern must correspond to the number of channels specified in channel list or an error is returned.

##### Examples of valid expressions

The following two examples are valid and achieve the same results:

- channel list = 
 19-0 and pattern = 
 0000 0XXX XX11 1111 1111
- channel list = 
 0-19 and pattern = 
 1111 1111 11XX XXX0 0000

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### trigger when

The conditions under which the trigger is sent.

| Pattern matches | The trigger is asserted when the sampled pattern matches the pattern specified in pattern. |
| --- | --- |
| Pattern does not match | The trigger is asserted when the sampled pattern does not match the pattern specified in pattern. |

Default value: Pattern matches

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=configure-pattern-match-ref-trigger.html language=enus -->
## TOPIC 00019: Configure Pattern Match Ref Trigger

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `configure-pattern-match-ref-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/configure-pattern-match-ref-trigger.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference trigger for pattern match triggering. If the Reference trigger asserts before the required number of pretrigger samples are acquired, it is ignored. This node is valid only for acquisition sessions. channel list The channels that are configured for pattern matching using the

Configure Pattern Match Ref Trigger

Configures the Reference trigger for pattern match triggering. If the Reference trigger asserts before the required number of pretrigger samples are acquired, it is ignored. This node is valid only for acquisition sessions.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

The channels that are configured for pattern matching using the 
pattern array value.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### pattern

The binary pattern that activates the pattern match trigger under the conditions specified in trigger when.

This string expression creates a mask for the pattern. This expression is composed of characters:

- X or 
 x : Ignore the channel
- 1 : Match on a logic 1
- 0 : Match on a logic 0
- R or 
 r : Match on a rising edge
- F or 
 f : Match on a falling edge
- E or 
 e : Match on either edge

The first character in the expression corresponds to the first channel in channel list. The number of characters in pattern must correspond to the number of channels specified in channel list or an error is returned.

##### Examples of valid expressions

The following two examples are valid and achieve the same results:

- channel list = 
 19-0 and pattern = 
 0000 0XXX XX11 1111 1111
- channel list = 
 0-19 and pattern = 
 1111 1111 11XX XXX0 0000

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### trigger when

The conditions under which the trigger is sent.

| Pattern matches | The trigger is asserted when the sampled pattern matches the pattern specified in pattern. |
| --- | --- |
| Pattern does not match | The trigger is asserted when the sampled pattern does not match the pattern specified in pattern. |

Default value: Pattern matches

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### pretrigger samples

The number of pretrigger samples the device must receive before the Reference trigger is acknowledged.

Default value: 500

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=configure-script-to-generate.html language=enus -->
## TOPIC 00020: Configure Script To Generate

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `configure-script-to-generate.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/configure-script-to-generate.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the script that is generated after you call the Initiatenode when the generation mode parameter of the Configure Generation Modenode is set to scripted. If multiple scripts load when the Initiatenode is called, one script must be designated the script to generate or you receive an error. This n

Configure Script To Generate

Sets the script that is generated after you call the Initiatenode when the generation mode parameter of the Configure Generation Modenode is set to 
scripted.

If multiple scripts load when the Initiatenode is called, one script must be designated the script to generate or you receive an error.

This node is only required if multiple scripts are present in the onboard memory.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### script name

The specified string containing a syntactically correct script that is written to the onboard memory.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Scripting

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=configure-trigger.html language=enus -->
## TOPIC 00021: Configure Trigger

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `configure-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/configure-trigger.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the specified trigger.

Configure Trigger

Configures the specified trigger.

Configuration

nodes

Configure Digital Edge Advance Trigger

node

Configure Digital Edge Reference Trigger

Configures the Reference trigger for digital edge triggering.

Configure Digital Edge Script Trigger

node

Configure Digital Edge Start Trigger

Configures the Start trigger for digital edge triggering.

Configure Digital Edge Stop Trigger

node

Configure Digital Level Pause Trigger

Configures the Pause trigger as a level trigger.

Configure Digital Level Script Trigger

node

Configure Multi-Sample Pattern Match Advance Trigger

Configures the Advance trigger for multi-sample pattern match triggering.

Configure Multi-Sample Pattern Match Advance Trigger (U32)

Configures the Advance trigger for multi-sample pattern match triggering.

Configure Multi-Sample Pattern Match Reference Trigger

Configures the Reference trigger for multi-sample pattern match triggering.

Configure Multi-Sample Pattern Match Reference Trigger (U32)

Configures the Reference trigger for multi-sample pattern match triggering.

Configure Multi-Sample Pattern Match Start Trigger

Configures the Start trigger for multi-sample pattern match triggering.

Configure Multi-Sample Pattern Match Start Trigger (U32)

Configures the Start trigger for multi-sample pattern match triggering.

Configure Pattern Match Advance Trigger

node

Configure Pattern Match Advance Trigger (U32)

node

Configure Pattern Match Pause Trigger

node

Configure Pattern Match Pause Trigger (U32)

node

Configure Pattern Match Ref Trigger

node

Configure Pattern Match Ref Trigger (U32)

Configures the Reference trigger for pattern match triggering.

Configure Pattern Match Start Trigger

node

Configure Pattern Match Start Trigger (U32)

node

Configure Software Advance Trigger

node

node

Configure Software Reference Trigger

Configures the Reference trigger for software triggering.

Configure Software Script Trigger

node

Configure Software Start Trigger

node

Configure Software Stop Trigger

node

node

Disable Advance Trigger

node

Disable Pause Trigger

node

Disable Reference Trigger

node

Disable Script Trigger

node

Disable Start Trigger

node

Disable Stop Trigger

node

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=configure-waveform-to-generate.html language=enus -->
## TOPIC 00022: Configure Waveform To Generate

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `configure-waveform-to-generate.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/configure-waveform-to-generate.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the waveform to be generated after a call to the Initiatenode when the generation mode parameter of the Configure Generation Modenode is set to Waveform. Waveform is the default value for the generation mode. If this node is not called and you have multiple waveforms in onboard memory, NI-HSDIO

Configure Waveform To Generate

Sets the waveform to be generated after a call to the Initiatenode when the generation mode parameter of the Configure Generation Modenode is set to 
Waveform.

Waveform is the default value for the 
 generation mode.

If this node is not called and you have multiple waveforms in onboard memory, NI-HSDIO generates an error at initiate.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### waveform name

The name of a previously allocated or written waveform to be generated at initiate.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Waveform Control

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=convert-binary-to-wdt.html language=enus -->
## TOPIC 00023: Convert Binary To WDT

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `convert-binary-to-wdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/convert-binary-to-wdt.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts unsigned binary data into the digital waveform data type (WDT). Use this node to easily create extended state (0, 1, H, L, X, Z) digital waveforms from binary data.

Convert Binary To WDT

Converts unsigned binary data into the digital waveform data type (WDT). Use this node to easily create extended state (0, 1, H, L, X, Z) digital waveforms from binary data.

Utility

nodes

Convert Binary To WDT Response Data (U32)

Converts binary data to expect low (L) or expect high (H) digital waveform data types.

Convert Binary To WDT Stimulus And Response Data (U32)

Compiles binary data to bidirectional drive (0, 1, Z) and compare (H, L, X) data.

Convert Binary To WDT Stimulus Data (U32)

Converts binary data to drive low (0) or drive high (1) digital waveform data types.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=disable-script-trigger.html language=enus -->
## TOPIC 00024: Disable Script Trigger

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `disable-script-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/disable-script-trigger.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables a Script trigger. This node is necessary only if you have configured a Script trigger and now want to disable it. This node is valid only for generation sessions. session in Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or th

Disable Script Trigger

Disables a Script trigger. This node is necessary only if you have configured a Script trigger and now want to disable it.

This node is valid only for generation sessions.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### trigger id

The specified instance of the Script trigger.

You can choose 
 Script Trigger 0, 
 Script Trigger 1, 
 Script Trigger 2, or 
 Script Trigger 3 based on which trigger you are using for your Script.

Note

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=external-calibration.html language=enus -->
## TOPIC 00025: External Calibration

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `external-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/external-calibration.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the External Calibration nodes to perform external calibration operations.

External Calibration

Use the External Calibration nodes to perform external calibration operations.

Calibration

nodes

Initialize External Calibration

Creates and initializes a special NI-HSDIO external calibration session.

Initialize Child Calibration Session

session type

Close Child Calibration Session

node

Close External Calibration

Closes an NI-HSDIO external calibration session and, if specified, stores the new calibration constants and calibration data in the onboard EEPROM.

Adjust Calibration (DBL)

Performs internal calculations on a single floating point value and saves the resulting values until the end of the External Calibration session.

Configure Calibration State

Configures the internal routing of the device or the channel so that you can perform specific calibration steps.

Clear Calibration State

Restores the internal routing of the device to the default, unconfigured state.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=initialize.html language=enus -->
## TOPIC 00026: Initialize

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `initialize.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/initialize.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new acquisition or generation session. You can perform static and dynamic acquisition operations with this session.

Initialize

Creates a new acquisition or generation session. You can perform static and dynamic acquisition operations with this session.

NI-HSDIO Nodes

nodes

Initialize Acquisition Session

Creates a new acquisition session. You can perform static and dynamic acquisition operations with this session.

Initialize Generation Session

Creates a new generation session. You can perform static and dynamic generation operations with this session.

Parent topic:

NI-HSDIO Nodes

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=nihsdio-configure-acquisition-size.html language=enus -->
## TOPIC 00027: Configure Acquisition Size

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `nihsdio-configure-acquisition-size.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/nihsdio-configure-acquisition-size.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the size of the acquisition, including how many records are acquired and the minimum record size. session in Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode. samples per record The n

Configure Acquisition Size

Configures the size of the acquisition, including how many records are acquired and the minimum record size.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples per record

The number of samples to acquire per record.

If you need pretrigger and posttrigger points, configure a Reference trigger with the niHSDIO Configure Triggernode and specify the number of pretrigger samples in that node call.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number of records

The number of records you want to acquire. A record is a group of samples.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=property-node.html language=enus -->
## TOPIC 00028: Property Node

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `property-node.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/property-node.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets, gets, or checks properties. Some NI-HSDIO properties are channel based. When a property is channel based, you must specify an active channel before setting, getting, or checking properties. ni-HSDIO in A reference from a previous node. error in Error conditions that occur before this node runs

Property Node

Sets, gets, or checks properties.

Some NI-HSDIO properties are channel based. When a property is channel based, you must specify an active channel before setting, getting, or checking properties.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### ni-HSDIO in

A reference from a previous node.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### ni-HSDIO out

The returned reference from the NI-Digital Waveform Generator/Analyzer Driver session to another node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

NI-HSDIO Nodes

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=read-bus-waveform-wdt.html language=enus -->
## TOPIC 00029: Read Bus Waveform (WDT)

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `read-bus-waveform-wdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/read-bus-waveform-wdt.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the acquired waveform data as an array of waveforms, one for each element in the channel list array. This node allows you to read data in any order or subset that you desire without the need to manipulate the data after reading it. session in Instrument session obtained from the Initialize A

Read Bus Waveform (WDT)

Returns the acquired waveform data as an array of waveforms, one for each element in the channel list array.

This node allows you to read data in any order or subset that you desire without the need to manipulate the data after reading it.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples to read

The specified number of samples to fetch per waveform.

If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to 
 -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Sizenode.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum time (ms)

The time, in milliseconds, allotted for the node to complete before NI-HSDIO returns a timeout error.

If you set the value to 
 -1, the node never times out. If you set this parameter to 
 0, the node returns immediately with up to the number of samples specified in samples to read.

If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples.

Default value: 10000

[IMAGE alt='datatype_icon' src='/assets/img/c1dstr.png']

##### channel list

The channels from which you want to read waveform data. You must assign all channels that you want to read using the niHSDIO Assign Dynamic Channelsnode before selecting those channels with this parameter.

NI-HSDIO reads waveform data in the order that you list channels in this parameter, not in the order that those channels are listed in the niHSDIO Assign Dynamic Channelsnode. If you leave this parameter blank, NI-HSDIO reads all channels.

Each element in this array, consisting of its specified channels, is output as a single waveform in the 
 data parameter. Specify multiple channels in each element by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 
 0,2 specifies a waveform showing channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 
 0-2 specifies a waveform showing channels 0, 1, and 2).

You can include the same channel in multiple elements of this array. For example, if you choose 
 0:2 as the first element, 
 0, 2 as the second element, and 
 0 as the third element, the 
 data parameter returns three waveforms: the first depicting channels 0 through 2, the second depicting channels 0 and 2, and the third depicting just channel 0.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### timestamp type

Parameter that specifies whether the timestamp for the waveform data is relative or absolute.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### starting record

The record at which you want to start fetching data.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/idigwfm.png']

##### data

The acquired data as an array of waveforms, one for each element in the channel list parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### number of samples read

The number of samples that were successfully acquired and transferred into 
data.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

NI-HSDIO Nodes

Parent topic:

Read Waveform

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=read-multi-record-2d-u8.html language=enus -->
## TOPIC 00030: Read Multi Record (2D U8)

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `read-multi-record-2d-u8.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/read-multi-record-2d-u8.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the acquired waveform as a two-dimensional array of unsigned 8-bit integers. session in Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode. samples to read The specified number of samples

Read Multi Record (2D U8)

Returns the acquired waveform as a two-dimensional array of unsigned 8-bit integers.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### samples to read

The specified number of samples to fetch.

If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to 
 -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Sizenode.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum time (ms)

The time, in milliseconds, allotted for the node to complete before NI-HSDIO returns a timeout error.

If you set the value to 
 -1, the node never times out. If you set this parameter to 
 0, the node returns immediately with up to the number of samples specified in samples to read.

If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples.

Default value: 10000

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### starting record

The record at which you want to start fetching data.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### records to fetch

The number of records you want to fetch from onboard memory.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### data

The returned data for the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/i1dnclst.png']

##### waveform info

The absolute and relative timestamp for the operation, the dt, and the actual number of samples read.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### absolute timestamp

absolute timestamp returns the absolute timestamp for the operation.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### relative timestamp

relative timestamp returns the relative timestamp for the operation.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

dt returns the time between values in the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### actual samples read

The returned number of samples read.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### reserved 1

reserved 1 is reserved for future use.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### reserved 2

reserved 2 is reserved for future use.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Read Waveform

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=read-multi-record-wdt.html language=enus -->
## TOPIC 00031: Read Multi Record (WDT)

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `read-multi-record-wdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/read-multi-record-wdt.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the acquired waveforms from the subset of channels listed in the channel list parameter as an array of waveform data type data. Each waveform only contains data from the subset of channels specified in the channel list parameter, not from all of the channels listed in the Assign Dynamic Chan

Read Multi Record (WDT)

Returns the acquired waveforms from the subset of channels listed in the channel list parameter as an array of waveform data type data.

Each waveform only contains data from the subset of channels specified in the channel list parameter, not from all of the channels listed in the Assign Dynamic Channelsnode, unless you leave the channel list parameter blank.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples to read

The specified number of samples to fetch.

If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to 
 -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Sizenode.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum time (ms)

The time, in milliseconds, allotted for the node to complete before NI-HSDIO returns a timeout error.

If you set the value to 
 -1, the node never times out. If you set this parameter to 
 0, the node returns immediately with up to the number of samples specified in samples to read.

If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples.

Default value: 10000

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

The specified channels from which to read waveform data.

You must assign all channels that you want to read using the niHSDIO Assign Dynamic Channelsnode before selecting those channels with this parameter.

NI-HSDIO reads waveform data in the order that you list channels in this parameter, not in the order that those channels are listed in the niHSDIO Assign Dynamic Channelsnode. If you leave this parameter blank, NI-HSDIO reads all channels that were set using the niHSDIO Assign Dynamic Channelsnode.

Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 
 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 
 0-2 specifies channels 0, 1, and 2).

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### timestamp type

Parameter that specifies whether the timestamp for the waveform data is relative or absolute.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### starting record

The record at which you want to start fetching data.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### records to fetch

The number of records you want to fetch from onboard memory.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### data

The returned data for the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### actual samples read

The returned number of samples read.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Read Waveform

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=read-static-pfi-u32.html language=enus -->
## TOPIC 00032: Read Static PFI (U32)

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `read-static-pfi-u32.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/read-static-pfi-u32.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Immediately reads all PFI channels configured for static acquisition. The least significant bit of read data corresponds to the lowest physical PFI channel number. You can configure a channel for static acquisition using the Assign Static Channelsnode. Channels not configured for static acquisition

Read Static PFI (U32)

Immediately reads all PFI channels configured for static acquisition. The least significant bit of read data corresponds to the lowest physical PFI channel number.

You can configure a channel for static acquisition using the Assign Static Channelsnode. Channels not configured for static acquisition return a zero. Channels that do not exist on the hardware also return a zero.

Values obtained from static read operations are affected by the data interpretation parameter of the Configure Data Interpretationnode.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### read data

The returned bit value of data read from PFI channels configured for static acquisition.

The least significant bit of read data corresponds to the lowest physical channel number. For example, bit 0 corresponds to PFI0, and bit 31 corresponds to PFI31, if that channel exists on the hardware.

If read data returns a value of 0x000F, channels PFI0 to PFI3 are logic one and the remaining channels are logic zero or are not configured for static acquisition.

If read data returns a value of 0xFFF0, channels PFI4 to PFI15 are logic one and the remaining channels are logic zero or are not configured for static acquisition.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Action

Parent topic:

Static

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=read-waveform-wdt.html language=enus -->
## TOPIC 00033: Read Waveform (WDT)

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `read-waveform-wdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/read-waveform-wdt.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the acquired waveform data from the subset of channels listed in the channel list parameter as a waveform data type. The waveform only contains data from the subset of channels specified in the channel list parameter, not from all of the channels listed in the Assign Dynamic Channelsnode, un

Read Waveform (WDT)

Returns the acquired waveform data from the subset of channels listed in the channel list parameter as a waveform data type.

The waveform only contains data from the subset of channels specified in the channel list parameter, not from all of the channels listed in the Assign Dynamic Channelsnode, unless you leave the 
 channel list parameter blank.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### timestamp type

Parameter that specifies whether the timestamp for the waveform data is relative or absolute.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

The specified channels from which to read waveform data.

You must assign all channels that you want to read using the niHSDIO Assign Dynamic Channelsnode before selecting those channels with this parameter.

NI-HSDIO reads waveform data in the order that you list channels in this parameter, not in the order that those channels are listed in the niHSDIO Assign Dynamic Channelsnode. If you leave this parameter blank, NI-HSDIO reads all channels that were set using the niHSDIO Assign Dynamic Channelsnode.

Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 
 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 
 0-2 specifies channels 0, 1, and 2).

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples to read

The specified number of samples to fetch.

If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to 
 -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Sizenode.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum time (ms)

The time, in milliseconds, allotted for the node to complete before NI-HSDIO returns a timeout error.

If you set the value to 
 -1, the node never times out. If you set this parameter to 
 0, the node returns immediately with up to the number of samples specified in samples to read.

If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples.

Default value: 10000

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### record to fetch

Parameter that specifies which record you want to fetch from onboard memory.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/idigwfm.png']

##### data

The returned acquired waveform.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### number of samples read

The number of samples that were successfully acquired and transferred into 
data.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Read Waveform

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=reset-device.html language=enus -->
## TOPIC 00034: Reset Device

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `reset-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/reset-device.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the device to its initial state and reloads the FPGA. Use this node to re-enable your device if it has disabled itself because the device temperature has risen above its optimal operating temperature. All channels and front panel terminals are put into a high-impedance state. All software att

Reset Device

Resets the device to its initial state and reloads the FPGA. Use this node to re-enable your device if it has disabled itself because the device temperature has risen above its optimal operating temperature.

All channels and front panel terminals are put into a high-impedance state. All software attributes are reset to their initial values.
 The entire contents of the FPGA and EEPROM files are reloaded.

During a device reset, signal routes between this and other devices are released, regardless of which device created the route. For instance, a trigger signal being exported to a PXI trigger line and used by another device is no longer exported.

Generally, using the Resetnode is acceptable in place of the Reset Devicenode. The Resetnode executes more quickly.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=scripting.html language=enus -->
## TOPIC 00035: Scripting

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `scripting.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/scripting.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Scripting nodes to create and configure scripts for your generation operation.

Scripting

Use the Scripting nodes to create and configure scripts for your generation operation.

Configuration

nodes

Configure Generation Mode

Specifies whether to initiate the waveform generation based on a specified script or based on a waveform.

Write Script

Writes a string to the onboard memory containing scripts that govern the waveform generation.

Configure Script To Generate

node

generation mode

node

scripted

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=self-test.html language=enus -->
## TOPIC 00036: Self-Test

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `self-test.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/self-test.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a self-test on the instrument and returns the test results. The Self-Testnode performs a simple series of tests that ensure the instrument is powered up and responding. This node does not perform complete functional testing and calibration. This node is internal and does not affect external

Self-Test

Performs a self-test on the instrument and returns the test results.

The Self-Testnode performs a simple series of tests that ensure the instrument is powered up and responding. This node does not perform complete functional testing and calibration.

This node is internal and does not affect external I/O connections or connections between devices.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### self test result

The value returned from the device self-test. A 0 means the self-test passed; anything else means the test failed.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### self test message

The returned self-test response string from the device.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=send-software-edge-trigger.html language=enus -->
## TOPIC 00037: Send Software Edge Trigger

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `send-software-edge-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/send-software-edge-trigger.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Forces a particular edge, pattern match, or software trigger to occur. This node applies only to the triggers listed below, and it is valid only if the particular trigger has been configured for edge, pattern match, or software triggering: Start Trigger Reference Trigger Advance Trigger Script Trigg

Send Software Edge Trigger

Forces a particular edge, pattern match, or software trigger to occur.

This node applies only to the triggers listed below, and it is valid only if the particular trigger has been configured for edge, pattern match, or software triggering:

- Start Trigger
- Reference Trigger
- Advance Trigger
- Script Trigger
- Stop Trigger

For edge or pattern match triggers, you can use this node as a software override.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### trigger

The trigger you want to assert.

You can select 
 Start Trigger, 
 Reference Trigger, 
 Advance Trigger, 
 Script Trigger, or 
 Stop Trigger as the value for this control.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### trigger id

The specified details of the script trigger.

This parameter can be 
 ScriptTrigger0, 
 ScriptTrigger1, 
 ScriptTrigger2, or 
 ScriptTrigger3; or you can leave this parameter blank for the Start, Reference, Advance, and Stop triggers.

Note

ScriptTrigger 3

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=set-cal-user-defined-info.html language=enus -->
## TOPIC 00038: Set Calibration User Defined Info

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `set-cal-user-defined-info.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/set-cal-user-defined-info.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores a user-defined string of characters in the device onboard EEPROM. If the string is longer than the maximum allowable size, it is truncated. This node overwrites any existing user-defined information. If you call this node in a session, information is immediately changed. If you call this node

Set Calibration User Defined Info

Stores a user-defined string of characters in the device onboard EEPROM.

If the string is longer than the maximum allowable size, it is truncated.

This node overwrites any existing user-defined information. If you call this node in a session, information is immediately changed. If you call this node in an external calibration session, information is changed only after you close the session using the Close Ext Calnode with calibration close action set to 
 Commit.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument handle that identifies your calibration session.

This parameter is obtained from the niHSDIO Initialize External Calibrationnode

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### info

The string to store in the onboard EEPROM.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=stpmu-measure-voltage.html language=enus -->
## TOPIC 00039: stPMU Measure Voltage

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `stpmu-measure-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/stpmu-measure-voltage.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measures the voltage on the channels specified in the channel list parameter. You can call this node at any time, including while in a digital state or a PMU state. Only the PXIe-6555 and the PXIe-6556 support this node. session in Instrument session obtained from the Initialize Acquisition Sessionn

stPMU Measure Voltage

Measures the voltage on the channels specified in the channel list parameter. You can call this node at any time, including while in a digital state or a PMU state.

Note

node

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel list

The channels you want to configure.

Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 
 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 
 0-2 specifies channels 0, 1, and 2).

Use 
 PFI1 or 
 PFI2 to specify a valid PFI channel. Use 
 DDC_CLKOUT or 
 STROBE to specify a valid clocking terminal. If you configure multiple channels with this parameter, all those channels have the same settings. Selecting no channels for this parameter returns an error.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### aperture time (4E-06)

Parameter that configures the amount of time, in seconds, to measure each channel.

The aperture time determines the number of hardware averages per measurement. The larger the aperture time, the greater the number of hardware averages.

Default value: 4E<sup>^</sup>6 (0.000004)

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sense (local)

Parameter that selects between local or remote sensing on the specified channel(s).

| local | 88 | Local sensing of voltages. This value is measured on the DDC connector. |
| --- | --- | --- |
| remote | 89 | Remote sensing of voltages. This value is measured on the Remote Sense connector. |

Default value: local

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### voltage measurements

The returned array of double-precision numbers that represents the averaged measured voltages, per channel, in volts (V), over time.

The order of the returned voltages directly corresponds with the order in which the channels are configured in the channel list parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Committing your session

If you have not yet committed your session, calling this node implicitly commits your session. If you have already committed your session by calling a node such as the Commitnode, the Initiatenode, the Read Waveformnode, the Write Named Waveformnode, or the other nodes, this node will 
 not commit your session again.

Parent topic:

Software-Timed PMU

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=waveform-control.html language=enus -->
## TOPIC 00040: Waveform Control

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `waveform-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/waveform-control.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Waveform Control nodes to configure the waveforms in your generation operation.

Waveform Control

Use the Waveform Control nodes to configure the waveforms in your generation operation.

Configuration

nodes

Configure Waveform To Generate

node

generation mode

node

Waveform

Allocate Named Waveform

Reserves waveform space in onboard memory and associates a waveform name with it. Individual waveforms are stored contiguously in onboard memory.

Delete Named Waveform

Frees waveform space in onboard memory.

Set Named Waveform Next Write Position

Modifies where to next write within a named waveform.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=write-named-waveform-1d-u16.html language=enus -->
## TOPIC 00041: Write Named Waveform (1D U16)

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `write-named-waveform-1d-u16.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/write-named-waveform-1d-u16.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the waveform to onboard memory from a one-dimensional array of unsigned 16-bit data. This node accepts multiple data types for the data parameter. Hover over data for more information. waveform name The name of the waveform to configure position. You should name waveforms using this node unde

Write Named Waveform (1D U16)

Writes the waveform to onboard memory from a one-dimensional array of unsigned 16-bit data.

Note

node

data

data

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### waveform name

The name of the waveform to configure position.

You should name waveforms using this node under either of the following conditions:

- You are using scripts.
- You want to download multiple waveforms into the hardware.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1du16.png']

##### data

The data to write.

This input accepts the following data types:

- Waveform
- 1D array of 8-bit unsigned integers
- 1D array of 16-bit unsigned integers
- 1D array of 32-bit unsigned integers

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Write Named Waveform

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=write-named-waveform-1d-u8.html language=enus -->
## TOPIC 00042: Write Named Waveform (1D U8)

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `write-named-waveform-1d-u8.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/write-named-waveform-1d-u8.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the waveform to onboard memory from a one-dimensional array of unsigned 8-bit data. This node accepts multiple data types for the data parameter. Hover over data for more information. waveform name The name of the waveform to configure position. You should name waveforms using this node under

Write Named Waveform (1D U8)

Writes the waveform to onboard memory from a one-dimensional array of unsigned 8-bit data.

Note

node

data

data

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### waveform name

The name of the waveform to configure position.

You should name waveforms using this node under either of the following conditions:

- You are using scripts.
- You want to download multiple waveforms into the hardware.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1du8.png']

##### data

The specified data for the waveform to be written.

This input accepts the following data types:

- Waveform
- 1D array of 8-bit unsigned integers
- 1D array of 16-bit unsigned integers
- 1D array of 32-bit unsigned integers

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Write Named Waveform

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=write-named-waveform-from-file-hws.html language=enus -->
## TOPIC 00043: Write Named Waveform From File (HWS)

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `write-named-waveform-from-file-hws.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/write-named-waveform-from-file-hws.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the waveform to onboard memory from a .hws (Hierarchical Waveform Storage) file. waveform name The name of the waveform to configure position. You should name waveforms using this node under either of the following conditions: You are using scripts. You want to download multiple waveforms int

Write Named Waveform From File (HWS)

Writes the waveform to onboard memory from a 
.hws (Hierarchical Waveform Storage) file.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### waveform name

The name of the waveform to configure position.

You should name waveforms using this node under either of the following conditions:

- You are using scripts.
- You want to download multiple waveforms into the hardware.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### file path

The path and file name of the HWS file you want to open.

The 
 .hws extension is typically used for HWS files, although using this extension is optional.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### use rate from waveform

A Boolean that specifies how the sample rate is computed.

| True | The sample rate from the WDT value is computed. |
| --- | --- |
| False | The sample rate from the WDT value is not computed. |

If the sample rate has been configured using the Configure Sample Clocknode, use rate from waveform overrides the sample rate.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### waveform size

The returned number of samples that the waveform contains.

Parent topic:

Write Named Waveform

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=write-named-waveform-wdt.html language=enus -->
## TOPIC 00044: Write Named Waveform (WDT)

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `write-named-waveform-wdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/write-named-waveform-wdt.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the waveform to onboard memory as waveform data type data. waveform name The name of the waveform to configure position. You should name waveforms using this node under either of the following conditions: You are using scripts. You want to download multiple waveforms into the hardware. sessio

Write Named Waveform (WDT)

Writes the waveform to onboard memory as waveform data type data.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### waveform name

The name of the waveform to configure position.

You should name waveforms using this node under either of the following conditions:

- You are using scripts.
- You want to download multiple waveforms into the hardware.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdigwfm.png']

##### data

Parameter that provides a waveform to generate.

This input accepts the following data types:

- Waveform
- 1D array of 8-bit unsigned integers
- 1D array of 16-bit unsigned integers
- 1D array of 32-bit unsigned integers

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### use rate from waveform

A Boolean that specifies how the sample rate is computed.

| True | The sample rate from the WDT value is computed. |
| --- | --- |
| False | The sample rate from the WDT value is not computed. |

If the sample rate has been configured using the Configure Sample Clocknode, use rate from waveform overrides the sample rate.

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Write Named Waveform

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=write-named-waveform.html language=enus -->
## TOPIC 00045: Write Named Waveform

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `write-named-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/write-named-waveform.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transfers waveform data from PC memory to onboard memory. If you specify a waveform name not already being used on the instrument, the appropriate amount of onboard memory is allocated (if available) and the data is stored in that new location.

Write Named Waveform

Transfers waveform data from PC memory to onboard memory.If you specify a waveform name not already being used on the instrument, the appropriate amount of onboard memory is allocated (if available) and the data is stored in that new location.

Action

nodes

Write Named Waveform (1D U8)

Writes the waveform to onboard memory from a one-dimensional array of unsigned 8-bit data.

Write Named Waveform (1D U16)

Writes the waveform to onboard memory from a one-dimensional array of unsigned 16-bit data.

Write Named Waveform (1D U32)

Writes the waveform to onboard memory from a one-dimensional array of unsigned 32-bit data.

Write Named Waveform (Direct DMA)

Writes a specified amount of data from a Direct DMA-compatible device to the waveform in onboard memory.

Write Named Waveform (WDT)

Writes the waveform to onboard memory as waveform data type data.

Write Named Waveform From File (HWS)

.hws

Parent topic:

Action

<!--NI_TOPIC bundle=ni-hsdio-19.5-lvnxg-api-ref path=write-script.html language=enus -->
## TOPIC 00046: Write Script

- bundle_id: `ni-hsdio-19.5-lvnxg-api-ref`
- source_path: `write-script.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-19.5-lvnxg-api-ref/raw/resource/enus/write-script.html
- document_id: `ni-hsdio-19.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a string to the onboard memory containing scripts that govern the waveform generation. If this node is called repeatedly, previously written scripts with unique names remain loaded. Previously written scripts with identical names to those being written are replaced. If multiple scripts load w

Write Script

Writes a string to the onboard memory containing scripts that govern the waveform generation.

If this node is called repeatedly, previously written scripts with unique names remain loaded. Previously written scripts with identical names to those being written are replaced. If multiple scripts load when the Initiatenode is called, one script must be designated as the script to generate. If only one script exists in memory, you do not need to designate the script to generate.

This node returns an error if the script uses incorrect syntax. This node calls the Dynamic instance of the Commitnode. All pending attributes are committed to hardware.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from the Initialize Acquisition Sessionnode, the Initialize Generation Sessionnode, or the Initialize External Calibrationnode.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### script

The specified text of the script you want to use for your generation operation.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Handle that identifies the session in all subsequent node calls.

The session out parameter is obtained from the Initialize Acquisition Sessionnode or the Initialize Generation Sessionnode.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Scripting
