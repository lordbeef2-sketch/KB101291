# NI DOCUMENT BUNDLE: ni-rfsa-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-rfsa-lvnxg-api-ref start=1 end=95 -->
<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=abort.html language=enus -->
## TOPIC 00001: Abort

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `abort.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/abort.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops an acquisition previously started with Initiate or Read Power Spectrum. You can also use this node to stop a self calibration. Calling this node is optional, unless you want to stop an acquisition before it is complete or you are continuously acquiring data. session in Instrument session obtai

Abort

Stops an acquisition previously started with [Initiate](initiate.html) or [Read Power Spectrum](read-power-spectrum.html).

You can also use this node to stop a self calibration.

Calling this node is optional, unless you want to stop an acquisition before it is complete or you are continuously acquiring data.

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

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5698
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Optimize Adjacent Channel Power

#### Types of Acquisitions to Stop

You can use this node to stop the following kinds of acquisitions:

- Triggered spectrum acquisitions that have not yet been triggered
- Multispan acquisitions in progress
- Average spectrum acquisitions in progress
- Single-record spectrum acquisitions in progress
- Streaming in progress

Parent topic:

Low Level Measurement

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=calibration.html language=enus -->
## TOPIC 00002: Calibration

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/calibration.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Calibration

NI-RFSA Nodes

Use NI-RFSA nodes to develop applications for your vector signal analyzer.

Self Calibrate

NI-RFSA

Self Calibrate Range

Self-calibrates all configurations within the specified frequency and reference level limits.

Is Self Calibration Valid?

Returns an array to indicate which calibration steps contain valid calibration data.

Perform Thermal Correction

Corrects for temperature variations while acquiring the same signal for extended periods of time in a continuous acquisition.

Get Self Calibration Last Date And Time

Returns the date and time of the last successful self-calibration.

Get Self Calibration Last Temp

Returns the temperature, in degrees Celsius, at the last successful self-calibration.

Set Calibration User Defined Info

Writes user-defined information into the onboard EEPROM.

Get Calibration User Defined Info

Returns user-defined information from the onboard EEPROM.

Clear Self Calibrate Range

Self Calibrate Range

External Alignment

External Calibration

Parent topic:

NI-RFSA Nodes

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=change-external-cal-password.html language=enus -->
## TOPIC 00003: Change External Calibration Password

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `change-external-cal-password.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/change-external-cal-password.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the password that is required to initialize an external calibration session. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error B

Change External Calibration Password

Changes the password that is required to initialize an external calibration session.

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

##### old password

Old (current) external calibration password.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### new password

New (desired) external calibration password.

The maximum length of the password varies by device.

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

- PXIe-5601/5603/5605/5606
- PXIe-5693/5694/5698
- PXIe-5820/5840

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=check-acquisition-status.html language=enus -->
## TOPIC 00004: Check Acquisition Status

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `check-acquisition-status.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/check-acquisition-status.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the acquisition. Use this node to check for any errors that may occur during signal acquisition or to check whether the device has completed the acquisition operation. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur befor

Check Acquisition Status

Checks the status of the acquisition.

Use this node to check for any errors that may occur during signal acquisition or to check whether the device has completed the acquisition operation.

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

Boolean value that returns the signal acquisition status.

| True | Signal acquisition is complete. |
| --- | --- |
| False | Signal acquisition is not complete. |

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5694/5698
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Peer-to-Peer Streaming with RFSG

Parent topic:

Low Level Measurement

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=clear-self-calibrate-range.html language=enus -->
## TOPIC 00005: Clear Self Calibrate Range

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `clear-self-calibrate-range.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/clear-self-calibrate-range.html
- document_id: `ni-rfsa-lvnxg-api-ref`
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

Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=clock.html language=enus -->
## TOPIC 00006: Clock

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/clock.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Clock

Configuration

Configure Ref Clock

NI-RFSA

Configure PXI Chassis Clk10

10 MHz

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=close-external-alignment-step.html language=enus -->
## TOPIC 00007: Close External Alignment Step

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `close-external-alignment-step.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/close-external-alignment-step.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an EEPROM-specific external alignment step opened by Initialize External Alignment Step. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Stand

Close External Alignment Step

Closes an EEPROM-specific external alignment step opened by [Initialize External Alignment Step](initialize-external-alignment-step.html).

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

- PXIe-5605 (PXIe-5665 only)
- PXIe-5606 (PXIe-5668 only)

Parent topic:

External Alignment

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=close-external-alignment.html language=enus -->
## TOPIC 00008: Close External Alignment

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `close-external-alignment.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/close-external-alignment.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an NI-RFSA external alignment session and, if specified, stores the new external alignment constants and data, such as time and temperature, in the onboard EEPROM. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs.

Close External Alignment

Closes an NI-RFSA external alignment session and, if specified, stores the new external alignment constants and data, such as time and temperature, in the onboard EEPROM.

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

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### action

Utilization of the alignment values from the closed session.

| Abort | 0 | The old alignment constants are kept, and the new ones are discarded. |
| --- | --- | --- |
| Commit | 1 | The new alignment constants are stored in the EEPROM. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5605 (PXIe-5665 only)
- PXIe-5606 (PXIe-5668 only)

Parent topic:

External Alignment

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=close-external-calibration.html language=enus -->
## TOPIC 00009: Close External Calibration

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `close-external-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/close-external-calibration.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an NI-RFSA external calibration session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node

Close External Calibration

Closes an NI-RFSA external calibration session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM.

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

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### action

Use of the calibration values from this session as the session is closed.

| Abort | 0 | The old calibration constants are kept, and the new ones are discarded. |
| --- | --- | --- |
| Commit | 1 | The new calibration constants are stored in the EEPROM. |

Default value: Abort

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5693/5694/5698
- PXIe-5820/5840

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=close.html language=enus -->
## TOPIC 00010: Close

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `close.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/close.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session to the device. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. Unlike most nodes, this node runs normally even if an error occurs before this node runs.Standard Error Behavior Default value: no error

Close

Closes the session to the device.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5693/5694/5698
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Getting Started IQ
- RFSA Getting Started Spectrum
- RFSA Getting Started Multi Record IQ

#### Closing a Session with SFP Session Access Enabled

If you close a session that has Soft Front Panel (SFP) session access enabled, any application connected to the shared device session is no longer usable.

Parent topic:

