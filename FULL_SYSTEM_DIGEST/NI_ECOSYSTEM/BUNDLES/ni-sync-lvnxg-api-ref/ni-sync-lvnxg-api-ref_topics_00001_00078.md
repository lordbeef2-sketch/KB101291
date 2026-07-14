# NI DOCUMENT BUNDLE: ni-sync-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-sync-lvnxg-api-ref start=1 end=78 -->
<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=adjust-clk10-phase-voltage.html language=enus -->
## TOPIC 00001: Adjust Clk10 Phase Voltage

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `adjust-clk10-phase-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/adjust-clk10-phase-voltage.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Clk10 phase voltage value to be written to the specified device's non-volatile onboard memory using an external calibration reference. The value you enter in new voltage is written to the non-volatile onboard memory of the specified device and becomes the new calibration constant if you set

Adjust Clk10 Phase Voltage

Sets the Clk10 phase voltage value to be written to the specified device's non-volatile onboard memory using an external calibration reference.

The value you enter in new voltage is written to the non-volatile onboard memory of the specified device and becomes the new calibration constant if you set action of Close External Calibration to 
 Commit. You must use this function in a session created with Initialize External Calibration.

The Clk10 phase voltage controls the phase between PXI_Clk10 and an external reference clock connected to ClkIn when the specified device is configured to route ClkIn to PXI_Clk10_In. This can be used to minimize the time between the rising edge of the reference clock and PXI_Clk10. You must connect an external calibration reference to the module in order to adjust the default Clk10 phase voltage.

Note

- Use Get Clk10 Phase Voltage to return the Clk10 phase voltage value currently stored in the device's non-volatile onboard memory.
- This function does not immediately change the Clk10 phase voltage. Use the Clk10 Phase Adjust property of niSync Properties to immediately adjust the Clk10 phase voltage.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session handle that you obtain from Initialize External Calibration. The handle identifies the device to calibrate.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### new voltage

The new Clk10 phase voltage value, in volts, to write to the non-volatile onboard memory of the instrument you are calibrating.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle you obtained from Initialize External Calibration. The handle identifies the device you have calibrated.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### old voltage

The Clk10 phase voltage value, in volts, that was last written to the specified device's non-volatile onboard memory.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=adjust-dds-start-voltage.html language=enus -->
## TOPIC 00002: Adjust DDS Start Pulse Phase Voltage

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `adjust-dds-start-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/adjust-dds-start-voltage.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the DDS start pulse phase voltage to be written to the specified device's non-volatile onboard memory using an external calibration reference. The value you enter in new voltage is written to the non-volatile onboard memory of the specified device and becomes the new calibration constant if you

Adjust DDS Start Pulse Phase Voltage

Sets the DDS start pulse phase voltage to be written to the specified device's non-volatile onboard memory using an external calibration reference.

The value you enter in new voltage is written to the non-volatile onboard memory of the specified device and becomes the new calibration constant if you set action of Close External Calibration to 
 Commit. You must use this function in a session created with Initialize External Calibration.

Note

- Use Get DDS Start Pulse Phase Voltage to return the DDS start pulse phase voltage currently stored on the device's onboard memory.
- This function does not immediately change the DDS start pulse phase voltage. Use the DDS Phase Adjust Voltage property of niSync Properties to immediately adjust the DDS start pulse phase voltage.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session handle that you obtain from Initialize External Calibration. The handle identifies the device to calibrate.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### new voltage

The new DDS start pulse phase voltage value, in volts, to write to the non-volatile onboard memory of the instrument you are calibrating.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle you obtained from Initialize External Calibration. The handle identifies the device you have calibrated.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### old voltage

The DDS start pulse phase voltage, in volts, last written to the device's non-volatile onboard memory.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=adjust-oscillator-voltage.html language=enus -->
## TOPIC 00003: Adjust Oscillator Voltage

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `adjust-oscillator-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/adjust-oscillator-voltage.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the oscillator voltage value to be written to the specified device's non-volatile onboard memory using an external calibration reference. The oscillator voltage controls the frequency of the specified device's oscillator. The value you enter in new voltage is written to the non-volatile onboard

Adjust Oscillator Voltage

Sets the oscillator voltage value to be written to the specified device's non-volatile onboard memory using an external calibration reference.

The oscillator voltage controls the frequency of the specified device's oscillator. The value you enter in new voltage is written to the non-volatile onboard memory of the specified device if you set action of Close External Calibration to 
 Commit. You must use this function in a session created with Initialize External Calibration.

Note

- Use Get Oscillator Voltage to return the oscillator voltage value currently stored in the device's non-volatile onboard memory.
- This function does not immediately change the oscillator voltage. Use the Oscillator Voltage property of niSync Properties to immediately adjust the oscillator voltage.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session handle that you obtain from Initialize External Calibration. The handle identifies the device to calibrate.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### new voltage

The new oscillator voltage, in volts, to write to the device's non-volatile onboard memory.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle you obtained from Initialize External Calibration. The handle identifies the device you have calibrated.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### old voltage

The value of the oscillator voltage, in volts, last written to the device's non-volatile onboard memory.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=calibration-palette.html language=enus -->
## TOPIC 00004: Calibration

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `calibration-palette.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/calibration-palette.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calibration functions for NI-Sync.

Calibration

Calibration functions for NI-Sync.

NI-Sync Nodes

Nodes to control NI timing and synchronization modules.

Adjust Clk10 Phase Voltage

Sets the Clk10 phase voltage value to be written to the specified device's non-volatile onboard memory using an external calibration reference.

Adjust DDS Start Pulse Phase Voltage

Sets the DDS start pulse phase voltage to be written to the specified device's non-volatile onboard memory using an external calibration reference.

Adjust Oscillator Voltage

Sets the oscillator voltage value to be written to the specified device's non-volatile onboard memory using an external calibration reference.

Change External Calibration Password

Sets the password required to begin a new external calibration session on the specified device.

Close External Calibration

Ends an external calibration session that you began using Initialize External Calibration.

Get Clk10 Phase Voltage

Reads the Clk10 phase voltage value currently stored on the specified device's non-volatile onboard memory.

Get DDS Start Pulse Phase Voltage

Reads the phase voltage of the DDS start pulse currently stored on the specified device's non-volatile onboard memory.

Get External Calibration Last Date and Time

Reads the date and time, in Greenwich Mean Time (GMT), of the specified device's last external calibration session.

Get External Calibration Last Temperature

Reads the temperature, in degrees Celsius, of the specified module's circuitry during its last external calibration session.

Get External Calibration Recommended Interval

Returns the number of months recommended between external calibration sessions for the device.

Get Oscillator Voltage

Reads the voltage that controls the oscillator frequency currently stored on the specified device's non-volatile onboard memory.

Initialize External Calibration (niSync)

Begins an external calibration session for the specified device.

Parent topic:

NI-Sync Nodes

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=change-external-calibration-password.html language=enus -->
## TOPIC 00005: Change External Calibration Password

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `change-external-calibration-password.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/change-external-calibration-password.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the password required to begin a new external calibration session on the specified device. You must supply the existing calibration password for this operation to succeed. If this is the first time you have set the device's calibration password, refer to the device's calibration procedure manua

Change External Calibration Password

Sets the password required to begin a new external calibration session on the specified device.

Note

- You must supply the existing calibration password for this operation to succeed. If this is the first time you have set the device's calibration password, refer to the device's calibration procedure manual to find the default calibration password.
- You can invoke this node with an instrument handle created with either Initialize (niSync) or Initialize External Calibration.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session handle that you obtain from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### old password

The old external calibration password for the device.

Old password must exactly match the value, including case, in the device's non-volatile onboard memory for this operation to succeed.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### new password

The new external calibration password for the module.

The new password is case-sensitive and must be entered exactly to begin a new external calibration session.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtained from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=clear-clock.html language=enus -->
## TOPIC 00006: Clear Clock

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `clear-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/clear-clock.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Frees a resource that contains a generated clock. Once you clear the clock, you can use the associated terminal for other operations. session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The node responds to this input according to stand

Clear Clock

Frees a resource that contains a generated clock.
 
 Once you clear the clock, you can use the associated terminal for other operations.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The line that contains the generated clock to clear.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=clear-future-time-events.html language=enus -->
## TOPIC 00007: Clear Future Time Events

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `clear-future-time-events.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/clear-future-time-events.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Frees the terminal of any future time events previously created. Once you invoke this function, you can use the associated terminal for other operations. The specified line is tri-stated and the resource is freed. session in The session that you obtain from Initialize. error in Error conditions that

Clear Future Time Events

Frees the terminal of any future time events previously created.

Once you invoke this function, you can use the associated terminal for other operations. The specified line is tri-stated and the resource is freed.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The terminal that will no longer generate future time events.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=close-external-calibration.html language=enus -->
## TOPIC 00008: Close External Calibration

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `close-external-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/close-external-calibration.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Ends an external calibration session that you began using Initialize External Calibration. You can choose whether or not to write the new calibration constants set by an external calibration function to the device's non-volatile onboard memory using action. After invoking Close External Calibration,

Close External Calibration

Ends an external calibration session that you began using Initialize External Calibration.
 
 You can choose whether or not to write the new calibration constants set by an external calibration function to the device's non-volatile onboard memory using action.

Note

- After invoking Close External Calibration, you cannot use the NI-Sync session handle again until you invoke Initialize (niSync) or Initialize External Calibration.
- If you invoke this function with action set to Commit, the function updates the external calibration date stored in the device's non-volatile onboard memory, even if no calibration constants were changed.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### action

A 32-bit integer that specifies whether or not to write the external calibration constants set using an external calibration function to the device's non-volatile onboard memory.

Valid values:

| Abort | Discards any changes made with an external calibration function and maintains calibration constants at their original value. |
| --- | --- |
| Commit | Writes any changes made with an external calibration function to the device's non-volatile onboard memory. These are the new default calibration constants for the device. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=close.html language=enus -->
## TOPIC 00009: Close

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `close.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/close.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Ends an NI-Sync instrument driver session and frees the device for other operations. You must use this function any time you begin a session using Initialize. This function clears or disables any generated clocks, future time events, and timestamp triggers on the associated device. Calling this func

Close

Ends an NI-Sync instrument driver session and frees the device for other operations.

You must use this function any time you begin a session using Initialize. This function clears or disables any generated clocks, future time events, and timestamp triggers on the associated device.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

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

NI-Sync Nodes

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=connect-clock-terminals.html language=enus -->
## TOPIC 00010: Connect Clock Terminals

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `connect-clock-terminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/connect-clock-terminals.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects a source clock terminal to a destination clock terminal. A clock terminal connection is characterized by its source terminal and destination terminal. For help choosing compatible clock source and destination terminals, refer to Clock Terminal Connections. session in The session that you ob

Connect Clock Terminals

Connects a source clock terminal to a destination clock terminal.

A clock terminal connection is characterized by its source terminal and destination terminal.

Note

Clock Terminal Connections

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source terminal

The source clock terminal of the clock you would like to connect.

| PXI_Clk10 | The 10 MHz backplane clock of the PXI or PXIe chassis. |
| --- | --- |
| ClkIn | The ClkIn input connector on the front panel of your device. |
| Oscillator | The oscillator of the device specified in the instrument handle terminal. |
| DDS Clock | The DDS signal generated by the device specified in the instrument handle terminal. |
| PFI_LVDS<n> | The PFI low voltage differential signaling (LVDS) input/output connectors on the front panel of the module. |
| PXIe_DStarC<n> | The differential star trigger line of the PXIe chassis. Use DStarC lines to route clock and/or trigger signals from a peripheral slot to a system timing slot. Note Each PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor-specific. Refer to the chassis' documentation for more information on the mapping of differential star trigger lines. |
| PXIe_DStarA | The differential star trigger line of the PXIe chassis. Use DStarA lines to route clock signals from a system timing slot to a peripheral slot. Note Each PXIe_DStarA trigger is mapped to a single slot. This mapping is vendor specific. Refer to the chassis' documentation for more information on the mapping of differential star trigger lines. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### destination terminal

