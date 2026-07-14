# NI DOCUMENT BUNDLE: ni-rfsg-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-rfsg-lvnxg-api-ref start=1 end=84 -->
<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=abort.html language=enus -->
## TOPIC 00001: Abort

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `abort.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/abort.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops signal generation. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session out Reference to you

Abort

Stops signal generation.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Arbitrary Waveform Streaming

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=action-nodes.html language=enus -->
## TOPIC 00002: Action Nodes

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `action-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/action-nodes.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Action Nodes

NI-RFSG Nodes

Initiate

NI-RFSG

Abort

Stops signal generation.

Check Generation Status

Checks the status of the generation.

Send Software Edge Trigger

Forces a trigger to occur.

Commit

Programs the device with the correct settings.

Wait Until Settled

Waits until the RF output signal settles.

Configure Output Enabled

Enables or disables signal output.

Perform Power Search

Performs a power search if the ALC Control property is disabled.

Parent topic:

NI-RFSG Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=allocate-arbitrary-waveform.html language=enus -->
## TOPIC 00003: Allocate Arbitrary Waveform

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `allocate-arbitrary-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/allocate-arbitrary-waveform.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Allocates onboard memory space for the arbitrary waveform. Use this node to specify the total size of a waveform before writing the data. Use this node only if you are calling Write Arb Waveform multiple times to write a large waveform in smaller blocks. The NI-RFSG device must be in the Configurati

Allocate Arbitrary Waveform

Allocates onboard memory space for the arbitrary waveform.

Use this node to specify the total size of a waveform before writing the data. Use this node only if you are calling Write Arb Waveform multiple times to write a large waveform in smaller blocks.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

Name used to store the waveform.

This string is case-insensitive and alphanumeric, and it cannot use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### size in samples

Size of the waveform to allocate in samples. Each I/Q pair is considered one sample.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Arbitrary Waveform Streaming
- RFSG Large Arbitrary Waveform Generation

Parent topic:

Arbitrary Waveform Generator Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=arbitrary-waveform-generator-nodes.html language=enus -->
## TOPIC 00004: Arbitrary Waveform Generator Nodes

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `arbitrary-waveform-generator-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/arbitrary-waveform-generator-nodes.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Arbitrary Waveform Generator Nodes

Configuration Nodes

Write Arbitrary Waveform

Check If Waveform Exists

Returns whether the waveform that you specify exists.

Clear Arbitrary Waveform

Deletes a specified waveform from the set of currently defined waveforms.

Clear All Arbitrary Waveforms

Deletes all currently defined waveforms and scripts.

Configure Digital Modulation User Defined Waveform

Specifies the message signal used for digital modulation when the Modulation Type property is enabled and the Waveform Type property is set to User-defined.

Allocate Arbitrary Waveform

Allocates onboard memory space for the arbitrary waveform.

Select Arbitrary Waveform

Specifies the waveform that is generated.

Set Arbitrary Waveform Next Write Position

Write Arbitrary Waveform

Configure Signal Bandwidth

Configures the signal bandwidth of the arbitrary waveform.

Query Arbitrary Waveform Capabilities

Queries and returns the device arbitrary waveform capabilities, which are related to the current device configuration.

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=calibration-nodes.html language=enus -->
## TOPIC 00005: Calibration Nodes

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `calibration-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/calibration-nodes.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Calibration Nodes

NI-RFSG Nodes

Self Calibration

Performs an internal self-calibration on the device and associated modules that support self-calibration.

Self Calibrate Range

Self-calibrates all configurations within the specified frequency and peak power level limits.

Perform Thermal Correction

Corrects for any signal drift due to temperature variation when generating the same signal for extended periods of time without a parameter change.

Get Self Calibration Date and Time

Returns the date and time of the last successful self-calibration.

Get Self Calibration Temperature

Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.

Clear Self Calibrate Range

Self Calibrate Range

External Calibration Nodes

Parent topic:

NI-RFSG Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=change-external-calibration-password.html language=enus -->
## TOPIC 00006: Change External Calibration Password

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `change-external-calibration-password.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/change-external-calibration-password.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the external calibration password of the device. This node works with a regular NI-RFSG session or an NI-RFSG calibration session. session in Instrument session obtained from Initialize External Calibration. error in Error conditions that occur before this node runs. The node responds to thi

Change External Calibration Password

Changes the external calibration password of the device.