NI-RFSA Nodes

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=commit.html language=enus -->
## TOPIC 00011: Commit

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `commit.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/commit.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to hardware. Calling this node is optional. Settings are automatically committed to hardware when you call Initiate, Read IQ, or Read Power Spectrum. This node does not wait for settling time, unlike Initiate. session in Instrument session obtained from Initialize With Options. erro

Commit

Commits settings to hardware.

Note

Initiate

Read IQ

Read Power Spectrum

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

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5693/5694/5698
- PXIe-5820/5840

Parent topic:

Low Level Measurement

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configuration-list.html language=enus -->
## TOPIC 00012: Configuration List

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configuration-list.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configuration-list.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Configuration List

Configuration

Create Configuration List

Creates an empty configuration list for RF list mode.

Create Configuration List Step

Creates a new configuration list step in the configuration list for RF list mode specified by the Active Configuration List property.

Delete Configuration List

Deletes a previously created configuration list and all the configuration list steps in the RF list mode configuration list.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configuration.html language=enus -->
## TOPIC 00013: Configuration

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configuration.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Configuration

NI-RFSA Nodes

Use NI-RFSA nodes to develop applications for your vector signal analyzer.

Configure Acquisition Type

Configures whether the session acquires I/Q data or computes a power spectrum over the specified frequency range.

Configure Reference Level

Configures the reference level.

IQ

Spectrum

Configuration List

Trigger

Clock

Parent topic:

NI-RFSA Nodes

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-acquisition-type.html language=enus -->
## TOPIC 00014: Configure Acquisition Type

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-acquisition-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-acquisition-type.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether the session acquires I/Q data or computes a power spectrum over the specified frequency range. session in Instrument session obtained from Initialize With Options. acquisition type Type of acquisition. IQ Configures NI-RFSA for I/Q acquisitions. Spectrum Configures NI-RFSA for spe

Configure Acquisition Type

Configures whether the session acquires I/Q data or computes a power spectrum over the specified frequency range.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### acquisition type

Type of acquisition.

| IQ | Configures NI-RFSA for I/Q acquisitions. |
| --- | --- |
| Spectrum | Configures NI-RFSA for spectrum acquisitions. |

Default value: IQ

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Getting Started IQ
- RFSA Getting Started Spectrum
- RFSA Getting Started Multi Record IQ

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-iq-carrier-frequency.html language=enus -->
## TOPIC 00015: Configure IQ Carrier Frequency

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-iq-carrier-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-iq-carrier-frequency.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the carrier frequency of the vector signal analyzer hardware for an I/Q acquisition. The carrier frequency is the center frequency of the I/Q acquisition. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The n

Configure IQ Carrier Frequency

Configures the carrier frequency of the vector signal analyzer hardware for an I/Q acquisition.

The carrier frequency is the center frequency of the I/Q acquisition.

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

##### carrier frequency

Carrier frequency, in hertz (Hz), of the RF signal to acquire.

The vector signal analyzer tunes to this frequency. NI-RFSA may coerce this value based on hardware settings and downconversion settings.

NI-RFSA sets the IQ Carrier Frequency property to this value. Refer to the specifications for your device for allowable frequency settings.

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Getting Started IQ
- RFSA Getting Started Multi Record IQ
- RFSA Acquire Continuous IQ

Parent topic:

IQ

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-iq-rate.html language=enus -->
## TOPIC 00016: Configure IQ Rate

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-iq-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-iq-rate.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the I/Q rate, in samples per second (S/s), for the acquisition. For the PXIe-5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect your measurements. session in Instrument session obtained from Initialize With Options. error in

Configure IQ Rate

Specifies the I/Q rate, in samples per second (S/s), for the acquisition.

Note

NI-RFSA

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

##### IQ rate

I/Q rate, expressed in samples per second (S/s), for the acquisition.

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Getting Started IQ
- RFSA Getting Started Multi Record IQ
- RFSA Acquire Continuous IQ

#### Digitizer Bandwidth Behavior

For the PXIe-5663E/5665/5667/5668, when you set the Digitizer Sample Clock Timebase Source property to OnboardClock, the digitizer bandwidth is greater than or equal to the coerced IQ rate times 0.8.

#### Device-Specific Signal Bandwidth Limitations

Actual signal bandwidth is limited for all supported devices by the anti-aliasing filter. Further device-specific limitations are as follows.

- PXIe-5663E, PXIe-5644/5645/5646, PXIe-5840 : Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use.
- PXIe-5665 : Actual signal bandwidth is limited by the preselector and the combination of the chosen IF filter and anti-aliasing filter. Maximum allowed instantaneous bandwidth is independent of the downconverter center frequency for frequencies less than 3.6 GHz . At frequencies greater than 3.6 GHz , if your device supports the preselector (YIG-tuned filter) and you have enabled it for your application, the maximum allowed instantaneous bandwidth is limited to the instantaneous bandwidth of the preselector.
- PXIe-5667 : Actual signal bandwidth is limited by the preselector and the combination of the chosen IF filter and anti-aliasing filter. Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use.
- PXIe-5668 : Actual signal bandwidth is limited by the FPGA image that is downloaded upon opening the session to the PXIe-5624 IF digitizer. Maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use.

Note

Parent topic:

IQ

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-number-of-records.html language=enus -->
## TOPIC 00017: Configure Number of Records

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-number-of-records.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-number-of-records.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of records in a finite acquisition or configures the device to continuously acquire records. You can only configure the device to acquire a finite number of records if you set number of records is finite input to True. session in Instrument session obtained from Initialize With

Configure Number of Records

Configures the number of records in a finite acquisition or configures the device to continuously acquire records.

Note

number of records is finite

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

##### number of records is finite

Boolean value that specifies whether to configure the device to acquire a finite number of records or to acquire records continuously.

| True | The NI-RFSA device acquires a finite number of records. |
| --- | --- |
| False | The NI-RFSA device acquires records continuously until you call Abort to abort the acquisition. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### number of records

Number of records to acquire if the number of records is finite input is set to True.

Default value: 1

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Getting Started Multi Record IQ
- RFSA List Mode Frequency and Power Sweep (Power Triggered)
- RFSA List Mode Frequency and Power Sweep (Timer Triggered)

#### Continuously Acquire Records

If you configure the device to continuously acquire records, it acquires records until you call 
 [Abort](abort.html) to abort the acquisition. The device stores records in onboard memory in a circular fashion. After the device fills the memory, it starts overwriting previously acquired records from the beginning of the memory buffer. Fetch the records as they are being acquired using 
 [Fetch IQ](fetch-iq-data.html) to avoid overwriting data before you retrieve it.

#### Acquire More Records than Device Memory Allows

To acquire more records than will fit into the device memory without continuously acquiring records, set number of records is finite to True and the Allow More Records Than Memory property to True.

Parent topic:

IQ

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-number-of-samples.html language=enus -->
## TOPIC 00018: Configure Number of Samples

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-number-of-samples.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-number-of-samples.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of samples in a finite acquisition or configures the device to continuously acquire samples. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard er

Configure Number of Samples

Configures the number of samples in a finite acquisition or configures the device to continuously acquire samples.

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

##### number of samples is finite

Boolean value that specifies whether to configure the device to acquire a finite number of samples or to acquire samples continuously.

| True | The NI-RFSA device acquires a finite number of samples. |
| --- | --- |
| False | The NI-RFSA device continuously acquires samples until you call Abort to abort the acquisition. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### samples per record

Number of samples per record if the number of samples is finite input is set to True.

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Getting Started IQ
- RFSA Getting Started Multi Record IQ
- RFSA Acquire IQ Data in Blocks

#### Configuring the Device for Finite Acquisition

If you configure the device for finite acquisition, it acquires the specified number of samples and then stops the acquisition. You can configure the device to acquire multiple records using 
 [Configure Number of Records](configure-number-of-records.html). Each record contains the number of samples specified in this node. The default number of records to acquire is 1.

#### Configuring the Device to Continuously Acquire Samples

If you configure the device to continuously acquire samples, it continues acquiring data until you call 
 [Abort](abort.html) to abort the acquisition. The device stores data in onboard memory in a circular fashion. After the device fills the memory, it starts overwriting previously acquired data from the beginning of the memory buffer. Retrieve the samples as they are being acquired using 
 [Fetch IQ](fetch-iq-data.html) to avoid overwriting data before you retrieve it.

Parent topic:

IQ

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-pxi-chassis-clk10.html language=enus -->
## TOPIC 00019: Configure PXI Chassis Clk10

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-pxi-chassis-clk10.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-pxi-chassis-clk10.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. This option can be configured only when the PXI-5600 is installed in the Star Trigger Controller Slot, also known as the System Timing Slot, of the PXI chassis. session in Instrument session obtained from Initialize With

Configure PXI Chassis Clk10

Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. This option can be configured only when the PXI-5600 is installed in the Star Trigger Controller Slot, also known as the System Timing Slot, of the PXI chassis.

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

##### PXI Clk10 source

Source of the Reference Clock signal.

This option can only be configured when the PXI-5600 is in Slot 2 of the PXI chassis.

| None | The device does not drive the PXI 10 MHz backplane Reference clock. |
| --- | --- |
| OnboardClock | The device drives the PXI 10 MHz backplane Reference Clock with the PXI-5600 onboard clock. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O on the PXI-5600 front panel to use this option. |
| RefIn | The device drives the PXI 10 MHz backplane Reference Clock with the reference source attached to the PXI-5600 REF IN connector. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O on the PXI-5600 front panel to use this option. |

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

- PXI-5600 (external digitizer mode)
- PXI-5661

Parent topic:

Clock

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-ref-clock.html language=enus -->
## TOPIC 00020: Configure Ref Clock

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-ref-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-ref-clock.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the NI-RFSA device Reference Clock. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error clock

Configure Ref Clock

Configures the NI-RFSA device Reference Clock.

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

##### clock source

Source of the Reference Clock signal.

| OnboardClock | PXIe-5663E: Lock the PXIe-5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector on the PXIe-5652 to the CLK IN connector on the PXIe-5622. PXIe-5665: Lock the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN connector on the PXIe-5622. PXIe-5667: Lock the PXIe-5667 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN connector on the PXIe-5622, and connect the 10 MHz REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. PXIe-5668: Lock the PXIe-5668 to the PXIe-5653 LO source onboard clock. Connect the LO2 OUT terminal on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840: Lock the device to its onboard clock. PXIe-5840 with PXIe-5653: Lock to the PXIe-5653 onboard clock. Connect the REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. Configure open NI-RFSG sessions to the device to use RefIn for the PXIe-5840 or RefIn2 for the PXIe-5840 with PXIe-5653. |
| --- | --- |
| RefIn | PXIe-5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector on the PXIe-5652 to the CLK IN connector on the PXIe-5622. PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN connector on the PXIe-5622. PXIe-5667: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN connector on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. PXIe-5668: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT terminal on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840: Lock the device to the signal at the external REF IN connector. PXIe-5840 with PXIe-5653: Lock to the signal at the REF IN connector on the associated PXIe-5653. Connect the REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. |
| PXI_CLK | PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5694, PXIe-5820/5840/5840 with PXIe-5653: Lock the device to the PXI backplane clock. PXIe-5668: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 Out connector to the CLK IN connector on the PXIe-5624. |
| ClkIn | PXIe-5644/5645/5646, PXIe-5820/5840/5840 with PXIe-5653: This configuration does not apply. PXIe-5663E: Lock the PXIe-5663E to an external 10 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652. PXIe-5665: Lock the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the clock rate input to 100 MHz. PXIe-5667: Lock the PXIe-5667 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Connect the 10 MHZ REF OUT connector on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. Set the clock rate input to 100 MHz. PXIe-5668: Lock the PXIe-5668 to an external 10 MHz or 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the clock rate input to 10 MHz or 100 MHz, as appropriate. |
| None | No Reference Clock is required for the current device configuration. |
| RefIn2 | PXIe-5840 with PXIe-5653: NI-RFSA locks the device to the clock sourced at the PXIe-5840 REF IN terminal that is already configured by an NI-RFSG session. Connect the PXIe-5840 REF OUT connector to the PXIe-5653 REF IN connector. Configure open NI-RFSG sessions to the device to use RefIn for the PXIe-5840 or Onboard Clock for the PXIe-5840 with PXIe-5653. PXIe-5644/5645/5646, PXIe-5663E/5665/5667/5668, PXIe-5820/5840: This configuration does not apply. |
| PXI_ClkMaster | PXIe-5840 with PXIe-5653: NI-RFSA configures the PXIe-5653 to export the Reference Clock, and configures the PXIe-5840 to use PXI_Clk. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. For best performance, configure all other devices in the system to use PXI_Clk as the Reference Clock source. PXIe-5644/5645/5646, PXIe-5663E/5665/5667/5668, PXIe-5820/5840: This configuration does not apply. |

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### clock rate

Reference Clock rate, specified in Hz.

Default value: 10 MHz

##### Device-Specific Values

For the PXIe-5601, PXIe-5644/5645/5646, PXIe-5694, and the PXIe-5820/5840, 10 MHz is the only supported value.

For the PXIe-5665/5667/5668, you can specify values between 5 MHz and 100 MHz, in increments of 1 MHz.

##### External Clock Frequency

For the PXIe-5665/5667/5668, if your external clock signal frequency is set to a frequency other than 10 MHz, set the this input according to the frequency of your external clock signal.

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

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5694
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Synchronization (TClk, Shared LO and Reference Clock)
- RFSA Synchronization (TClk, Shared LO and Reference Clock, and Continuous Acquisition)

Parent topic:

Clock

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-reference-level.html language=enus -->
## TOPIC 00021: Configure Reference Level

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-reference-level.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-reference-level.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level. The reference level represents the maximum expected power of an input RF signal. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard erro

Configure Reference Level

Configures the reference level.

The reference level represents the maximum expected power of an input RF signal.

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

##### reference level

Total expected power, in dBm, of the RF input signal.

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

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Getting Started IQ
- RFSA Getting Started Spectrum
- RFSA Getting Started Multi Record IQ

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-resolution-bandwidth.html language=enus -->
## TOPIC 00022: Configure Resolution Bandwidth

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-resolution-bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-resolution-bandwidth.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth of a spectrum acquisition. The resolution bandwidth controls the width of the frequency bins in the power spectrum computed by NI-RFSA. A larger value for resolution bandwidth creates wider frequency bins, which results in fewer bins, or spectral lines. session in

Configure Resolution Bandwidth

Configures the resolution bandwidth of a spectrum acquisition.

The resolution bandwidth controls the width of the frequency bins in the power spectrum computed by NI-RFSA. A larger value for resolution bandwidth creates wider frequency bins, which results in fewer bins, or spectral lines.

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

##### resolution bandwidth

Resolution bandwidth of a spectrum acquisition, in hertz (Hz).

Configure the type of resolution bandwidth with the Resolution Bandwidth Type property.

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Getting Started Spectrum
- RFSA Frequency Sweep
- RFSA In-band Retuning

#### Specifying the Frequency Bin Width

By default, the resolution bandwidth value corresponds to the 3 decibels (dB) bandwidth of the window type NI-RFSA uses to compute the spectrum. To directly specify the frequency bin width, set the Resolution Bandwidth Type property to 
 Bin Width.

Parent topic:

Spectrum

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-spectrum-frequency-center-span.html language=enus -->
## TOPIC 00023: Center Span

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-spectrum-frequency-center-span.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-spectrum-frequency-center-span.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the span and center frequency of the spectrum read by NI-RFSA. A spectrum acquisition consists of data surrounding the center frequency. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to th

Center Span

Configures the span and center frequency of the spectrum read by NI-RFSA.

A spectrum acquisition consists of data surrounding the center frequency.

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

Center frequency, in hertz (Hz), in a spectrum acquisition.

The NI-RFSA device you use determines the valid range. Refer to the specifications for your device for more information about frequency range.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### span

Span, in hertz (Hz), of a spectrum acquisition.

Note

PXIe-5663E/5665/5667/5668

NI-RFSA

Digitizer Dither Enabled

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

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Configure Spectrum Frequency

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-spectrum-frequency-start-stop.html language=enus -->
## TOPIC 00024: Start & Stop

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-spectrum-frequency-start-stop.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-spectrum-frequency-start-stop.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the start and stop frequencies of a spectrum read by NI-RFSA. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Defa

Start & Stop

Configures the start and stop frequencies of a spectrum read by NI-RFSA.

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

##### start frequency

Lower limit of a span of frequencies, in hertz (Hz).

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### stop frequency

Upper limit of a span of frequencies, in hertz (Hz).

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

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

#### Spectrum Span Behavior

If you configure the spectrum span ( stop frequency – start frequency ) to a value larger than the instantaneous bandwidth of the device, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you requested.

#### PXIe-5663E Multispan Acquisition Behavior

For the PXIe-5663E, NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the bandwidths that correspond to each span are different (10 MHz and 20 MHz, respectively).

Parent topic:

Configure Spectrum Frequency

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-spectrum-frequency.html language=enus -->
## TOPIC 00025: Configure Spectrum Frequency

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-spectrum-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-spectrum-frequency.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency range of the spectrum read by NI-RFSA.

Configure Spectrum Frequency

Configures the frequency range of the spectrum read by NI-RFSA.

Spectrum

Center Span

NI-RFSA

Start & Stop

NI-RFSA

Parent topic:

Spectrum

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-trigger-advance-digital-edge.html language=enus -->
## TOPIC 00026: Digital Edge

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-trigger-advance-digital-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-trigger-advance-digital-edge.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge Advance Trigger. The Advance Trigger indicates where a new record begins. This node is not supported if you set the acquisition type input of Configure Acquisition Type to Spectrum or the Acquisition Type property to Spectrum. session in Instrument se

Digital Edge

Configures the device to wait for a digital edge Advance Trigger.

The Advance Trigger indicates where a new record begins.

Note

acquisition type

Configure Acquisition Type

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

Source of the digital edge for the Advance Trigger.

| PFI0 | The trigger is received on PFI 0. |
| --- | --- |
| PFI1 | The trigger is received on PFI 1. |
| PXI_Trig0 | The trigger is received on PXI trigger line 0. |
| PXI_Trig1 | The trigger is received on PXI trigger line 1. |
| PXI_Trig2 | The trigger is received on PXI trigger line 2. |
| PXI_Trig3 | The trigger is received on PXI trigger line 3. |
| PXI_Trig4 | The trigger is received on PXI trigger line 4. |
| PXI_Trig5 | The trigger is received on PXI trigger line 5. |
| PXI_Trig6 | The trigger is received on PXI trigger line 6. |
| PXI_Trig7 | The trigger is received on PXI trigger line 7. |
| PXI_STAR | The trigger is received on the PXI star trigger line. This value is not supported by the PXIe-5644/5645/5646. |
| PXIe_DStarB | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5840. |
| TimerEvent | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840 and for digital edge Advance triggers on the PXIe-5644/5645/5646 and the PXIe-5663E/5665. |

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### edge

Trigger edge to detect.

| Rising Edge | NI-RFSA detects a rising edge. |
| --- | --- |
| Falling Edge | NI-RFSA detects a falling edge. |

Default value: Rising Edge

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-trigger-advance-none.html language=enus -->
## TOPIC 00027: None

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-trigger-advance-none.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-trigger-advance-none.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not use an Advance Trigger. This node is necessary only if you configured an Advance Trigger in the past and now want to disable it. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node resp

None

Configures the device to not use an Advance Trigger.

This node is necessary only if you configured an Advance Trigger in the past and now want to disable it.

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-trigger-advance-software-edge.html language=enus -->
## TOPIC 00028: Software Edge

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-trigger-advance-software-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-trigger-advance-software-edge.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software Advance Trigger. The Advance Trigger indicates where a new record begins. This node is not supported if you set the acquisition type input of Configure Acquisition Type to Spectrum or the Acquisition Type property to Spectrum. session in Instrument sessio

Software Edge

Configures the device to wait for a software Advance Trigger.

The Advance Trigger indicates where a new record begins.

Note

acquisition type

Configure Acquisition Type

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

#### Programming Patterns

The device waits until you call 
 [Send Software Edge Trigger](send-software-edge-trigger.html) to assert the trigger.

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-trigger-ref-digital-edge.html language=enus -->
## TOPIC 00029: Digital Edge

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-trigger-ref-digital-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-trigger-ref-digital-edge.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge Reference Trigger to mark a reference point within the record. You can use this trigger with the NI-TClk API. The PXIe-5644/5645/5646 do not support the NI-TClk API. session in Instrument session obtained from Initialize With Options. error in Error c

Digital Edge

Configures the device to wait for a digital edge Reference Trigger to mark a reference point within the record.

Note

NI-TClk

PXIe-5644/5645/5646

NI-TClk

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

Source of the digital edge for the Reference Trigger.

| PFI0 | The trigger is received on PFI 0. |
| --- | --- |
| PFI1 | The trigger is received on PFI 1. |
| PXI_Trig0 | The trigger is received on PXI trigger line 0. |
| PXI_Trig1 | The trigger is received on PXI trigger line 1. |
| PXI_Trig2 | The trigger is received on PXI trigger line 2. |
| PXI_Trig3 | The trigger is received on PXI trigger line 3. |
| PXI_Trig4 | The trigger is received on PXI trigger line 4. |
| PXI_Trig5 | The trigger is received on PXI trigger line 5. |
| PXI_Trig6 | The trigger is received on PXI trigger line 6. |
| PXI_Trig7 | The trigger is received on PXI trigger line 7. |
| PXI_STAR | The trigger is received on the PXI star trigger line. This value is not supported by the PXIe-5644/5645/5646. |
| PXIe_DStarB | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5840. |
| TimerEvent | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840 and for digital edge Advance triggers on the PXIe-5644/5645/5646 and the PXIe-5663E/5665. |

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### edge

Trigger edge to detect.

| Rising Edge | NI-RFSA detects a rising edge. |
| --- | --- |
| Falling Edge | NI-RFSA detects a falling edge. |

Default value: Rising Edge

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### pretrigger samples

Number of samples to store for each record that is acquired immediately before the trigger occurs.

Default value: 0

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-trigger-ref-iq-power-edge.html language=enus -->
## TOPIC 00030: IQ Power Edge

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-trigger-ref-iq-power-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-trigger-ref-iq-power-edge.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. You can use this trigger with the NI-TClk API. The PXIe-5644/5645/5646 do not support the NI-TClk API. session in Instrument session obtained from Initial

IQ Power Edge

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

Note

NI-TClk

PXIe-5644/5645/5646

NI-TClk

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

Source of the RF signal for the power edge Reference Trigger. The only supported value is 0.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### level

Threshold, in dBm, above or below which the device triggers.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### slope

Type of slope that the device detects on the trigger signal.

| Rising Slope | NI-RFSA detects a rising edge (positive slope). |
| --- | --- |
| Falling Slope | NI-RFSA detects a falling edge (negative slope). |

Default value: Rising Slope

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### pretrigger samples

Number of samples to store for each record that is acquired immediately before the trigger occurs.

Default value: 0

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

#### Triggering on Burst Signals

To trigger on burst signals, specify a minimum quiet time using the Minimum Quiet Time property to ensure the trigger does not occur in the middle of a burst if the acquisition starts while a burst is generating. The quiet time should be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-trigger-ref-none.html language=enus -->
## TOPIC 00031: None

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-trigger-ref-none.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-trigger-ref-none.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a Reference Trigger to mark a reference point within a record. This node is necessary only if you previously configured a Reference Trigger and now want to disable it. session in Instrument session obtained from Initialize With Options. error in Error conditions

None

Configures the device to not wait for a Reference Trigger to mark a reference point within a record.

This node is necessary only if you previously configured a Reference Trigger and now want to disable it.

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-trigger-ref-software-edge.html language=enus -->
## TOPIC 00032: Software Edge

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-trigger-ref-software-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-trigger-ref-software-edge.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software Reference Trigger to mark a reference point within the record. The device waits until you call Send Software Edge Trigger to assert the trigger. You can use this trigger with the NI-TClk API. The PXIe-5644/5645/5646 do not support the NI-TClk API. This no

Software Edge

Configures the device to wait for a software Reference Trigger to mark a reference point within the record.

The device waits until you call 
 [Send Software Edge Trigger](send-software-edge-trigger.html) to assert the trigger.

Note

NI-TClk

PXIe-5644/5645/5646

NI-TClk

Note

acquisition type

Configure Acquisition Type

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

##### pretrigger samples

Number of samples to store for each record that is acquired immediately before the trigger occurs.

Default value: 0

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-trigger-start-digital-edge.html language=enus -->
## TOPIC 00033: Digital Edge

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-trigger-start-digital-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-trigger-start-digital-edge.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge Start Trigger at the beginning of the acquisition. You can use this trigger with the NI-TClk API. The PXIe-5644/5645/5646 do not support the NI-TClk API. This node is not supported if you set the acquisition type input of Configure Acquisition Type to

Digital Edge

Configures the device to wait for a digital edge Start Trigger at the beginning of the acquisition.

Note

NI-TClk

PXIe-5644/5645/5646

NI-TClk

Note

acquisition type

Configure Acquisition Type

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

Source of the digital edge for the Start Trigger.

| PFI0 | The trigger is received on PFI 0. |
| --- | --- |
| PFI1 | The trigger is received on PFI 1. |
| PXI_Trig0 | The trigger is received on PXI trigger line 0. |
| PXI_Trig1 | The trigger is received on PXI trigger line 1. |
| PXI_Trig2 | The trigger is received on PXI trigger line 2. |
| PXI_Trig3 | The trigger is received on PXI trigger line 3. |
| PXI_Trig4 | The trigger is received on PXI trigger line 4. |
| PXI_Trig5 | The trigger is received on PXI trigger line 5. |
| PXI_Trig6 | The trigger is received on PXI trigger line 6. |
| PXI_Trig7 | The trigger is received on PXI trigger line 7. |
| PXI_STAR | The trigger is received on the PXI star trigger line. This value is not supported by the PXIe-5644/5645/5646. |
| PXIe_DStarB | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5840. |
| TimerEvent | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840 and for digital edge Advance triggers on the PXIe-5644/5645/5646 and the PXIe-5663E/5665. |

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### edge

Trigger edge to detect.

| Rising Edge | NI-RFSA detects a rising edge. |
| --- | --- |
| Falling Edge | NI-RFSA detects a falling edge. |

Default value: Rising Edge

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-trigger-start-none.html language=enus -->
## TOPIC 00034: None

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-trigger-start-none.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-trigger-start-none.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a Start Trigger at the beginning of the acquisition. This node is necessary only if you previously configured a Start Trigger and now want to disable it. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur be

None

Configures the device to not wait for a Start Trigger at the beginning of the acquisition.

This node is necessary only if you previously configured a Start Trigger and now want to disable it.

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-trigger-start-software-edge.html language=enus -->
## TOPIC 00035: Software Edge

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-trigger-start-software-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-trigger-start-software-edge.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software Start Trigger at the beginning of the acquisition. You can use this trigger with the NI-TClk API. The PXIe-5644/5645/5646 do not support the NI-TClk API. This node is not supported if you set the acquisition type input of Configure Acquisition Type to Spe

Software Edge

Configures the device to wait for a software Start Trigger at the beginning of the acquisition.

Note

NI-TClk

PXIe-5644/5645/5646

NI-TClk

Note

acquisition type

Configure Acquisition Type

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

#### Programming Patterns

The device waits until you call 
 [Send Software Edge Trigger](send-software-edge-trigger.html) to assert the trigger.

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=configure-trigger.html language=enus -->
## TOPIC 00036: Configure Trigger

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `configure-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/configure-trigger.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start, Reference, and Advance Triggers.