The destination clock terminal to which the source terminal connects.

| PXI_Clk10_In | The connector pin used to provide the backplane with a reference 10 MHz signal from the system timing slot. When you connect a signal to this pin, PXI_Clk10 and PXIe_Clk100 are phase-aligned to this reference. |
| --- | --- |
| ClkOut | The ClkOut connector on the front panel of the module. |
| BoardClk | The timekeeper used to schedule future time events and timestamping on certain modules. BoardClk accepts a 10 MHz reference clock and multiples it by 10 to create a 100 MHz clock for use as a timekeeper. Note BoardClk is a valid terminal only on PXI-668x devices. |
| PFI_LVDS<n> | The PFI_LVDS output connector on the front panel of your device. |
| PXIe_DStarA<n> | The differential star trigger line of the PXIe chassis. Use DStarA lines to route clock signals from a system timing slot to a peripheral slot. Note Each PXIe_DStarA trigger is mapped to a single slot. This mapping is vendor specific. Refer to the chassis' documentation for more information on the mapping of differential star trigger lines. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle for the NI-Sync device. Pass this handle to other NI-Sync nodes to
 program the behavior of the device.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Routing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=connect-software-trigger.html language=enus -->
## TOPIC 00011: Connect Software Trigger

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `connect-software-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/connect-software-trigger.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects the global software trigger terminal to a destination trigger terminal. Once you connect the global software trigger, you can fire the trigger using Send Software Trigger. The destination terminal you specify in this function determines the full-speed synchronization clock used by the globa

Connect Software Trigger

Connects the global software trigger terminal to a destination trigger terminal.

Once you connect the global software trigger, you can fire the trigger using Send Software Trigger.

Note

destination terminal

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### update edge

The synchronization clock update edge on which the connected signal is propagated.

The source and destination terminals must be connected synchronously for this parameter to apply.

| Rising Edge | 0 | Propagates the trigger when the digital signal of the synchronization clock transitions from low to high, i.e. the rising edge. |
| --- | --- | --- |
| Falling Edge | 1 | Propagates the trigger when the digital signal of the synchronization clock transitions from high to low, i.e. the falling edge. |

Default value: Rising Edge

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### synchronization clock

The clock to use to synchronize a trigger signal.

Note

| Full Speed Clock | Uses the full speed frequency of the synchronization clock to synchronize the trigger. |
| --- | --- |
| Divided Clock 1 | Divides the synchronization clock by the value specified in the Clock Divisor 1 property of the niSync Property Node and uses the frequency of the divided clock to synchronize the trigger. |
| Divided Clock 2 | Divides the synchronization clock by the value specified in the Clock Divisor 2 property of the niSync Property Node and uses the frequency of the divided clock to synchronize the trigger. |

Default value: Full Speed Clock

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source terminal

The source software trigger terminal to connect to the destination terminal.

The only acceptable value is Global Software Trigger.

Default value: Global Software Trigger

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### destination terminal

The destination trigger terminal that the global software trigger terminal will connect to.

| PXI_Trig<n> | The basic trigger lines of a PXI or PXIe chassis. |
| --- | --- |
| PXI_Star<n> | The star trigger lines of a PXI or PXIe chassis. Each star trigger line is a dedicated connection between the system timing slot and one other slot. Note Each PXI_Star trigger is mapped to a single slot. This mapping is vendor specific. Refer to the hardware documentation to determine the orientation of PXI_Star lines in the chassis. |
| PFI<n> | The PFI connectors on the front panel of the module. |
| PFI_LVDS<n> | The PFI low voltage differential signaling (LVDS) input/output connectors on the front panel of the device. |
| PXIe_DStarB<n> | The differential star trigger lines of the PXIe chassis. Use PXIe_DStarB lines to send trigger signals from the system timing slot to a peripheral slot of the chassis. |
| PXIe_DStarC | The differential star trigger lines of the PXIe chassis. Use PXIe_DStarC lines to send trigger and clock signals from a peripheral slot to the system timing slot of the chassis. |

Default value: PXI_Trig0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### invert

A ring value that specifies whether or not to invert the source terminal signal at the destination terminal.

Note

| Don't Invert Signal | 0 | Keeps the digital signal of the source trigger terminal in its original format. |
| --- | --- | --- |
| Invert Signal | 1 | Inverts the digital signal of the source trigger terminal so that its rising edges are now its falling edges, and vice versa. |

Default value: Don't Invert Signal

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### delay

The number of seconds to delay the global software trigger pulse.

The delay must be a multiple of the synchronization clock period. The global software trigger can be delayed up to 15 clock cycles for each route.

Note

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Routing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=connect-trigger-terminals.html language=enus -->
## TOPIC 00012: Connect Trigger Terminals

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `connect-trigger-terminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/connect-trigger-terminals.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes triggers through the PXI backplane, between devices, or between multiple chassis. Once a terminal route is connected, you can invert the trigger signal at the destination terminal, synchronize the trigger to the rising or falling edge of a synchronization clock, fire the trigger asynchronousl

Connect Trigger Terminals

Routes triggers through the PXI backplane, between devices, or between multiple chassis.

Once a terminal route is connected, you can invert the trigger signal at the destination terminal, synchronize the trigger to the rising or falling edge of a synchronization clock, fire the trigger asynchronously, or route the trigger to other trigger terminals.

Note

destination terminal

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### update edge

The synchronization clock update edge on which the connected signal is propagated.

The source and destination terminals must be connected synchronously for this parameter to apply.

| Rising Edge | 0 | Propagates the trigger when the digital signal of the synchronization clock transitions from low to high, i.e. the rising edge. |
| --- | --- | --- |
| Falling Edge | 1 | Propagates the trigger when the digital signal of the synchronization clock transitions from high to low, i.e. the falling edge. |

Default value: Rising Edge

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### synchronization clock

A string value that specifies whether to use the full-speed or a divided synchronization clock to control trigger firing.

The trigger is synchronized with the rising or falling edge of the clock you select in this parameter.

| Asynchronous | SyncClkAsync | The trigger is not synchronized to any clock. |
| --- | --- | --- |
| Full Speed Clock | SyncClkFullSpeed | Uses the full speed frequency of the synchronization clock to synchronize the trigger. |
| Divided Clock 1 | SyncClkDivided1 | Divides the synchronization clock by the value specified in the Clock Divisor 1 property of niSync Properties and uses the frequency of the divided clock to synchronize the trigger. |
| Clock Divisor 2 | SyncClkDivided2 | Divides the synchronization clock by the value specified in the Clock Divisor 2 property of niSync Properties and uses the frequency of the divided clock to synchronize the trigger. |

Default value: Asynchronous

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source terminal

The source trigger terminal to connect to the destination terminal.

| PXI_Trig<n> | The basic trigger lines of a PXI or PXIe chassis. |
| --- | --- |
| PXI_Star<n> | The star trigger lines of a PXI or PXIe chassis. Note Each PXI_Star trigger is mapped to a single slot. This mapping is vendor specific. Refer to the hardware documentation to determine the orientation of PXI_Star lines in the chassis. |
| PFI<n> | The PFI connectors on the front panel of the module. You can use PFI connectors to route triggers between multiple chassis or devices. |
| PFI_LVDS<n> | The PFI low voltage differential signaling (LVDS) input/output connectors on the front panel of your device. Signals on PFI LVDS lines use the standard PFI synchronization clock. |
| Ground | The Ground connector continuously outputs a logic low signal, unless it is inverted. |
| Full Speed Clock | The full speed synchronization clock signal of the destination terminal zone. Use this source to send a full-speed clock signal along a trigger line (for example, to route a PXI_Clk10 clock signal to a PFI line). Caution Routing a clock signal through a PXI_Trig line is not recommended, due to poor clock signal integrity caused by the topology of the PXI_Trig lines. Use PXI_Star, PXIe_DStar, or PFI lines instead. |
| Divided Clock 1 | The first divided clock signal of the destination terminal zone. This source divides the synchronization clock of the destination terminal by the value you specify in the Clock Divisor 1 parameter of niSync Properties and uses the result as the trigger source. |
| Divided Clock 2 | The second divided clock signal of the destination terminal zone. This source divides the synchronization clock of the destination terminal by the value you specify in the Clock Divisor 2 property of niSync Properties and uses the result as the trigger source. |
| ClkIn | The ClkIn connector on the front panel of the device. Use this terminal to route triggers from an external device. |
| PXIe_DStarC<n> | The differential star trigger lines of the PXIe chassis. Use PXIe_DStarC lines to send trigger and clock signals from a peripheral slot to the system timing slot of the chassis. Note Each PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor specific. Refer to your chassis documentation to determine the orientation of differential star trigger lines. |
| PXIe_DStarB | The differential star trigger lines of the PXIe chassis. Use PXIe_DStarB lines to send trigger signals from the system timing slot to a peripheral slot of the chassis. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### destination terminal

The destination trigger terminal to which the source terminal connects.

| PXI_Trig<n> | The basic trigger lines of the PXI or PXIe chassis. |
| --- | --- |
| PXI_Star<n> | The star trigger lines of the PXI or PXIe chassis. Each star trigger line is a dedicated connection between the system timing slot and one other slot.Note Each PXI_Star trigger is mapped to a single slot. This mapping is vendor specific. Refer to the hardware documentation to determine the orientation of PXI_Star lines in the chassis. |
| PFI<n> | The PFI connectors on the front panel of the module. |
| PFI_LVDS<n> | The PFI low voltage differential signaling (LVDS) input/output connectors on the front panel of the module. |
| PXIe_DStarB<n> | The differential star trigger lines of the PXIe chassis. Use PXIe_DStarB lines to send trigger signals from the system timing slot to a peripheral slot of the chassis.Note Each PXIe_DStarB trigger is mapped to a single slot. This mapping is vendor specific. Refer to the chassis documentation to determine the orientation of differential star trigger lines. |
| PXIe_DStarC | The differential star trigger lines of the PXIe chassis. Use PXIe_DStarC lines to send trigger and clock signals from a peripheral slot to the system timing slot of the chassis. |

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### invert

A ring value that specifies whether or not to invert the source terminal signal at the destination terminal.

Note

| Don't Invert Signal | 0 | Keeps the digital signal of the source trigger terminal in its original format. |
| --- | --- | --- |
| Invert Signal | 1 | Inverts the digital signal of the source trigger terminal so that its rising edges are now its falling edges, and vice versa. |

Default value: Don't Invert Signal

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle for the NI-Sync device. Pass this handle to other NI-Sync nodes to
 program the behavior of the device.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Routing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=create-clock-frequency.html language=enus -->