This node works with a regular NI-RFSG session or an NI-RFSG calibration session.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize External Calibration](initialize-external-calibration.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### password

Old (current) external calibration password.

This password is case sensitive.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### new password

New (desired) external calibration password.

The password can be no longer than four characters.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXIe-5653/5654
- PXIe-5673E
- PXIe-5696
- PXIe-5820/5840

Parent topic:

External Calibration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=check-generation-status.html language=enus -->
## TOPIC 00007: Check Generation Status

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `check-generation-status.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/check-generation-status.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the generation. This node returns any errors that may occur during signal generation and returns whether the device finishes generating signals. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The n

Check Generation Status

Checks the status of the generation.

This node returns any errors that may occur during signal generation and returns whether the device finishes generating signals.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### done?

Boolean value that indicates whether the signal generation has completed.

| True | Signal generation is complete. |
| --- | --- |
| False | Signal generation is not complete. |

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Getting Started Single Tone Generation
- RFSG Arbitrary Waveform Generation (Arb)
- RFSG Getting Started Script (Script)

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=check-if-configuration-list-exists.html language=enus -->
## TOPIC 00008: Check If Configuration List Exists

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `check-if-configuration-list-exists.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/check-if-configuration-list-exists.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the configuration list that you specify exists. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value

Check If Configuration List Exists

Returns whether the configuration list that you specify exists.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### list name

Name of the configuration list. This string is case-insensitive and alphanumeric, and it cannot contain spaces or use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### list exists?

Boolean value that indicates whether the configuration list exists.

| True | The configuration list exists. |
| --- | --- |
| False | The configuration list does not exist. |

#### Hardware Support

This node supports the following hardware:

- PXIe-5650/5651/5652/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

List Mode Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=check-if-script-exists.html language=enus -->
## TOPIC 00009: Check If Script Exists

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `check-if-script-exists.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/check-if-script-exists.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the script that you specify exists. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error s

Check If Script Exists

Returns whether the script that you specify exists.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### script name

Name of the script. This string is case-insensitive.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### script exists?

Boolean value that indicates whether the script exists.

| True | The script exists. |
| --- | --- |
| False | The script does not exist. |

#### Hardware Support

This node supports the following hardware:

- PXIe-5673E

Parent topic:

Script Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=check-if-waveform-exists.html language=enus -->
## TOPIC 00010: Check If Waveform Exists

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `check-if-waveform-exists.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/check-if-waveform-exists.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the waveform that you specify exists. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error

Check If Waveform Exists

Returns whether the waveform that you specify exists.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### waveform name

Name used to store the waveform. This string is case-insensitive.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### waveform exists?

Boolean value that indicates whether the waveform exists.

| True | The waveform exists. |
| --- | --- |
| False | The waveform does not exist. |

#### Hardware Support

This node supports the following hardware:

- PXIe-5673E

Parent topic:

Arbitrary Waveform Generator Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=clear-all-arbitrary-waveforms.html language=enus -->
## TOPIC 00011: Clear All Arbitrary Waveforms

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `clear-all-arbitrary-waveforms.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/clear-all-arbitrary-waveforms.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes all currently defined waveforms and scripts. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input accor

Clear All Arbitrary Waveforms

Deletes all currently defined waveforms and scripts.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Arbitrary Waveform Generator Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=clear-arbitrary-waveform.html language=enus -->
## TOPIC 00012: Clear Arbitrary Waveform

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `clear-arbitrary-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/clear-arbitrary-waveform.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes a specified waveform from the set of currently defined waveforms. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node respond

Clear Arbitrary Waveform

Deletes a specified waveform from the set of currently defined waveforms.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

Name used to store the waveform.

This string is case-insensitive and alphanumeric, and it cannot use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Arbitrary Waveform Generator Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=clear-self-calibrate-range.html language=enus -->
## TOPIC 00013: Clear Self Calibrate Range

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `clear-self-calibrate-range.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/clear-self-calibrate-range.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the data obtained from Self Calibrate Range. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error s

Clear Self Calibrate Range

Clears the data obtained from [Self Calibrate Range](self-calibrate-range.html).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646

Parent topic:

Calibration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=clock-nodes.html language=enus -->
## TOPIC 00014: Clock Nodes

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `clock-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/clock-nodes.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Clock Nodes

Configuration Nodes

Configure Ref Clock

NI-RFSG

Configure PXI Chassis Clk10

10 MHz

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=close-external-calibration.html language=enus -->
## TOPIC 00015: Close External Calibration

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `close-external-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/close-external-calibration.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the calibration values from the current driver session to the device. session in Instrument session obtained from Initialize External Calibration. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error B

Close External Calibration

Writes the calibration values from the current driver session to the device.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize External Calibration](initialize-external-calibration.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### write calibration to hardware?

Boolean value that indicates whether the calibration values from the current driver session are stored to the device EEPROM.

| True | Overwrites the EEPROM. |
| --- | --- |
| False | Discards the current calibration values. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654
- PXIe-5673E
- PXIe-5696

#### Close External Calibration Behavior for PXIe-5611/5673E

This node also writes the current date and time as the last external calibration date and time.

Parent topic:

External Calibration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=close.html language=enus -->
## TOPIC 00016: Close

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `close.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/close.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts any signal generation in progress and destroys the instrument driver session. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error B

Close

Aborts any signal generation in progress and destroys the instrument driver session.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

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

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXI-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Getting Started Single Tone Generation
- RFSG Arbitrary Waveform Generation (Arb)
- RFSG Getting Started Script (Script)

Parent topic:

NI-RFSG Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=commit.html language=enus -->
## TOPIC 00017: Commit

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `commit.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/commit.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Programs the device with the correct settings. Calling this node moves the NI-RFSG device from the Configuration state to the Committed state. After this node executes, a change to any property reverts the NI-RFSG device to the Configuration state. session in Instrument session obtained from Initial

Commit

Programs the device with the correct settings.

Calling this node moves the NI-RFSG device from the Configuration state to the Committed state. After this node executes, a change to any property reverts the NI-RFSG device to the Configuration state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Frequency Sweep
- RFSG Power Sweep

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configuration-nodes.html language=enus -->
## TOPIC 00018: Configuration Nodes

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configuration-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configuration-nodes.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Configuration Nodes

NI-RFSG Nodes

Configure Generation Mode

NI-RFSG

Configure RF

Configures the frequency and power level of the RF output signal.

Configure Power Level Type

NI-RFSG

Arbitrary Waveform Generator Nodes

Script Nodes

List Mode Nodes

Trigger Nodes

Clock Nodes

Parent topic:

NI-RFSG Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-digital-modulation-user-defined-waveform.html language=enus -->
## TOPIC 00019: Configure Digital Modulation User Defined Waveform

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-digital-modulation-user-defined-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-digital-modulation-user-defined-waveform.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the message signal used for digital modulation when the Modulation Type property is enabled and the Waveform Type property is set to User-defined. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node respo

Configure Digital Modulation User Defined Waveform

Specifies the message signal used for digital modulation when the Modulation Type property is enabled and the Waveform Type property is set to User-defined.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1di8.png']

##### user defined waveform

User-defined message signal used for digital modulation.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXI/PXIe-5650/5651/5652

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG 565x Digital Modulation

Parent topic:

Arbitrary Waveform Generator Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-generation-mode.html language=enus -->
## TOPIC 00020: Configure Generation Mode

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-generation-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-generation-mode.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the NI-RFSG device to generate a continuous sine tone (CW), apply I/Q (vector) modulation to the RF output signal, or generate arbitrary waveforms according to scripts. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained

Configure Generation Mode

Configures the NI-RFSG device to generate a continuous sine tone (CW), apply I/Q (vector) modulation to the RF output signal, or generate arbitrary waveforms according to scripts.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### generation mode

Mode used to generate an RF output signal.

| CW | 0 | Configures the RF analog signal generator to generate a CW signal. |
| --- | --- | --- |
| Arb Waveform | 1 | Configures the RF analog signal generator to generate arbitrary waveforms. This mode is not supported for the PXI/PXIe-5650/5651/5652 , PXIe-5654/5654 with PXIe-5696. |
| Script | 2 | Configures the RF analog signal generator to generate arbitrary waveforms as directed by scripts. This mode is not supported for the PXI/PXIe-5650/5651/5652 , PXIe-5654/5654 with PXIe-5696. Some script instructions are not supported for use with vector signal transceivers. |

Default value: CW

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Getting Started Single Tone Generation (CW)
- RFSG Arbitrary Waveform Generation (Arb)
- RFSG Getting Started Script (Script)

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-output-enabled.html language=enus -->
## TOPIC 00021: Configure Output Enabled

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-output-enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-output-enabled.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables signal output. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error output enabled Boo

Configure Output Enabled

Enables or disables signal output.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### output enabled

Boolean value that indicates whether the RF output is enabled.

| True | Enables signal output. |
| --- | --- |
| False | Disables signal output. |

##### Output Behavior During the Generation State

Setting output enabled to False while in the Generation state attenuates the generated signal so that no signal is output.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-power-level-type.html language=enus -->
## TOPIC 00022: Configure Power Level Type

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-power-level-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-power-level-type.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how NI-RFSG interprets the value of the Power Level property. In average power mode, NI-RFSG automatically scales waveform data to use the maximum dynamic range. In peak power mode, NI-RFSG scales waveforms according to the Software Scaling Factor property. session in Instrument session ob

Configure Power Level Type

Specifies how NI-RFSG interprets the value of the Power Level property.

In average power mode, NI-RFSG automatically scales waveform data to use the maximum dynamic range. In peak power mode, NI-RFSG scales waveforms according to the Software Scaling Factor property.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### power level type

Type of power NI-RFSG uses based on the value of the Power Level property.

| Average Power | 0 | Indicates the desired power averaged in time. The driver maximizes the dynamic range by scaling the I/Q waveform so that its peak magnitude is equal to one. If your write more than one waveform, NI-RFSG scales each waveform without preserving the power level ratio between the waveforms. This value is not valid for the PXIe-5820. |
| --- | --- | --- |
| Peak Power | 1 | Indicates the maximum power level of the RF signal averaged over one period of the RF carrier frequency (the peak envelope power). This setting requires the magnitude of the I/Q waveform be less than or equal to one. When using peak power, the power level of the RF signal matches the specified power level at moments when the magnitude of the I/Q waveform equals one. If you write more than one waveform, the relative scaling between waveforms is preserved. In peak power mode, waveforms are scaled according to theSoftware Scaling Factor property. |

Default value: Average Power

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Arbitrary Waveform Streaming
- RFSG Multitone Generation

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-pxi-chassis-clk10.html language=enus -->
## TOPIC 00023: Configure PXI Chassis Clk10

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-pxi-chassis-clk10.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-pxi-chassis-clk10.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. This option can only be configured when the PXI-5610 is in Slot 2 of the PXI chassis. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained from Initialize

Configure PXI Chassis Clk10

Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane.

This option can only be configured when the PXI-5610 is in Slot 2 of the PXI chassis.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### PXI clk10 source

Source of the Reference Clock signal.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXI-5610
- PXI-5670/5671

Parent topic:

Clock Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-ref-clock.html language=enus -->
## TOPIC 00024: Configure Ref Clock

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-ref-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-ref-clock.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the NI-RFSG device Reference Clock. The Reference Clock ensures that the NI-RFSG devices are operating from a common timebase. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained from Initialize With Options. error in Err

Configure Ref Clock

Configures the NI-RFSG device Reference Clock.

The Reference Clock ensures that the NI-RFSG devices are operating from a common timebase.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### ref clock source

Source of the Reference Clock signal.

| Onboard Clock | Uses the onboard Reference Clock as the clock source. PXIe-5840 with PXIe-5653: Lock to the PXIe-5653 onboard clock. Connect the REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. Configure open NI-RFSA sessions to the device to use RefIn for the PXIe-5840 or RefIn2 for the PXIe-5840 with PXIe-5653. |
| --- | --- |
| RefIn | Uses the clock signal present at the front panel REF IN connector as the clock source. PXIe-5840 with PXIe-5653: Lock to the signal at the REF IN connector on the associated PXIe-5653. Connect the REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. |
| PXI Clock | Uses the PXI_CLK signal, which is present on the PXI backplane, as the clock source. |
| ClkIn | Uses the clock signal present at the front panel CLK IN connector as the clock source. |
| RefIn2 | This value is valid on only the PXIe-5840 with PXIe-5653. NI-RFSG locks the Reference Clock to the clock sourced at the PXIe-5840 REF IN terminal that is already configured by an NI-RFSA session. Connect the PXIe-5840 REF OUT connector to the PXIe-5653 REF IN connector. Configure open NI-RFSA sessions to the device to use RefIn for the PXIe-5840 or Onboard Clock for the PXIe-5840 with PXIe-5653. |
| PXI_ClkMaster | This value is valid on only the PXIe-5840 with PXIe-5653. NI-RFSA configures the PXIe-5653 to export the Reference Clock, and configures the PXIe-5840 to use PXI_Clk. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector for this configuration. For best performance, configure all other devices in the system to use PXI_Clk as the Reference Clock source. |

Default value: Onboard Clock

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### ref clock rate

Reference Clock rate, in hertz (Hz).

Default value: Auto (-1.0)

##### Automatic Reference Clock Detection

Specifying the Reference Clock rate value as Auto allows NI-RFSG to either use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if auto-detection is supported on the device.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Getting Started Single Tone Generation
- RFSG Arbitrary Waveform Generation (Arb)
- RFSG Getting Started Script (Script)

Parent topic:

Clock Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-rf.html language=enus -->
## TOPIC 00025: Configure RF

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-rf.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-rf.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency and power level of the RF output signal. The PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673E, and PXIe-5840 can be in the Configuration state or Generation state when you call this node. session in Instrument session obtained from Init

Configure RF

Configures the frequency and power level of the RF output signal.

The PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673E, and PXIe-5840 can be in the Configuration state or Generation state when you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency

Frequency of the generated RF signal. This value is expressed in hertz.

For arbitrary waveform generation, this input specifies the center frequency of the signal.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### power level

Power level of the generated RF signal. This value is expressed in dBm.

This input specifies the average power of the signal when the Power Level Type property is set to Average Power, which is the default setting.

##### Configuring the Power Level for Varying Power

To configure the power level of a waveform with varying power, set the Power Level Type property to Peak Power.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Getting Started Single Tone Generation
- RFSG Frequency Sweep
- RFSG Configuration List Frequency and Power Sweep

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-signal-bandwidth.html language=enus -->
## TOPIC 00026: Configure Signal Bandwidth

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-signal-bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-signal-bandwidth.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the signal bandwidth of the arbitrary waveform. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input

Configure Signal Bandwidth

Configures the signal bandwidth of the arbitrary waveform.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### signal bandwidth

Signal bandwidth used by NI-RFSG for generating an RF output signal.

NI-RFSG

Signal Bandwidth

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Getting Started Script (Script)
- RFSG Arbitrary Waveform Generation (Arb)

#### NI-RFSG Signal Bandwidth Definition

NI-RFSG defines 
 *signal bandwidth* as twice the maximum baseband signal deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such cases, the signal bandwidth is the baseband signal's minimum frequency subtracted from its maximum frequency, or f<sub>max</sub> - f<sub>min</sub>. NI-RFSG uses this value to optimally configure the center frequency of the upconverter to help minimize phase noise. The generated signal is not filtered to achieve the set bandwidth. However, specifying a bandwidth smaller than the actual bandwidth of the signal could potentially result in spectral distortion.

Parent topic:

Arbitrary Waveform Generator Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-trigger-configuration-list-step-digital-edge.html language=enus -->
## TOPIC 00027: Digital Edge

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-trigger-configuration-list-step-digital-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-trigger-configuration-list-step-digital-edge.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the configuration list step trigger for digital edge triggering. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior D

Digital Edge

Configures the configuration list step trigger for digital edge triggering.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

Trigger source terminal for the digital edge configuration list step trigger.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### edge

Active edge for the digital edge configuration list step trigger.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5650/5651/5652/5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-trigger-configuration-list-step-none.html language=enus -->
## TOPIC 00028: None

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-trigger-configuration-list-step-none.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-trigger-configuration-list-step-none.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device not to receive triggers for the configuration list. The configuration list does not advance steps if this trigger is disabled. Call this node only if a previously configured trigger needs to be disabled. session in Instrument session obtained from Initialize With Options. error

None

Configures the device not to receive triggers for the configuration list.

The configuration list does not advance steps if this trigger is disabled. Call this node only if a previously configured trigger needs to be disabled.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5650/5651/5652/5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-trigger-script-digital-edge.html language=enus -->
## TOPIC 00029: Digital Edge

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-trigger-script-digital-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-trigger-script-digital-edge.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a specified Script Trigger for digital edge triggering. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to th

Digital Edge

Configures a specified Script Trigger for digital edge triggering.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

Trigger source terminal for the digital edge Script Trigger.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### edge

Active edge for the digital edge Script Trigger.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### trigger id

Script Trigger to configure.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-trigger-script-digital-level.html language=enus -->
## TOPIC 00030: Digital Level

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-trigger-script-digital-level.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-trigger-script-digital-level.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a specified Script Trigger for digital level triggering. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to t

Digital Level

Configures a specified Script Trigger for digital level triggering.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

Trigger source terminal for the digital level Script Trigger.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### level

Active level for the digital level Script Trigger.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### trigger id

Script Trigger to configure.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-trigger-script-none.html language=enus -->
## TOPIC 00031: None

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-trigger-script-none.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-trigger-script-none.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device not to wait for the specified Script Trigger. Call this node only if you previously configured a Script Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained from Initialize With

None

Configures the device not to wait for the specified Script Trigger.

Call this node only if you previously configured a Script Trigger and now want it disabled.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### trigger id

Script Trigger to configure.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-trigger-script-software.html language=enus -->
## TOPIC 00032: Software

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-trigger-script-software.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-trigger-script-software.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a specified Script Trigger for software triggering. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this i

Software

Configures a specified Script Trigger for software triggering.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### trigger id

Script Trigger to configure.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

#### Programming Patterns

Use 
 [Send Software Edge Trigger](send-software-edge-trigger.html) to assert the trigger.

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-trigger-start-digital-edge.html language=enus -->
## TOPIC 00033: Digital Edge

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-trigger-start-digital-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-trigger-start-digital-edge.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start Trigger for digital edge triggering. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input

Digital Edge

Configures the Start Trigger for digital edge triggering.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

Trigger source terminal for the digital edge Start Trigger.

##### Start Trigger Functionality During RF List Mode

PXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### edge

Active edge for the digital edge Start Trigger.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-trigger-start-none.html language=enus -->
## TOPIC 00034: None

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-trigger-start-none.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-trigger-start-none.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device not to wait for a Start Trigger. This node is necessary only if you previously configured a Start Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained from Initialize With Optio

None

Configures the device not to wait for a Start Trigger.

This node is necessary only if you previously configured a Start Trigger and now want it disabled.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-trigger-start-p2p-endpoint-fullness.html language=enus -->
## TOPIC 00035: P2P Endpoint Fullness

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-trigger-start-p2p-endpoint-fullness.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-trigger-start-p2p-endpoint-fullness.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start Trigger to detect peer-to-peer endpoint fullness. Generation begins when the number of samples in the peer-to-peer endpoint reaches the threshold specified by the level. Due to an additional internal FIFO in the RF analog signal generator, the writer peer actually writes 2,304 b

P2P Endpoint Fullness

Configures the Start Trigger to detect peer-to-peer endpoint fullness.

Generation begins when the number of samples in the peer-to-peer endpoint reaches the threshold specified by the level. Due to an additional internal FIFO in the RF analog signal generator, the writer peer actually writes 2,304 bytes more than the quantity of data specified by this node to satisfy the trigger level.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### level

Quantity of data in the FIFO endpoint that asserts the trigger in samples per second.

Default value: -1, which allows NI-RFSG to select the appropriate fullness value.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-trigger-start-software.html language=enus -->
## TOPIC 00036: Software

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-trigger-start-software.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-trigger-start-software.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start Trigger for software triggering. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input acco

Software

Configures the Start Trigger for software triggering.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

#### Programming Patterns

Use 
 [Send Software Edge Trigger](send-software-edge-trigger.html) to assert the trigger.

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=configure-trigger.html language=enus -->
## TOPIC 00037: Configure Trigger

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `configure-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/configure-trigger.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start, Script, and Configuration List Step Triggers.

Configure Trigger

Configures the Start, Script, and Configuration List Step Triggers.

Trigger Nodes

Parent topic:

Trigger Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=create-configuration-list-step.html language=enus -->
## TOPIC 00038: Create Configuration List Step

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `create-configuration-list-step.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/create-configuration-list-step.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new configuration list step in the configuration list specified by the Active Configuration List property. When you create a configuration list step, a new instance of each property specified by the configuration list properties is created. Configuration list properties are specified when

Create Configuration List Step

Creates a new configuration list step in the configuration list specified by the Active Configuration List property.

When you create a configuration list step, a new instance of each property specified by the configuration list properties is created. Configuration list properties are specified when a configuration list is created. The new instance of a property can be accessed with a property node using the Active Configuration List and Active Configuration List Step properties to index the desired instance of the property.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### set as active step

Boolean value that indicates whether this step is the active step for the active configuration list.

NI recommends that you keep this input set to True when creating the list steps.

| True | This step is the active step for the active configuration list. |
| --- | --- |
| False | The step is not the active step for the active configuration list. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5650/5651/5652/5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Configuration List Frequency and Power Sweep
- RFSG Configuration List Frequency and Power Sweep (Script Triggered)

Parent topic:

List Mode Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=create-configuration-list.html language=enus -->
## TOPIC 00039: Create Configuration List

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `create-configuration-list.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/create-configuration-list.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an empty configuration list. Calling this node allocates space for each of the configuration list properties. Use the Active Configuration List property to enable a configuration list created by this node. session in Instrument session obtained from Initialize With Options. error in Error co

Create Configuration List

Creates an empty configuration list.

Calling this node allocates space for each of the configuration list properties. Use the Active Configuration List property to enable a configuration list created by this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### list name

Name of the configuration list. This string is case-insensitive and alphanumeric, and it cannot contain spaces or use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/c1du32.png']

##### configuration list properties

Properties that you intend to change between configuration list steps.

##### Listable Configuration List Properties

You can include the following properties in your configuration list based on your device:

ALC Control

PXIe-5654

PXIe-5696

Amp Path

PXIe-5654

PXIe-5696

Amplitude Settling

PXIe-5654/5654

PXIe-5696

PXIe-5820/5840

Attenuator Setting (dB)

PXIe-5654

PXIe-5696

Automatic Power Search

PXIe-5650/5651/5652/5654

PXIe-5696

Digital Gain (dB)

PXIe-5644/5645/5646

PXIe-5820/5840

External Gain

PXIe-5820/5840

Frequency (Hz)

PXIe-5644/5645/5646

PXIe-5650/5651/5652/5653/5654/5654

PXIe-5696

PXIe-5673E

PXIe-5820/5840

Frequency Settling

PXIe-5650/5651/5652/5653/5654/5654

PXIe-5696

PXIe-5673E

IQ Out Port Carrier Frequency

PXIe-5645

PXIe-5654/5654

PXIe-5696

PXIe-5820

IQ Out Port Common Mode Offset

PXIe-5645

PXIe-5654/5654

PXIe-5696

PXIe-5820

IQ Out Port Level

PXIe-5645

PXIe-5654

PXIe-5696

PXIe-5820

IQ Out Port Offset

PXIe-5645

PXIe-5654

PXIe-5696

PXIe-5820

Output Enabled

PXIe-5654/5654

PXIe-5696

Phase Offset (Degrees)

PXIe-5644/5645/5646

PXIe-5650/5651/5652/5653

PXIe-5673E

PXIe-5820/5840

Power Level (dBm)

PXIe-5644/5645/5646

PXIe-5650/5651/5652/5654/5654

PXIe-5696

PXIe-5673E

PXIe-5840

Pre-filter Gain (dB)

PXIe-5820/5840

Pulse Modulation Enabled

PXIe-5654/5654

PXIe-5696

PXIe-5673E

Signal Bandwidth (Hz)

PXIe-5820/5840

Timer Event Interval (s)

PXIe-5644/5645/5646

PXIe-5650/5651/5652/5654/5654

PXIe-5696

PXIe-5673E

PXIe-5820/5840

Upconverter Center Frequency (Hz)

PXIe-5644/5645/5646

PXIe-5673E

PXIe-5840

Upconverter Frequency Offset (Hz)

PXIe-5840

##### NI-RFSG Property Node Behavior

When you use the NI-RFSG Property Node to set one of the configuration list properties, that property is set as one of the configuration list steps. Use the Active Configuration List Step property to specify which configuration list step to configure.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### set as active list

Boolean value that indicates whether the configuration list is active.

NI recommends that you set this input to True when creating the list.

| True | This configuration list is the active configuration list. |
| --- | --- |
| False | This configuration list is not the active configuration list. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5650/5651/5652/5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Configuration List Frequency and Power Sweep
- RFSG Configuration List Frequency and Power Sweep (Script Triggered)
- RFSG Configuration List Frequency and Power Sweep (Timer Triggered)

#### Programming Patterns

Call 
 [Create Configuration List Step](create-configuration-list-step.html) to add steps to the configuration list.

Parent topic:

List Mode Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=delete-configuration-list.html language=enus -->
## TOPIC 00040: Delete Configuration List

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `delete-configuration-list.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/delete-configuration-list.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes a previously created configuration list and all the configuration list steps in the configuration list. When a configuration list step is deleted, all the instances of the properties associated with the configuration list step are also removed. When you delete the active configuration list,

Delete Configuration List

Deletes a previously created configuration list and all the configuration list steps in the configuration list. When a configuration list step is deleted, all the instances of the properties associated with the configuration list step are also removed. When you delete the active configuration list, NI-RFSG automatically resets the Active Configuration List property to "" (empty string), which indicates no list is active, and the Active Configuration List Step property to 0.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### list name

Name of the configuration list. This string is case-insensitive and alphanumeric, and it cannot contain spaces or use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

List Mode Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=error-message.html language=enus -->
## TOPIC 00041: Error Message

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `error-message.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/error-message.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an error code returned by an NI-RFSG node into a user-readable string. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavi

Error Message

Converts an error code returned by an NI-RFSG node into a user-readable string.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### error code

Error code returned from any NI-RFSG node.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### error message

User-readable message string that corresponds to the error code you specify.

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=export-signal.html language=enus -->
## TOPIC 00042: Export Signal

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `export-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/export-signal.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes signals (triggers, clocks, and events) to a specified output terminal. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node res

Export Signal

Routes signals (triggers, clocks, and events) to a specified output terminal.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### signal

Type of signal to route.

| Start Trigger | Exports a Start Trigger. |
| --- | --- |
| Script Trigger | Exports a Script Trigger. |
| Marker Event | Exports a Marker Event. |
| Ref Clock | Routes the onboard 10 MHz synchronization clock (PXI chassis only). |
| Started Event | Exports a Started Event. |
| Done Event | Exports a Done Event. |
| Configuration List Step Trigger | Exports a Configuration List Step Trigger. |
| Configuration Settled Event | Exports a Configuration Settled Event. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### signal identifier

Script Trigger or Marker Event to configure.

signal

Script Trigger

Marker Event

None

| scriptTrigger0 | Specifies Script Trigger 0. |
| --- | --- |
| scriptTrigger1 | Specifies Script Trigger 1. |
| scriptTrigger2 | Specifies Script Trigger 2. |
| scriptTrigger3 | Specifies Script Trigger 3. |
| marker0 | Specifies Marker 0. |
| marker1 | Specifies Marker 1. |
| marker2 | Specifies Marker 2. |
| marker3 | Specifies Marker 3. |
| None | Does not export a signal. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### output terminal

Terminal where the signal is exported.

You can choose not to export any signal.

| Do not export signal | Does not export a signal. |
| --- | --- |
| RefOut | Exports a signal to the REF OUT terminal. |
| RefOut2 | Exports a signal to the REF OUT2 terminal. |
| ClkOut | Exports a signal to the CLKOUT terminal. |
| PFI0 | Exports a signal to the PFI 0 terminal. |
| PFI1 | Exports a signal to the PFI 1 terminal. |
| PFI4 | Exports a signal to the PFI 4 terminal. |
| PFI5 | Exports a signal to the PFI 5 terminal. |
| PXI_TRIG0 | Exports a signal to the PXI trigger line 0 terminal. |
| PXI_TRIG1 | Exports a signal to the PXI trigger line 1 terminal. |
| PXI_TRIG2 | Exports a signal to the PXI trigger line 2 terminal. |
| PXI_TRIG3 | Exports a signal to the PXI trigger line 3 terminal. |
| PXI_TRIG4 | Exports a signal to the PXI trigger line 4 terminal. |
| PXI_TRIG5 | Exports a signal to the PXI trigger line 5 terminal. |
| PXI_TRIG6 | Exports a signal to the PXI trigger line 6 terminal. |
| PXI_Star | Exports a signal to the PXI star trigger line terminal. |
| PXIe_DStarC | Exports a signal to the PXIe DStar C trigger line terminal. This value is supported on only the PXIe-5820/5840. |
| TrigOut | Exports a signal to the TRIG IN/OUT terminal. |

##### Signal Exporting Behavior

If you export a signal with this node and commit the session with 
 [Commit](commit.html), the signal is routed to the output terminal you specify. If you then reconfigure the signal to have a different output terminal, the previous output terminal is tristated when the session is next committed. If you change the output terminal to Do Not Export and commit the session, the previous output terminal is tristated.

Any signals exported within a session persist after the session closes to prevent signal glitches between sessions. If you want to tristate the exported output terminal that the signal was exported to when the session closes, first change the value of the output terminal for the exported signal to Do Not Export, and then commit the session again before closing it.

You can also tristate all PFI lines by setting the reset device input within 
 [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Export Start Trigger
- RFSG Marker Events

Parent topic:

Trigger Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=external-calibration-nodes.html language=enus -->
## TOPIC 00043: External Calibration Nodes

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `external-calibration-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/external-calibration-nodes.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

External Calibration Nodes

Calibration Nodes

Initialize External Calibration

NI-RFSG

Close External Calibration

Writes the calibration values from the current driver session to the device.

Get External Calibration Last Date and Time

Returns the date and time of the last successful external calibration.

Change External Calibration Password

Changes the external calibration password of the device.

Update External Calibration Temperature

Updates the temperature of the last external calibration to the current temperature.

Parent topic:

Calibration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=get-external-calibration-last-date-and-time.html language=enus -->
## TOPIC 00044: Get External Calibration Last Date and Time

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `get-external-calibration-last-date-and-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/get-external-calibration-last-date-and-time.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time. session in Instrument session obtained from Initialize External Calibration. error in Error conditions that occur before this node runs. The node responds to this input accordin

Get External Calibration Last Date and Time

Returns the date and time of the last successful external calibration.

The time returned is 24-hour (military) local time.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize External Calibration](initialize-external-calibration.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### last external calibration date and time

Date and time of the last successful external calibration.

##### Example Date and Time Format

If the device was calibrated at 2:30 PM, this output returns 
 14 for the hours and 
 30 for the minutes.

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654
- PXIe-5673E
- PXIe-5696
- PXIe-5820/5840

Parent topic:

External Calibration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=get-ni-tclk-session-reference.html language=enus -->
## TOPIC 00045: Get NI-TClk Session Reference

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `get-ni-tclk-session-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/get-ni-tclk-session-reference.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts a session that can be passed to NI-TClk nodes. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No err

Get NI-TClk Session Reference

Extracts a session that can be passed to NI-TClk nodes.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### session reference

Reference to the device session that can be passed to NI-TClk nodes.

Session references are of generic data type, which means that the corresponding wires are blue-green, unlike the wires for regular instrument driver sessions.

#### Hardware Support

This node supports the following hardware:

- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG 5673 Synchronization (TClk, Shared LO)

Parent topic:

Trigger Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=get-self-calibration-date-and-time.html language=enus -->
## TOPIC 00046: Get Self Calibration Date and Time

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `get-self-calibration-date-and-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/get-self-calibration-date-and-time.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time of the last successful self-calibration. The time returned is 24-hour (military) local time. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standar

Get Self Calibration Date and Time

Returns the date and time of the last successful self-calibration.

The time returned is 24-hour (military) local time.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### module

Module from which to retrieve the last successful self-calibration date and time.

| Primary Module | The stand-alone device or the main module in a multi-module device. |
| --- | --- |
| AWG | The AWG associated with the primary module. |
| LO | The LO associated with the primary module. |

Default value: 
 Primary Module

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### self calibration date and time

Date and time of the last successful self-calibration.

##### Example Date and Time Format

If the device was calibrated at 2:30 PM, this output returns 
 14 for the hours and 
 30 for the minutes.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5653
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Calibration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=get-self-calibration-temperature.html language=enus -->
## TOPIC 00047: Get Self Calibration Temperature

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `get-self-calibration-temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/get-self-calibration-temperature.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. S

Get Self Calibration Temperature

Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### module

Module from which to retrieve the last successful self-calibration temperature.

| Primary Module | The stand-alone device or the main module in a multi-module device. |
| --- | --- |
| AWG | The AWG associated with the primary module. |
| LO | The LO associated with the primary module. |

Default value: 
 Primary Module

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### self calibration temperature

Temperature, in degrees Celsius, of the device at the last successful self-calibration.

#### Hardware Support

This node supports the following hardware:

- PXIe-5653
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Calibration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=get-stream-endpoint-handle.html language=enus -->
## TOPIC 00048: Get Stream Endpoint Handle

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `get-stream-endpoint-handle.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/get-stream-endpoint-handle.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a reader endpoint handle that can be used with NI-P2P to configure a peer-to-peer stream with an RF signal generator endpoint. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input acco

Get Stream Endpoint Handle

Returns a reader endpoint handle that can be used with NI-P2P to configure a peer-to-peer stream with an RF signal generator endpoint.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### stream endpoint

Stream resources to use.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### reader handle

Reader endpoint handle that is used with NI-P2P to create a stream with the NI-RFSG device as an endpoint.

#### Hardware Support

This node supports the following hardware:

- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=get-terminal-name.html language=enus -->
## TOPIC 00049: Get Terminal Name

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `get-terminal-name.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/get-terminal-name.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully-qualified name of the specified signal. The fully-qualified signal name is helpful when you want to automatically route signals in a multi-segment chassis. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node run

Get Terminal Name

Returns the fully-qualified name of the specified signal.

The fully-qualified signal name is helpful when you want to automatically route signals in a multi-segment chassis.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### signal

Signal to query.

| Start Trigger | Queries the Start Trigger. |
| --- | --- |
| Script Trigger | Queries a Script Trigger. |
| Marker Event | Queries a Marker Event. |
| Ref Clock | Queries the Reference Clock. |
| Started Event | Queries the Started Event. |
| Done Event | Queries the Done Event. |
| Configuration List Step Trigger | Queries the Configuration List Step Trigger. |
| Configuration Settled Event | Queries the Configuration Settled Event. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### signal identifier

Script Trigger or Marker Event to configure.

signal

Script Trigger

Marker Event

None

| scriptTrigger0 | Specifies Script Trigger 0. |
| --- | --- |
| scriptTrigger1 | Specifies Script Trigger 1. |
| scriptTrigger2 | Specifies Script Trigger 2. |
| scriptTrigger3 | Specifies Script Trigger 3. |
| marker0 | Specifies Marker 0. |
| marker1 | Specifies Marker 1. |
| marker2 | Specifies Marker 2. |
| marker3 | Specifies Marker 3. |
| None | Does not export a signal. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### terminal name

Fully-qualified string.

#### Hardware Support

This node supports the following hardware:

- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Trigger Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=initialize-external-calibration.html language=enus -->
## TOPIC 00050: Initialize External Calibration

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `initialize-external-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/initialize-external-calibration.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates and initializes an NI-RFSG external calibration session. resource name Resource name of the device to initialize. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error

Initialize External Calibration

Creates and initializes an NI-RFSG external calibration session.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### resource name

Resource name of the device to initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### password

Calibration password required to open an external calibration session to the device.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### option string

Initial value of certain properties for the session.

You can set the following properties using this input:

- Range Check
- Query Instrument Status
- Cache
- Coercions
- Simulate
- Driver Setup

##### Option String Syntax

The syntax for option string consists of the following relations:

propertyName=value

where

- propertyName is the name of the property.
- value is the value to which the property is set.

##### Syntax for Setting Multiple Properties

To set multiple properties, separate their assignments with a comma, as shown in the following option string:

"RangeCheck=1, QueryInstrStatus=0, Cache=1, DriverSetup=AWG:pxi1slot4"

##### Configuring the Driver Setup String

1. Use the Driver Setup keyword in the option string to complete the following tasks:
  - Specify your hardware device or external (non-National Instruments) device
  - Simulate hardware that is not present
  - Specify an NI-RFSG instrument driver FPGA extensions bitfile 
 org.dita.html5/xsl/topic.xsl 455 Note Specifying an AE, AWG, or LO module in the Driver Setup string overrides any different existing association configured in MAX.
2. Use the following format when configuring the Driver Setup string: 
 Tag:Value
3. When specifying or simulating multiple devices, separate them with a semicolon, as shown in the following string: 
 DriverSetup=AWG:pxi1slot4; LO:pxi1slot7

| Use | Example Driver Setup String | Supported Devices |
| --- | --- | --- |
| Specify an Amplitude Extender (AE) | DriverSetup=AE:Dev1 | PXIe-5654/5654 with PXIe-5696 |
| Specify a Waveform Generator (AWG) | DriverSetup=AWG:Dev1 | PXIe-5611, PXIe-5673E |
| Specify an external AWG | DriverSetup=AWG:<external> |  |
| Specify a local oscillator (LO) | DriverSetup=LO:Dev1 |  |
| Specify an external LO | DriverSetup=LO:<external> | PXIe-5611, PXIe-5644/5645/5646, PXIe-5673E, PXIe-5840 |
| Specify an NI-RFSG instrument driver FPGA extensions bitfile | DriverSetup=Bitfile:filename.lvbitx | PXIe-5644/5645/5646, PXIe-5820/5840 |
| Simulate a device | DriverSetup=Model:model number; BoardType:type | Refer to Simulating an NI-RFSG Device for more information about supported devices. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5696

Parent topic:

External Calibration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=initialize-with-options.html language=enus -->
## TOPIC 00051: Initialize With Options

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `initialize-with-options.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/initialize-with-options.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a session for the supported hardware you specify, sets initial values of certain properties for the session, and returns a reference that identifies the instrument in all subsequent NI-RFSG nodes. resource name Resource name of the device to initialize. error in Error conditions that occur bef

Initialize With Options

Opens a session for the supported hardware you specify, sets initial values of certain properties for the session, and returns a reference that identifies the instrument in all subsequent NI-RFSG nodes.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### resource name

Resource name of the device to initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### option string

Initial value of certain properties for the session.

You can set the following properties using this input:

- Range Check
- Query Instrument Status
- Cache
- Coercions
- Simulate
- Driver Setup

##### Option String Syntax

The syntax for option string consists of the following relations:

propertyName=value

where

- propertyName is the name of the property.
- value is the value to which the property is set.

##### Syntax for Setting Multiple Properties

To set multiple properties, separate their assignments with a comma, as shown in the following option string:

"RangeCheck=1, QueryInstrStatus=0, Cache=1, DriverSetup=AWG:pxi1slot4"

##### Configuring the Driver Setup String

1. Use the Driver Setup keyword in the option string to complete the following tasks:
  - Specify your hardware device or external (non-National Instruments) device
  - Simulate hardware that is not present
  - Specify an NI-RFSG instrument driver FPGA extensions bitfile 
 org.dita.html5/xsl/topic.xsl 455 Note Specifying an AE, AWG, or LO module in the Driver Setup string overrides any different existing association configured in MAX.
2. Use the following format when configuring the Driver Setup string: 
 Tag:Value
3. When specifying or simulating multiple devices, separate them with a semicolon, as shown in the following string: 
 DriverSetup=AWG:pxi1slot4; LO:pxi1slot7

| Use | Example Driver Setup String | Supported Devices |
| --- | --- | --- |
| Specify an Amplitude Extender (AE) | DriverSetup=AE:Dev1 | PXIe-5654/5654 with PXIe-5696 |
| Specify a Waveform Generator (AWG) | DriverSetup=AWG:Dev1 | PXIe-5611, PXIe-5673E |
| Specify an external AWG | DriverSetup=AWG:<external> |  |
| Specify a local oscillator (LO) | DriverSetup=LO:Dev1 |  |
| Specify an external LO | DriverSetup=LO:<external> | PXIe-5611, PXIe-5644/5645/5646, PXIe-5673E, PXIe-5840 |
| Specify an NI-RFSG instrument driver FPGA extensions bitfile | DriverSetup=Bitfile:filename.lvbitx | PXIe-5644/5645/5646, PXIe-5820/5840 |
| Simulate a device | DriverSetup=Model:model number; BoardType:type | Refer to Simulating an NI-RFSG Device for more information about supported devices. |

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### id query

Boolean value that indicates whether NI-RFSG performs an ID query.

| True | NI-RFSG performs an ID query. |
| --- | --- |
| False | NI-RFSG does not perform an ID query. |

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

Boolean value that indicates whether the NI-RFSG device is reset during the initialization procedure.

| True | The device is reset. |
| --- | --- |
| False | The device is not reset. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

NI-RFSG Nodes

Related information:

- Simulating an NI-RFSG Device

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=initiate.html language=enus -->
## TOPIC 00052: Initiate

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `initiate.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/initiate.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates signal generation, causing the NI-RFSG device to leave the Configuration state or Committed state and enter the Generation state. If settings have not been committed to the device before you use this node, they are committed by this node. The operation returns when the RF output signal set

Initiate

Initiates signal generation, causing the NI-RFSG device to leave the Configuration state or Committed state and enter the Generation state.

If settings have not been committed to the device before you use this node, they are committed by this node. The operation returns when the RF output signal settles. To return to the Configuration state, use 
 [Abort](abort.html).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXI-5611
- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Getting Started Single Tone Generation
- RFSG Arbitrary Waveform Generation (Arb)
- RFSG Getting Started Script (Script)

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=list-mode-nodes.html language=enus -->
## TOPIC 00053: List Mode Nodes

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `list-mode-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/list-mode-nodes.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

List Mode Nodes

Configuration Nodes

Create Configuration List

Creates an empty configuration list.

Create Configuration List Step

Creates a new configuration list step in the configuration list specified by the Active Configuration List property.

Delete Configuration List

Deletes a previously created configuration list and all the configuration list steps in the configuration list.

Check If Configuration List Exists

Returns whether the configuration list that you specify exists.

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=ni-rfsg-nodes.html language=enus -->
## TOPIC 00054: NI-RFSG Nodes

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `ni-rfsg-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/ni-rfsg-nodes.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

NI-RFSG Nodes

Initialize With Options

NI-RFSG

Close

Aborts any signal generation in progress and destroys the instrument driver session.

NI-RFSG Properties

NI-RFSG

Configuration Nodes

Action Nodes

Utility Nodes

Calibration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=ni-rfsg-properties.html language=enus -->
## TOPIC 00055: NI-RFSG Properties

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `ni-rfsg-properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/ni-rfsg-properties.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads), sets (writes), or resets (sets to default value) NI-RFSG properties. When you read a property, NI-RFSG analyzes the current configuration to return the coerced value for that property. NI-RFSG verifies many properties upon reading, thereby either transitioning the session to the verifi