Configure Trigger

Configures the Start, Reference, and Advance Triggers.

Trigger

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=create-configuration-list-step.html language=enus -->
## TOPIC 00037: Create Configuration List Step

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `create-configuration-list-step.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/create-configuration-list-step.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new configuration list step in the configuration list for RF list mode specified by the Active Configuration List property. When you create a configuration list step, a new instance of each property specified by the configuration list properties is created. Configuration list properties ar

Create Configuration List Step

Creates a new configuration list step in the configuration list for RF list mode specified by the Active Configuration List property.

When you create a configuration list step, a new instance of each property specified by the configuration list properties is created. Configuration list properties are specified when you create a configuration list.

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

Boolean value that specifies whether this step is the active step for the active configuration list.

Note

Active Configuration List Step

| True | The step is the active configuration list step. |
| --- | --- |
| False | The step is not the active configuration list step. |

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
- PXIe-5663E/5665/5667
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA List Mode Frequency and Power Sweep (Power Triggered)
- RFSA List Mode Frequency and Power Sweep (Timer Triggered)
- RFSA Lost Mode Open Loop Synchronization with RFSG (Multiple Waveforms)

Parent topic:

Configuration List

Related information:

- RF List Mode
- Using RF List Mode

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=create-configuration-list.html language=enus -->
## TOPIC 00038: Create Configuration List

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `create-configuration-list.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/create-configuration-list.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an empty configuration list for RF list mode. Calling this node allocates space for each of the configuration list properties. After you create a configuration list, enable the list using the set as active list input. session in Instrument session obtained from Initialize With Options. error

Create Configuration List

Creates an empty configuration list for RF list mode.

Calling this node allocates space for each of the configuration list properties. After you create a configuration list, enable the list using the set as active list input.

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

Name of the configuration list.

This string may not contain spaces, special characters, or punctuation marks.

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### configuration list properties

Properties that you intend to change between configuration list steps.

##### Listable Configuration List Properties

You can include the following properties in your configuration list based on your device:

Channel Coupling

Device Instantaneous Bandwidth

PXIe-5663E/5665/5667

PXIe-5820/5840

Downconverter Center Frequency

PXIe-5663E/5665/5667

PXIe-5644/5645/5646

PXIe-5840

Downconverter Frequency Offset

Downconverter Preselector Enabled

PXIe-5665

14 GHz

PXIe-5667

7 GHz

PXIe-5840

External Gain

PXIe-5663E/5665/5667

PXIe-5820/5840

Frequency Settling

PXIe-5663E/5665/5667

PXIe-5840

IF Filter Bandwidth

PXIe-5663E/5665/5667

IF Output Power Level

PXIe-5663E/5665/5667

IF Output Power Level Offset

PXIe-5663E/5665/5667

IQ Carrier Frequency

PXIe-5663E/5665/5667

PXIe-5644/5645/5646

PXIe-5820/5840

IQ In Port Carrier Frequency

PXIe-5645

PXIe-5820

IQ In Port Vertical Range

PXIe-5645

PXIe-5820

IQ Power Edge Trigger Level

PXIe-5663E/5665/5667

PXIe-5644/5645/5646

PXIe-5820/5840

Low Frequency Bypass Enabled

PXIe-5667

Mechanical Attenuation

PXIe-5663E/5665/5667

Mechanical Attenuator Enabled

PXIe-5663E

Minimum ACPR

PXIe-5665

Notch Filter Enabled

PXIe-5667

Number of Samples

PXIe-5820/5840

OSP Data Scaling Factor

PXIe-5663E/5665/5667

PXIe-5820/5840

Reference Level

PXIe-5663E/5665/5667

PXIe-5644/5645/5646

PXIe-5840

RF Attenuation

PXIe-5663E/5665/5667

RF Preamp Enabled

PXIe-5663E/5665/5667

PXIe-5840

RF Preselector Filter

PXIe-5667

Timer Event interval

PXIe-5663E/5665/5667

PXIe-5644/5645/5646

PXIe-5820/5840

##### Property Node Behavior

When you use the NI-RFSA property node to set one of the configuration list properties, that property is set as one of the configuration list steps. Use the Active Configuration List property to specify which configuration list step to configure.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### set as active list

Boolean value that specifies whether the list is the active configuration list.

| True | The list is the active configuration list. |
| --- | --- |
| False | The list is not the active configuration list. |

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
- PXIe-5663E/5665/5667
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA List Mode Frequency and Power Sweep (Power Triggered)
- RFSA List Mode Frequency and Power Sweep (Timer Triggered)
- RFSA List Mode Open Loop Synchronization with RFSG (Multiple Waveforms)

#### Programming Patterns

Call 
 [Create Configuration List Step](create-configuration-list-step.html) to add steps to the active configuration list.

Parent topic:

Configuration List

Related information:

- RF List Mode
- Using RF List Mode

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=delete-configuration-list.html language=enus -->
## TOPIC 00039: Delete Configuration List

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `delete-configuration-list.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/delete-configuration-list.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes a previously created configuration list and all the configuration list steps in the RF list mode configuration list. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to s

Delete Configuration List

Deletes a previously created configuration list and all the configuration list steps in the RF list mode configuration list.

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

Name of the configuration list.

This string may not contain spaces, special characters, or punctuation marks.

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
- PXIe-5663E/5665/5667
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA List Mode Frequency and Power Sweep (Power Triggered)
- RFSA List Mode Frequency and Power Sweep (Timer Triggered)
- RFSA Lost Mode Open Loop Synchronization with RFSG (Multiple Waveforms)

#### Deleting a Configuration List Step

When you delete a configuration list step, all the instances of the properties associated with the configuration list step are also removed.

#### Deleting the Active Configuration List

When you delete the active configuration list, NI-RFSA automatically resets the Active Configuration List property to "" (empty string), which indicates no list is active, and the Active Configuration List Step property to 0.

Parent topic:

Configuration List

Related information:

- RF List Mode
- Using RF List Mode

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=enable-session-access.html language=enus -->
## TOPIC 00040: Enable Session Access

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `enable-session-access.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/enable-session-access.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables SFP session access for the specified instrument. SFP session access allows the NI-RFSA Soft Front Panel (SFP) to access a device with an existing open session and can help you debug your code. session in Instrument session obtained from Initialize With Options. error in Error con