## TOPIC 00013: Frequency

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `create-clock-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/create-clock-frequency.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a clock that runs at a custom frequency and duty cycle. Once you generate a clock in a terminal, you cannot use that terminal for other operations until you clear the clock with Clear Clock or close the session with Close. When you invoke this function, the digital signal on the specified

Frequency

Generates a clock that runs at a custom frequency and duty cycle.

Once you generate a clock in a terminal, you cannot use that terminal for other operations until you clear the clock with Clear Clock or close the session with Close. When you invoke this function, the digital signal on the specified terminal is driven low until the clock starts.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### duty cycle

The desired duty cycle of the clock generated on the specified terminal.

Note

coerced duty cycle

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency

The desired frequency of the clock generated on the specified terminal.

Note

coerced frequency

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The line you would like to generate the clock on.

You cannot use this line for other operations until you clear the generated clock using Clear Clock or close the session.

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### start time

The time to start the generated clock.

This time is synchronized with the board time of the module you use to create the clock.

Default value: immediate

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### stop time

The board time when to stop the generated clock.

This time is synchronized with the board time of the module you use to create the clock.

Default value: never

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in (no error)

error in (no error) accepts error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced frequency

The actual frequency at which the clock is generated.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced duty cycle

The actual duty cycle at which the clock is generated.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

error out passes error or warning information out of a VI to be used by other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

Parent topic:

Create Clock Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=create-clock-ticks.html language=enus -->
## TOPIC 00014: Ticks

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `create-clock-ticks.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/create-clock-ticks.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a clock synchronized to the board time associated with the specified instrument handle. This clock runs for a specified number of high and low ticks every cycle. The terminal associated with this clock cannot be used for other operations until the clock is cleared with Clear Clock or the s

Ticks

Generates a clock synchronized to the board time associated with the specified instrument handle. This clock runs for a specified number of high and low ticks every cycle.

The terminal associated with this clock cannot be used for other operations until the clock is cleared with Clear Clock or the session is closed with Close. When this function is invoked, the digital signal on the specified terminal is driven low until the clock starts.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### low ticks

The number of ticks the generated clock should spend in the low logic state.

You can view the length of a tick using the Clock Resolution property of niSync Properties.

Default value: 100

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### high ticks

The number of ticks the generated clock should spend in the high logic state.

You can view the length of a tick using the Clock Resolution property of niSync Properties.

Default value: 100

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The line you would like to generate the clock on.

You cannot use this line for other operations until you clear the generated clock using Clear Clock or close the session.

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### start time

The time to start the generated clock.

This time is synchronized with the board time of the module you use to create the clock.

Default value: immediate

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### stop time

The board time when to stop the generated clock.

This time is synchronized with the board time of the module you use to create the clock.

Default value: never

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Create Clock Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=create-clock-time.html language=enus -->
## TOPIC 00015: Time

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `create-clock-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/create-clock-time.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a clock that is time-based. With this mode, you can specify how long the clock runs at a high logic level and how long it runs at a low logic level. The terminal associated with this clock cannot be used for other operations until the clock is cleared with Clear Clock or the session is clo

Time

Generates a clock that is time-based. With this mode, you can specify how long the clock runs at a high logic level and how long it runs at a low logic level.

The terminal associated with this clock cannot be used for other operations until the clock is cleared with Clear Clock or the session is closed with Close . When this function is invoked, the digital signal on the specified terminal is driven low until the clock starts.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### low time

The desired duration of the logic low state of the clock.

Note

coerced low time

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### high time

The desired duration of the logic high state of the clock.

Note

coerced high time

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The line you would like to generate the clock on.

You cannot use this line for other operations until you clear the generated clock using Clear Clock or close the session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in (no error)

error in (no error) accepts error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### start time

The time to start the generated clock.

This time is synchronized with the board time of the module you use to create the clock.

Default value: immediate

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### stop time

The board time when to stop the generated clock.

This time is synchronized with the board time of the module you use to create the clock.

Default value: never

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced low time

The actual duration, in seconds, of the logic low state at which the clock is generated.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced high time

The actual duration, in seconds, of the logic high state at which the clock is generated.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

error out passes error or warning information out of a VI to be used by other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

Parent topic:

Create Clock Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=create-clock.html language=enus -->
## TOPIC 00016: Create Clock Multimode Function

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `create-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/create-clock.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a clock synchronized to the board time of the module.

Create Clock Multimode Function

Generates a clock synchronized to the board time of the module.

Timing

Timing nodes for NI-Sync devices.

Frequency

Generates a clock that runs at a custom frequency and duty cycle.

Ticks

Generates a clock synchronized to the board time associated with the specified instrument handle. This clock runs for a specified number of high and low ticks every cycle.

Time

Generates a clock that is time-based. With this mode, you can specify how long the clock runs at a high logic level and how long it runs at a low logic level.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=create-future-time-event.html language=enus -->
## TOPIC 00017: Create Future Time Event

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `create-future-time-event.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/create-future-time-event.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Schedules a future time event. A future time event changes the digital signal at the terminal you specify—either from low to high or high to low—when the board time of the specified module reaches the specified time. The future time event you create with this function is synchronized with the board

Create Future Time Event

Schedules a future time event.

A future time event changes the digital signal at the terminal you specify—either from low to high or high to low—when the board time of the specified module reaches the specified time. The future time event you create with this function is synchronized with the board time of the module.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The terminal whose digital signal will be changed by the future time event.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### output level

The level to set the digital signal to at the specified time.

| high | Sets the digital signal to a logic high state. |
| --- | --- |
| low | Sets the digital signal to a logic low state. |

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### time

The board time when the future time event should occur.

When the board time of the module reaches this time, the digital signal changes. The default value of this parameter is immediate, which triggers the future time event as soon as the function is invoked.

Default value: Immediate

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Creating Multiple Future Time Events

To create multiple future time events, invoke this function multiple times.

#### Future Time Event Terminals

Once you generate a future time event on a terminal, you cannot use that terminal for operations other than generating future time events until you clear all future time events with Clear Future Time Events or you close the session with Close. When you invoke this function, the digital signal on the specified terminal is driven low until the first future time event occurs.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=default.html language=enus -->
## TOPIC 00018: NI-Sync Nodes

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `default.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/default.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Nodes to control NI timing and synchronization modules.

NI-Sync Nodes

Nodes to control NI timing and synchronization modules.

Close

Ends an NI-Sync instrument driver session and frees the device for other operations.

Initialize (niSync)

Creates a new NI-Sync instrument driver session.

niSync Properties

Sets and displays parameters of NI-Sync devices.

NI-Sync Resource Name

Specifies the instrument handle to use for NI-Sync operations.

Routing

Routing functions for NI-Sync devices.

Timing

Timing nodes for NI-Sync devices.

Utility

Utility functions for NI-Sync.

Calibration

Calibration functions for NI-Sync.

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=disable-gps-irig-timestamping-gps.html language=enus -->
## TOPIC 00019: GPS

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `disable-gps-irig-timestamping-gps.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/disable-gps-irig-timestamping-gps.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables timestamping of the GPS pulse per second. session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session out The

GPS

Disables timestamping of the GPS pulse per second.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Disable GPS or IRIG Timestamping Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=disable-gps-or-irig-timestamping-irig.html language=enus -->
## TOPIC 00020: IRIG

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `disable-gps-or-irig-timestamping-irig.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/disable-gps-or-irig-timestamping-irig.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables timestamping of IRIG-B AM or IRIG-B DC decodes. session in The session that you obtain from Initialize. terminal The terminal on which to disable IRIG decoding. You can then use this terminal for other operations. error in Error conditions that occur before this node runs. The node responds

IRIG

Disables timestamping of IRIG-B AM or IRIG-B DC decodes.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The terminal on which to disable IRIG decoding. You can then use this terminal for other operations.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Disable GPS or IRIG Timestamping Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=disable-gps-or-irig-timestamping.html language=enus -->
## TOPIC 00021: Disable GPS or IRIG Timestamping Multimode Function

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `disable-gps-or-irig-timestamping.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/disable-gps-or-irig-timestamping.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Ends GPS or IRIG timestamping on the specified device. You must use this function every time you invoke Enable GPS or IRIG Timestamping.

Disable GPS or IRIG Timestamping Multimode Function

Ends GPS or IRIG timestamping on the specified device. You must use this function every time you invoke Enable GPS or IRIG Timestamping.

GPS/IRIG

GPS and IRIG functions for NI-Sync.

GPS

Disables timestamping of the GPS pulse per second.

IRIG

Disables timestamping of IRIG-B AM or IRIG-B DC decodes.

Parent topic:

GPS/IRIG

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=disable-time-stamp-trigger.html language=enus -->
## TOPIC 00022: Disable Time Stamp Trigger

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `disable-time-stamp-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/disable-time-stamp-trigger.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Ends timestamping enabled by Enable Time Stamp Trigger. Once you disable the timestamp trigger, you can use the associated terminal for other operations. session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The node responds to this inpu

Disable Time Stamp Trigger

Ends timestamping enabled by Enable Time Stamp Trigger.

Once you disable the timestamp trigger, you can use the associated terminal for other operations.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The terminal that contains the digital signal that is the trigger to stop timestamping.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=disconnect-clock-terminals.html language=enus -->
## TOPIC 00023: Disconnect Clock Terminals

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `disconnect-clock-terminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/disconnect-clock-terminals.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a route between a source clock terminal and a destination clock terminal. session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default v

Disconnect Clock Terminals

Closes a route between a source clock terminal and a destination clock terminal.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source terminal

The source clock terminal of the clock you would like to connect.

| PXI_Clk10 | The 10 MHz backplane clock of the PXI or PXIe chassis. |
| --- | --- |
| ClkIn | The ClkIn input connector on the front panel of your device. |
| Oscillator | The oscillator of the device specified in the instrument handle terminal. |
| DDS Clock | The DDS signal generated by the device specified in the instrument handle terminal. |
| PFI_LVDS<n> | The PFI low voltage differential signaling (LVDS) input/output connectors on the front panel of the module. |
| PXIe_DStarC<n> | The differential star trigger line of the PXIe chassis. Use DStarC lines to route clock and/or trigger signals from a peripheral slot to a system timing slot. Note Each PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor-specific. Refer to the chassis' documentation for more information on the mapping of differential star trigger lines. |
| PXIe_DStarA | The differential star trigger line of the PXIe chassis. Use DStarA lines to route clock signals from a system timing slot to a peripheral slot. Note Each PXIe_DStarA trigger is mapped to a single slot. This mapping is vendor specific. Refer to the chassis' documentation for more information on the mapping of differential star trigger lines. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### destination terminal

The destination clock terminal to which the source terminal connects.

| PXI_Clk10_In | The connector pin used to provide the backplane with a reference 10 MHz signal from the system timing slot. When you connect a signal to this pin, PXI_Clk10 and PXIe_Clk100 are phase-aligned to this reference. |
| --- | --- |
| ClkOut | The ClkOut connector on the front panel of the module. |
| BoardClk | The timekeeper used to schedule future time events and timestamping on certain modules. BoardClk accepts a 10 MHz reference clock and multiples it by 10 to create a 100 MHz clock for use as a timekeeper. Note BoardClk is a valid terminal only on PXI-668x devices. |
| PFI_LVDS<n> | The PFI_LVDS output connector on the front panel of your device. |
| PXIe_DStarA<n> | The differential star trigger line of the PXIe chassis. Use DStarA lines to route clock signals from a system timing slot to a peripheral slot. Note Each PXIe_DStarA trigger is mapped to a single slot. This mapping is vendor specific. Refer to the chassis' documentation for more information on the mapping of differential star trigger lines. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle for the NI-Sync device. Pass this handle to other NI-Sync nodes to
 program the behavior of the device.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Routing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=disconnect-software-trigger.html language=enus -->
## TOPIC 00024: Disconnect Software Trigger

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `disconnect-software-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/disconnect-software-trigger.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a route between the global software trigger and a destination trigger terminal. You must use this function every time you connect a software trigger using Connect Software Trigger. Once you invoke this function, you can use the associated terminal for other operations. session in The session

Disconnect Software Trigger