NI-RFSG Properties

Gets (reads), sets (writes), or resets (sets to default value) NI-RFSG properties.

When you read a property, NI-RFSG analyzes the current configuration to return the coerced value for that property. NI-RFSG verifies many properties upon reading, thereby either transitioning the session to the verified state or alerting you of an invalid configuration. Setting or resetting a property transitions the session to an unverified state.

For a list of supported properties, refer to NI-RFSG Properties.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### NI-RFSG in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### NI-RFSG out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

NI-RFSG Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=perform-power-search.html language=enus -->
## TOPIC 00056: Perform Power Search

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `perform-power-search.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/perform-power-search.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a power search if the ALC Control property is disabled. Calling this node disables modulation for a short time while the device levels the output signal. Power search temporarily enables the ALC, so ensure the appropriate included cable is connected between the PXIe-5654 ALC IN connector an

Perform Power Search

Performs a power search if the ALC Control property is disabled.

Calling this node disables modulation for a short time while the device levels the output signal.

Note

PXIe-5654

PXIe-5696

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5654 with PXIe-5696

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=perform-thermal-correction.html language=enus -->
## TOPIC 00057: Perform Thermal Correction

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `perform-thermal-correction.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/perform-thermal-correction.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Corrects for any signal drift due to temperature variation when generating the same signal for extended periods of time without a parameter change. Under normal circumstances of short-term signal generation, NI-RFSG performs thermal correction automatically by ensuring stable power levels, and you d