Enable Session Access

Enables or disables SFP session access for the specified instrument.

SFP session access allows the NI-RFSA Soft Front Panel (SFP) to access a device with an existing open session and can help you debug your code.

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

##### session access enabled

Boolean value that enables or disables SFP session access for the specified device.

| True | Enables SFP session access. |
| --- | --- |
| False | Disables SFP session access. |

Default value: False

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

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5693/5694/5698
- PXIe-5840

#### Enabling SFP Session Access

To enable session access, specify a session in and wire True to the session access enabled input.

#### Disabling SFP Session Access

To disable session access wire False to the session access enabled input.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=export-signal.html language=enus -->
## TOPIC 00041: Export Signal

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `export-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/export-signal.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes signals (triggers, clocks, and events) to the specified output terminal. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavi

Export Signal

Routes signals (triggers, clocks, and events) to the specified output terminal.

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

| Start Trigger | NI-RFSA routes a Start Trigger. |
| --- | --- |
| Ref Trigger | NI-RFSA routes a Reference Trigger. |
| Advance Trigger | NI-RFSA routes an Advance Trigger. |
| Ready for Start Event | NI-RFSA routes a Ready for Start Event. |
| Ready for Ref Event | NI-RFSA routes a Ready for Reference Event. |
| Ready for Advance Event | NI-RFSA routes a Ready for Advance Event. |
| End of Record Event | NI-RFSA routes an End of Record Event. |
| Done Event | NI-RFSA routes a Done Event. |
| Reference Clock | NI-RFSA routes a Reference Clock signal. |
| User | NI-RFSA routes a user-defined signal, specified using the signal identifier input. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### signal identifier

User-defined signal to route.

Specify the signal you have implemented using FPGA extensions.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### output terminal

Terminal where the signal is exported. You can choose not to export any signal.

| Do not export signal | The signal is not exported. |
| --- | --- |
| ClkOut | The signal is exported to the CLK OUT connector on the PXIe-5622 front panel. |
| RefOut | The signal is exported to the REF IN/OUT terminal on the PXIe-5652 and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5840. |
| RefOut2 | The signal is exported to the REF OUT2 terminal on the LO. This connector exists on only the PXIe-5652. |
| PFI0 | The signal is exported to the PFI 0 connector. |
| PFI1 | The signal is exported to the PFI 1 connector on the PXIe-5622. |
| PXI_Trig0 | The signal is exported to the PXI trigger line 0. |
| PXI_Trig1 | The signal is exported to the PXI trigger line 1. |
| PXI_Trig2 | The signal is exported to the PXI trigger line 2. |
| PXI_Trig3 | The signal is exported to the PXI trigger line 3. |
| PXI_Trig4 | The signal is exported to the PXI trigger line 4. |
| PXI_Trig5 | The signal is exported to the PXI trigger line 5. |
| PXI_Trig6 | The signal is exported to the PXI trigger line 6. |
| PXIe_DStarC | The signal is exported to the PXIe_DStarC trigger line. This value is valid on only the PXIe-5820/5840. |

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
- PXIe-5663E/5665/5667/5668
- PXIe-5694
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Getting Started Spectrum
- RFSA Frequency Sweep
- RFSA In-band Retuning

#### Tristate Output Terminals

If you export a signal with this node and commit the session, the signal is routed to the output terminal you specify. If you then reconfigure the signal to have a different output terminal, the previous output terminal is tristated when the session is next committed. If you set the output terminal output to Do Not Export and commit, the previous output terminal is tristated.

#### Tristate PXI Trigger Lines

Any signals, except for those exported over PXI trigger lines, that are exported within a session persist after the session closes to prevent signal glitches between sessions. PXI trigger lines are always set to tristate when a session is closed. If you wish to have the output terminal tristated when the session closes, change the output terminal output for the exported signal to Do Not Export, and commit the session again before closing it.

#### Tristate PFI Lines

You can tristate all PFI lines by setting the reset input of Initialize to True or by using 
 [Reset](reset.html).

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=external-alignment.html language=enus -->
## TOPIC 00042: External Alignment

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `external-alignment.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/external-alignment.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

External Alignment

Calibration

Initialize External Alignment

NI-RFSA

Initialize External Alignment Step

Initializes an EEPROM-specific external alignment step.

Close External Alignment Step

Initialize External Alignment Step

Close External Alignment

NI-RFSA

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=external-calibration.html language=enus -->
## TOPIC 00043: External Calibration

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `external-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/external-calibration.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

External Calibration

Calibration

Init External Calibration

NI-RFSA

Close External Calibration

NI-RFSA

Get External Calibration Last Date and Time

Returns the date and time of the last successful external calibration.

Get External Calibration Last Temp

Returns the temperature, in degrees Celsius, at the last successful external calibration.

Get External Calibration Recommended Interval

Returns the recommended interval between external calibrations, in months.

Change External Calibration Password

Changes the password that is required to initialize an external calibration session.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=fetch-iq-data-more-1d-i16.html language=enus -->
## TOPIC 00044: 1D I16

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `fetch-iq-data-more-1d-i16.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/fetch-iq-data-more-1d-i16.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches binary I/Q data from a single record in an acquisition. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value

1D I16

Fetches binary I/Q data from a single record in an acquisition.

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

##### samples to read

Number of samples to fetch.

A value of -1 specifies that NI-RFSA fetches all samples.

Note

NI-RFSA

Fetch Relative To

Fetch Offset

Default value: -1

##### Number of Samples Not Available

If the number of samples specified in this input is not available after the time duration specified in the timeout input, 
 [Fetch IQ](fetch-iq-data.html) returns no data with a timeout error.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time, in seconds, allotted for the node to complete before returning a timeout error. For the PXIe-5644/5645/5646, PXIe-5668, and the PXIe-5820/5840, this input specifies the time allotted to receive the reference trigger.

Default value: 10

##### Timeout Value Behaviors

A value of -1 specifies that the node waits until all data is available. A value of 0 specifies that the node immediately returns available data.

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### record to fetch

Record to retrieve.

Record numbers are zero-based.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1di16.png']

##### data

Acquired unscaled, complex waveform.

The array is composed of interleaved I and Q samples, where the order of the array is as follows:

- Array[0] = I(0)
- Array[1] = Q(0)
- Array[2] = I(1)
- Array[3] = Q(1)

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### wfm info

Absolute and relative timestamps for the operation, the time interval, and the actual number of samples read.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### absolute timestamp

Timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.

Note

PXIe-5644/5645/5646

PXIe-5668

PXIe-5820/5840

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### relative timestamp

Timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location.

Note

PXIe-5644/5645/5646

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data points in the acquired signal.

The I/Q data sample rate is the reciprocal of this value.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### actual samples read

Integer representing the number of samples in the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### offset

Offset to scale data, (b), in 
mx + 
b form.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### gain

Gain to scale data, (m), in 
mx + 
b form.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Fetch IQ Data

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=fetch-iq-data-more-2d-i16.html language=enus -->
## TOPIC 00045: 2D I16

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `fetch-iq-data-more-2d-i16.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/fetch-iq-data-more-2d-i16.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches binary I/Q data from multiple records in an acquisition. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default valu

2D I16

Fetches binary I/Q data from multiple records in an acquisition.

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

##### samples to read

Number of samples to fetch.

A value of -1 specifies that NI-RFSA fetches all samples.

Note

NI-RFSA

Fetch Relative To

Fetch Offset

Default value: -1

##### Number of Samples Not Available

If the number of samples specified in this input is not available after the time duration specified in the timeout input, 
 [Fetch IQ](fetch-iq-data.html) returns no data with a timeout error.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time, in seconds, allotted for the node to complete before returning a timeout error. For the PXIe-5644/5645/5646, PXIe-5668, and the PXIe-5820/5840, this input specifies the time allotted to receive the reference trigger.

Default value: 10

##### Timeout Value Behaviors

A value of -1 specifies that the node waits until all data is available. A value of 0 specifies that the node immediately returns available data.

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### starting record

First record to retrieve.

Record numbers are zero-based.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### number of records

Number of records to fetch.

A value of -1 specifies that NI-RFSA fetches all records in an acquisition. Record numbers are zero-based.

Note

Default value: -1

##### Input Value Behaviors

If starting record is set to a value greater than 0, setting this input to -1 returns an error. If you set starting record to a value greater than 0, set this input to the exact number of records to fetch.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1di16.png']

##### data

Array of the acquired unscaled, complex waveform for each record.

##### Order of the Array

Each record occupies a row of the two-dimensional array. A record is composed of interleaved I and Q samples, where the order of the array is as follows:

- Array[0] = I(0)
- Array[1] = Q(0)
- Array[2] = I(1)
- Array[3] = Q(1)

[IMAGE alt='datatype_icon' src='/assets/img/i1dnclst.png']

##### wfm info

Absolute and relative timestamps for the operation, the time interval, and the actual number of samples read.

Each element of this array corresponds to a record.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### absolute timestamp

Timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.

Note

PXIe-5644/5645/5646

PXIe-5668

PXIe-5820/5840

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### relative timestamp

Timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location.

Note

PXIe-5644/5645/5646

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data points in the acquired signal.

The I/Q data sample rate is the reciprocal of this value.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### actual samples read

Integer representing the number of samples in the waveform.

Note

Number of Samples

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### offset

Offset to scale data, (b), in 
mx + 
b form.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### gain

Gain to scale data, (m), in 
mx + 
b form.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Fetch IQ Data

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=fetch-iq-data-multi-rec-1d-complex-cluster-csgl.html language=enus -->
## TOPIC 00046: 1D Complex Cluster CSGL

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `fetch-iq-data-multi-rec-1d-complex-cluster-csgl.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/fetch-iq-data-multi-rec-1d-complex-cluster-csgl.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches I/Q data from multiple records in an acquisition. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No e

1D Complex Cluster CSGL

Fetches I/Q data from multiple records in an acquisition.

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

##### samples to read

Number of samples to fetch.

A value of -1 specifies that NI-RFSA fetches all samples.

Note

NI-RFSA

Fetch Relative To

Fetch Offset

Default value: -1

##### Number of Samples Not Available

If the number of samples specified in this input is not available after the time duration specified in the timeout input, 
 [Fetch IQ](fetch-iq-data.html) returns no data with a timeout error.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time, in seconds, allotted for the node to complete before returning a timeout error. For the PXIe-5644/5645/5646, PXIe-5668, and the PXIe-5820/5840, this input specifies the time allotted to receive the reference trigger.

Default value: 10

##### Timeout Value Behaviors

A value of -1 specifies that the node waits until all data is available. A value of 0 specifies that the node immediately returns available data.

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### starting record

First record to retrieve.

Record numbers are zero-based.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### number of records

Number of records to fetch.

A value of -1 specifies that NI-RFSA fetches all records in an acquisition. Record numbers are zero-based.

Note

Default value: -1

##### Input Value Behaviors

If starting record is set to a value greater than 0, setting this input to -1 returns an error. If you set starting record to a value greater than 0, set this input to the exact number of records to fetch.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### data

Cluster of the acquired waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Start time of the first sample returned.

The timestamp corresponds to the difference in seconds between the first sample returned and the Reference Trigger location.

Note

t0

data

PXIe-5644/5645/5646

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data points in the acquired signal.

The I/Q data sample rate is the reciprocal of this value.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

Complex-value time domain data array.

The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

##### Calculating Instantaneous Power of a Sampled I/Q Point

To calculate the instantaneous power of a sampled I/Q point, use the equation (I<sup>2</sup> + Q<sup>2</sup>)/2R, where 
 R is the input impedance in ohms (Ω). For vector signal analyzers, 
 R = 50 Ω.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Fetch IQ Data

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=fetch-iq-data-multi-rec-1d-complex-cluster.html language=enus -->
## TOPIC 00047: 1D Complex Cluster

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `fetch-iq-data-multi-rec-1d-complex-cluster.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/fetch-iq-data-multi-rec-1d-complex-cluster.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches I/Q data from multiple records in an acquisition. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No e

1D Complex Cluster

Fetches I/Q data from multiple records in an acquisition.

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

##### samples to read

Number of samples to fetch.

A value of -1 specifies that NI-RFSA fetches all samples.

Note

NI-RFSA

Fetch Relative To

Fetch Offset

Default value: -1

##### Number of Samples Not Available

If the number of samples specified in this input is not available after the time duration specified in the timeout input, 
 [Fetch IQ](fetch-iq-data.html) returns no data with a timeout error.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time, in seconds, allotted for the node to complete before returning a timeout error. For the PXIe-5644/5645/5646, PXIe-5668, and the PXIe-5820/5840, this input specifies the time allotted to receive the reference trigger.

Default value: 10

##### Timeout Value Behaviors

A value of -1 specifies that the node waits until all data is available. A value of 0 specifies that the node immediately returns available data.

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### starting record

First record to retrieve.

Record numbers are zero-based.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### number of records

Number of records to fetch.

A value of -1 specifies that NI-RFSA fetches all records in an acquisition. Record numbers are zero-based.

Note

Default value: -1

##### Input Value Behaviors

If starting record is set to a value greater than 0, setting this input to -1 returns an error. If you set starting record to a value greater than 0, set this input to the exact number of records to fetch.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### data

Cluster of the acquired data.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Start time of the first sample returned.

The timestamp corresponds to the difference in seconds between the first sample returned and the Reference Trigger location.

Note

t0

data

PXIe-5644/5645/5646

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data points in the acquired signal.

The I/Q data sample rate is the reciprocal of this value.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

Complex-value time domain data array.

The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

##### Calculating Instantaneous Power of a Sampled I/Q Point

To calculate the instantaneous power of a sampled I/Q point, use the equation (I<sup>2</sup> + Q<sup>2</sup>)/2R, where 
 R is the input impedance in ohms (Ω). For vector signal analyzers, 
 R = 50 Ω.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Fetch IQ Data

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=fetch-iq-data-multi-rec-1d-complex-wdt.html language=enus -->
## TOPIC 00048: 1D Complex WDT (Waveform Datatype)

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `fetch-iq-data-multi-rec-1d-complex-wdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/fetch-iq-data-multi-rec-1d-complex-wdt.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches I/Q data from multiple records in an acquisition. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No e