Closes a route between the global software trigger and a destination trigger terminal.

You must use this function every time you connect a software trigger using Connect Software Trigger. Once you invoke this function, you can use the associated terminal for other operations.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source terminal

The source software trigger terminal to connect to the destination terminal.

The only acceptable value is Global Software Trigger.

Default value: Global Software Trigger

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### destination terminal

The destination trigger terminal that the global software trigger terminal will connect to.

| PXI_Trig<n> | The basic trigger lines of a PXI or PXIe chassis. |
| --- | --- |
| PXI_Star<n> | The star trigger lines of a PXI or PXIe chassis. Each star trigger line is a dedicated connection between the system timing slot and one other slot. Note Each PXI_Star trigger is mapped to a single slot. This mapping is vendor specific. Refer to the hardware documentation to determine the orientation of PXI_Star lines in the chassis. |
| PFI<n> | The PFI connectors on the front panel of the module. |
| PFI_LVDS<n> | The PFI low voltage differential signaling (LVDS) input/output connectors on the front panel of the device. |
| PXIe_DStarB<n> | The differential star trigger lines of the PXIe chassis. Use PXIe_DStarB lines to send trigger signals from the system timing slot to a peripheral slot of the chassis. |
| PXIe_DStarC | The differential star trigger lines of the PXIe chassis. Use PXIe_DStarC lines to send trigger and clock signals from a peripheral slot to the system timing slot of the chassis. |

Default value: PXI_Trig0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Routing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=disconnect-trigger-terminals.html language=enus -->
## TOPIC 00025: Disconnect Trigger Terminals

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `disconnect-trigger-terminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/disconnect-trigger-terminals.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a route between a source trigger terminal and a destination trigger terminal. After you invoke this function, you can use the associated terminal for other operations. You must use this node any time you connect trigger terminals using Connect Trigger Terminals. session in The session that yo

Disconnect Trigger Terminals

Closes a route between a source trigger terminal and a destination trigger terminal.

After you invoke this function, you can use the associated terminal for other operations. You must use this node any time you connect trigger terminals using Connect Trigger Terminals.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source terminal

The source trigger terminal to connect to the destination terminal.

| PXI_Trig<n> | The basic trigger lines of a PXI or PXIe chassis. |
| --- | --- |
| PXI_Star<n> | The star trigger lines of a PXI or PXIe chassis. Note Each PXI_Star trigger is mapped to a single slot. This mapping is vendor specific. Refer to the hardware documentation to determine the orientation of PXI_Star lines in the chassis. |
| PFI<n> | The PFI connectors on the front panel of the module. You can use PFI connectors to route triggers between multiple chassis or devices. |
| PFI_LVDS<n> | The PFI low voltage differential signaling (LVDS) input/output connectors on the front panel of your device. Signals on PFI LVDS lines use the standard PFI synchronization clock. |
| Ground | The Ground connector continuously outputs a logic low signal, unless it is inverted. |
| Full Speed Clock | The full speed synchronization clock signal of the destination terminal zone. Use this source to send a full-speed clock signal along a trigger line (for example, to route a PXI_Clk10 clock signal to a PFI line). Caution Routing a clock signal through a PXI_Trig line is not recommended, due to poor clock signal integrity caused by the topology of the PXI_Trig lines. Use PXI_Star, PXIe_DStar, or PFI lines instead. |
| Divided Clock 1 | The first divided clock signal of the destination terminal zone. This source divides the synchronization clock of the destination terminal by the value you specify in the Clock Divisor 1 parameter of niSync Properties and uses the result as the trigger source. |
| Divided Clock 2 | The second divided clock signal of the destination terminal zone. This source divides the synchronization clock of the destination terminal by the value you specify in the Clock Divisor 2 property of niSync Properties and uses the result as the trigger source. |
| ClkIn | The ClkIn connector on the front panel of the device. Use this terminal to route triggers from an external device. |
| PXIe_DStarC<n> | The differential star trigger lines of the PXIe chassis. Use PXIe_DStarC lines to send trigger and clock signals from a peripheral slot to the system timing slot of the chassis. Note Each PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor specific. Refer to your chassis documentation to determine the orientation of differential star trigger lines. |
| PXIe_DStarB | The differential star trigger lines of the PXIe chassis. Use PXIe_DStarB lines to send trigger signals from the system timing slot to a peripheral slot of the chassis. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### destination terminal

The destination trigger terminal to which the source terminal connects.

| PXI_Trig<n> | The basic trigger lines of the PXI or PXIe chassis. |
| --- | --- |
| PXI_Star<n> | The star trigger lines of the PXI or PXIe chassis. Each star trigger line is a dedicated connection between the system timing slot and one other slot.Note Each PXI_Star trigger is mapped to a single slot. This mapping is vendor specific. Refer to the hardware documentation to determine the orientation of PXI_Star lines in the chassis. |
| PFI<n> | The PFI connectors on the front panel of the module. |
| PFI_LVDS<n> | The PFI low voltage differential signaling (LVDS) input/output connectors on the front panel of the module. |
| PXIe_DStarB<n> | The differential star trigger lines of the PXIe chassis. Use PXIe_DStarB lines to send trigger signals from the system timing slot to a peripheral slot of the chassis.Note Each PXIe_DStarB trigger is mapped to a single slot. This mapping is vendor specific. Refer to the chassis documentation to determine the orientation of differential star trigger lines. |
| PXIe_DStarC | The differential star trigger lines of the PXIe chassis. Use PXIe_DStarC lines to send trigger and clock signals from a peripheral slot to the system timing slot of the chassis. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle for the NI-Sync device. Pass this handle to other NI-Sync nodes to
 program the behavior of the device.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Routing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=enable-gps-irig-timestamping-gps.html language=enus -->
## TOPIC 00026: GPS

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `enable-gps-irig-timestamping-gps.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/enable-gps-irig-timestamping-gps.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables timestamping of the GPS pulse per second signal. You must set the time reference for the module specified in instrument handle to GPS for this node to function. session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The node respon

GPS

Enables timestamping of the GPS pulse per second signal.

You must set the time reference for the module specified in instrument handle to GPS for this node to function.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Enable GPS or IRIG Timestamping Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=enable-gps-or-irig-timestamping-irig.html language=enus -->
## TOPIC 00027: IRIG

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `enable-gps-or-irig-timestamping-irig.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/enable-gps-or-irig-timestamping-irig.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Timestamps an incoming IRIG signal with the current board time of the specified module. Use this function to test the stability of an external IRIG source relative to another external time reference. session in The session that you obtain from Initialize. IRIG type The type of IRIG output generated

IRIG

Timestamps an incoming IRIG signal with the current board time of the specified module.

Use this function to test the stability of an external IRIG source relative to another external time reference.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### IRIG type

The type of IRIG output generated by the external IRIG source.

| IRIGB DC | The IRIG-B DC output. |
| --- | --- |
| IRIGB AM | The IRIG-B AM output. |

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The terminal that contains the external IRIG source you would like to timestamp.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in (no error)

error in (no error) accepts error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

error out passes error or warning information out of a VI to be used by other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

Parent topic:

Enable GPS or IRIG Timestamping Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=enable-gps-or-irig-timestamping.html language=enus -->
## TOPIC 00028: Enable GPS or IRIG Timestamping Multimode Function

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `enable-gps-or-irig-timestamping.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/enable-gps-or-irig-timestamping.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Timestamps an incoming GPS or IRIG signal with the current board time of the specified module.

Enable GPS or IRIG Timestamping Multimode Function

Timestamps an incoming GPS or IRIG signal with the current board time of the specified module.

GPS/IRIG

GPS and IRIG functions for NI-Sync.

GPS

Enables timestamping of the GPS pulse per second signal.

IRIG

Timestamps an incoming IRIG signal with the current board time of the specified module.

Parent topic:

GPS/IRIG

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=enable-time-stamp-trigger.html language=enus -->
## TOPIC 00029: Enable Time Stamp Trigger

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `enable-time-stamp-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/enable-time-stamp-trigger.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a timestamp every time the signal of a specified trigger or clock changes. You can then read a single timestamp or multiple timestamps at a later point in the data flow. You cannot use the input terminal specified in this function for other operations until you disable the timestamp trigger

Enable Time Stamp Trigger

Creates a timestamp every time the signal of a specified trigger or clock changes. You can then read a single timestamp or multiple timestamps at a later point in the data flow.

You cannot use the input terminal specified in this function for other operations until you disable the timestamp trigger using Disable Time Stamp Trigger or close the session with Close. You can create timestamps for triggers, future time events, clocks created using Create Clock, and external devices.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The terminal that contains the trigger signal you would like to timestamp.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### active edge

The point in the trigger signal to record a timestamp in the software buffer.

| rising | Records a timestamp on the rising edge of the trigger, i.e. when the trigger signal transitions from low to high. |
| --- | --- |
| falling | Records a timestamp on the falling edge of the trigger, i.e. when the trigger signal transitions from high to low. |
| any | Records a timestamp on either a rising or falling edge of the trigger. |

Default value: rising

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### decimation count

A number that specifies by how much to decimate incoming trigger events.

Use this value to adjust the number of timestamps that should elapse before the next timestamp is recorded. For example, if you set decimation count to 10, the function will record every tenth timestamp. Decimation count must be greater than or equal to one.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Troubleshooting Overflow Errors

If you are recording multiple timestamps, you may encounter a software buffer overflow error. This means that LabVIEW does not have enough memory to store the timestamps you are trying to record. You can take one or more of the following actions to resolve a software buffer overflow error:

- Set a higher value in the decimation count parameter.
- Set the Time Stamp Buffer Size property in niSync Properties by selecting 
 Timing»Time Stamps»Time Stamp Buffer Size . Use this value to manually adjust the size, in number of timestamps, of the software buffer where timestamps are stored.
- Set the number of timestamps terminal in Read Trigger Time Stamp to a lower value.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=error-message.html language=enus -->
## TOPIC 00030: Error Message

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `error-message.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/error-message.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an error or warning code returned by an NI-Sync function into a readable string. You can display the error string in a dialog box or an indicator on the front panel. session in The session handle that you obtain from Initialize or Initialize External Calibration. error in Error conditions t

Error Message

Converts an error or warning code returned by an NI-Sync function into a readable string.

You can display the error string in a dialog box or an indicator on the front panel.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session handle that you obtain from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### error code

The error code that is explained in a user-readable string.

code

Note

error code

Error Message

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle for the NI-Sync device. Pass this handle to other NI-Sync nodes to
 program the behavior of the device.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### error message

A user-readable message string.

error code

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=get-clk10-phase-voltage.html language=enus -->
## TOPIC 00031: Get Clk10 Phase Voltage

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `get-clk10-phase-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/get-clk10-phase-voltage.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the Clk10 phase voltage value currently stored on the specified device's non-volatile onboard memory. You can adjust this value using Adjust Clk10 Phase Voltage. Use this function in conjunction with the other NI-Sync external calibration functions to determine if the device needs an external

Get Clk10 Phase Voltage

Reads the Clk10 phase voltage value currently stored on the specified device's non-volatile onboard memory.

You can adjust this value using Adjust Clk10 Phase Voltage. Use this function in conjunction with the other NI-Sync external calibration functions to determine if the device needs an external calibration session.

Note

- You do not need a calibration password to use this function. You can invoke this function with an instrument handle created with either Initialize (niSync) or Initialize External Calibration.
- If you adjust the Clk10 phase voltage using Adjust Clk10 Phase Voltage as part of an open session, this function returns the new Clk10 phase voltage value you set using Adjust Clk10 Phase Voltage.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session handle that you obtain from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtained from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### voltage

The current Clk10 phase voltage, in volts, stored on the device's non-volatile onboard memory.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=get-dds-start-pulse-phase-voltage.html language=enus -->
## TOPIC 00032: Get DDS Start Pulse Phase Voltage

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `get-dds-start-pulse-phase-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/get-dds-start-pulse-phase-voltage.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the phase voltage of the DDS start pulse currently stored on the specified device's non-volatile onboard memory. You can adjust this value using Adjust DDS Start Pulse Phase Voltage. Use this function to determine if the device needs to be externally calibrated. You do not need a calibration p