Perform Thermal Correction

Corrects for any signal drift due to temperature variation when generating the same signal for extended periods of time without a parameter change.

Under normal circumstances of short-term signal generation, NI-RFSG performs thermal correction automatically by ensuring stable power levels, and you do not need to call this node. Use this node when generating the same signal for a long period of time in a temperature-fluctuating environment.

The NI-RFSG device must be in the Generation state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Thermal Correction

Parent topic:

Calibration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=query-arbitrary-waveform-capabilities.html language=enus -->
## TOPIC 00058: Query Arbitrary Waveform Capabilities

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `query-arbitrary-waveform-capabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/query-arbitrary-waveform-capabilities.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries and returns the device arbitrary waveform capabilities, which are related to the current device configuration. The NI-RFSG device must be in the Configuration or Generation state before you call this node. session in Instrument session obtained from Initialize With Options. error in Error co

Query Arbitrary Waveform Capabilities

Queries and returns the device arbitrary waveform capabilities, which are related to the current device configuration.

The NI-RFSG device must be in the Configuration or Generation state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### waveform quantum

Quantum value the signal generator uses.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### maximum number of waveforms

Maximum number of arbitrary waveforms that you can write.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### maximum waveform size

Largest allowable waveform size.

The number of samples that you write must be less than or equal to this value.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### minimum waveform size

Smallest allowable waveform size.

The number of samples that you write must be greater than or equal to this value.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Configuration List Frequency and Power Sweep (Script Triggered)

Parent topic:

Arbitrary Waveform Generator Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=reset-device.html language=enus -->
## TOPIC 00059: Reset Device

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `reset-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/reset-device.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a hard reset on the device. A hard reset consists of the following actions: Signal generation is stopped. All routes are released. External bidirectional terminals are tristated. FPGAs are reset. Hardware is configured to its default state. All session properties are reset to their default