1D Complex WDT (Waveform Datatype)

Fetches I/Q data from multiple records in an acquisition.

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

##### samples to read

Number of samples to fetch.

A value of -1 specifies that NI-RFSA fetches all samples.

Note

NI-RFSA

Fetch Relative To

Fetch Offset

Default value: -1

##### Number of Samples Not Available

If the number of samples specified in this input is not available after the time duration specified in the timeout input, 
 [Fetch IQ](fetch-iq-data.html) returns no data with a timeout error.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time, in seconds, allotted for the node to complete before returning a timeout error. For the PXIe-5644/5645/5646, PXIe-5668, and the PXIe-5820/5840, this input specifies the time allotted to receive the reference trigger.

Default value: 10

##### Timeout Value Behaviors

A value of -1 specifies that the node waits until all data is available. A value of 0 specifies that the node immediately returns available data.

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### starting record

First record to retrieve.

Record numbers are zero-based.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### number of records

Number of records to fetch.

A value of -1 specifies that NI-RFSA fetches all records in an acquisition. Record numbers are zero-based.

Note

Default value: -1

##### Input Value Behaviors

If starting record is set to a value greater than 0, setting this input to -1 returns an error. If you set starting record to a value greater than 0, set this input to the exact number of records to fetch.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### timestamp type

Time format of the data output.

Note

PXIe-5644/5645/5646

| Relative | The timestamp corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. |
| --- | --- |
| Absolute | The timestamp corresponds to the date and time of the acquisition of the first sample returned. |

Default value: Relative

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### data

Acquired waveform.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Fetch IQ Data

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=fetch-iq-data-single-rec-complex-cluster-csgl.html language=enus -->
## TOPIC 00049: Complex Cluster CSGL

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `fetch-iq-data-single-rec-complex-cluster-csgl.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/fetch-iq-data-single-rec-complex-cluster-csgl.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches I/Q data from a single record in an acquisition. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No er

Complex Cluster CSGL

Fetches I/Q data from a single record in an acquisition.

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

##### samples to read

Number of samples to fetch.

A value of -1 specifies that NI-RFSA fetches all samples.

Note

NI-RFSA

Fetch Relative To

Fetch Offset

Default value: -1

##### Number of Samples Not Available

If the number of samples specified in this input is not available after the time duration specified in the timeout input, 
 [Fetch IQ](fetch-iq-data.html) returns no data with a timeout error.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time, in seconds, allotted for the node to complete before returning a timeout error. For the PXIe-5644/5645/5646, PXIe-5668, and the PXIe-5820/5840, this input specifies the time allotted to receive the reference trigger.

Default value: 10

##### Timeout Value Behaviors

A value of -1 specifies that the node waits until all data is available. A value of 0 specifies that the node immediately returns available data.

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### record to fetch

Record to retrieve.

Record numbers are zero-based.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### data

Cluster of the acquired data.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Start time of the first sample returned.

The timestamp corresponds to the difference in seconds between the first sample returned and the Reference Trigger location.

Note

t0

data

PXIe-5644/5645/5646

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data points in the acquired signal.

The I/Q data sample rate is the reciprocal of this value.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

Complex-value time domain data array.

The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

##### Calculating Instantaneous Power of a Sampled I/Q Point

To calculate the instantaneous power of a sampled I/Q point, use the equation (I<sup>2</sup> + Q<sup>2</sup>)/2R, where 
 R is the input impedance in ohms (Ω). For vector signal analyzers, 
 R = 50 Ω.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Fetch IQ Data

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=fetch-iq-data-single-rec-complex-cluster.html language=enus -->
## TOPIC 00050: Complex Cluster

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `fetch-iq-data-single-rec-complex-cluster.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/fetch-iq-data-single-rec-complex-cluster.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches I/Q data from a single record in an acquisition. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No er

Complex Cluster

Fetches I/Q data from a single record in an acquisition.

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

##### samples to read

Number of samples to fetch.

A value of -1 specifies that NI-RFSA fetches all samples.

Note

NI-RFSA

Fetch Relative To

Fetch Offset

Default value: -1

##### Number of Samples Not Available

If the number of samples specified in this input is not available after the time duration specified in the timeout input, 
 [Fetch IQ](fetch-iq-data.html) returns no data with a timeout error.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time, in seconds, allotted for the node to complete before returning a timeout error. For the PXIe-5644/5645/5646, PXIe-5668, and the PXIe-5820/5840, this input specifies the time allotted to receive the reference trigger.

Default value: 10

##### Timeout Value Behaviors

A value of -1 specifies that the node waits until all data is available. A value of 0 specifies that the node immediately returns available data.

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### record to fetch

Record to retrieve.

Record numbers are zero-based.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### data

Cluster of the acquired data.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Start time of the first sample returned.

The timestamp corresponds to the difference in seconds between the first sample returned and the Reference Trigger location.

Note

t0

data

PXIe-5644/5645/5646

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data points in the acquired signal.

The I/Q data sample rate is the reciprocal of this value.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

Complex-value time domain data array.

The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

Note

Number of Samples

##### Calculating Instantaneous Power of a Sampled I/Q Point

To calculate the instantaneous power of a sampled I/Q point, use the equation (I<sup>2</sup> + Q<sup>2</sup>)/2R, where 
 R is the input impedance in ohms (Ω). For vector signal analyzers, 
 R=50 Ω.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Fetch IQ Data

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=fetch-iq-data-single-rec-complex-wdt.html language=enus -->
## TOPIC 00051: Complex WDT (Waveform Datatype)

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `fetch-iq-data-single-rec-complex-wdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/fetch-iq-data-single-rec-complex-wdt.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches I/Q data from a single record in an acquisition. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No er

Complex WDT (Waveform Datatype)

Fetches I/Q data from a single record in an acquisition.

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

##### samples to read

Number of samples to fetch.

A value of -1 specifies that NI-RFSA fetches all samples.

Note

NI-RFSA

Fetch Relative To

Fetch Offset

Default value: -1

##### Number of Samples Not Available

If the number of samples specified in this input is not available after the time duration specified in the timeout input, 
 [Fetch IQ](fetch-iq-data.html) returns no data with a timeout error.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Time, in seconds, allotted for the node to complete before returning a timeout error. For the PXIe-5644/5645/5646, PXIe-5668, and the PXIe-5820/5840, this input specifies the time allotted to receive the reference trigger.

Default value: 10

##### Timeout Value Behaviors

A value of -1 specifies that the node waits until all data is available. A value of 0 specifies that the node immediately returns available data.

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### record to fetch

Record to retrieve.

Record numbers are zero-based.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### timestamp type

Time format of the data output.

Note

PXIe-5644/5645/5646

| Relative | The timestamp corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. |
| --- | --- |
| Absolute | The timestamp corresponds to the date and time of the acquisition of the first sample returned. |

Default value: Relative

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### data

Baseband (downconverted) time-domain data for demodulation.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Fetch IQ Data

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=fetch-iq-data.html language=enus -->
## TOPIC 00052: Fetch IQ Data

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `fetch-iq-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/fetch-iq-data.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transfers acquired waveform data from device memory to computer memory; this process is also known as fetching.The data transferred is acquired to onboard memory previously by the hardware after the acquisition is initiated.

Fetch IQ Data

Transfers acquired waveform data from device memory to computer memory; this process is also known as fetching.The data transferred is acquired to onboard memory previously by the hardware after the acquisition is initiated.

Low Level Measurement

Parent topic:

Low Level Measurement

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=get-calibration-user-defined-info.html language=enus -->
## TOPIC 00053: Get Calibration User Defined Info

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `get-calibration-user-defined-info.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/get-calibration-user-defined-info.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns user-defined information from the onboard EEPROM. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No e

Get Calibration User Defined Info

Returns user-defined information from the onboard EEPROM.

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

##### user defined info

String that returns the user-defined information.

#### Hardware Support

This node supports the following hardware:

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5693/5694/5698

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=get-external-cal-interval.html language=enus -->
## TOPIC 00054: Get External Calibration Recommended Interval

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `get-external-cal-interval.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/get-external-cal-interval.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recommended interval between external calibrations, in months. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior De

Get External Calibration Recommended Interval

Returns the recommended interval between external calibrations, in months.

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

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### months

Returns the recommended maximum interval between external calibrations, in months.

#### Hardware Support

This node supports the following hardware:

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663/5663E/5665/5667/5668
- PXIe-5693/5694/5698
- PXIe-5820/5840

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=get-external-cal-last-date-and-time.html language=enus -->
## TOPIC 00055: Get External Calibration Last Date and Time

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `get-external-cal-last-date-and-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/get-external-cal-last-date-and-time.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time of the last successful external calibration. The time returned is 24-hour local time and the date is returned as integer values. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node respond

Get External Calibration Last Date and Time

Returns the date and time of the last successful external calibration.

The time returned is 24-hour local time and the date is returned as integer values.

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

##### year

Year of the last external calibration.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### hour

Hour of the last external calibration.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### minute

Minute of the last external calibration.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### month

Month of the last external calibration.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### day

Day of the last external calibration.

#### Hardware Support

This node supports the following hardware:

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5693/5694/5698
- PXIe-5820/5840

#### Example Date and Time Format

If the device was calibrated at 2:30 PM on December 31, 2010, this node returns 
 **14** for the hour output, 
 **30** for the minute output, 
 **12** for the month output, 
 **31** for the day output, and 
 **2010** for the year output.

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=get-external-cal-last-temp.html language=enus -->
## TOPIC 00056: Get External Calibration Last Temp

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `get-external-cal-last-temp.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/get-external-cal-last-temp.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the temperature, in degrees Celsius, at the last successful external calibration. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Er

Get External Calibration Last Temp

Returns the temperature, in degrees Celsius, at the last successful external calibration.

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

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### temperature

Temperature, in degrees Celsius, of the last external calibration.

#### Hardware Support

This node supports the following hardware:

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5693/5694/5698

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Downconverter with External Digitizer

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=get-fetch-backlog.html language=enus -->
## TOPIC 00057: Get Fetch Backlog

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `get-fetch-backlog.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/get-fetch-backlog.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of points acquired that have not yet been fetched. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default

Get Fetch Backlog

Returns the number of points acquired that have not yet been fetched.

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

##### record number

Record from which to read the backlog.

Record numbers are zero-based.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii64.png']

##### backlog

Number of samples available to read for the requested record.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Low Level Measurement Information

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=get-frequency-response.html language=enus -->
## TOPIC 00058: Get Frequency Response

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `get-frequency-response.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/get-frequency-response.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the requested response type, based on current NI-RFSA settings. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Defau

Get Frequency Response

Returns the requested response type, based on current NI-RFSA settings.

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

##### response type

Type of response (IF, RF, or combined (IF and RF)) of the downconverter or NI-RFSA device that NI-RFSA returns.

| Downconverter IF Response | Returns the IF response of the downconverter. |
| --- | --- |
| Downconverter RF Response | Returns the RF response of the downconverter. This value is supported on only the PXIe-5603/5605/5606, PXIe-5665/5667/5668, and PXIe-5593. |
| Downconverter Combined Response | Returns the combined RF and IF response of the downconverter. The combined response is in terms of IF frequency. This value is supported on only the PXIe-5603/5605/5606, PXIe-5665/5667/5668. |
| VSA IF Response | Returns the IF response of the entire device. This value is supported on only the PXIe-5665/5667/5668. |
| VSA Combined Response | Returns the combined IF and RF response of the entire NI-RFSA device. The combined response is in terms of IF frequency. This value is supported on only the PXIe-5665/5667/5668. |

Default value: 
 Downconverter IF Response

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### frequencies

Array containing the frequencies, in hertz (Hz), that correspond to the response data.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### magnitude response

Array containing the magnitude response, in decibels (dB).

The magnitude response is normalized to the center frequency at each frequency in the frequencies output.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### phase response

Array containing the phase response, in radians.

The phase response is normalized to the center frequency at each frequency entry in the frequencies output.

This array may contain zeros if the device does not contain a stored phase response in its calibration data.

#### Hardware Support

This node supports the following hardware:

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5663E/5665/5667/5668
- PXIe-5693/5694/5698

#### Automatic IF and RF Response Correction

The PXIe-5663E/5665/5667/5668 automatically corrects the IF and RF response when you set the Digital IF Equalization Enabled property to True.

#### External Digitizer Mode

If you are using external digitizer mode, you can use information returned from this node to correct your measurement.