Get DDS Start Pulse Phase Voltage

Reads the phase voltage of the DDS start pulse currently stored on the specified device's non-volatile onboard memory.

You can adjust this value using Adjust DDS Start Pulse Phase Voltage. Use this function to determine if the device needs to be externally calibrated.

Note

- You do not need a calibration password to use this function. You can invoke this function with an instrument handle created with either Initialize (niSync) or Initialize External Calibration.
- If you adjust the DDS start pulse phase voltage using Adjust DDS Start Pulse Phase Voltage as part of an open session, this function returns the new DDS start pulse phase voltage value you set using Adjust DDS Start Pulse Phase Voltage.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session handle that you obtain from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtained from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### voltage

The current DDS start pulse phase voltage, in volts, stored in the device's non-volatile onboard memory.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=get-ext-cal-last-date-time.html language=enus -->
## TOPIC 00033: Get External Calibration Last Date and Time

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `get-ext-cal-last-date-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/get-ext-cal-last-date-time.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the date and time, in Greenwich Mean Time (GMT), of the specified device's last external calibration session. Use this function to determine if your device needs external calibration or plan ahead for a future external calibration session. You do not need to enter a calibration password to use

Get External Calibration Last Date and Time

Reads the date and time, in Greenwich Mean Time (GMT), of the specified device's last external calibration session.

Use this function to determine if your device needs external calibration or plan ahead for a future external calibration session.

Note

- You do not need to enter a calibration password to use this function. You can invoke this function with an instrument handle created with either Initialize (niSync) or Initialize External Calibration.
- The date and time returned by this function updates every time you invoke Close External Calibration with action set to 
 Commit , even if no calibration constants were changed.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session handle that you obtain from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtained from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### year

The year of the module's last external calibration.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### month

The month of the module's last external calibration session.

Valid values:

| Value | Month |
| --- | --- |
| 1 | January |
| 2 | February |
| 3 | March |
| 4 | April |
| 5 | May |
| 6 | June |
| 7 | July |
| 8 | August |
| 9 | September |
| 10 | October |
| 11 | November |
| 12 | December |

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### day

The day of the month when the module was last externally calibrated.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### hour

The hour, in GMT, of the module's last external calibration.

| Value | Hour (GMT) |
| --- | --- |
| 0 | Midnight |
| 1 | 1:00 a.m. |
| 2 | 2:00 a.m. |
| 3 | 3:00 a.m. |
| 4 | 4:00 a.m. |
| 5 | 5:00 a.m. |
| 6 | 6:00 a.m. |
| 7 | 7:00 a.m. |
| 8 | 8:00 a.m. |
| 9 | 9:00 a.m. |
| 10 | 10:00 a.m. |
| 11 | 11:00 a.m. |
| 12 | Noon |
| 13 | 1:00 p.m. |
| 14 | 2:00 p.m. |
| 15 | 3:00 p.m. |
| 16 | 4:00 p.m. |
| 17 | 5:00 p.m. |
| 18 | 6:00 p.m. |
| 19 | 7:00 p.m. |
| 20 | 8:00 p.m. |
| 21 | 9:00 p.m. |
| 22 | 10:00 p.m. |
| 23 | 11:00 p.m. |

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### minute

The minute, in GMT, of the module's last external calibration.

Valid values range from 0 to 59.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=get-external-calibration-last-temperature.html language=enus -->
## TOPIC 00034: Get External Calibration Last Temperature

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `get-external-calibration-last-temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/get-external-calibration-last-temperature.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the temperature, in degrees Celsius, of the specified module's circuitry during its last external calibration session. Use this function in conjunction with Read Current Temperature to determine if the device is running at a temperature comparable to when it was last calibrated. You do not nee

Get External Calibration Last Temperature

Reads the temperature, in degrees Celsius, of the specified module's circuitry during its last external calibration session.

Use this function in conjunction with Read Current Temperature to determine if the device is running at a temperature comparable to when it was last calibrated.

Note

- You do not need a calibration password to use this function. You can invoke this function with an instrument handle created with either Initialize (niSync) or Initialize External Calibration.
- This function does not return the ambient temperature of the module. The temperature of the circuitry is generally higher than the ambient temperature.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session handle that you obtain from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtained from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### temperature

The temperature, in degrees Celsius, of the device's circuitry during its last external calibration session.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=get-external-calibration-recommended-interval.html language=enus -->
## TOPIC 00035: Get External Calibration Recommended Interval

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `get-external-calibration-recommended-interval.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/get-external-calibration-recommended-interval.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of months recommended between external calibration sessions for the device. You can use this node in conjunction with other external calibration nodes to determine the next time to run the device through an external calibration session. You do not need a calibration password to us

Get External Calibration Recommended Interval

Returns the number of months recommended between external calibration sessions for the device.

You can use this node in conjunction with other external calibration nodes to determine the next time to run the device through an external calibration session.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session handle that you obtain from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtained from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### months

The recommended external calibration interval, in months, for the specified module.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=get-location.html language=enus -->
## TOPIC 00036: Get Location

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `get-location.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/get-location.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the last calculated latitude, longitude, and altitude of the device's onboard GPS receiver. You must connect an external GPS antenna to the device and set the device's external time reference to GPS in order to receive valid data from this function. For best results, allow the GPS receiver t

Get Location

Returns the last calculated latitude, longitude, and altitude of the device's onboard GPS receiver.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### latitude

The current latitude, in degrees, of the connected device's GPS receiver.

Negative values represent southern latitudes. Positive values represent northern latitudes.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### longitude

The current longitude, in degrees, of the connected device's GPS receiver.

Negative values represent western longitudes. Positive values represent eastern longitudes.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### altitude

The current altitude, in meters, of the connected device's GPS receiver using the WGS-84 earth ellipsoid standard.

Parent topic:

GPS/IRIG

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=get-oscillator-voltage.html language=enus -->
## TOPIC 00037: Get Oscillator Voltage

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `get-oscillator-voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/get-oscillator-voltage.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the voltage that controls the oscillator frequency currently stored on the specified device's non-volatile onboard memory. You can adjust the oscillator voltage using Adjust Oscillator Voltage during an external calibration session. Use this function in conjunction with the other NI-Sync exter

Get Oscillator Voltage

Reads the voltage that controls the oscillator frequency currently stored on the specified device's non-volatile onboard memory.

You can adjust the oscillator voltage using Adjust Oscillator Voltage during an external calibration session. Use this function in conjunction with the other NI-Sync external calibration functions to determine if the function needs an external calibration session.

Note

- You do not need a calibration password to use this function. You can invoke this function with an instrument handle created with either the Initialize (niSync) or Initialize External Calibration.
- If you adjust the oscillator voltage using Adjust Oscillator Voltage as part of an open session, this function returns the new oscillator voltage value you set using Adjust Oscillator Voltage.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session handle that you obtain from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtained from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### voltage

The oscillator voltage, in volts, currently stored on the device's non-volatile onboard memory.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=get-time.html language=enus -->
## TOPIC 00038: Get Time

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `get-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/get-time.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays the current board time of the specified device. NI-Sync supports only the time range between 1 January 1970 and 1 January 2100. Therefore, if the supported time range has ended, an error is returned. NI-Sync devices use the TAI timescale. session in The session that you obtain from Initiali

Get Time

Displays the current board time of the specified device.

NI-Sync supports only the time range between 1 January 1970 and 1 January 2100. Therefore, if the supported time range has ended, an error is returned.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### time

The current board time of the device.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=get-velocity.html language=enus -->
## TOPIC 00039: Get Velocity

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `get-velocity.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/get-velocity.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the last calculated velocity of the specified device's onboard GPS receiver. You can display east velocity, north velocity, and up velocity in meters per second. You must connect an external GPS antenna to your device to receive valid data from this function, and you must enable Mobile Mode

Get Velocity

Returns the last calculated velocity of the specified device's onboard GPS receiver.

You can display east velocity, north velocity, and up velocity in meters per second.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### east velocity

The current east velocity, in meters per second, of the device.

Negative values represent how fast the device is traveling west. Positive values represent how fast the device is traveling east.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### north velocity

The current north velocity, in meters per second, of the device.

Negative values represent how fast the device is traveling south. Positive values represent how fast the device is traveling north.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### up velocity

The current up velocity, in meters per second, of the device.

Negative values represent how fast the device is traveling down. Positive values represent how fast the device is traveling up.

Parent topic:

GPS/IRIG

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=initialize-external-calibration.html language=enus -->
## TOPIC 00040: Initialize External Calibration (niSync)

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `initialize-external-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/initialize-external-calibration.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an external calibration session for the specified device. This function returns an instrument driver session handle that you can use to adjust calibration constants for the module or read current calibration constants stored in the device's non-volatile memory. You must close the external cal

Initialize External Calibration (niSync)

Begins an external calibration session for the specified device.

This function returns an instrument driver session handle that you can use to adjust calibration constants for the module or read current calibration constants stored in the device's non-volatile memory. You must close the external calibration session using Close External Calibration.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### resource name

The resource name of the module to initialize. You can assign the resource name in NI Measurement & Automation Explorer (MAX).

Optional fields are shown in square brackets.

##### Syntax for Resource Names

Use the following syntax to specify resource names for this parameter:

```text
PXI[bus number]::device number
```

VISA aliases are also valid for the resource name.

##### Resource Name Examples

| Resource Name | Description |
| --- | --- |
| Dev1 | DAQmx name (set in MAX) |
| PXI1Slot5 | DAQmx name |
| PXI0::15::INSTR | PXI bus 0, device number 15 |
| PXI::15::INSTR | PXI bus 0, device number 15 |
| PXI4::9::INSTR | PXI bus 4, device number 9 |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### password

The external calibration password for the module.

You must enter the correct case-sensitive password exactly as it is stored in the device's non-volatile onboard memory to begin an external calibration session.

Note

Change External Calibration Password

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### calibration session out

A session handle you use to identify the device in all subsequent NI-Sync nodes, including external calibration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=initialize-nisync.html language=enus -->
## TOPIC 00041: Initialize (niSync)

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `initialize-nisync.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/initialize-nisync.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new NI-Sync instrument driver session. You must invoke this node any time you want to use NI-Sync functions, and you must open a separate session for each device. You can use the instrument handle returned from this node to identify the device to other NI-Sync nodes, including NI-Sync exte

Initialize (niSync)

Creates a new NI-Sync instrument driver session.

You must invoke this node any time you want to use NI-Sync functions, and you must open a separate session for each device. You can use the instrument handle returned from this node to identify the device to other NI-Sync nodes, including NI-Sync external calibration nodes.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### resource name

The resource name of the module to initialize. You can assign the resource name in NI Measurement & Automation Explorer (MAX).

Optional fields are shown in square brackets.

##### Syntax for Resource Names

Use the following syntax to specify resource names for this parameter:

```text
PXI[bus number]::device number
```

VISA aliases are also valid for the resource name.

##### Resource Name Examples

| Resource Name | Description |
| --- | --- |
| Dev1 | DAQmx name (set in MAX) |
| PXI1Slot5 | DAQmx name |
| PXI0::15::INSTR | PXI bus 0, device number 15 |
| PXI::15::INSTR | PXI bus 0, device number 15 |
| PXI4::9::INSTR | PXI bus 4, device number 9 |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### id query

A Boolean that specifies whether to query the instrument ID to determine if the instrument is compatible with the NI-Sync driver.

| True | Queries the instrument ID. |
| --- | --- |
| False | Does not query the instrument ID. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset device

A Boolean value that specifies whether to reset the NI-Sync module (including the external time reference, any connected terminals, and all scheduled future time events) during the initialization procedure.

| True | The NI-Sync module is reset during the initialization procedure. |
| --- | --- |
| False | The NI-Sync module is not reset during the initialization procedure. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle for the NI-Sync device. Pass this handle to other NI-Sync nodes to
 program the behavior of the device.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

NI-Sync Nodes

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=measure-frequency.html language=enus -->
## TOPIC 00042: Measure Frequency

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `measure-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/measure-frequency.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency of a signal at the specified terminal. The terminal you specify in source terminal must contain a digital signal to function. session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The node responds to this input acco