Reset Device

Performs a hard reset on the device.

A hard reset consists of the following actions:

- Signal generation is stopped.
- All routes are released.
- External bidirectional terminals are tristated.
- FPGAs are reset.
- Hardware is configured to its default state.
- All session properties are reset to their default states.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E

#### Signal Routing Behavior During a Device Reset

During a device reset, routes of signals between this and other devices are released, regardless of which device created the route. For example, a trigger signal exported to a PXI trigger line that is used by another device is no longer exported.

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=reset.html language=enus -->
## TOPIC 00060: Reset

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `reset.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/reset.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets all properties to their default values, aborts signal generation, clears all routes, and moves the NI-RFSG device to the Configuration state. During a reset, routes of signals between this and other devices are released, regardless of which device created the route. session in Instrument sess

Reset

Resets all properties to their default values, aborts signal generation, clears all routes, and moves the NI-RFSG device to the Configuration state.

During a reset, routes of signals between this and other devices are released, regardless of which device created the route.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=revision-query.html language=enus -->
## TOPIC 00061: Revision Query

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `revision-query.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/revision-query.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision numbers of the NI-RFSG driver and the instrument firmware. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavi

Revision Query

Returns the revision numbers of the NI-RFSG driver and the instrument firmware.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### instrument driver revision