Parent topic:

Low Level Measurement Information

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=get-iq-components.html language=enus -->
## TOPIC 00059: Get IQ Components

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `get-iq-components.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/get-iq-components.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accepts waveform data and returns the I and Q data as waveform data types. Use this node to graph either the I or Q components or to perform operations that apply to one or the other component. error in Error conditions that occur before this node runs. The node responds to this input according to s

Get IQ Components

Accepts waveform data and returns the I and Q data as waveform data types.

Use this node to graph either the I or Q components or to perform operations that apply to one or the other component.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### data

Acquired waveform.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### I

In-phase (I) component of the data.

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### Q

Quadrature (Q) component of the data.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### number of samples

Number of samples in the input waveform.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5840/5820

Parent topic:

Low Level Measurement Information

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=get-ni-tclk-session-reference.html language=enus -->
## TOPIC 00060: Get NI-TClk Session Reference

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `get-ni-tclk-session-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/get-ni-tclk-session-reference.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts a session that can be passed to NI-TClk nodes. Session references are of generic type, which means that the corresponding wires are blue-green, unlike the wires for regular instrument driver sessions. session in Instrument session obtained from Initialize With Options. error in Error condit

Get NI-TClk Session Reference

Extracts a session that can be passed to NI-TClk nodes.

Session references are of generic type, which means that the corresponding wires are blue-green, unlike the wires for regular instrument driver sessions.

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

#### Hardware Support

This node supports the following hardware:

- PXIe-5663E/5665/5667
- PXIe-5820/5840

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=get-scaling-coefficients.html language=enus -->
## TOPIC 00061: Get Scaling Coefficients

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `get-scaling-coefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/get-scaling-coefficients.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns coefficients you can use to convert unscaled data to scaled I/Q data. The coefficients are calculated by NI-RFSA for the current configuration of the device, so they are valid only for acquisitions obtained with the same device configuration. session in Instrument session obtained from Initi

Get Scaling Coefficients

Returns coefficients you can use to convert unscaled data to scaled I/Q data.

Note

NI-RFSA

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

[IMAGE alt='datatype_icon' src='/assets/img/i1dnclst.png']

##### coefficient info

Array with coefficient information.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### offset

Number to add to the data from a peer-to-peer stream after the gain has been applied in order to scale unscaled data.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### gain

Multiplier to use to scale data obtained from a peer-to-peer stream.

#### Hardware Support

This node supports the following hardware:

- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

#### Scaling I/Q Values

Acquired data may be unscaled when sent by a peer-to-peer stream or when fetched as unscaled data. Use this node to scale such I/Q values.

#### Obtaining Scaled I/Q Values

The coefficient info array returns one cluster that contains gain and offset elements. To obtain scaled I/Q values, multiply the unscaled data by the gain value of the cluster, then add the offset.

Parent topic:

Low Level Measurement Information

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=get-self-cal-last-date-time.html language=enus -->
## TOPIC 00062: Get Self Calibration Last Date And Time

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `get-self-cal-last-date-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/get-self-cal-last-date-time.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time of the last successful self-calibration. The time returned is 24-hour local time and the date is returned as integer values. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to

Get Self Calibration Last Date And Time

Returns the date and time of the last successful self-calibration.

The time returned is 24-hour local time and the date is returned as integer values.

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

##### self cal step 2

Self-calibration step to query for the last successful self-calibration date and time data.

| Preselector Alignment | Selects the Preselector Alignment self-calibration step. |
| --- | --- |
| Gain Reference | Selects the Gain Reference self-calibration step. |
| IF Flatness | Selects the IF Flatness self-calibration step. |
| Digitizer Self Cal | Selects the Digitizer Self Cal self-calibration step. |
| LO Self Cal | Selects the LO Self Cal self-calibration step. |
| Amplitude Accuracy | Selects the Amplitude Accuracy self-calibration step. |
| Residual LO Power | Selects the Residual LO Power self-calibration step. |
| Image Suppression | Selects the Image Suppression self-calibration step. |
| Synthesizer Alignment | Selects the Synthesizer Alignment self-calibration step. |
| DC Offset | Selects the DC Offset self-calibration step. |

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### year

Year of the last self-calibration.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### hour

Hour of the last self-calibration.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### month

Month of the last self-calibration.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### day

Day of the last self-calibration.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### minute

Minute of the last self-calibration.

#### Hardware Support

This node supports the following hardware:

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

#### Example Date and Time Format

If the device was calibrated at 2:30 PM on December 31, 2010, this node returns 
 **14** for the hour output, 
 **30** for the minute output, 
 **12** for the month output, 
 **31** for the day output, and 
 **2010** for the year output.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=get-self-cal-last-temp.html language=enus -->
## TOPIC 00063: Get Self Calibration Last Temp

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `get-self-cal-last-temp.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/get-self-cal-last-temp.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the temperature, in degrees Celsius, at the last successful self-calibration. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error

Get Self Calibration Last Temp

Returns the temperature, in degrees Celsius, at the last successful self-calibration.

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

##### self cal step 2

Self-calibration step to query for the last successful self-calibration temperature data.

Note

PXIe-5644/5645/5646

Image Suppression

sel cal step

| Preselector Alignment | Selects the Preselector Alignment self-calibration step. |
| --- | --- |
| Gain Reference | Selects the Gain Reference self-calibration step. |
| IF Flatness | Selects the IF Flatness self-calibration step. |
| Digitizer Self Cal | Selects the Digitizer Self Cal self-calibration step. |
| LO Self Cal | Selects the LO Self Cal self-calibration step. |
| Amplitude Accuracy | Selects the Amplitude Accuracy self-calibration step. |
| Residual LO Power | Selects the Residual LO Power self-calibration step. |
| Image Suppression | Selects the Image Suppression self-calibration step. |
| Synthesizer Alignment | Selects the Synthesizer Alignment self-calibration step. |
| DC Offset | Selects the DC Offset self-calibration step. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### temperature

Temperature, in degrees Celsius, at the last self-calibration.

#### Hardware Support

This node supports the following hardware:

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=get-stream-endpoint-handle.html language=enus -->
## TOPIC 00064: Get Stream Endpoint Handle

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `get-stream-endpoint-handle.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/get-stream-endpoint-handle.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a writer endpoint handle that you can use with NI-P2P to configure a peer-to-peer stream with the digitizer as an endpoint. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input accordi

Get Stream Endpoint Handle

Returns a writer endpoint handle that you can use with NI-P2P to configure a peer-to-peer stream with the digitizer as an endpoint.

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

Name of the stream resources you want to use.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### writer handle

Writer endpoint handle which you use with NI-P2P to create a stream with the digitizer as an endpoint.

#### Hardware Support

This node supports the following hardware:

- PXIe-5663E/5665/5667
- PXIe-5820/5840

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=get-terminal-name.html language=enus -->
## TOPIC 00065: Get Terminal Name

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `get-terminal-name.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/get-terminal-name.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified name of the signal being queried. Signals can be triggers, clocks, or events. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behav

Get Terminal Name

Returns the fully qualified name of the signal being queried.

Signals can be triggers, clocks, or events.

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

Signal for which you want to query the terminal.

| Start Trigger | NI-RFSA returns the terminal name for the Start Trigger. |
| --- | --- |
| Ref Trigger | NI-RFSA returns the terminal name for the Reference Trigger. |
| Advance Trigger | NI-RFSA returns the terminal name for the Advance Trigger. |
| Ready for Start Event | NI-RFSA returns the terminal name for the Ready for Start Event. |
| Ready for Ref Event | NI-RFSA returns the terminal name for the Ready for Reference Event. |
| Ready for Advance Event | NI-RFSA returns the terminal name for the Ready for Advance Event. |
| End of Record Event | NI-RFSA returns the terminal name for the End of Record Event. |
| Done Event | NI-RFSA returns the terminal name for the Done Event. |
| Reference Clock | NI-RFSA does not support this option for Get Terminal Name. |
| User | NI-RFSA routes a user-defined signal. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### signal identifier

User-defined signal to route.

Specify the signal you have implemented using FPGA extensions.

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

Fully qualified name of the signal being queried.

You can pass the this output to the source input of [Configure Trigger](configure-trigger.html).

#### Hardware Support

This node supports the following hardware:

- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=init-external-calibration.html language=enus -->
## TOPIC 00066: Init External Calibration

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `init-external-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/init-external-calibration.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates and initializes a special NI-RFSA external calibration session. The session out returned is an NI-RFSA session that you can use to configure the device using normal properties and nodes. However, NI-RFSA sets flags that allow you to program an external calibration procedure using the calibra

Init External Calibration

Creates and initializes a special NI-RFSA external calibration session.

The session out returned is an NI-RFSA session that you can use to configure the device using normal properties and nodes. However, NI-RFSA sets flags that allow you to program an external calibration procedure using the calibration properties and nodes.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### resource name

Resource name of the device to initialize.

##### Renaming Your Device in MAX

For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is 
 PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting 
 Rename from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility.

Note

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### password

Password for the calibration session.

The initial password is factory configured to 
 NI. The password can be a maximum of ten alphanumeric characters.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### option string

Initial value of certain properties for the session.

You can set the following properties using this input:

- Range Check
- Query Instrument Status
- Cache
- Driver Setup
- Simulate

##### Option String Syntax

The format of this string is 
 "PropertyName=Value'" where 
 PropertyName is the name of the property and 
 Value is the value to which the property is set. To set multiple properties, separate their assignments with a comma.

| Property | Use | Valid Values | Example String Syntax |
| --- | --- | --- | --- |
| Range Check | Specify whether to validate property values and node parameters. | 0 (false), 1 (true) | "RangeCheck=1" |
| Query Instrument Status | Query the device status after each operation. | 0 (false), 1 (true) | "QueryInstrumentStatus=1" |
| Cache | Cache the value of properties. | 0 (false), 1 (true) | "Cache=1" |
| Driver Setup | Specify an FPGA bitfile, enable soft front panel (SFP) session access, or specify a device. | Refer to Driver Setup Options for more information about using the driver setup string, including valid values. | "DriverSetup=SFPSessionAccess:1;LO:my5652" |
| Simulate | Simulate I/O operations using NI-RFSA. | 0 (false), 1 (true) | "Simulate=1" |

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

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5693/5694/5698
- PXIe-5820/5840

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=initialize-external-alignment-step.html language=enus -->
## TOPIC 00067: Initialize External Alignment Step

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `initialize-external-alignment-step.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/initialize-external-alignment-step.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an EEPROM-specific external alignment step. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No err

Initialize External Alignment Step

Initializes an EEPROM-specific external alignment step.

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

##### ext align step

External alignment step that you want to initialize.

| Preselector Alignment | Initiates preselector alignment. This step generates coefficients to align the preselector across the frequency range of 3.6 GHz to 14 GHz for the PXIe-5605 and the frequency range of 3.6 GHz to 26.5 GHz for the PXIe-5606. |
| --- | --- |

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

- PXIe-5605 (PXIe-5665 only)
- PXIe-5606 (PXIe-5668 only)

#### Programming Patterns

You must call 
 [Close External Alignment Step](close-external-alignment-step.html) after you call this node to complete the external alignment.

Parent topic:

External Alignment

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=initialize-external-alignment.html language=enus -->
## TOPIC 00068: Initialize External Alignment

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `initialize-external-alignment.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/initialize-external-alignment.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates and initializes a special NI-RFSA external alignment session. resource name Resource name of the device to initialize. Device Name Syntax For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your dev

Initialize External Alignment

Creates and initializes a special NI-RFSA external alignment session.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### resource name

Resource name of the device to initialize.

##### Device Name Syntax

For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is 
 PXI1Slot2. You can rename your devices by right-clicking the name in MAX, selecting 
 Rename from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility.

Note

##### Creating a New Session for a Vector Signal Analyzer

To create a new session for your vector signal analyzer, you must wire the downconverter resource name to this input.

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
- Driver Setup
- Simulate

##### Option String Syntax

The format of this string is 
 "PropertyName=Value'" where 
 PropertyName is the name of the property and 
 Value is the value to which the property is set. To set multiple properties, separate their assignments with a comma.

| Property | Use | Valid Values | Example String Syntax |
| --- | --- | --- | --- |
| Range Check | Specify whether to validate property values and node parameters. | 0 (false), 1 (true) | "RangeCheck=1" |
| Query Instrument Status | Query the device status after each operation. | 0 (false), 1 (true) | "QueryInstrumentStatus=1" |
| Cache | Cache the value of properties. | 0 (false), 1 (true) | "Cache=1" |
| Driver Setup | Specify an FPGA bitfile, enable soft front panel (SFP) session access, or specify a device. | Refer to Driver Setup Options for more information about using the driver setup string, including valid values. | "DriverSetup=SFPSessionAccess:1;LO:my5652" |
| Simulate | Simulate I/O operations using NI-RFSA. | 0 (false), 1 (true) | "Simulate=1" |

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

- PXIe-5605 (PXIe-5665 only)
- PXIe-5606 (PXIe-5668 only)

#### External Alignment Session

The session out returned is an NI-RFSA session that you can use to configure your device using normal properties and nodes. However, NI-RFSA sets flags that allow you to additionally program an external alignment procedure using specific external alignment properties and nodes. The NI-RFSA external alignment session is an alternative to 
 [Self Calibrate](self-calibrate.html) that you should use when you require external hardware to perform typically self-contained self-calibration steps.