Measure Frequency

Returns the frequency of a signal at the specified terminal.

The terminal you specify in source terminal must contain a digital signal to function.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source terminal

The source terminal of the signal to measure.

Valid values:

| Name | Description |
| --- | --- |
| PFI<n> | The PFI connectors on the front panel of your module. |
| PFI_LVDS<n> | The PFI low voltage differential signaling (LVDS) input/output connectors on the front panel of your device. Signals on PFI_LVDS lines use the standard PFI synchronization clock. |
| PXI_Trig<n> | The basic trigger lines of the PXI or PXIe chassis. |
| PXI_Star<n> | The star trigger lines of the PXI or PXIe chassis. Each trigger line is a dedicated connection between the system timing slot and one other slot. Note Each PXI_Star trigger is mapped to a single slot. This mapping is vendor specific. Refer to the hardware documentation to determine the orientation of PXI_Star lines in the chassis. |
| PXIe_DStarC<n> | The differential star trigger line of the PXIe chassis. Use PXIe_DStarC lines to send trigger and clock signals from a peripheral slot to the system timing slot of the chassis. Note Each PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor specific. Refer to the chassis documentation to determine the orientation of differential star trigger lines. |
| PXIe_DStarB | The differential star trigger lines of the PXIe chassis. Use PXIe_DStarB lines to send trigger signals from the system timing slot to a peripheral slot of the chassis. Note Each PXI_DStarB trigger is mapped to a single slot. This mapping is vendor specific. Refer to the chassis documentation to determine the orientation of differential star trigger lines. |
| Oscillator | The oscillator of the device specified in the instrument handle terminal. |
| ClkIn | The ClkIn input connector on the front panel of the device. Using ClkIn, you can connect a 10 MHz reference clock directly to the PXI_Clk10_In pin. |

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### duration

The length of time, in seconds, to measure the frequency.

Set a longer duration to return a more accurate frequency measurement.

Default value: 0.00000100

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### decimation count

How much to decimate incoming trigger events.

Use this value with a time-based device to adjust the number of timestamps that should elapse before the next timestamp is recorded. For example, if you set the decimation count to 10, the function will record every tenth timestamp. The value must be greater than or equal to one.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### measured frequency

The frequency, in Hz, measured at the specified terminal.

The measurable frequency range is dependent on the hardware; refer to the hardware's documentation to determine the frequency range of any given terminal.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### actual duration

The actual duration, in seconds, that the function measured the frequency of the signal at the specified terminal.

If the value you entered in duration is not a multiple of the PXI_Clk10 period, the actual duration will be the closest multiple of 100 ns.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### frequency error

The margin of error calculated for the frequency measurement.

The formula used to calculate the error is:

error = [ (10M / base_freq) ] / [actual_duration]

where base_freq refers to the base frequency and actual_duration refers to the output of the actual duration terminal.

#### Using Measure Frequency with Time-Based Devices

The following time-based timing and synchronization devices are compatible with Measure Frequency:

- PXI-6683
- PXI-6683H
- PXI-6682
- PXI-6682H

When using Measure Frequency with a PXI-6683(H) or other time-based device, timestamping is used to measure the frequency. The function will measure timestamps that have an actual duration greater than or equal to the specified duration. If timestamps are not detected or not enough timestamps are detected due to a slow signal or a decimation count that is too high, the function may encounter an error. Generally, you should have a timestamp within every second to avoid this error.

Note

The decimation count terminal is only necessary on PXI-6683(H) and other time-based devices. In order to set the decimation count accurately, you should have a general idea of what range (Hz, kHz, MHz) the signal to be measured occupies.

Only PFI and PXI_Trig lines can be used as the source terminal on time-based devices.

For the most accurate measurement, the board clock for the time-based device you are trying to measure should be set to free running. If you are synchronizing to GPS, IRIG, or a PTP protocol like 1588, the function may encounter an error or the result may be unreliable.

#### Troubleshooting the Software Buffer Overflow Error

When you are measuring frequency with this function using a time-based device, you may encounter a software buffer overflow error. This means that LabVIEW does not have enough memory to store the recorded timestamps when measuring frequency. You can take one or more of the following actions to resolve a software buffer overflow error:

- Set a higher value in the decimation count terminal.
- Set the Time Stamp Buffer Size property with niSync Properties by selecting 
 Timing»Time Stamps»Time Stamp Buffer Size . Use this value to manually adjust the size, in number of time stamps, of the software buffer where timestamps are stored.

#### Using Measure Frequency with Signal-Based Devices

The following signal-based timing and synchronization devices are compatible with Measure Frequency:

- PXI-6652 (PFI0 only)
- PXI-6653 (PFI0 only)
- PXI-6672 (PFI0 only)
- PXIe-6674T

Using a signal-based device and Measure Frequency, you can measure the frequency of the device's oscillator, an external clock connected to a front panel input, or a full speed or divided synchronization clock.

When measuring the frequency on a signal-based device, you must set the duration in multiples of 100 nanoseconds, i.e. a multiple of the PXI_Clk10 period. If the duration is not a multiple of the PXI_Clk10 period, it will be coerced to the closest multiple and returned in the actual duration terminal.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=nisync-constant.html language=enus -->
## TOPIC 00043: NI-Sync Resource Name

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `nisync-constant.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/nisync-constant.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the instrument handle to use for NI-Sync operations.

NI-Sync Resource Name

Specifies the instrument handle to use for NI-Sync operations.

Parent topic:

NI-Sync Nodes

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=nisync-prop-node.html language=enus -->
## TOPIC 00044: niSync Properties

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `nisync-prop-node.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/nisync-prop-node.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets and displays parameters of NI-Sync devices. You can use this function to perform configuration tasks for NI-Sync devices, including monitoring trigger line states, adjusting the frequency of a generated clock, and setting a synchronization clock. nisync in The instrument handle that you obtain

niSync Properties

Sets and displays parameters of NI-Sync devices.

You can use this function to perform configuration tasks for NI-Sync devices, including
 monitoring trigger line states, adjusting the frequency of a generated clock, and setting a
 synchronization clock.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### nisync in

The instrument handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### nisync out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

NI-Sync Nodes

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=persist-configuration.html language=enus -->
## TOPIC 00045: Persist Configuration

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `persist-configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/persist-configuration.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns modified settings even after the controller is rebooted. This node is supported only on Linux RT targets. By default, modified NI-Sync settings are reverted to the last saved (persisted) configuration after the controller reboots. Call this node after you have modified settings to keep those

Persist Configuration

Returns modified settings even after the controller is rebooted.

Note

By default, modified NI-Sync settings are reverted to the last saved (persisted) configuration after the controller reboots. Call this node after you have modified settings to keep those settings.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=read-current-temperature.html language=enus -->
## TOPIC 00046: Read Current Temperature

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `read-current-temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/read-current-temperature.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the current circuitry temperature, in degrees Celsius, of the device. Use this function to determine if the module is in a properly cooled location or if it needs external calibration. You do not need a calibration password to use this function. You can invoke this function with an instrument

Read Current Temperature

Reads the current circuitry temperature, in degrees Celsius, of the device.

Use this function to determine if the module is in a properly cooled location or if it needs external calibration.

Note

- You do not need a calibration password to use this function. You can invoke this function with an instrument handle created with either Initialize (niSync) or Initialize External Calibration.
- This function does not return the ambient temperature of the module. The temperature of the circuitry is generally higher than the ambient temperature.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session handle that you obtain from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtained from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### temperature

The temperature, in degrees Celsius, of the specified module's circuitry.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=read-last-gps-irig-timestamp-gps.html language=enus -->
## TOPIC 00047: GPS

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `read-last-gps-irig-timestamp-gps.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/read-last-gps-irig-timestamp-gps.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns two timestamps: one with the module's board time when the module received the GPS pulse per second signal, and the other with the time of the onboard GPS receiver. Use these two values to determine the delay between GPS and the module. session in The session that you obtain from Initialize.

GPS

Returns two timestamps: one with the module's board time when the module received the GPS pulse per second signal, and the other with the time of the onboard GPS receiver.

Use these two values to determine the delay between GPS and the module.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### GPS time

The time reported by the onboard GPS receiver.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### timestamp

The board time at which the GPS pulse per second was received.

The parameter returns 0 if the module never received a valid timestamp.

Parent topic:

Read Last GPS or IRIG Timestamp Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=read-last-gps-or-irig-timestamp-irig.html language=enus -->
## TOPIC 00048: IRIG

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `read-last-gps-or-irig-timestamp-irig.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/read-last-gps-or-irig-timestamp-irig.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns two timestamps: one with the board time when the module received the IRIG message, and one with the time encoded in the IRIG message. You can use these two values to determine the delay between the external IRIG source and the module or to test the stability of an external IRIG source agains

IRIG

Returns two timestamps: one with the board time when the module received the IRIG message, and one with the time encoded in the IRIG message.

You can use these two values to determine the delay between the external IRIG source and the module or to test the stability of an external IRIG source against an external time reference.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The terminal that is connected to the external IRIG source.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### IRIG time

The time encoded in the IRIG message.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### timestamp

The board time at which the IRIG message was received.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Read Last GPS or IRIG Timestamp Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=read-last-gps-or-irig-timestamp.html language=enus -->
## TOPIC 00049: Read Last GPS or IRIG Timestamp Multimode Function

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `read-last-gps-or-irig-timestamp.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/read-last-gps-or-irig-timestamp.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the last GPS or IRIG timestamp received from the device.

Read Last GPS or IRIG Timestamp Multimode Function

Returns the last GPS or IRIG timestamp received from the device.

GPS/IRIG

GPS and IRIG functions for NI-Sync.

GPS

Returns two timestamps: one with the module's board time when the module received the GPS pulse per second signal, and the other with the time of the onboard GPS receiver.

IRIG

Returns two timestamps: one with the board time when the module received the IRIG message, and one with the time encoded in the IRIG message.

Parent topic:

GPS/IRIG

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=read-trigger-time-stamp-multiple.html language=enus -->
## TOPIC 00050: Multiple Timestamps

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `read-trigger-time-stamp-multiple.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/read-trigger-time-stamp-multiple.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads multiple timestamps recorded on the internal software buffer for a specific terminal and returns them in an array. You must invoke Enable Time Stamp Trigger for this function to return timestamps. session in The session that you obtain from Initialize. terminal The terminal that contains the d

Multiple Timestamps

Reads multiple timestamps recorded on the internal software buffer for a specific terminal and returns them in an array.