Instrument driver software revision numbers in the form of a string.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### firmware revision

Instrument firmware revision numbers in the form of a string.

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=script-nodes.html language=enus -->
## TOPIC 00062: Script Nodes

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `script-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/script-nodes.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Script Nodes

Configuration Nodes

Write Script

Writes a script to the device to control waveform generation in Script mode.

Check If Script Exists

Returns whether the script that you specify exists.

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=select-arbitrary-waveform.html language=enus -->
## TOPIC 00063: Select Arbitrary Waveform

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `select-arbitrary-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/select-arbitrary-waveform.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the waveform that is generated. Before using this node, you must first configure your device for Arb Waveform generation mode by calling Configure Generation Mode. The NI-RFSG device must be in the Configuration state before you call this node. session in Instrument session obtained from I

Select Arbitrary Waveform

Specifies the waveform that is generated.

Before using this node, you must first configure your device for Arb Waveform generation mode by calling 
 [Configure Generation Mode](configure-generation-mode.html).

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

Name of the stored waveform to generate.

You must specify a waveform name if you have written multiple waveforms. This string is case-insensitive and alphanumeric, and it cannot use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Multiple Arbitrary Waveforms

Parent topic:

Arbitrary Waveform Generator Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=self-calibrate-range.html language=enus -->
## TOPIC 00064: Self Calibrate Range

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `self-calibrate-range.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/self-calibrate-range.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Self-calibrates all configurations within the specified frequency and peak power level limits. NI recommends that no external signals are present on the RF In or IQ In ports during the calibration. session in Instrument session obtained from Initialize With Options. error in Error conditions that oc

Self Calibrate Range

Self-calibrates all configurations within the specified frequency and peak power level limits.

NI recommends that no external signals are present on the RF In or IQ In ports during the calibration.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### steps to omit

Calibration steps to skip during the self-calibration process.

| LO Self Cal | Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted. |
| --- | --- |
| Power Level Accuracy | Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted. |
| Residual LO Power | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted. |
| Image Suppression | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted. |
| Synthesizer Alignment | Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted. |

Default value: The default value is an empty array, which specifies that all calibration steps are performed.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### min frequency

Minimum frequency to calibrate.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### max frequency

Maximum frequency to calibrate.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### min peak power level

Minimum power level to calibrate.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### max peak power level

Maximum power level to calibrate.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5820/5840

#### Recommendations for Best Results

For best results, NI recommends that you perform self-calibration without omitting any steps. However, if certain aspects of performance are less important for your application, you can omit certain steps for faster calibration.

#### Open NI-RFSA Sessions

If there is an existing NI-RFSA session open for the same PXIe-5644/5645/5646, it may remain open but cannot be used while this node runs.

If there is an existing NI-RFSA session open for the same PXIe-5820/5840 while this node runs, it may remain open but cannot be used for operations that access the hardware, for example NI-RFSA Commit or NI-RFSAInitiate.

#### Clearing Data

You can clear the self calibration range data by calling the [Clear Self Calibrate Range](clear-self-calibrate-range.html) or by restarting the system.

Parent topic:

Calibration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=self-calibration.html language=enus -->
## TOPIC 00065: Self Calibration

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `self-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/self-calibration.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs an internal self-calibration on the device and associated modules that support self-calibration. If the calibration is successful, new calibration data and constants are stored in the onboard nonvolatile memory of the module. session in Instrument session obtained from Initialize With Optio

Self Calibration

Performs an internal self-calibration on the device and associated modules that support self-calibration.

If the calibration is successful, new calibration data and constants are stored in the onboard nonvolatile memory of the module.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5653
- PXIe-5673E
- PXIe-5820/5840

#### Open NI-RFSA Session for the PXIe-5820/5840

If there is an existing NI-RFSA session open for the same PXIe-5820/5840 while this node runs, it may remain open but cannot be used for operations that access the hardware, for example NI-RFSACommit or NI-RFSAInitiate.

Parent topic:

Calibration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=self-test.html language=enus -->
## TOPIC 00066: Self Test

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `self-test.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/self-test.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a self-test on the NI-RFSG device and returns the test results. This node performs a simple series of tests to determine whether the NI-RFSG device is powered up and responding. This node does not affect external I/O connections or connections between devices. Complete functional testing an

Self Test

Performs a self-test on the NI-RFSG device and returns the test results.

This node performs a simple series of tests to determine whether the NI-RFSG device is powered up and responding. This node does not affect external I/O connections or connections between devices. Complete functional testing and calibration are not performed by this node.

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### self test result

Value returned from the device self-test.

##### Self Test Result Values

A value of 0 indicates that the device is powered on and responding.

A value of 1 indicates that the device failed the self test.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### self test message

Self-test response string from the NI-RFSG device.

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=send-software-edge-trigger.html language=enus -->
## TOPIC 00067: Send Software Edge Trigger

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `send-software-edge-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/send-software-edge-trigger.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Forces a trigger to occur. The specified trigger generates regardless of whether the trigger has been configured as a software trigger. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input acc

Send Software Edge Trigger

Forces a trigger to occur.

The specified trigger generates regardless of whether the trigger has been configured as a software trigger.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### trigger type

Type of trigger to send.

NI-RFSG can send a Start Trigger or a Script Trigger.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### trigger ID

Script Trigger to configure.

trigger type

Script Trigger

| scriptTrigger0 | Specifies Script Trigger 0. |
| --- | --- |
| scriptTrigger1 | Specifies Script Trigger 1. |
| scriptTrigger2 | Specifies Script Trigger 2. |
| scriptTrigger3 | Specifies Script Trigger 3. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Single Tone Generation with Start Trigger
- RFSG Scripting with Triggers

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=set-arbitrary-waveform-next-write-position.html language=enus -->
## TOPIC 00068: Set Arbitrary Waveform Next Write Position

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `set-arbitrary-waveform-next-write-position.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/set-arbitrary-waveform-next-write-position.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the start position to use for writing a waveform before calling Write Arbitrary Waveform. This node allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the name input of Allocate Arbitrary Waveform or Wri

Set Arbitrary Waveform Next Write Position

Configures the start position to use for writing a waveform before calling 
[Write Arbitrary Waveform](write-arb-waveform.html).

This node allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the name input of 
 [Allocate Arbitrary Waveform](allocate-arbitrary-waveform.html) or Write Arbitrary Waveform. Subsequent writes to that waveform begin where the last write ended, unless this node is called again.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### relative to

Reference position in the waveform.

The position and offset together determine where to start loading data into the waveform.

| Start of Waveform | 0 | The reference position is relative to the start of the waveform. |
| --- | --- | --- |
| Current Position | 1 | The reference position is relative to the current position. |

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### offset

Offset from the relative to input at which to start loading the data into the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

Name of the waveform.

This string is case-insensitive and alphanumeric, and it cannot use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5820/5840

Parent topic:

Arbitrary Waveform Generator Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=trigger-nodes.html language=enus -->
## TOPIC 00069: Trigger Nodes

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `trigger-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/trigger-nodes.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Trigger Nodes

Configuration Nodes

Configure Trigger

Configures the Start, Script, and Configuration List Step Triggers.

Get Terminal Name

Returns the fully-qualified name of the specified signal.

Get NI-TClk Session Reference

NI-TClk

Export Signal

Routes signals (triggers, clocks, and events) to a specified output terminal.

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=update-external-calibration-temperature.html language=enus -->
## TOPIC 00070: Update External Calibration Temperature

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `update-external-calibration-temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/update-external-calibration-temperature.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates the temperature of the last external calibration to the current temperature. session in Instrument session obtained from Initialize External Calibration. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard

Update External Calibration Temperature

Updates the temperature of the last external calibration to the current temperature.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize External Calibration](initialize-external-calibration.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5653/5654
- PXIe-5696

Parent topic:

External Calibration Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=utility-nodes.html language=enus -->
## TOPIC 00071: Utility Nodes

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `utility-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/utility-nodes.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Utility Nodes

NI-RFSG Nodes

Reset

NI-RFSG

Reset Device

Performs a hard reset on the device.

Self Test

NI-RFSG

Error Message

NI-RFSG

Revision Query

NI-RFSG

Get Stream Endpoint Handle

Returns a reader endpoint handle that can be used with NI-P2P to configure a peer-to-peer stream with an RF signal generator endpoint.

Write P2P Endpoint (I16)

Writes an array of 16-bit integer data to the peer-to-peer endpoint.

Parent topic:

NI-RFSG Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=wait-until-settled.html language=enus -->
## TOPIC 00072: Wait Until Settled

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `wait-until-settled.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/wait-until-settled.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the RF output signal settles. This node is useful for devices that support changes while in the Generation state. Call this node after making a dynamic change to wait for the output signal to settle. You can also call this node after calling Commit to wait for changes to settle. Wait Unt

Wait Until Settled

Waits until the RF output signal settles.

This node is useful for devices that support changes while in the Generation state. Call this node after making a dynamic change to wait for the output signal to settle. You can also call this node after calling 
 [Commit](commit.html) to wait for changes to settle. Wait Until Settled is not required after calling 
 [Initiate](initiate.html) because Initiate automatically waits for the output to settle.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### max time

Maximum time the node waits for the output to settle.

If the maximum time is exceeded, this node returns an error.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5611
- PXIe-5644/5645/5646
- PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Frequency Sweep (565x and 5673)
- RFSG Forward Frequency Sweep (5673 In-band Retuning)

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=write-arb-waveform-complex-dbl-cluster.html language=enus -->
## TOPIC 00073: Complex DBL Cluster

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `write-arb-waveform-complex-dbl-cluster.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/write-arb-waveform-complex-dbl-cluster.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the NI-RFSG device. This node accepts the complex baseband signal data in the form of a complex cluster. When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state. session in Instrument session obtained from Initialize With O

Complex DBL Cluster

Writes an arbitrary waveform to the NI-RFSG device.

This node accepts the complex baseband signal data in the form of a complex cluster.

When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### IQ waveform

Complex baseband signal to write to the NI-RFSG device.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the acquired Y array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between the samples in the acquired Y array. dt is the reciprocal of the I/Q rate.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### Y

Array of complex-valued time domain data.

The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### use waveform dt for IQ rate?

Boolean value that indicates whether the node uses the waveform dt to configure the I/Q rate.

| True | Uses the waveform dt to configure the I/Q rate |
| --- | --- |
| False | Does not use the waveform dt to configure the I/Q rate. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

Name used to store the waveform.

This string is case-insensitive and alphanumeric, and it cannot use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### more data pending?

Boolean value that indicates whether the data block contains the end of the waveform.

| True | Allows the data to be appended to the waveform later. |
| --- | --- |
| False | This data block contains the end of the waveform. |

Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. You can append data to a previously written waveform by using the saved waveform name.

Note

PXIe-5644/5645/5646/5673E/5820/5840

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Write Arbitrary Waveform

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=write-arb-waveform-complex-dbl-waveform.html language=enus -->
## TOPIC 00074: Complex DBL Waveform

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `write-arb-waveform-complex-dbl-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/write-arb-waveform-complex-dbl-waveform.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the NI-RFSG device. This node accepts the complex baseband data in the form of complex waveform data type. When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state. session in Instrument session obtained from Initialize With

Complex DBL Waveform

Writes an arbitrary waveform to the NI-RFSG device.

This node accepts the complex baseband data in the form of complex waveform data type.

When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### IQ waveform

Complex waveform to write to the NI-RFSG device.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### use waveform dt for IQ rate?

Boolean value that indicates whether the node uses the waveform dt to configure the I/Q rate.

| True | Uses the waveform dt to configure the I/Q rate |
| --- | --- |
| False | Does not use the waveform dt to configure the I/Q rate. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

Name used to store the waveform.

This string is case-insensitive and alphanumeric, and it cannot use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### more data pending?

Boolean value that indicates whether the data block contains the end of the waveform.

| True | Allows the data to be appended to the waveform later. |
| --- | --- |
| False | This data block contains the end of the waveform. |

Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. You can append data to a previously written waveform by using the saved waveform name.

Note

PXIe-5644/5645/5646/5673E/5820/5840

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Write Arbitrary Waveform

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=write-arb-waveform-complex-dbl.html language=enus -->
## TOPIC 00075: Complex DBL

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `write-arb-waveform-complex-dbl.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/write-arb-waveform-complex-dbl.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the NI-RFSG device. This node accepts the complex baseband data in the form of complex double data type. When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state. session in Instrument session obtained from Initialize With O

Complex DBL

Writes an arbitrary waveform to the NI-RFSG device.

This node accepts the complex baseband data in the form of complex double data type.

When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1dcdb.png']

##### waveform data

Array of data to load into the waveform.

You must normalize the data points in the array to have polar magnitudes between 0.0 and +1.00.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

Name used to store the waveform.

This string is case-insensitive and alphanumeric, and it cannot use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### more data pending?

Boolean value that indicates whether the data block contains the end of the waveform.

| True | Allows the data to be appended to the waveform later. |
| --- | --- |
| False | This data block contains the end of the waveform. |

Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. You can append data to a previously written waveform by using the saved waveform name.

Note