Parent topic:

External Alignment

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=initialize-with-options.html language=enus -->
## TOPIC 00069: Initialize With Options

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `initialize-with-options.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/initialize-with-options.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new session for the hardware, sets initial values of certain properties for the session, and sends initialization commands to reset all hardware modules to a known state necessary for NI-RFSA operation. resource name Resource name of the device to initialize. Device Name Syntax For NI-RFSA

Initialize With Options

Creates a new session for the hardware, sets initial values of certain properties for the session, and sends initialization commands to reset all hardware modules to a known state necessary for NI-RFSA operation.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### resource name

Resource name of the device to initialize.

##### Device Name Syntax

For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is 
 PXI1Slot2. You can rename your devices by right-clicking the name in MAX, selecting 
 Rename from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility.

Note

##### Creating a New Session for a Vector Signal Analyzer

To create a new session for your vector signal analyzer, you must wire the downconverter resource name to this input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### id query

Boolean value that indicates whether NI-RFSA performs an ID query.

When you perform an ID query, NI-RFSA verifies the device you initialize is supported.

| True | NI-RFSA performs an ID query. |
| --- | --- |
| False | NI-RFSA does not perform an ID query. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

Boolean value that specifies whether the NI-RFSA device is reset during the initialization procedure.

| True | The device is reset. |
| --- | --- |
| False | The device is not reset. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### option string

Initial value of certain properties for the session.

You can set the following properties using this input:

- Range Check
- Query Instrument Status
- Cache
- Driver Setup
- Simulate

##### Option String Syntax

The format of this string is 
 "PropertyName=Value'" where 
 PropertyName is the name of the property and 
 Value is the value to which the property is set. To set multiple properties, separate their assignments with a comma.

| Property | Use | Valid Values | Example String Syntax |
| --- | --- | --- | --- |
| Range Check | Specify whether to validate property values and node parameters. | 0 (false), 1 (true) | "RangeCheck=1" |
| Query Instrument Status | Query the device status after each operation. | 0 (false), 1 (true) | "QueryInstrumentStatus=1" |
| Cache | Cache the value of properties. | 0 (false), 1 (true) | "Cache=1" |
| Driver Setup | Specify an FPGA bitfile, enable soft front panel (SFP) session access, or specify a device. | Refer to Driver Setup Options for more information about using the driver setup string, including valid values. | "DriverSetup=SFPSessionAccess:1;LO:my5652" |
| Simulate | Simulate I/O operations using NI-RFSA. | 0 (false), 1 (true) | "Simulate=1" |

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

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5693/5694/5698
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Downconverter with External Digitizer
- RFSA In-band Retuning with External LO

#### Accessing the Device Session with the Soft Front Panel

You can access the new device session using the NI-RFSA Soft Front Panel (SFP). Accessing the device session with the SFP can help you debug your code.

To enable SFP session access, create a new session for your device by wiring the following string into the option string input: 
 DriverSetup=SFPSessionAccess:1.

To disable SFP session access, wire the following string into the option string input: 
 DriverSetup=SFPSessionAccess:0.

Parent topic:

NI-RFSA Nodes

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=initiate.html language=enus -->
## TOPIC 00070: Initiate

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `initiate.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/initiate.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to hardware, waits for hardware settling, and starts an acquisition. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error

Initiate

Commits settings to hardware, waits for hardware settling, and starts an acquisition.

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

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5693/5694/5698
- PXIe-5820/5840

#### Retrieving I/Q Data

Fetch IQ

Read IQ

#### External Digitizer Mode Behavior

Commit

Parent topic:

Low Level Measurement

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=iq.html language=enus -->
## TOPIC 00071: IQ

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `iq.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/iq.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

IQ

Configuration

Configure IQ Carrier Frequency

Configures the carrier frequency of the vector signal analyzer hardware for an I/Q acquisition.

Configure IQ Rate

Specifies the I/Q rate, in samples per second (S/s), for the acquisition.

Configure Number of Samples

Configures the number of samples in a finite acquisition or configures the device to continuously acquire samples.

Configure Number of Records

Configures the number of records in a finite acquisition or configures the device to continuously acquire records.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=is-self-calibration-valid.html language=enus -->
## TOPIC 00072: Is Self Calibration Valid?

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `is-self-calibration-valid.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/is-self-calibration-valid.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array to indicate which calibration steps contain valid calibration data. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error B

Is Self Calibration Valid?

Returns an array to indicate which calibration steps contain valid calibration data.

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

##### self calibration valid

Boolean value that indicates whether the calibration data is valid.

| True | The calibration data is valid. |
| --- | --- |
| False | The calibration data is invalid. |

[IMAGE alt='datatype_icon' src='/assets/img/i1di64.png']

##### valid steps

Valid steps.

| Preselector Alignment | Indicates the Preselector Alignment calibration data is valid. This step generates coefficients to align the preselector across the frequency range for your device. |
| --- | --- |
| Gain Reference | Indicates the Gain Reference calibration data is valid. This step measures the changes in gain since the last external calibration was run. |
| IF Flatness | Indicates the IF Flatness calibration data is valid. This step measures the IF response of the entire system for each of the supported IF filters. |
| Digitizer Self Cal | Indicates the Digitizer Self Cal calibration data is valid. This step calls for digitizer self-calibration, if the digitizer is associated with the RF downconverter. |
| LO Self Cal | Indicates the LO Self Cal calibration data is valid. This step calls for LO self-calibration, if the LO source module is associated with the RF downconverter. |

#### Hardware Support

This node supports the following hardware:

- PXIe-5663E/5665/5667/5668

#### Omitting Steps

To omit steps with valid calibration data from self-calibration, you can pass the valid steps output to the steps to omit input of 
 [Self Calibration](self-calibrate.html).

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=low-level-measurement-info.html language=enus -->
## TOPIC 00073: Low Level Measurement Information

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `low-level-measurement-info.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/low-level-measurement-info.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Low Level Measurement Information

Low Level Measurement

Get Fetch Backlog

Returns the number of points acquired that have not yet been fetched.

Get IQ Components

Accepts waveform data and returns the I and Q data as waveform data types.

Get Scaling Coefficients

Returns coefficients you can use to convert unscaled data to scaled I/Q data.

Get Frequency Response

NI-RFSA

Parent topic:

Low Level Measurement

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=low-level-measurement.html language=enus -->
## TOPIC 00074: Low Level Measurement

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `low-level-measurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/low-level-measurement.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Low Level Measurement

Measurement

Initiate

Commits settings to hardware, waits for hardware settling, and starts an acquisition.

Fetch IQ Data

Transfers acquired waveform data from device memory to computer memory; this process is also known as fetching.The data transferred is acquired to onboard memory previously by the hardware after the acquisition is initiated.

Abort

Initiate

Read Power Spectrum

Check Acquisition Status

Checks the status of the acquisition.

Send Software Edge Trigger

Configure Trigger

Commit

Commits settings to hardware.

Low Level Measurement Information

Parent topic:

Measurement

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=measurement.html language=enus -->
## TOPIC 00075: Measurement

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `measurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/measurement.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Measurement

NI-RFSA Nodes

Use NI-RFSA nodes to develop applications for your vector signal analyzer.

Read Power Spectrum

Initiates a spectrum acquisition and returns power spectrum data.

Read IQ Data

Initiates an acquisition and fetches a single I/Q data record.Do not use this node if you have configured the device to continuously acquire data samples or to acquire multiple records.

Low Level Measurement

Parent topic:

NI-RFSA Nodes

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=ni-rfsa-properties.html language=enus -->
## TOPIC 00076: NI-RFSA Properties

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `ni-rfsa-properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/ni-rfsa-properties.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads), sets (writes), or resets (sets to default value) NI-RFSA properties. When you read a property, NI-RFSA analyzes the current configuration to return the coerced value for that property. NI-RFSA verifies many properties upon reading, thereby either transitioning the session to the verifi

NI-RFSA Properties

Gets (reads), sets (writes), or resets (sets to default value) NI-RFSA properties.

When you read a property, NI-RFSA analyzes the current configuration to return the coerced value for that property. NI-RFSA verifies many properties upon reading, thereby either transitioning the session to the verified state or alerting you of an invalid configuration. Setting or resetting a property transitions the session to an unverified state.

For a list of supported properties, refer to NI-RFSA Properties.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### NI-RFSA in

Instrument session obtained from [Initialize With Options](initialize-with-options.html).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### NI-RFSA out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

NI-RFSA Nodes

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=nirfsa-nodes.html language=enus -->
## TOPIC 00077: NI-RFSA Nodes

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `nirfsa-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/nirfsa-nodes.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use NI-RFSA nodes to develop applications for your vector signal analyzer.

NI-RFSA Nodes

Use NI-RFSA nodes to develop applications for your vector signal analyzer.

Initialize With Options

NI-RFSA

Close

Closes the session to the device.

NI-RFSA Properties

NI-RFSA

Configuration

Measurement

Utility

Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=perform-thermal-correction.html language=enus -->
## TOPIC 00078: Perform Thermal Correction

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `perform-thermal-correction.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/perform-thermal-correction.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Corrects for temperature variations while acquiring the same signal for extended periods of time in a continuous acquisition. You cannot call this node if your device is operating in RF list mode. session in Instrument session obtained from Initialize With Options. error in Error conditions that occ

Perform Thermal Correction

Corrects for temperature variations while acquiring the same signal for extended periods of time in a continuous acquisition.

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

- PXIe-5663E/5665/5667/5668
- PXIe-5693/5694
- PXIe-5840

#### Frequency of Node Use

NI-RFSA internally acquires the temperature every time you initiate an acquisition. If you are performing a continuous acquisition, National Instruments recommends calling this node once every 10 minutes in a stable temperature environment to periodically update temperature calibration. If the ambient temperature varies, call this node more frequently.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=read-iq-data-complex-cluster.html language=enus -->
## TOPIC 00079: Complex Cluster

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `read-iq-data-complex-cluster.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/read-iq-data-complex-cluster.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q data as a complex cluster. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error timeout Ti

Complex Cluster

Returns the I/Q data as a complex cluster.

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

##### timeout

Time, in seconds, allotted for the node to complete before returning a timeout error.

A value of -1 specifies that the node waits until all data is available.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### data

Cluster of the acquired data.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### t0

Start time of the first sample returned.

The timestamp corresponds to the difference in seconds between the first sample returned and the Reference Trigger location.

Note

t0

data

PXIe-5644/5645/5646

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### dt

Time interval between data points in the acquired signal.

The I/Q data sample rate is the reciprocal of this value.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcdb.png']

##### Y

Complex-value time domain data array.

The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

##### Calculating Instantaneous Power of a Sampled I/Q Point

To calculate the instantaneous power of a sampled I/Q point, use the equation (I<sup>2</sup> + Q<sup>2</sup>)/2R, where 
 R is the input impedance in ohms (Ω). For vector signal analyzers, 
 R = 50 Ω.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Read IQ Data

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=read-iq-data-complex-wdt.html language=enus -->
## TOPIC 00080: Complex WDT (Waveform Datatype)

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `read-iq-data-complex-wdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/read-iq-data-complex-wdt.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q data as a complex WDT. timestamp type Time format of the data output. The value of the timestamps returned is always 0 for the PXIe-5644/5645/5646. Relative The timestamp corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location.

Complex WDT (Waveform Datatype)

Returns the I/Q data as a complex WDT.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### timestamp type

Time format of the data output.

Note

PXIe-5644/5645/5646

| Relative | The timestamp corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. |
| --- | --- |
| Absolute | The timestamp corresponds to the date and time of the acquisition of the first sample returned. |

Default value: Relative

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

##### timeout

Time, in seconds, allotted for the node to complete before returning a timeout error.

A value of -1 specifies that the node waits until all data is available.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### data

Baseband (downconverted) time-domain data for demodulation.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Read IQ Data

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=read-iq-data.html language=enus -->
## TOPIC 00081: Read IQ Data

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `read-iq-data.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/read-iq-data.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates an acquisition and fetches a single I/Q data record.Do not use this node if you have configured the device to continuously acquire data samples or to acquire multiple records.

Read IQ Data

Initiates an acquisition and fetches a single I/Q data record.Do not use this node if you have configured the device to continuously acquire data samples or to acquire multiple records.

Measurement

Complex WDT (Waveform Datatype)

Returns the I/Q data as a complex WDT.

Complex Cluster

Returns the I/Q data as a complex cluster.

Parent topic:

Measurement

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=read-power-spectrum-cluster-dbl.html language=enus -->
## TOPIC 00082: Cluster DBL

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `read-power-spectrum-cluster-dbl.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/read-power-spectrum-cluster-dbl.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates a spectrum acquisition and returns double precision power spectrum data. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Beh

Cluster DBL

Initiates a spectrum acquisition and returns double precision power spectrum data.

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

##### timeout

Time, in seconds, allotted for the node to complete before returning a timeout error.

A value of -1 specifies that the node waits until all data is available.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### power spectrum

Power spectrum data.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### f0

Center frequency, in Hz, of the first bin of the power spectrum data.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### df

Frequency interval, in Hz, between data points in the spectrum.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### data

Array of the acquired waveform.

If averaging is enabled, this output returns the averaged power spectrum.

#### Hardware Support

This node supports the following hardware:

- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

Parent topic:

Read Power Spectrum

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=read-power-spectrum-cluster-sgl.html language=enus -->
## TOPIC 00083: Cluster SGL

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `read-power-spectrum-cluster-sgl.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/read-power-spectrum-cluster-sgl.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates a spectrum acquisition and returns single precision power spectrum data. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Beh

Cluster SGL

Initiates a spectrum acquisition and returns single precision power spectrum data.

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

##### timeout

Time, in seconds, allotted for the node to complete before returning a timeout error.

A value of -1 specifies that the node waits until all data is available.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### power spectrum

Power spectrum data.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### f0

Center frequency, in Hz, of the first bin of the power spectrum data.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### df

Frequency interval, in Hz, between data points in the spectrum.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### data

Array of the acquired waveform.

If averaging is enabled, this output returns the averaged power spectrum.

#### Hardware Support

This node supports the following hardware:

- PXIe-5820/5840

Parent topic:

Read Power Spectrum

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=read-power-spectrum.html language=enus -->
## TOPIC 00084: Read Power Spectrum

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `read-power-spectrum.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/read-power-spectrum.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates a spectrum acquisition and returns power spectrum data.

Read Power Spectrum

Initiates a spectrum acquisition and returns power spectrum data.

Measurement

Cluster DBL

Initiates a spectrum acquisition and returns double precision power spectrum data.

Cluster SGL

Initiates a spectrum acquisition and returns single precision power spectrum data.

Parent topic:

Measurement

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=reset-device.html language=enus -->
## TOPIC 00085: Reset Device

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `reset-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/reset-device.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a hard reset on the device. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session out Refe

Reset Device

Performs a hard reset on the device.

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

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5663E/5665/5667/5668
- PXIe-5693/5694/5698

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Downconverter with External Digitizer

#### Hard Reset Behavior

A hard reset consists of the following actions:

- Signal acquisition is stopped.
- All routes are released.
- External bidirectional terminals are tristated.
- FPGAs are reset.
- Hardware is configured to its default state.
- All session properties are reset to their default states.

During a device reset, routes of signals between this and other devices are released, regardless of which device created the route. For example, a trigger signal exported to a PXI trigger line that is used by another device is no longer exported.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=reset.html language=enus -->
## TOPIC 00086: Reset

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `reset.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/reset.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets all properties to default values and stops export of all external signals and events. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard

Reset

Resets all properties to default values and stops export of all external signals and events.

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

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5693/5694/5698
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Synchronization (TClk, Shared LO and Reference Clock)
- RFSA Synchronization (TClk, Shared LO and Reference Clock, and Continuous Acquisition)
- RFSA Synchronization With TClk and RFSG

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=revision-query.html language=enus -->
## TOPIC 00087: Revision Query

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `revision-query.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/revision-query.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision numbers of the NI-RFSA instrument driver. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value:

Revision Query

Returns the revision numbers of the NI-RFSA instrument driver.

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

Instrument driver software revision returned as a numeric string.

The value of the Revision property is returned.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### firmware revision

Instrument firmware revision returned as a numeric string.

The value of the Firmware Revision property is returned.

#### Hardware Support

This node supports the following hardware:

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5644/5645/5646
- PXIe-5663E/5665/5667/5668
- PXIe-5693/5694/5698
- PXIe-5820/5840

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=self-calibrate-range.html language=enus -->
## TOPIC 00088: Self Calibrate Range

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `self-calibrate-range.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/self-calibrate-range.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Self-calibrates all configurations within the specified frequency and reference level limits. If there is an open session for NI-RFSG for your device, it may remain open but cannot be used while this node runs. This node is only valid during the current session and does not update self-calibration d

Self Calibrate Range

Self-calibrates all configurations within the specified frequency and reference level limits.

If there is an open session for NI-RFSG for your device, it may remain open but cannot be used while this node runs.

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

[IMAGE alt='datatype_icon' src='/assets/img/c1di64.png']

##### steps to omit

Calibration steps to skip during the self-calibration process.

| Preselector Alignment | Not used by this node. |
| --- | --- |
| Gain Reference | Not used by this node. |
| IF Flatness | Not used by this node. |
| Digitizer Self Cal | Not used by this node. |
| LO Self Cal | Omits the LO Self Cal step. If you omit this step and Is Self Cal Valid indicates the calibration data for this step is invalid, the LO PLL may fail to lock. |
| Amplitude Accuracy | Omits the Amplitude Accuracy step. If you omit this step, the absolute accuracy of the device is not adjusted. |
| Residual LO Power | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted. |
| Image Suppression | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted. |
| Synthesizer Alignment | Omits the VCO Alignment step. If you omit this step, the LO PLL is not adjusted. |
| DC Offset | Omits the DC Offset step. |

Default value: The default value is an empty array, which indicates that all calibration steps are performed.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### min frequency

Minimum frequency, in hertz (Hz), for the custom self calibration range.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### max frequency

Specifies the maximum frequency, in hertz (Hz), for the custom self calibration range.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### min ref level

Minimum reference level, in dBm, for the custom self calibration range.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### max ref level

Maximum reference level, in dBm, for the custom self calibration range.

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

#### Self-Calibration Best Practices

For best results, NI recommends that you perform a complete self-calibration without omitting any steps. However, if certain aspects of performance are less important for your application, you can omit that step for faster execution.

NI recommends that no external signals are present on the RF In port while the calibration is taking place.

#### Open NI-RFSG Sessions

If there is an existing NI-RFSG session open for the same PXIe-5644/5645/5646, it may remain open but cannot be used while this node runs.

If there is an existing NI-RFSG session open for the same PXIe-5820/5840 while this node runs, it may remain open but cannot be used for operations that access the hardware, for example NI-RFSGCommit or NI-RFSGInitiate.

#### Clearing Data

You can clear the self-calibration range data by calling 
 [Clear Self Calibrate Range](clear-self-calibrate-range.html) or by restarting the system.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=self-calibrate.html language=enus -->
## TOPIC 00089: Self Calibrate

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `self-calibrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/self-calibrate.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs self-calibration on the NI-RFSA device and associated modules that support self-calibration. If the self-calibration is successful, the new calibration constants are stored immediately to the nonvolatile memory of the module. session in Instrument session obtained from Initialize With Optio

Self Calibrate

Performs self-calibration on the NI-RFSA device and associated modules that support self-calibration.

If the self-calibration is successful, the new calibration constants are stored immediately to the nonvolatile memory of the module.

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

[IMAGE alt='datatype_icon' src='/assets/img/c1di64.png']

##### steps to omit

Calibration steps to skip during the self-calibration process.

| Preselector Alignment | Omits the Preselector Alignment step. If you omit this step and Is Self Cal Valid indicates the calibration data for this step is invalid, the preselector alignment specifications are not guaranteed. This step applies only to the PXIe-5605/5606. |
| --- | --- |
| Gain Reference | Omits the Gain Reference step. If you omit this step and Is Self Cal Valid indicates the calibration data for this step is invalid, the absolute accuracy of the device is not guaranteed. |
| IF Flatness | Omits the IF Flatness step. If you omit this step and Is Self Cal Valid indicates the calibration data for this step is invalid, the IF flatness specifications are not guaranteed. |
| Digitizer Self Cal | Omits the Digitizer Self Cal step. If you omit this step and Is Self Cal Valid indicates the calibration data for this step is invalid, the absolute accuracy of the device is not guaranteed. |
| LO Self Cal | Omits the LO Self Cal step. If you omit this step and Is Self Cal Valid indicates the calibration data for this step is invalid, the LO PLL may fail to lock. |
| Amplitude Accuracy | Not used by this node. |
| Residual LO Power | Not used by this node. |
| Image Suppression | Not used by this node. |
| Synthesizer Alignment | Omits the Synthesizer Alignment step. If you omit this step and Is Self Cal Valid indicates the calibration data for this step is invalid, the synthesizer alignment specifications are not guaranteed. |
| DC Offset | Omits the DC Offset Step. If you omit this step and Is Self Cal Valid indicates the calibration data for this step is invalid, the DC offset specifications are not guaranteed. |

Default value: The default value is an empty array, which indicates that all calibration steps are performed.

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

- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

#### Self-Calibration Best Practices

For best results, NI recommends that you perform a complete self-calibration without omitting any steps. However, if 
 [Is Self Calibration Valid?](is-self-calibration-valid.html) indicates that the calibration data for a specific step is still valid, you can omit that step for faster execution.

#### Open NI-RFSG Session for the PXIe-5820/5840

If there is an existing NI-RFSG session open for the same PXIe-5820/5840 while this node runs, it may remain open but cannot be used for operations that access the hardware, for example NI-RFSGCommit or NI-RFSGInitiate.

#### Device-Specific IF Flatness Step Time

- The IF Flatness step can take approximately 15 minutes to complete on the PXIe-5665 ( 3.6 GHz ) and approximately 25 minutes to complete on the PXIe-5665 ( 14 GHz ).
- The IF Flatness step can take approximately 1 minute to complete on the PXIe-5667 ( 3.6 GHz ) and approximately 1.5 minutes to complete on the PXIe-5667 ( 7 GHz ).
- The IF Flatness step can take approximately 15 minutes to complete on the PXIe-5668 .

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=self-test.html language=enus -->
## TOPIC 00090: Self Test

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `self-test.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/self-test.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a self-test on the NI-RFSA device and returns the test result. This node performs a simple series of tests verifying that the NI-RFSA device is powered on and responding. This node calls Reset, which resets the software state. session in Instrument session obtained from Initialize With Opti

Self Test

Performs a self-test on the NI-RFSA device and returns the test result.

This node performs a simple series of tests verifying that the NI-RFSA device is powered on and responding.

Note

Reset

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

Value returned from the device self test.

##### Self Test Result Values

A value of 0 indicates a successful self test.

All other values indicate the device failed the self test.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### self test message

Self test response string from the NI-RFSA device.

#### Hardware Support

This node supports the following hardware:

- PXIe-5601/5603/5605/5606 (external digitizer mode)
- PXIe-5663E/5665/5667/5668
- PXIe-5693/5694/5698
- PXIe-5820/5840

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=send-software-edge-trigger.html language=enus -->
## TOPIC 00091: Send Software Edge Trigger

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `send-software-edge-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/send-software-edge-trigger.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use Configure Trigger to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this node to override a hardware trigger. session in Instrument session obtained from Initialize With Options. error in Error

Send Software Edge Trigger

Sends a trigger to the device when you use [Configure Trigger](configure-trigger.html) to choose a software version of a trigger and the device is waiting for the trigger to be sent.

You can also use this node to override a hardware trigger.

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

##### trigger

Software signal to send.

| Start Trigger | NI-RFSA sends a Start software trigger. |
| --- | --- |
| Ref trigger | NI-RFSA sends a Reference software trigger. |
| Advance Trigger | NI-RFSA sends an Advance software trigger. |
| Arm Ref trigger | NI-RFSA sends an Arm Reference software trigger. |

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
- PXIe-5663E/5665/5667/5668
- PXIe-5820/5840

#### Examples

Search within the programming environment to access the following installed examples:

- RFSA Getting Started Multi Record IQ

#### Error Situations

This node returns an error in the following situations:

- If you configure an invalid trigger.
- If you set acquisition type to Spectrum using 
 Configure Acquisition Type .
- If you have not previously called 
 Initiate .

Parent topic:

Low Level Measurement

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=set-calibration-user-defined-info.html language=enus -->
## TOPIC 00092: Set Calibration User Defined Info

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `set-calibration-user-defined-info.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/set-calibration-user-defined-info.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes user-defined information into the onboard EEPROM. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No er

Set Calibration User Defined Info

Writes user-defined information into the onboard EEPROM.

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

##### user defined info

String that specifies the user information.

This string can be up to 21 characters long.

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

- PXIe-5601/5603/5605/5606
- PXIe-5693/5694/5698

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=spectrum.html language=enus -->
## TOPIC 00093: Spectrum

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `spectrum.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/spectrum.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Spectrum

Configuration

Configure Spectrum Frequency

NI-RFSA

Configure Resolution Bandwidth

Configures the resolution bandwidth of a spectrum acquisition.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=trigger.html language=enus -->
## TOPIC 00094: Trigger

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/trigger.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Trigger

Configuration

Configure Trigger

Configures the Start, Reference, and Advance Triggers.

Get Terminal Name

Returns the fully qualified name of the signal being queried.

Export Signal

Routes signals (triggers, clocks, and events) to the specified output terminal.

Get NI-TClk Session Reference

Extracts a session that can be passed to NI-TClk nodes.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-rfsa-lvnxg-api-ref path=utility.html language=enus -->
## TOPIC 00095: Utility

- bundle_id: `ni-rfsa-lvnxg-api-ref`
- source_path: `utility.html`
- source_url: https://docs-be.ni.com/bundle/ni-rfsa-lvnxg-api-ref/raw/resource/enus/utility.html
- document_id: `ni-rfsa-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`

Utility

NI-RFSA Nodes

Use NI-RFSA nodes to develop applications for your vector signal analyzer.

Reset

Resets all properties to default values and stops export of all external signals and events.

Reset Device

Performs a hard reset on the device.

Self Test

NI-RFSA

Revision Query

NI-RFSA

Get Stream Endpoint Handle

Returns a writer endpoint handle that you can use with NI-P2P to configure a peer-to-peer stream with the digitizer as an endpoint.

Enable Session Access

Enables or disables SFP session access for the specified instrument.

Parent topic:

NI-RFSA Nodes