You must invoke Enable Time Stamp Trigger for this function to return timestamps.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The terminal that contains the digital signal you want to read timestamps from.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The number of seconds to wait for a time stamp to be generated before returning a timeout error.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### number of timestamps

The number of timestamps to read.

If the number of timestamps is not available before the timeout elapses, the number read before the timeout occurred is returned through the time stamp(s) out and detected edges arrays.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in (no error)

error in (no error) accepts error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/i1dtimestamp.png']

##### time stamp(s) out

The oldest unread timestamp detected on the specified trigger terminal.

The timestamp is removed from the software buffer when read.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### detected edges

Returns an array of integer enumerations of size equal to the number of timestamps read that specifies the detected trigger conditions.

| rising | The detected timestamp was recorded on the rising edge of the trigger. |
| --- | --- |
| falling | The detected timestamp was recorded on the falling edge of the trigger. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

error out passes error or warning information out of a VI to be used by other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

#### Troubleshooting a Full Buffer

If the buffer associated with terminal is full, timestamp and trigger timestamp operations are suspended and you receive Error -1074118582. This function continues to return previously generated timestamps, despite the overflow condition, until no timestamps are available. You can clear this error condition using Disable Time Stamp Trigger, or you can expand the size of the timestamp buffer using niSync Properties.

Parent topic:

Read Trigger Time Stamp Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=read-trigger-time-stamp-single.html language=enus -->
## TOPIC 00051: Single Timestamp

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `read-trigger-time-stamp-single.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/read-trigger-time-stamp-single.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a timestamp recorded on the internal software buffer for a specific terminal. You must invoke Enable Time Stamp Trigger for this function to return a timestamp. session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The node responds

Single Timestamp

Reads a timestamp recorded on the internal software buffer for a specific terminal.

You must invoke Enable Time Stamp Trigger for this function to return a timestamp.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The terminal that contains the digital signal you want to read timestamps from.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The number of seconds to wait for a time stamp to be generated before returning a timeout error.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### time stamp out

The oldest unread timestamp detected on the specified trigger terminal.

The timestamp is removed from the software buffer when read.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### detected edge

The detected trigger condition of the timestamp.

| rising | The timestamp was written on the rising edge of the digital signal. |
| --- | --- |
| falling | The timestamp was written on the falling edge of the digital signal. |

#### Troubleshooting a Full Buffer

If the buffer associated with terminal is full, timestamp and trigger timestamp operations are suspended and you receive Error -1074118582. This function continues to return previously generated timestamps, despite the overflow condition, until no timestamps are available. You can clear this error condition using Disable Time Stamp Trigger, or you can expand the size of the timestamp buffer using niSync Properties.

Parent topic:

Read Trigger Time Stamp Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=read-trigger-time-stamp.html language=enus -->
## TOPIC 00052: Read Trigger Time Stamp Multimode Function

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `read-trigger-time-stamp.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/read-trigger-time-stamp.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads timestamps recorded on the internal software buffer for the specified terminal.You must invoke Enable Time Stamp Trigger for this function to return any timestamps.

Read Trigger Time Stamp Multimode Function

Reads timestamps recorded on the internal software buffer for the specified terminal.You must invoke Enable Time Stamp Trigger for this function to return any timestamps.

Timing

Timing nodes for NI-Sync devices.

Single Timestamp

Reads a timestamp recorded on the internal software buffer for a specific terminal.

Multiple Timestamps

Reads multiple timestamps recorded on the internal software buffer for a specific terminal and returns them in an array.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=reset.html language=enus -->
## TOPIC 00053: Reset

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `reset.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/reset.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the specified device to its default state. You can also reset a module before the program starts by using reset device of Initialize (niSync). session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The node responds to this input ac

Reset

Resets the specified device to its default state.

You can also reset a module before the program starts by using reset device of Initialize (niSync).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Reset Behavior

When you invoke this function on an NI-Sync device, it executes the following actions:

- Disconnects all terminal connections.
- Sets the DDS frequency to 0 Hz.
- Disables the PLL circuit.
- Sets all PFI front panel connectors to 50 ohm input impedance.
- Sets the front and rear zone synchronization clock sources to PXI_Clk10.

#### Reset Behavior for Time-Based Modules

For time-based timing and synchronization modules, invoking this function also executes the following actions:

- Stops PTP participation.
- Resets the 1588 clock to the current system time.
- Clears all clocks.
- Clears all hardware and software triggers.
- Clears all future time events.
- Disables timestamp triggers.
- Sets the external time reference to the default source.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=resource-name-control.html language=enus -->
## TOPIC 00054: NI-Sync Resource Name Control

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `resource-name-control.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/resource-name-control.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the instrument handle to use for NI-Sync operations.

NI-Sync Resource Name Control

Specifies the instrument handle to use for NI-Sync operations.

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=revision-query.html language=enus -->
## TOPIC 00055: Revision Query

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `revision-query.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/revision-query.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision numbers of the NI-Sync driver and the specified module's firmware. Use this function to confirm that your hardware and software is up to date or compatible with a specific feature. session in The session that you obtain from Initialize. error in Error conditions that occur befor

Revision Query

Returns the revision numbers of the NI-Sync driver and the specified module's firmware.

Use this function to confirm that your hardware and software is up to date or compatible with a specific feature.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### firmware revision

The firmware revision number of the device.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### instrument driver revision

The revision numbers of the installed NI-Sync drivers.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=routing-category.html language=enus -->
## TOPIC 00056: Routing

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `routing-category.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/routing-category.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routing functions for NI-Sync devices.

Routing

Routing functions for NI-Sync devices.

NI-Sync Nodes

Nodes to control NI timing and synchronization modules.

Connect Clock Terminals

Connects a source clock terminal to a destination clock terminal.

Connect Software Trigger

Connects the global software trigger terminal to a destination trigger terminal.

Connect Trigger Terminals

Routes triggers through the PXI backplane, between devices, or between multiple chassis.

Disconnect Clock Terminals

Closes a route between a source clock terminal and a destination clock terminal.

Disconnect Software Trigger

Closes a route between the global software trigger and a destination trigger terminal.

Disconnect Trigger Terminals

Closes a route between a source trigger terminal and a destination trigger terminal.

Send Software Trigger

Sends a trigger pulse using the global software trigger. The global software trigger terminal must be connected to a destination terminal for this operation to have any effect.

Parent topic:

NI-Sync Nodes

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=self-test.html language=enus -->
## TOPIC 00057: Self-Test

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `self-test.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/self-test.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs the module's self-test routine and returns the test results. This operation verifies that the NI-Sync I/O session can communicate with the module's driver. session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The node responds to th

Self-Test

Runs the module's self-test routine and returns the test results.

This operation verifies that the NI-Sync I/O session can communicate with the module's driver.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### self-test message

The self-test response from the module.

Refer to the device's documentation for an explanation of the self-test response.

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### self test result

The result of the instrument self-test.

| Self-Test Code | Description |
| --- | --- |
| 0 | Self-test passed |
| 1 | Self-test failed |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=send-software-trigger.html language=enus -->
## TOPIC 00058: Send Software Trigger

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `send-software-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/send-software-trigger.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger pulse using the global software trigger. The global software trigger terminal must be connected to a destination terminal for this operation to have any effect. When you invoke this function, the global software trigger pulse sends simultaneously to all the destination terminals it i

Send Software Trigger

Sends a trigger pulse using the global software trigger. The global software trigger terminal must be connected to a destination terminal for this operation to have any effect.

When you invoke this function, the global software trigger pulse sends simultaneously to all the destination terminals it is connected to. Using this function, the user of the program can send a trigger signal by pushing a button or executing a command.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source terminal

The source software trigger terminal to connect to the destination terminal.

The only acceptable value is Global Software Trigger.

Default value: Global Software Trigger

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Routing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=set-time-manual.html language=enus -->
## TOPIC 00059: Manual

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `set-time-manual.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/set-time-manual.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the absolute board time to a user-specified time. NI-Sync devices use the TAI timescale. session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behav

Manual

Sets the absolute board time to a user-specified time.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### initial time

The time to apply as the current board time.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Set Time Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=set-time-reference-1588-ordinary-clock.html language=enus -->
## TOPIC 00060: 1588 Ordinary Clock

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `set-time-reference-1588-ordinary-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/set-time-reference-1588-ordinary-clock.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the external time reference of the device to 1588 ordinary clock. If the device is not a 1588 slave and you set the time reference to 1588 Ordinary Clock, the board time enters Free Running mode. Calling this function does not explicitly start the 1588 protocol. You must invoke Start 1588 after

1588 Ordinary Clock

Sets the external time reference of the device to 1588 ordinary clock.

If the device is not a 1588 slave and you set the time reference to 1588 Ordinary Clock, the board time enters Free Running mode. Calling this function does not explicitly start the 1588 protocol. You must invoke Start 1588 after setting the time reference for the device to participate in 1588.

Note

- NI-Sync devices use the TAI timescale.
- The servo may apply a macro phase adjustment when your device's board time and the external time reference varies by more than 1 ms. A macro phase adjustment adjust the external time reference by a significant amount, and the time no longer atomically increments. This should not occur on a well-designed and stable network. A macro phase adjustment may affect future time events, clocks, and timestamps. If the external time reference is set forward, future time events and clock transitions that were missed occur immediately. If the external time reference is set backward, future time events and clock transitions are delayed.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in (no error)

error in (no error) accepts error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

error out passes error or warning information out of a VI to be used by other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

Parent topic:

Set Time Reference Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=set-time-reference-802.1as.html language=enus -->
## TOPIC 00061: 802.1AS

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `set-time-reference-802.1as.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/set-time-reference-802.1as.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the external time reference of the device to 802.1AS clock. If the device is not a 802.1AS slave and you set the time reference to 802.1AS, the board time enters Free Running mode. Calling this function does not explicitly start the 802.1AS protocol. You must invoke Start 802.1AS after setting

802.1AS

Sets the external time reference of the device to 802.1AS clock.

If the device is not a 802.1AS slave and you set the time reference to 802.1AS, the board time enters Free Running mode. Calling this function does not explicitly start the 802.1AS protocol. You must invoke Start 802.1AS after setting the time reference for the device to participate in 802.1AS.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in (no error)

error in (no error) accepts error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

error out passes error or warning information out of a VI to be used by other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

Parent topic:

Set Time Reference Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=set-time-reference-free-running.html language=enus -->
## TOPIC 00062: Free Running

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `set-time-reference-free-running.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/set-time-reference-free-running.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time reference of the device to free running. In Free Running mode, the clock's start time and frequency are not tied to any external time reference. The board time atomically increments at the last applied frequency. Use this mode if you do not have a strong connection to a network or an e

Free Running

Sets the time reference of the device to free running.

In Free Running mode, the clock's start time and frequency are not tied to any external time reference. The board time atomically increments at the last applied frequency. Use this mode if you do not have a strong connection to a network or an external time reference. Your device will automatically enter free running mode if the external time reference you select does not provide valid time information.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Set Time Reference Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=set-time-reference-gps.html language=enus -->
## TOPIC 00063: GPS

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `set-time-reference-gps.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/set-time-reference-gps.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the external time reference of the device to GPS. The servo may apply a macro phase adjustment when your device's board time and the external time reference varies by more than 1 ms. A macro phase adjustment adjust the external time reference by a significant amount, and the time no longer atom

GPS

Sets the external time reference of the device to GPS.

Note

- The servo may apply a macro phase adjustment when your device's board time and the external time reference varies by more than 1 ms. A macro phase adjustment adjust the external time reference by a significant amount, and the time no longer atomically increments. This should not occur on a well-designed and stable network. A macro phase adjustment may affect future time events, clocks, and timestamps. If the external time reference is set forward, future time events and clock transitions that were missed occur immediately. If the external time reference is set backward, future time events and clock transitions are delayed.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in (no error)

error in (no error) accepts error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

error out passes error or warning information out of a VI to be used by other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

Parent topic:

Set Time Reference Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=set-time-reference-irig.html language=enus -->
## TOPIC 00064: IRIG

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `set-time-reference-irig.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/set-time-reference-irig.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the external time reference of the device to IRIG-B AM or IRIG-B DC. You must have an external IRIG source connected to the specified terminal for this mode to function. The servo may apply a macro phase adjustment when the device's board time and the external time reference varies by more than