PXIe-5644/5645/5646/5673E/5820/5840

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Write Arbitrary Waveform

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=write-arb-waveform-complex-sgl-cluster.html language=enus -->
## TOPIC 00076: Complex SGL Cluster

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `write-arb-waveform-complex-sgl-cluster.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/write-arb-waveform-complex-sgl-cluster.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the NI-RFSG device. This node accepts the complex baseband signal data in the form of a complex cluster. When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state. session in Instrument session obtained from Initialize With O

Complex SGL Cluster

Writes an arbitrary waveform to the NI-RFSG device.

This node accepts the complex baseband signal data in the form of a complex cluster.

When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### IQ waveform

Complex baseband signal to write to the NI-RFSG device.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### t0

Trigger (start) time of the acquired Y array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### dt

Time interval between the samples in the acquired Y array. dt is the reciprocal of the I/Q rate.

[IMAGE alt='datatype_icon' src='/assets/img/c1dcsg.png']

##### Y

Array of complex-valued time domain data.

The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### use waveform dt for IQ rate?

Boolean value that indicates whether the node uses the waveform dt to configure the I/Q rate.

| True | Uses the waveform dt to configure the I/Q rate |
| --- | --- |
| False | Does not use the waveform dt to configure the I/Q rate. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

Name used to store the waveform.

This string is case-insensitive and alphanumeric, and it cannot use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### more data pending?

Boolean value that indicates whether the data block contains the end of the waveform.

| True | Allows the data to be appended to the waveform later. |
| --- | --- |
| False | This data block contains the end of the waveform. |

Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. You can append data to a previously written waveform by using the saved waveform name.

Note

PXIe-5644/5645/5646/5673E/5820/5840

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Write Arbitrary Waveform

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=write-arb-waveform-complex-sgl-waveform.html language=enus -->
## TOPIC 00077: Complex SGL Waveform

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `write-arb-waveform-complex-sgl-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/write-arb-waveform-complex-sgl-waveform.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the NI-RFSG device. This node accepts the complex baseband data in the form of complex waveform data type consisting of singles. When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state. session in Instrument session obtaine

Complex SGL Waveform

Writes an arbitrary waveform to the NI-RFSG device.

This node accepts the complex baseband data in the form of complex waveform data type consisting of singles.

When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### IQ waveform

Complex waveform to write to the NI-RFSG device.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### use waveform dt for IQ rate?

Boolean value that indicates whether the node uses the waveform dt to configure the I/Q rate.

| True | Uses the waveform dt to configure the I/Q rate |
| --- | --- |
| False | Does not use the waveform dt to configure the I/Q rate. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

Name used to store the waveform.

This string is case-insensitive and alphanumeric, and it cannot use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### more data pending?

Boolean value that indicates whether the data block contains the end of the waveform.

| True | Allows the data to be appended to the waveform later. |
| --- | --- |
| False | This data block contains the end of the waveform. |

Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. You can append data to a previously written waveform by using the saved waveform name.

Note

PXIe-5644/5645/5646/5673E/5820/5840

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Write Arbitrary Waveform

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=write-arb-waveform-complex-sgl.html language=enus -->
## TOPIC 00078: Complex SGL

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `write-arb-waveform-complex-sgl.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/write-arb-waveform-complex-sgl.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the NI-RFSG device. This node accepts the complex baseband data in the form of complex single data type. When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state. session in Instrument session obtained from Initialize With O

Complex SGL

Writes an arbitrary waveform to the NI-RFSG device.

This node accepts the complex baseband data in the form of complex single data type.

When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1dcsg.png']

##### waveform data

Array of data to load into the waveform.

You must normalize the data points in the array to have polar magnitudes between 0.0 and +1.00.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

Name used to store the waveform.

This string is case-insensitive and alphanumeric, and it cannot use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### more data pending?

Boolean value that indicates whether the data block contains the end of the waveform.

| True | Allows the data to be appended to the waveform later. |
| --- | --- |
| False | This data block contains the end of the waveform. |

Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. You can append data to a previously written waveform by using the saved waveform name.

Note

PXIe-5644/5645/5646/5673E/5820/5840

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Write Arbitrary Waveform

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=write-arb-waveform-i-q-arrays-dbl.html language=enus -->
## TOPIC 00079: I-Q Arrays DBL

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `write-arb-waveform-i-q-arrays-dbl.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/write-arb-waveform-i-q-arrays-dbl.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the NI-RFSG device. This node accepts the I and Q vectors of a complex baseband signal. When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state. session in Instrument session obtained from Initialize With Options. error in

I-Q Arrays DBL

Writes an arbitrary waveform to the NI-RFSG device.

This node accepts the I and Q vectors of a complex baseband signal.

When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### I data

In-phase (I) component of the complex baseband signal.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### Q data

Quadrature-phase (Q) component of the complex baseband signal.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

Name used to store the waveform.

This string is case-insensitive and alphanumeric, and it cannot use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### more data pending?

Boolean value that indicates whether the data block contains the end of the waveform.

| True | Allows the data to be appended to the waveform later. |
| --- | --- |
| False | This data block contains the end of the waveform. |

Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. You can append data to a previously written waveform by using the saved waveform name.

Note

PXIe-5644/5645/5646/5673E/5820/5840

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Write Arbitrary Waveform

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=write-arb-waveform-i-q-arrays-sgl.html language=enus -->
## TOPIC 00080: I-Q Arrays SGL

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `write-arb-waveform-i-q-arrays-sgl.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/write-arb-waveform-i-q-arrays-sgl.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the NI-RFSG device. This node accepts the I and Q vectors of a complex baseband signal containing singles. When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state. session in Instrument session obtained from Initialize With

I-Q Arrays SGL

Writes an arbitrary waveform to the NI-RFSG device.

This node accepts the I and Q vectors of a complex baseband signal containing singles.

When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1dsgl.png']

##### I data

In-phase (I) component of the complex baseband signal.

[IMAGE alt='datatype_icon' src='/assets/img/c1dsgl.png']

##### Q data

Quadrature-phase (Q) component of the complex baseband signal.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

Name used to store the waveform.

This string is case-insensitive and alphanumeric, and it cannot use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### more data pending?

Boolean value that indicates whether the data block contains the end of the waveform.

| True | Allows the data to be appended to the waveform later. |
| --- | --- |
| False | This data block contains the end of the waveform. |

Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. You can append data to a previously written waveform by using the saved waveform name.

Note

PXIe-5644/5645/5646/5673E/5820/5840

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Write Arbitrary Waveform

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=write-arb-waveform-i16.html language=enus -->
## TOPIC 00081: I16

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `write-arb-waveform-i16.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/write-arb-waveform-i16.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the NI-RFSG device. This node accepts the interleaved I/Q date of a complex baseband signal. When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state. session in Instrument session obtained from Initialize With Options. erro

I16

Writes an arbitrary waveform to the NI-RFSG device.

This node accepts the interleaved I/Q date of a complex baseband signal.

When streaming is enabled, you can call this node when the NI-RFSG device is in the Generation state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/c1di16.png']

##### interleaved IQ data

Array of interleaved I data and Q data to load into the waveform, paired in binary (I16) format.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

Name used to store the waveform.

This string is case-insensitive and alphanumeric, and it cannot use reserved words.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

Parent topic:

Write Arbitrary Waveform

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=write-arb-waveform.html language=enus -->
## TOPIC 00082: Write Arbitrary Waveform

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `write-arb-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/write-arb-waveform.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the device.

Write Arbitrary Waveform

Writes an arbitrary waveform to the device.

Arbitrary Waveform Generator Nodes

Complex DBL

NI-RFSG

Complex SGL

NI-RFSG

Complex DBL Cluster

NI-RFSG

Complex SGL Cluster

NI-RFSG

Complex DBL Waveform

NI-RFSG

Complex SGL Waveform

NI-RFSG

I-Q Arrays DBL

NI-RFSG

I-Q Arrays SGL

NI-RFSG

I16

NI-RFSG

Parent topic:

Arbitrary Waveform Generator Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=write-p2p-endpoint-i16.html language=enus -->
## TOPIC 00083: Write P2P Endpoint (I16)

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `write-p2p-endpoint-i16.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/write-p2p-endpoint-i16.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an array of 16-bit integer data to the peer-to-peer endpoint. Use this node to write initial data from the host to the endpoint before starting generation to avoid underflow when you start the generation. session in Instrument session obtained from Initialize With Options. error in Error cond

Write P2P Endpoint (I16)

Writes an array of 16-bit integer data to the peer-to-peer endpoint.

Use this node to write initial data from the host to the endpoint before starting generation to avoid underflow when you start the generation.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### stream endpoint

Stream endpoint FIFO to configure.

[IMAGE alt='datatype_icon' src='/assets/img/c1di16.png']

##### interleaved IQ data

Array of data to write into the endpoint FIFO.

The binary data is left-justified.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### stream endpoint out

Stream resources to use.

#### Hardware Support

This node supports the following hardware:

- PXIe-5673E

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-rfsg-lvnxg-api-ref path=write-script.html language=enus -->
## TOPIC 00084: Write Script

- bundle_id: `ni-rfsg-lvnxg-api-ref`
- source_path: `write-script.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsg-lvnxg-api-ref/raw/resource/enus/write-script.html
- document_id: `ni-rfsg-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a script to the device to control waveform generation in Script mode. Before using this node, you must first configure your device for Script generation mode by calling Configure Generation Mode. The NI-RFSG device must be in the Configuration state before you call this node. session in Instr

Write Script

Writes a script to the device to control waveform generation in Script mode.

Before using this node, you must first configure your device for Script generation mode by calling 
 [Configure Generation Mode](configure-generation-mode.html).

The NI-RFSG device must be in the Configuration state before you call this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### script

Script that controls waveform generation.

##### Supported Scripts

NI-RFSG supports generating multiple scripts that you select using the Selected Script property.

If you are using a vector signal transceiver, some script instructions are not supported.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5673E
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSG Getting Started Script

Parent topic:

Script Nodes