IRIG

Sets the external time reference of the device to IRIG-B AM or IRIG-B DC.

You must have an external IRIG source connected to the specified terminal for this mode to function.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### IRIG type

The type of IRIG output generated by the external IRIG source.

| IRIGB DC | The IRIG-B DC output. |
| --- | --- |
| IRIGB AM | The IRIG-B AM output. |

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The terminal on which to enable IRIG as the time reference.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in (no error)

error in (no error) accepts error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

error out passes error or warning information out of a VI to be used by other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

Parent topic:

Set Time Reference Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=set-time-reference-pps.html language=enus -->
## TOPIC 00065: PPS

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `set-time-reference-pps.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/set-time-reference-pps.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the external time reference of the device to PPS (pulse per second). The servo may apply a macro phase adjustment when your device's board time and the external time reference varies by more than 1 ms. A macro phase adjustment adjusts the external time reference by a significant amount, and the

PPS

Set the external time reference of the device to PPS (pulse per second).

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### use manual time

A Boolean value that specifies whether or not to use the user-supplied time or the OS system time to represent the time at which the first pulse is received.

| False | Reads the OS system time when the first pulse is received and uses that time to set the board time. |
| --- | --- |
| True | Uses the user-specified initial time to set the board time when the first pulse is received. |

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### terminal

The terminal on which the PPS signal is supplied.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in (no error)

error in (no error) accepts error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### initial time

The value to set the board time to when the module receives the first pulse.

use manual time

True

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

error out passes error or warning information out of a VI to be used by other VIs.

The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### status

status is either TRUE (X) for an error, or FALSE (checkmark) for no error or a warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### code

code identifies the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### source

source specifies the origin of the error or warning. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed.

Parent topic:

Set Time Reference Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=set-time-reference.html language=enus -->
## TOPIC 00066: Set Time Reference Multimode Function

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `set-time-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/set-time-reference.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the external time reference of a time-based timing and synchronization module. NI-Sync uses this time reference to update the value and frequency of the module's board time.

Set Time Reference Multimode Function

Sets the external time reference of a time-based timing and synchronization module. NI-Sync uses this time reference to update the value and frequency of the module's board time.

Timing

Timing nodes for NI-Sync devices.

1588 Ordinary Clock

Sets the external time reference of the device to 1588 ordinary clock.

802.1AS

Sets the external time reference of the device to 802.1AS clock.

Free Running

Sets the time reference of the device to free running.

GPS

Sets the external time reference of the device to GPS.

IRIG

Sets the external time reference of the device to IRIG-B AM or IRIG-B DC.

PPS

Set the external time reference of the device to PPS (pulse per second).

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=set-time-system-clock.html language=enus -->
## TOPIC 00067: System Clock

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `set-time-system-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/set-time-system-clock.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the absolute board time to the OS system time. This function does not change the internal frequency at which the board time increments. NI-Sync devices use the TAI timescale. session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The

System Clock

Sets the absolute board time to the OS system time.

This function does not change the internal frequency at which the board time increments.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Set Time Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=set-time.html language=enus -->
## TOPIC 00068: Set Time Multimode Function

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `set-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/set-time.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the absolute board time of the device to a certain time. This function does not change the frequency at which the board time increments; use Reset Frequency to reset the board time increment frequency.NI-Sync devices use the TAI timescale.

Set Time Multimode Function

Sets the absolute board time of the device to a certain time. This function does not change the frequency at which the board time increments; use Reset Frequency to reset the board time increment frequency.NI-Sync devices use the TAI timescale.

Timing

Timing nodes for NI-Sync devices.

Manual

Sets the absolute board time to a user-specified time.

System Clock

Sets the absolute board time to the OS system time.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=start-1588.html language=enus -->
## TOPIC 00069: Start 1588

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `start-1588.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/start-1588.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts running the IEEE-1588 time reference. session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session out The sessi

Start 1588

Starts running the IEEE-1588 time reference.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Start Time Reference Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=start-802.1as.html language=enus -->
## TOPIC 00070: Start 802.1AS

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `start-802.1as.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/start-802.1as.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts running the IEEE-802.1AS time reference. session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session out The se

Start 802.1AS

Starts running the IEEE-802.1AS time reference.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Start Time Reference Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=start-time-reference.html language=enus -->
## TOPIC 00071: Start Time Reference Multimode Function

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `start-time-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/start-time-reference.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts running a specified time reference. To synchronize clocks, future time events, and triggered timestamps to a time reference, use this node in conjunction with Set Time Reference. Use Stop Time Reference to stop running the specified time reference.

Start Time Reference Multimode Function

Starts running a specified time reference. To synchronize clocks, future time events, and triggered timestamps to a time reference, use this node in conjunction with Set Time Reference. Use Stop Time Reference to stop running the specified time reference.

Timing

Timing nodes for NI-Sync devices.

Start 1588

Starts running the IEEE-1588 time reference.

Start 802.1AS

Starts running the IEEE-802.1AS time reference.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=stop-1588.html language=enus -->
## TOPIC 00072: Stop 1588

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `stop-1588.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/stop-1588.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops running the IEEE-1588 time reference. session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session out The sessio

Stop 1588

Stops running the IEEE-1588 time reference.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Stop Time Reference Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=stop-802.1as.html language=enus -->
## TOPIC 00073: Stop 802.1AS

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `stop-802.1as.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/stop-802.1as.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops running the IEEE-802.1AS time reference. session in The session that you obtain from Initialize. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session out The ses

Stop 802.1AS

Stops running the IEEE-802.1AS time reference.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Stop Time Reference Multimode Function

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=stop-time-reference.html language=enus -->
## TOPIC 00074: Stop Time Reference Multimode Function

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `stop-time-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/stop-time-reference.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops running a specified time reference. To synchronize clocks, future time events, and triggered timestamps to a time reference, use this node in conjunction with Set Time Reference. Use Stop Time Reference to stop running the specified time reference.

Stop Time Reference Multimode Function

Stops running a specified time reference. To synchronize clocks, future time events, and triggered timestamps to a time reference, use this node in conjunction with Set Time Reference. Use Stop Time Reference to stop running the specified time reference.

Timing

Timing nodes for NI-Sync devices.

Stop 1588

Stops running the IEEE-1588 time reference.

Stop 802.1AS

Stops running the IEEE-802.1AS time reference.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=sync-gps-irig-category.html language=enus -->
## TOPIC 00075: GPS/IRIG

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `sync-gps-irig-category.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/sync-gps-irig-category.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GPS and IRIG functions for NI-Sync.

GPS/IRIG

GPS and IRIG functions for NI-Sync.

Timing

Timing nodes for NI-Sync devices.

Disable GPS or IRIG Timestamping Multimode Function

Ends GPS or IRIG timestamping on the specified device. You must use this function every time you invoke Enable GPS or IRIG Timestamping.

Enable GPS or IRIG Timestamping Multimode Function

Timestamps an incoming GPS or IRIG signal with the current board time of the specified module.

Get Location

Returns the last calculated latitude, longitude, and altitude of the device's onboard GPS receiver.

Get Velocity

Returns the last calculated velocity of the specified device's onboard GPS receiver.

Read Last GPS or IRIG Timestamp Multimode Function

Returns the last GPS or IRIG timestamp received from the device.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=sync-timing-category.html language=enus -->
## TOPIC 00076: Timing

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `sync-timing-category.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/sync-timing-category.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Timing nodes for NI-Sync devices.

Timing

Timing nodes for NI-Sync devices.

NI-Sync Nodes

Nodes to control NI timing and synchronization modules.

Clear Clock

Frees a resource that contains a generated clock.

Clear Future Time Events

Frees the terminal of any future time events previously created.

Create Clock Multimode Function

Generates a clock synchronized to the board time of the module.

Create Future Time Event

Schedules a future time event.

Disable Time Stamp Trigger

Ends timestamping enabled by Enable Time Stamp Trigger.

Enable Time Stamp Trigger

Creates a timestamp every time the signal of a specified trigger or clock changes. You can then read a single timestamp or multiple timestamps at a later point in the data flow.

Get Time

Displays the current board time of the specified device.

Read Trigger Time Stamp Multimode Function

Reads timestamps recorded on the internal software buffer for the specified terminal.You must invoke Enable Time Stamp Trigger for this function to return any timestamps.

Set Time Multimode Function

Sets the absolute board time of the device to a certain time. This function does not change the frequency at which the board time increments; use Reset Frequency to reset the board time increment frequency.NI-Sync devices use the TAI timescale.

Set Time Reference Multimode Function

Sets the external time reference of a time-based timing and synchronization module. NI-Sync uses this time reference to update the value and frequency of the module's board time.

Wait Until Time

Waits until the board time of the device reaches a specified time before continuing the program.

Start Time Reference Multimode Function

Starts running a specified time reference. To synchronize clocks, future time events, and triggered timestamps to a time reference, use this node in conjunction with Set Time Reference. Use Stop Time Reference to stop running the specified time reference.

Stop Time Reference Multimode Function

Stops running a specified time reference. To synchronize clocks, future time events, and triggered timestamps to a time reference, use this node in conjunction with Set Time Reference. Use Stop Time Reference to stop running the specified time reference.

GPS/IRIG

GPS and IRIG functions for NI-Sync.

Parent topic:

NI-Sync Nodes

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=utility-palette.html language=enus -->
## TOPIC 00077: Utility

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `utility-palette.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/utility-palette.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Utility functions for NI-Sync.

Utility

Utility functions for NI-Sync.

NI-Sync Nodes

Nodes to control NI timing and synchronization modules.

Error Message

Converts an error or warning code returned by an NI-Sync function into a readable string.

Measure Frequency

Returns the frequency of a signal at the specified terminal.

Persist Configuration

Returns modified settings even after the controller is rebooted.

Read Current Temperature

Reads the current circuitry temperature, in degrees Celsius, of the device.

Reset

Resets the specified device to its default state.

Revision Query

Returns the revision numbers of the NI-Sync driver and the specified module's firmware.

Self-Test

Runs the module's self-test routine and returns the test results.

Parent topic:

NI-Sync Nodes

<!--NI_TOPIC bundle=ni-sync-lvnxg-api-ref path=wait-until-time.html language=enus -->
## TOPIC 00078: Wait Until Time

- bundle_id: `ni-sync-lvnxg-api-ref`
- source_path: `wait-until-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-lvnxg-api-ref/raw/resource/enus/wait-until-time.html
- document_id: `ni-sync-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the board time of the device reaches a specified time before continuing the program. Use this function to ensure that future time events have completed before you close the session or stop the application. NI-Sync devices use the TAI timescale. session in The session handle that you obta

Wait Until Time

Waits until the board time of the device reaches a specified time before continuing the program.

Use this function to ensure that future time events have completed before you close the session or stop the application.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The session handle that you obtain from Initialize or Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### time stamp

The board time to wait for before continuing execution.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

The session handle that you obtain from Initialize.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Timing
