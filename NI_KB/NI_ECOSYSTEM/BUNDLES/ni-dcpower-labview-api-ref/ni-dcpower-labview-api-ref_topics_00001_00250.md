# NI DOCUMENT BUNDLE: ni-dcpower-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-dcpower-labview-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=api-reference.html language=enus -->
## TOPIC 00001: NI-DCPower LabVIEW API Reference

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `api-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/api-reference.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This API reference provides information about the programmatic elements available for this product. Looking for Something Else? For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse R

### NI-DCPower LabVIEW API Reference

This API reference provides information about the programmatic elements available for this product.

#### Looking for Something Else?

For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse *Related Information*.

Related information:

- NI-DCPower Driver Downloads
- NI-DCPower Release Notes
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/advancedsequencing-mnu.html language=enus -->
## TOPIC 00002: Advanced Sequencing

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/advancedsequencing-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/advancedsequencing-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower Advanced Sequence VIs for configuring the source and measure unit with a series of property or attribute values. You must set the source mode to Sequence. Use advanced sequencing instead of Sequence source mode when you want more options for configuring the device in each step of

### Advanced Sequencing

Use the NI-DCPower Advanced Sequence VIs for configuring the source and measure unit with a series of property or attribute values. You must set the source mode to Sequence.

Use advanced sequencing instead of Sequence source mode when you want more options for configuring the device in each step of the sequence.

- [niDCPower Create Advanced Sequence With Channels VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-with-channels-vi.html) Creates an empty advanced sequence. Call the niDCPower Create Advanced Sequence Step Poly VI to add steps and, optionally, a Commit step to the active advanced sequence.
- [niDCPower Create Advanced Sequence Step With Channels (Poly) VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-step-with-channels-poly-vi.html) Creates a step in the Active advanced sequence.
- [niDCPower Delete Advanced Sequence With Channels VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-delete-advanced-sequence-with-channels-vi.html) Deletes a previously created advanced sequence and all the advanced sequence steps in the advanced sequence.

Parent topic:

Source

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/calibration-mnu.html language=enus -->
## TOPIC 00003: Calibration

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/calibration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/calibration-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower Calibration VIs to perform a self calibration or an external calibration on the device. icon

### Calibration

Use the NI-DCPower Calibration VIs to perform a self calibration or an external calibration on the device.

[IMAGE alt='icon' src='calibration-mnu.png']

- [niDCPower Cal Self Calibrate VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-self-calibrate-vi.html) Performs a self-calibration upon the specified channel(s).
- [External Calibration](../../instr-lib/nidcpower/externalcalibration-mnu.html) Use the NI-DCPower External Calibration VIs to perform an external calibration of the device. Refer to the manual calibration procedure for your device for more information.
- [Calibration Utility](../../instr-lib/nidcpower/calibrationutility-mnu.html) Use the NI-DCPower Calibration Utility VIs to get and set information related to the calibration of the device.
- [LCR Compensation](../../instr-lib/nidcpower/lcrcompensation-mnu.html) Use the NI-DCPower LCR Compensation VIs to perform custom cable compensation and LCR compensation for LCR measurements.

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/calibrationutility-mnu.html language=enus -->
## TOPIC 00004: Calibration Utility

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/calibrationutility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/calibrationutility-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower Calibration Utility VIs to get and set information related to the calibration of the device. icon

### Calibration Utility

Use the NI-DCPower Calibration Utility VIs to get and set information related to the calibration of the device.

[IMAGE alt='icon' src='calibrationutility-mnu.png']

- [niDCPower Change Ext Cal Password VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-change-ext-cal-password-vi.html) Changes the password that is required to initialize an external calibration session. The password can be a maximum of four alphanumeric characters.
- [niDCPower Get Cal User Defined Info VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-get-cal-user-defined-info-vi.html) Returns the user-defined information in the device onboard EEPROM.
- [niDCPower Set Cal User Defined Info VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-set-cal-user-defined-info-vi.html) Stores a user-defined string of characters in the device onboard EEPROM. If the string is longer than the maximum allowable size, it is truncated.
- [niDCPower Get Cal User Defined Info Max Size VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-get-cal-user-defined-info-max-size-vi.html) Returns the maximum number of characters that can be used to store user-defined information in the device onboard EEPROM.
- [niDCPower Get Ext Cal Last Date And Time VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-get-ext-cal-last-date-and-time-vi.html) Returns the date and time of the last successful calibration.
- [niDCPower Get Ext Cal Last Temp VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-get-ext-cal-last-temp-vi.html) Returns the onboard temperature of the device, in degrees Celsius, during the last successful external calibration.
- [niDCPower Read Current Temperature VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-read-current-temperature-vi.html) Returns the current onboard temperature, in degrees Celsius, of the device.
- [niDCPower Get Self Cal Last Date And Time VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-get-self-cal-last-date-and-time-vi.html) Returns the date and time of the oldest successful self-calibration from among the channels in the session.
- [niDCPower Get Self Cal Last Temp VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-get-self-cal-last-temp-vi.html) Returns the onboard temperature of the device, in degrees Celsius, during the oldest successful self-calibration from among the channels in the session.
- [niDCPower Get Ext Cal Recommended Interval VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-get-ext-cal-recommended-interval-vi.html) Returns the recommended number of months between external calibrations.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/control-mnu.html language=enus -->
## TOPIC 00005: Control

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/control-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/control-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower Control VIs to control the channel(s) in the session. icon

### Control

Use the NI-DCPower Control VIs to control the channel(s) in the session.

[IMAGE alt='icon' src='control-mnu.png']

- [niDCPower Commit With Channels VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-commit-with-channels-vi.html) Applies previously configured settings to the specified channel(s). Calling this VI moves the channel(s) from the Uncommitted state into the Committed state.
- [niDCPower Initiate With Channels VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-initiate-with-channels-vi.html) Starts generation or acquisition, causing the specified channel(s) to leave the Uncommitted state or Committed state and enter the Running state.
- [niDCPower Abort With Channels VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-abort-with-channels-vi.html) Transitions the specified channel(s) from the Running state to the Uncommitted state. If a sequence is running, it is stopped.

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/dccurrent-mnu.html language=enus -->
## TOPIC 00006: DC Current

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/dccurrent-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/dccurrent-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower DC Current VIs for changing channel settings when the channel is configured for the DC Current output function. icon

### DC Current

Use the NI-DCPower DC Current VIs for changing channel settings when the channel is configured for the DC Current output function.

[IMAGE alt='icon' src='dccurrent-mnu.png']

- [niDCPower Configure Current Level VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-level-vi.html) Configures the current level that the specified channel(s) attempt to generate. A channel must be enabled for the specified current level to take effect.
- [niDCPower Configure Current Level Range VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-level-range-vi.html) Configures the current level range for the specified channel(s).
- [niDCPower Configure Voltage Limit VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-limit-vi.html) Configures the voltage limit for the specified channel(s). The channel must be enabled for the specified voltage limit to take effect.
- [niDCPower Configure Voltage Limit Range VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-limit-range-vi.html) Configures the voltage limit range for the specified channel(s).

Parent topic:

Source

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/dcvoltage-mnu.html language=enus -->
## TOPIC 00007: DC Voltage

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/dcvoltage-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/dcvoltage-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower DC Voltage VIs for changing channel settings when the channel is configured for the DC Voltage output function. icon

### DC Voltage

Use the NI-DCPower DC Voltage VIs for changing channel settings when the channel is configured for the DC Voltage output function.

[IMAGE alt='icon' src='dcvoltage-mnu.png']

- [niDCPower Configure Voltage Level VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-level-vi.html) Configures the voltage level the specified channel(s) attempt to generate. A channel must be enabled for the specified voltage level to take effect.
- [niDCPower Configure Voltage Level Range VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-level-range-vi.html) Configures the voltage level range for the specified channel(s).
- [niDCPower Configure Current Limit VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-limit-vi.html) Configures the current limit for the specified channel(s). The channel must be enabled for the specified current limit to take effect.
- [niDCPower Configure Current Limit Range VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-limit-range-vi.html) Configures the current limit range for the specified channel(s).
- [niDCPower Configure Output Resistance VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-resistance-vi.html) Configures the output resistance that the specified channel(s) attempt to generate. A channel must be enabled for the specified output resistance to take effect.

Parent topic:

Source

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/dir-mnu.html language=enus -->
## TOPIC 00008: NI-DCPower

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/dir-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use NI-DCPower VIs to create applications for your NI-DCPower instruments. icon

### NI-DCPower

Use NI-DCPower VIs to create applications for your NI-DCPower instruments.

[IMAGE alt='icon' src='dir-mnu.png']

- [niDCPower Initialize With Independent Channels VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-with-independent-channels-vi.html) Creates a new NI-DCPower session to the specified instrument(s) and channel(s) and returns a session handle to be used in all subsequent NI-DCPower VI calls.
- [niDCPower Close VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-close-vi.html) Closes the session specified in instrument handle and deallocates the resources that NI-DCPower reserved.
- [Source](../../instr-lib/nidcpower/source-mnu.html) Use the NI-DCPower Source VIs to configure the source unit.
- [Measure](../../instr-lib/nidcpower/measure-mnu.html) Use the NI-DCPower Measure VIs to configure the measure unit and acquire measurements.
- [Control](../../instr-lib/nidcpower/control-mnu.html) Use the NI-DCPower Control VIs to control the channel(s) in the session.
- [Triggers and Events](../../instr-lib/nidcpower/triggersevents-mnu.html) Use the NI-DCPower Triggers and Events VIs to configure triggers and events.
- [niDCPower Property Node VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-property-node-vi.html) Sets or gets properties of instruments or channels. For multi-channel sessions in which you want to configure subsets of channels differently, you must wire an Active Channel of an NI-DCPower property node. The Active Channel is listed first in the property node.
- [Query](../../instr-lib/nidcpower/query-mnu.html) Use the NI-DCPower Query VIs to query information about the capabilities and state of the device.
- [Calibration](../../instr-lib/nidcpower/calibration-mnu.html) Use the NI-DCPower Calibration VIs to perform a self calibration or an external calibration on the device.
- [Utility](../../instr-lib/nidcpower/utility-mnu.html) Use the NI-DCPower Utility VIs for miscellaneous functionality.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/externalcalibration-mnu.html language=enus -->
## TOPIC 00009: External Calibration

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/externalcalibration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/externalcalibration-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower External Calibration VIs to perform an external calibration of the device. Refer to the manual calibration procedure for your device for more information. icon

### External Calibration

Use the NI-DCPower External Calibration VIs to perform an external calibration of the device. Refer to the manual calibration procedure for your device for more information.

[IMAGE alt='icon' src='externalcalibration-mnu.png']

- [niDCPower Initialize External Calibration VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-external-calibration-vi.html) If password is valid, this VI creates a new IVI instrument driver session to the device specified in resource name and returns an instrument handle you use to identify the device in all subsequent NI-DCPower VI calls. This VI also sends initialization commands to set the device to the state necessary for the operation of NI-DCPower.
- [niDCPower Close External Calibration VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-close-external-calibration-vi.html) Closes the session specified in instrument handle and deallocates the resources that NI-DCPower reserved for calibration.
- [niDCPower Cal Adjust Voltage Level VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-voltage-level-vi.html) Calculates the calibration constants for the voltage level for the specified channel.
- [niDCPower Cal Adjust Voltage Measurement VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-voltage-measurement-vi.html) Calculates the calibration constants for the voltage measurements returned by the niDCPower Measure VI for the specified channel.
- [niDCPower Cal Adjust Current Limit VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-current-limit-vi.html) Calculates the calibration constants for the current limit for the specified channel and range.
- [niDCPower Cal Adjust Current Measurement VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-current-measurement-vi.html) Calibrates the current measurements returned by the niDCPower Measure VI for the specified channel.
- [niDCPower Cal Adjust Residual Voltage Offset VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-residual-voltage-offset-vi.html) Calculates the calibration constants for the residual voltage offsets for the specified channel. Residual offsets account for minor offset effects on the device that lie outside of the self-calibration circuitry. These offsets can include multiplexer input offsets and leakage effects from internal switching.
- [niDCPower Cal Adjust Residual Current Offset VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-residual-current-offset-vi.html) Calculates the calibration constants for the residual current offsets for the specified channel. Residual offsets account for minor offset effects on the device that lie outside of the self-calibration circuitry. These offsets can include multiplexer input offsets and leakage effects from internal switching.
- [niDCPower Connect Internal Reference VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-connect-internal-reference-vi.html) Connects the Internal Reference to the Calibration Pin / Measurement Channel in preparation for adjustment.
- [niDCPower Cal Adjust Internal Reference VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-internal-reference-vi.html) Programs the adjusted reference value to the device.
- [niDCPower Cal Adjust Output Resistance VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-output-resistance-vi.html) Compares the array in requested outputs to the array in measured outputs and calculates the calibration constants for the output resistance of the specified channel. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this VI. This VI can only be called from an external calibration session.
- [LCR External Calibration](../../instr-lib/nidcpower/lcrexternalcalibration-mnu.html) Use the NI-DCPower LCR External Calibration VIs to perform an LCR external calibration of the device. Refer to the manual calibration procedure for your device for more information.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/lcrcompensation-mnu.html language=enus -->
## TOPIC 00010: LCR Compensation

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/lcrcompensation-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/lcrcompensation-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower LCR Compensation VIs to perform custom cable compensation and LCR compensation for LCR measurements. icon

### LCR Compensation

Use the NI-DCPower LCR Compensation VIs to perform custom cable compensation and LCR compensation for LCR measurements.

[IMAGE alt='icon' src='lcrcompensation-mnu.png']

- [niDCPower Perform LCR Open Compensation VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-open-compensation-vi.html) Generates open compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify.
- [niDCPower Perform LCR Short Compensation VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-short-compensation-vi.html) Generates short compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify.
- [niDCPower Perform LCR Load Compensation VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-load-compensation-vi.html) Generates load compensation data for LCR measurements for the test spots you specify.
- [niDCPower Perform LCR Open Custom Cable Compensation VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-open-custom-cable-compensation-vi.html) Generates open custom cable compensation data for LCR measurements.
- [niDCPower Perform LCR Short Custom Cable Compensation VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-short-custom-cable-compensation-vi.html) Generates short custom cable compensation data for LCR measurements.
- [niDCPower Configure LCR Compensation VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-lcr-compensation-vi.html) Applies previously generated open, short, load, as well as open, short custom cable compensation data to LCR measurements.
- [niDCPower Get LCR Compensation Data VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-get-lcr-compensation-data-vi.html) Collects previously generated open, short, load compensation data as well as open and short custom cable compensation data so you can then apply it to LCR measurements with Configure LCR Compensation .
- [niDCPower Get LCR Compensation Last Date And Time VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-get-lcr-compensation-last-date-and-time-vi.html) Returns the date and time the specified type of compensation data for LCR measurements was most recently generated.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/lcrexternalcalibration-mnu.html language=enus -->
## TOPIC 00011: LCR External Calibration

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/lcrexternalcalibration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/lcrexternalcalibration-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower LCR External Calibration VIs to perform an LCR external calibration of the device. Refer to the manual calibration procedure for your device for more information. icon

### LCR External Calibration

Use the NI-DCPower LCR External Calibration VIs to perform an LCR external calibration of the device. Refer to the manual calibration procedure for your device for more information.

[IMAGE alt='icon' src='lcrexternalcalibration-mnu.png']

- [niDCPower Cal Begin AC Flatness VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-begin-ac-flatness-vi.html) Begins AC voltage flatness calibration.
- [niDCPower Cal End AC Flatness VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-end-ac-flatness-vi.html) Ends the AC voltage flatness calibration.
- [niDCPower Cal Config AC Flatness VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-config-ac-flatness-vi.html) Configures the device to output a voltage stimulus for AC voltage flatness calibration.
- [niDCPower Cal Adjust AC Flatness VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-ac-flatness-vi.html) Adjusts the AC voltage flatness calibration based on the frequency and voltage stimulus values generated by the niDCPower Cal Config AC Flatness VI and the voltage measured by an external oscilloscope.

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/measure-mnu.html language=enus -->
## TOPIC 00012: Measure

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/measure-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/measure-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower Measure VIs to configure the measure unit and acquire measurements. icon

### Measure

Use the NI-DCPower Measure VIs to configure the measure unit and acquire measurements.

[IMAGE alt='icon' src='measure-mnu.png']

- [niDCPower Configure Aperture Time VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-aperture-time-vi.html) Configures the aperture time on the specified channel(s).
- [niDCPower Configure Auto Zero VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-auto-zero-vi.html) Configures auto zero for the device.
- [niDCPower Configure Power Line Frequency VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-power-line-frequency-vi.html) Specifies the power line frequency for all channels in the session.
- [niDCPower Configure Sense VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-sense-vi.html) Specifies whether to use local or remote sensing of the output voltage on the specified channel(s).
- [niDCPower Measure VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-measure-vi.html) Returns the measured value of either the voltage or current on the specified channel.
- [niDCPower Measure Multiple VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-measure-multiple-vi.html) Returns arrays of the measured voltage and current values on the specified channel(s).
- [niDCPower Fetch Multiple VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-fetch-multiple-vi.html) Returns an array of voltage measurements, an array of current measurements, and an array of compliance measurements that were previously taken and are stored in the niDCPower buffer.
- [niDCPower Query In Compliance VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-query-in-compliance-vi.html) Queries the specified channel to determine if it is operating at the compliance limit.
- [niDCPower Query Output State VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-query-output-state-vi.html) Queries the specified channel to determine if the channel is currently in the state specified by output state .
- [niDCPower Measure Multiple LCR VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-measure-multiple-lcr-vi.html) Measures and returns an array of LCR data on the specified channel(s).
- [niDCPower Fetch Multiple LCR VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-fetch-multiple-lcr-vi.html) Returns an array of previously measured LCR data on the specified channel that have been taken and stored in a buffer.

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/measurementlink-mnu.html language=enus -->
## TOPIC 00013: MeasurementLink

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/measurementlink-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/measurementlink-mnu.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette in conjunction with MeasurementLink Session Management. icon

### MeasurementLink

Use the VIs on this palette in conjunction with MeasurementLink Session Management.

[IMAGE alt='icon' src='measurementlink-mnu.png']

- [niDCPower Initialize With Independent Channels for gRPC session VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-with-independent-channels-for-grpc-session-vi.html) Initializes a new NI-DCPower session on the specified NI gRPC Device Server and attaches to it. Returns a session handle to be used in all subsequent NI-DCPower VI calls.
- [niDCPower Attach gRPC session VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-attach-grpc-session-vi.html) Attaches to an existing NI-DCPower session with the specified session name on the specified NI gRPC Device Server. Returns a session handle to be used in all subsequent NI-DCPower VI calls.
- [niDCPower Detach gRPC session VI](../../instr-lib/nidcpower/nidcpower-llb/nidcpower-detach-grpc-session-vi.html) Closes the session specified in instrument handle but leaves the session open on the NI gRPC Device Server.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-abort-with-channels-vi.html language=enus -->
## TOPIC 00014: niDCPower Abort With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-abort-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-abort-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transitions the specified channel(s) from the Running state to the Uncommitted state. If a sequence is running, it is stopped. Any configuration VIs called after this VI are not applied until the niDCPower Initiate With Channels VI is called. If power output is enabled when you call this VI, the cha

### niDCPower Abort With Channels VI

Transitions the specified channel(s) from the Running state to the Uncommitted state. If a sequence is running, it is stopped.

Any configuration VIs called after this VI are not applied until the [niDCPower Initiate With Channels](nidcpower-initiate-with-channels-vi.html) VI is called.
 If power output is enabled when you call this VI, the channel(s) remain in their current state and continue providing power. Use the [niDCPower Configure Output Enabled](nidcpower-configure-output-enabled-vi.html) VI or the the [niDCPower Reset With Channels](nidcpower-reset-with-channels-vi.html) VI to disable power output on a per channel basis.

Note

**Related topics:**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

[IMAGE alt='icon' src='nidcpower-abort-with-channels-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this provides standard error in functionality. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out. The default is no error. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Control

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-attach-grpc-session-vi.html language=enus -->
## TOPIC 00015: niDCPower Attach gRPC session VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-attach-grpc-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-attach-grpc-session-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Attaches to an existing NI-DCPower session with the specified session name on the specified NI gRPC Device Server. Returns a session handle to be used in all subsequent NI-DCPower VI calls. If you do not specify a session name for the server, or if the specified session name did not previously exist

### niDCPower Attach gRPC session VI

Attaches to an existing NI-DCPower session with the specified session name on the specified NI gRPC Device Server. Returns a session handle to be used in all subsequent NI-DCPower VI calls.

Note

This VI creates a new session in LabVIEW that corresponds to the Session Name specified in the server. If a session with the specified name did not previously exist on the server, then NI-DCPower will return an error.

The resulting session in LabVIEW forwards driver calls to the corresponding session on the server.

[IMAGE alt='icon' src='nidcpower-attach-grpc-session-vi.png']

#### Inputs/Outputs

| gRPC options — gRPC options specifies the information used to connect to the server. session name — session name specifies the name of the MeasurementLink gRPC session. address (localhost) — address (localhost) specifies the address of the NI gRPC Device Server. port (31763) — port (31763) specifies the port that the NI gRPC Device Server monitors for connections. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| session name — session name specifies the name of the MeasurementLink gRPC session. address (localhost) — address (localhost) specifies the address of the NI gRPC Device Server. port (31763) — port (31763) specifies the port that the NI gRPC Device Server monitors for connections. |

Parent topic:

MeasurementLink

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-ac-flatness-vi.html language=enus -->
## TOPIC 00016: niDCPower Cal Adjust AC Flatness VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-ac-flatness-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-ac-flatness-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the AC voltage flatness calibration based on the frequency and voltage stimulus values generated by the niDCPower Cal Config AC Flatness VI and the voltage measured by an external oscilloscope. This VI returns the number of steps remaining in the calibration procedure. This VI is not support

### niDCPower Cal Adjust AC Flatness VI

Adjusts the AC voltage flatness calibration based on the frequency and voltage stimulus values generated by the [niDCPower Cal Config AC Flatness VI](/csh?context=nidcpower_nidcpowerviref_nidcpower_cal_config_ac_flatness) and the voltage measured by an external oscilloscope.

This VI returns the number of steps remaining in the calibration procedure.

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-cal-adjust-ac-flatness-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument calibration session. instrument handle is obtained from the niDCPower Initialize External Calibration VI. channel name — channel name specifies the channel to which these calibration settings apply. Only one channel at a time can be calibrated. generated frequency — generated frequency specifies the generated frequency, in Hz, utilized by the oscilloscope for the present AC flatness calibration step. generated voltage RMS — generated voltage RMS specifies the RMS voltage, in volts, utilitized by the oscilloscope for the present AC flatness calibration step. measured voltage RMS — measured voltage RMS specifies the RMS voltage, in volts, measured by the oscilloscope for the present AC flatness calibration step. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. number of steps remaining — number of steps remaining returns the remaining number of steps to complete the AC flatness calibration. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

LCR External Calibration

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-current-limit-vi.html language=enus -->
## TOPIC 00017: niDCPower Cal Adjust Current Limit VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-current-limit-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-current-limit-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates the calibration constants for the current limit for the specified channel and range. NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively. This VI is not supported by all devices. Ref

### niDCPower Cal Adjust Current Limit VI

Calculates the calibration constants for the current limit for the specified channel and range.

Note

Note

Supported VIs by Device

This VI compares the array in **requested outputs** to the array in **measured outputs** and calculates the calibration constants for the current limit returned by the device.

Refer to the calibration procedure for the device you are calibrating for
 detailed instructions on the appropriate use of this VI. This VI can only be called from an
 external calibration session.

[IMAGE alt='icon' src='nidcpower-cal-adjust-current-limit-vi.png']

#### Inputs/Outputs

| range — range specifies the range to calibrate with these settings. instrument handle — instrument handle identifies a particular instrument calibration session. instrument handle is obtained from the niDCPower Initialize External Calibration VI. channel name — channel name specifies the channel to which these calibration settings apply. Only one channel at a time can be calibrated. number of measurements — number of measurements specifies the number of elements in requested outputs and measured outputs. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. requested outputs — requested outputs specifies an array of the output values requested in the niDCPower Configure Current Limit VI. measured outputs — measured outputs specifies an array of the output values measured by an external precision digital multimeter. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-current-measurement-vi.html language=enus -->
## TOPIC 00018: niDCPower Cal Adjust Current Measurement VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-current-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-current-measurement-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calibrates the current measurements returned by the niDCPower Measure VI for the specified channel. This VI calculates new calibration coefficients for the specified current measurement range based on the reported outputs and measured outputs. Refer to the calibration procedure for the device you ar

### niDCPower Cal Adjust Current Measurement VI

Calibrates the current measurements returned by the [niDCPower Measure](/csh?topicname=nidcpower-measure-vi.html) VI for the specified channel.

This VI calculates new calibration coefficients for the specified current measurement range based on the **reported outputs** and **measured outputs**.

Refer to the calibration procedure for the device you are calibrating for
 detailed instructions on the appropriate use of this VI. This VI can only be called in an
 external calibration session.

Note

[IMAGE alt='icon' src='nidcpower-cal-adjust-current-measurement-vi.png']

#### Inputs/Outputs

| range — range specifies the range to calibrate with these settings. instrument handle — instrument handle identifies a particular instrument calibration session. instrument handle is obtained from the niDCPower Initialize External Calibration VI. channel name — channel name specifies the channel to which these calibration settings apply. Only one channel at a time can be calibrated. number of measurements — number of measurements specifies the number of elements in requested outputs and measured outputs. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. reported outputs — reported outputs specifies an array of the output values that were returned by the niDCPower Measure VI. measured outputs — measured outputs specifies an array of the output values measured by an external precision digital multimeter. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-internal-reference-vi.html language=enus -->
## TOPIC 00019: niDCPower Cal Adjust Internal Reference VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-internal-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-internal-reference-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Programs the adjusted reference value to the device. This VI is not supported by all devices. Refer to Supported VIs by Device for information about supported devices. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this VI. T

### niDCPower Cal Adjust Internal Reference VI

Programs the adjusted reference value to the device.

Note

Supported VIs by Device

Refer to the calibration procedure for the device you are calibrating for
 detailed instructions on the appropriate use of this VI. This VI can only be called from an
 external calibration session.

[IMAGE alt='icon' src='nidcpower-cal-adjust-internal-reference-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument calibration session. instrument handle is obtained from the niDCPower Initialize External Calibration VI. internal reference — internal reference specifies the internal reference to be adjusted. 5V Reference (1054) Calibration pin connected to 5 V internal reference. 100kOhm Reference (1055) Calibration pin connected to 100 kΩ internal reference. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. adjusted internal reference value — adjusted internal reference value specifies the updated value of the internal reference that will be programmed to the device. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 5V Reference (1054) | Calibration pin connected to 5 V internal reference. |
| 100kOhm Reference (1055) | Calibration pin connected to 100 kΩ internal reference. |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-output-resistance-vi.html language=enus -->
## TOPIC 00020: niDCPower Cal Adjust Output Resistance VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-output-resistance-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-output-resistance-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compares the array in requested outputs to the array in measured outputs and calculates the calibration constants for the output resistance of the specified channel. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this VI. Thi

### niDCPower Cal Adjust Output Resistance VI

Compares the array in **requested outputs** to the array in **measured outputs** and calculates the calibration constants for the output resistance of the specified channel. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this VI. This VI can only be called from an external calibration session.

Note

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-cal-adjust-output-resistance-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument calibration session. instrument handle is obtained from the niDCPower Initialize External Calibration VI. channel name — channel name specifies the channel to which these calibration settings apply. Only one channel at a time can be calibrated. number of measurements — number of measurements specifies the number of elements in requested outputs and measured outputs. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. requested outputs — requested outputs specifies an array of the output values requested in the niDCPower Configure Current Limit VI. measured outputs — measured outputs specifies an array of the output values measured by an external precision digital multimeter. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-residual-current-offset-vi.html language=enus -->
## TOPIC 00021: niDCPower Cal Adjust Residual Current Offset VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-residual-current-offset-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-cal-adjust-residual-current-offset-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates the calibration constants for the residual current offsets for the specified channel. Residual offsets account for minor offset effects on the device that lie outside of the self-calibration circuitry. These offsets can include multiplexer input offsets and leakage effects from internal s

### niDCPower Cal Adjust Residual Current Offset VI

Calculates the calibration constants for the residual current offsets for the specified channel. Residual offsets account for minor offset effects on the device that lie outside of the self-calibration circuitry. These offsets can include multiplexer input offsets and leakage effects from internal switching.

This VI requires that the output be open prior to it being invoked.

Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this VI. This VI can be called only in an external calibration session.

Note

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-cal-adjust-residual-current-offset-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument calibration session. instrument handle is obtained from the niDCPower Initialize External Calibration VI. channel name — channel name specifies the channel to which these calibration settings apply. Only one channel at a time can be calibrated. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-clear-interchange-warnings-vi.html language=enus -->
## TOPIC 00022: niDCPower Clear Interchange Warnings VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-clear-interchange-warnings-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-clear-interchange-warnings-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the list of current interchange warnings. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provides standard error

### niDCPower Clear Interchange Warnings VI

Clears the list of current interchange warnings.

[IMAGE alt='icon' src='nidcpower-clear-interchange-warnings-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Other IVI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-clear-latched-output-cutoff-state-vi.html language=enus -->
## TOPIC 00023: niDCPower Clear Latched Output Cutoff State VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-clear-latched-output-cutoff-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-clear-latched-output-cutoff-state-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the state of an output cutoff that was engaged. To clear the state for all output cutoff reasons, use All. NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively. This VI is not supported b

### niDCPower Clear Latched Output Cutoff State VI

Clears the state of an output cutoff that was engaged.

To clear the state for all output cutoff reasons, use **All**.

Note

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-clear-latched-output-cutoff-state-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. reason — reason specifies the reasons for which to clear the output cutoff state. All (-1) Clears all output cutoff conditions. Voltage Output High (1) Clears cutoffs caused when the output exceeded the high cutoff limit for voltage output. Voltage Output Low (2) Clears cutoffs caused when the output fell below the low cutoff limit for voltage output. Current Measure High (4) Clears cutoffs caused when the measured current exceeded the high cutoff limit for current output. Current Measure Low (8) Clears cutoffs caused when the measured current fell below the low cutoff limit for current output. Voltage Change High (16) Clears cutoffs caused when the voltage slew rate increased beyond the positive change cutoff for voltage output. Voltage Change Low (32) Clears cutoffs caused when the voltage slew rate decreased beyond the negative change cutoff for voltage output. Current Change High (64) Clears cutoffs caused when the current slew rate increased beyond the positive change cutoff for current output. Current Change Low (128) Clears cutoffs caused when the voltage slew rate decreased beyond the negative change cutoff for current output. Current Saturated (512) The measured current saturates the current range. Voltage Measure High (1024) The measured voltage exceeded the high cutoff limit for voltage output. Voltage Measure Low (2048) The measured voltage fell below the low cutoff limit for voltage output. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| All (-1) | Clears all output cutoff conditions. |
| Voltage Output High (1) | Clears cutoffs caused when the output exceeded the high cutoff limit for voltage output. |
| Voltage Output Low (2) | Clears cutoffs caused when the output fell below the low cutoff limit for voltage output. |
| Current Measure High (4) | Clears cutoffs caused when the measured current exceeded the high cutoff limit for current output. |
| Current Measure Low (8) | Clears cutoffs caused when the measured current fell below the low cutoff limit for current output. |
| Voltage Change High (16) | Clears cutoffs caused when the voltage slew rate increased beyond the positive change cutoff for voltage output. |
| Voltage Change Low (32) | Clears cutoffs caused when the voltage slew rate decreased beyond the negative change cutoff for voltage output. |
| Current Change High (64) | Clears cutoffs caused when the current slew rate increased beyond the positive change cutoff for current output. |
| Current Change Low (128) | Clears cutoffs caused when the voltage slew rate decreased beyond the negative change cutoff for current output. |
| Current Saturated (512) | The measured current saturates the current range. |
| Voltage Measure High (1024) | The measured voltage exceeded the high cutoff limit for voltage output. |
| Voltage Measure Low (2048) | The measured voltage fell below the low cutoff limit for voltage output. |

Parent topic:

Query

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-close-external-calibration-vi.html language=enus -->
## TOPIC 00024: niDCPower Close External Calibration VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-close-external-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-close-external-calibration-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session specified in instrument handle and deallocates the resources that NI-DCPower reserved for calibration. Refer to the calibration procedure for the device you are calibrating for detailed instructions on the appropriate use of this VI. If an error occurs before this VI, calibration

### niDCPower Close External Calibration VI

Closes the session specified in **instrument handle** and
 deallocates the resources that NI-DCPower reserved for calibration.

Refer to the calibration procedure for the device you
 are calibrating for detailed instructions on the appropriate use of this VI. If an error occurs before this VI, **calibration close action**
 defaults to **Cancel**.

[IMAGE alt='icon' src='nidcpower-close-external-calibration-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument calibration session. instrument handle is obtained from the niDCPower Initialize External Calibration VI. calibration close action — calibration close action specifies how to use the calibration values from this session as the session is closed. The default value is Cancel. Cancel (1001) The old calibration constants are kept, and the new ones are discarded. Commit (1002) The new calibration constants are stored in the EEPROM. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Cancel (1001) | The old calibration constants are kept, and the new ones are discarded. |
| Commit (1002) | The new calibration constants are stored in the EEPROM. |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-close-vi.html language=enus -->
## TOPIC 00025: niDCPower Close VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-close-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-close-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session specified in instrument handle and deallocates the resources that NI-DCPower reserved. If power output is enabled when you call this VI, the channels remain in their existing state and continue providing power. Use the niDCPower Configure Output Enabled VI or niDCPower Reset With

### niDCPower Close VI

Closes the session specified in **instrument handle** and
 deallocates the resources that NI-DCPower reserved.

If power output is enabled when you call this
 VI, the channels remain in their existing state and continue providing power. Use the [niDCPower Configure Output Enabled](nidcpower-configure-output-enabled-vi.html) VI or [niDCPower Reset With Channels](nidcpower-reset-with-channels-vi.html) VI to disable power output on a per
 channel basis.

Note

**Related topics:**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

[IMAGE alt='icon' src='nidcpower-close-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this provides standard error in functionality. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out. The default is no error. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-commit-with-channels-vi.html language=enus -->
## TOPIC 00026: niDCPower Commit With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-commit-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-commit-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies previously configured settings to the specified channel(s). Calling this VI moves the channel(s) from the Uncommitted state into the Committed state. After calling this VI, modifying any property reverts the channel(s) to the Uncommitted state. Use the niDCPower Initiate With Channels VI to

### niDCPower Commit With Channels VI

Applies previously configured settings to the specified channel(s). Calling this VI moves the channel(s) from the Uncommitted state into the Committed state.

After calling this VI, modifying any property reverts the channel(s) to the Uncommitted state. Use the [niDCPower Initiate With Channels](nidcpower-initiate-with-channels-vi.html) VI to transition to the Running state.

**Related topics:**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

[IMAGE alt='icon' src='nidcpower-commit-with-channels-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Control

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-aperture-time-vi.html language=enus -->
## TOPIC 00027: niDCPower Configure Aperture Time VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-aperture-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-aperture-time-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the aperture time on the specified channel(s). This VI is not supported by all devices. Refer to Supported VIs by Device for information about supported devices. The supported values depend on both the aperture time units and the specific device. Refer to the Aperture Time topic for your

### niDCPower Configure Aperture Time VI

Configures the aperture time on the specified channel(s).

Note

Supported VIs by Device

The supported values depend on both the **aperture time units** and the specific device. Refer to the *Aperture Time* topic for your device in the *NI DC Power Supplies and SMUs Help* for more information. In general, devices support discrete **aperture time** values. If you configure **aperture time** to some unsupported value, NI-DCPower coerces it up to the next supported value.

Refer to the *Measurement Configuration and Timing* or *DC Noise Rejection* topic for your device in the *NI DC Power Supplies and SMUs Help* for more information about how to configure your measurements.

[IMAGE alt='icon' src='nidcpower-configure-aperture-time-vi.png']

#### Inputs/Outputs

| aperture time units — aperture time units specifies the aperture time units. Seconds (1028) Specifies the aperture time in units of seconds. Power Line Cycles (1029) Specifies the aperture time in power line cycles. instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. aperture time — aperture time specifies the aperture time. Refer to the Aperture Time topic for your device in the NI DC Power Supplies and SMUs Help for more information. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Seconds (1028) | Specifies the aperture time in units of seconds. |
| Power Line Cycles (1029) | Specifies the aperture time in power line cycles. |

Parent topic:

Measure

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-auto-zero-vi.html language=enus -->
## TOPIC 00028: niDCPower Configure Auto Zero VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-auto-zero-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-auto-zero-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures auto zero for the device. This VI is not supported by all devices. Refer to Supported VIs by Device for information about supported devices. Refer to the Auto Zero and Measurement Configuration and Timing topics for the NI PXI-4132 in the NI DC Power Supplies and SMUs Help for more inform

### niDCPower Configure Auto Zero VI

Configures auto zero for the device.

Note

Supported VIs by Device

Refer to the *Auto Zero* and *Measurement Configuration and Timing* topics for the NI PXI-4132 in the *NI DC Power Supplies and SMUs Help* for more information about how to configure your measurements.

[IMAGE alt='icon' src='nidcpower-configure-auto-zero-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. auto zero — auto zero specifies the auto-zero setting. Refer to the Measurement Configuration and Timing topic and the Auto Zero topic for your device for more information about how to configure your measurements. Off (0) Disables auto-zero. Once (1024) Makes zero conversions following the first measurement after initiating the channel(s). Channels use these zero conversions for the preceding measurement and future measurements until they are reinitiated. On (1) Makes zero conversions for every measurement. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Off (0) | Disables auto-zero. |
| Once (1024) | Makes zero conversions following the first measurement after initiating the channel(s). Channels use these zero conversions for the preceding measurement and future measurements until they are reinitiated. |
| On (1) | Makes zero conversions for every measurement. |

Parent topic:

Measure

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-level-range-vi.html language=enus -->
## TOPIC 00029: niDCPower Configure Current Level Range VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-level-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-level-range-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the current level range for the specified channel(s). The configured range defines the valid values that the current level can be set to using the niDCPower Configure Current Level VI. The current level range setting is applicable only if the channel is set to the DC Current output functi

### niDCPower Configure Current Level Range VI

Configures the current level range for the specified channel(s).

The configured range defines the valid values that the current level can be set to using the [niDCPower Configure Current Level](nidcpower-configure-current-level-vi.html) VI. The current level range setting is applicable only if the channel is set to the **DC Current** output function using the [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Use the [Current Level Autorange](/csh?context=nidcpower_dcpowerpropref_pnidcpower_currentlevelautorange) property to enable automatic selection of the current level range.

[IMAGE alt='icon' src='nidcpower-configure-current-level-range-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. current level range — current level range specifies the current level range, in amps, for the specified channel(s). For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DC Current

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-level-vi.html language=enus -->
## TOPIC 00030: niDCPower Configure Current Level VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-level-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the current level that the specified channel(s) attempt to generate. A channel must be enabled for the specified current level to take effect. Refer to the niDCPower Configure Output Enabled VI for more information about enabling the channel. The current level setting is applicable only i

### niDCPower Configure Current Level VI

Configures the current level that the specified channel(s) attempt to generate. A channel must be enabled for the specified current level to take effect.

Refer to the [niDCPower Configure Output Enabled](nidcpower-configure-output-enabled-vi.html) VI for more information about enabling the channel. The current level setting is applicable only if the channel is set to the **DC Current** output function using the [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Channels actively regulate the current at the specified level unless doing so causes a voltage greater than the [voltage limit](nidcpower-configure-voltage-limit-vi.html) across the channels' output terminals.

Note

[IMAGE alt='icon' src='nidcpower-configure-current-level-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. current level — current level specifies the current level, in amps, to generate for the specified channel(s). The valid values for this parameter are defined by the current level range that is selected using the niDCPower Configure Current Level Range VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DC Current

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-limit-range-vi.html language=enus -->
## TOPIC 00031: niDCPower Configure Current Limit Range VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-limit-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-limit-range-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the current limit range for the specified channel(s). The configured range defines the valid values that the current limit can be set to using the niDCPower Configure Current Limit VI. The current limit range setting is applicable only if the channel is set to the DC Voltage output functi

### niDCPower Configure Current Limit Range VI

Configures the current limit range for the specified channel(s).

The configured range defines the valid values that the current limit can be set to using the [niDCPower Configure Current Limit](nidcpower-configure-current-limit-vi.html) VI. The current limit range setting is applicable only if the channel is set to the **DC Voltage** output function using the [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Use the [Current Limit Autorange](/csh?context=nidcpower_dcpowerpropref_pnidcpower_currentlimitautorange) property to enable automatic selection of the current limit range.

[IMAGE alt='icon' src='nidcpower-configure-current-limit-range-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. current limit range — current limit range specifies the current limit range, in amps, for the specified channel(s). For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-limit-vi.html language=enus -->
## TOPIC 00032: niDCPower Configure Current Limit VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-limit-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-current-limit-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the current limit for the specified channel(s). The channel must be enabled for the specified current limit to take effect. Refer to the niDCPower Configure Output Enabled VI for more information about enabling the channel. The current limit is the current that the output should not excee

### niDCPower Configure Current Limit VI

Configures the current limit for the specified channel(s). The channel must be enabled for
 the specified current limit to take effect.

Refer to the [niDCPower Configure Output Enabled](nidcpower-configure-output-enabled-vi.html) VI for more information about enabling the channel. The current limit is the current that the output should not exceed when generating the desired [voltage level](nidcpower-configure-voltage-level-vi.html). The current limit setting is only applicable if the channel is set to the **DC Voltage** output function using the [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Note

[IMAGE alt='icon' src='nidcpower-configure-current-limit-vi.png']

#### Inputs/Outputs

| behavior — behavior specifies how the output current should behave when the current limit is reached. Regulate The channel controls the output current so that it does not exceed the current limit. The channel continues to generate power, even if the current limit has been reached. instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. current limit — current limit specifies the current limit on the specified channel(s). The limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. The valid values for this parameter are defined by the current limit range that is configured using the niDCPower Configure Current Limit Range VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Regulate | The channel controls the output current so that it does not exceed the current limit. The channel continues to generate power, even if the current limit has been reached. |

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-measure-trigger-with-channels-vi.html language=enus -->
## TOPIC 00033: niDCPower Configure Digital Edge Measure Trigger With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-measure-trigger-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-measure-trigger-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Measure trigger for digital edge triggering. icon Inputs/Outputs ci32.png edge (rising) edge (rising) specifies whether to configure the Measure trigger to assert on the rising or falling edge. Rising Edge (1016) Asserts the trigger on the rising edge of the digital signal. Falling Ed

### niDCPower Configure Digital Edge Measure Trigger With Channels VI

Configures the Measure trigger for digital edge triggering.

[IMAGE alt='icon' src='nidcpower-configure-digital-edge-measure-trigger-with-channels-vi.png']

#### Inputs/Outputs

| edge (rising) — edge (rising) specifies whether to configure the Measure trigger to assert on the rising or falling edge. Rising Edge (1016) Asserts the trigger on the rising edge of the digital signal. Falling Edge (1017) Asserts the trigger on the falling edge of the digital signal. instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. input terminal — input terminal specifies the input terminal for the digital edge Measure trigger. You can specify any valid input terminal for this VI. Valid terminals are listed in MAX under the Device Routes tab. For the PXIe-4147 and PXIe-4162/4163, refer to the Signal Routing topic for the device to determine which routes are available. This information is not available on a Device Routes tab in MAX. Specify the input terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal. The input terminal can also be a terminal from another instrument or channel. For example, you can set the input terminal on Dev1 to be /Dev2/Engine0/SourceCompleteEvent, where Engine0 is channel 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Rising Edge (1016) | Asserts the trigger on the rising edge of the digital signal. |
| Falling Edge (1017) | Asserts the trigger on the falling edge of the digital signal. |

Parent topic:

niDCPower Configure Trigger With Channels (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-pulse-trigger-with-channels-vi.html language=enus -->
## TOPIC 00034: niDCPower Configure Digital Edge Pulse Trigger With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-pulse-trigger-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-pulse-trigger-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Pulse trigger for digital edge triggering. icon Inputs/Outputs ci32.png edge (rising) edge (rising) specifies whether to configure the Pulse trigger to assert on the rising or falling edge. Rising Edge (1016) Asserts the trigger on the rising edge of the digital signal. Falling Edge (

### niDCPower Configure Digital Edge Pulse Trigger With Channels VI

Configures the Pulse trigger for digital edge triggering.

[IMAGE alt='icon' src='nidcpower-configure-digital-edge-pulse-trigger-with-channels-vi.png']

#### Inputs/Outputs

| edge (rising) — edge (rising) specifies whether to configure the Pulse trigger to assert on the rising or falling edge. Rising Edge (1016) Asserts the trigger on the rising edge of the digital signal. Falling Edge (1017) Asserts the trigger on the falling edge of the digital signal. instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. input terminal — input terminal specifies the input terminal for the digital edge Pulse trigger. You can specify any valid input terminal for this VI. Valid terminals are listed in MAX under the Device Routes tab. Specify the input terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal. The input terminal can also be a terminal from another instrument or channel. For example, you can set the input terminal on Dev1 to be /Dev2/Engine0/SourceCompleteEvent, where Engine0 is channel 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Rising Edge (1016) | Asserts the trigger on the rising edge of the digital signal. |
| Falling Edge (1017) | Asserts the trigger on the falling edge of the digital signal. |

Parent topic:

niDCPower Configure Trigger With Channels (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-sequence-advance-trigger-with-channels-vi.html language=enus -->
## TOPIC 00035: niDCPower Configure Digital Edge Sequence Advance Trigger With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-sequence-advance-trigger-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-sequence-advance-trigger-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Sequence Advance trigger for digital edge triggering. icon Inputs/Outputs ci32.png edge (rising) edge (rising) specifies whether to configure the Sequence Advance trigger to assert on the rising or falling edge. Rising Edge (1016) Asserts the trigger on the rising edge of the digital

### niDCPower Configure Digital Edge Sequence Advance Trigger With Channels VI

Configures the Sequence Advance trigger for digital edge triggering.

[IMAGE alt='icon' src='nidcpower-configure-digital-edge-sequence-advance-trigger-with-channels-vi.png']

#### Inputs/Outputs

| edge (rising) — edge (rising) specifies whether to configure the Sequence Advance trigger to assert on the rising or falling edge. Rising Edge (1016) Asserts the trigger on the rising edge of the digital signal. Falling Edge (1017) Asserts the trigger on the falling edge of the digital signal. instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. input terminal — input terminal specifies the input terminal for the digital edge Sequence Advance trigger. You can specify any valid input terminal for this VI. Valid terminals are listed in MAX under the Device Routes tab. For the PXIe-4147 and PXIe-4162/4163, refer to the Signal Routing topic for the device to determine which routes are available. This information is not available on a Device Routes tab in MAX. Specify the input terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal. The input terminal can also be a terminal from another instrument or channel. For example, you can set the input terminal on Dev1 to be /Dev2/Engine0/SourceCompleteEvent, where Engine0 is channel 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Rising Edge (1016) | Asserts the trigger on the rising edge of the digital signal. |
| Falling Edge (1017) | Asserts the trigger on the falling edge of the digital signal. |

Parent topic:

niDCPower Configure Trigger With Channels (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-shutdown-trigger-with-channels-vi.html language=enus -->
## TOPIC 00036: niDCPower Configure Digital Edge Shutdown Trigger With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-shutdown-trigger-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-shutdown-trigger-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Shutdown trigger for digital edge triggering. icon Inputs/Outputs ci32.png edge (rising) edge (rising) specifies whether to configure the Shutdown trigger to assert on the rising or falling edge. Rising Edge (1016) Asserts the trigger on the rising edge of the digital signal. Falling

### niDCPower Configure Digital Edge Shutdown Trigger With Channels VI

Configures the Shutdown trigger for digital edge triggering.

[IMAGE alt='icon' src='nidcpower-configure-digital-edge-shutdown-trigger-with-channels-vi.png']

#### Inputs/Outputs

| edge (rising) — edge (rising) specifies whether to configure the Shutdown trigger to assert on the rising or falling edge. Rising Edge (1016) Asserts the trigger on the rising edge of the digital signal. Falling Edge (1017) Asserts the trigger on the falling edge of the digital signal. instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. input terminal — input terminal specifies the input terminal for the digital edge Shutdown trigger. You can specify any valid input terminal for this VI. Valid terminals are listed in MAX under the Device Routes tab. For the PXIe-4138/4139, refer to the Signal Routing topic for the device to determine which routes are available. This information is not available on a Device Routes tab in MAX. Specify the input terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal. The input terminal can also be a terminal from another instrument or channel. For example, you can set the input terminal on Dev1 to be /Dev2/Engine0/SourceCompleteEvent, where Engine0 is channel 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Rising Edge (1016) | Asserts the trigger on the rising edge of the digital signal. |
| Falling Edge (1017) | Asserts the trigger on the falling edge of the digital signal. |

Parent topic:

niDCPower Configure Trigger With Channels (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-source-trigger-with-channels-vi.html language=enus -->
## TOPIC 00037: niDCPower Configure Digital Edge Source Trigger With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-source-trigger-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-source-trigger-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Source trigger for digital edge triggering. NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively. icon Inputs/Outputs ci32.png edge (rising) edge (rising) specifies whether to con

### niDCPower Configure Digital Edge Source Trigger With Channels VI

Configures the Source trigger for digital edge triggering.

Note

[IMAGE alt='icon' src='nidcpower-configure-digital-edge-source-trigger-with-channels-vi.png']

#### Inputs/Outputs

| edge (rising) — edge (rising) specifies whether to configure the Source trigger to assert on the rising or falling edge. Rising Edge (1016) Asserts the trigger on the rising edge of the digital signal. Falling Edge (1017) Asserts the trigger on the falling edge of the digital signal. instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. input terminal — input terminal specifies the input terminal for the digital edge Source trigger. You can specify any valid input terminal for this VI. Valid terminals are listed in MAX under the Device Routes tab. For the PXIe-4147 and PXIe-4162/4163, refer to the Signal Routing topic for the device to determine which routes are available. This information is not available on a Device Routes tab in MAX. Specify the input terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal. The input terminal can also be a terminal from another instrument or channel. For example, you can set the input terminal on Dev1 to be /Dev2/Engine0/SourceCompleteEvent, where Engine0 is channel 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Rising Edge (1016) | Asserts the trigger on the rising edge of the digital signal. |
| Falling Edge (1017) | Asserts the trigger on the falling edge of the digital signal. |

Parent topic:

niDCPower Configure Trigger With Channels (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-start-trigger-with-channels-vi.html language=enus -->
## TOPIC 00038: niDCPower Configure Digital Edge Start Trigger With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-start-trigger-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-digital-edge-start-trigger-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start trigger for digital edge triggering. icon Inputs/Outputs ci32.png edge (rising) edge (rising) specifies whether to configure the Start trigger to assert on the rising or falling edge. Rising Edge (1016) Asserts the trigger on the rising edge of the digital signal. Falling Edge (

### niDCPower Configure Digital Edge Start Trigger With Channels VI

Configures the Start trigger for digital edge triggering.

[IMAGE alt='icon' src='nidcpower-configure-digital-edge-start-trigger-with-channels-vi.png']

#### Inputs/Outputs

| edge (rising) — edge (rising) specifies whether to configure the Start trigger to assert on the rising or falling edge. Rising Edge (1016) Asserts the trigger on the rising edge of the digital signal. Falling Edge (1017) Asserts the trigger on the falling edge of the digital signal. instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. input terminal — input terminal specifies the input terminal for the digital edge Start trigger. You can specify any valid input terminal for this VI. Valid terminals are listed in MAX under the Device Routes tab. For the PXIe-4147 and PXIe-4162/4163, refer to the Signal Routing topic for the device to determine which routes are available. This information is not available on a Device Routes tab in MAX. Specify the input terminal using the form /Dev1/PXI_Trig0, where Dev1 is the instrument and PXI_Trig0 is the terminal. The input terminal can also be a terminal from another instrument or channel. For example, you can set the input terminal on Dev1 to be /Dev2/Engine0/SourceCompleteEvent, where Engine0 is channel 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Rising Edge (1016) | Asserts the trigger on the rising edge of the digital signal. |
| Falling Edge (1017) | Asserts the trigger on the falling edge of the digital signal. |

Parent topic:

niDCPower Configure Trigger With Channels (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-lcr-compensation-vi.html language=enus -->
## TOPIC 00039: niDCPower Configure LCR Compensation VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-lcr-compensation-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-lcr-compensation-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies previously generated open, short, load, as well as open, short custom cable compensation data to LCR measurements. This VI applies open, short, load compensation data when you have set LCR Open/Short/Load Compensation Data Source to As Configured, and it also applies custom cable compensatio

### niDCPower Configure LCR Compensation VI

Applies previously generated open, short, load, as well as open, short custom cable compensation data to LCR measurements.

This VI applies open, short, load compensation data when you have set [LCR Open/Short/Load Compensation Data Source](/csh?context=nidcpower_dcpowerpropref_pnidcpower_lcropenshortloadcompensationdatasource) to **As Configured**, and it also applies custom cable compensation data when you have set [Cable Length](/csh?context=nidcpower_dcpowerpropref_pnidcpower_cablelength) to **Custom (As Configured)**.

Call this VI after you have obtained LCR compensation data. If [LCR Short Custom Cable Compensation Enabled](/csh?context=nidcpower_dcpowerpropref_pnidcpower_lcrshortcustomcablecompensationenabled) is set to TRUE, you must generate data with both [niDCPower Perform LCR Open Custom Cable Compensation](nidcpower-perform-lcr-open-custom-cable-compensation-vi.html) and [niDCPower Perform LCR Short Custom Cable Compensation](nidcpower-perform-lcr-short-custom-cable-compensation-vi.html); if FALSE, you must only use [niDCPower Perform LCR Open Custom Cable Compensation](nidcpower-perform-lcr-open-custom-cable-compensation-vi.html), and NI-DCPower uses default short data.

Call [niDCPower Get LCR Compensation Data](nidcpower-get-lcr-compensation-data-vi.html) and pass the **compensation data** to this VI.

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-configure-lcr-compensation-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. compensation data — compensation data specifies the open, short, load, open custom cable, and short custom cable compensation data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

LCR Compensation

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-lcr-custom-cable-compensation-vi.html language=enus -->
## TOPIC 00040: niDCPower Configure LCR Custom Cable Compensation VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-lcr-custom-cable-compensation-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-lcr-custom-cable-compensation-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI is deprecated, use niDCPower Configure LCR Compensation instead. Applies previously generated open and short custom cable compensation data to LCR measurements. This VI applies custom cable compensation data when you have set Cable Length to Custom (As Configured). Call this VI after you hav

### niDCPower Configure LCR Custom Cable Compensation VI

This VI is deprecated, use [niDCPower Configure LCR Compensation](/csh?topicname=nidcpower-configure-lcr-compensation-vi.html) instead.

Applies previously generated open and short custom cable compensation data to LCR measurements.

This VI applies custom cable compensation data when you have set [Cable Length](/csh?context=nidcpower_dcpowerpropref_pnidcpower_cablelength) to **Custom (As Configured)**.

Call this VI after you have obtained custom cable compensation data. If [LCR Short Custom Cable Compensation Enabled](/csh?context=nidcpower_dcpowerpropref_pnidcpower_lcrshortcustomcablecompensationenabled) is set to TRUE, you must generate data with both [niDCPower Perform LCR Open Custom Cable Compensation](nidcpower-perform-lcr-open-custom-cable-compensation-vi.html) and [niDCPower Perform LCR Short Custom Cable Compensation](nidcpower-perform-lcr-short-custom-cable-compensation-vi.html); if FALSE, you must only use [niDCPower Perform LCR Open Custom Cable Compensation](nidcpower-perform-lcr-open-custom-cable-compensation-vi.html), and NI-DCPower uses default short data.

Call [niDCPower Get LCR Custom Cable Compensation Data](nidcpower-get-lcr-custom-cable-compensation-data-vi.html) and pass the **custom cable compensation data** to this VI.

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-configure-lcr-custom-cable-compensation-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. custom cable compensation data — custom cable compensation data is the open and short custom cable compensation data to apply. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-enabled-vi.html language=enus -->
## TOPIC 00041: niDCPower Configure Output Enabled VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-enabled-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-enabled-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables generation on the specified channel(s). Depending on the selected output function, the corresponding level properties or Output Resistance must be set in addition to enabling the output to generate the desired level. For more information about configuring the output level, refer

### niDCPower Configure Output Enabled VI

Enables or disables generation on the specified channel(s).

Depending on the selected output function, the corresponding level properties or
 [Output Resistance](/csh?context=nidcpower_dcpowerpropref_pnidcpower_outputresistance)
 must be set in addition to enabling the output to generate the desired level.
 For more information about configuring the output level, refer to the
 [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Note

Uncommitted

niDCPower Initiate With Channels

Note

[IMAGE alt='icon' src='nidcpower-configure-output-enabled-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. output enabled — output enabled specifies whether the channels are enabled or disabled. true Enables generation on the specified channel(s). false Disables generation on the specified channel(s). This parameter has no effect on the output disconnect relay. To toggle the relay, use the Output Connected property. The default value is true if you use the niDCPower Initialize With Independent Channels VI to open the session. Otherwise the default value is false, including when you use a calibration session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| true | Enables generation on the specified channel(s). |
| false | Disables generation on the specified channel(s). This parameter has no effect on the output disconnect relay. To toggle the relay, use the Output Connected property. |

Parent topic:

Source

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-function-vi.html language=enus -->
## TOPIC 00042: niDCPower Configure Output Function VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-function-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-function-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the function that the specified channels attempt to generate. NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively. icon Inputs/Outputs civrn.png instrument handle instrument handle i

### niDCPower Configure Output Function VI

Configures the function that the specified channels attempt to generate.

Note

[IMAGE alt='icon' src='nidcpower-configure-output-function-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. output function — output function configures the function to generate for the specified channel(s). The default value is DC Voltage (1006). DC Voltage (1006) Sets the output function to DC voltage. DC Current (1007) Sets the output function to DC current. Pulse Voltage (1049) Sets the output function to pulse voltage. Pulse Current (1050) Sets the output function to pulse current. Constant Resistance (1161) Sets the output function to constant resistance. Constant Power (1162) Sets the output function to constant power. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| DC Voltage (1006) | Sets the output function to DC voltage. |
| DC Current (1007) | Sets the output function to DC current. |
| Pulse Voltage (1049) | Sets the output function to pulse voltage. |
| Pulse Current (1050) | Sets the output function to pulse current. |
| Constant Resistance (1161) | Sets the output function to constant resistance. |
| Constant Power (1162) | Sets the output function to constant power. |

#### Details

When **DC Voltage** is selected, a channel generates the desired voltage level on the output as long as the output current is below the current limit. The following VIs can be used to configure the channel when **DC Voltage** is selected:

- niDCPower Configure Voltage Level
- niDCPower Configure Current Limit
- niDCPower Configure Voltage Level Range
- niDCPower Configure Current Limit Range

When **DC Current** is selected, a channel generates the desired current level on the output as long as the output voltage is below the voltage limit. The following VIs can be used to configure the channel when **DC Current** is selected:

- niDCPower Configure Current Level
- niDCPower Configure Voltage Limit
- niDCPower Configure Current Level Range
- niDCPower Configure Voltage Limit Range

When **Pulse Voltage** is selected, a channel generates pulses at the desired pulse voltage levels on the output as long as the output current is below the pulse current limit. The following VIs can be used to configure the channel when **Pulse Voltage** is selected:

- niDCPower Configure Pulse Voltage Level
- niDCPower Configure Pulse Bias Voltage Level
- niDCPower Configure Pulse Current Limit
- niDCPower Configure Pulse Bias Current Limit
- niDCPower Configure Pulse Voltage Level Range
- niDCPower Configure Pulse Current Limit Range

When **Pulse Current** is selected, a channel generates pulses at the desired pulse current levels on the output as long as the output voltage is below the pulse voltage limit. The following VIs can be used to configure the channel when **Pulse Current** is selected:

- niDCPower Configure Pulse Current Level
- niDCPower Configure Pulse Bias Current Level
- niDCPower Configure Pulse Voltage Limit
- niDCPower Configure Pulse Bias Voltage Limit
- niDCPower Configure Pulse Current Level Range
- niDCPower Configure Pulse Voltage Limit Range

When **Constant Resistance** is selected, a channel generates the desired resistance level on the output as long as the output current is below the current limit. The following properties can be used to configure the channel when **Constant Resistance** is selected:

- Constant Resistance Level
- Constant Resistance Current Limit
- Constant Resistance Level Range

When **Constant Power** is selected, a channel generates the desired power level on the output as long as the output current is below the current limit. The following properties can be used to configure the channel when **Constant Power** is selected:

- Constant Power Level
- Constant Power Current Limit
- Constant Power Level Range

Parent topic:

Source

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-range-vi.html language=enus -->
## TOPIC 00043: niDCPower Configure Output Range VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-range-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI is deprecated. Use the following VIs instead: - niDCPower Configure Voltage Level Range - niDCPower Configure Current Limit Range - niDCPower Configure Current Level Range - niDCPower Configure Voltage Limit Range Configures either the voltage level range or the current limit range. If range

### niDCPower Configure Output Range VI

This VI is deprecated. Use the following VIs instead:

- [niDCPower Configure Voltage Level Range](nidcpower-configure-voltage-level-range-vi.html)

- [niDCPower Configure Current Limit Range](nidcpower-configure-current-limit-range-vi.html)

- [niDCPower Configure Current Level Range](nidcpower-configure-current-level-range-vi.html)

- [niDCPower Configure Voltage Limit Range](nidcpower-configure-voltage-limit-range-vi.html)

Configures either the voltage level range or the current limit range. If **range type** is Voltage, the voltage level range is configured. If **range type** is Current, the current limit range is configured.

This VI does not configure any of the DC Current output function settings. Refer to the [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI for more information.

[IMAGE alt='icon' src='nidcpower-configure-output-range-vi.png']

#### Inputs/Outputs

| range type — range type specifies the type of the range: voltage or current. Voltage NI-DCPower configures the voltage range. Current NI-DCPower configures the current range. instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. range — range specifies the requested range. Refer to the NI DC Power Supplies and SMUs Help for the valid output ranges for your device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Voltage | NI-DCPower configures the voltage range. |
| Current | NI-DCPower configures the current range. |

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-resistance-vi.html language=enus -->
## TOPIC 00044: niDCPower Configure Output Resistance VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-resistance-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-output-resistance-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the output resistance that the specified channel(s) attempt to generate. A channel must be enabled for the specified output resistance to take effect. Refer to the niDCPower Configure Output Enabled VI for more information about enabling the channel. Channels actively regulate the current

### niDCPower Configure Output Resistance VI

Configures the output resistance that the specified channel(s) attempt to generate. A channel must be enabled for the specified output resistance to take effect.

Refer to the [niDCPower Configure Output Enabled](nidcpower-configure-output-enabled-vi.html) VI for more information about enabling the channel.

Channels actively regulate the current and voltage to reach the specified output resistance, although in DC Voltage output mode, the voltage at the output experiences a "virtual drop" that is proportional to its current.

Note

Output Function

Constant Resistance

Constant Resistance Level

Note

Note

Supported VIs by Device

Depending on the instrument, output resistance is configurable only if you set the output function of the channel using the [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI as follows:

- PXIe-4141, PXIe-4143, PXIe-4145: DC Voltage
- PXIe-4135, PXIe-4137, PXIe-4139, PXIe-4147, PXIe-4162, PXIe-4163: DC Current or DC Voltage

[IMAGE alt='icon' src='nidcpower-configure-output-resistance-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. resistance — resistance specifies the output resistance, in ohms, for the specified channel(s). For more information about configuring output resistance, refer to the topic on output resistance for your device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Programmable Resistance Range and Merged Channels**

Using the [Merged Channels](/csh?context=nidcpower_dcpowerpropref_pnidcpower_mergedchannels)
 property to merge instrument outputs affects the valid output resistance range you can program.
 Refer to the Merged Channels topic for your device for details.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-power-line-frequency-vi.html language=enus -->
## TOPIC 00045: niDCPower Configure Power Line Frequency VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-power-line-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-power-line-frequency-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power line frequency for all channels in the session. NI-DCPower uses this value to select a timebase for setting the niDCPower Configure Aperture Time VI in power line cycles (PLCs). This VI is not supported by all devices. Refer to Supported VIs by Device for information about suppor

### niDCPower Configure Power Line Frequency VI

Specifies the power line frequency for all channels in the session.

NI-DCPower uses this value to select a timebase for setting the [niDCPower Configure Aperture Time](nidcpower-configure-aperture-time-vi.html) VI in power line cycles (PLCs).

Note

Supported VIs by Device

Refer to the *Measurement Configuration and Timing* topic for your device in the *NI DC Power Supplies and SMUs Help* for more information about how to configure your measurements.

[IMAGE alt='icon' src='nidcpower-configure-power-line-frequency-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. power line frequency — power line frequency specifies the power line frequency in hertz for specified channel(s). NI-DCPower uses this value to select a timebase for setting the Aperture Time property in power line cycles (PLCs). Refer to the Measurement Configuration and Timing topic for more information about how to configure your measurements. The valid values are 50 Hz and 60 Hz. Note Set this parameter to the frequency of the AC power line. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Measure

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-current-level-vi.html language=enus -->
## TOPIC 00046: niDCPower Configure Pulse Bias Current Level VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-current-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-current-level-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse bias current level that the specified channel(s) attempt to generate during the off phase of a pulse. A channel must be enabled for the specified current level to take effect. Refer to the niDCPower Configure Output Enabled VI for more information about enabling the channel. The

### niDCPower Configure Pulse Bias Current Level VI

Configures the pulse bias current level that the specified channel(s) attempt to generate during the off phase of a pulse.
 A channel must be enabled for the specified current level to take effect.

Refer to the [niDCPower Configure Output Enabled](nidcpower-configure-output-enabled-vi.html) VI for more information about enabling
 the channel. The **pulse current level** setting is applicable only if the channel is set to the **Pulse Current** output function using the
 [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Channels actively regulate the current at the specified level unless doing so causes a voltage drop greater than the [pulse bias voltage limit](nidcpower-configure-pulse-bias-voltage-limit-vi.html) across the channels' output terminals.

Note

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-configure-pulse-bias-current-level-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. pulse bias current level — pulse bias current level specifies the pulse bias current level, in amps, on the specified channel(s). error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Pulse Current

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-current-limit-vi.html language=enus -->
## TOPIC 00047: niDCPower Configure Pulse Bias Current Limit VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-current-limit-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-current-limit-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse bias current limit for the specified channel(s). A channel must be enabled for the specified current limit to take effect. Refer to the niDCPower Configure Output Enabled VI for more information about enabling the channel. The pulse bias current limit is the current that the out

### niDCPower Configure Pulse Bias Current Limit VI

Configures the pulse bias current limit for the specified channel(s). A channel must be enabled for
 the specified current limit to take effect.

Refer to the [niDCPower Configure Output Enabled](nidcpower-configure-output-enabled-vi.html) VI for more information about enabling the channel. The pulse bias current limit is the current that the output must not exceed when generating the desired [pulse bias voltage level](nidcpower-configure-pulse-bias-voltage-level-vi.html). The **pulse bias current limit** setting is only applicable if the channel is set to the **Pulse Voltage** output function using the [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Note

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-configure-pulse-bias-current-limit-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. pulse bias current limit — pulse bias current limit specifies the pulse bias current limit, in amps, on the specified channel(s). The limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Pulse Voltage

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-voltage-level-vi.html language=enus -->
## TOPIC 00048: niDCPower Configure Pulse Bias Voltage Level VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-voltage-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-voltage-level-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse bias voltage level that specified channel(s) attempt to generate during the off phase of a pulse. A channel must be enabled for the specified voltage level to take effect. Refer to the niDCPower Configure Output Enabled VI for more information about enabling the channel. The pul

### niDCPower Configure Pulse Bias Voltage Level VI

Configures the pulse bias voltage level that specified channel(s) attempt to generate during the off phase of a pulse.
 A channel must be enabled for the specified voltage level to take effect.

Refer to the [niDCPower Configure Output Enabled](nidcpower-configure-output-enabled-vi.html) VI for more information about enabling the channel. The **pulse bias voltage level** setting is applicable only if the channel is set to the **Pulse Voltage** output function using the [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Channels actively regulate the voltage at the specified level unless doing so causes a current greater than the [pulse bias current limit](nidcpower-configure-pulse-bias-current-limit-vi.html) through the channels' output terminals.

Note

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-configure-pulse-bias-voltage-level-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. pulse bias voltage level — pulse bias voltage level specifies the pulse bias voltage level, in volts, for the channel(s) generation. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Pulse Voltage

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-voltage-limit-vi.html language=enus -->
## TOPIC 00049: niDCPower Configure Pulse Bias Voltage Limit VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-voltage-limit-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-bias-voltage-limit-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse bias voltage limit for the specified channel(s). A channel must be enabled for the specified voltage limit to take effect. Refer to the niDCPower Configure Output Enabled VI for more information about enabling the channel. The pulse bias voltage limit is the voltage that the out

### niDCPower Configure Pulse Bias Voltage Limit VI

Configures the pulse bias voltage limit for the specified channel(s). A channel must be enabled for
 the specified voltage limit to take effect.

Refer to the [niDCPower Configure Output Enabled](nidcpower-configure-output-enabled-vi.html) VI for more information about enabling the channel. The pulse bias voltage limit is the voltage that the output must not exceed when generating the desired [pulse bias current level](nidcpower-configure-pulse-bias-current-level-vi.html). The **pulse bias voltage limit** setting is only applicable if the channel is set to the **Pulse Current** output function using the [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Note

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-configure-pulse-bias-voltage-limit-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. pulse bias voltage limit — pulse bias voltage limit specifies the pulse bias voltage limit, in volts, on the specified channel(s). The limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Pulse Current

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-current-level-vi.html language=enus -->
## TOPIC 00050: niDCPower Configure Pulse Current Level VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-current-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-current-level-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse current level that the specified channel(s) attempt to generate during the on phase of a pulse. A channel must be enabled for the specified current level to take effect. Refer to the niDCPower Configure Output Enabled VI for more information about enabling the channel. The pulse

### niDCPower Configure Pulse Current Level VI

Configures the pulse current level that the specified channel(s) attempt to generate during the on phase of a pulse.
 A channel must be enabled for the specified current level to take effect.

Refer to the [niDCPower Configure Output Enabled](nidcpower-configure-output-enabled-vi.html) VI for more information about enabling
 the channel. The **pulse current level** setting is applicable only if the channel is set to the **Pulse Current** output function using the
 [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Channels actively regulate the current at the specified level unless doing so causes a voltage drop greater than the [pulse voltage limit](nidcpower-configure-pulse-voltage-limit-vi.html) across the channels' output terminals.

Note

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-configure-pulse-current-level-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. pulse current level — pulse current level specifies the pulse current level, in amps, on the specified channel(s). error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Pulse Current

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-current-limit-range-vi.html language=enus -->
## TOPIC 00051: niDCPower Configure Pulse Current Limit Range VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-current-limit-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-current-limit-range-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse current limit range for the specified channel(s). The configured range defines the valid values to which you can set the pulse current limit and pulse bias current limit using the niDCPower Configure Pulse Current Limit and niDCPower Configure Pulse Bias Current Limit VIs. The p

### niDCPower Configure Pulse Current Limit Range VI

Configures the pulse current limit range for the specified channel(s).

The configured range defines the valid values to which you can set the **pulse current limit** and **pulse bias current limit** using the [niDCPower Configure Pulse Current Limit](nidcpower-configure-pulse-current-limit-vi.html) and [niDCPower Configure Pulse Bias Current Limit](nidcpower-configure-pulse-bias-current-limit-vi.html) VIs. The **pulse current limit range** setting is applicable only if the channel is set to the **Pulse Voltage** output function using the [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-configure-pulse-current-limit-range-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. pulse current limit range — pulse current limit range specifies the pulse current limit range, in amps, on the specified channel(s). error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Pulse Voltage

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-current-limit-vi.html language=enus -->
## TOPIC 00052: niDCPower Configure Pulse Current Limit VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-current-limit-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-pulse-current-limit-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pulse current limit for the specified channel(s). A channel must be enabled for the specified current limit to take effect. Refer to the niDCPower Configure Output Enabled VI for more information about enabling the channel. The pulse current limit is the current that the output must n

### niDCPower Configure Pulse Current Limit VI

Configures the pulse current limit for the specified channel(s). A channel must be enabled for
 the specified current limit to take effect.

Refer to the [niDCPower Configure Output Enabled](nidcpower-configure-output-enabled-vi.html) VI for more information about enabling the channel. The pulse current limit is the current that the output must not exceed when generating the desired [pulse voltage level](nidcpower-configure-pulse-voltage-level-vi.html). The **pulse current limit** setting is only applicable if the channel is set to the **Pulse Voltage** output function using the [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Note

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-configure-pulse-current-limit-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. pulse current limit — pulse current limit specifies the pulse current limit, in amps, on the specified channel(s). The limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Pulse Voltage

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-software-edge-shutdown-trigger-with-channels-vi.html language=enus -->
## TOPIC 00053: niDCPower Configure Software Edge Shutdown Trigger With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-software-edge-shutdown-trigger-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-software-edge-shutdown-trigger-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Shutdown trigger for software edge triggering. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png channel name channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/

### niDCPower Configure Software Edge Shutdown Trigger With Channels VI

Configures the Shutdown trigger for software edge triggering.

[IMAGE alt='icon' src='nidcpower-configure-software-edge-shutdown-trigger-with-channels-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niDCPower Configure Trigger With Channels (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-level-range-vi.html language=enus -->
## TOPIC 00054: niDCPower Configure Voltage Level Range VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-level-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-level-range-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the voltage level range for the specified channel(s). The configured range defines the valid values that the voltage level can be set to using the niDCPower Configure Voltage Level VI. The voltage level range setting is applicable only if the channel is set to the DC Voltage output functi

### niDCPower Configure Voltage Level Range VI

Configures the voltage level range for the specified channel(s).

The configured range defines the valid values that the voltage level can be set to using the [niDCPower Configure Voltage Level](nidcpower-configure-voltage-level-vi.html) VI. The voltage level range setting is applicable only if the channel is set to the **DC Voltage** output function using the [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Use the [Voltage Level Autorange](/csh?context=nidcpower_dcpowerpropref_pnidcpower_voltagelevelautorange) property to enable automatic selection of the voltage level range.

[IMAGE alt='icon' src='nidcpower-configure-voltage-level-range-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. voltage level range — voltage level range specifies the voltage level range, in volts, on the specified channel(s). For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-level-vi.html language=enus -->
## TOPIC 00055: niDCPower Configure Voltage Level VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-level-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the voltage level the specified channel(s) attempt to generate. A channel must be enabled for the specified voltage level to take effect. Refer to the niDCPower Configure Output Enabled VI for more information about enabling a channel. The voltage level setting is applicable only if the c

### niDCPower Configure Voltage Level VI

Configures the voltage level the specified channel(s) attempt to generate. A channel must be enabled for the specified voltage level to take effect.

Refer to the [niDCPower Configure Output Enabled](nidcpower-configure-output-enabled-vi.html) VI for more information about enabling
 a channel. The voltage level setting is applicable only if the channel is set to the **DC Voltage** output function using the
 [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Channels actively regulate the voltage at the specified level unless doing so causes a current drop greater than the [current limit](nidcpower-configure-current-limit-vi.html) across the channels' output terminals.

Note

[IMAGE alt='icon' src='nidcpower-configure-voltage-level-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. voltage level — voltage level specifies the voltage level, in volts, for the channel(s) generation. The valid values for this parameter are defined by the voltage level range that is selected using the niDCPower Configure Voltage Level Range VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-limit-range-vi.html language=enus -->
## TOPIC 00056: niDCPower Configure Voltage Limit Range VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-limit-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-limit-range-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the voltage limit range for the specified channel(s). The configured range defines the valid values the voltage limit can be set to using the niDCPower Configure Voltage Limit VI. The voltage limit range setting is applicable only if the channel is set to the DC Current output function us

### niDCPower Configure Voltage Limit Range VI

Configures the voltage limit range for the specified channel(s).

The configured range defines the valid values the voltage limit can be set to using the [niDCPower Configure Voltage Limit](nidcpower-configure-voltage-limit-vi.html) VI. The voltage limit range setting is applicable only if the channel is set to the **DC Current** output function using the [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Use the [Voltage Limit Autorange](/csh?context=nidcpower_dcpowerpropref_pnidcpower_voltagelimitautorange) property to enable automatic selection of the voltage limit range.

[IMAGE alt='icon' src='nidcpower-configure-voltage-limit-range-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. voltage limit range — voltage limit range specifies the voltage limit range, in volts, on the specified channel(s). For valid ranges, refer to the Ranges topics for your device in the NI DC Power Supplies and SMUs Help. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DC Current

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-limit-vi.html language=enus -->
## TOPIC 00057: niDCPower Configure Voltage Limit VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-limit-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-configure-voltage-limit-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the voltage limit for the specified channel(s). The channel must be enabled for the specified voltage limit to take effect. Refer to the niDCPower Configure Output Enabled VI for more information about enabling the channel. The voltage limit is the voltage that the output should not excee

### niDCPower Configure Voltage Limit VI

Configures the voltage limit for the specified channel(s). The channel must be enabled for the specified voltage limit to take effect.

Refer to the [niDCPower Configure Output Enabled](nidcpower-configure-output-enabled-vi.html) VI for more information about enabling the channel. The voltage limit is the voltage that the output should not exceed when generating the desired [current level](nidcpower-configure-current-level-vi.html). The voltage limit setting is applicable only if the channel is set to the **DC Current** output function using the [niDCPower Configure Output Function](nidcpower-configure-output-function-vi.html) VI.

Note

[IMAGE alt='icon' src='nidcpower-configure-voltage-limit-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. voltage limit — voltage limit specifies the voltage limit, in volts, on the specified channel(s). The limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. The valid values for this parameter are defined by the voltage limit range that is configured using the niDCPower Configure Voltage Limit Range VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DC Current

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-connect-internal-reference-vi.html language=enus -->
## TOPIC 00058: niDCPower Connect Internal Reference VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-connect-internal-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-connect-internal-reference-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects the Internal Reference to the Calibration Pin / Measurement Channel in preparation for adjustment. This VI is not supported by all devices. Refer to Supported VIs by Device for information about supported devices. Refer to the calibration procedure for the device you are calibrating for det

### niDCPower Connect Internal Reference VI

Connects the Internal Reference to the Calibration Pin / Measurement Channel in preparation for adjustment.

Note

Supported VIs by Device

Refer to the calibration procedure for the device you are calibrating for
 detailed instructions on the appropriate use of this VI. This VI can only be called from an
 external calibration session.

[IMAGE alt='icon' src='nidcpower-connect-internal-reference-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument calibration session. instrument handle is obtained from the niDCPower Initialize External Calibration VI. internal reference — internal reference specifies the internal reference to be connected to the calibration pin / measurement channel. 5V Reference (1054) Calibration pin / measurement channel connected to 5 V internal reference. 7V Reference (1119) Calibration pin / measurement channel connected to 7 V internal reference. 1kOhm Reference (1120) Calibration pin / measurement channel connected to 1 kΩ internal reference. 100kOhm Reference (1055) Calibration pin / measurement channel connected to 100 kΩ internal reference. Ground Reference (1056) Calibration pin / measurement channel connected to ground reference. None (1057) Calibration pin / measurement channel disconnected from internal reference. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 5V Reference (1054) | Calibration pin / measurement channel connected to 5 V internal reference. |
| 7V Reference (1119) | Calibration pin / measurement channel connected to 7 V internal reference. |
| 1kOhm Reference (1120) | Calibration pin / measurement channel connected to 1 kΩ internal reference. |
| 100kOhm Reference (1055) | Calibration pin / measurement channel connected to 100 kΩ internal reference. |
| Ground Reference (1056) | Calibration pin / measurement channel connected to ground reference. |
| None (1057) | Calibration pin / measurement channel disconnected from internal reference. |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-commit-step-with-channels-vi.html language=enus -->
## TOPIC 00059: niDCPower Create Advanced Sequence Commit Step With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-commit-step-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-commit-step-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a Commit step in the Active advanced sequence. A Commit step configures channels to a user-defined known state before starting the advanced sequence. You can specify the Active advanced sequence using the Active Advanced Sequence property. You must set the source mode to Sequence to use this

### niDCPower Create Advanced Sequence Commit Step With Channels VI

Creates a Commit step in the Active advanced sequence. A Commit step configures channels to a user-defined known state before starting the advanced sequence.

Note

You must set the source mode to Sequence to use this VI.

When you create an advanced sequence step, each property you passed to [niDCPower Create Advanced Sequence With Channels](nidcpower-create-advanced-sequence-with-channels-vi.html) is reset to its default value for the new step. To configure the step, you must first designate the new step as the Active step using the Active Advanced Sequence Step property or the **set as active step** parameter of this VI. Once the step is Active, use the [niDCPower Property Node](nidcpower-property-node-vi.html) to configure new values for the step.

Note

**Support for this VI**

This VI is not supported by all devices. Refer to [Supported VIs by Device](supportedvis.html) for information about supported devices.

Using [niDCPower Set Sequence](nidcpower-set-sequence-vi.html) with Advanced Sequence Mode VIs or functions for the same channel in the same session is not supported.

When a Commit step exists in the Active advanced sequence, you cannot set Output Function to Pulse Voltage or Pulse Current in either the Commit step (-1) or step 0.

[IMAGE alt='icon' src='nidcpower-create-advanced-sequence-commit-step-with-channels-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. set as active step (true) — set as active step specifies whether the step created with this VI is active in the Active advanced sequence. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**When Does the Commit Step Run in a Sequence?**

The driver applies the Commit step to a channel when it transitions to the Committed state. After the driver applies the Commit step to channels, the driver waits until the Source Delay has elapsed before waiting for the Start trigger.

Note

niDCPower Create Advanced Sequence With Channels

niDCPower Initiate With Channels

**Differences Between the Commit Step and Other Steps**

Parent topic:

niDCPower Create Advanced Sequence Step With Channels (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-step-with-channels-poly-vi.html language=enus -->
## TOPIC 00060: niDCPower Create Advanced Sequence Step With Channels (Poly) VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-step-with-channels-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-step-with-channels-poly-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a step in the Active advanced sequence. You can run this VI only when there is an Active advanced sequence. Create an advanced sequence using the niDCPower Create Advanced Sequence With Channels VI. Related Topics: Advanced Sequence Mode Programming States niDCPower Create Advanced Sequence

### niDCPower Create Advanced Sequence Step With Channels (Poly) VI

Creates a step in the Active advanced sequence.

Note

niDCPower Create Advanced Sequence With Channels

**Related Topics**:

[Advanced Sequence Mode](/csh?context=nidcpower_ni_dc_power_supplies_help_advancedsequencemode)

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

[niDCPower Create Advanced Sequence With Channels](nidcpower-create-advanced-sequence-with-channels-vi.html)

[IMAGE alt='icon' src='nidcpower-create-advanced-sequence-step-with-channels-poly-vi.png']

- [niDCPower Create Advanced Sequence Step With Channels VI](../../../instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-step-with-channels-vi.html) Creates a new advanced sequence step in the Active advanced sequence. You can configure properties for the new step only after the step is created.
- [niDCPower Create Advanced Sequence Commit Step With Channels VI](../../../instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-commit-step-with-channels-vi.html) Creates a Commit step in the Active advanced sequence. A Commit step configures channels to a user-defined known state before starting the advanced sequence.

Parent topic:

Advanced Sequencing

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-step-with-channels-vi.html language=enus -->
## TOPIC 00061: niDCPower Create Advanced Sequence Step With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-step-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-step-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new advanced sequence step in the Active advanced sequence. You can configure properties for the new step only after the step is created. When you create an advanced sequence step, each property you passed to niDCPower Create Advanced Sequence With Channels is reset to its default value fo

### niDCPower Create Advanced Sequence Step With Channels VI

Creates a new advanced sequence step in the Active advanced sequence. You can configure properties for the new step only after the step is created.

When you create an advanced sequence step, each property you passed to [niDCPower Create Advanced Sequence With Channels](nidcpower-create-advanced-sequence-with-channels-vi.html) is reset to its default value for the new step. To configure the step, you must first designate the new step as the Active step using the Active Advanced Sequence Step property or the **set as active step** parameter of this VI. Once the step is Active, use the [niDCPower Property Node](nidcpower-property-node-vi.html) to configure new values for the step.

**Support for this VI**

This VI is not supported by all devices. Refer to [Supported VIs by Device](supportedvis.html) for information about supported devices.

You must set the source mode to Sequence to use this VI.

Using the niDCPower Set Sequence VI with Advanced Sequence Mode VIs or functions for the same channel in the same session is unsupported.

[IMAGE alt='icon' src='nidcpower-create-advanced-sequence-step-with-channels-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. set as active step (true) — set as active step specifies whether the step created with this VI is active in the Active advanced sequence. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niDCPower Create Advanced Sequence Step With Channels (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-with-channels-vi.html language=enus -->
## TOPIC 00062: niDCPower Create Advanced Sequence With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-create-advanced-sequence-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an empty advanced sequence. Call the niDCPower Create Advanced Sequence Step Poly VI to add steps and, optionally, a Commit step to the active advanced sequence. You can create multiple advanced sequences for a channel. Advanced sequences for a particular channel are independent from any adv

### niDCPower Create Advanced Sequence With Channels VI

Creates an empty advanced sequence. Call the niDCPower Create Advanced Sequence Step Poly VI to add steps and, optionally, a Commit step to the active advanced sequence.

You can create multiple advanced sequences for a channel. Advanced sequences for a particular channel are independent from any advanced sequences of other channels. You can configure advanced sequences for one channel at a time or you can configure identical advanced sequences for multiple channels in unison.

Note

**Support for this VI**

You must set the source mode to Sequence to use this VI.

This VI is not supported by all devices. Refer to [Supported VIs by Device](supportedvis.html) for information about supported devices.

Using the [niDCPower Set Sequence](nidcpower-set-sequence-vi.html) VI with Advanced Sequence VIs for the same channel in the same session is unsupported.

Use this VI in the Uncommitted or Committed programming states. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for more information about NI-DCPower programming states.

**Related Topics**:

[Advanced Sequence Mode](/csh?context=nidcpower_ni_dc_power_supplies_help_advancedsequencemode)

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

[niDCPower Create Advanced Sequence Step With Channels (Poly)](nidcpower-create-advanced-sequence-step-with-channels-poly-vi.html)

[IMAGE alt='icon' src='nidcpower-create-advanced-sequence-with-channels-vi.png']

#### Inputs/Outputs

| set as active sequence (true) — set as active sequence specifies that this current sequence is active. instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. sequence name — sequence name specifies the name of the sequence to create. advanced sequence properties — advanced sequence properties specifies the properties you reconfigure per step in the advanced sequence. Refer to Supported Properties by Device for more information on properties that can be configured in an advanced sequence and their respective supported device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced Sequencing

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-detach-grpc-session-vi.html language=enus -->
## TOPIC 00063: niDCPower Detach gRPC session VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-detach-grpc-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-detach-grpc-session-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session specified in instrument handle but leaves the session open on the NI gRPC Device Server. NI-DCPower returns an error unless an open session at instrument handle exists and was created using the niDCPower Initialize With Independent Channels for gRPC session VI or the niDCPower Att

### niDCPower Detach gRPC session VI

Closes the session specified in **instrument handle** but leaves the session open on the NI gRPC Device Server.

NI-DCPower returns an error unless an open session at **instrument handle** exists and was created using the [niDCPower Initialize With Independent Channels for gRPC session](/csh?context=nidcpower_nidcpowerviref_nidcpower_initialize_with_independent_channels_for_grpc_session) VI or the [niDCPower Attach gRPC session](/csh?context=nidcpower_nidcpowerviref_nidcpower_attach_grpc_session) VI.

[IMAGE alt='icon' src='nidcpower-detach-grpc-session-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this provides standard error in functionality. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out. The default is no error. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

MeasurementLink

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-disable-pulse-trigger-with-channels-vi.html language=enus -->
## TOPIC 00064: niDCPower Disable Pulse Trigger With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-disable-pulse-trigger-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-disable-pulse-trigger-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the Pulse trigger. The specified channel(s) do not wait for a pulse trigger before performing a pulse operation. This VI is necessary only if you configured a Pulse trigger in the past and now want to disable it. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a

### niDCPower Disable Pulse Trigger With Channels VI

Disables the Pulse trigger. The specified channel(s) do not wait for a pulse trigger before performing a pulse operation.

This VI is necessary only if you configured a Pulse trigger in the past and now want to disable it.

[IMAGE alt='icon' src='nidcpower-disable-pulse-trigger-with-channels-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niDCPower Configure Trigger With Channels (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-disable-start-trigger-with-channels-vi.html language=enus -->
## TOPIC 00065: niDCPower Disable Start Trigger With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-disable-start-trigger-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-disable-start-trigger-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the Start trigger. The specified channel(s) do not wait for a Start trigger when starting generation or acquisition. This VI is necessary only if you configured a Start trigger in the past and now want to disable it. icon Inputs/Outputs civrn.png instrument handle instrument handle identifi

### niDCPower Disable Start Trigger With Channels VI

Disables the Start trigger. The specified channel(s) do not wait for a Start trigger when starting generation or acquisition.

This VI is necessary only if you configured a Start trigger in the past and now want to disable it.

[IMAGE alt='icon' src='nidcpower-disable-start-trigger-with-channels-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niDCPower Configure Trigger With Channels (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-disable-vi.html language=enus -->
## TOPIC 00066: niDCPower Disable VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-disable-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-disable-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI performs the same actions as the niDCPower Reset With Channels VI, except that this VI also immediately sets the Output Enabled property to FALSE. This VI opens the output relay on instruments that have an output relay. This VI applies to all channels and instruments in the session. NI-DCPow

### niDCPower Disable VI

This VI performs the same actions as the [niDCPower Reset With Channels](/csh?topicname=nidcpower-reset-with-channels-vi.html) VI, except that this VI also immediately sets the [Output Enabled](/csh?context=nidcpower_dcpowerpropref_pnidcpower_outputenabled) property to FALSE.

This VI opens the output relay on instruments that have an output relay.

This VI applies to all channels and instruments in the session.

Note

[IMAGE alt='icon' src='nidcpower-disable-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this provides standard error in functionality. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out. The default is no error. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-export-attribute-configuration-buffer-vi.html language=enus -->
## TOPIC 00067: niDCPower Export Attribute Configuration Buffer VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-export-attribute-configuration-buffer-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-export-attribute-configuration-buffer-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports a session configuration to a buffer. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provides standard error in

### niDCPower Export Attribute Configuration Buffer VI

Exports a session configuration to a buffer.

[IMAGE alt='icon' src='nidcpower-export-attribute-configuration-buffer-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. buffer — buffer is a byte array containing the exported session attribute configuration. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Channel Mapping Behavior**

When importing and exporting configurations between NI-DCPower sessions that were initialized with different channels, the configurations of the exporting channels are mapped to the importing channels based on the order of the resources you specify in the **resource name** input to the [niDCPower Initialize With Independent Channels](nidcpower-initialize-with-independent-channels-vi.html) VI.

Refer to [Import/Export Attribute Configuration Mapping Behavior](/csh?context=nidcpower_ni_dc_power_supplies_help_import_export_attribute_configuration_mapping_behavior) for details.

Parent topic:

niDCPower Export Attribute Configuration (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-export-attribute-configuration-file-vi.html language=enus -->
## TOPIC 00068: niDCPower Export Attribute Configuration File VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-export-attribute-configuration-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-export-attribute-configuration-file-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports a session configuration to the specified file. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cpath.png file path file path specifies the absolute path to the file to contain the exported attribute configuration. If you specify a

### niDCPower Export Attribute Configuration File VI

Exports a session configuration to the specified file.

[IMAGE alt='icon' src='nidcpower-export-attribute-configuration-file-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. file path — file path specifies the absolute path to the file to contain the exported attribute configuration. If you specify an empty or relative path, this VI returns an error. Default file extension: .nidcpowerconfig error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Channel Mapping Behavior**

When importing and exporting configurations between NI-DCPower sessions that were initialized with different channels, the configurations of the exporting channels are mapped to the importing channels based on the order of the resources you specify in the **resource name** input to the [niDCPower Initialize With Independent Channels](nidcpower-initialize-with-independent-channels-vi.html) VI.

Refer to [Import/Export Attribute Configuration Mapping Behavior](/csh?context=nidcpower_ni_dc_power_supplies_help_import_export_attribute_configuration_mapping_behavior) for details.

Parent topic:

niDCPower Export Attribute Configuration (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-export-attribute-configuration-poly-vi.html language=enus -->
## TOPIC 00069: niDCPower Export Attribute Configuration (Poly) VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-export-attribute-configuration-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-export-attribute-configuration-poly-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports a session configuration to either a file or a buffer. You can export and import supported configurations only between NI‑DCPower devices with identical model numbers and the same number of initialized channels. This VI verifies that the attributes you have configured for the session are vali

### niDCPower Export Attribute Configuration (Poly) VI

Exports a session configuration to either a file or a buffer.

You can export and import supported configurations only between NI‑DCPower devices with identical model numbers and the same number of initialized channels.

This VI verifies that the attributes you have configured for the session are valid. If the configuration is invalid, NI‑DCPower returns an error.

**Supported Configurations**

You can export and import the following configurations between NI‑DCPower sessions:

- Attribute configurations
- Advanced sequences

**Support for this VI**

You must set the source mode to **Sequence** in order to configure or export and import advanced sequences.

Configuration exports from sessions created with the [niDCPower Initialize With Independent Channels](nidcpower-initialize-with-independent-channels-vi.html) VI cannot be imported into sessions created with deprecated initialize VIs.

Note

**Related topics:**

[Using Properties and Attributes](/csh?context=nidcpower_ni_dc_power_supplies_help_using_properties_and_attributes)

[Setting Properties and Attributes Before Reading Them](/csh?context=nidcpower_ni_dc_power_supplies_help_setting_before_reading_attributes)

[IMAGE alt='icon' src='nidcpower-export-attribute-configuration-poly-vi.png']

#### Details

**Channel Mapping Behavior**

When importing and exporting configurations between NI-DCPower sessions that were initialized with different channels, the configurations of the exporting channels are mapped to the importing channels based on the order of the resources you specify in the **resource name** input to the [niDCPower Initialize With Independent Channels](nidcpower-initialize-with-independent-channels-vi.html) VI.

Refer to [Import/Export Attribute Configuration Mapping Behavior](/csh?context=nidcpower_ni_dc_power_supplies_help_import_export_attribute_configuration_mapping_behavior) for details.

- [niDCPower Export Attribute Configuration File VI](../../../instr-lib/nidcpower/nidcpower-llb/nidcpower-export-attribute-configuration-file-vi.html) Exports a session configuration to the specified file.
- [niDCPower Export Attribute Configuration Buffer VI](../../../instr-lib/nidcpower/nidcpower-llb/nidcpower-export-attribute-configuration-buffer-vi.html) Exports a session configuration to a buffer.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-export-signal-with-channels-vi.html language=enus -->
## TOPIC 00070: niDCPower Export Signal With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-export-signal-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-export-signal-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes signals (triggers and events) to the output terminal you specify. This VI is not supported by all devices. Refer to Supported VIs by Device for information about supported devices. The route is created when the specified channel is Committed. icon Inputs/Outputs cstr.png signal identifier (no

### niDCPower Export Signal With Channels VI

Routes signals (triggers and events) to the output terminal you specify.

Note

Supported VIs by Device

The route is created when the specified channel is [Committed](nidcpower-commit-with-channels-vi.html).

[IMAGE alt='icon' src='nidcpower-export-signal-with-channels-vi.png']

#### Inputs/Outputs

| signal identifier (none) — signal identifier (none) is reserved for future use. instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel to which you export the signal. You can only export a signal to one channel at a time. Specify the channel using the form PXI1Slot3/0, where PXI1Slot3 is the instrument resource name and 0 is the channel. signal — signal specifies which trigger or event to export. Source Complete Event (1030) Exports the Source Complete event. Measure Complete Event (1031) Exports the Measure Complete event. Sequence Iteration Complete Event (1032) Exports the Sequence Iteration Complete event. Sequence Engine Done Event (1033) Exports the Sequence Engine Done event. Pulse Complete Event (1053) Exports the Pulse Complete event. Ready for Pulse Trigger Event (1052) Exports the Ready for Pulse Trigger event. Start Trigger (1036) Exports the Start trigger. Source Trigger (1037) Exports the Source trigger. Measure Trigger (1038) Exports the Measure trigger Sequence Advance Trigger (1039) Exports the Sequence Advance trigger. Pulse Trigger (1040) Exports the Pulse trigger. output terminal — output terminal specifies where to export the selected signal. "" Do not export signal. "PXI_Trig0" The signal is exported on PXI or RTSI line 0. "PXI_Trig1" The signal is exported on PXI or RTSI line 1. "PXI_Trig2" The signal is exported on PXI or RTSI line 2. "PXI_Trig3" The signal is exported on PXI or RTSI line 3. "PXI_Trig4" The signal is exported on PXI or RTSI line 4. "PXI_Trig5" The signal is exported on PXI or RTSI line 5. "PXI_Trig6" The signal is exported on PXI or RTSI line 6. "PXI_Trig7" The signal is exported on PXI or RTSI line 7. You can also supply a fully qualified terminal name to this parameter, for example, /Dev1/PXI_Trig0, or /Dev1/Engine0/PXI_Trig0, where Engine0 is channel 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Source Complete Event (1030) | Exports the Source Complete event. |
| Measure Complete Event (1031) | Exports the Measure Complete event. |
| Sequence Iteration Complete Event (1032) | Exports the Sequence Iteration Complete event. |
| Sequence Engine Done Event (1033) | Exports the Sequence Engine Done event. |
| Pulse Complete Event (1053) | Exports the Pulse Complete event. |
| Ready for Pulse Trigger Event (1052) | Exports the Ready for Pulse Trigger event. |
| Start Trigger (1036) | Exports the Start trigger. |
| Source Trigger (1037) | Exports the Source trigger. |
| Measure Trigger (1038) | Exports the Measure trigger |
| Sequence Advance Trigger (1039) | Exports the Sequence Advance trigger. |
| Pulse Trigger (1040) | Exports the Pulse trigger. |
| "" | Do not export signal. |
| "PXI_Trig0" | The signal is exported on PXI or RTSI line 0. |
| "PXI_Trig1" | The signal is exported on PXI or RTSI line 1. |
| "PXI_Trig2" | The signal is exported on PXI or RTSI line 2. |
| "PXI_Trig3" | The signal is exported on PXI or RTSI line 3. |
| "PXI_Trig4" | The signal is exported on PXI or RTSI line 4. |
| "PXI_Trig5" | The signal is exported on PXI or RTSI line 5. |
| "PXI_Trig6" | The signal is exported on PXI or RTSI line 6. |
| "PXI_Trig7" | The signal is exported on PXI or RTSI line 7. |

Parent topic:

Triggers and Events

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-fetch-multiple-lcr-vi.html language=enus -->
## TOPIC 00071: niDCPower Fetch Multiple LCR VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-fetch-multiple-lcr-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-fetch-multiple-lcr-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of previously measured LCR data on the specified channel that have been taken and stored in a buffer. To use this VI: Set Measure When to Automatically after Source Complete or On Measure Trigger Put the channel in the Running state (call niDCPower Initiate With Channels) This funct

### niDCPower Fetch Multiple LCR VI

Returns an array of previously measured LCR data on the specified channel that have been taken and stored in a buffer.

To use this VI:

- Set Measure When to Automatically after Source Complete or On Measure Trigger
- Put the channel in the Running state (call niDCPower Initiate With Channels )

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-fetch-multiple-lcr-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel from which to fetch data. You can only fetch data from one channel at a time. Specify the channel using the form PXI1Slot3/0, where PXI1Slot3 is the instrument resource name and 0 is the channel. count (1) — count (1) specifies the number of measurements to fetch. timeout (1.0) — timeout (1.0) specifies the maximum time allowed for this VI to complete, in seconds. If the VI does not complete within this time interval, NI-DCPower returns an error. Note When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. actual count — actual count indicates the number of measured values actually retrieved from the specified channel. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. measurements — measurements returns an array of LCR measurement data. V DC — V DC is the measured DC voltage, in volts. I DC — I DC is the measured DC current, in amps. stimulus frequency — stimulus frequency is the frequency of the LCR test signal, in Hz. AC voltage — AC voltage is the measured AC voltage, in volts RMS. AC current — AC current is the measured AC current, in amps RMS. Z — Z is the complex impedance. Z magnitude — Z magnitude is the magnitude of the complex impedance, in ohms. Z theta — Z theta is the impedance phase angle, in degrees. Y — Y is the complex admittance. Y magnitude — Y magnitude is the magnitude of the complex admittance, in siemens. Y theta — Y theta is the admittance phase angle, in degrees. Ls — Ls is the inductance, in henrys, as measured using a series circuit model. Cs — Cs is the capacitance, in farads, as measured using a series circuit model. Rs — Rs is the resistance, in ohms, as measured using a series circuit model. Lp — Lp is the inductance, in henrys, as measured using a parallel circuit model. Cp — Cp is the capacitance, in farads, as measured using a parallel circuit model. Rp — Rp is the resistance, in ohms, as measured using a parallel circuit model. D — D is the dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor. Q — Q is the quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor. measurement mode — measurement mode returns the measurement mode. SMU (1061) The channel(s) are operating as a power supply/SMU. LCR (1062) The channel(s) are operating as an LCR meter. DC in compliance — DC in compliance indicates whether the output was in DC compliance at the time the measurement was taken. Pad 0 — AC in compliance — AC in compliance indicates whether the output was in AC compliance at the time the measurement was taken. Pad 1 — unbalanced — unbalanced indicates whether the bridge was unbalanced at the time the measurement was taken. Pad 2 — Reserved 1 — Reserved 2 — Reserved 3 — Reserved 4 — Reserved 5 — Reserved 6 — Reserved 7 — error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| V DC — V DC is the measured DC voltage, in volts. I DC — I DC is the measured DC current, in amps. stimulus frequency — stimulus frequency is the frequency of the LCR test signal, in Hz. AC voltage — AC voltage is the measured AC voltage, in volts RMS. AC current — AC current is the measured AC current, in amps RMS. Z — Z is the complex impedance. Z magnitude — Z magnitude is the magnitude of the complex impedance, in ohms. Z theta — Z theta is the impedance phase angle, in degrees. Y — Y is the complex admittance. Y magnitude — Y magnitude is the magnitude of the complex admittance, in siemens. Y theta — Y theta is the admittance phase angle, in degrees. Ls — Ls is the inductance, in henrys, as measured using a series circuit model. Cs — Cs is the capacitance, in farads, as measured using a series circuit model. Rs — Rs is the resistance, in ohms, as measured using a series circuit model. Lp — Lp is the inductance, in henrys, as measured using a parallel circuit model. Cp — Cp is the capacitance, in farads, as measured using a parallel circuit model. Rp — Rp is the resistance, in ohms, as measured using a parallel circuit model. D — D is the dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor. Q — Q is the quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor. measurement mode — measurement mode returns the measurement mode. SMU (1061) The channel(s) are operating as a power supply/SMU. LCR (1062) The channel(s) are operating as an LCR meter. DC in compliance — DC in compliance indicates whether the output was in DC compliance at the time the measurement was taken. Pad 0 — AC in compliance — AC in compliance indicates whether the output was in AC compliance at the time the measurement was taken. Pad 1 — unbalanced — unbalanced indicates whether the bridge was unbalanced at the time the measurement was taken. Pad 2 — Reserved 1 — Reserved 2 — Reserved 3 — Reserved 4 — Reserved 5 — Reserved 6 — Reserved 7 — |  |
| SMU (1061) | The channel(s) are operating as a power supply/SMU. |
| LCR (1062) | The channel(s) are operating as an LCR meter. |

Parent topic:

Measure

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-fetch-multiple-vi.html language=enus -->
## TOPIC 00072: niDCPower Fetch Multiple VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-fetch-multiple-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-fetch-multiple-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of voltage measurements, an array of current measurements, and an array of compliance measurements that were previously taken and are stored in the niDCPower buffer. This VI should not be used when the Measure When property is configured to On Demand. You must first call niDCPower I

### niDCPower Fetch Multiple VI

Returns an array of voltage measurements, an array of current measurements, and an array of compliance measurements that were previously taken and are stored in the niDCPower buffer.

This VI should not be used when the [Measure When](/csh?context=nidcpower_dcpowerpropref_pnidcpower_measurewhen) property is configured to **On Demand**. You must first call [niDCPower Initiate With Channels](nidcpower-initiate-with-channels-vi.html) before calling this VI.

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-fetch-multiple-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel from which to fetch data. You can only fetch data from one channel at a time. Specify the channel using the form PXI1Slot3/0, where PXI1Slot3 is the instrument resource name and 0 is the channel. count (1) — count (1) specifies the number of measurements to fetch. timeout (1.0) — timeout (1.0) specifies the maximum time allowed for this VI to complete, in seconds. If the VI does not complete within this time interval, NI-DCPower returns an error. Note When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. actual count — actual count indicates the number of measured values actually retrieved from the specified channel. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. voltage measurements — voltage measurements returns an array of voltage measurements. current measurements — current measurements returns an array of current measurements. The measurements in the array are returned in the same order as the channels specified in channel name. in compliance — in compliance returns an array of Boolean values indicating whether the output was in compliance at the time the measurement was taken. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Behavior with LCR Measurements**

LCR-specific measurements may be present in the buffer when you call this VI in certain cases, such as when changing the instrument mode during an advanced sequence. If LCR measurements are in the buffer, this VI returns the DC portion of any available voltage and current measurements and discards LCR-specific measurements.

Parent topic:

Measure

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-get-cal-user-defined-info-max-size-vi.html language=enus -->
## TOPIC 00073: niDCPower Get Cal User Defined Info Max Size VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-get-cal-user-defined-info-max-size-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-get-cal-user-defined-info-max-size-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum number of characters that can be used to store user-defined information in the device onboard EEPROM. This VI can only be used in a session initialized to a single instrument. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument ses

### niDCPower Get Cal User Defined Info Max Size VI

Returns the maximum number of characters that can be used to store user-defined
 information in the device onboard EEPROM.

Note

[IMAGE alt='icon' src='nidcpower-get-cal-user-defined-info-max-size-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. info size — info size returns the number of characters that can be stored in the device onboard EEPROM. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-get-cal-user-defined-info-vi.html language=enus -->
## TOPIC 00074: niDCPower Get Cal User Defined Info VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-get-cal-user-defined-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-get-cal-user-defined-info-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the user-defined information in the device onboard EEPROM. This VI can only be used in a session initialized to a single instrument. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in (no error) error in des

### niDCPower Get Cal User Defined Info VI

Returns the user-defined information in the device onboard EEPROM.

Note

[IMAGE alt='icon' src='nidcpower-get-cal-user-defined-info-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. info — info returns the user-defined information stored in the device onboard EEPROM. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-import-attribute-configuration-buffer-vi.html language=enus -->
## TOPIC 00075: niDCPower Import Attribute Configuration Buffer VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-import-attribute-configuration-buffer-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-import-attribute-configuration-buffer-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports a configuration to the session from the specified buffer. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. c1du8.png buffer buffer is a byte array containing the session attribute configuration to import. cerrcodeclst.png error in

### niDCPower Import Attribute Configuration Buffer VI

Imports a configuration to the session from the specified buffer.

[IMAGE alt='icon' src='nidcpower-import-attribute-configuration-buffer-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. buffer — buffer is a byte array containing the session attribute configuration to import. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Channel Mapping Behavior**

When importing and exporting configurations between NI-DCPower sessions that were initialized with different channels, the configurations of the exporting channels are mapped to the importing channels based on the order of the resources you specify in the **resource name** input to the [niDCPower Initialize With Independent Channels](nidcpower-initialize-with-independent-channels-vi.html) VI.

Refer to [Import/Export Attribute Configuration Mapping Behavior](/csh?context=nidcpower_ni_dc_power_supplies_help_import_export_attribute_configuration_mapping_behavior) for details.

Parent topic:

niDCPower Import Attribute Configuration (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-import-attribute-configuration-file-vi.html language=enus -->
## TOPIC 00076: niDCPower Import Attribute Configuration File VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-import-attribute-configuration-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-import-attribute-configuration-file-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports a configuration to the session from the specified file. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cpath.png file path file path specifies the absolute path to the file containing the attribute configuration to import. If you

### niDCPower Import Attribute Configuration File VI

Imports a configuration to the session from the specified file.

[IMAGE alt='icon' src='nidcpower-import-attribute-configuration-file-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. file path — file path specifies the absolute path to the file containing the attribute configuration to import. If you specify an empty or relative path, this VI returns an error. Default file extension: .nidcpowerconfig error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Channel Mapping Behavior**

When importing and exporting configurations between NI-DCPower sessions that were initialized with different channels, the configurations of the exporting channels are mapped to the importing channels based on the order of the resources you specify in the **resource name** input to the [niDCPower Initialize With Independent Channels](nidcpower-initialize-with-independent-channels-vi.html) VI.

Refer to [Import/Export Attribute Configuration Mapping Behavior](/csh?context=nidcpower_ni_dc_power_supplies_help_import_export_attribute_configuration_mapping_behavior) for details.

Parent topic:

niDCPower Import Attribute Configuration (Poly) VI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-import-attribute-configuration-poly-vi.html language=enus -->
## TOPIC 00077: niDCPower Import Attribute Configuration (Poly) VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-import-attribute-configuration-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-import-attribute-configuration-poly-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports a configuration to the session from either a file or a buffer. You can export and import supported configurations only between NI‑DCPower devices with identical model numbers and the same number of initialized channels. You cannot call this VI while any channel is in the Running state. Suppo

### niDCPower Import Attribute Configuration (Poly) VI

Imports a configuration to the session from either a file or a buffer.

You can export and import supported configurations only between NI‑DCPower devices with identical model numbers and the same number of initialized channels.

Note

Running

**Supported Configurations**

You can export and import the following configurations between NI‑DCPower sessions:

- Attribute configurations
- Advanced sequences

**Support for this VI**

You must set the source mode to **Sequence** in order to configure or export and import advanced sequences.

Configuration exports from sessions created with the [niDCPower Initialize With Independent Channels](nidcpower-initialize-with-independent-channels-vi.html) VI cannot be imported into sessions created with deprecated initialize VIs.

Note

**Related topics:**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

[Using Properties and Attributes](/csh?context=nidcpower_ni_dc_power_supplies_help_using_properties_and_attributes)

[Setting Properties and Attributes Before Reading Them](/csh?context=nidcpower_ni_dc_power_supplies_help_setting_before_reading_attributes)

[IMAGE alt='icon' src='nidcpower-import-attribute-configuration-poly-vi.png']

#### Details

**Channel Mapping Behavior**

When importing and exporting configurations between NI-DCPower sessions that were initialized with different channels, the configurations of the exporting channels are mapped to the importing channels based on the order of the resources you specify in the **resource name** input to the [niDCPower Initialize With Independent Channels](nidcpower-initialize-with-independent-channels-vi.html) VI.

Refer to [Import/Export Attribute Configuration Mapping Behavior](/csh?context=nidcpower_ni_dc_power_supplies_help_import_export_attribute_configuration_mapping_behavior) for details.

- [niDCPower Import Attribute Configuration File VI](../../../instr-lib/nidcpower/nidcpower-llb/nidcpower-import-attribute-configuration-file-vi.html) Imports a configuration to the session from the specified file.
- [niDCPower Import Attribute Configuration Buffer VI](../../../instr-lib/nidcpower/nidcpower-llb/nidcpower-import-attribute-configuration-buffer-vi.html) Imports a configuration to the session from the specified buffer.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-external-calibration-vi.html language=enus -->
## TOPIC 00078: niDCPower Initialize External Calibration VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-external-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-external-calibration-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: If password is valid, this VI creates a new IVI instrument driver session to the device specified in resource name and returns an instrument handle you use to identify the device in all subsequent NI-DCPower VI calls. This VI also sends initialization commands to set the device to the state necessar

### niDCPower Initialize External Calibration VI

If **password** is valid, this VI creates a new IVI instrument
 driver session to the device specified in **resource name** and
 returns an instrument handle you use to identify the device in all subsequent NI-DCPower
 VI calls. This VI also sends initialization commands to set the device to the state
 necessary for the operation of NI-DCPower.

Opening a calibration session always performs a reset. Refer to the calibration procedure for the device you
 are calibrating for detailed instructions on the appropriate use of this VI.

Note

[IMAGE alt='icon' src='nidcpower-initialize-external-calibration-vi.png']

#### Inputs/Outputs

| resource name — resource name specifies the resource name assigned by Measurement & Automation Explorer (MAX), for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. resource name can also accept a logical IVI name for a device. password — password specifies the password for opening a calibration session. password can be a maximum of four alphanumeric characters. The initial password is factory configured to NI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-vi.html language=enus -->
## TOPIC 00079: niDCPower Initialize VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI is deprecated, use niDCPower Initialize With Independent Channels instead. Creates a new IVI instrument driver session to the power supply specified in resource name and returns a session handle you use to identify the session in all subsequent NI-DCPower VI calls. This VI also sends initial

### niDCPower Initialize VI

This VI is deprecated, use [niDCPower Initialize With Independent Channels](/csh?topicname=nidcpower-initialize-with-independent-channels-vi.html) instead.

Creates a new IVI instrument driver session to the power supply specified in **resource name** and returns a session handle you use to identify the
 session in all subsequent NI-DCPower VI calls. This VI also sends initialization
 commands to set the power supply to the state necessary for NI-DCPower to operate.

To place the power supply in a known startup state when creating a new session, set **reset device** to TRUE. This action is equivalent to using the [niDCPower Reset With Channels](nidcpower-reset-with-channels-vi.html) VI.

To open a session and leave the device in its existing configuration without passing through a transitional output state, set **reset device** to FALSE, and then immediately call the [niDCPower Abort With Channels](nidcpower-abort-with-channels-vi.html) VI. Then configure the device as in the previous session changing only the desired settings, and then call the [niDCPower Initiate With Channels](nidcpower-initiate-with-channels-vi.html) VI.

[IMAGE alt='icon' src='nidcpower-initialize-vi.png']

#### Inputs/Outputs

| resource name — resource name specifies the resource name assigned by Measurement & Automation Explorer (MAX), for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. resource name can also accept a logical IVI name for a device. id query — id query specifies whether the device is queried to determine if the device is a valid instrument for NI-DCPower. The default is TRUE. reset device — reset device specifies whether to reset the device during the initialization procedure. The default is TRUE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-with-channels-vi.html language=enus -->
## TOPIC 00080: niDCPower Initialize With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI is deprecated, use niDCPower Initialize With Independent Channels instead. Creates and returns a new NI-DCPower session to the instrument specified in resource name to be used in all subsequent NI-DCPower VI calls. With this VI, you can optionally set the initial state of the following sessi

### niDCPower Initialize With Channels VI

This VI is deprecated, use [niDCPower Initialize With Independent Channels](/csh?topicname=nidcpower-initialize-with-independent-channels-vi.html) instead.

Creates and returns a new NI-DCPower session to the instrument specified in **resource name** to be used in all subsequent NI-DCPower VI calls.

With this VI, you can optionally set the initial state of the following session properties:
 [Simulate](/csh?context=nidcpower_dcpowerpropref_pnidcpower_simulate) and [Driver Setup](/csh?context=nidcpower_dcpowerpropref_pnidcpower_driversetup). After calling this VI, the session will be in the Uncommitted state. Refer to the [Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) topic in the *NI DC Power Supplies and SMUs Help* for details about specific software states.

To place the device in a known startup state when creating a new session, set **reset** to TRUE. This action is equivalent to using the [niDCPower Reset With Channels](nidcpower-reset-with-channels-vi.html) VI immediately after initializing the session.

To open a session and leave the device in its existing configuration without passing through a transitional output state, set **reset** to FALSE. Next, configure the device as in the previous session, change the desired settings, and then call the [niDCPower Initiate With Channels](nidcpower-initiate-with-channels-vi.html) VI to write both settings.

**Related topics:**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

[IMAGE alt='icon' src='nidcpower-initialize-with-channels-vi.png']

#### Inputs/Outputs

| option string — option string specifies the initial value of certain properties for the session. The syntax for option string is a list of properties with an assigned value where 1 is TRUE and 0 is FALSE. For example: Simulate=0, DriverSetup=Model:<model number>; BoardType:<bus connector> To simulate a multi-instrument session, set Simulate to 1 and list multiple instruments for DriverSetup. For example: Simulate=1, DriverSetup=ResourceName:<instrument name>; Model:<model number>; BoardType:<bus connector> & ResourceName:<resource name>; Model:<model number>; BoardType:<bus connector> You do not have to specify a value for all the properties. If you do not specify a value for a property, the default value is used. For more information about simulating a device, refer to Simulating an Instrument in the NI DC Power Supplies and SMUs Help. resource name — resource name specifies the resource name assigned by Measurement & Automation Explorer (MAX), for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. resource name can also accept a logical IVI name for a device. channels — channels specifies which channel(s) to include in the newly created session. Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2). In the Running state, multiple channel configurations are performed sequentially based on the order specified in this parameter. If you do not wire this parameter, by default all channels on the device are included in the session. reset (false) — reset (false) specifies whether to reset channel(s) during the initialization procedure. The default is FALSE. To place channel(s) in a known startup state when creating a new session, set reset to TRUE. This action is equivalent to using the niDCPower Reset With Channels VI immediately after initializing the session. To open a session and leave the channel(s) in an existing configuration without passing through a transitional output state, set reset to FALSE. Next, configure the channel(s) as in the previous session, change the desired settings, and then call the niDCPower Initiate With Channels VI to write both settings. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-with-independent-channels-for-grpc-session-vi.html language=enus -->
## TOPIC 00081: niDCPower Initialize With Independent Channels for gRPC session VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-with-independent-channels-for-grpc-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-with-independent-channels-for-grpc-session-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new NI-DCPower session on the specified NI gRPC Device Server and attaches to it. Returns a session handle to be used in all subsequent NI-DCPower VI calls. This VI initializes a NI-DCPower session on the specified NI gRPC Device Server and attaches to it from LabVIEW. If the session n

### niDCPower Initialize With Independent Channels for gRPC session VI

Initializes a new NI-DCPower session on the specified NI gRPC Device Server and attaches to it. Returns a session handle to be used in all subsequent NI-DCPower VI calls.

This VI initializes a NI-DCPower session on the specified NI gRPC Device Server and attaches to it from LabVIEW. If the session name is specified in the gRPC options and the same session name is already in use on the server, then NI-DCPower will return an error. If the session name in the gRPC options is empty, the resource name will be used as a session name.

The resulting session in LabVIEW forwards driver calls to the corresponding session on the server.

[IMAGE alt='icon' src='nidcpower-initialize-with-independent-channels-for-grpc-session-vi.png']

#### Inputs/Outputs

| option string — option string specifies the initial value of certain properties for the session. The syntax for option string is a list of properties with an assigned value where 1 is TRUE and 0 is FALSE. For example: Simulate=0, DriverSetup=Model:<model number>; BoardType:<bus connector> To simulate a multi-instrument session, set Simulate to 1 and list multiple instruments for DriverSetup. For example: Simulate=1, DriverSetup=ResourceName:<instrument name>; Model:<model number>; BoardType:<bus connector> & ResourceName:<resource name>; Model:<model number>; BoardType:<bus connector> You do not have to specify a value for all the properties. If you do not specify a value for a property, the default value is used. For more information about simulating a device, refer to Simulating an Instrument in the NI DC Power Supplies and SMUs Help. resource name — resource name specifies the NI-DCPower resources to use in the session. NI-DCPower resources can be names of the instrument(s) assigned by Measurement & Automation Explorer (MAX) and the channel(s) to initialize. Specify the instrument(s) and channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not specify channels, all channels of the instrument(s) are included in the session. gRPC options — gRPC options specifies the information used to connect to the server. session name — session name specifies the name of the MeasurementLink gRPC session. address (localhost) — address (localhost) specifies the address of the NI gRPC Device Server. port (31763) — port (31763) specifies the port that the NI gRPC Device Server monitors for connections. reset (false) — reset (false) specifies whether to reset channel(s) during the initialization procedure. The default is FALSE. To place channel(s) in a known startup state when creating a new session, set reset to TRUE. This action is equivalent to using the niDCPower Reset With Channels VI immediately after initializing the session. To open a session and leave the channel(s) in an existing configuration without passing through a transitional output state, set reset to FALSE. Next, configure the channel(s) as in the previous session, change the desired settings, and then call the niDCPower Initiate With Channels VI to write both settings. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| session name — session name specifies the name of the MeasurementLink gRPC session. address (localhost) — address (localhost) specifies the address of the NI gRPC Device Server. port (31763) — port (31763) specifies the port that the NI gRPC Device Server monitors for connections. |

Parent topic:

MeasurementLink

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-with-independent-channels-vi.html language=enus -->
## TOPIC 00082: niDCPower Initialize With Independent Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-with-independent-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-initialize-with-independent-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new NI-DCPower session to the specified instrument(s) and channel(s) and returns a session handle to be used in all subsequent NI-DCPower VI calls. After calling this VI, the specified channel or channels will be in the Uncommitted state. With this VI and channel-based NI-DCPower VIs and p

### niDCPower Initialize With Independent Channels VI

Creates a new NI-DCPower session to the specified instrument(s) and channel(s) and returns a session handle to be used in all subsequent NI-DCPower VI calls.

After calling this VI, the specified channel or channels will be in the Uncommitted state.

With this VI and channel-based NI-DCPower VIs and properties, you can use any channels in the session independently. For example, you can initiate a subset of channels in the session with [niDCPower Initiate With Channels](nidcpower-initiate-with-channels-vi.html), and the other channels in the session remain in the Uncommitted state.

**Related topics:**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

[IMAGE alt='icon' src='nidcpower-initialize-with-independent-channels-vi.png']

#### Inputs/Outputs

| option string — option string specifies the initial value of certain properties for the session. The syntax for option string is a list of properties with an assigned value where 1 is TRUE and 0 is FALSE. For example: Simulate=0, DriverSetup=Model:<model number>; BoardType:<bus connector> To simulate a multi-instrument session, set Simulate to 1 and list multiple instruments for DriverSetup. For example: Simulate=1, DriverSetup=ResourceName:<instrument name>; Model:<model number>; BoardType:<bus connector> & ResourceName:<resource name>; Model:<model number>; BoardType:<bus connector> You do not have to specify a value for all the properties. If you do not specify a value for a property, the default value is used. For more information about simulating a device, refer to Simulating an Instrument in the NI DC Power Supplies and SMUs Help. resource name — resource name specifies the NI-DCPower resources to use in the session. NI-DCPower resources can be names of the instrument(s) assigned by Measurement & Automation Explorer (MAX) and the channel(s) to initialize. Specify the instrument(s) and channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not specify channels, all channels of the instrument(s) are included in the session. reset (false) — reset (false) specifies whether to reset channel(s) during the initialization procedure. The default is FALSE. To place channel(s) in a known startup state when creating a new session, set reset to TRUE. This action is equivalent to using the niDCPower Reset With Channels VI immediately after initializing the session. To open a session and leave the channel(s) in an existing configuration without passing through a transitional output state, set reset to FALSE. Next, configure the channel(s) as in the previous session, change the desired settings, and then call the niDCPower Initiate With Channels VI to write both settings. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Details of Independent Channel Operation**

When you initialize with independent channels, each channel steps through the NI-DCPower programming state model independently of all other channels, and you can specify a subset of channels for most operations.

Note

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-load-compensation-vi.html language=enus -->
## TOPIC 00083: niDCPower Perform LCR Load Compensation VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-load-compensation-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-load-compensation-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates load compensation data for LCR measurements for the test spots you specify. You must physically configure your LCR circuit with an appropriate reference load to use this VI to generate valid load compensation data. When you call this function: The load compensation data is written to the o

### niDCPower Perform LCR Load Compensation VI

Generates load compensation data for LCR measurements for the test spots you specify.

You must physically configure your LCR circuit with an appropriate reference load to use this VI to generate valid load compensation data.

Note

- The load compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
- Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

To apply the load compensation data you generate with this VI to your LCR measurements, set the [Load Compensation Enabled](/csh?context=nidcpower_dcpowerpropref_pnidcpower_lcrloadcompensationenabled) property to TRUE.

Note

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-perform-lcr-load-compensation-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. load compensation spots — load compensation spots defines the frequencies and DUT specifications to use for LCR load compensation. You can specify <=1000 spot frequencies. frequency — frequency is the spot frequency. reference value type — reference value type is a known specification value of your DUT to use as the basis for load compensation. Impedance (1076) The actual impedance, comprising real resistance and imaginary reactance, of your DUT. Supply resistance, in ohms, to reference value A; supply reactance, in ohms, to reference value B. Ideal Capacitance (1077) The ideal capacitance of your DUT. Supply capacitance, in farads, to reference value A. Ideal Inductance (1078) The ideal inductance of your DUT. Supply inductance, in henrys, to reference value A. Ideal Resistance (1079) The ideal resistance of your DUT. Supply resistance, in ohms, to reference value A. reference value A — reference value A is a value that describes the reference value type specification. Use as indicated by the reference value type option you choose. reference value B — reference value B is, if applicable, a value that describes the reference value type specification. Use as indicated by the reference value type option you choose. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| frequency — frequency is the spot frequency. reference value type — reference value type is a known specification value of your DUT to use as the basis for load compensation. Impedance (1076) The actual impedance, comprising real resistance and imaginary reactance, of your DUT. Supply resistance, in ohms, to reference value A; supply reactance, in ohms, to reference value B. Ideal Capacitance (1077) The ideal capacitance of your DUT. Supply capacitance, in farads, to reference value A. Ideal Inductance (1078) The ideal inductance of your DUT. Supply inductance, in henrys, to reference value A. Ideal Resistance (1079) The ideal resistance of your DUT. Supply resistance, in ohms, to reference value A. reference value A — reference value A is a value that describes the reference value type specification. Use as indicated by the reference value type option you choose. reference value B — reference value B is, if applicable, a value that describes the reference value type specification. Use as indicated by the reference value type option you choose. |  |
| Impedance (1076) | The actual impedance, comprising real resistance and imaginary reactance, of your DUT. Supply resistance, in ohms, to reference value A; supply reactance, in ohms, to reference value B. |
| Ideal Capacitance (1077) | The ideal capacitance of your DUT. Supply capacitance, in farads, to reference value A. |
| Ideal Inductance (1078) | The ideal inductance of your DUT. Supply inductance, in henrys, to reference value A. |
| Ideal Resistance (1079) | The ideal resistance of your DUT. Supply resistance, in ohms, to reference value A. |

Parent topic:

LCR Compensation

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-open-compensation-vi.html language=enus -->
## TOPIC 00084: niDCPower Perform LCR Open Compensation VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-open-compensation-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-open-compensation-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates open compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify. You must physically configure an open LCR circuit to use this VI to generate valid open compensation data. When you call this function: The open c

### niDCPower Perform LCR Open Compensation VI

Generates open compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify.

You must physically configure an open LCR circuit to use this VI to generate valid open compensation data.

Note

- The open compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
- Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

To apply the open compensation data you generate with this VI to your LCR measurements, set the [Open Compensation Enabled](/csh?context=nidcpower_dcpowerpropref_pnidcpower_lcropencompensationenabled) property to TRUE.

Corrections for frequencies other than the default frequencies or any additional frequencies you specify are interpolated.

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-perform-lcr-open-compensation-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. additional frequencies — additional frequencies defines a further set of frequencies, in addition to the default frequencies, to perform the compensation for. You can specify <=200 additional frequencies. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Default Open Compensation Frequencies**

By default, NI-DCPower uses the following frequencies for LCR open compensation:

- 10 logarithmic steps at 1 kHz frequency decade
- 10 logarithmic steps at 10 kHz frequency decade
- 100 logarithmic steps at 100 kHz frequency decade
- 100 logarithmic steps at 1 MHz frequency decade

Note

Parent topic:

LCR Compensation

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-short-compensation-vi.html language=enus -->
## TOPIC 00085: niDCPower Perform LCR Short Compensation VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-short-compensation-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-short-compensation-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates short compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify. You must physically configure your LCR circuit with a short to use this VI to generate valid short compensation data. When you call this function

### niDCPower Perform LCR Short Compensation VI

Generates short compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify.

You must physically configure your LCR circuit with a short to use this VI to generate valid short compensation data.

Note

- The short compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
- Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

To apply the short compensation data you generate with this VI to your LCR measurements, set the [Short Compensation Enabled](/csh?context=nidcpower_dcpowerpropref_pnidcpower_lcrshortcompensationenabled) property to TRUE.

Corrections for frequencies other than the default frequencies or any additional frequencies you specify are interpolated.

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-perform-lcr-short-compensation-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. additional frequencies — additional frequencies defines a further set of frequencies, in addition to the default frequencies, to perform the compensation for. You can specify <=200 additional frequencies. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Default Short Compensation Frequencies**

By default, NI-DCPower uses the following frequencies for LCR short compensation:

- 10 logarithmic steps at 1 kHz frequency decade
- 10 logarithmic steps at 10 kHz frequency decade
- 100 logarithmic steps at 100 kHz frequency decade
- 100 logarithmic steps at 1 MHz frequency decade

Note

Parent topic:

LCR Compensation

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-short-custom-cable-compensation-vi.html language=enus -->
## TOPIC 00086: niDCPower Perform LCR Short Custom Cable Compensation VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-short-custom-cable-compensation-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-perform-lcr-short-custom-cable-compensation-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates short custom cable compensation data for LCR measurements. To use this VI: You must physically configure your LCR circuit with a short to generate valid short custom cable compensation data. Set LCR Short Custom Cable Compensation Enabled to TRUE. When you call this function: The short com

### niDCPower Perform LCR Short Custom Cable Compensation VI

Generates short custom cable compensation data for LCR measurements.

To use this VI:

- You must physically configure your LCR circuit with a short to generate valid short custom cable compensation data.
- Set LCR Short Custom Cable Compensation Enabled to TRUE .

Note

- The short compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
- Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-perform-lcr-short-custom-cable-compensation-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Options for Short Custom Cable Compensation**

Custom cable compensation requires both open and short compensation data. You must generate your own open data, but you can choose among two options for providing short data.

- Use this VI if you want to generate short custom cable compensation data specific to your setup.
- You can also use a generic set of short cable compensation data for cable compensation. To use generic short cable compensation data, set LCR Short Custom Cable Compensation Enabled to FALSE and do not call this VI.

Parent topic:

LCR Compensation

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-property-node-vi.html language=enus -->
## TOPIC 00087: niDCPower Property Node VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-property-node-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets or gets properties of instruments or channels. For multi-channel sessions in which you want to configure subsets of channels differently, you must wire an Active Channel of an NI-DCPower property node. The Active Channel is listed first in the property node. Channel Based Properties Some NI-DCP

### niDCPower Property Node VI

Sets or gets properties of instruments or channels. For multi-channel sessions in which you want to configure subsets of channels differently, you must wire an Active Channel of an NI-DCPower property node. The Active Channel is listed first in the property node.

[IMAGE alt='image' src='loc_nidcpowerpropertynode_base.gif']

**Channel Based Properties**

Some NI-DCPower properties are channel based or apply to a specific channel. When a property is channel based, you must specify an active channel before setting or getting properties. In the following example, ch0 is configured to output voltage and ch1 is configured to output current. Both properties are channel based.

[IMAGE alt='image' src='loc_nidcpowerpropertynode_channel.gif']

**Non-Channel Based Properties**

To set or get NI-DCPower properties that are not channel based, you must not specify an active channel or must specify an active channel of "". The following example shows a property node used to get the value of the [Driver Vendor](/csh?context=nidcpower_dcpowerpropref_pnidcpower_drivervendor) property.

[IMAGE alt='image' src='loc_nidcpowerpropertynode_nonchannel.gif']

**Related topics:**

[Using Properties and Attributes](/csh?context=nidcpower_ni_dc_power_supplies_help_using_properties_and_attributes)

[niDCPower Properties](/csh?context=nidcpower_nidcpower_p)

[IMAGE alt='icon' src='nidcpower-property-node-vi.png']

#### Inputs/Outputs

| reference — reference passes a reference to your instrument session to the next VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. reference out — reference out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. Property — property are examples of properties you want to set (write) or get (read). |
| --- |

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-query-in-compliance-vi.html language=enus -->
## TOPIC 00088: niDCPower Query In Compliance VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-query-in-compliance-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-query-in-compliance-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the specified channel to determine if it is operating at the compliance limit. The compliance limit is the current limit when the Output Function property is set to DC Voltage, Pulse Voltage, Constant Resistance or Constant Power. If the output is operating at the compliance limit, the outpu

### niDCPower Query In Compliance VI

Queries the specified channel to determine if it is operating at the compliance limit.

The compliance limit is the current limit when the [Output Function](/csh?context=nidcpower_dcpowerpropref_pnidcpower_outputfunction) property is set to **DC Voltage**, **Pulse Voltage**, **Constant Resistance** or **Constant Power**. If the output is operating at the compliance limit, the output reaches the current limit before the desired voltage, resistance or power level.

The compliance limit is the voltage limit when the [Output Function](/csh?context=nidcpower_dcpowerpropref_pnidcpower_outputfunction) property is set to **DC Current** or **Pulse Current**. If the output is operating at the compliance limit, the output reaches the voltage limit before the desired current level.

Refer to the [Output Function](/csh?context=nidcpower_dcpowerpropref_pnidcpower_outputfunction) property for more information about the applicable properties to configure for each output function.

Note

[IMAGE alt='icon' src='nidcpower-query-in-compliance-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel to query. The compliance status can be queried for only one channel at a time. Specify the channel using the form PXI1Slot3/0, where PXI1Slot3 is the instrument resource name and 0 is the channel. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. in compliance? — in compliance? returns whether the specified channel is in compliance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Measure

Parent topic:

Query

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-query-latched-output-cutoff-state-vi.html language=enus -->
## TOPIC 00089: niDCPower Query Latched Output Cutoff State VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-query-latched-output-cutoff-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-query-latched-output-cutoff-state-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Discovers if an output cutoff limit was exceeded for the specified reason. When an output cutoff is engaged, the output of the channel(s) is disconnected. If a limit was exceeded, the state is latched until you clear it with niDCPower Clear Latched Output Cutoff State or niDCPower Reset With Channel

### niDCPower Query Latched Output Cutoff State VI

Discovers if an output cutoff limit was exceeded for the specified reason.

When an output cutoff is engaged, the output of the channel(s) is disconnected. If a limit was exceeded, the state is latched until you clear it with [niDCPower Clear Latched Output Cutoff State](nidcpower-clear-latched-output-cutoff-state-vi.html) or [niDCPower Reset With Channels](nidcpower-reset-with-channels-vi.html)

**reason** specifies the conditions for which an output is disconnected.

Note

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-query-latched-output-cutoff-state-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies to which channel(s) to apply this configuration value. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. reason — reason specifies which output cutoff conditions to query. All (-1) Any output cutoff condition was met. Voltage Output High (1) The output exceeded the high cutoff limit for voltage output. Voltage Output Low (2) The output fell below the low cutoff limit for voltage output. Current Measure High (4) The measured current exceeded the high cutoff limit for current output. Current Measure Low (8) The measured current fell below the low cutoff limit for current output. Voltage Change High (16) The voltage slew rate increased beyond the positive change cutoff for voltage output. Voltage Change Low (32) The voltage slew rate decreased beyond the negative change cutoff for voltage output. Current Change High (64) The current slew rate increased beyond the positive change cutoff for current output. Current Change Low (128) The current slew rate decreased beyond the negative change cutoff for current output. Current Saturated (512) The measured current saturates the current range. Voltage Measure High (1024) The measured voltage exceeded the high cutoff limit for voltage output. Voltage Measure Low (2048) The measured voltage fell below the low cutoff limit for voltage output. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. state — state specifies whether an output cutoff has engaged. true An output cutoff has engaged for the conditions in reason. false No output cutoff has engaged for the specified reason. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| All (-1) | Any output cutoff condition was met. |
| Voltage Output High (1) | The output exceeded the high cutoff limit for voltage output. |
| Voltage Output Low (2) | The output fell below the low cutoff limit for voltage output. |
| Current Measure High (4) | The measured current exceeded the high cutoff limit for current output. |
| Current Measure Low (8) | The measured current fell below the low cutoff limit for current output. |
| Voltage Change High (16) | The voltage slew rate increased beyond the positive change cutoff for voltage output. |
| Voltage Change Low (32) | The voltage slew rate decreased beyond the negative change cutoff for voltage output. |
| Current Change High (64) | The current slew rate increased beyond the positive change cutoff for current output. |
| Current Change Low (128) | The current slew rate decreased beyond the negative change cutoff for current output. |
| Current Saturated (512) | The measured current saturates the current range. |
| Voltage Measure High (1024) | The measured voltage exceeded the high cutoff limit for voltage output. |
| Voltage Measure Low (2048) | The measured voltage fell below the low cutoff limit for voltage output. |
| true | An output cutoff has engaged for the conditions in reason. |
| false | No output cutoff has engaged for the specified reason. |

Parent topic:

Query

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-query-max-current-limit-vi.html language=enus -->
## TOPIC 00090: niDCPower Query Max Current Limit VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-query-max-current-limit-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-query-max-current-limit-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the maximum current limit on a channel if the channel is set to the specified voltage level. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png channel name channel name specifies the channel to query. The maximum current li

### niDCPower Query Max Current Limit VI

Queries the maximum current limit on a channel if the channel is set to the specified
 **voltage level**.

[IMAGE alt='icon' src='nidcpower-query-max-current-limit-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel to query. The maximum current limit can be queried for only one channel at a time. Specify the channel using the form PXI1Slot3/0, where PXI1Slot3 is the instrument resource name and 0 is the channel. voltage level — voltage level specifies the voltage level to use when calculating the max current limit. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. max current limit — max current limit returns the maximum current limit that can be set with the specified voltage level. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Query

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-query-max-voltage-level-vi.html language=enus -->
## TOPIC 00091: niDCPower Query Max Voltage Level VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-query-max-voltage-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-query-max-voltage-level-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the maximum voltage level on a channel if the channel is set to the specified current limit. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png channel name channel name specifies the channel to query. The maximum voltage le

### niDCPower Query Max Voltage Level VI

Queries the maximum voltage level on a channel if the channel is set to the specified
 **current limit**.

[IMAGE alt='icon' src='nidcpower-query-max-voltage-level-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel to query. The maximum voltage level can be queried for only one channel at a time. Specify the channel using the form PXI1Slot3/0, where PXI1Slot3 is the instrument resource name and 0 is the channel. current limit — current limit specifies the current limit to use when calculating the max voltage level. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. max voltage level — max voltage level returns the maximum voltage level that can be set on a channel with the specified current limit. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Query

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-query-min-current-limit-vi.html language=enus -->
## TOPIC 00092: niDCPower Query Min Current Limit VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-query-min-current-limit-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-query-min-current-limit-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the minimum current limit on a channel if the channel is set to the specified voltage level. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png channel name channel name specifies the channel to query. The minimum current li

### niDCPower Query Min Current Limit VI

Queries the minimum current limit on a channel if the channel is set to the specified
 **voltage level**.

[IMAGE alt='icon' src='nidcpower-query-min-current-limit-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel to query. The minimum current limit can be queried for only one channel at a time. Specify the channel using the form PXI1Slot3/0, where PXI1Slot3 is the instrument resource name and 0 is the channel. voltage level — voltage level specifies the voltage level to use when calculating the min current limit. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. min current limit — min current limit returns the minimum current limit that can be set on a channel with the specified voltage level. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Query

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-query-output-state-vi.html language=enus -->
## TOPIC 00093: niDCPower Query Output State VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-query-output-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-query-output-state-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the specified channel to determine if the channel is currently in the state specified by output state. NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively. icon Inputs/Outputs civrn.png

### niDCPower Query Output State VI

Queries the specified channel to determine if the channel is currently in
 the state specified by **output state**.

Note

[IMAGE alt='icon' src='nidcpower-query-output-state-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel to query. The output state can be queried for only one channel at a time. Specify the channel using the form PXI1Slot3/0, where PXI1Slot3 is the instrument resource name and 0 is the channel. output state — output state specifies the output state of the channel that is being queried. The default value is Constant Voltage (0). Constant Voltage (0) The channel is maintaining a constant voltage at its output. Constant Current (1) The channel is maintaining a constant current at its output. Inhibited (1163) The channel is in the inhibited state. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. in state? — in state? returns whether the specified channel is in the specified output state. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Constant Voltage (0) | The channel is maintaining a constant voltage at its output. |
| Constant Current (1) | The channel is maintaining a constant current at its output. |
| Inhibited (1163) | The channel is in the inhibited state. |

Parent topic:

Measure

Parent topic:

Query

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-read-current-temperature-vi.html language=enus -->
## TOPIC 00094: niDCPower Read Current Temperature VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-read-current-temperature-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-read-current-temperature-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current onboard temperature, in degrees Celsius, of the device. This VI can only be used in a session initialized to a single instrument. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in (no error) err

### niDCPower Read Current Temperature VI

Returns the current onboard temperature, in degrees Celsius, of the device.

Note

[IMAGE alt='icon' src='nidcpower-read-current-temperature-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. temperature — temperature returns the onboard temperature, in degrees Celsius, of the device. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-device-vi.html language=enus -->
## TOPIC 00095: niDCPower Reset Device VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-device-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-device-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets all instruments in the session to a known state. This VI disables power generation, resets all properties for all instruments included in the session to their default values, clears errors such as overtemperature and unexpected loss of auxiliary power, commits the instrument properties, and l

### niDCPower Reset Device VI

Resets all instruments in the session to a known state. This VI disables power generation, resets
 all properties for all instruments included in the session to their default values, clears errors such as overtemperature and
 unexpected loss of auxiliary power, commits the instrument properties, and leaves the
 instrument(s) in the Uncommitted state. This VI also performs a hard reset on the instrument(s) and driver
 software. This VI has the same functionality as using reset in Measurement & Automation Explorer (MAX).

This VI opens the output relay on instruments that have an output relay.

Note

**Related topics:**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

[IMAGE alt='icon' src='nidcpower-reset-device-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this provides standard error in functionality. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out. The default is no error. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-interchange-check-vi.html language=enus -->
## TOPIC 00096: niDCPower Reset Interchange Check VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-interchange-check-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-interchange-check-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures interchangeability-checking algorithms to ignore all previous configuration options. This VI does not clear the interchangeability warnings from the list of previously recorded interchangeability warnings. If you want to guarantee that the niDCPower Get Next Interchange Warning VI only re

### niDCPower Reset Interchange Check VI

Configures interchangeability-checking algorithms to ignore all previous configuration options.

This VI does not clear the interchangeability warnings from the list of
 previously recorded interchangeability warnings. If you want to guarantee that the [niDCPower Get Next Interchange Warning](nidcpower-get-next-interchange-warning-vi.html) VI only returns those
 interchangeability warnings that are generated after calling this VI, clear the list of
 interchangeability warnings by repeatedly calling the [niDCPower Get Next Interchange Warning](nidcpower-get-next-interchange-warning-vi.html) VI until no interchangeability
 warnings are returned. If you are not interested in the content of those warnings, call the
 [niDCPower Clear Interchange Warnings](nidcpower-clear-interchange-warnings-vi.html) VI.

[IMAGE alt='icon' src='nidcpower-reset-interchange-check-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

When developing a complex test system that consists of multiple test modules, it is
 generally a good idea to design the test modules so that they can run in any order. To do
 so requires ensuring that each test module completely configures the state of each
 instrument it uses. If a particular test module does not completely configure the state of
 an instrument, the state depends on the configuration from a previously executed test
 module. If you execute the test modules in a different order, the behavior of the
 instrument and therefore the entire test module can change. This behavior change is
 generally instrument-specific and represents an interchangeability problem.

You can use the niDCPower Reset Interchange Check VI to test for such cases. After you
 use this VI, the interchangeability-checking algorithms in NI-DCPower ignore all previous
 configuration operations. By using this VI at the beginning of a test module, you can
 determine whether the test module has dependencies on the operation of previously executed
 test modules.

Parent topic:

Other IVI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-with-channels-vi.html language=enus -->
## TOPIC 00097: niDCPower Reset With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the specified channel(s) to a known state. This VI disables power generation, resets channel properties to their default values, commits the channel properties, and leaves the channel(s) in the Uncommitted state. You can use this VI to clear certain errors in less time than using the niDCPowe

### niDCPower Reset With Channels VI

Resets the specified channel(s) to a known state. This VI disables power generation, resets channel
 properties to their default values, commits the channel properties, and leaves the channel(s) in the Uncommitted state. You can use this VI to clear certain errors in less time than using the niDCPower Reset Device VI.

**Related topics:**

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

[IMAGE alt='icon' src='nidcpower-reset-with-channels-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this provides standard error in functionality. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out. The default is no error. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-with-defaults-vi.html language=enus -->
## TOPIC 00098: niDCPower Reset with Defaults VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-with-defaults-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-reset-with-defaults-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets all channels in the session to a known state. This VI disables power generation, resets session properties to their default values, commits the session properties, and leaves the session in the Running state. In addition to exhibiting the behavior of the niDCPower Reset With Channels VI, this

### niDCPower Reset with Defaults VI

Resets all channels in the session to a known state. This VI disables power generation, resets
 session properties to their default values, commits the session properties, and leaves the session in the [Running](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates) state. In addition to exhibiting the behavior of the [niDCPower Reset With Channels](/csh?topicname=nidcpower-reset-with-channels-vi.html) VI, this VI can assign user-defined default values for configurable properties from the IVI configuration.

[IMAGE alt='icon' src='nidcpower-reset-with-defaults-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this provides standard error in functionality. This node runs normally even if an error occurred previously. If an error occurred before this node runs, the node passes the error in value to error out, and no errors that occur while this node runs are recorded. If an error occurs while this node runs and no error occurred previously, the node sets its own error status in error out. The default is no error. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Other IVI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-revision-query-vi.html language=enus -->
## TOPIC 00099: niDCPower Revision Query VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-revision-query-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-revision-query-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision information of NI-DCPower and the device firmware. In multi-instrument sessions, this VI returns an error if any instruments have different firmware revisions. In this case, instead of using this VI, read the Firmware Revision property for the single instrument you specify with

### niDCPower Revision Query VI

Returns the revision information of NI-DCPower and the device firmware.

In multi-instrument sessions, this VI returns an error if any instruments have different firmware revisions. In this case, instead of using this VI, read the [Firmware Revision](/csh?context=nidcpower_dcpowerpropref_pnidcpower_firmwarerevision) property for the single instrument you specify with the Active Channel property.

[IMAGE alt='icon' src='nidcpower-revision-query-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. firmware rev — firmware rev returns the firmware revision information for the device. instr driver rev — instr driver rev returns the driver revision information for NI-DCPower. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Other IVI

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-self-test-vi.html language=enus -->
## TOPIC 00100: niDCPower Self Test VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-self-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-self-test-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the device self-test routine and returns the test result(s). Calling this VI implicitly calls the niDCPower Reset With Channels VI. When calling niDCPower Self Test with any niDCPower PXIe device that has more than one channel, specify all channels of your PXIe device with the resource name

### niDCPower Self Test VI

Performs the device self-test routine and returns the test result(s). Calling this VI
 implicitly calls the niDCPower Reset With Channels VI.

When calling niDCPower Self Test with any niDCPower PXIe device that has more than one channel, specify all channels of your PXIe device with the **resource name** input of niDCPower [niDCPower Initialize With Independent Channels](nidcpower-initialize-with-independent-channels-vi.html). You cannot self test a subset of channels on these devices.

[IMAGE alt='icon' src='nidcpower-self-test-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. self test result — self test result returns the value result from the device self-test. 0 indicates success. Other values indicate the error code corresponding to the self test result message. self test message — self test message returns the self test result message. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/nidcpower-send-software-edge-trigger-with-channels-vi.html language=enus -->
## TOPIC 00101: niDCPower Send Software Edge Trigger With Channels VI

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/nidcpower-send-software-edge-trigger-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/nidcpower-send-software-edge-trigger-with-channels-vi.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asserts the specified trigger. This VI can override an external edge trigger. This VI is not supported by all devices. Refer to Supported VIs by Device for information about supported devices. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument sessio

### niDCPower Send Software Edge Trigger With Channels VI

Asserts the specified trigger. This VI can override an external edge trigger.

Note

Supported VIs by Device

[IMAGE alt='icon' src='nidcpower-send-software-edge-trigger-with-channels-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel name — channel name specifies the channel(s) to use. Specify the channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are instrument resource names and 0, 2, and 3 are channels. If you do not wire this parameter, all channels in the session are used. signal — signal specifies which trigger to override. Start Trigger (1034) Overrides the Start trigger. Source Trigger (1035) Overrides the Source trigger. Measure Trigger (1036) Overrides the Measure trigger. Sequence Advance Trigger (1037) Overrides the Sequence Advance trigger. Pulse Trigger (1053) Overrides the Pulse trigger. Shutdown Trigger (1118) Overrides the Shutdown trigger. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes the handle used to identify the session in all subsequent NI-DCPower VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Start Trigger (1034) | Overrides the Start trigger. |
| Source Trigger (1035) | Overrides the Source trigger. |
| Measure Trigger (1036) | Overrides the Measure trigger. |
| Sequence Advance Trigger (1037) | Overrides the Sequence Advance trigger. |
| Pulse Trigger (1053) | Overrides the Pulse trigger. |
| Shutdown Trigger (1118) | Overrides the Shutdown trigger. |

Parent topic:

Triggers and Events

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/standard-functionality-for-error-out-parameters.html language=enus -->
## TOPIC 00102: Using the Standard Functionality for error out Parameters

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/standard-functionality-for-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/standard-functionality-for-error-out-parameters.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard err

### Using the Standard Functionality for error out Parameters

Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

Standard error out functionality is as follows:

|  | error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

error out contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or during the running of this node or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/supported-vis-4110.html language=enus -->
## TOPIC 00103: VIs Supported by the PXI-4110

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/supported-vis-4110.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/supported-vis-4110.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table shows which VIs are supported by NI-DCPower devices. A indicates that the device supports the VI; an indicates that the device does not support the VI. VI PXI-4110 niDCPower Abort With Channels VI^3 niDCPower Cal Adjust AC Flatness VI niDCPower Cal Adjust Current Limit VI niDCPow

### VIs Supported by the PXI-4110

The following table shows which VIs are supported by NI-DCPower devices. A [IMAGE alt='image' src='../../../images/checkmark.gif'] indicates that the device supports the VI; an [IMAGE alt='image' src='../../../images/xmark.gif'] indicates that the device does not support the VI.

| VI | PXI-4110 |
| --- | --- |
| niDCPower Abort With Channels VI[3] |  |
| niDCPower Cal Adjust AC Flatness VI |  |
| niDCPower Cal Adjust Current Limit VI |  |
| niDCPower Cal Adjust Current Measurement VI |  |
| niDCPower Cal Adjust Internal Reference VI |  |
| niDCPower Cal Adjust Output Resistance VI |  |
| niDCPower Cal Adjust Residual Current Offset VI |  |
| niDCPower Cal Adjust Residual Voltage Offset VI |  |
| niDCPower Cal Adjust Voltage Level VI |  |
| niDCPower Cal Adjust Voltage Measurement VI |  |
| niDCPower Cal Begin AC Flatness VI |  |
| niDCPower Cal Config AC Flatness VI |  |
| niDCPower Cal End AC Flatness VI |  |
| niDCPower Cal Self Calibrate VI |  |
| niDCPower Change Ext Cal Password VI |  |
| niDCPower Clear Interchange Warnings VI |  |
| niDCPower Clear Latched Output Cutoff State VI |  |
| niDCPower Close VI |  |
| niDCPower Close External Calibration VI |  |
| niDCPower Commit With Channels VI[3] |  |
| niDCPower Configure Aperture Time VI |  |
| niDCPower Configure Auto Zero VI |  |
| niDCPower Configure Current Level VI |  |
| niDCPower Configure Current Level Range VI |  |
| niDCPower Configure Current Limit VI |  |
| niDCPower Configure Current Limit Range VI |  |
| niDCPower Configure LCR Compensation VI |  |
| niDCPower Configure LCR Custom Cable Compensation VI |  |
| niDCPower Configure Output Enabled VI |  |
| niDCPower Configure Output Function VI |  |
| niDCPower Configure Output Resistance VI |  |
| niDCPower Configure Power Line Frequency VI |  |
| niDCPower Configure Pulse Bias Current Level VI |  |
| niDCPower Configure Pulse Bias Current Limit VI |  |
| niDCPower Configure Pulse Bias Voltage Level VI |  |
| niDCPower Configure Pulse Bias Voltage Limit VI |  |
| niDCPower Configure Pulse Current Level VI |  |
| niDCPower Configure Pulse Current Level Range VI |  |
| niDCPower Configure Pulse Current Limit VI |  |
| niDCPower Configure Pulse Current Limit Range VI |  |
| niDCPower Configure Pulse Voltage Level VI |  |
| niDCPower Configure Pulse Voltage Level Range VI |  |
| niDCPower Configure Pulse Voltage Limit VI |  |
| niDCPower Configure Pulse Voltage Limit Range VI |  |
| niDCPower Configure Sense VI |  |
| niDCPower Configure Source Mode With Channels VI[3] |  |
| niDCPower Configure Trigger With Channels (Poly) VI[3] |  |
| niDCPower Configure Voltage Level VI |  |
| niDCPower Configure Voltage Level Range VI |  |
| niDCPower Configure Voltage Limit VI |  |
| niDCPower Configure Voltage Limit Range VI |  |
| niDCPower Connect Internal Reference VI |  |
| niDCPower Create Advanced Sequence With Channels VI[3] |  |
| niDCPower Create Advanced Sequence Step With Channels VI[3] |  |
| niDCPower Create Advanced Sequence Commit Step With Channels VI |  |
| niDCPower Delete Advanced Sequence With Channels VI[3] |  |
| niDCPower Disable VI |  |
| niDCPower Export Attribute Configuration (Poly) VI |  |
| niDCPower Export Signal With Channels VI[3] |  |
| niDCPower Fetch Multiple VI |  |
| niDCPower Fetch Multiple LCR VI |  |
| niDCPower Get Cal User Defined Info VI |  |
| niDCPower Get Cal User Defined Info Max Size VI |  |
| niDCPower Get Channel Name (Poly) VI |  |
| niDCPower Get Ext Cal Last Date And Time VI |  |
| niDCPower Get Ext Cal Last Temp VI |  |
| niDCPower Get Ext Cal Recommended Interval VI |  |
| niDCPower Get LCR Compensation Last Date And Time VI |  |
| niDCPower Get LCR Compensation Data VI |  |
| niDCPower Get LCR Custom Cable Compensation Data VI |  |
| niDCPower Get Next Coercion Record VI |  |
| niDCPower Get Next Interchange Warning VI |  |
| niDCPower Get Self Cal Last Date And Time VI |  |
| niDCPower Get Self Cal Last Temp VI |  |
| niDCPower Import Attribute Configuration (Poly) VI |  |
| niDCPower Initialize External Calibration VI |  |
| niDCPower Initialize With Independent Channels VI[2] |  |
| niDCPower Initiate With Channels VI[3] |  |
| niDCPower Measure VI |  |
| niDCPower Measure Multiple VI |  |
| niDCPower Measure Multiple LCR VI |  |
| niDCPower Perform LCR Load Compensation VI |  |
| niDCPower Perform LCR Open Compensation VI |  |
| niDCPower Perform LCR Open Custom Cable Compensation VI |  |
| niDCPower Perform LCR Short Compensation VI |  |
| niDCPower Perform LCR Short Custom Cable Compensation VI |  |
| niDCPower Property Node VI |  |
| niDCPower Query In Compliance VI |  |
| niDCPower Query Latched Output Cutoff State VI |  |
| niDCPower Query Max Current Limit VI |  |
| niDCPower Query Max Voltage Level VI |  |
| niDCPower Query Min Current Limit VI |  |
| niDCPower Query Output State VI |  |
| niDCPower Read Current Temperature VI |  |
| niDCPower Reset With Channels VI[3] |  |
| niDCPower Reset Device VI |  |
| niDCPower Reset Interchange Check VI |  |
| niDCPower Reset with Defaults VI |  |
| niDCPower Revision Query VI |  |
| niDCPower Self Test VI |  |
| niDCPower Send Software Edge Trigger With Channels VI[3] |  |
| niDCPower Set Cal User Defined Info VI |  |
| niDCPower Set Sequence VI |  |
| niDCPower Wait For Event With Channels VI[3] | [1] |

1

Source Complete event only.

2

The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

3

The deprecated, not-channel-based version of this VI is supported but not recommended.

Parent topic:

Supported VIs by Device

<sup>1</sup> Source Complete event only.

<sup>2</sup> The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

<sup>3</sup> The deprecated, not-channel-based version of this VI is supported but not recommended.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/supported-vis-4112-4113.html language=enus -->
## TOPIC 00104: VIs Supported by the PXIe-4112/4113

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/supported-vis-4112-4113.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/supported-vis-4112-4113.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table shows which VIs are supported by NI-DCPower devices. A indicates that the device supports the VI; an indicates that the device does not support the VI. VI PXIe-4112/4113 niDCPower Abort With Channels VI^2 niDCPower Cal Adjust AC Flatness VI niDCPower Cal Adjust Current Limit VI n

### VIs Supported by the PXIe-4112/4113

The following table shows which VIs are supported by NI-DCPower devices. A [IMAGE alt='image' src='../../../images/checkmark.gif'] indicates that the device supports the VI; an [IMAGE alt='image' src='../../../images/xmark.gif'] indicates that the device does not support the VI.

| VI | PXIe-4112/4113 |
| --- | --- |
| niDCPower Abort With Channels VI[2] |  |
| niDCPower Cal Adjust AC Flatness VI |  |
| niDCPower Cal Adjust Current Limit VI |  |
| niDCPower Cal Adjust Current Measurement VI |  |
| niDCPower Cal Adjust Internal Reference VI |  |
| niDCPower Cal Adjust Output Resistance VI |  |
| niDCPower Cal Adjust Residual Current Offset VI |  |
| niDCPower Cal Adjust Residual Voltage Offset VI |  |
| niDCPower Cal Adjust Voltage Level VI |  |
| niDCPower Cal Adjust Voltage Measurement VI |  |
| niDCPower Cal Begin AC Flatness VI |  |
| niDCPower Cal Config AC Flatness VI |  |
| niDCPower Cal End AC Flatness VI |  |
| niDCPower Cal Self Calibrate VI |  |
| niDCPower Change Ext Cal Password VI |  |
| niDCPower Clear Interchange Warnings VI |  |
| niDCPower Clear Latched Output Cutoff State VI |  |
| niDCPower Close VI |  |
| niDCPower Close External Calibration VI |  |
| niDCPower Commit With Channels VI[2] |  |
| niDCPower Configure Aperture Time VI |  |
| niDCPower Configure Auto Zero VI |  |
| niDCPower Configure Current Level VI |  |
| niDCPower Configure Current Level Range VI |  |
| niDCPower Configure Current Limit VI |  |
| niDCPower Configure Current Limit Range VI |  |
| niDCPower Configure LCR Compensation VI |  |
| niDCPower Configure LCR Custom Cable Compensation VI |  |
| niDCPower Configure Output Enabled VI |  |
| niDCPower Configure Output Function VI |  |
| niDCPower Configure Output Resistance VI |  |
| niDCPower Configure Power Line Frequency VI |  |
| niDCPower Configure Pulse Bias Current Level VI |  |
| niDCPower Configure Pulse Bias Current Limit VI |  |
| niDCPower Configure Pulse Bias Voltage Level VI |  |
| niDCPower Configure Pulse Bias Voltage Limit VI |  |
| niDCPower Configure Pulse Current Level VI |  |
| niDCPower Configure Pulse Current Level Range VI |  |
| niDCPower Configure Pulse Current Limit VI |  |
| niDCPower Configure Pulse Current Limit Range VI |  |
| niDCPower Configure Pulse Voltage Level VI |  |
| niDCPower Configure Pulse Voltage Level Range VI |  |
| niDCPower Configure Pulse Voltage Limit VI |  |
| niDCPower Configure Pulse Voltage Limit Range VI |  |
| niDCPower Configure Sense VI |  |
| niDCPower Configure Source Mode With Channels VI[2] |  |
| niDCPower Configure Trigger With Channels (Poly) VI[2] |  |
| niDCPower Configure Voltage Level VI |  |
| niDCPower Configure Voltage Level Range VI |  |
| niDCPower Configure Voltage Limit VI |  |
| niDCPower Configure Voltage Limit Range VI |  |
| niDCPower Connect Internal Reference VI |  |
| niDCPower Create Advanced Sequence With Channels VI[2] |  |
| niDCPower Create Advanced Sequence Step With Channels VI[2] |  |
| niDCPower Create Advanced Sequence Commit Step With Channels VI |  |
| niDCPower Delete Advanced Sequence With Channels VI[2] |  |
| niDCPower Disable VI |  |
| niDCPower Export Attribute Configuration (Poly) VI |  |
| niDCPower Export Signal With Channels VI[2] |  |
| niDCPower Fetch Multiple VI |  |
| niDCPower Fetch Multiple LCR VI |  |
| niDCPower Get Cal User Defined Info VI |  |
| niDCPower Get Cal User Defined Info Max Size VI |  |
| niDCPower Get Channel Name (Poly) VI |  |
| niDCPower Get Ext Cal Last Date And Time VI |  |
| niDCPower Get Ext Cal Last Temp VI |  |
| niDCPower Get Ext Cal Recommended Interval VI |  |
| niDCPower Get LCR Compensation Last Date And Time VI |  |
| niDCPower Get LCR Compensation Data VI |  |
| niDCPower Get LCR Custom Cable Compensation Data VI |  |
| niDCPower Get Next Coercion Record VI |  |
| niDCPower Get Next Interchange Warning VI |  |
| niDCPower Get Self Cal Last Date And Time VI |  |
| niDCPower Get Self Cal Last Temp VI |  |
| niDCPower Import Attribute Configuration (Poly) VI |  |
| niDCPower Initialize External Calibration VI |  |
| niDCPower Initialize With Independent Channels VI[1] |  |
| niDCPower Initiate With Channels VI[2] |  |
| niDCPower Measure VI |  |
| niDCPower Measure Multiple VI |  |
| niDCPower Measure Multiple LCR VI |  |
| niDCPower Perform LCR Load Compensation VI |  |
| niDCPower Perform LCR Open Compensation VI |  |
| niDCPower Perform LCR Open Custom Cable Compensation VI |  |
| niDCPower Perform LCR Short Compensation VI |  |
| niDCPower Perform LCR Short Custom Cable Compensation VI |  |
| niDCPower Property Node VI |  |
| niDCPower Query In Compliance VI |  |
| niDCPower Query Latched Output Cutoff State VI |  |
| niDCPower Query Max Current Limit VI |  |
| niDCPower Query Max Voltage Level VI |  |
| niDCPower Query Min Current Limit VI |  |
| niDCPower Query Output State VI |  |
| niDCPower Read Current Temperature VI |  |
| niDCPower Reset With Channels VI[2] |  |
| niDCPower Reset Device VI |  |
| niDCPower Reset Interchange Check VI |  |
| niDCPower Reset with Defaults VI[2] |  |
| niDCPower Revision Query VI |  |
| niDCPower Self Test VI |  |
| niDCPower Send Software Edge Trigger With Channels VI[2] |  |
| niDCPower Set Cal User Defined Info VI |  |
| niDCPower Set Sequence VI |  |
| niDCPower Wait For Event With Channels VI[2] |  |

1

The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

2

The deprecated, not-channel-based version of this VI is supported but not recommended.

Parent topic:

Supported VIs by Device

<sup>1</sup> The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

<sup>2</sup> The deprecated, not-channel-based version of this VI is supported but not recommended.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/supported-vis-4130.html language=enus -->
## TOPIC 00105: VIs Supported by the PXI-4130

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/supported-vis-4130.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/supported-vis-4130.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table shows which VIs are supported by NI-DCPower devices. A indicates that the device supports the VI; an indicates that the device does not support the VI. VI PXI-4130 niDCPower Abort With Channels VI^3 niDCPower Cal Adjust AC Flatness VI niDCPower Cal Adjust Current Limit VI niDCPow

### VIs Supported by the PXI-4130

The following table shows which VIs are supported by NI-DCPower devices. A [IMAGE alt='image' src='../../../images/checkmark.gif'] indicates that the device supports the VI; an [IMAGE alt='image' src='../../../images/xmark.gif'] indicates that the device does not support the VI.

| VI | PXI-4130 |
| --- | --- |
| niDCPower Abort With Channels VI[3] |  |
| niDCPower Cal Adjust AC Flatness VI |  |
| niDCPower Cal Adjust Current Limit VI |  |
| niDCPower Cal Adjust Current Measurement VI |  |
| niDCPower Cal Adjust Internal Reference VI |  |
| niDCPower Cal Adjust Output Resistance VI |  |
| niDCPower Cal Adjust Residual Current Offset VI |  |
| niDCPower Cal Adjust Residual Voltage Offset VI |  |
| niDCPower Cal Adjust Voltage Level VI |  |
| niDCPower Cal Adjust Voltage Measurement VI |  |
| niDCPower Cal Begin AC Flatness VI |  |
| niDCPower Cal Config AC Flatness VI |  |
| niDCPower Cal End AC Flatness VI |  |
| niDCPower Cal Self Calibrate VI |  |
| niDCPower Change Ext Cal Password VI |  |
| niDCPower Clear Interchange Warnings VI |  |
| niDCPower Clear Latched Output Cutoff State VI |  |
| niDCPower Close VI |  |
| niDCPower Close External Calibration VI |  |
| niDCPower Commit With Channels VI[3] |  |
| niDCPower Configure Aperture Time VI |  |
| niDCPower Configure Auto Zero VI |  |
| niDCPower Configure Current Level VI |  |
| niDCPower Configure Current Level Range VI |  |
| niDCPower Configure Current Limit VI |  |
| niDCPower Configure Current Limit Range VI |  |
| niDCPower Configure LCR Compensation VI |  |
| niDCPower Configure LCR Custom Cable Compensation VI |  |
| niDCPower Configure Output Enabled VI |  |
| niDCPower Configure Output Function VI |  |
| niDCPower Configure Output Resistance VI |  |
| niDCPower Configure Power Line Frequency VI |  |
| niDCPower Configure Pulse Bias Current Level VI |  |
| niDCPower Configure Pulse Bias Current Limit VI |  |
| niDCPower Configure Pulse Bias Voltage Level VI |  |
| niDCPower Configure Pulse Bias Voltage Limit VI |  |
| niDCPower Configure Pulse Current Level VI |  |
| niDCPower Configure Pulse Current Level Range VI |  |
| niDCPower Configure Pulse Current Limit VI |  |
| niDCPower Configure Pulse Current Limit Range VI |  |
| niDCPower Configure Pulse Voltage Level VI |  |
| niDCPower Configure Pulse Voltage Level Range VI |  |
| niDCPower Configure Pulse Voltage Limit VI |  |
| niDCPower Configure Pulse Voltage Limit Range VI |  |
| niDCPower Configure Sense VI |  |
| niDCPower Configure Source Mode With Channels VI[3] |  |
| niDCPower Configure Trigger With Channels (Poly) VI[3] |  |
| niDCPower Configure Voltage Level VI |  |
| niDCPower Configure Voltage Level Range VI |  |
| niDCPower Configure Voltage Limit VI |  |
| niDCPower Configure Voltage Limit Range VI |  |
| niDCPower Connect Internal Reference VI |  |
| niDCPower Create Advanced Sequence With Channels VI[3] |  |
| niDCPower Create Advanced Sequence Step With Channels VI[3] |  |
| niDCPower Create Advanced Sequence Commit Step With Channels VI |  |
| niDCPower Delete Advanced Sequence With Channels VI[3] |  |
| niDCPower Disable VI |  |
| niDCPower Export Attribute Configuration (Poly) VI |  |
| niDCPower Export Signal With Channels VI[3] |  |
| niDCPower Fetch Multiple VI |  |
| niDCPower Fetch Multiple LCR VI |  |
| niDCPower Get Cal User Defined Info VI |  |
| niDCPower Get Cal User Defined Info Max Size VI |  |
| niDCPower Get Channel Name (Poly) VI |  |
| niDCPower Get Ext Cal Last Date And Time VI |  |
| niDCPower Get Ext Cal Last Temp VI |  |
| niDCPower Get Ext Cal Recommended Interval VI |  |
| niDCPower Get LCR Compensation Last Date And Time VI |  |
| niDCPower Get LCR Compensation Data VI |  |
| niDCPower Get LCR Custom Cable Compensation Data VI |  |
| niDCPower Get Next Coercion Record VI |  |
| niDCPower Get Next Interchange Warning VI |  |
| niDCPower Get Self Cal Last Date And Time VI |  |
| niDCPower Get Self Cal Last Temp VI |  |
| niDCPower Import Attribute Configuration (Poly) VI |  |
| niDCPower Initialize External Calibration VI |  |
| niDCPower Initialize With Independent Channels VI[2] |  |
| niDCPower Initiate With Channels VI[3] |  |
| niDCPower Measure VI |  |
| niDCPower Measure Multiple VI |  |
| niDCPower Measure Multiple LCR VI |  |
| niDCPower Perform LCR Load Compensation VI |  |
| niDCPower Perform LCR Open Compensation VI |  |
| niDCPower Perform LCR Open Custom Cable Compensation VI |  |
| niDCPower Perform LCR Short Compensation VI |  |
| niDCPower Perform LCR Short Custom Cable Compensation VI |  |
| niDCPower Property Node VI |  |
| niDCPower Query In Compliance VI |  |
| niDCPower Query Latched Output Cutoff State VI |  |
| niDCPower Query Max Current Limit VI |  |
| niDCPower Query Max Voltage Level VI |  |
| niDCPower Query Min Current Limit VI |  |
| niDCPower Query Output State VI |  |
| niDCPower Read Current Temperature VI |  |
| niDCPower Reset With Channels VI[3] |  |
| niDCPower Reset Device VI |  |
| niDCPower Reset Interchange Check VI |  |
| niDCPower Reset with Defaults VI |  |
| niDCPower Revision Query VI |  |
| niDCPower Self Test VI |  |
| niDCPower Send Software Edge Trigger With Channels VI[3] |  |
| niDCPower Set Cal User Defined Info VI |  |
| niDCPower Set Sequence VI |  |
| niDCPower Wait For Event With Channels VI[3] | [1] |

1

Source Complete event only.

2

The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

3

The deprecated, not-channel-based version of this VI is supported but not recommended.

Parent topic:

Supported VIs by Device

<sup>1</sup> Source Complete event only.

<sup>2</sup> The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

<sup>3</sup> The deprecated, not-channel-based version of this VI is supported but not recommended.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/supported-vis-4138-4139.html language=enus -->
## TOPIC 00106: VIs Supported by the PXIe-4138/4139

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/supported-vis-4138-4139.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/supported-vis-4138-4139.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table shows which VIs are supported by NI-DCPower devices. A indicates that the device supports the VI; an indicates that the device does not support the VI. VI PXIe-4138/4139 niDCPower Abort With Channels VI^3 niDCPower Cal Adjust AC Flatness VI niDCPower Cal Adjust Current Limit VI n

### VIs Supported by the PXIe-4138/4139

The following table shows which VIs are supported by NI-DCPower devices. A [IMAGE alt='image' src='../../../images/checkmark.gif'] indicates that the device supports the VI; an [IMAGE alt='image' src='../../../images/xmark.gif'] indicates that the device does not support the VI.

| VI | PXIe-4138/4139 |
| --- | --- |
| niDCPower Abort With Channels VI[3] |  |
| niDCPower Cal Adjust AC Flatness VI |  |
| niDCPower Cal Adjust Current Limit VI |  |
| niDCPower Cal Adjust Current Measurement VI |  |
| niDCPower Cal Adjust Internal Reference VI |  |
| niDCPower Cal Adjust Output Resistance VI |  |
| niDCPower Cal Adjust Residual Current Offset VI |  |
| niDCPower Cal Adjust Residual Voltage Offset VI |  |
| niDCPower Cal Adjust Voltage Level VI |  |
| niDCPower Cal Adjust Voltage Measurement VI |  |
| niDCPower Cal Begin AC Flatness VI |  |
| niDCPower Cal Config AC Flatness VI |  |
| niDCPower Cal End AC Flatness VI |  |
| niDCPower Cal Self Calibrate VI |  |
| niDCPower Change Ext Cal Password VI |  |
| niDCPower Clear Interchange Warnings VI |  |
| niDCPower Clear Latched Output Cutoff State VI |  |
| niDCPower Close VI |  |
| niDCPower Close External Calibration VI |  |
| niDCPower Commit With Channels VI[3] |  |
| niDCPower Configure Aperture Time VI |  |
| niDCPower Configure Auto Zero VI |  |
| niDCPower Configure Current Level VI |  |
| niDCPower Configure Current Level Range VI |  |
| niDCPower Configure Current Limit VI |  |
| niDCPower Configure Current Limit Range VI |  |
| niDCPower Configure LCR Compensation VI |  |
| niDCPower Configure LCR Custom Cable Compensation VI |  |
| niDCPower Configure Output Enabled VI |  |
| niDCPower Configure Output Function VI |  |
| niDCPower Configure Output Resistance VI | [1] |
| niDCPower Configure Power Line Frequency VI |  |
| niDCPower Configure Pulse Bias Current Level VI |  |
| niDCPower Configure Pulse Bias Current Limit VI |  |
| niDCPower Configure Pulse Bias Voltage Level VI |  |
| niDCPower Configure Pulse Bias Voltage Limit VI |  |
| niDCPower Configure Pulse Current Level VI |  |
| niDCPower Configure Pulse Current Level Range VI |  |
| niDCPower Configure Pulse Current Limit VI |  |
| niDCPower Configure Pulse Current Limit Range VI |  |
| niDCPower Configure Pulse Voltage Level VI |  |
| niDCPower Configure Pulse Voltage Level Range VI |  |
| niDCPower Configure Pulse Voltage Limit VI |  |
| niDCPower Configure Pulse Voltage Limit Range VI |  |
| niDCPower Configure Sense VI |  |
| niDCPower Configure Source Mode With Channels VI[3] |  |
| niDCPower Configure Trigger With Channels (Poly) VI[3] |  |
| niDCPower Configure Voltage Level VI |  |
| niDCPower Configure Voltage Level Range VI |  |
| niDCPower Configure Voltage Limit VI |  |
| niDCPower Configure Voltage Limit Range VI |  |
| niDCPower Connect Internal Reference VI |  |
| niDCPower Create Advanced Sequence With Channels VI[3] |  |
| niDCPower Create Advanced Sequence Commit Step With Channels VI |  |
| niDCPower Create Advanced Sequence Step With Channels VI[3] |  |
| niDCPower Delete Advanced Sequence With Channels VI[3] |  |
| niDCPower Disable VI |  |
| niDCPower Export Attribute Configuration (Poly) VI |  |
| niDCPower Export Signal With Channels VI[3] |  |
| niDCPower Fetch Multiple VI |  |
| niDCPower Fetch Multiple LCR VI |  |
| niDCPower Get Cal User Defined Info VI |  |
| niDCPower Get Cal User Defined Info Max Size VI |  |
| niDCPower Get Channel Name (Poly) VI |  |
| niDCPower Get Ext Cal Last Date And Time VI |  |
| niDCPower Get Ext Cal Last Temp VI |  |
| niDCPower Get Ext Cal Recommended Interval VI |  |
| niDCPower Get LCR Compensation Last Date And Time VI |  |
| niDCPower Get LCR Compensation Data VI |  |
| niDCPower Get LCR Custom Cable Compensation Data VI |  |
| niDCPower Get Next Coercion Record VI |  |
| niDCPower Get Next Interchange Warning VI |  |
| niDCPower Get Self Cal Last Date And Time VI |  |
| niDCPower Get Self Cal Last Temp VI |  |
| niDCPower Import Attribute Configuration (Poly) VI |  |
| niDCPower Initialize External Calibration VI |  |
| niDCPower Initialize With Independent Channels VI[2] |  |
| niDCPower Initiate With Channels VI[3] |  |
| niDCPower Measure VI |  |
| niDCPower Measure Multiple VI |  |
| niDCPower Measure Multiple LCR VI |  |
| niDCPower Perform LCR Load Compensation VI |  |
| niDCPower Perform LCR Open Compensation VI |  |
| niDCPower Perform LCR Open Custom Cable Compensation VI |  |
| niDCPower Perform LCR Short Compensation VI |  |
| niDCPower Perform LCR Short Custom Cable Compensation VI |  |
| niDCPower Property Node VI |  |
| niDCPower Query In Compliance VI |  |
| niDCPower Query Latched Output Cutoff State VI |  |
| niDCPower Query Max Current Limit VI |  |
| niDCPower Query Max Voltage Level VI |  |
| niDCPower Query Min Current Limit VI |  |
| niDCPower Query Output State VI |  |
| niDCPower Read Current Temperature VI |  |
| niDCPower Reset With Channels VI[3] |  |
| niDCPower Reset Device VI |  |
| niDCPower Reset Interchange Check VI |  |
| niDCPower Reset with Defaults VI |  |
| niDCPower Revision Query VI |  |
| niDCPower Self Test VI |  |
| niDCPower Send Software Edge Trigger With Channels VI[3] |  |
| niDCPower Set Cal User Defined Info VI |  |
| niDCPower Set Sequence VI |  |
| niDCPower Wait For Event With Channels VI[3] |  |

1

PXIe-4137/4139/4141/4143/4145 only.

2

The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

3

The deprecated, not-channel-based version of this VI is supported but not recommended.

Parent topic:

Supported VIs by Device

<sup>1</sup> PXIe-4137/4139/4141/4143/4145 only.

<sup>2</sup> The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

<sup>3</sup> The deprecated, not-channel-based version of this VI is supported but not recommended.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/supported-vis-4147.html language=enus -->
## TOPIC 00107: VIs Supported by the PXIe-4147

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/supported-vis-4147.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/supported-vis-4147.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table shows which VIs are supported by NI-DCPower devices. A indicates that the device supports the VI; an indicates that the device does not support the VI. VI PXIe-4147 niDCPower Abort With Channels VI niDCPower Cal Adjust AC Flatness VI niDCPower Cal Adjust Current Limit VI niDCPowe

### VIs Supported by the PXIe-4147

The following table shows which VIs are supported by NI-DCPower devices. A [IMAGE alt='image' src='../../../images/checkmark.gif'] indicates that the device supports the VI; an [IMAGE alt='image' src='../../../images/xmark.gif'] indicates that the device does not support the VI.

| VI | PXIe-4147 |
| --- | --- |
| niDCPower Abort With Channels VI |  |
| niDCPower Cal Adjust AC Flatness VI |  |
| niDCPower Cal Adjust Current Limit VI |  |
| niDCPower Cal Adjust Current Measurement VI |  |
| niDCPower Cal Adjust Internal Reference VI |  |
| niDCPower Cal Adjust Output Resistance VI |  |
| niDCPower Cal Adjust Residual Current Offset VI |  |
| niDCPower Cal Adjust Residual Voltage Offset VI |  |
| niDCPower Cal Adjust Voltage Level VI |  |
| niDCPower Cal Adjust Voltage Measurement VI |  |
| niDCPower Cal Begin AC Flatness VI |  |
| niDCPower Cal Config AC Flatness VI |  |
| niDCPower Cal End AC Flatness VI |  |
| niDCPower Cal Self Calibrate VI |  |
| niDCPower Change Ext Cal Password VI |  |
| niDCPower Clear Interchange Warnings VI |  |
| niDCPower Clear Latched Output Cutoff State VI |  |
| niDCPower Close VI |  |
| niDCPower Close External Calibration VI |  |
| niDCPower Commit With Channels VI |  |
| niDCPower Configure Aperture Time VI |  |
| niDCPower Configure Auto Zero VI |  |
| niDCPower Configure Current Level VI |  |
| niDCPower Configure Current Level Range VI |  |
| niDCPower Configure Current Limit VI |  |
| niDCPower Configure Current Limit Range VI |  |
| niDCPower Configure LCR Compensation VI |  |
| niDCPower Configure LCR Custom Cable Compensation VI |  |
| niDCPower Configure Output Enabled VI |  |
| niDCPower Configure Output Function VI |  |
| niDCPower Configure Output Resistance VI |  |
| niDCPower Configure Power Line Frequency VI |  |
| niDCPower Configure Pulse Bias Current Level VI |  |
| niDCPower Configure Pulse Bias Current Limit VI |  |
| niDCPower Configure Pulse Bias Voltage Level VI |  |
| niDCPower Configure Pulse Bias Voltage Limit VI |  |
| niDCPower Configure Pulse Current Level VI |  |
| niDCPower Configure Pulse Current Level Range VI |  |
| niDCPower Configure Pulse Current Limit VI |  |
| niDCPower Configure Pulse Current Limit Range VI |  |
| niDCPower Configure Pulse Voltage Level VI |  |
| niDCPower Configure Pulse Voltage Level Range VI |  |
| niDCPower Configure Pulse Voltage Limit VI |  |
| niDCPower Configure Pulse Voltage Limit Range VI |  |
| niDCPower Configure Sense VI |  |
| niDCPower Configure Source Mode With Channels VI |  |
| niDCPower Configure Trigger With Channels (Poly) VI |  |
| niDCPower Configure Voltage Level VI |  |
| niDCPower Configure Voltage Level Range VI |  |
| niDCPower Configure Voltage Limit VI |  |
| niDCPower Configure Voltage Limit Range VI |  |
| niDCPower Connect Internal Reference VI |  |
| niDCPower Create Advanced Sequence With Channels VI |  |
| niDCPower Create Advanced Sequence Commit Step With Channels VI |  |
| niDCPower Create Advanced Sequence Step With Channels VI |  |
| niDCPower Delete Advanced Sequence With Channels VI |  |
| niDCPower Disable VI |  |
| niDCPower Export Attribute Configuration (Poly) VI |  |
| niDCPower Export Signal With Channels VI |  |
| niDCPower Fetch Multiple VI |  |
| niDCPower Fetch Multiple LCR VI |  |
| niDCPower Get Cal User Defined Info VI |  |
| niDCPower Get Cal User Defined Info Max Size VI |  |
| niDCPower Get Channel Name |  |
| niDCPower Get Ext Cal Last Date And Time VI |  |
| niDCPower Get Ext Cal Last Temp VI |  |
| niDCPower Get Ext Cal Recommended Interval VI |  |
| niDCPower Get LCR Compensation Last Date And Time VI |  |
| niDCPower Get LCR Compensation Data VI |  |
| niDCPower Get LCR Custom Cable Compensation Data VI |  |
| niDCPower Get Next Coercion Record VI |  |
| niDCPower Get Next Interchange Warning VI |  |
| niDCPower Get Self Cal Last Date And Time VI |  |
| niDCPower Get Self Cal Last Temp VI |  |
| niDCPower Import Attribute Configuration (Poly) VI |  |
| niDCPower Initialize VI |  |
| niDCPower Initialize External Calibration VI |  |
| niDCPower Initialize With Independent Channels VI |  |
| niDCPower Initialize With Options VI |  |
| niDCPower Initiate With Channels VI |  |
| niDCPower Measure VI |  |
| niDCPower Measure Multiple VI |  |
| niDCPower Measure Multiple LCR VI |  |
| niDCPower Perform LCR Load Compensation VI |  |
| niDCPower Perform LCR Open Compensation VI |  |
| niDCPower Perform LCR Open Custom Cable Compensation VI |  |
| niDCPower Perform LCR Short Compensation VI |  |
| niDCPower Perform LCR Short Custom Cable Compensation VI |  |
| niDCPower Property Node VI |  |
| niDCPower Query In Compliance VI |  |
| niDCPower Query Latched Output Cutoff State VI |  |
| niDCPower Query Max Current Limit VI |  |
| niDCPower Query Max Voltage Level VI |  |
| niDCPower Query Min Current Limit VI |  |
| niDCPower Query Output State VI |  |
| niDCPower Read Current Temperature VI |  |
| niDCPower Reset With Channels VI |  |
| niDCPower Reset Device VI |  |
| niDCPower Reset Interchange Check VI |  |
| niDCPower Reset with Defaults VI |  |
| niDCPower Revision Query VI |  |
| niDCPower Self Test VI |  |
| niDCPower Send Software Edge Trigger With Channels VI |  |
| niDCPower Set Cal User Defined Info VI |  |
| niDCPower Set Sequence VI |  |
| niDCPower Wait For Event With Channels VI |  |

Parent topic:

Supported VIs by Device

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/supported-vis-414x.html language=enus -->
## TOPIC 00108: VIs Supported by the PXIe-4140/4141/4142/4143/4144/4145

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/supported-vis-414x.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/supported-vis-414x.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table shows which VIs are supported by NI-DCPower devices. A indicates that the device supports the VI; an indicates that the device does not support the VI. VI PXIe-414x niDCPower Abort With Channels VI^3 niDCPower Cal Adjust AC Flatness VI niDCPower Cal Adjust Current Limit VI niDCPo

### VIs Supported by the PXIe-4140/4141/4142/4143/4144/4145

The following table shows which VIs are supported by NI-DCPower devices. A [IMAGE alt='image' src='../../../images/checkmark.gif'] indicates that the device supports the VI; an [IMAGE alt='image' src='../../../images/xmark.gif'] indicates that the device does not support the VI.

| VI | PXIe-414x |
| --- | --- |
| niDCPower Abort With Channels VI[3] |  |
| niDCPower Cal Adjust AC Flatness VI |  |
| niDCPower Cal Adjust Current Limit VI |  |
| niDCPower Cal Adjust Current Measurement VI |  |
| niDCPower Cal Adjust Internal Reference VI |  |
| niDCPower Cal Adjust Output Resistance VI |  |
| niDCPower Cal Adjust Residual Current Offset VI |  |
| niDCPower Cal Adjust Residual Voltage Offset VI |  |
| niDCPower Cal Adjust Voltage Level VI |  |
| niDCPower Cal Adjust Voltage Measurement VI |  |
| niDCPower Cal Begin AC Flatness VI |  |
| niDCPower Cal Config AC Flatness VI |  |
| niDCPower Cal End AC Flatness VI |  |
| niDCPower Cal Self Calibrate VI |  |
| niDCPower Change Ext Cal Password VI |  |
| niDCPower Clear Interchange Warnings VI |  |
| niDCPower Clear Latched Output Cutoff State VI |  |
| niDCPower Close VI |  |
| niDCPower Close External Calibration VI |  |
| niDCPower Commit With Channels VI[3] |  |
| niDCPower Configure Aperture Time VI |  |
| niDCPower Configure Auto Zero VI |  |
| niDCPower Configure Current Level VI |  |
| niDCPower Configure Current Level Range VI |  |
| niDCPower Configure Current Limit VI |  |
| niDCPower Configure Current Limit Range VI |  |
| niDCPower Configure LCR Compensation VI |  |
| niDCPower Configure LCR Custom Cable Compensation VI |  |
| niDCPower Configure Output Enabled VI |  |
| niDCPower Configure Output Function VI |  |
| niDCPower Configure Output Resistance VI | [1] |
| niDCPower Configure Power Line Frequency VI |  |
| niDCPower Configure Pulse Bias Current Level VI |  |
| niDCPower Configure Pulse Bias Current Limit VI |  |
| niDCPower Configure Pulse Bias Voltage Level VI |  |
| niDCPower Configure Pulse Bias Voltage Limit VI |  |
| niDCPower Configure Pulse Current Level VI |  |
| niDCPower Configure Pulse Current Level Range VI |  |
| niDCPower Configure Pulse Current Limit VI |  |
| niDCPower Configure Pulse Current Limit Range VI |  |
| niDCPower Configure Pulse Voltage Level VI |  |
| niDCPower Configure Pulse Voltage Level Range VI |  |
| niDCPower Configure Pulse Voltage Limit VI |  |
| niDCPower Configure Pulse Voltage Limit Range VI |  |
| niDCPower Configure Sense VI |  |
| niDCPower Configure Source Mode With Channels VI[3] |  |
| niDCPower Configure Trigger With Channels (Poly) VI[3] |  |
| niDCPower Configure Voltage Level VI |  |
| niDCPower Configure Voltage Level Range VI |  |
| niDCPower Configure Voltage Limit VI |  |
| niDCPower Configure Voltage Limit Range VI |  |
| niDCPower Connect Internal Reference VI |  |
| niDCPower Create Advanced Sequence With Channels VI[3] |  |
| niDCPower Create Advanced Sequence Commit Step With Channels VI |  |
| niDCPower Create Advanced Sequence Step With Channels VI[3] |  |
| niDCPower Delete Advanced Sequence With Channels VI[3] |  |
| niDCPower Disable VI |  |
| niDCPower Export Attribute Configuration (Poly) VI |  |
| niDCPower Export Signal With Channels VI[3] |  |
| niDCPower Fetch Multiple VI |  |
| niDCPower Fetch Multiple LCR VI |  |
| niDCPower Get Cal User Defined Info VI |  |
| niDCPower Get Cal User Defined Info Max Size VI |  |
| niDCPower Get Channel Name (Poly) VI |  |
| niDCPower Get Ext Cal Last Date And Time VI |  |
| niDCPower Get Ext Cal Last Temp VI |  |
| niDCPower Get Ext Cal Recommended Interval VI |  |
| niDCPower Get LCR Compensation Last Date And Time VI |  |
| niDCPower Get LCR Compensation Data VI |  |
| niDCPower Get LCR Custom Cable Compensation Data VI |  |
| niDCPower Get Next Coercion Record VI |  |
| niDCPower Get Next Interchange Warning VI |  |
| niDCPower Get Self Cal Last Date And Time VI |  |
| niDCPower Get Self Cal Last Temp VI |  |
| niDCPower Import Attribute Configuration (Poly) VI |  |
| niDCPower Initialize External Calibration VI |  |
| niDCPower Initialize With Independent Channels VI[2] |  |
| niDCPower Initiate With Channels VI[3] |  |
| niDCPower Measure VI |  |
| niDCPower Measure Multiple VI |  |
| niDCPower Measure Multiple LCR VI |  |
| niDCPower Perform LCR Load Compensation VI |  |
| niDCPower Perform LCR Open Compensation VI |  |
| niDCPower Perform LCR Open Custom Cable Compensation VI |  |
| niDCPower Perform LCR Short Compensation VI |  |
| niDCPower Perform LCR Short Custom Cable Compensation VI |  |
| niDCPower Property Node VI |  |
| niDCPower Query In Compliance VI |  |
| niDCPower Query Latched Output Cutoff State VI |  |
| niDCPower Query Max Current Limit VI |  |
| niDCPower Query Max Voltage Level VI |  |
| niDCPower Query Min Current Limit VI |  |
| niDCPower Query Output State VI |  |
| niDCPower Read Current Temperature VI |  |
| niDCPower Reset With Channels VI[3] |  |
| niDCPower Reset Device VI |  |
| niDCPower Reset Interchange Check VI |  |
| niDCPower Reset with Defaults VI |  |
| niDCPower Revision Query VI |  |
| niDCPower Self Test VI |  |
| niDCPower Send Software Edge Trigger With Channels VI[3] |  |
| niDCPower Set Cal User Defined Info VI |  |
| niDCPower Set Sequence VI |  |
| niDCPower Wait For Event With Channels VI[3] |  |

1

PXIe-4139/4141/4143/4145 only.

2

The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

3

The deprecated, not-channel-based version of this VI is supported but not recommended.

Parent topic:

Supported VIs by Device

<sup>1</sup> PXIe-4139/4141/4143/4145 only.

<sup>2</sup> The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

<sup>3</sup> The deprecated, not-channel-based version of this VI is supported but not recommended.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/supported-vis-4150-4151.html language=enus -->
## TOPIC 00109: VIs Supported by the PXIe-4150/4151

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/supported-vis-4150-4151.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/supported-vis-4150-4151.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table shows which VIs are supported by NI-DCPower devices. A indicates that the device supports the VI; an indicates that the device does not support the VI. VI PXIe-4150/4151 niDCPower Abort With Channels VI^2 niDCPower Cal Adjust AC Flatness VI niDCPower Cal Adjust Current Limit VI n

### VIs Supported by the PXIe-4150/4151

The following table shows which VIs are supported by NI-DCPower devices. A [IMAGE alt='image' src='../../../images/checkmark.gif'] indicates that the device supports the VI; an [IMAGE alt='image' src='../../../images/xmark.gif'] indicates that the device does not support the VI.

| VI | PXIe-4150/4151 |
| --- | --- |
| niDCPower Abort With Channels VI[2] |  |
| niDCPower Cal Adjust AC Flatness VI |  |
| niDCPower Cal Adjust Current Limit VI |  |
| niDCPower Cal Adjust Current Measurement VI |  |
| niDCPower Cal Adjust Internal Reference VI |  |
| niDCPower Cal Adjust Output Resistance VI |  |
| niDCPower Cal Adjust Residual Current Offset VI |  |
| niDCPower Cal Adjust Residual Voltage Offset VI |  |
| niDCPower Cal Adjust Voltage Level VI |  |
| niDCPower Cal Adjust Voltage Measurement VI |  |
| niDCPower Cal Begin AC Flatness VI |  |
| niDCPower Cal Config AC Flatness VI |  |
| niDCPower Cal End AC Flatness VI |  |
| niDCPower Cal Self Calibrate VI |  |
| niDCPower Change Ext Cal Password VI |  |
| niDCPower Clear Interchange Warnings VI |  |
| niDCPower Clear Latched Output Cutoff State VI |  |
| niDCPower Close VI |  |
| niDCPower Close External Calibration VI |  |
| niDCPower Commit With Channels VI[2] |  |
| niDCPower Configure Aperture Time VI |  |
| niDCPower Configure Auto Zero VI |  |
| niDCPower Configure Current Level VI |  |
| niDCPower Configure Current Level Range VI |  |
| niDCPower Configure Current Limit VI |  |
| niDCPower Configure Current Limit Range VI |  |
| niDCPower Configure LCR Compensation VI |  |
| niDCPower Configure LCR Custom Cable Compensation VI |  |
| niDCPower Configure Output Enabled VI |  |
| niDCPower Configure Output Function VI |  |
| niDCPower Configure Output Resistance VI |  |
| niDCPower Configure Power Line Frequency VI |  |
| niDCPower Configure Pulse Bias Current Level VI |  |
| niDCPower Configure Pulse Bias Current Limit VI |  |
| niDCPower Configure Pulse Bias Voltage Level VI |  |
| niDCPower Configure Pulse Bias Voltage Limit VI |  |
| niDCPower Configure Pulse Current Level VI |  |
| niDCPower Configure Pulse Current Level Range VI |  |
| niDCPower Configure Pulse Current Limit VI |  |
| niDCPower Configure Pulse Current Limit Range VI |  |
| niDCPower Configure Pulse Voltage Level VI |  |
| niDCPower Configure Pulse Voltage Level Range VI |  |
| niDCPower Configure Pulse Voltage Limit VI |  |
| niDCPower Configure Pulse Voltage Limit Range VI |  |
| niDCPower Configure Sense VI |  |
| niDCPower Configure Source Mode With Channels VI[2] |  |
| niDCPower Configure Trigger With Channels (Poly) VI[2] |  |
| niDCPower Configure Voltage Level VI |  |
| niDCPower Configure Voltage Level Range VI |  |
| niDCPower Configure Voltage Limit VI |  |
| niDCPower Configure Voltage Limit Range VI |  |
| niDCPower Connect Internal Reference VI |  |
| niDCPower Create Advanced Sequence With Channels VI[2] |  |
| niDCPower Create Advanced Sequence Commit Step With Channels VI |  |
| niDCPower Create Advanced Sequence Step With Channels VI[2] |  |
| niDCPower Delete Advanced Sequence With Channels VI[2] |  |
| niDCPower Disable VI |  |
| niDCPower Export Attribute Configuration (Poly) VI |  |
| niDCPower Export Signal With Channels VI[2] |  |
| niDCPower Fetch Multiple VI |  |
| niDCPower Fetch Multiple LCR VI |  |
| niDCPower Get Cal User Defined Info VI |  |
| niDCPower Get Cal User Defined Info Max Size VI |  |
| niDCPower Get Channel Name (Poly) VI |  |
| niDCPower Get Ext Cal Last Date And Time VI |  |
| niDCPower Get Ext Cal Last Temp VI |  |
| niDCPower Get Ext Cal Recommended Interval VI |  |
| niDCPower Get LCR Compensation Last Date And Time VI |  |
| niDCPower Get LCR Compensation Data VI |  |
| niDCPower Get LCR Custom Cable Compensation Data VI |  |
| niDCPower Get Next Coercion Record VI |  |
| niDCPower Get Next Interchange Warning VI |  |
| niDCPower Get Self Cal Last Date And Time VI |  |
| niDCPower Get Self Cal Last Temp VI |  |
| niDCPower Import Attribute Configuration (Poly) VI |  |
| niDCPower Initialize External Calibration VI |  |
| niDCPower Initialize With Independent Channels VI[1] |  |
| niDCPower Initiate With Channels VI[2] |  |
| niDCPower Measure VI |  |
| niDCPower Measure Multiple VI |  |
| niDCPower Measure Multiple LCR VI |  |
| niDCPower Perform LCR Load Compensation VI |  |
| niDCPower Perform LCR Open Compensation VI |  |
| niDCPower Perform LCR Open Custom Cable Compensation VI |  |
| niDCPower Perform LCR Short Compensation VI |  |
| niDCPower Perform LCR Short Custom Cable Compensation VI |  |
| niDCPower Property Node VI |  |
| niDCPower Query In Compliance VI |  |
| niDCPower Query Latched Output Cutoff State VI |  |
| niDCPower Query Max Current Limit VI |  |
| niDCPower Query Max Voltage Level VI |  |
| niDCPower Query Min Current Limit VI |  |
| niDCPower Query Output State VI |  |
| niDCPower Read Current Temperature VI |  |
| niDCPower Reset With Channels VI[2] |  |
| niDCPower Reset Device VI |  |
| niDCPower Reset Interchange Check VI |  |
| niDCPower Reset with Defaults VI |  |
| niDCPower Revision Query VI |  |
| niDCPower Self Test VI |  |
| niDCPower Send Software Edge Trigger With Channels VI[2] |  |
| niDCPower Set Cal User Defined Info VI |  |
| niDCPower Set Sequence VI |  |
| niDCPower Wait For Event With Channels VI[2] |  |

1

The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

2

The deprecated, not-channel-based version of this VI is supported but not recommended.

Parent topic:

Supported VIs by Device

<sup>1</sup> The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

<sup>2</sup> The deprecated, not-channel-based version of this VI is supported but not recommended.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/supported-vis-4154.html language=enus -->
## TOPIC 00110: VIs Supported by the PXIe-4154

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/supported-vis-4154.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/supported-vis-4154.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table shows which VIs are supported by NI-DCPower devices. A indicates that the device supports the VI; an indicates that the device does not support the VI. VI PXIe-4154 niDCPower Abort With Channels VI^3 niDCPower Cal Adjust AC Flatness VI niDCPower Cal Adjust Current Limit VI niDCPo

### VIs Supported by the PXIe-4154

The following table shows which VIs are supported by NI-DCPower devices. A [IMAGE alt='image' src='../../../images/checkmark.gif'] indicates that the device supports the VI; an [IMAGE alt='image' src='../../../images/xmark.gif'] indicates that the device does not support the VI.

| VI | PXIe-4154 |
| --- | --- |
| niDCPower Abort With Channels VI[3] |  |
| niDCPower Cal Adjust AC Flatness VI |  |
| niDCPower Cal Adjust Current Limit VI |  |
| niDCPower Cal Adjust Current Measurement VI |  |
| niDCPower Cal Adjust Internal Reference VI |  |
| niDCPower Cal Adjust Output Resistance VI |  |
| niDCPower Cal Adjust Residual Current Offset VI |  |
| niDCPower Cal Adjust Residual Voltage Offset VI |  |
| niDCPower Cal Adjust Voltage Level VI |  |
| niDCPower Cal Adjust Voltage Measurement VI |  |
| niDCPower Cal Begin AC Flatness VI |  |
| niDCPower Cal Config AC Flatness VI |  |
| niDCPower Cal End AC Flatness VI |  |
| niDCPower Cal Self Calibrate VI |  |
| niDCPower Change Ext Cal Password VI |  |
| niDCPower Clear Interchange Warnings VI |  |
| niDCPower Clear Latched Output Cutoff State VI |  |
| niDCPower Close VI |  |
| niDCPower Close External Calibration VI |  |
| niDCPower Commit With Channels VI[3] |  |
| niDCPower Configure Aperture Time VI |  |
| niDCPower Configure Auto Zero VI |  |
| niDCPower Configure Current Level VI |  |
| niDCPower Configure Current Level Range VI |  |
| niDCPower Configure Current Limit VI |  |
| niDCPower Configure Current Limit Range VI |  |
| niDCPower Configure LCR Compensation VI |  |
| niDCPower Configure LCR Custom Cable Compensation VI |  |
| niDCPower Configure Output Enabled VI |  |
| niDCPower Configure Output Function VI |  |
| niDCPower Configure Output Resistance VI | [1] |
| niDCPower Configure Power Line Frequency VI |  |
| niDCPower Configure Pulse Bias Current Level VI |  |
| niDCPower Configure Pulse Bias Current Limit VI |  |
| niDCPower Configure Pulse Bias Voltage Level VI |  |
| niDCPower Configure Pulse Bias Voltage Limit VI |  |
| niDCPower Configure Pulse Current Level VI |  |
| niDCPower Configure Pulse Current Level Range VI |  |
| niDCPower Configure Pulse Current Limit VI |  |
| niDCPower Configure Pulse Current Limit Range VI |  |
| niDCPower Configure Pulse Voltage Level VI |  |
| niDCPower Configure Pulse Voltage Level Range VI |  |
| niDCPower Configure Pulse Voltage Limit VI |  |
| niDCPower Configure Pulse Voltage Limit Range VI |  |
| niDCPower Configure Sense VI |  |
| niDCPower Configure Source Mode With Channels VI[3] |  |
| niDCPower Configure Trigger With Channels (Poly) VI[3] |  |
| niDCPower Configure Voltage Level VI |  |
| niDCPower Configure Voltage Level Range VI |  |
| niDCPower Configure Voltage Limit VI |  |
| niDCPower Configure Voltage Limit Range VI |  |
| niDCPower Connect Internal Reference VI |  |
| niDCPower Create Advanced Sequence With Channels VI[3] |  |
| niDCPower Create Advanced Sequence Commit Step With Channels VI |  |
| niDCPower Create Advanced Sequence Step With Channels VI[3] |  |
| niDCPower Delete Advanced Sequence With Channels VI[3] |  |
| niDCPower Disable VI |  |
| niDCPower Export Attribute Configuration (Poly) VI |  |
| niDCPower Export Signal With Channels VI[3] |  |
| niDCPower Fetch Multiple VI |  |
| niDCPower Fetch Multiple LCR VI |  |
| niDCPower Get Cal User Defined Info VI |  |
| niDCPower Get Cal User Defined Info Max Size VI |  |
| niDCPower Get Channel Name (Poly) VI |  |
| niDCPower Get Ext Cal Last Date And Time VI |  |
| niDCPower Get Ext Cal Last Temp VI |  |
| niDCPower Get Ext Cal Recommended Interval VI |  |
| niDCPower Get LCR Compensation Last Date And Time VI |  |
| niDCPower Get LCR Compensation Data VI |  |
| niDCPower Get LCR Custom Cable Compensation Data VI |  |
| niDCPower Get Next Coercion Record VI |  |
| niDCPower Get Next Interchange Warning VI |  |
| niDCPower Get Self Cal Last Date And Time VI |  |
| niDCPower Get Self Cal Last Temp VI |  |
| niDCPower Import Attribute Configuration (Poly) VI |  |
| niDCPower Initialize External Calibration VI |  |
| niDCPower Initialize With Independent Channels VI[2] |  |
| niDCPower Initiate With Channels VI[3] |  |
| niDCPower Measure VI |  |
| niDCPower Measure Multiple VI |  |
| niDCPower Measure Multiple LCR VI |  |
| niDCPower Perform LCR Load Compensation VI |  |
| niDCPower Perform LCR Open Compensation VI |  |
| niDCPower Perform LCR Open Custom Cable Compensation VI |  |
| niDCPower Perform LCR Short Compensation VI |  |
| niDCPower Perform LCR Short Custom Cable Compensation VI |  |
| niDCPower Property Node VI |  |
| niDCPower Query In Compliance VI |  |
| niDCPower Query Latched Output Cutoff State VI |  |
| niDCPower Query Max Current Limit VI |  |
| niDCPower Query Max Voltage Level VI |  |
| niDCPower Query Min Current Limit VI |  |
| niDCPower Query Output State VI |  |
| niDCPower Read Current Temperature VI |  |
| niDCPower Reset With Channels VI[3] |  |
| niDCPower Reset Device VI |  |
| niDCPower Reset Interchange Check VI |  |
| niDCPower Reset with Defaults VI |  |
| niDCPower Revision Query VI |  |
| niDCPower Self Test VI |  |
| niDCPower Send Software Edge Trigger With Channels VI[3] |  |
| niDCPower Set Cal User Defined Info VI |  |
| niDCPower Set Sequence VI |  |
| niDCPower Wait For Event With Channels VI[3] |  |

1

Channel 0 only.

2

The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

3

The deprecated, not-channel-based version of this VI is supported but not recommended.

Parent topic:

Supported VIs by Device

<sup>1</sup> Channel 0 only.

<sup>2</sup> The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

<sup>3</sup> The deprecated, not-channel-based version of this VI is supported but not recommended.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/supported-vis-4162-4163.html language=enus -->
## TOPIC 00111: VIs Supported by the PXIe-4162/4163

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/supported-vis-4162-4163.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/supported-vis-4162-4163.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table shows which VIs are supported by NI-DCPower devices. A indicates that the device supports the VI; an indicates that the device does not support the VI. VI PXIe-4162/4163 niDCPower Abort With Channels VI^2 niDCPower Cal Adjust AC Flatness VI niDCPower Cal Adjust Current Limit VI n

### VIs Supported by the PXIe-4162/4163

The following table shows which VIs are supported by NI-DCPower devices. A [IMAGE alt='image' src='../../../images/checkmark.gif'] indicates that the device supports the VI; an [IMAGE alt='image' src='../../../images/xmark.gif'] indicates that the device does not support the VI.

| VI | PXIe-4162/4163 |
| --- | --- |
| niDCPower Abort With Channels VI[2] |  |
| niDCPower Cal Adjust AC Flatness VI |  |
| niDCPower Cal Adjust Current Limit VI |  |
| niDCPower Cal Adjust Current Measurement VI |  |
| niDCPower Cal Adjust Internal Reference VI |  |
| niDCPower Cal Adjust Output Resistance VI |  |
| niDCPower Cal Adjust Residual Current Offset VI |  |
| niDCPower Cal Adjust Residual Voltage Offset VI |  |
| niDCPower Cal Adjust Voltage Level VI |  |
| niDCPower Cal Adjust Voltage Measurement VI |  |
| niDCPower Cal Begin AC Flatness VI |  |
| niDCPower Cal Config AC Flatness VI |  |
| niDCPower Cal End AC Flatness VI |  |
| niDCPower Cal Self Calibrate VI |  |
| niDCPower Change Ext Cal Password VI |  |
| niDCPower Clear Interchange Warnings VI |  |
| niDCPower Clear Latched Output Cutoff State VI |  |
| niDCPower Close VI |  |
| niDCPower Close External Calibration VI |  |
| niDCPower Commit With Channels VI[2] |  |
| niDCPower Configure Aperture Time VI |  |
| niDCPower Configure Auto Zero VI |  |
| niDCPower Configure Current Level VI |  |
| niDCPower Configure Current Level Range VI |  |
| niDCPower Configure Current Limit VI |  |
| niDCPower Configure Current Limit Range VI |  |
| niDCPower Configure LCR Compensation VI |  |
| niDCPower Configure LCR Custom Cable Compensation VI |  |
| niDCPower Configure Output Enabled VI |  |
| niDCPower Configure Output Function VI |  |
| niDCPower Configure Output Resistance VI |  |
| niDCPower Configure Power Line Frequency VI |  |
| niDCPower Configure Pulse Bias Current Level VI |  |
| niDCPower Configure Pulse Bias Current Limit VI |  |
| niDCPower Configure Pulse Bias Voltage Level VI |  |
| niDCPower Configure Pulse Bias Voltage Limit VI |  |
| niDCPower Configure Pulse Current Level VI |  |
| niDCPower Configure Pulse Current Level Range VI |  |
| niDCPower Configure Pulse Current Limit VI |  |
| niDCPower Configure Pulse Current Limit Range VI |  |
| niDCPower Configure Pulse Voltage Level VI |  |
| niDCPower Configure Pulse Voltage Level Range VI |  |
| niDCPower Configure Pulse Voltage Limit VI |  |
| niDCPower Configure Pulse Voltage Limit Range VI |  |
| niDCPower Configure Sense VI |  |
| niDCPower Configure Source Mode With Channels VI[2] |  |
| niDCPower Configure Trigger With Channels (Poly) VI[2] |  |
| niDCPower Configure Voltage Level VI |  |
| niDCPower Configure Voltage Level Range VI |  |
| niDCPower Configure Voltage Limit VI |  |
| niDCPower Configure Voltage Limit Range VI |  |
| niDCPower Connect Internal Reference VI |  |
| niDCPower Create Advanced Sequence With Channels VI[2] |  |
| niDCPower Create Advanced Sequence Commit Step With Channels VI |  |
| niDCPower Create Advanced Sequence Step With Channels VI[2] |  |
| niDCPower Delete Advanced Sequence With Channels VI[2] |  |
| niDCPower Disable VI |  |
| niDCPower Export Attribute Configuration (Poly) VI |  |
| niDCPower Export Signal With Channels VI[2] |  |
| niDCPower Fetch Multiple VI |  |
| niDCPower Fetch Multiple LCR VI |  |
| niDCPower Get Cal User Defined Info VI |  |
| niDCPower Get Cal User Defined Info Max Size VI |  |
| niDCPower Get Channel Name (Poly) VI |  |
| niDCPower Get Ext Cal Last Date And Time VI |  |
| niDCPower Get Ext Cal Last Temp VI |  |
| niDCPower Get Ext Cal Recommended Interval VI |  |
| niDCPower Get LCR Compensation Last Date And Time VI |  |
| niDCPower Get LCR Compensation Data VI |  |
| niDCPower Get LCR Custom Cable Compensation Data VI |  |
| niDCPower Get Next Coercion Record VI |  |
| niDCPower Get Next Interchange Warning VI |  |
| niDCPower Get Self Cal Last Date And Time VI |  |
| niDCPower Get Self Cal Last Temp VI |  |
| niDCPower Import Attribute Configuration (Poly) VI |  |
| niDCPower Initialize External Calibration VI |  |
| niDCPower Initialize With Independent Channels VI[1] |  |
| niDCPower Initiate With Channels VI[2] |  |
| niDCPower Measure VI |  |
| niDCPower Measure Multiple VI |  |
| niDCPower Measure Multiple LCR VI |  |
| niDCPower Perform LCR Load Compensation VI |  |
| niDCPower Perform LCR Open Compensation VI |  |
| niDCPower Perform LCR Open Custom Cable Compensation VI |  |
| niDCPower Perform LCR Short Compensation VI |  |
| niDCPower Perform LCR Short Custom Cable Compensation VI |  |
| niDCPower Property Node VI |  |
| niDCPower Query In Compliance VI |  |
| niDCPower Query Latched Output Cutoff State VI |  |
| niDCPower Query Max Current Limit VI |  |
| niDCPower Query Max Voltage Level VI |  |
| niDCPower Query Min Current Limit VI |  |
| niDCPower Query Output State VI |  |
| niDCPower Read Current Temperature VI |  |
| niDCPower Reset With Channels VI[2] |  |
| niDCPower Reset Device VI |  |
| niDCPower Reset Interchange Check VI |  |
| niDCPower Reset with Defaults VI |  |
| niDCPower Revision Query VI |  |
| niDCPower Self Test VI |  |
| niDCPower Send Software Edge Trigger With Channels VI[2] |  |
| niDCPower Set Cal User Defined Info VI |  |
| niDCPower Set Sequence VI |  |
| niDCPower Wait For Event With Channels VI[2] |  |

1

The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

2

The deprecated, not-channel-based version of this VI is supported but not recommended.

Parent topic:

Supported VIs by Device

<sup>1</sup> The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

<sup>2</sup> The deprecated, not-channel-based version of this VI is supported but not recommended.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/supported-vis-4190.html language=enus -->
## TOPIC 00112: VIs Supported by the PXIe-4190

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/supported-vis-4190.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/supported-vis-4190.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table shows which VIs are supported by NI-DCPower devices. A indicates that the device supports the VI; an indicates that the device does not support the VI. VI PXIe-4190 niDCPower Abort With Channels VI^3 niDCPower Cal Adjust AC Flatness VI niDCPower Cal Adjust Current Limit VI niDCPo

### VIs Supported by the PXIe-4190

The following table shows which VIs are supported by NI-DCPower devices. A [IMAGE alt='image' src='../../../images/checkmark.gif'] indicates that the device supports the VI; an [IMAGE alt='image' src='../../../images/xmark.gif'] indicates that the device does not support the VI.

| VI | PXIe-4190 |
| --- | --- |
| niDCPower Abort With Channels VI[3] |  |
| niDCPower Cal Adjust AC Flatness VI |  |
| niDCPower Cal Adjust Current Limit VI |  |
| niDCPower Cal Adjust Current Measurement VI |  |
| niDCPower Cal Adjust Internal Reference VI |  |
| niDCPower Cal Adjust Output Resistance VI |  |
| niDCPower Cal Adjust Residual Current Offset VI |  |
| niDCPower Cal Adjust Residual Voltage Offset VI |  |
| niDCPower Cal Adjust Voltage Level VI |  |
| niDCPower Cal Adjust Voltage Measurement VI |  |
| niDCPower Cal Begin AC Flatness VI |  |
| niDCPower Cal Config AC Flatness VI |  |
| niDCPower Cal End AC Flatness VI |  |
| niDCPower Cal Self Calibrate VI |  |
| niDCPower Change Ext Cal Password VI |  |
| niDCPower Clear Interchange Warnings VI |  |
| niDCPower Clear Latched Output Cutoff State VI |  |
| niDCPower Close VI |  |
| niDCPower Close External Calibration VI |  |
| niDCPower Commit With Channels VI[3] |  |
| niDCPower Configure Aperture Time VI |  |
| niDCPower Configure Auto Zero VI |  |
| niDCPower Configure Current Level VI |  |
| niDCPower Configure Current Level Range VI |  |
| niDCPower Configure Current Limit VI |  |
| niDCPower Configure Current Limit Range VI |  |
| niDCPower Configure LCR Compensation VI |  |
| niDCPower Configure LCR Custom Cable Compensation VI |  |
| niDCPower Configure Output Enabled VI |  |
| niDCPower Configure Output Function VI |  |
| niDCPower Configure Output Resistance VI |  |
| niDCPower Configure Power Line Frequency VI |  |
| niDCPower Configure Pulse Bias Current Level VI |  |
| niDCPower Configure Pulse Bias Current Limit VI |  |
| niDCPower Configure Pulse Bias Voltage Level VI |  |
| niDCPower Configure Pulse Bias Voltage Limit VI |  |
| niDCPower Configure Pulse Current Level VI |  |
| niDCPower Configure Pulse Current Level Range VI |  |
| niDCPower Configure Pulse Current Limit VI |  |
| niDCPower Configure Pulse Current Limit Range VI |  |
| niDCPower Configure Pulse Voltage Level VI |  |
| niDCPower Configure Pulse Voltage Level Range VI |  |
| niDCPower Configure Pulse Voltage Limit VI |  |
| niDCPower Configure Pulse Voltage Limit Range VI |  |
| niDCPower Configure Sense VI |  |
| niDCPower Configure Source Mode With Channels VI[3] |  |
| niDCPower Configure Trigger With Channels (Poly) VI[3] |  |
| niDCPower Configure Voltage Level VI |  |
| niDCPower Configure Voltage Level Range VI |  |
| niDCPower Configure Voltage Limit VI |  |
| niDCPower Configure Voltage Limit Range VI |  |
| niDCPower Connect Internal Reference VI |  |
| niDCPower Create Advanced Sequence With Channels VI[3] |  |
| niDCPower Create Advanced Sequence Step With Channels VI[3] |  |
| niDCPower Create Advanced Sequence Commit Step With Channels VI |  |
| niDCPower Delete Advanced Sequence With Channels VI[3] |  |
| niDCPower Disable VI |  |
| niDCPower Export Attribute Configuration (Poly) VI |  |
| niDCPower Export Signal With Channels VI[3] |  |
| niDCPower Fetch Multiple VI |  |
| niDCPower Fetch Multiple LCR VI |  |
| niDCPower Get Cal User Defined Info VI |  |
| niDCPower Get Cal User Defined Info Max Size VI |  |
| niDCPower Get Channel Name (Poly) VI |  |
| niDCPower Get Ext Cal Last Date And Time VI |  |
| niDCPower Get Ext Cal Last Temp VI |  |
| niDCPower Get Ext Cal Recommended Interval VI |  |
| niDCPower Get LCR Compensation Last Date And Time VI |  |
| niDCPower Get LCR Compensation Data VI |  |
| niDCPower Get LCR Custom Cable Compensation Data VI |  |
| niDCPower Get Next Coercion Record VI |  |
| niDCPower Get Next Interchange Warning VI |  |
| niDCPower Get Self Cal Last Date And Time VI |  |
| niDCPower Get Self Cal Last Temp VI |  |
| niDCPower Import Attribute Configuration (Poly) VI |  |
| niDCPower Initialize External Calibration VI |  |
| niDCPower Initialize With Independent Channels VI[2] |  |
| niDCPower Initiate With Channels VI[3] |  |
| niDCPower Measure VI |  |
| niDCPower Measure Multiple VI |  |
| niDCPower Measure Multiple LCR VI |  |
| niDCPower Perform LCR Load Compensation VI |  |
| niDCPower Perform LCR Open Compensation VI |  |
| niDCPower Perform LCR Open Custom Cable Compensation VI |  |
| niDCPower Perform LCR Short Compensation VI |  |
| niDCPower Perform LCR Short Custom Cable Compensation VI |  |
| niDCPower Property Node VI |  |
| niDCPower Query In Compliance VI |  |
| niDCPower Query Latched Output Cutoff State VI |  |
| niDCPower Query Max Current Limit VI |  |
| niDCPower Query Max Voltage Level VI |  |
| niDCPower Query Min Current Limit VI |  |
| niDCPower Query Output State VI |  |
| niDCPower Read Current Temperature VI |  |
| niDCPower Reset With Channels VI[3] |  |
| niDCPower Reset Device VI |  |
| niDCPower Reset Interchange Check VI |  |
| niDCPower Reset with Defaults VI |  |
| niDCPower Revision Query VI |  |
| niDCPower Self Test VI |  |
| niDCPower Send Software Edge Trigger With Channels VI[3] |  |
| niDCPower Set Cal User Defined Info VI |  |
| niDCPower Set Sequence VI | [4] |
| niDCPower Wait For Event With Channels VI[3] | [1] |

1

Source Complete event only.

2

The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

3

The deprecated, not-channel-based version of this VI is supported but not recommended.

4

Only supported if Instrument Mode is set to SMU PS.

Parent topic:

Supported VIs by Device

<sup>1</sup> Source Complete event only.

<sup>2</sup> The deprecated niDCPower Initialize With Channels, Initialize With Options, and Initialize VIs are supported but not recommended.

<sup>3</sup> The deprecated, not-channel-based version of this VI is supported but not recommended.

<sup>4</sup> Only supported if Instrument Mode is set to SMU PS.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-llb/supportedvis.html language=enus -->
## TOPIC 00113: Supported VIs by Device

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-llb/supportedvis.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-llb/supportedvis.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following topics for information about VI support.

### Supported VIs by Device

Refer to the following topics for information about VI support.

- [VIs Supported by the PXIe-4051](../../../instr-lib/nidcpower/nidcpower-llb/supported-vis-4051.html)
- [VIs Supported by the PXI-4110](../../../instr-lib/nidcpower/nidcpower-llb/supported-vis-4110.html)
- [VIs Supported by the PXIe-4112/4113](../../../instr-lib/nidcpower/nidcpower-llb/supported-vis-4112-4113.html)
- [VIs Supported by the PXI-4130](../../../instr-lib/nidcpower/nidcpower-llb/supported-vis-4130.html)
- [VIs Supported by the PXI-4132](../../../instr-lib/nidcpower/nidcpower-llb/supported-vis-4132.html)
- [VIs Supported by the PXIe-4135](../../../instr-lib/nidcpower/nidcpower-llb/supported-vis-4135.html)
- [VIs Supported by the PXIe-4136/4137](../../../instr-lib/nidcpower/nidcpower-llb/supported-vis-4136-4137.html)
- [VIs Supported by the PXIe-4138/4139](../../../instr-lib/nidcpower/nidcpower-llb/supported-vis-4138-4139.html)
- [VIs Supported by the PXIe-4140/4141/4142/4143/4144/4145](../../../instr-lib/nidcpower/nidcpower-llb/supported-vis-414x.html)
- [VIs Supported by the PXIe-4147](../../../instr-lib/nidcpower/nidcpower-llb/supported-vis-4147.html)
- [VIs Supported by the PXIe-4150/4151](../../../instr-lib/nidcpower/nidcpower-llb/supported-vis-4150-4151.html)
- [VIs Supported by the PXIe-4154](../../../instr-lib/nidcpower/nidcpower-llb/supported-vis-4154.html)
- [VIs Supported by the PXIe-4162/4163](../../../instr-lib/nidcpower/nidcpower-llb/supported-vis-4162-4163.html)
- [VIs Supported by the PXIe-4190](../../../instr-lib/nidcpower/nidcpower-llb/supported-vis-4190.html)

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower-p.html language=enus -->
## TOPIC 00114: niDCPower Properties

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower-p.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower properties to access advanced configuration options. © 2006–2023 National Instruments Corporation. All rights reserved.

### niDCPower Properties

Use the NI-DCPower properties to access advanced configuration options.

© 2006–2023 National Instruments Corporation. All rights reserved.

- [Active Channel](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-activechannel.html) Specifies the channel(s) used to access all subsequent channel-based properties in this property node.
- [Source:Source Mode](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcemode.html) Specifies whether to run a single output point or a sequence. Refer to the Single Point source mode and Sequence source mode topics in the NI DC Power Supplies and SMUs Help for more information about source modes.
- [Source:Output Function](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputfunction.html) Configures the function to generate on the specified channel(s).
- [Source:Output Enabled](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputenabled.html) Specifies whether the output is enabled (TRUE) or disabled (FALSE).
- [Source:Output Connected](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputconnected.html) Specifies whether the output relay is connected (closed) or disconnected (open). The Output Enabled property does not change based on this property; they are independent of each other.
- [Source:Output Resistance](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputresistance.html) Specifies the output resistance that the device attempts to generate for the specified channel(s).
- [Source:Transient Response](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-transientresponse.html) Specifies the transient response. Refer to the Transient Response topic in the NI DC Power Supplies and SMUs Help for more information about transient response.
- [Source:Custom Transient Response:Voltage:Gain Bandwidth](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagegainbandwidth.html) The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the channel is in Constant Voltage mode.
- [Source:Custom Transient Response:Voltage:Compensation Frequency](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagecompensationfrequency.html) The frequency at which a pole-zero pair is added to the system when the channel is in Constant Voltage mode.
- [Source:Custom Transient Response:Voltage:Pole-Zero Ratio](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagepolezeroratio.html) The ratio of the pole frequency to the zero frequency when the channel is in Constant Voltage mode.
- [Source:Custom Transient Response:Current:Gain Bandwidth](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentgainbandwidth.html) The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the channel is in Constant Current mode.
- [Source:Custom Transient Response:Current:Compensation Frequency](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentcompensationfrequency.html) The frequency at which a pole-zero pair is added to the system when the channel is in Constant Current mode.
- [Source:Custom Transient Response:Current:Pole-Zero Ratio](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentpolezeroratio.html) The ratio of the pole frequency to the zero frequency when the channel is in Constant Current mode.
- [Source:Custom Transient Response:Constant Resistance:Gain Bandwidth](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancegainbandwidth.html) The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the Output Function property is set to Constant Resistance and the output current is below the current limit.
- [Source:Custom Transient Response:Constant Resistance:Compensation Frequency](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancecompensationfrequency.html) The frequency at which a pole-zero pair is added to the system when the Output Function property is set to Constant Resistance and the output current is below the current limit.
- [Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancepolezeroratio.html) The ratio of the pole frequency to the zero frequency when the Output Function property is set to Constant Resistance and the output current is below the current limit.
- [Source:Custom Transient Response:Constant Power:Gain Bandwidth](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowergainbandwidth.html) The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the Output Function property is set to Constant Power and the output current is below the current limit.
- [Source:Custom Transient Response:Constant Power:Compensation Frequency](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowercompensationfrequency.html) The frequency at which a pole-zero pair is added to the system when the Output Function property is set to Constant Power and the output current is below the current limit.
- [Source:Custom Transient Response:Constant Power:Pole-Zero Ratio](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowerpolezeroratio.html) The ratio of the pole frequency to the zero frequency when the Output Function property is set to Constant Power and the output current is below the current limit.
- [Source:DC Voltage:Voltage Level](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelevel.html) Specifies the voltage level, in volts, that the device attempts to generate on the specified channel(s).
- [Source:DC Voltage:Voltage Level Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelevelrange.html) Specifies the voltage level range, in volts, for the specified channel(s).
- [Source:DC Voltage:Voltage Level Autorange](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelevelautorange.html) Specifies whether NI-DCPower automatically selects the voltage level range based on the desired voltage level for the specified channel(s).
- [Source:DC Voltage:Current Limit](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimit.html) Specifies the current limit, in amps, that the output cannot exceed when generating the desired voltage on the specified channel(s). Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.
- [Source:DC Voltage:Current Limit High](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimithigh.html) Specifies the maximum current, in amps, that the output can produce when generating the desired voltage on the specified channel(s).
- [Source:DC Voltage:Current Limit Low](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimitlow.html) Specifies the minimum current, in amps, that the output can produce when generating the desired voltage on the specified channel(s).
- [Source:DC Voltage:Current Limit Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimitrange.html) Specifies the current limit range, in amps, for the specified channel(s).
- [Source:DC Voltage:Current Limit Autorange](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimitautorange.html) Specifies whether NI-DCPower automatically selects the current limit range based on the desired current limit for the specified channel(s).
- [Source:DC Current:Current Level](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevel.html) Specifies the current level, in amps, that the device attempts to generate on the specified channel(s).
- [Source:DC Current:Current Level Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelrange.html) Specifies the current level range, in amps, for the specified channel(s).
- [Source:DC Current:Current Level Autorange](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelautorange.html) Specifies whether NI-DCPower automatically selects the current level range based on the desired current level for the specified channel(s).
- [Source:DC Current:Voltage Limit](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimit.html) Specifies the voltage limit, in volts, that the output cannot exceed when generating the desired current level on the specified channels. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.
- [Source:DC Current:Voltage Limit High](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimithigh.html) Specifies the maximum voltage, in volts, that the output can produce when generating the desired current on the specified channel(s).
- [Source:DC Current:Voltage Limit Low](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimitlow.html) Specifies the minimum voltage, in volts, that the output can produce when generating the desired current on the specified channel(s).
- [Source:DC Current:Voltage Limit Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimitrange.html) Specifies the voltage limit range, in volts, for the specified channel(s).
- [Source:DC Current:Voltage Limit Autorange](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-voltagelimitautorange.html) Specifies whether NI-DCPower automatically selects the voltage limit range based on the desired voltage limit for the specified channel(s).
- [Source:DC Current:Current Level Slew Rate:Rising](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelrisingslewrate.html) Specifies the rate of increase, in amps per microsecond, to apply to the absolute magnitude of the current level of the specified channel(s).
- [Source:DC Current:Current Level Slew Rate:Falling](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelfallingslewrate.html) Specifies the rate of decrease, in amps per microsecond, to apply to the absolute magnitude of the current level of the specified channel(s).
- [Source:Pulse Voltage:Pulse Voltage Level](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelevel.html) Specifies the pulse voltage level, in volts, that the device attempts to generate on the specified channel(s) during the on phase of a pulse.
- [Source:Pulse Voltage:Pulse Bias Voltage Level](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelevel.html) Specifies the pulse bias voltage level, in volts, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
- [Source:Pulse Voltage:Pulse Voltage Level Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelevelrange.html) Specifies the pulse voltage level range, in volts, for the specified channel(s).
- [Source:Pulse Voltage:Pulse Current Limit](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimit.html) Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.
- [Source:Pulse Voltage:Pulse Current Limit High](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimithigh.html) Specifies the maximum current, in amps, that the output can produce when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
- [Source:Pulse Voltage:Pulse Current Limit Low](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimitlow.html) Specifies the minimum current, in amps, that the output can produce when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
- [Source:Pulse Voltage:Pulse Bias Current Limit](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlimit.html) Specifies the pulse bias current limit, in amps, that the output cannot exceed when generating the desired pulse bias voltage on the specified channel(s) during the off phase of a pulse. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.
- [Source:Pulse Voltage:Pulse Bias Current Limit High](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlimithigh.html) Specifies the maximum current, in amps, that the output can produce when generating the desired pulse voltage on the specified channel(s) during the off phase of a pulse.
- [Source:Pulse Voltage:Pulse Bias Current Limit Low](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlimitlow.html) Specifies the minimum current, in amps, that the output can produce when generating the desired pulse voltage on the specified channel(s) during the off phase of a pulse.
- [Source:Pulse Voltage:Pulse Current Limit Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlimitrange.html) Specifies the pulse current limit range, in amps, for the specified channel(s).
- [Source:Pulse Current:Pulse Current Level](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlevel.html) Specifies the pulse current level, in amps, that the device attempts to generate on the specified channel(s) during the on phase of a pulse.
- [Source:Pulse Current:Pulse Bias Current Level](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlevel.html) Specifies the pulse bias current level, in amps, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
- [Source:Pulse Current:Pulse Current Level Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecurrentlevelrange.html) Specifies the pulse current level range, in amps, for the specified channel(s).
- [Source:Pulse Current:Pulse Voltage Limit](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimit.html) Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current on the specified channel(s) during the on phase of a pulse. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.
- [Source:Pulse Current:Pulse Voltage Limit High](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimithigh.html) Specifies the maximum voltage, in volts, that the output can produce when generating the desired pulse current on the specified channel(s) during the on phase of a pulse.
- [Source:Pulse Current:Pulse Voltage Limit Low](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimitlow.html) Specifies the minimum voltage, in volts, that the output can produce when generating the desired pulse current on the specified channel(s) during the on phase of a pulse.
- [Source:Pulse Current:Pulse Bias Voltage Limit](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelimit.html) Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current on the specified channel(s) during the off phase of a pulse. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.
- [Source:Pulse Current:Pulse Bias Voltage Limit High](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelimithigh.html) Specifies the maximum voltage, in volts, that the output can produce when generating the desired pulse current on the specified channel(s) during the off phase of a pulse.
- [Source:Pulse Current:Pulse Bias Voltage Limit Low](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasvoltagelimitlow.html) Specifies the minimum voltage, in volts, that the output can produce when generating the desired pulse current on the specified channel(s) during the off phase of a pulse.
- [Source:Pulse Current:Pulse Voltage Limit Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsevoltagelimitrange.html) Specifies the pulse voltage limit range, in volts, for the specified channel(s).
- [Source:Constant Resistance:Level](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancelevel.html) Specifies the resistance level, in ohms, that the device attempts to generate on the specified channel(s).
- [Source:Constant Resistance:Level Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancelevelrange.html) Specifies the resistance level range, in ohms, for the specified channel(s).
- [Source:Constant Resistance:Current Limit](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancecurrentlimit.html) Specifies the current limit, in amps, that the output cannot exceed when generating the desired resistance level on the specified channel(s).
- [Source:Constant Power:Level](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowerlevel.html) Specifies the power level, in watts, that the device attempts to generate on the specified channel(s).
- [Source:Constant Power:Level Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowerlevelrange.html) Specifies the power level range, in watts, for the specified channel(s).
- [Source:Constant Power:Current Limit](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowercurrentlimit.html) Specifies the current limit, in amps, that the output cannot exceed when generating the desired power level on the specified channel(s).
- [Source:Advanced:Source Delay](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcedelay.html) Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the Measure When property is set to Automatically After Source Complete .
- [Source:Advanced:Pulse Bias Delay](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiasdelay.html) Determines when, in seconds, the device generates the Pulse Complete event after generating the off level of a pulse.
- [Source:Advanced:Pulse On Time](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulseontime.html) Determines the length, in seconds, of the on phase of a pulse.
- [Source:Advanced:Pulse Off Time](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulseofftime.html) Determines the length, in seconds, of the off phase of a pulse.
- [Source:Advanced:OVP Enabled](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-ovpenabled.html) Enables (TRUE) or disables (FALSE) overvoltage protection (OVP).
- [Source:Advanced:OVP Limit](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-ovplimit.html) Determines the voltage limit, in volts, beyond which overvoltage protection (OVP) engages. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. For example, setting the OVP Limit to 65 will configure the OVP feature to trigger an OVP error if the output exceeds ±65 V.
- [Source:Advanced:Overranging Enabled](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-overrangingenabled.html) Specifies whether NI-DCPower allows setting the voltage level , current level , voltage limit , and current limit outside the device specification limits. TRUE means that overranging is enabled.
- [Source:Advanced:Output Capacitance](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcapacitance.html) Specifies whether to use a low or high capacitance on the output for the specified channel(s).
- [Source:Advanced:Sequence Loop Count](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceloopcount.html) Specifies the number of times a sequence is run after initiation.
- [Source:Advanced:Sequence Loop Count Is Finite](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceloopcountisfinite.html) Specifies whether a sequence should repeat indefinitely.
- [Source:Advanced:Active Advanced Sequence](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-activeadvancedsequence.html) Specifies the advanced sequence to configure or generate.
- [Source:Advanced:Active Advanced Sequence Step](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-activeadvancedsequencestep.html) Specifies the advanced sequence step to configure.
- [Source:Advanced:Compliance Limit Symmetry](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-compliancelimitsymmetry.html) Specifies whether compliance limits for current generation and voltage generation for the device are applied symmetrically about 0 V and 0 A or asymmetrically with respect to 0 V and 0 A.
- [Source:Advanced:Sequence Step Delta Time](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequencestepdeltatime.html) Specifies the amount of time, in seconds, between the start of two consecutive steps in a sequence.
- [Source:Advanced:Sequence Step Delta Time Enabled](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequencestepdeltatimeenabled.html) Specifies whether the Sequence Step dt property is enabled (TRUE) or disabled (FALSE).
- [Source:Advanced:Requested Power Allocation](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-requestedpowerallocation.html) Specifies the power, in watts, to request the device to source from each active channel.
- [Source:Advanced:Actual Power Allocation](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-actualpowerallocation.html) Returns the power, in watts, the device is sourcing on each active channel if the Power Allocation Mode property is set to Automatic or Manual .
- [Source:Advanced:Power Allocation Mode](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powerallocationmode.html) Determines whether the device sources the power its source configuration requires or a specific wattage you request; determines whether NI-DCPower proactively checks that this sourcing power is within the maximum per-channel and overall sourcing power of the device.
- [Source:Advanced:Merged Channels](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-mergedchannels.html) Specifies the merge channel(s) to combine with a designated primary channel of an instrument in order to increase the maximum current you can source from the instrument.
- [Source:Advanced:Conduction Voltage:Mode](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-conductionvoltagemode.html) Specifies whether the conduction voltage feature is enabled on the specified channel(s).
- [Source:Advanced:Conduction Voltage:On Threshold](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-conductionvoltageonthreshold.html) Specifies the required minimum voltage, in volts, at the input of the specified channel(s) before the instrument starts sinking on the specified channel(s) when the conduction voltage feature is enabled.
- [Source:Advanced:Conduction Voltage:Off Threshold](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-conductionvoltageoffthreshold.html) Specifies the minimum voltage, in volts, at the input of the specified channel(s) below which the instrument stops sinking on the specified channel(s) when the conduction voltage feature is enabled.
- [Source:Advanced:Output Shorted](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputshorted.html) Specifies whether the input of the instrument simulates a short circuit.
- [Source:Output Cutoff:Enabled](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffenabled.html) Enables or disables output cutoff functionality. If enabled, you can define output cutoffs that, if exceeded, cause the output of the specified channel(s) to be disconnected.
- [Source:Output Cutoff:Voltage Output Limit High](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltageoutputlimithigh.html) Specifies a high limit voltage value, in volts, for output cutoff. If the voltage output exceeds this limit, the output is disconnected.
- [Source:Output Cutoff:Voltage Output Limit Low](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltageoutputlimitlow.html) Specifies a low limit voltage value, in volts, for output cutoff. If the voltage output falls below this limit, the output is disconnected.
- [Source:Output Cutoff:Voltage Measure Limit High](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagemeasurelimithigh.html) Specifies a high limit voltage value, in volts, for output cutoff. If the measured voltage exceeds this limit, the output is disconnected.
- [Source:Output Cutoff:Voltage Measure Limit Low](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagemeasurelimitlow.html) Specifies a low limit voltage value, in volts, for output cutoff. If the measured voltage falls below this limit, the output is disconnected.
- [Source:Output Cutoff:Current Measure Limit High](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentmeasurelimithigh.html) Specifies a high limit current value, in amps, for output cutoff. If the measured current exceeds this limit, the output is disconnected.
- [Source:Output Cutoff:Current Measure Limit Low](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentmeasurelimitlow.html) Specifies a low limit current value, in amps, for output cutoff. If the measured current falls below this limit, the output is disconnected.
- [Source:Output Cutoff:Voltage Change Limit High](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagechangelimithigh.html) Specifies a limit for positive voltage slew rate, in volts per microsecond, for output cutoff. If the voltage increases at a rate that exceeds this limit, the output is disconnected.
- [Source:Output Cutoff:Voltage Change Limit Low](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagechangelimitlow.html) Specifies a limit for negative voltage slew rate, in volts per microsecond, for output cutoff. If the voltage decreases at a rate that exceeds this limit, the output is disconnected.
- [Source:Output Cutoff:Current Change Limit High](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentchangelimithigh.html) Specifies a limit for positive current slew rate, in amps per microsecond, for output cutoff. If the current increases at a rate that exceeds this limit, the output is disconnected.
- [Source:Output Cutoff:Current Change Limit Low](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentchangelimitlow.html) Specifies a limit for negative current slew rate, in amps per microsecond, for output cutoff. If the current decreases at a rate that exceeds this limit, the output is disconnected.
- [Source:Output Cutoff:Current Overrange Enabled](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentoverrangeenabled.html) Enables or disables current overrange functionality for output cutoff. If enabled, the output is disconnected when the measured current saturates the current range.
- [Source:Output Cutoff:Delay](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffdelay.html) Delays disconnecting the output by the time you specify, in seconds, when a limit is exceeded.
- [Measurement:Sense](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sense.html) Selects either local or remote sensing of the output voltage for the specified channel(s).
- [Measurement:Auto Zero](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autozero.html) Specifies the auto-zero method to use on the device.
- [Measurement:Aperture Time Units](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-aperturetimeunits.html) Specifies the units of the Aperture Time property for the channel configuration.
- [Measurement:Aperture Time](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-aperturetime.html) Specifies the measurement aperture time for the channel configuration. Aperture time is specified in the units set by the Aperture Time Units property.
- [Measurement:Aperture Time Auto Mode](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-aperturetimeautomode.html) Automatically optimizes the measurement aperture time according to the actual current range when measurement autorange is enabled. Optimization accounts for power line frequency when the Aperture Time Units property is set to Power Line Cycles .
- [Measurement:Power Line Frequency](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powerlinefrequency.html) Specifies the power line frequency for specified channel(s). NI-DCPower uses this value to select a timebase for setting the Aperture Time property in power line cycles (PLCs).
- [Measurement:Samples To Average](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-samplestoaverage.html) Specifies the number of samples to average when you take a measurement.
- [Measurement:Measure Record Length](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurerecordlength.html) Specifies how many measurements compose a measure record. When this property is set to a value greater than 1, the Measure When property must be set to Automatically after Source Complete or On Measure Trigger .
- [Measurement:Measure Record Length Is Finite](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurerecordlengthisfinite.html) Specifies whether to take continuous measurements. Call the niDCPower Abort With Channels VI to stop continuous measurements. When this property is set to FALSE and the Source Mode property is set to Single Point , the Measure When property must be set to Automatically after Source Complete or On Measure Trigger . When this property is set to FALSE and the Source Mode property is set to Sequence , the Measure When property must be set to On Measure Trigger .
- [Measurement:Measure Record Delta Time](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurerecorddeltatime.html) Queries the amount of time, in seconds, between the start of two consecutive measurements in a measure record. Only query this property after the desired measurement settings are committed.
- [Measurement:Fetch Backlog](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-fetchbacklog.html) Returns the number of measurements acquired that have not been fetched yet.
- [Measurement:Autorange](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorange.html) Specifies whether the hardware automatically selects the best range to measure the signal.
- [Measurement:Advanced:Measure When](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurewhen.html) Specifies when the measure unit should acquire measurements. Unless this property is configured to On Measure Trigger , the Measure Trigger Type property is ignored.
- [Measurement:Advanced:Reset Average Before Measurement](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-resetaveragebeforemeasurement.html) Specifies whether the measurement returned from any measurement call starts with a new measurement call (TRUE) or returns a measurement that has already begun or completed (FALSE).
- [Measurement:Advanced:DC Noise Rejection](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-dcnoiserejection.html) Determines the relative weighting of samples in a measurement.
- [Measurement:Advanced:Measure Buffer Size](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurebuffersize.html) Specifies the number of samples that the active channel measurement buffer can hold.
- [Measurement:Advanced:Autorange Behavior](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangebehavior.html) Specifies the algorithm the hardware uses for measurement autoranging.
- [Measurement:Advanced:Autorange Aperture Time Mode](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeaperturetimemode.html) Specifies whether the aperture time used for the measurement autorange algorithm is determined automatically or customized using the Autorange Minimum Aperture Time property.
- [Measurement:Advanced:Autorange Minimum Aperture Time](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumaperturetime.html) Specifies the measurement autorange aperture time used for the measurement autorange algorithm.
- [Measurement:Advanced:Autorange Minimum Aperture Time Units](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumaperturetimeunits.html) Specifies the units of the Autorange Minimum Aperture Time property.
- [Measurement:Advanced:Autorange Minimum Current Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumcurrentrange.html) Specifies the lowest range used during measurement autoranging.
- [Measurement:Advanced:Autorange Minimum Voltage Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumvoltagerange.html) Specifies the lowest range used during measurement autoranging.
- [Measurement:Advanced:Autorange Threshold Mode](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangethresholdmode.html) Specifies thresholds used during autoranging to determine when range changing occurs.
- [Measurement:Advanced:Autorange Maximum Delay After Range Change](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangemaximumdelayafterrangechange.html) Balances between settling time and maximum measurement time by specifying the maximum time delay between when a range change occurs and when measurements resume.
- [Triggers:Start Trigger:Trigger Type](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-starttriggertype.html) Specifies the behavior of the Start trigger.
- [Triggers:Start Trigger:Export Output Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedstarttriggeroutputterminal.html) Specifies the output terminal for exporting the Start trigger.
- [Triggers:Start Trigger:Digital Edge:Edge](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-starttriggerdigitaledgeedge.html) Specifies whether to configure the Start trigger to assert on the rising or falling edge.
- [Triggers:Start Trigger:Digital Edge:Input Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-starttriggerdigitaledgeinputterminal.html) Specifies the input terminal for the Start trigger. This property is used only when the Start Trigger Type property is set to Digital Edge .
- [Triggers:Source Trigger:Trigger Type](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcetriggertype.html) Specifies the behavior of the Source trigger.
- [Triggers:Source Trigger:Export Output Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedsourcetriggeroutputterminal.html) Specifies the output terminal for exporting the Source trigger.
- [Triggers:Source Trigger:Digital Edge:Edge](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcetriggerdigitaledgeedge.html) Specifies whether to configure the Source trigger to assert on the rising or falling edge.
- [Triggers:Source Trigger:Digital Edge:Input Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcetriggerdigitaledgeinputterminal.html) Specifies the input terminal for the Source trigger. This property is used only when the Source Trigger Type property is set to Digital Edge .
- [Triggers:Measure Trigger:Trigger Type](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measuretriggertype.html) Specifies the behavior of the Measure trigger.
- [Triggers:Measure Trigger:Export Output Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedmeasuretriggeroutputterminal.html) Specifies the output terminal for exporting the Measure trigger.
- [Triggers:Measure Trigger:Digital Edge:Edge](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measuretriggerdigitaledgeedge.html) Specifies whether to configure the Measure trigger to assert on the rising or falling edge.
- [Triggers:Measure Trigger:Digital Edge:Input Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measuretriggerdigitaledgeinputterminal.html) Specifies the input terminal for the Measure trigger. This property is used only when the Measure Trigger Type property is set to Digital Edge .
- [Triggers:Sequence Advance Trigger:Trigger Type](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceadvancetriggertype.html) Specifies the behavior of the Sequence Advance trigger.
- [Triggers:Sequence Advance Trigger:Export Output Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedsequenceadvancetriggeroutputterminal.html) Specifies the output terminal for exporting the Sequence Advance trigger.
- [Triggers:Sequence Advance Trigger:Digital Edge:Edge](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceadvancetriggerdigitaledgeedge.html) Specifies whether to configure the Sequence trigger to assert on the rising or falling edge.
- [Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceadvancetriggerdigitaledgeinputterminal.html) Specifies the input terminal for the Sequence Advance trigger. This property is used only when the Sequence Advance Trigger Type property is set to Digital Edge .
- [Events:Source Complete Event:Output Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventoutputterminal.html) Specifies the output terminal for exporting the Source Complete event.
- [Events:Source Complete Event:Output Behavior](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventoutputbehavior.html) Specifies the output behavior for exporting the Source Complete event.
- [Events:Source Complete Event:Toggle:Initial State](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventtoggleinitialstate.html) Specifies the initial state of the Source Complete event if you set the Source Complete Event Output Behavior to Toggle Event Output .
- [Events:Source Complete Event:Pulse:Polarity](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventpulsepolarity.html) Specifies the behavior of the Source Complete event.
- [Events:Source Complete Event:Pulse:Width](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sourcecompleteeventpulsewidth.html) Specifies the width of the Source Complete event, in seconds.
- [Events:Measure Complete Event:Output Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventoutputterminal.html) Specifies the output terminal for exporting the Measure Complete event.
- [Events:Measure Complete Event:Output Behavior](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventoutputbehavior.html) Specifies the output behavior for exporting the Measure Complete event.
- [Events:Measure Complete Event:Toggle:Initial State](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventtoggleinitialstate.html) Specifies the initial state of the Measure Complete event if you set the Measure Complete Event Output Behavior to Toggle Event Output .
- [Events:Measure Complete Event:Event Delay](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventeventdelay.html) Specifies the amount of time to delay the generation of the Measure Complete event, in seconds.
- [Events:Measure Complete Event:Pulse:Polarity](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventpulsepolarity.html) Specifies the behavior of the Measure Complete event.
- [Events:Measure Complete Event:Pulse:Width](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventpulsewidth.html) Specifies the width of the Measure Complete event, in seconds.
- [Events:Sequence Iteration Complete Event:Output Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventoutputterminal.html) Specifies the output terminal for exporting the Sequence Iteration Complete event.
- [Events:Sequence Iteration Complete Event:Output Behavior](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventoutputbehavior.html) Specifies the output behavior for exporting the Sequence Iteration Complete event.
- [Events:Sequence Iteration Complete Event:Toggle:Initial State](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventtoggleinitialstate.html) Specifies the initial state of the Sequence Iteration Complete event if you set the Sequence Iteration Complete Event Output Behavior to Toggle Event Output .
- [Events:Sequence Iteration Complete Event:Pulse:Polarity](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventpulsepolarity.html) Specifies the behavior of the Sequence Iteration Complete event.
- [Events:Sequence Iteration Complete Event:Pulse:Width](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceiterationcompleteeventpulsewidth.html) Specifies the width of the Sequence Iteration Complete event, in seconds.
- [Events:Sequence Engine Done Event:Output Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventouputterminal.html) Specifies the output terminal for exporting the Sequence Engine Done Complete event.
- [Events:Sequence Engine Done Event:Output Behavior](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventoutputbehavior.html) Specifies the output behavior for exporting the Sequence Engine Done event.
- [Events:Sequence Engine Done Event:Toggle:Initial State](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventtoggleinitialstate.html) Specifies the initial state of the Sequence Engine Done event if you set the Sequence Engine Done Event Output Behavior to Toggle Event Output .
- [Events:Sequence Engine Done Event:Pulse:Polarity](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventpulsepolarity.html) Specifies the behavior of the Sequence Engine Done event.
- [Events:Sequence Engine Done Event:Pulse:Width](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-sequenceenginedoneeventpulsewidth.html) Specifies the width of the Sequence Engine Done event, in seconds.
- [Triggers:Pulse Trigger:Trigger Type](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsetriggertype.html) Specifies the behavior of the Pulse trigger.
- [Triggers:Pulse Trigger:Export Output Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedpulsetriggeroutputterminal.html) Specifies the output terminal for exporting the Pulse trigger.
- [Triggers:Pulse Trigger:Digital Edge:Edge](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsetriggerdigitaledgeedge.html) Specifies whether to configure the Pulse trigger to assert on the rising or falling edge.
- [Triggers:Pulse Trigger:Digital Edge:Input Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsetriggerdigitaledgeinputterminal.html) Specifies the input terminal for the Pulse trigger. This property is used only when the Pulse Trigger Type property is set to Digital Edge .
- [Events:Pulse Complete Event:Output Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecompleteeventouputterminal.html) Specifies the output terminal for exporting the Pulse Complete event.
- [Events:Pulse Complete Event:Pulse:Polarity](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecompleteeventpulsepolarity.html) Specifies the behavior of the Pulse Complete event.
- [Events:Pulse Complete Event:Pulse:Width](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsecompleteeventpulsewidth.html) Specifies the width of the Pulse Complete event, in seconds.
- [Events:Ready For Pulse Trigger Event:Output Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-readyforpulsetriggereventouputterminal.html) Specifies the output terminal for exporting the Ready For Pulse Trigger event.
- [Events:Ready For Pulse Trigger Event:Pulse:Polarity](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-readyforpulsetriggereventpulsepolarity.html) Specifies the behavior of the Ready For Pulse Trigger event.
- [Events:Ready For Pulse Trigger Event:Pulse:Width](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-readyforpulsetriggereventpulsewidth.html) Specifies the width of the Ready For Pulse Trigger event, in seconds.
- [Triggers:Shutdown Trigger:Trigger Type](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-shutdowntriggertype.html) Specifies the behavior of the Shutdown trigger.
- [Triggers:Shutdown Trigger:Digital Edge:Edge](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-shutdowntriggerdigitaledgeedge.html) Specifies whether to configure the Shutdown trigger to assert on the rising or falling edge.
- [Triggers:Shutdown Trigger:Digital Edge:Input Terminal](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-shutdowntriggerdigitaledgeinputterminal.html) Specifies the input terminal for the Shutdown trigger. This property is used only when the Shutdown Trigger Type property is set to Digital Edge .
- [LCR:Instrument Mode](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-instrumentmode.html) Specifies the mode of operation for an instrument channel for instruments that support multiple modes.
- [LCR:Source Delay Mode](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrsourcedelaymode.html) For instruments in LCR mode, determines whether NI-DCPower automatically calculates and applies the source delay or applies a source delay you set manually.
- [LCR:Measurement Time](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrmeasurementtime.html) Selects a general aperture time profile for LCR measurements.
- [LCR:Custom Measurement Time](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrcustommeasurementtime.html) Specifies the LCR measurement aperture time for a channel, in seconds, when the LCR Measurement Time property is set to Custom .
- [LCR:AC Stimulus:Function](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrstimulusfunction.html) Specifies the type of test signal to apply to the DUT for LCR measurements.
- [LCR:AC Stimulus:Frequency](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrfrequency.html) Specifies the frequency of the AC test signal applied to the DUT for LCR measurements.
- [LCR:AC Stimulus:Voltage Amplitude](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrvoltageamplitude.html) Specifies the amplitude, in V RMS, of the AC voltage test signal applied to the DUT for LCR measurements.
- [LCR:AC Stimulus:Current Amplitude](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrcurrentamplitude.html) Specifies the amplitude, in A RMS, of the AC current test signal applied to the DUT for LCR measurements.
- [LCR:AC Stimulus:Automatic Level Control](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrautomaticlevelcontrol.html) Specifies whether the channel actively attempts to maintain a constant test voltage or current across the DUT for LCR measurements.
- [LCR:AC Stimulus:Advanced:Voltage Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrvoltagerange.html) Specifies the voltage range, in volts RMS, that defines the values to which you can set the LCR Voltage Amplitude for the specified channel(s).
- [LCR:AC Stimulus:Advanced:Current Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrcurrentrange.html) Specifies the current range, in amps RMS, that defines the values to which you can set the LCR Current Amplitude for the specified channel(s).
- [LCR:AC Stimulus:Advanced:Dither Enabled](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcracditherenabled.html) Specifies whether dithering is enabled during LCR measurements.
- [LCR:AC Stimulus:Advanced:Source Aperture Time](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrsourceaperturetime.html) Specifies the LCR source aperture time, in seconds, for a channel in LCR mode.
- [LCR:DC Bias:Source](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrdcbiassource.html) Specifies how to apply DC bias for LCR measurements.
- [LCR:DC Bias:Voltage Level](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrdcbiasvoltagelevel.html) Specifies the DC bias voltage level, in volts, when the LCR DC Bias Source is set to Voltage .
- [LCR:DC Bias:Current Level](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrdcbiascurrentlevel.html) Specifies the DC bias current level, in amperes, when the LCR DC Bias Source is set to Current .
- [LCR:DC Bias:Automatic Level Control](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrdcbiasautomaticlevelcontrol.html) Specifies whether the channel actively maintains a constant DC bias voltage or current across the DUT for LCR measurements.
- [LCR:DC Bias:Advanced:Voltage Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrdcbiasvoltagerange.html) Specifies the voltage range, in volts, that defines the values to which you can set the LCR DC Bias Voltage Level for the specified channel(s).
- [LCR:DC Bias:Advanced:Current Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrdcbiascurrentrange.html) Specifies the current range, in amps, that defines the values to which you can set the LCR DC Bias Current Level for the specified channel(s).
- [LCR:DC Bias:Advanced:Transient Response](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrdcbiastransientresponse.html) For instruments in LCR mode, determines whether NI-DCPower automatically calculates and applies the transient response values for DC bias or applies the transient response you set manually.
- [LCR:Compensation:Open:Enabled](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcropencompensationenabled.html) Specifies whether to apply open LCR compensation data to LCR measurements.
- [LCR:Compensation:Open:Conductance](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcropenconductance.html) Specifies the conductance, in siemens, of the circuit used for open LCR compensation.
- [LCR:Compensation:Open:Susceptance](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcropensusceptance.html) Specifies the susceptance, in siemens, of the circuit used for open LCR compensation.
- [LCR:Compensation:Short:Enabled](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrshortcompensationenabled.html) Specifies whether to apply short LCR compensation data to LCR measurements.
- [LCR:Compensation:Short:Resistance](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrshortresistance.html) Specifies the resistance, in ohms, of the circuit used for short LCR compensation.
- [LCR:Compensation:Short:Reactance](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrshortreactance.html) Specifies the reactance, in ohms, of the circuit used for short LCR compensation.
- [LCR:Compensation:Load:Enabled](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadcompensationenabled.html) Specifies whether to apply load LCR compensation data to LCR measurements.
- [LCR:Compensation:Load:Measured Resistance](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrmeasuredloadresistance.html) Specifies the resistance, in ohms, of the load used for load LCR compensation as measured by the instrument.
- [LCR:Compensation:Load:Measured Reactance](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrmeasuredloadreactance.html) Specifies the reactance, in ohms, of the load used for load LCR compensation as measured by the instrument.
- [LCR:Compensation:Load:Actual Resistance](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcractualloadresistance.html) Specifies the actual resistance, in ohms, of the load used for load LCR compensation.
- [LCR:Compensation:Load:Actual Reactance](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcractualloadreactance.html) Specifies the actual reactance, in ohms, of the load used for load LCR compensation.
- [LCR:Compensation:LCR Open/Short/Load Compensation Data Source](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcropenshortloadcompensationdatasource.html) Specifies the source of the LCR compensation data NI-DCPower applies to LCR measurements.
- [LCR:Compensation:LCR Short Custom Cable Compensation Enabled](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrshortcustomcablecompensationenabled.html) Defines how to apply short custom cable compensation in LCR mode when Cable Length is set to Custom (Onboard Storage) or Custom (As Configured) .
- [LCR:Compensation:LCR AC Electrical Cable Length Delay](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcracelectricalcablelengthdelay.html) Specifies the one-way electrical length delay of the cable, in seconds.
- [LCR:Impedance Range:Impedance Range](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrimpedancerange.html) Specifies the impedance range the channel uses for LCR measurements.
- [LCR:Impedance Range:Impedance Autorange](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrimpedanceautorange.html) Defines whether an instrument in LCR mode automatically selects the best impedance range for each given LCR measurement.
- [LCR:Impedance Range:Advanced:Impedance Range Source](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrimpedancerangesource.html) Specifies how the impedance range for LCR measurements is determined.
- [LCR:Impedance Range:Advanced:Load Resistance](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadresistance.html) Specifies the load resistance, in ohms and assuming a series model, of the DUT in order to compute the impedance range when the LCR Impedance Range Source is set to LCR Load Configuration .
- [LCR:Impedance Range:Advanced:Load Inductance](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadinductance.html) Specifies the load inductance, in henrys and assuming a series model, of the DUT in order to compute the impedance range when the LCR Impedance Range Source is set to LCR Load Configuration .
- [LCR:Impedance Range:Advanced:Load Capacitance](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadcapacitance.html) Specifies the load capacitance, in farads and assuming a series model, of the DUT in order to compute the impedance range when the LCR Impedance Range Source is set to LCR Load Configuration .
- [Device Specific:LCR:Cable Length](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-cablelength.html) Specifies how to apply cable compensation data for instruments that support LCR functionality.
- [Advanced:Power Source](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powersource.html) For sessions initialized with deprecated Initialize VIs, this property specifies the power source to use. NI-DCPower switches the power source used by the device to the specified value.
- [Advanced:Power Source In Use](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powersourceinuse.html) Indicates whether the device is using the internal or auxiliary power source to generate power.
- [Advanced:Auxiliary Power Source Available](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-auxiliarypowersourceavailable.html) Indicates whether an auxiliary power source is connected to the device.
- [Advanced:Self-Calibration Persistence](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-selfcalibrationpersistence.html) Specifies whether the values calculated during self-calibration should be written to hardware to be used until the next self-calibration or only used until the niDCPower Reset Device VI is called or the machine is powered down.
- [Advanced:Interlock Input Open](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-interlockinputopen.html) Indicates whether the safety interlock circuit is open.
- [Advanced:Isolation State](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-isolationstate.html) Defines whether the channel is isolated.
- [Inherent IVI Attributes:User Options:Range Check](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-rangecheck.html) Specifies whether to validate property values and VI parameters.
- [Inherent IVI Attributes:User Options:Query Instrument Status](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-queryinstrumentstatus.html) Specifies whether NI-DCPower queries instrument status after each operation.
- [Inherent IVI Attributes:User Options:Cache](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-cache.html) Specifies whether to cache the value of properties.
- [Inherent IVI Attributes:User Options:Simulate](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-simulate.html) Specifies whether to simulate NI-DCPower I/O operations. TRUE specifies that operation is simulated.
- [Inherent IVI Attributes:User Options:Record Value Coercions](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-recordvaluecoercions.html) Specifies whether the IVI engine records the value coercions it makes for ViInt32 and ViReal64 properties.
- [Inherent IVI Attributes:User Options:Interchange Check](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-interchangecheck.html) Specifies whether to perform interchangeability checking and log interchangeability warnings when you call NI-DCPower VIs. TRUE specifies that interchangeability checking is enabled.
- [Inherent IVI Attributes:Driver Identification:Description](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-description.html) Contains a brief description of the specific driver.
- [Inherent IVI Attributes:Driver Identification:Driver Prefix](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-driverprefix.html) Contains the prefix for NI-DCPower. The name of each user-callable VI in NI-DCPower begins with this prefix.
- [Inherent IVI Attributes:Driver Identification:Driver Vendor](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-drivervendor.html) Contains the name of the vendor that supplies NI-DCPower.
- [Inherent IVI Attributes:Driver Identification:Revision](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-revision.html) Contains additional version information about NI-DCPower.
- [Inherent IVI Attributes:Driver Identification:Class Specification Major Version](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-classspecificationmajorversion.html) Contains the major version number of the class specification with which NI-DCPower is compliant.
- [Inherent IVI Attributes:Driver Identification:Class Specification Minor Version](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-classspecificationminorversion.html) Contains the minor version number of the class specification with which NI-DCPower is compliant.
- [Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-supportedinstrumentmodels.html) Contains a comma-separated (,) list of supported NI-DCPower device models.
- [Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-classgroupcapabilities.html) Contains a comma-separated (,) list of class-extension groups that NI-DCPower implements.
- [Inherent IVI Attributes:Driver Capabilities:Channel Count](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-channelcount.html) Indicates the number of channels in the session. For channel-based properties, the IVI engine maintains a separate cache value for each channel.
- [Inherent IVI Attributes:Instrument Identification:Manufacturer](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-manufacturer.html) Contains the name of the manufacturer for the instrument you are currently using.
- [Inherent IVI Attributes:Instrument Identification:Model](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-model.html) Contains the model number or name of the instrument you are currently using.
- [Inherent IVI Attributes:Instrument Identification:Firmware Revision](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-firmwarerevision.html) Contains the firmware revision information for the instrument you are currently using.
- [Inherent IVI Attributes:Instrument Identification:Serial Number](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-serialnumber.html) Contains the serial number information for the device you are currently using.
- [Inherent IVI Attributes:Advanced Session Information:Driver Setup](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-driversetup.html) Indicates the Driver Setup string that you specified when initializing the driver.
- [Inherent IVI Attributes:Advanced Session Information:Logical Name](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-logicalname.html) Contains the logical name(s) you specified when opening the current IVI session.
- [Inherent IVI Attributes:Advanced Session Information:Resource Descriptor](../../../instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-resourcedescriptor.html) Indicates the resource descriptor NI-DCPower uses to identify the resource(s) used by the NI-DCPower session.

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-activeadvancedsequence.html language=enus -->
## TOPIC 00115: Source:Advanced:Active Advanced Sequence

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-activeadvancedsequence.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-activeadvancedsequence.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the advanced sequence to configure or generate. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Remarks The following table lists the characteristics of this property. Short Name Active Advanced Sequence Data t

### Source:Advanced:Active Advanced Sequence

Specifies the advanced sequence to configure or generate.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Active Advanced Sequence |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-activeadvancedsequencestep.html language=enus -->
## TOPIC 00116: Source:Advanced:Active Advanced Sequence Step

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-activeadvancedsequencestep.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-activeadvancedsequencestep.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the advanced sequence step to configure. Sequence steps are zero-indexed. To configure the Commit step, enter -1 . This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Remarks The following table lists the character

### Source:Advanced:Active Advanced Sequence Step

Specifies the advanced sequence step to configure.

Sequence steps are zero-indexed. To configure the Commit step, enter
 -1
 .

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Active Advanced Sequence Step |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-activechannel.html language=enus -->
## TOPIC 00117: Active Channel

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-activechannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-activechannel.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel(s) used to access all subsequent channel-based properties in this property node. Specify the channel(s) before setting channel-based properties and use the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3 , where PXI1Slot3 and PXI1Slot4 ar

### Active Channel

Specifies the channel(s) used to access all subsequent channel-based properties in this property node.

Specify the channel(s) before setting channel-based properties and use the form
 PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3
 or
 PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3
 , where
 PXI1Slot3
 and
 PXI1Slot4
 are instrument resource names and 0, 2, and 3 are channels.

For instrument-based properties, you can also specify an instrument with the form
 PXI1Slot3
 .

Specifying
 ""
 (empty string) or omitting this property has the following effects, depending on the property type:

- Channel-based properties: applies properties for all channels in the session
- Instrument-based properties: applies properties for all instruments in the session

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Active Channel |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-actualpowerallocation.html language=enus -->
## TOPIC 00118: Source:Advanced:Actual Power Allocation

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-actualpowerallocation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-actualpowerallocation.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power, in watts, the device is sourcing on each active channel if the Power Allocation Mode property is set to Automatic or Manual . NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectiv

### Source:Advanced:Actual Power Allocation

Returns the power, in watts, the device is sourcing on each active channel if the
 [Power Allocation Mode](/csh?topicname=pnidcpower-powerallocationmode.html)
 property is set to
 **Automatic**
 or
 **Manual**
 .

Note

Note

Supported Properties by Device

**Valid Values**
 : [0, device per-channel maximum power]

Note

Power Allocation Mode

Disabled

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Actual Power Allocation |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-aperturetime.html language=enus -->
## TOPIC 00119: Measurement:Aperture Time

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-aperturetime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-aperturetime.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement aperture time for the channel configuration. Aperture time is specified in the units set by the Aperture Time Units property. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer

### Measurement:Aperture Time

Specifies the measurement aperture time for the channel configuration. Aperture time is specified in the units set by the
 [Aperture Time Units](/csh?topicname=pnidcpower-aperturetimeunits.html)
 property.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Aperture Time |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Aperture Time |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-aperturetimeautomode.html language=enus -->
## TOPIC 00120: Measurement:Aperture Time Auto Mode

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-aperturetimeautomode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-aperturetimeautomode.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Automatically optimizes the measurement aperture time according to the actual current range when measurement autorange is enabled. Optimization accounts for power line frequency when the Aperture Time Units property is set to Power Line Cycles. This property is not supported by all devices. Refer to

### Measurement:Aperture Time Auto Mode

Automatically optimizes the measurement aperture time according to the
 actual current range when measurement autorange is enabled. Optimization
 accounts for power line frequency when the
 [Aperture Time Units](/csh?topicname=pnidcpower-aperturetimeunits.html)
 property is set to **Power Line Cycles**.

Note

Supported Properties by Device

**Default Value**: Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Voltage** and
 the [Autorange](pnidcpower-autorange.html) property
 is set to **On**.

**Related topics:**

[Autorange](pnidcpower-autorange.html)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Aperture Time Auto Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Off | 1135 | Disables automatic aperture time scaling. The Aperture Time property specifies the aperture time for all ranges. |
| --- | --- | --- |
| Short | 1136 | Prioritizes measurement speed over measurement accuracy by quickly scaling down aperture time in larger current ranges. The Aperture Time property specifies the aperture time for the minimum range. |
| Normal | 1137 | Balances measurement accuracy and speed by scaling down aperture time in larger current ranges. The Aperture Time property specifies the aperture time for the minimum range. |
| Long | 1138 | Prioritizes accuracy while still decreasing measurement time by slowly scaling down aperture time in larger current ranges. The Aperture Time property specifies the aperture time for the minimum range. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-aperturetimeunits.html language=enus -->
## TOPIC 00121: Measurement:Aperture Time Units

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-aperturetimeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-aperturetimeunits.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of the Aperture Time property for the channel configuration. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by device. Rem

### Measurement:Aperture Time Units

Specifies the units of the
 [Aperture Time](/csh?topicname=pnidcpower-aperturetime.html)
 property for the channel configuration.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Aperture Time Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Aperture Time |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Seconds | 1028 | Specifies aperture time in seconds. |
| --- | --- | --- |
| Power Line Cycles | 1029 | Specifies aperture time in power line cycles (PLCs). |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorange.html language=enus -->
## TOPIC 00122: Measurement:Autorange

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the hardware automatically selects the best range to measure the signal. Note the highest range the algorithm uses is dependent on the corresponding limit range property. The algorithm the hardware uses can be controlled using the Autorange Aperture Time Mode property. This propert

### Measurement:Autorange

Specifies whether the hardware automatically selects the best range to measure the signal.

Note the highest range the algorithm uses is dependent on the corresponding limit range property. The algorithm the hardware uses can be controlled using the
 [Autorange Aperture Time Mode](pnidcpower-autorangeaperturetimemode.html)
 property.

Note

Supported Properties by Device

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Autorange |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Off | 0 | The hardware does not select the range. |
| --- | --- | --- |
| On | 1 | The hardware selects the range based on the compliance range and autorange properties. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeaperturetimemode.html language=enus -->
## TOPIC 00123: Measurement:Advanced:Autorange Aperture Time Mode

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeaperturetimemode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeaperturetimemode.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the aperture time used for the measurement autorange algorithm is determined automatically or customized using the Autorange Minimum Aperture Time property. This property is not supported by all devices. Refer to the Supported Properties by Device for information about devices that

### Measurement:Advanced:Autorange Aperture Time Mode

Specifies whether the aperture time used for the measurement autorange algorithm is determined automatically or customized using the
 [Autorange Minimum Aperture Time](/csh?topicname=pnidcpower-autorangeminimumaperturetime.html)
 property.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Autorange Aperture Time Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Auto | 1110 | NI-DCPower optimizes the aperture time for the autorange algorithm based on the module range. |
| --- | --- | --- |
| Custom | 1111 | The user specifies a minimum aperture time for the algorithm using the Autorange Minimum Aperture Time property and the corresponding Autorange Minimum Aperture Time Units property. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangebehavior.html language=enus -->
## TOPIC 00124: Measurement:Advanced:Autorange Behavior

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangebehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangebehavior.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the algorithm the hardware uses for measurement autoranging. This property is not supported by all devices. Refer to the Supported Properties by Device for information about devices that support this attribute. Remarks The following table lists the characteristics of this property. Short N

### Measurement:Advanced:Autorange Behavior

Specifies the algorithm the hardware uses for measurement autoranging.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Autorange Behavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Range Up To Limit Then Down | 1107 | >Go to the range limit then range down as needed until measured value is within thresholds. |
| --- | --- | --- |
| Range Up | 1108 | Go up one range when the upper threshold is reached. |
| Range Up And Down | 1109 | Go up or down one range when the upper/lower threshold is reached. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangemaximumdelayafterrangechange.html language=enus -->
## TOPIC 00125: Measurement:Advanced:Autorange Maximum Delay After Range Change

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangemaximumdelayafterrangechange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangemaximumdelayafterrangechange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Balances between settling time and maximum measurement time by specifying the maximum time delay between when a range change occurs and when measurements resume. Valid Values: The minimum and maximum values of this property are hardware-dependent. PXIe-4135/4136/4137: 0 to 9 seconds PXIe-4138/4139:

### Measurement:Advanced:Autorange Maximum Delay After Range Change

Balances between settling time and maximum measurement time by specifying the maximum time delay between when a range change occurs and when measurements resume.

**Valid Values**: The minimum and maximum values of this property are hardware-dependent.

- PXIe-4135/4136/4137: 0 to 9 seconds
- PXIe-4138/4139: 0 to 9 seconds
- PXIe-4147: 0 to 9 seconds
- PXIe-4163: 0 to 0.1 seconds

**Default Value**: Refer to [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) for the default value by device.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Autorange Maximum Delay After Range Change |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumaperturetime.html language=enus -->
## TOPIC 00126: Measurement:Advanced:Autorange Minimum Aperture Time

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumaperturetime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumaperturetime.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement autorange aperture time used for the measurement autorange algorithm. The aperture time is specified in the units set by the Autorange Minimum Aperture Time Units property. This value will typically be smaller than the aperture time used for measurements. For smaller ranges

### Measurement:Advanced:Autorange Minimum Aperture Time

Specifies the measurement autorange aperture time used for the measurement autorange algorithm.

The aperture time is specified in the units set by the
 [Autorange Minimum Aperture Time Units](pnidcpower-autorangeminimumaperturetimeunits.html)
 property. This value will typically be smaller than the aperture time used for measurements.

Note

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Autorange Minimum Aperture Time |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumaperturetimeunits.html language=enus -->
## TOPIC 00127: Measurement:Advanced:Autorange Minimum Aperture Time Units

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumaperturetimeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumaperturetimeunits.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of the Autorange Minimum Aperture Time property. This attribute is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Remarks The following table lists the characteristics of this property. Short Name Autorange Minimum A

### Measurement:Advanced:Autorange Minimum Aperture Time Units

Specifies the units of the
 [Autorange Minimum Aperture Time](/csh?topicname=pnidcpower-autorangeminimumaperturetime.html)
 property.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Autorange Minimum Aperture Time Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Seconds | 1028 | Specifies aperture time in seconds. |
| --- | --- | --- |
| Power Line Cycles | 1029 | Specifies aperture time in power line cycles (PLCs). |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumcurrentrange.html language=enus -->
## TOPIC 00128: Measurement:Advanced:Autorange Minimum Current Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumcurrentrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumcurrentrange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lowest range used during measurement autoranging. Limiting the lowest range used during autoranging can improve the speed of the autoranging algorithm and minimize frequent and unpredictable range changes for noisy signals. The maximum range used is the range that includes the value sp

### Measurement:Advanced:Autorange Minimum Current Range

Specifies the lowest range used during measurement autoranging.

Limiting the lowest range used during autoranging can improve the speed of the autoranging algorithm and minimize frequent and unpredictable range changes for noisy signals.

Note

Voltage Limit
 Range

Current Limit
 Range

Output Function

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Autorange Minimum Current Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumvoltagerange.html language=enus -->
## TOPIC 00129: Measurement:Advanced:Autorange Minimum Voltage Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumvoltagerange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangeminimumvoltagerange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lowest range used during measurement autoranging. Limiting the lowest range used during autoranging can improve the speed of the autoranging algorithm and minimize frequent and unpredictable range changes for noisy signals. The maximum range used is the range that includes the value sp

### Measurement:Advanced:Autorange Minimum Voltage Range

Specifies the lowest range used during measurement autoranging.

Limiting the lowest range used during autoranging can improve the speed of the autoranging algorithm and minimize frequent and unpredictable range changes for noisy signals.

Note

Voltage Limit Range

Current Limit Range

Output Function

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Autorange Minimum Voltage Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangethresholdmode.html language=enus -->
## TOPIC 00130: Measurement:Advanced:Autorange Threshold Mode

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangethresholdmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autorangethresholdmode.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies thresholds used during autoranging to determine when range changing occurs. This attribute is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Remarks The following table lists the characteristics of this property. Short Name Au

### Measurement:Advanced:Autorange Threshold Mode

Specifies thresholds used during autoranging to determine when range changing occurs.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Autorange Threshold Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Normal | 1112 | Thresholds are selected based on a balance between accuracy and hysteresis. |
| --- | --- | --- |
| Fast Step | 1113 | Optimized for faster changes in the measured signal. Thresholds are configured to be a smaller percentage of the range. |
| High Hysteresis | 1114 | Optimized for noisy signals to minimize frequent and unpredictable range changes. Thresholds are configured to be a larger percentage of the range. |
| Medium Hysteresis | 1115 | Optimized for noisy signals to minimize frequent and unpredictable range changes. Thresholds are configured to be a medium percentage of the range. |
| Hold | 1116 | Attempt to maintain the active range. Thresholds will favor the active range. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autozero.html language=enus -->
## TOPIC 00131: Measurement:Auto Zero

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autozero.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-autozero.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the auto-zero method to use on the device. Default Value :Refer to Supported Properties by Device for the default value by device. Remarks The following table lists the characteristics of this property. Short Name Auto Zero Data type ci32.png Permissions Read/Write High-level VIs niDCPower

### Measurement:Auto Zero

Specifies the auto-zero method to use on the device.

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto Zero |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Auto Zero |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Off | 0 | Disables auto-zero. |
| --- | --- | --- |
| Once | 1024 | Makes zero conversions following the first measurement after initiating the device. The device uses these zero conversions for the preceding measurement and future measurements until the device is reinitiated. |
| On | 1 | Makes zero conversions for every measurement. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-auxiliarypowersourceavailable.html language=enus -->
## TOPIC 00132: Advanced:Auxiliary Power Source Available

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-auxiliarypowersourceavailable.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-auxiliarypowersourceavailable.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether an auxiliary power source is connected to the device. This property is not supported in sessions initialized with independent channels. A value of FALSE may indicate that the auxiliary input fuse has blown. Refer to the Detecting Internal/Auxiliary Power topic in the NI DC Power Su

### Advanced:Auxiliary Power Source Available

Indicates whether an auxiliary power source is connected to the device.

Note

A value of FALSE may indicate that the auxiliary input fuse has blown. Refer to the
 [Detecting Internal/Auxiliary Power](/csh?context=nidcpower_ni_dc_power_supplies_help_detecting_internal_auxiliary_power)
 topic in the
 *NI DC Power Supplies and SMUs Help*
 for more information about internal and auxiliary power.

Note

Power Source In Use

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auxiliary Power Source Available |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-cablelength.html language=enus -->
## TOPIC 00133: Device Specific:LCR:Cable Length

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-cablelength.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-cablelength.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to apply cable compensation data for instruments that support LCR functionality. Supported instruments use cable compensation for the following operations: SMU mode: to stabilize DC current sourcing in the two smallest current ranges LCR mode: to compensate for the effects of cabling o

### Device Specific:LCR:Cable Length

Specifies how to apply cable compensation data for instruments that support LCR functionality.

Supported instruments use cable compensation for the following operations:

- SMU mode: to stabilize DC current sourcing in the two smallest current ranges
- LCR mode: to compensate for the effects of cabling on LCR measurements

Note

Supported Properties by Device

For NI standard options, select the length of your NI cable to apply compensation data for a typical cable of that type.

For custom options, choose the source of the custom cable compensation data. You must then generate the custom cable compensation data.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Cable Length |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| 0m | 1121 | Uses predefined cable compensation data for a 0m cable (direct connection). |
| --- | --- | --- |
| NI Standard 0.5m | 1153 | Uses predefined cable compensation data for an NI standard 0.5m coaxial cable. |
| NI Standard 1m | 1122 | Uses predefined cable compensation data for an NI standard 1m coaxial cable. |
| NI Standard 2m | 1123 | Uses predefined cable compensation data for an NI standard 2m coaxial cable. |
| NI Standard 4m | 1124 | Uses predefined cable compensation data for an NI standard 4m coaxial cable. |
| NI Standard Triaxial 1m | 1139 | Uses predefined cable compensation data for an NI standard 1m triaxial cable. |
| NI Standard Triaxial 2m | 1140 | Uses predefined cable compensation data for an NI standard 2m triaxial cable. |
| NI Standard Triaxial 4m | 1141 | Uses predefined cable compensation data for an NI standard 4m triaxial cable. |
| Custom (Onboard Storage) | 1125 | Uses previously generated custom cable compensation data from onboard storage. Only the most recently performed compensation data for each custom cable compensation type (open, short) is stored. |
| Custom (As Configured) | 1126 | Uses the custom cable compensation data supplied to Configure LCR Compensation. Use this option to manage multiple sets of custom cable compensation data. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-cache.html language=enus -->
## TOPIC 00134: Inherent IVI Attributes:User Options:Cache

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-cache.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-cache.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to cache the value of properties. When caching is enabled, NI-DCPower records the current instrument settings and avoids sending redundant commands to the instrument. Enabling caching can significantly increase execution speed. NI-DCPower might always cache or never cache particula

### Inherent IVI Attributes:User Options:Cache

Specifies whether to cache the value of properties.

When caching is enabled, NI-DCPower records the current instrument settings and avoids sending redundant commands to the instrument. Enabling caching can significantly increase execution speed.

NI-DCPower might always cache or never cache particular properties regardless of the setting of this property.

Use the
 [niDCPower Initialize With Independent Channels](/csh?context=nidcpower_nidcpowerviref_nidcpower_initialize_with_channels)
 VI to override this value.

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Cache |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-channelcount.html language=enus -->
## TOPIC 00135: Inherent IVI Attributes:Driver Capabilities:Channel Count

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-channelcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-channelcount.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of channels in the session. For channel-based properties, the IVI engine maintains a separate cache value for each channel. Remarks The following table lists the characteristics of this property. Short Name Channel Count Data type ci32.png Permissions Read Only High-level VIs N/

### Inherent IVI Attributes:Driver Capabilities:Channel Count

Indicates the number of channels in the session. For channel-based properties, the IVI engine maintains a separate cache value for each channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Channel Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-classgroupcapabilities.html language=enus -->
## TOPIC 00136: Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-classgroupcapabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-classgroupcapabilities.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains a comma-separated (,) list of class-extension groups that NI-DCPower implements. Remarks The following table lists the characteristics of this property. Short Name Class Group Capabilities Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Instrument-based No Reset

### Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities

Contains a comma-separated (,) list of class-extension groups that NI-DCPower implements.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Class Group Capabilities |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-classspecificationmajorversion.html language=enus -->
## TOPIC 00137: Inherent IVI Attributes:Driver Identification:Class Specification Major Version

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-classspecificationmajorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-classspecificationmajorversion.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the major version number of the class specification with which NI-DCPower is compliant. Remarks The following table lists the characteristics of this property. Short Name Class Specification Major Version Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based No Instrumen

### Inherent IVI Attributes:Driver Identification:Class Specification Major Version

Contains the major version number of the class specification with which NI-DCPower is compliant.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Class Specification Major Version |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-classspecificationminorversion.html language=enus -->
## TOPIC 00138: Inherent IVI Attributes:Driver Identification:Class Specification Minor Version

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-classspecificationminorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-classspecificationminorversion.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the minor version number of the class specification with which NI-DCPower is compliant. Remarks The following table lists the characteristics of this property. Short Name Class Specification Minor Version Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based No Instrumen

### Inherent IVI Attributes:Driver Identification:Class Specification Minor Version

Contains the minor version number of the class specification with which NI-DCPower is compliant.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Class Specification Minor Version |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-compliancelimitsymmetry.html language=enus -->
## TOPIC 00139: Source:Advanced:Compliance Limit Symmetry

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-compliancelimitsymmetry.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-compliancelimitsymmetry.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether compliance limits for current generation and voltage generation for the device are applied symmetrically about 0 V and 0 A or asymmetrically with respect to 0 V and 0 A. When set to Symmetric , voltage limits and current limits are set using a single property with a positive value.

### Source:Advanced:Compliance Limit Symmetry

Specifies whether compliance limits for current generation and voltage generation for the device are applied symmetrically about 0 V and 0 A or asymmetrically with respect to 0 V and 0 A.

When set to
 **Symmetric**
 , voltage limits and current limits are set using a single property with a positive value. The resulting range is bounded by this positive value and its opposite.

When set to
 **Asymmetric**
 , you must separately set a limit high and a limit low using distinct properties.

For asymmetric limits, the range bounded by the limit high and limit low must include zero.

Note

Supported Properties by Device

**Default Value:**
 Symmetric

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Compliance Limit Symmetry |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Symmetric | 0 | Compliance limits are specified symmetrically about 0. |
| --- | --- | --- |
| Asymmetric | 1 | Compliance limits can be specified asymmetrically with respect to 0. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-conductionvoltagemode.html language=enus -->
## TOPIC 00140: Source:Advanced:Conduction Voltage:Mode

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-conductionvoltagemode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-conductionvoltagemode.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the conduction voltage feature is enabled on the specified channel(s). When the conduction voltage feature is enabled: The instrument will not begin sinking on the specified channel(s) until the voltage at the input of the specified channel(s) rises above Conduction Voltage On Thre

### Source:Advanced:Conduction Voltage:Mode

Specifies whether the conduction voltage feature is enabled on the specified channel(s).

When the conduction voltage feature is enabled:

- The instrument will not begin sinking on the specified channel(s) until the voltage at the input of the specified channel(s) rises above
 Conduction Voltage On Threshold .
- The instrument will stop sinking on the specified channel(s) if the voltage at the input of the specified channel(s) falls below
 Conduction Voltage Off Threshold .

When the conduction voltage feature is disabled, the instrument will start sinking on the specified channel(s) regardless of the voltage at the input of the specified channel(s).

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Conduction Voltage Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Automatic | 1155 | The conduction voltage feature is only enabled when you set the Output Function property to DC Current or Constant Power. |
| --- | --- | --- |
| Enabled | 1156 | The conduction voltage feature is enabled. |
| Disabled | 1157 | The conduction voltage feature is disabled. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-conductionvoltageoffthreshold.html language=enus -->
## TOPIC 00141: Source:Advanced:Conduction Voltage:Off Threshold

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-conductionvoltageoffthreshold.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-conductionvoltageoffthreshold.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum voltage, in volts, at the input of the specified channel(s) below which the instrument stops sinking on the specified channel(s) when the conduction voltage feature is enabled. This property is not supported by all instruments. Refer to Supported Properties by Device for inform

### Source:Advanced:Conduction Voltage:Off Threshold

Specifies the minimum voltage, in volts, at the input of the specified channel(s) below which the instrument stops sinking on the specified channel(s) when the conduction voltage feature is enabled.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Conduction Voltage Off Threshold |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-conductionvoltageonthreshold.html language=enus -->
## TOPIC 00142: Source:Advanced:Conduction Voltage:On Threshold

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-conductionvoltageonthreshold.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-conductionvoltageonthreshold.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the required minimum voltage, in volts, at the input of the specified channel(s) before the instrument starts sinking on the specified channel(s) when the conduction voltage feature is enabled. This property is not supported by all instruments. Refer to Supported Properties by Device for i

### Source:Advanced:Conduction Voltage:On Threshold

Specifies the required minimum voltage, in volts, at the input of the specified channel(s) before the instrument starts sinking on the specified channel(s) when the conduction voltage feature is enabled.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Conduction Voltage On Threshold |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowercompensationfrequency.html language=enus -->
## TOPIC 00143: Source:Custom Transient Response:Constant Power:Compensation Frequency

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowercompensationfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowercompensationfrequency.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The frequency at which a pole-zero pair is added to the system when the Output Function property is set to Constant Power and the output current is below the current limit. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

### Source:Custom Transient Response:Constant Power:Compensation Frequency

The frequency at which a pole-zero pair is added to the system when the
 [Output Function](/csh?topicname=pnidcpower-outputfunction.html)
 property is set to
 **Constant Power**
 and the output current is below the current limit.

Note

Supported Properties by Device

Note

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Constant Power Compensation Freq |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowercurrentlimit.html language=enus -->
## TOPIC 00144: Source:Constant Power:Current Limit

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowercurrentlimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowercurrentlimit.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit, in amps, that the output cannot exceed when generating the desired power level on the specified channel(s). The device will operate in Constant Current mode if the current exceeds the specified limit. This property is applicable only if the Output Function property is se

### Source:Constant Power:Current Limit

Specifies the current limit, in amps, that the output cannot exceed when generating the desired power level on the specified channel(s).

The device will operate in Constant Current mode if the current exceeds the specified limit.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Constant Power**
 and the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Symmetric**
 .

Note

Output Enabled

Note

**Valid Values:**
 The valid values for this property are determined by the selected value for the
 [Constant Power Level Range](pnidcpower-constantpowerlevelrange.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Constant Power Current Limit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowergainbandwidth.html language=enus -->
## TOPIC 00145: Source:Custom Transient Response:Constant Power:Gain Bandwidth

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowergainbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowergainbandwidth.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the Output Function property is set to Constant Power and the output current is below the current limit. This property is not supported by all devices. Re

### Source:Custom Transient Response:Constant Power:Gain Bandwidth

The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes.
 This property takes effect when the
 [Output Function](/csh?topicname=pnidcpower-outputfunction.html)
 property is set to
 **Constant Power**
 and the output current is below the current limit.

Note

Supported Properties by Device

Note

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Constant Power GBW |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowerlevel.html language=enus -->
## TOPIC 00146: Source:Constant Power:Level

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowerlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowerlevel.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level, in watts, that the device attempts to generate on the specified channel(s). This property is applicable only if the Output Function property is set to Constant Power . The channel must be enabled for the specified power level to take effect. Refer to the Output Enabled pro

### Source:Constant Power:Level

Specifies the power level, in watts, that the device attempts to generate on the specified channel(s).

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Constant Power**
 .

Note

Output Enabled

Note

**Valid Values:**
 The valid values for this property are determined by the selected value for the
 [Constant Power Level Range](pnidcpower-constantpowerlevelrange.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Constant Power Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowerlevelrange.html language=enus -->
## TOPIC 00147: Source:Constant Power:Level Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowerlevelrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowerlevelrange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level range, in watts, for the specified channel(s). The range defines the valid values to which you can set the power level. This property is applicable only if the Output Function property is set to Constant Power . The voltage range and current range used by the instrument are

### Source:Constant Power:Level Range

Specifies the power level range, in watts, for the specified channel(s).

The range defines the valid values to which you can set the power level.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Constant Power**
 .

Note

Note

For valid ranges, refer to the specifications for your instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Constant Power Level Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowerpolezeroratio.html language=enus -->
## TOPIC 00148: Source:Custom Transient Response:Constant Power:Pole-Zero Ratio

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowerpolezeroratio.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantpowerpolezeroratio.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The ratio of the pole frequency to the zero frequency when the Output Function property is set to Constant Power and the output current is below the current limit. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. NI-DCPow

### Source:Custom Transient Response:Constant Power:Pole-Zero Ratio

The ratio of the pole frequency to the zero frequency when the
 [Output Function](/csh?topicname=pnidcpower-outputfunction.html)
 property is set to
 **Constant Power**
 and the output current is below the current limit.

Note

Supported Properties by Device

Note

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Constant Power Pole-Zero Ratio |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancecompensationfrequency.html language=enus -->
## TOPIC 00149: Source:Custom Transient Response:Constant Resistance:Compensation Frequency

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancecompensationfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancecompensationfrequency.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The frequency at which a pole-zero pair is added to the system when the Output Function property is set to Constant Resistance and the output current is below the current limit. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported dev

### Source:Custom Transient Response:Constant Resistance:Compensation Frequency

The frequency at which a pole-zero pair is added to the system when the
 [Output Function](/csh?topicname=pnidcpower-outputfunction.html)
 property is set to
 **Constant Resistance**
 and the output current is below the current limit.

Note

Supported Properties by Device

Note

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Constant Resistance Compensation Freq |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancecurrentlimit.html language=enus -->
## TOPIC 00150: Source:Constant Resistance:Current Limit

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancecurrentlimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancecurrentlimit.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit, in amps, that the output cannot exceed when generating the desired resistance level on the specified channel(s). The device will operate in Constant Current mode if the current exceeds the specified limit. This property is applicable only if the Output Function property

### Source:Constant Resistance:Current Limit

Specifies the current limit, in amps, that the output cannot exceed when generating the desired resistance level on the specified channel(s).

The device will operate in Constant Current mode if the current exceeds the specified limit.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Constant Resistance**
 and the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Symmetric**
 .

Note

Output Enabled

Note

**Valid Values:**
 The valid values for this property are determined by the selected value for the
 [Constant Resistance Level Range](pnidcpower-constantresistancelevelrange.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Constant Resistance Current Limit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancegainbandwidth.html language=enus -->
## TOPIC 00151: Source:Custom Transient Response:Constant Resistance:Gain Bandwidth

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancegainbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancegainbandwidth.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the Output Function property is set to Constant Resistance and the output current is below the current limit. This property is not supported by all device

### Source:Custom Transient Response:Constant Resistance:Gain Bandwidth

The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes.
 This property takes effect when the
 [Output Function](/csh?topicname=pnidcpower-outputfunction.html)
 property is set to
 **Constant Resistance**
 and the output current is below the current limit.

Note

Supported Properties by Device

Note

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Constant Resistance GBW |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancelevel.html language=enus -->
## TOPIC 00152: Source:Constant Resistance:Level

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancelevel.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resistance level, in ohms, that the device attempts to generate on the specified channel(s). This property is applicable only if the Output Function property is set to Constant Resistance . The channel must be enabled for the specified resistance level to take effect. Refer to the Outp

### Source:Constant Resistance:Level

Specifies the resistance level, in ohms, that the device attempts to generate on the specified channel(s).

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Constant Resistance**
 .

Note

Output Enabled

Note

**Valid Values:**
 The valid values for this property are determined by the selected value for the
 [Constant Resistance Level Range](pnidcpower-constantresistancelevelrange.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Constant Resistance Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancelevelrange.html language=enus -->
## TOPIC 00153: Source:Constant Resistance:Level Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancelevelrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancelevelrange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resistance level range, in ohms, for the specified channel(s). The range defines the valid values to which you can set the resistance level. This property is applicable only if the Output Function property is set to Constant Resistance . The voltage range and current range used by the

### Source:Constant Resistance:Level Range

Specifies the resistance level range, in ohms, for the specified channel(s).

The range defines the valid values to which you can set the resistance level.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Constant Resistance**
 .

Note

Note

For valid ranges, refer to the specifications for your instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Constant Resistance Level Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancepolezeroratio.html language=enus -->
## TOPIC 00154: Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancepolezeroratio.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-constantresistancepolezeroratio.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The ratio of the pole frequency to the zero frequency when the Output Function property is set to Constant Resistance and the output current is below the current limit. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. NI-

### Source:Custom Transient Response:Constant Resistance:Pole-Zero Ratio

The ratio of the pole frequency to the zero frequency when the
 [Output Function](/csh?topicname=pnidcpower-outputfunction.html)
 property is set to
 **Constant Resistance**
 and the output current is below the current limit.

Note

Supported Properties by Device

Note

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Constant Resistance Pole-Zero Ratio |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentcompensationfrequency.html language=enus -->
## TOPIC 00155: Source:Custom Transient Response:Current:Compensation Frequency

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentcompensationfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentcompensationfrequency.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The frequency at which a pole-zero pair is added to the system when the channel is in Constant Current mode. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value : Refer to Supported Properties by Device for the

### Source:Custom Transient Response:Current:Compensation Frequency

The frequency at which a pole-zero pair is added to the system when the channel is in
 Constant Current mode.

Note

Supported Properties by Device

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current Compensation Freq |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentgainbandwidth.html language=enus -->
## TOPIC 00156: Source:Custom Transient Response:Current:Gain Bandwidth

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentgainbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentgainbandwidth.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the channel is in Constant Current mode. This property is not supported by all devices. Refer to Supported Properties by Device for information about supp

### Source:Custom Transient Response:Current:Gain Bandwidth

The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the channel is in
 Constant Current mode.

Note

Supported Properties by Device

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current GBW |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevel.html language=enus -->
## TOPIC 00157: Source:DC Current:Current Level

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevel.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current level, in amps, that the device attempts to generate on the specified channel(s). This property is applicable only if the Output Function property is set to DC Current . The channel must be enabled for the specified current level to take effect. Refer to the Output Enabled prop

### Source:DC Current:Current Level

Specifies the current level, in amps, that the device attempts to generate on the specified channel(s).

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Current**
 .

Note

Output Enabled

**Valid Values:**
 The valid values for this property are defined by the values to which the
 [Current Level Range](pnidcpower-currentlevelrange.html)
 property is set.

**Related topics:**

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Current Level |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelautorange.html language=enus -->
## TOPIC 00158: Source:DC Current:Current Level Autorange

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelautorange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelautorange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether NI-DCPower automatically selects the current level range based on the desired current level for the specified channel(s). If you set this property to On , NI-DCPower ignores any changes you make to the Current Level Range property. If you change the Current Level Autorange property

### Source:DC Current:Current Level Autorange

Specifies whether NI-DCPower automatically selects the current level range based on the desired current level for the specified channel(s).

If you set this property to
 **On**
 , NI-DCPower ignores any changes you make to the
 [Current Level Range](pnidcpower-currentlevelrange.html)
 property. If you change the Current Level Autorange property from
 **On**
 to
 **Off**
 , NI-DCPower retains the last value the
 [Current Level Range](pnidcpower-currentlevelrange.html)
 property was set to (or the default value if it was never set) and uses that value as the current level range.

Refer to the
 [Current Level Range](pnidcpower-currentlevelrange.html)
 property for information about which range NI-DCPower automatically selects.

The Current Level Autorange property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Current**
 .

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current Level Autorange |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Off | 0 | NI-DCPower does not automatically select the current level range. |
| --- | --- | --- |
| On | 1 | NI-DCPower automatically selects the current level range. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelfallingslewrate.html language=enus -->
## TOPIC 00159: Source:DC Current:Current Level Slew Rate:Falling

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelfallingslewrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelfallingslewrate.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rate of decrease, in amps per microsecond, to apply to the absolute magnitude of the current level of the specified channel(s). This property is applicable only if you set the Output Function property to DC Current . This property is not supported by all instruments. Refer to Supported

### Source:DC Current:Current Level Slew Rate:Falling

Specifies the rate of decrease, in amps per microsecond, to apply to the absolute magnitude of the current level of the specified channel(s).

This property is applicable only if you set the
 [Output Function](pnidcpower-outputfunction.html)
 property to
 **DC Current**
 .

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current Level Falling Slew Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelrange.html language=enus -->
## TOPIC 00160: Source:DC Current:Current Level Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelrange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current level range, in amps, for the specified channel(s). The range defines the valid values to which the current level can be set. Use the Current Level Autorange property to enable automatic selection of the current level range. The Current Level Range property is applicable only i

### Source:DC Current:Current Level Range

Specifies the current level range, in amps, for the specified channel(s).

The range defines the valid values to which the current level can be set. Use the
 [Current Level Autorange](pnidcpower-currentlevelautorange.html)
 property to enable automatic selection of the current level range.

The Current Level Range property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Current**
 .

Note

Output Enabled

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current Level Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Current Level Range |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelrisingslewrate.html language=enus -->
## TOPIC 00161: Source:DC Current:Current Level Slew Rate:Rising

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelrisingslewrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlevelrisingslewrate.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rate of increase, in amps per microsecond, to apply to the absolute magnitude of the current level of the specified channel(s). This property is applicable only if you set the Output Function property to DC Current . This property is not supported by all instruments. Refer to Supported

### Source:DC Current:Current Level Slew Rate:Rising

Specifies the rate of increase, in amps per microsecond, to apply to the absolute magnitude of the current level of the specified channel(s).

This property is applicable only if you set the
 [Output Function](pnidcpower-outputfunction.html)
 property to
 **DC Current**
 .

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current Level Rising Slew Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimit.html language=enus -->
## TOPIC 00162: Source:DC Voltage:Current Limit

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimit.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit, in amps, that the output cannot exceed when generating the desired voltage on the specified channel(s). Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. This property is applicable only if the Output Function

### Source:DC Voltage:Current Limit

Specifies the current limit, in amps, that the output cannot exceed when generating the desired voltage on the specified channel(s). Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Voltage**
 and the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Symmetric**
 .

Note

Output Enabled

Note

**Valid Values:**
 The valid values for this property are defined by the values to which the
 [Current Limit Range](pnidcpower-currentlimitrange.html)
 property is set.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current Limit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Current Limit |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimitautorange.html language=enus -->
## TOPIC 00163: Source:DC Voltage:Current Limit Autorange

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimitautorange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimitautorange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether NI-DCPower automatically selects the current limit range based on the desired current limit for the specified channel(s). If you set this property to On , NI-DCPower ignores any changes you make to the Current Limit Range property. If you change the Current Limit Autorange property

### Source:DC Voltage:Current Limit Autorange

Specifies whether NI-DCPower automatically selects the current limit range based on the desired current limit for the specified channel(s).

If you set this property to
 **On**
 , NI-DCPower ignores any changes you make to the
 [Current Limit Range](pnidcpower-currentlimitrange.html)
 property. If you change the Current Limit Autorange property from
 **On**
 to
 **Off**
 , NI-DCPower retains the last value the Current Limit Range property was set to (or the default value if it was never set) and uses that value as the current limit range.

Refer to the
 [Current Limit Range](pnidcpower-currentlimitrange.html)
 property for information about which range NI-DCPower automatically selects.

The Current Limit Autorange property is applicable only if the channel is configured to
 **DC Voltage**
 in the
 [Output Function](pnidcpower-outputfunction.html)
 property.

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current Limit Autorange |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Off | 0 | NI-DCPower does not automatically select the current limit range. |
| --- | --- | --- |
| On | 1 | NI-DCPower automatically selects the current limit range. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimithigh.html language=enus -->
## TOPIC 00164: Source:DC Voltage:Current Limit High

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimithigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimithigh.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum current, in amps, that the output can produce when generating the desired voltage on the specified channel(s). This property is applicable only if the Compliance Limit Symmetry property is set to Asymmetric and the Output Function property is set to DC Voltage . You must also s

### Source:DC Voltage:Current Limit High

Specifies the maximum current, in amps, that the output can produce when generating the desired voltage on the specified channel(s).

This property is applicable only if the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Asymmetric**
 and the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Voltage**
 .

You must also specify a
 [Current Limit Low](pnidcpower-currentlimitlow.html)
 to complete the asymmetric range.

Note

Output Enabled

Output Connected

Note

Note

Supported Properties by Device

**Valid Values:**
 [1% of
 [Current Limit Range](pnidcpower-currentlimitrange.html)
 ,
 [Current Limit Range](pnidcpower-currentlimitrange.html)
 ]

- The range bounded by the limit high and limit low must include zero.

Note

Overranging Enabled

**Default Value:**
 Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current Limit High |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimitlow.html language=enus -->
## TOPIC 00165: Source:DC Voltage:Current Limit Low

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimitlow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimitlow.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum current, in amps, that the output can produce when generating the desired voltage on the specified channel(s). This property is applicable only if the Compliance Limit Symmetry property is set to Asymmetric and the Output Function property is set to DC Voltage . You must also s

### Source:DC Voltage:Current Limit Low

Specifies the minimum current, in amps, that the output can produce when generating the desired voltage on the specified channel(s).

This property is applicable only if the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Asymmetric**
 and the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Voltage**
 .

You must also specify a
 [Current Limit High](pnidcpower-currentlimithigh.html)
 to complete the asymmetric range.

Note

Output Enabled

Output Connected

Note

Note

Supported Properties by Device

**Valid Values:**
 [-
 [Current Limit Range](pnidcpower-currentlimitrange.html)
 , -1% of
 [Current Limit Range](pnidcpower-currentlimitrange.html)
 ]

- The range bounded by the limit high and limit low must include zero.

Note

Overranging Enabled

**Default Value:**
 Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current Limit Low |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimitrange.html language=enus -->
## TOPIC 00166: Source:DC Voltage:Current Limit Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimitrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentlimitrange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit range, in amps, for the specified channel(s). The range defines the valid values to which the current limit can be set. Use the Current Limit Autorange property to enable automatic selection of the current limit range. The Current Limit Range property is applicable only i

### Source:DC Voltage:Current Limit Range

Specifies the current limit range, in amps, for the specified channel(s).

The range defines the valid values to which the current limit can be set. Use the
 [Current Limit Autorange](pnidcpower-currentlimitautorange.html)
 property to enable automatic selection of the current limit range.

The Current Limit Range property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **DC Voltage**
 .

Note

Output Enabled

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current Limit Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Current Limit Range |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentpolezeroratio.html language=enus -->
## TOPIC 00167: Source:Custom Transient Response:Current:Pole-Zero Ratio

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentpolezeroratio.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-currentpolezeroratio.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The ratio of the pole frequency to the zero frequency when the channel is in Constant Current mode. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default v

### Source:Custom Transient Response:Current:Pole-Zero Ratio

The ratio of the pole frequency to the zero frequency when the channel is in
 Constant Current mode.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current Pole-Zero Ratio |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-dcnoiserejection.html language=enus -->
## TOPIC 00168: Measurement:Advanced:DC Noise Rejection

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-dcnoiserejection.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-dcnoiserejection.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the relative weighting of samples in a measurement. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value : Normal To specify a channel name when accessing this property, you must first initialize the

### Measurement:Advanced:DC Noise Rejection

Determines the relative weighting of samples in a measurement.

Note

Supported Properties by Device

**Default Value**
 :
 **Normal**

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DC Noise Rejection |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Normal | 1044 | Normal DC noise rejection. |
| --- | --- | --- |
| Second-Order | 1043 | Second-order DC noise rejection. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-description.html language=enus -->
## TOPIC 00169: Inherent IVI Attributes:Driver Identification:Description

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-description.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-description.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains a brief description of the specific driver. Remarks The following table lists the characteristics of this property. Short Name Description Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Instrument-based No Resettable No

### Inherent IVI Attributes:Driver Identification:Description

Contains a brief description of the specific driver.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Description |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-driverprefix.html language=enus -->
## TOPIC 00170: Inherent IVI Attributes:Driver Identification:Driver Prefix

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-driverprefix.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-driverprefix.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the prefix for NI-DCPower. The name of each user-callable VI in NI-DCPower begins with this prefix. Remarks The following table lists the characteristics of this property. Short Name Driver Prefix Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Instrument-based

### Inherent IVI Attributes:Driver Identification:Driver Prefix

Contains the prefix for NI-DCPower. The name of each user-callable VI in NI-DCPower begins with this prefix.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Driver Prefix |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-driversetup.html language=enus -->
## TOPIC 00171: Inherent IVI Attributes:Advanced Session Information:Driver Setup

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-driversetup.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-driversetup.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the Driver Setup string that you specified when initializing the driver. Some cases exist where you must specify the instrument driver options at initialization time. An example of this case is specifying a particular instrument model from among a family of instruments that the driver supp

### Inherent IVI Attributes:Advanced Session Information:Driver Setup

Indicates the Driver Setup string that you specified when initializing the driver.

Some cases exist where you must specify the instrument driver options at initialization time. An example of this case is specifying a particular instrument model from among a family of instruments that the driver supports. This property is useful when
 [simulating](/csh?context=nidcpower_ni_dc_power_supplies_help_simulate)
 a device. You can specify the driver-specific options through the Driver Setup keyword in the
 **options string**
 parameter in the
 [niDCPower Initialize With Independent Channels](/csh?context=nidcpower_nidcpowerviref_nidcpower_initialize_with_channels)
 VI or through the IVI Configuration Utility.

If you do not specify a Driver Setup string, this property returns an empty string.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Driver Setup |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niDCPower Initialize With Channels |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-drivervendor.html language=enus -->
## TOPIC 00172: Inherent IVI Attributes:Driver Identification:Driver Vendor

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-drivervendor.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-drivervendor.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the name of the vendor that supplies NI-DCPower. Remarks The following table lists the characteristics of this property. Short Name Driver Vendor Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Instrument-based No Resettable No

### Inherent IVI Attributes:Driver Identification:Driver Vendor

Contains the name of the vendor that supplies NI-DCPower.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Driver Vendor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedmeasuretriggeroutputterminal.html language=enus -->
## TOPIC 00173: Triggers:Measure Trigger:Export Output Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedmeasuretriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedmeasuretriggeroutputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal for exporting the Measure trigger. Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your instrument. For the PXIe-4147, PXIe-4162, and PXIe-4163, refer to the Signal Routing topic for the instrument to determin

### Triggers:Measure Trigger:Export Output Terminal

Specifies the output terminal for exporting the Measure trigger.

Refer to the
 **Device Routes**
 tab in Measurement & Automation Explorer for a list of the terminals available on your instrument. For the PXIe-4147, PXIe-4162, and PXIe-4163, refer to the Signal Routing topic for the instrument to determine which routes are available (this information is not available on a Device Routes tab in MAX).

Specify the output terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal.

Note

Supported Properties by Device

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Measure Trigger Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Export Signal |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedpulsetriggeroutputterminal.html language=enus -->
## TOPIC 00174: Triggers:Pulse Trigger:Export Output Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedpulsetriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedpulsetriggeroutputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal for exporting the Pulse trigger. Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device. Specify the output terminal using the form /Dev1/PXI_Trig0 , where Dev1 is the instrument and PXI_Trig0 is the term

### Triggers:Pulse Trigger:Export Output Terminal

Specifies the output terminal for exporting the Pulse trigger.

Refer to the
 **Device Routes**
 tab in Measurement & Automation Explorer for a list of the terminals available on your device.

Specify the output terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal.

Note

Supported Properties by Device

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Pulse Trigger Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedsequenceadvancetriggeroutputterminal.html language=enus -->
## TOPIC 00175: Triggers:Sequence Advance Trigger:Export Output Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedsequenceadvancetriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedsequenceadvancetriggeroutputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal for exporting the Sequence Advance trigger. Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your instrument. For the PXIe-4147, PXIe-4162, and PXIe-4163, refer to the Signal Routing topic for the instrument to

### Triggers:Sequence Advance Trigger:Export Output Terminal

Specifies the output terminal for exporting the Sequence Advance trigger.

Refer to the
 **Device Routes**
 tab in Measurement & Automation Explorer for a list of the terminals available on your instrument. For the PXIe-4147, PXIe-4162, and PXIe-4163, refer to the Signal Routing topic for the instrument to determine which routes are available (this information is not available on a Device Routes tab in MAX).

Specify the output terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal.

Note

Supported Properties by Device

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Sequence Advance Trigger Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Export Signal |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedsourcetriggeroutputterminal.html language=enus -->
## TOPIC 00176: Triggers:Source Trigger:Export Output Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedsourcetriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedsourcetriggeroutputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal for exporting the Source trigger. Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your instrument. For the PXIe-4147, PXIe-4162, and PXIe-4163, refer to the Signal Routing topic for the instrument to determine

### Triggers:Source Trigger:Export Output Terminal

Specifies the output terminal for exporting the Source trigger.

Refer to the
 **Device Routes**
 tab in Measurement & Automation Explorer for a list of the terminals available on your instrument. For the PXIe-4147, PXIe-4162, and PXIe-4163, refer to the Signal Routing topic for the instrument to determine which routes are available (this information is not available on a Device Routes tab in MAX).

Specify the output terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal.

Note

Supported Properties by Device

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Source Trigger Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Export Signal |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedstarttriggeroutputterminal.html language=enus -->
## TOPIC 00177: Triggers:Start Trigger:Export Output Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedstarttriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-exportedstarttriggeroutputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal for exporting the Start trigger. Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your instrument. For the PXIe-4147, PXIe-4162, and PXIe-4163, refer to the Signal Routing topic for the instrument to determine

### Triggers:Start Trigger:Export Output Terminal

Specifies the output terminal for exporting the Start trigger.

Refer to the
 **Device Routes**
 tab in Measurement & Automation Explorer for a list of the terminals available on your instrument. For the PXIe-4147, PXIe-4162, and PXIe-4163, refer to the Signal Routing topic for the instrument to determine which routes are available (this information is not available on a Device Routes tab in MAX).

Specify the output terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal.

Note

Supported Properties by Device

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Start Trigger Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Export Signal |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-fetchbacklog.html language=enus -->
## TOPIC 00178: Measurement:Fetch Backlog

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-fetchbacklog.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-fetchbacklog.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of measurements acquired that have not been fetched yet. To specify a channel name when accessing this property, you must first initialize the session using the Initialize With Independent Channels VI. Remarks The following table lists the characteristics of this property. Short N

### Measurement:Fetch Backlog

Returns the number of measurements acquired that have not been fetched yet.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Fetch Backlog |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-interchangecheck.html language=enus -->
## TOPIC 00179: Inherent IVI Attributes:User Options:Interchange Check

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-interchangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-interchangecheck.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to perform interchangeability checking and log interchangeability warnings when you call NI-DCPower VIs. TRUE specifies that interchangeability checking is enabled. Interchangeability warnings indicate that using your application with a different instrument might cause different be

### Inherent IVI Attributes:User Options:Interchange Check

Specifies whether to perform interchangeability checking and log interchangeability warnings when you call NI-DCPower VIs. TRUE specifies that interchangeability checking is enabled.

Interchangeability warnings indicate that using your application with a different instrument might cause different behavior. Call the
 [niDCPower Get Next Interchange Warning](/csh?context=nidcpower_nidcpowerviref_nidcpower_get_next_interchange_warning)
 VI to retrieve interchange warnings.

Call the
 [niDCPower Clear Interchange Warnings](/csh?context=nidcpower_nidcpowerviref_nidcpower_clear_interchange_warnings)
 VI to clear the list of interchangeability warnings without reading them.

Interchangeability checking examines the properties in a capability group only if you specify a value for at least one property within that group. Interchangeability warnings can occur when a property affects the behavior of the instrument and you have not set that property or when the property has been invalidated since you set it.

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Interchange Check |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-interlockinputopen.html language=enus -->
## TOPIC 00180: Advanced:Interlock Input Open

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-interlockinputopen.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-interlockinputopen.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the safety interlock circuit is open. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Defined Values FALSE Safety interlock input is closed. TRUE Safety interlock input is open. To specify an instrument

### Advanced:Interlock Input Open

Indicates whether the safety interlock circuit is open.

Note

Supported Properties by Device

**Defined Values**

| FALSE | Safety interlock input is closed. |
| --- | --- |
| TRUE | Safety interlock input is open. |

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Interlock Input Open |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | Yes |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-isolationstate.html language=enus -->
## TOPIC 00181: Advanced:Isolation State

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-isolationstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-isolationstate.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines whether the channel is isolated. This property is not supported by all instruments. Refer to Supported Properties by Device for information about supported instruments. Defines whether the channel is isolated or not. Default Value : Refer to Supported Properties by Device for the default val

### Advanced:Isolation State

Defines whether the channel is isolated.

Note

Supported Properties by Device

Defines whether the channel is isolated or not.

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Isolation State |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Isolated | 1128 | The channel is disconnected from chassis ground. |
| --- | --- | --- |
| Non-isolated | 1129 | The channel is connected to chassis ground. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcracditherenabled.html language=enus -->
## TOPIC 00182: LCR:AC Stimulus:Advanced:Dither Enabled

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcracditherenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcracditherenabled.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether dithering is enabled during LCR measurements. Dithering adds out-of-band noise to improve measurements of small voltage and current signals. Hardware is only warranted to meet its accuracy specs with dither enabled. You can disable dither if the added noise interferes with your dev

### LCR:AC Stimulus:Advanced:Dither Enabled

Specifies whether dithering is enabled during LCR measurements.

Dithering adds out-of-band noise to improve measurements of small voltage and current signals.

Note

Note

Supported Properties by Device

**Defined Values**

| FALSE | Dithering is not applied to LCR measurements. |
| --- | --- |
| TRUE | Dithering is applied to LCR measurements. |

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR AC Dither Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcracelectricalcablelengthdelay.html language=enus -->
## TOPIC 00183: LCR:Compensation:LCR AC Electrical Cable Length Delay

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcracelectricalcablelengthdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcracelectricalcablelengthdelay.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the one-way electrical length delay of the cable, in seconds. The default value depends on Cable Length. This property is not supported by all instruments. Refer to Supported Properties by Device for information about supported instruments. Remarks The following table lists the characteris

### LCR:Compensation:LCR AC Electrical Cable Length Delay

Specifies the one-way electrical length delay of the cable, in seconds.

The default value depends on [Cable Length](pnidcpower-cablelength.html).

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR AC Electrical Cable Length Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcractualloadreactance.html language=enus -->
## TOPIC 00184: LCR:Compensation:Load:Actual Reactance

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcractualloadreactance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcractualloadreactance.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the actual reactance, in ohms, of the load used for load LCR compensation. This property applies when LCR Open/Short/Load Compensation Data Source is set to As Defined. This property is not supported by all instruments. Refer to Supported Properties by Device for information about supporte

### LCR:Compensation:Load:Actual Reactance

Specifies the actual reactance, in ohms, of the load used for load LCR compensation.

This property applies when [LCR Open/Short/Load Compensation Data Source](pnidcpower-lcropenshortloadcompensationdatasource.html) is set to **As Defined**.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Actual Load Reactance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcractualloadresistance.html language=enus -->
## TOPIC 00185: LCR:Compensation:Load:Actual Resistance

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcractualloadresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcractualloadresistance.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the actual resistance, in ohms, of the load used for load LCR compensation. This property applies when LCR Open/Short/Load Compensation Data Source is set to As Defined. This property is not supported by all instruments. Refer to Supported Properties by Device for information about support

### LCR:Compensation:Load:Actual Resistance

Specifies the actual resistance, in ohms, of the load used for load LCR compensation.

This property applies when [LCR Open/Short/Load Compensation Data Source](pnidcpower-lcropenshortloadcompensationdatasource.html) is set to **As Defined**.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Actual Load Resistance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrautomaticlevelcontrol.html language=enus -->
## TOPIC 00186: LCR:AC Stimulus:Automatic Level Control

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrautomaticlevelcontrol.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrautomaticlevelcontrol.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the channel actively attempts to maintain a constant test voltage or current across the DUT for LCR measurements. The use of voltage or current depends on the test signal you configure with the LCR Stimulus Function property. This property is not supported by all instruments. Refer

### LCR:AC Stimulus:Automatic Level Control

Specifies whether the channel actively attempts to maintain a constant test voltage or current across the DUT for LCR measurements.

The use of voltage or current depends on the test signal you configure with the
 [LCR Stimulus Function](pnidcpower-lcrstimulusfunction.html)
 property.

Note

Supported Properties by Device

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Automatic Level Control |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Off | 0 | The channel does not correct for variation in voltage or current across the DUT. Note Because the PXIe-4190 output impedance is a function of the impedance range, selecting this option may result in an actual AC stimulus amplitude at the load that is different from the value you specify. Impedance measurements take this difference into account and remain accurate. |
| --- | --- | --- |
| On | 1 | The channel attempts to maintain a constant voltage or current across the DUT. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrdcbiasvoltagerange.html language=enus -->
## TOPIC 00187: LCR:DC Bias:Advanced:Voltage Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrdcbiasvoltagerange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrdcbiasvoltagerange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage range, in volts, that defines the values to which you can set the LCR DC Bias Voltage Level for the specified channel(s). For valid ranges, refer to the specifications for your instrument. This property is not supported by all instruments. Refer to Supported Properties by Devic

### LCR:DC Bias:Advanced:Voltage Range

Specifies the voltage range, in volts, that defines the values to which you can set the [LCR DC Bias Voltage Level](/csh?topicname=pnidcpower-lcrdcbiasvoltagelevel.html) for the specified channel(s).

For valid ranges, refer to the specifications for your instrument.

Note

Supported Properties by Device

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR DC Bias Voltage Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrfrequency.html language=enus -->
## TOPIC 00188: LCR:AC Stimulus:Frequency

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrfrequency.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency of the AC test signal applied to the DUT for LCR measurements. This property is not supported by all instruments. Refer to Supported Properties by Device for information about supported instruments. Valid Values : 40 Hz to 2 MHz Instrument specifications affect the valid valu

### LCR:AC Stimulus:Frequency

Specifies the frequency of the AC test signal applied to the DUT for LCR measurements.

Note

Supported Properties by Device

**Valid Values**
 : 40 Hz to 2 MHz

Instrument specifications affect the valid values you can program. Refer to the specifications for your instrument for more information.

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrimpedanceautorange.html language=enus -->
## TOPIC 00189: LCR:Impedance Range:Impedance Autorange

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrimpedanceautorange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrimpedanceautorange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines whether an instrument in LCR mode automatically selects the best impedance range for each given LCR measurement. Impedance autoranging may be enabled only when both: The Source Mode property is set to Single Point The Measure When property is set to a value other than On Measure Trigger You

### LCR:Impedance Range:Impedance Autorange

Defines whether an instrument in LCR mode automatically selects the best impedance range for each given LCR measurement.

Impedance autoranging may be enabled only when both:

- The Source Mode property is set to Single Point
- The Measure When property is set to a value other than On Measure Trigger

You can read [LCR Impedance Range](pnidcpower-lcrimpedancerange.html) back after a measurement to determine the actual range used.

When enabled, impedance autoranging overrides impedance range settings you configure manually with any other properties.

Note

On

Off

LCR Impedance Range Source

LCR Load Configuration

Note

Supported Properties by Device

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Impedance Autorange |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Off | 1068 | Disables automatic selection of the impedance range. Channel(s) use the impedance range you specify with the LCR Impedance Range property. |
| --- | --- | --- |
| On | 1070 | Channel(s) automatically select the optimal LCR Impedance Range for the measured signal. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrimpedancerange.html language=enus -->
## TOPIC 00190: LCR:Impedance Range:Impedance Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrimpedancerange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrimpedancerange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the impedance range the channel uses for LCR measurements. This property is not supported by all instruments. Refer to Supported Properties by Device for information about supported instruments. Valid Values: 0 ohms to +inf ohms Default Value : Refer to Supported Properties by Device for t

### LCR:Impedance Range:Impedance Range

Specifies the impedance range the channel uses for LCR measurements.

Note

Supported Properties by Device

**Valid Values**: 0 ohms to +inf ohms

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Impedance Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrimpedancerangesource.html language=enus -->
## TOPIC 00191: LCR:Impedance Range:Advanced:Impedance Range Source

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrimpedancerangesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrimpedancerangesource.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how the impedance range for LCR measurements is determined. LCR Impedance Autorange overrides the impedance range determined by this property. This property is not supported by all instruments. Refer to Supported Properties by Device for information about supported instruments. Default Val

### LCR:Impedance Range:Advanced:Impedance Range Source

Specifies how the impedance range for LCR measurements is determined.

Note

LCR Impedance Autorange

Note

Supported Properties by Device

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Impedance Range Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| LCR Impedance Range | 1142 | Uses the impedance range you specify with the LCR Impedance Range property. |
| --- | --- | --- |
| LCR Load Configuration | 1143 | Computes the impedance range to select based on the values you supply to the LCR Load Resistance, LCR Load Inductance, and LCR Load Capacitance properties. NI-DCPower uses a series model of load resistance, load inductance, and load capacitance to compute the impedance range. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadcapacitance.html language=enus -->
## TOPIC 00192: LCR:Impedance Range:Advanced:Load Capacitance

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadcapacitance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadcapacitance.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the load capacitance, in farads and assuming a series model, of the DUT in order to compute the impedance range when the LCR Impedance Range Source is set to LCR Load Configuration. This property is not supported by all instruments. Refer to Supported Properties by Device for information a

### LCR:Impedance Range:Advanced:Load Capacitance

Specifies the load capacitance, in farads and assuming a series model,
 of the DUT in order to compute the impedance range when the
 [LCR Impedance Range Source](/csh?topicname=pnidcpower-lcrimpedancerangesource.html)
 is set to
 **LCR Load Configuration**.

Note

Supported Properties by Device

**Valid Values**
 : (0 farads, +inf farads)

0 is a special value that signifies +inf farads.

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Load Capacitance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadcompensationenabled.html language=enus -->
## TOPIC 00193: LCR:Compensation:Load:Enabled

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadcompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadcompensationenabled.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply load LCR compensation data to LCR measurements. Both the LCR Open Compensation Enabled and LCR Short Compensation Enabled properties must be set to TRUE in order to set this property to TRUE . Use the LCR Open/Short/Load Compensation Data Source property to define where th

### LCR:Compensation:Load:Enabled

Specifies whether to apply load LCR compensation data to LCR measurements.

Both the
 [LCR Open Compensation Enabled](pnidcpower-lcropencompensationenabled.html)
 and
 [LCR Short Compensation Enabled](pnidcpower-lcrshortcompensationenabled.html)
 properties must be set to
 TRUE
 in order to set this property to
 TRUE
 .

Use the
 [LCR Open/Short/Load Compensation Data Source](pnidcpower-lcropenshortloadcompensationdatasource.html)
 property to define where the load compensation data that is applied to LCR measurements comes from.

Note

Perform LCR Load Compensation

Note

Supported Properties by Device

| TRUE | Load LCR compensation data are applied. |
| --- | --- |
| FALSE | Load LCR compensation data are not applied. |

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Load Compensation Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadinductance.html language=enus -->
## TOPIC 00194: LCR:Impedance Range:Advanced:Load Inductance

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadinductance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadinductance.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the load inductance, in henrys and assuming a series model, of the DUT in order to compute the impedance range when the LCR Impedance Range Source is set to LCR Load Configuration. This property is not supported by all instruments. Refer to Supported Properties by Device for information ab

### LCR:Impedance Range:Advanced:Load Inductance

Specifies the load inductance, in henrys and assuming a series model,
 of the DUT in order to compute the impedance range when the
 [LCR Impedance Range Source](/csh?topicname=pnidcpower-lcrimpedancerangesource.html)
 is set to
 **LCR Load Configuration**.

Note

Supported Properties by Device

**Valid Values**
 : [0 henrys, +inf henrys)

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Load Inductance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadresistance.html language=enus -->
## TOPIC 00195: LCR:Impedance Range:Advanced:Load Resistance

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrloadresistance.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the load resistance, in ohms and assuming a series model, of the DUT in order to compute the impedance range when the LCR Impedance Range Source is set to LCR Load Configuration. This property is not supported by all instruments. Refer to Supported Properties by Device for information abou

### LCR:Impedance Range:Advanced:Load Resistance

Specifies the load resistance, in ohms and assuming a series model,
 of the DUT in order to compute the impedance range when the
 [LCR Impedance Range Source](/csh?topicname=pnidcpower-lcrimpedancerangesource.html)
 is set to
 **LCR Load Configuration**.

Note

Supported Properties by Device

**Valid Values**
 : [0 ohms, +inf ohms)

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Load Resistance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrmeasuredloadreactance.html language=enus -->
## TOPIC 00196: LCR:Compensation:Load:Measured Reactance

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrmeasuredloadreactance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrmeasuredloadreactance.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reactance, in ohms, of the load used for load LCR compensation as measured by the instrument. This property applies when LCR Open/Short/Load Compensation Data Source is set to As Defined. This property is not supported by all instruments. Refer to Supported Properties by Device for inf

### LCR:Compensation:Load:Measured Reactance

Specifies the reactance, in ohms, of the load used for load LCR compensation as measured by the instrument.

This property applies when [LCR Open/Short/Load Compensation Data Source](pnidcpower-lcropenshortloadcompensationdatasource.html) is set to **As Defined**.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Measured Load Reactance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrmeasuredloadresistance.html language=enus -->
## TOPIC 00197: LCR:Compensation:Load:Measured Resistance

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrmeasuredloadresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrmeasuredloadresistance.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resistance, in ohms, of the load used for load LCR compensation as measured by the instrument. This property applies when LCR Open/Short/Load Compensation Data Source is set to As Defined. This property is not supported by all instruments. Refer to Supported Properties by Device for in

### LCR:Compensation:Load:Measured Resistance

Specifies the resistance, in ohms, of the load used for load LCR compensation as measured by the instrument.

This property applies when [LCR Open/Short/Load Compensation Data Source](pnidcpower-lcropenshortloadcompensationdatasource.html) is set to **As Defined**.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Measured Load Resistance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrmeasurementtime.html language=enus -->
## TOPIC 00198: LCR:Measurement Time

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrmeasurementtime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrmeasurementtime.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects a general aperture time profile for LCR measurements. The actual duration of each profile depends on the frequency of the LCR test signal. This property is not supported by all instruments. Refer to Supported Properties by Device for information about supported instruments. Default Value : R

### LCR:Measurement Time

Selects a general aperture time profile for LCR measurements.

The actual duration of each profile depends on the frequency of the LCR test signal.

Note

Supported Properties by Device

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Measurement Time |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Short | 1071 | Uses a short aperture time for LCR measurements. |
| --- | --- | --- |
| Medium | 1072 | Uses a medium aperture time for LCR measurements. |
| Long | 1073 | Uses a long aperture time for LCR measurements. |
| Custom | 1117 | Uses a custom aperture time for LCR measurements as specified by the LCR Custom Measurement Time property. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcropencompensationenabled.html language=enus -->
## TOPIC 00199: LCR:Compensation:Open:Enabled

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcropencompensationenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcropencompensationenabled.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply open LCR compensation data to LCR measurements. Use the LCR Open/Short/Load Compensation Data Source property to define where the open compensation data that is applied to LCR measurements comes from. This property is not supported by all instruments. Refer to Supported Pr

### LCR:Compensation:Open:Enabled

Specifies whether to apply open LCR compensation data to LCR measurements.

Use the
 [LCR Open/Short/Load Compensation Data Source](pnidcpower-lcropenshortloadcompensationdatasource.html)
 property to define where the open compensation data that is applied to LCR measurements comes from.

Note

Supported Properties by Device

| TRUE | Open LCR compensation data are applied. |
| --- | --- |
| FALSE | Open LCR compensation data are not applied. |

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Open Compensation Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcropenconductance.html language=enus -->
## TOPIC 00200: LCR:Compensation:Open:Conductance

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcropenconductance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcropenconductance.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the conductance, in siemens, of the circuit used for open LCR compensation. This property applies when LCR Open/Short/Load Compensation Data Source is set to As Defined. This property is not supported by all instruments. Refer to Supported Properties by Device for information about support

### LCR:Compensation:Open:Conductance

Specifies the conductance, in siemens, of the circuit used for open LCR compensation.

This property applies when [LCR Open/Short/Load Compensation Data Source](pnidcpower-lcropenshortloadcompensationdatasource.html) is set to **As Defined**.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Open Conductance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrshortreactance.html language=enus -->
## TOPIC 00201: LCR:Compensation:Short:Reactance

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrshortreactance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrshortreactance.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reactance, in ohms, of the circuit used for short LCR compensation. This property applies when LCR Open/Short/Load Compensation Data Source is set to As Defined. This property is not supported by all instruments. Refer to Supported Properties by Device for information about supported i

### LCR:Compensation:Short:Reactance

Specifies the reactance, in ohms, of the circuit used for short LCR compensation.

This property applies when [LCR Open/Short/Load Compensation Data Source](pnidcpower-lcropenshortloadcompensationdatasource.html) is set to **As Defined**.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Short Reactance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrshortresistance.html language=enus -->
## TOPIC 00202: LCR:Compensation:Short:Resistance

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrshortresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrshortresistance.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resistance, in ohms, of the circuit used for short LCR compensation. This property applies when LCR Open/Short/Load Compensation Data Source is set to As Defined. This property is not supported by all instruments. Refer to Supported Properties by Device for information about supported

### LCR:Compensation:Short:Resistance

Specifies the resistance, in ohms, of the circuit used for short LCR compensation.

This property applies when [LCR Open/Short/Load Compensation Data Source](pnidcpower-lcropenshortloadcompensationdatasource.html) is set to **As Defined**.

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Short Resistance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrsourceaperturetime.html language=enus -->
## TOPIC 00203: LCR:AC Stimulus:Advanced:Source Aperture Time

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrsourceaperturetime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrsourceaperturetime.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the LCR source aperture time, in seconds, for a channel in LCR mode. Use this attribute to adjust the aperture time for the LCR control loop. In systems that use multiple tones that are equally spaced, setting this attribute to 1/(Tone Spacing in Hz) can reduce the impact of external inter

### LCR:AC Stimulus:Advanced:Source Aperture Time

Specifies the LCR source aperture time, in seconds, for a channel in LCR mode.

Use this attribute to adjust the aperture time for the LCR control loop. In systems that use multiple
 tones that are equally spaced, setting this attribute to 1/(Tone Spacing in Hz) can reduce the impact
 of external interference and still maintain an integer number of cycles for all multi-tones. Increasing
 LCR source aperture time can increase the required settling time.

Note

Supported Properties by Device

**Valid Values**: 5.0e-6 s to 100.0e-3 s

**Default Value**: Refer to [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties) for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Source Aperture Time |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrsourcedelaymode.html language=enus -->
## TOPIC 00204: LCR:Source Delay Mode

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrsourcedelaymode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrsourcedelaymode.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For instruments in LCR mode, determines whether NI-DCPower automatically calculates and applies the source delay or applies a source delay you set manually. You can return the source delay duration for either option by reading Source Delay. When you use this property to manually set the source delay

### LCR:Source Delay Mode

For instruments in LCR mode, determines whether NI-DCPower automatically calculates and applies the source delay or applies a source delay you set manually.

You can return the source delay duration for either option by reading [Source Delay](pnidcpower-sourcedelay.html).

Note

Note

Supported Properties by Device

**Default Value**: **Automatic**

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Source Delay Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Automatic | 1144 | NI-DCPower automatically applies source delay of sufficient duration to account for settling time. |
| --- | --- | --- |
| Manual | 1145 | NI-DCPower applies the source delay that you set manually with Source Delay. You can use this option to set a shorter delay to reduce measurement time at the possible expense of measurement accuracy. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrstimulusfunction.html language=enus -->
## TOPIC 00205: LCR:AC Stimulus:Function

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrstimulusfunction.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrstimulusfunction.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of test signal to apply to the DUT for LCR measurements. This property is not supported by all instruments. Refer to Supported Properties by Device for information about supported instruments. Default Value : Refer to Supported Properties by Device for the default value by instrum

### LCR:AC Stimulus:Function

Specifies the type of test signal to apply to the DUT for LCR measurements.

Note

Supported Properties by Device

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Stimulus Function |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| AC Voltage | 1063 | Applies an AC voltage for LCR stimulus. |
| --- | --- | --- |
| AC Current | 1064 | Applies an AC current for LCR stimulus. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrvoltageamplitude.html language=enus -->
## TOPIC 00206: LCR:AC Stimulus:Voltage Amplitude

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrvoltageamplitude.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrvoltageamplitude.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amplitude, in V RMS, of the AC voltage test signal applied to the DUT for LCR measurements. This property applies when the LCR Stimulus Function property is set to AC Voltage . This property is not supported by all instruments. Refer to Supported Properties by Device for information ab

### LCR:AC Stimulus:Voltage Amplitude

Specifies the amplitude, in V RMS, of the AC voltage test signal applied to the DUT for LCR measurements.

This property applies when the
 [LCR Stimulus Function](pnidcpower-lcrstimulusfunction.html)
 property is set to
 **AC Voltage**
 .

Note

Supported Properties by Device

**Valid Values**
 : 7.08e-4 V RMS to 7.07 V RMS

Instrument specifications affect the valid values you can program. Refer to the specifications for your instrument for more information.

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Voltage Amplitude |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrvoltagerange.html language=enus -->
## TOPIC 00207: LCR:AC Stimulus:Advanced:Voltage Range

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrvoltagerange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-lcrvoltagerange.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage range, in volts RMS, that defines the values to which you can set the LCR Voltage Amplitude for the specified channel(s). For valid ranges, refer to the specifications for your instrument. This property is not supported by all instruments. Refer to Supported Properties by Devic

### LCR:AC Stimulus:Advanced:Voltage Range

Specifies the voltage range, in volts RMS, that defines the values to which you can set the [LCR Voltage Amplitude](/csh?topicname=pnidcpower-lcrvoltageamplitude.html) for the specified channel(s).

For valid ranges, refer to the specifications for your instrument.

Note

Supported Properties by Device

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LCR Voltage Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-logicalname.html language=enus -->
## TOPIC 00208: Inherent IVI Attributes:Advanced Session Information:Logical Name

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-logicalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-logicalname.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the logical name(s) you specified when opening the current IVI session. IVI logical names are not supported in sessions created using the Initialize With Independent Channels VI. You can pass a logical name to a deprecated initialize VI. The IVI Configuration Utility must contain an entry f

### Inherent IVI Attributes:Advanced Session Information:Logical Name

Contains the logical name(s) you specified when opening the current IVI session.

Note

Initialize With Independent Channels

You can pass a logical name to a deprecated initialize VI. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section in the IVI configuration file. The virtual instrument section specifies a physical instrument and initial user settings.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Logical Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventoutputbehavior.html language=enus -->
## TOPIC 00209: Events:Measure Complete Event:Output Behavior

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventoutputbehavior.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output behavior for exporting the Measure Complete event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by device. To specify a

### Events:Measure Complete Event:Output Behavior

Specifies the output behavior for exporting the Measure Complete event.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Measure Complete Event Output Behavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

| Pulse Event Output | 1147 | A single 250ns pulse is transmitted. |
| --- | --- | --- |
| Toggle Event Output | 1148 | The output level toggles between low and high, The initial output level is determined by Measure Complete Event Toggle Initial State . |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventoutputterminal.html language=enus -->
## TOPIC 00210: Events:Measure Complete Event:Output Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventoutputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal for exporting the Measure Complete event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Specify the output terminal using the form /Dev1/PXI_Trig0 , where Dev1 is the instrument and PXI_Tr

### Events:Measure Complete Event:Output Terminal

Specifies the output terminal for exporting the Measure Complete event.

Note

Supported Properties by Device

Specify the output terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Measure Complete Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventpulsepolarity.html language=enus -->
## TOPIC 00211: Events:Measure Complete Event:Pulse:Polarity

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventpulsepolarity.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the Measure Complete event. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by device. To specify a channel name when

### Events:Measure Complete Event:Pulse:Polarity

Specifies the behavior of the Measure Complete event.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Measure Complete Event Pulse Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

| Active High | 1018 | A high pulse occurs when the event is generated. The exported signal is low level both before and after the event is generated. |
| --- | --- | --- |
| Active Low | 1019 | A low pulse occurs when the event is generated. The exported signal is high level both before and after the event is generated. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventpulsewidth.html language=enus -->
## TOPIC 00212: Events:Measure Complete Event:Pulse:Width

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventpulsewidth.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width of the Measure Complete event, in seconds. The minimum event pulse width value for the NI PXI-4132 is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns. The maximum event pulse width value for all devices is 1.6 microseconds. This property is not s

### Events:Measure Complete Event:Pulse:Width

Specifies the width of the Measure Complete event, in seconds.

The minimum event pulse width value for the NI PXI-4132 is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.

The maximum event pulse width value for all devices is 1.6 microseconds.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Measure Complete Event Pulse Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventtoggleinitialstate.html language=enus -->
## TOPIC 00213: Events:Measure Complete Event:Toggle:Initial State

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventtoggleinitialstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurecompleteeventtoggleinitialstate.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial state of the Measure Complete event if you set the Measure Complete Event Output Behavior to Toggle Event Output. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Pr

### Events:Measure Complete Event:Toggle:Initial State

Specifies the initial state of the Measure Complete event if you set the [Measure Complete Event Output Behavior](/csh?topicname=pnidcpower-measurecompleteeventoutputbehavior.html) to **Toggle Event Output**.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Measure Complete Event Toggle Initial State |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

| Initial State Low | 1149 | The output is set to low at session commit. For operation in Single Point source mode, the output switches to high when the event occurs during the acquisition. The output then switches to low if a subsequent event occurs during the acquisition. This pattern repeats as events continue to be generated. For operation in Sequence source mode, the output switches to high the first time an event occurs during the acquisition. It then switches to low the second time an event occurs. This pattern repeats for any subsequent event occurrences. |
| --- | --- | --- |
| Initial State High | 1150 | The output is set to high at session commit. For operation in Single Point source mode, the output switches to low when the event occurs during the acquisition. The output then switches to high if a subsequent event occurs during the acquisition. This pattern repeats as events continue to be generated. For operation in Sequence source mode, the output switches to low the first time an event occurs during the acquisition. It then switches to high the second time an event occurs. This pattern repeats for any subsequent event occurrences. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurerecorddeltatime.html language=enus -->
## TOPIC 00214: Measurement:Measure Record Delta Time

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurerecorddeltatime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurerecorddeltatime.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the amount of time, in seconds, between the start of two consecutive measurements in a measure record. Only query this property after the desired measurement settings are committed. This property is not supported by all devices. Refer to Supported Properties by Device for information about s

### Measurement:Measure Record Delta Time

Queries the amount of time, in seconds, between the start of two consecutive measurements in a measure record. Only query this property after the desired measurement settings are committed.

Note

Supported Properties by Device

Note

Auto Zero

Once

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Measure Record dt |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurerecordlength.html language=enus -->
## TOPIC 00215: Measurement:Measure Record Length

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurerecordlength.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurerecordlength.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how many measurements compose a measure record. When this property is set to a value greater than 1, the Measure When property must be set to Automatically after Source Complete or On Measure Trigger . This property is not supported by all devices. Refer to Supported Properties by Device f

### Measurement:Measure Record Length

Specifies how many measurements compose a measure record. When this property is set to a value greater than 1, the
 [Measure When](/csh?topicname=pnidcpower-measurewhen.html)
 property must be set to
 **Automatically after Source Complete**
 or
 **On Measure Trigger**
 .

Note

Supported Properties by Device

**Valid Values**
 : 1 to 16,777,216

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Measure Record Length |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurerecordlengthisfinite.html language=enus -->
## TOPIC 00216: Measurement:Measure Record Length Is Finite

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurerecordlengthisfinite.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurerecordlengthisfinite.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to take continuous measurements. Call the niDCPower Abort With Channels VI to stop continuous measurements. When this property is set to FALSE and the Source Mode property is set to Single Point , the Measure When property must be set to Automatically after Source Complete or On Me

### Measurement:Measure Record Length Is Finite

Specifies whether to take continuous measurements. Call the
 [niDCPower Abort With Channels](/csh?context=nidcpower_nidcpowerviref_nidcpower_abort)
 VI to stop continuous measurements. When this property is set to FALSE and the
 [Source Mode](/csh?topicname=pnidcpower-sourcemode.html)
 property is set to
 **Single Point**
 , the
 [Measure When](/csh?topicname=pnidcpower-measurewhen.html)
 property must be set to
 **Automatically after Source Complete**
 or
 **On Measure Trigger**
 . When this property is set to FALSE and the Source Mode property is set to
 **Sequence**
 , the Measure When property must be set to
 **On Measure Trigger**
 .

Note

Supported Properties by Device

**Default Value**
 : TRUE

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Measure Record Length Is Finite |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measuretriggerdigitaledgeedge.html language=enus -->
## TOPIC 00217: Triggers:Measure Trigger:Digital Edge:Edge

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measuretriggerdigitaledgeedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measuretriggerdigitaledgeedge.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to configure the Measure trigger to assert on the rising or falling edge. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by

### Triggers:Measure Trigger:Digital Edge:Edge

Specifies whether to configure the Measure trigger to assert on the rising or falling edge.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Measure Trigger Digital Edge - Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Measure Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Rising | 1016 | Asserts the trigger on the rising edge of the digital signal. |
| --- | --- | --- |
| Falling | 1017 | Asserts the trigger on the falling edge of the digital signal. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measuretriggerdigitaledgeinputterminal.html language=enus -->
## TOPIC 00218: Triggers:Measure Trigger:Digital Edge:Input Terminal

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measuretriggerdigitaledgeinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measuretriggerdigitaledgeinputterminal.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal for the Measure trigger. This property is used only when the Measure Trigger Type property is set to Digital Edge . This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. You can specify any valid i

### Triggers:Measure Trigger:Digital Edge:Input Terminal

Specifies the input terminal for the Measure trigger. This property is used only when the
 [Measure Trigger Type](/csh?topicname=pnidcpower-measuretriggertype.html)
 property is set to
 **Digital Edge**
 .

Note

Supported Properties by Device

You can specify any valid input terminal for this property, and the driver will create a route between it and the Measure Trigger terminal at Commit. Valid terminals are listed in Measurement & Automation Explorer under the
 **Device Routes**
 tab. For the PXIe-4147, PXIe-4162, and PXIe-4163, refer to the Signal Routing topic for the instrument to determine which routes are available (this information is not available on a Device Routes tab in MAX).

Specify the input terminal using the form
 /Dev1/PXI_Trig0
 , where
 Dev1
 is the instrument and
 PXI_Trig0
 is the terminal. The input terminal can also be a terminal from another instrument. For example, you can set the input terminal on Dev1 to be
 /Dev2/Engine0/SourceCompleteEvent
 , where
 Engine0
 is channel 0.

Note

/Dev1/PXI_Trig0

Dev1

PXI_Trig0

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Measure Trigger Digital Edge - Input Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Measure Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measuretriggertype.html language=enus -->
## TOPIC 00219: Triggers:Measure Trigger:Trigger Type

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measuretriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measuretriggertype.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the Measure trigger. This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Default Value :Refer to Supported Properties by Device for the default value by device. To specify a channel name when access

### Triggers:Measure Trigger:Trigger Type

Specifies the behavior of the Measure trigger.

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Measure Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Digital Edge Measure Trigger, niDCPower Configure Software Edge Measure Trigger |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Digital Edge | 1014 | The data operation starts when a digital edge is detected. |
| --- | --- | --- |
| Software Edge | 1015 | The data operation starts when a software trigger occurs. |
| None | 1012 | No trigger is configured. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurewhen.html language=enus -->
## TOPIC 00220: Measurement:Advanced:Measure When

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurewhen.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-measurewhen.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies when the measure unit should acquire measurements. Unless this property is configured to On Measure Trigger , the Measure Trigger Type property is ignored. NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" a

### Measurement:Advanced:Measure When

Specifies when the measure unit should acquire measurements. Unless this property is configured to
 **On Measure Trigger**
 , the
 [Measure Trigger Type](/csh?topicname=pnidcpower-measuretriggertype.html)
 property is ignored.

Note

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Measure When |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Automatically after Source Complete | 1025 | Acquires a measurement after each Source Complete event completes. Use the niDCPower Fetch Multiple VI to retrieve the measurements. |
| --- | --- | --- |
| On Demand | 1026 | Acquires a measurement when the niDCPower Measure VI or niDCPower Measure Multiple VI is called. |
| On Measure Trigger | 1027 | Acquires a measurement when a Measure trigger is received. Use the niDCPower Fetch Multiple VI to retrieve the measurements. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-mergedchannels.html language=enus -->
## TOPIC 00221: Source:Advanced:Merged Channels

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-mergedchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-mergedchannels.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the merge channel(s) to combine with a designated primary channel of an instrument in order to increase the maximum current you can source from the instrument. Pass the primary channel as the Active Channel when setting this property, and pass the merge channels as the value of this proper

### Source:Advanced:Merged Channels

Specifies the merge channel(s) to combine with a designated primary channel of an instrument in order to increase the maximum current you can source from the instrument.

Pass the primary channel as the [Active Channel](/csh?context=nidcpower_dcpowerpropref_pnidcpower_activechannel) when setting this property, and pass the merge channels as the value of this property.

Refer to the Merged Channels topic in your instrument user manual for more information about using merged channels.

Note

Note

Supported Properties by Device

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

**Related Topics**
 :

[Programming States](/csh?context=nidcpower_ni_dc_power_supplies_help_programmingstates)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Merged Channels |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-model.html language=enus -->
## TOPIC 00222: Inherent IVI Attributes:Instrument Identification:Model

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-model.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-model.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the model number or name of the instrument you are currently using. To specify an instrument name when accessing this property, you must first initialize the session using the Initialize With Independent Channels VI. Remarks The following table lists the characteristics of this property. Sh

### Inherent IVI Attributes:Instrument Identification:Model

Contains the model number or name of the instrument you are currently using.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Model |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | Yes |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcapacitance.html language=enus -->
## TOPIC 00223: Source:Advanced:Output Capacitance

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcapacitance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcapacitance.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use a low or high capacitance on the output for the specified channel(s). NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively. This property is not supported by all devices

### Source:Advanced:Output Capacitance

Specifies whether to use a low or high capacitance on the output for the specified channel(s).

Note

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Capacitance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Low | 1010 | Output capacitance is low. |
| --- | --- | --- |
| High | 1011 | Output capacitance is high. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputconnected.html language=enus -->
## TOPIC 00224: Source:Output Connected

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputconnected.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputconnected.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the output relay is connected (closed) or disconnected (open). The Output Enabled property does not change based on this property; they are independent of each other. Set this property to FALSE to disconnect the output terminal from the output. Only disconnect the output when disco

### Source:Output Connected

Specifies whether the output relay is connected (closed) or disconnected (open). The
 [Output Enabled](/csh?topicname=pnidcpower-outputenabled.html)
 property does not change based on this property; they are independent of each other.

Set this property to FALSE to disconnect the output terminal from the output.

Note

Note

Note

Note

Supported Properties by Device

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Connected |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentchangelimithigh.html language=enus -->
## TOPIC 00225: Source:Output Cutoff:Current Change Limit High

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentchangelimithigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentchangelimithigh.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a limit for positive current slew rate, in amps per microsecond, for output cutoff. If the current increases at a rate that exceeds this limit, the output is disconnected. To find out whether an output has exceeded this limit, call the Query Latched Output Cutoff State VI with Current Chan

### Source:Output Cutoff:Current Change Limit High

Specifies a limit for positive current slew rate, in amps per microsecond, for output cutoff. If the current increases at a rate that exceeds this limit, the output is disconnected.

To find out whether an output has exceeded this limit, call the
 [Query Latched Output Cutoff State](/csh?context=nidcpower_nidcpowerviref_nidcpower_query_latched_output_cutoff_state)
 VI with
 **Current Change High**
 as the
 **reason**
 .

Note

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Cutoff Current Change Limit High |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentchangelimitlow.html language=enus -->
## TOPIC 00226: Source:Output Cutoff:Current Change Limit Low

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentchangelimitlow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentchangelimitlow.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a limit for negative current slew rate, in amps per microsecond, for output cutoff. If the current decreases at a rate that exceeds this limit, the output is disconnected. To find out whether an output has exceeded this limit, call the Query Latched Output Cutoff State VI with Current Chan

### Source:Output Cutoff:Current Change Limit Low

Specifies a limit for negative current slew rate, in amps per microsecond, for output cutoff. If the current decreases at a rate that exceeds this limit, the output is disconnected.

To find out whether an output has exceeded this limit, call the
 [Query Latched Output Cutoff State](/csh?context=nidcpower_nidcpowerviref_nidcpower_query_latched_output_cutoff_state)
 VI with
 **Current Change Low**
 as the
 **reason**
 .

Note

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Cutoff Current Change Limit Low |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentmeasurelimithigh.html language=enus -->
## TOPIC 00227: Source:Output Cutoff:Current Measure Limit High

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentmeasurelimithigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentmeasurelimithigh.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a high limit current value, in amps, for output cutoff. If the measured current exceeds this limit, the output is disconnected. To find out whether an output has exceeded this limit, call the Query Latched Output Cutoff State VI with Current Measure High as the reason . NI-DCPower uses the

### Source:Output Cutoff:Current Measure Limit High

Specifies a high limit current value, in amps, for output cutoff. If the measured current exceeds this limit, the output is disconnected.

To find out whether an output has exceeded this limit, call the
 [Query Latched Output Cutoff State](/csh?context=nidcpower_nidcpowerviref_nidcpower_query_latched_output_cutoff_state)
 VI with
 **Current Measure High**
 as the
 **reason**
 .

Note

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Cutoff Current Measure Limit High |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentmeasurelimitlow.html language=enus -->
## TOPIC 00228: Source:Output Cutoff:Current Measure Limit Low

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentmeasurelimitlow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentmeasurelimitlow.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a low limit current value, in amps, for output cutoff. If the measured current falls below this limit, the output is disconnected. To find out whether an output has fallen below this limit, call the Query Latched Output Cutoff State VI with Current Measure Low as the reason . NI-DCPower us

### Source:Output Cutoff:Current Measure Limit Low

Specifies a low limit current value, in amps, for output cutoff. If the measured current falls below this limit, the output is disconnected.

To find out whether an output has fallen below this limit, call the
 [Query Latched Output Cutoff State](/csh?context=nidcpower_nidcpowerviref_nidcpower_query_latched_output_cutoff_state)
 VI with
 **Current Measure Low**
 as the
 **reason**
 .

Note

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Cutoff Current Measure Limit Low |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentoverrangeenabled.html language=enus -->
## TOPIC 00229: Source:Output Cutoff:Current Overrange Enabled

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentoverrangeenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffcurrentoverrangeenabled.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables current overrange functionality for output cutoff. If enabled, the output is disconnected when the measured current saturates the current range. To find out whether an output has exceeded this limit, call the Query Latched Output Cutoff State VI with Current Saturated as the reas

### Source:Output Cutoff:Current Overrange Enabled

Enables or disables current overrange functionality for output cutoff. If enabled, the output is disconnected when the measured current saturates the current range.

To find out whether an output has exceeded this limit, call the
 [Query Latched Output Cutoff State](/csh?context=nidcpower_nidcpowerviref_nidcpower_query_latched_output_cutoff_state)
 VI with
 **Current Saturated**
 as the
 **reason**
 .

Note

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Cutoff Current Overrange Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffdelay.html language=enus -->
## TOPIC 00230: Source:Output Cutoff:Delay

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffdelay.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Delays disconnecting the output by the time you specify, in seconds, when a limit is exceeded. NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively. This property is not supported by all instrum

### Source:Output Cutoff:Delay

Delays disconnecting the output by the time you specify, in seconds, when a limit is exceeded.

Note

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Cutoff Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffenabled.html language=enus -->
## TOPIC 00231: Source:Output Cutoff:Enabled

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffenabled.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables output cutoff functionality. If enabled, you can define output cutoffs that, if exceeded, cause the output of the specified channel(s) to be disconnected. When this property is disabled, all other output cutoff properties are ignored. NI-DCPower uses the terms "source" and "outpu

### Source:Output Cutoff:Enabled

Enables or disables output cutoff functionality. If enabled, you can define output cutoffs that, if exceeded, cause the output of the specified channel(s) to be disconnected.

When this property is disabled, all other output cutoff properties are ignored.

Note

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Cutoff Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagechangelimithigh.html language=enus -->
## TOPIC 00232: Source:Output Cutoff:Voltage Change Limit High

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagechangelimithigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagechangelimithigh.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a limit for positive voltage slew rate, in volts per microsecond, for output cutoff. If the voltage increases at a rate that exceeds this limit, the output is disconnected. To find out whether an output has exceeded this limit, call the Query Latched Output Cutoff State VI with Voltage Cha

### Source:Output Cutoff:Voltage Change Limit High

Specifies a limit for positive voltage slew rate, in volts per microsecond, for output cutoff. If the voltage increases at a rate that exceeds this limit, the output is disconnected.

To find out whether an output has exceeded this limit, call the
 [Query Latched Output Cutoff State](/csh?context=nidcpower_nidcpowerviref_nidcpower_query_latched_output_cutoff_state)
 VI with
 **Voltage Change High**
 as the
 **reason**
 .

Note

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Cutoff Voltage Change Limit High |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagechangelimitlow.html language=enus -->
## TOPIC 00233: Source:Output Cutoff:Voltage Change Limit Low

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagechangelimitlow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagechangelimitlow.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a limit for negative voltage slew rate, in volts per microsecond, for output cutoff. If the voltage decreases at a rate that exceeds this limit, the output is disconnected. To find out whether an output has exceeded this limit, call the Query Latched Output Cutoff State VI with Voltage Cha

### Source:Output Cutoff:Voltage Change Limit Low

Specifies a limit for negative voltage slew rate, in volts per microsecond, for output cutoff. If the voltage decreases at a rate that exceeds this limit, the output is disconnected.

To find out whether an output has exceeded this limit, call the
 [Query Latched Output Cutoff State](/csh?context=nidcpower_nidcpowerviref_nidcpower_query_latched_output_cutoff_state)
 VI with
 **Voltage Change Low**
 as the
 **reason**
 .

Note

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Cutoff Voltage Change Limit Low |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagemeasurelimithigh.html language=enus -->
## TOPIC 00234: Source:Output Cutoff:Voltage Measure Limit High

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagemeasurelimithigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagemeasurelimithigh.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a high limit voltage value, in volts, for output cutoff. If the measured voltage exceeds this limit, the output is disconnected. To find out whether an output has exceeded this limit, call the Query Latched Output Cutoff State VI with Voltage Measure High as the reason . NI-DCPower uses th

### Source:Output Cutoff:Voltage Measure Limit High

Specifies a high limit voltage value, in volts, for output cutoff. If the measured voltage exceeds this limit, the output is disconnected.

To find out whether an output has exceeded this limit, call the
 [Query Latched Output Cutoff State](/csh?context=nidcpower_nidcpowerviref_nidcpower_query_latched_output_cutoff_state)
 VI with
 **Voltage Measure High**
 as the
 **reason**
 .

Note

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Cutoff Voltage Measure Limit High |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagemeasurelimitlow.html language=enus -->
## TOPIC 00235: Source:Output Cutoff:Voltage Measure Limit Low

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagemeasurelimitlow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltagemeasurelimitlow.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a low limit voltage value, in volts, for output cutoff. If the measured voltage falls below this limit, the output is disconnected. To find out whether an output has fallen below this limit, call the Query Latched Output Cutoff State VI with Voltage Measure Low as the reason . NI-DCPower u

### Source:Output Cutoff:Voltage Measure Limit Low

Specifies a low limit voltage value, in volts, for output cutoff. If the measured voltage falls below this limit, the output is disconnected.

To find out whether an output has fallen below this limit, call the
 [Query Latched Output Cutoff State](/csh?context=nidcpower_nidcpowerviref_nidcpower_query_latched_output_cutoff_state)
 VI with
 **Voltage Measure Low**
 as the
 **reason**
 .

Note

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Cutoff Voltage Measure Limit Low |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltageoutputlimithigh.html language=enus -->
## TOPIC 00236: Source:Output Cutoff:Voltage Output Limit High

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltageoutputlimithigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltageoutputlimithigh.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a high limit voltage value, in volts, for output cutoff. If the voltage output exceeds this limit, the output is disconnected. To find out whether an output has exceeded this limit, call the Query Latched Output Cutoff State VI with Voltage Output High as the reason . NI-DCPower uses the t

### Source:Output Cutoff:Voltage Output Limit High

Specifies a high limit voltage value, in volts, for output cutoff. If the voltage output exceeds this limit, the output is disconnected.

To find out whether an output has exceeded this limit, call the
 [Query Latched Output Cutoff State](/csh?context=nidcpower_nidcpowerviref_nidcpower_query_latched_output_cutoff_state)
 VI with
 **Voltage Output High**
 as the
 **reason**
 .

Note

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Cutoff Voltage Output Limit High |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltageoutputlimitlow.html language=enus -->
## TOPIC 00237: Source:Output Cutoff:Voltage Output Limit Low

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltageoutputlimitlow.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputcutoffvoltageoutputlimitlow.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a low limit voltage value, in volts, for output cutoff. If the voltage output falls below this limit, the output is disconnected. To find out whether an output has fallen below this limit, call the Query Latched Output Cutoff State VI with Voltage Output Low as the reason . NI-DCPower uses

### Source:Output Cutoff:Voltage Output Limit Low

Specifies a low limit voltage value, in volts, for output cutoff. If the voltage output falls below this limit, the output is disconnected.

To find out whether an output has fallen below this limit, call the
 [Query Latched Output Cutoff State](/csh?context=nidcpower_nidcpowerviref_nidcpower_query_latched_output_cutoff_state)
 VI with
 **Voltage Output Low**
 as the
 **reason**
 .

Note

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Cutoff Voltage Output Limit Low |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputenabled.html language=enus -->
## TOPIC 00238: Source:Output Enabled

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputenabled.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the output is enabled (TRUE) or disabled (FALSE). Depending on the value you specify for the Output Function property, you also must set the corresponding level properties or Output Resistance in addition to enabling the output to generate the desired level. For more information ab

### Source:Output Enabled

Specifies whether the output is enabled (TRUE) or disabled (FALSE).

Depending on the value you specify for the
 [Output Function](pnidcpower-outputfunction.html)
 property, you also must set the corresponding level properties or
 [Output Resistance](pnidcpower-outputresistance.html)
 in addition to enabling the output to generate the desired level.
 For more information about configuring the output level, refer to the
 [Output Function](pnidcpower-outputfunction.html)
 property.

This property has no effect on the output disconnect relay. To toggle the relay, use the
 [Output Connected](pnidcpower-outputconnected.html)
 property.

Note

niDCPower Initiate With Channels

Programming States

NI DC Power Supplies and SMUs Help

Note

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Output Enabled |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputfunction.html language=enus -->
## TOPIC 00239: Source:Output Function

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputfunction.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputfunction.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the function to generate on the specified channel(s). When DC Voltage is selected, the device generates the desired voltage level on the output as long as the output current is below the current limit. Use the following properties to configure the channel when DC Voltage is selected: Volt

### Source:Output Function

Configures the function to generate on the specified channel(s).

When
 **DC Voltage**
 is selected, the device generates the desired voltage level on the output as long as the output current is below the current limit. Use the following properties to configure the channel when
 **DC Voltage**
 is selected:

- Voltage Level
- Current Limit
- Current Limit High
- Current Limit Low
- Voltage Level Range
- Current Limit Range
- Compliance Limit Symmetry

When
 **DC Current**
 is selected, the device generates the desired current level on the output as long as the output voltage is below the voltage limit. Use the following properties to configure the channel when
 **DC Current**
 is selected:

- Current Level
- Voltage Limit
- Voltage Limit High
- Voltage Limit Low
- Current Level Range
- Voltage Limit Range
- Compliance Limit Symmetry

When
 **Pulse Voltage**
 is selected, the device generates pulses at the desired pulse voltage levels on the output as long as the output current is below the pulse current limit. Use the following properties to configure the channel when
 **Pulse Voltage**
 is selected:

- Pulse Voltage Level
- Pulse Bias Voltage Level
- Pulse Current Limit
- Pulse Current Limit High
- Pulse Current Limit Low
- Pulse Bias Current Limit
- Pulse Bias Current Limit High
- Pulse Bias Current Limit Low
- Pulse Voltage Level Range
- Pulse Current Limit Range
- Compliance Limit Symmetry

When
 **Pulse Current**
 is selected, the device generates pulses at the desired pulse current levels on the output as long as the output voltage is below the pulse voltage limit. Use the following properties to configure the channel when
 **Pulse Current**
 is selected:

- Pulse Current Level
- Pulse Bias Current Level
- Pulse Voltage Limit
- Pulse Voltage Limit High
- Pulse Voltage Limit Low
- Pulse Bias Voltage Limit
- Pulse Bias Voltage Limit High
- Pulse Bias Voltage Limit Low
- Pulse Current Level Range
- Pulse Voltage Limit Range
- Compliance Limit Symmetry

When
 **Constant Resistance**
 is selected, the device generates the desired resistance level on the output as long as the output current is below the current limit. Use the following properties to configure the channel when
 **Constant Resistance**
 is selected:

- Constant Resistance Level
- Constant Resistance Current Limit
- Constant Resistance Level Range

When
 **Constant Power**
 is selected, the device generates the desired power level on the output as long as the output current is below the current limit. Use the following properties to configure the channel when
 **Constant Power**
 is selected:

- Constant Power Level
- Constant Power Current Limit
- Constant Power Level Range

Note

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Function |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Output Function |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| DC Voltage | 1006 | Sets the output function to DC voltage. |
| --- | --- | --- |
| DC Current | 1007 | Sets the output function to DC current. |
| Pulse Voltage | 1049 | Sets the output function to pulse voltage. |
| Pulse Current | 1050 | Sets the output function to pulse current. |
| Constant Resistance | 1161 | Sets the output function to constant resistance. |
| Constant Power | 1162 | Sets the output function to constant power. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputresistance.html language=enus -->
## TOPIC 00240: Source:Output Resistance

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputresistance.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output resistance that the device attempts to generate for the specified channel(s). Depending on the instrument, output resistance is configurable only if you set the Output Function of the channel as follows: PXIe-4141, PXIe-4143, PXIe-4145: DC Voltage PXIe-4135, PXIe-4137, PXIe-4139

### Source:Output Resistance

Specifies the output resistance that the device attempts to generate for the specified channel(s).

Depending on the instrument, output resistance is configurable only if you set the
 [Output Function](/csh?context=nidcpower_dcpowerpropref_pnidcpower_outputfunction)
 of the channel as follows:

- PXIe-4141, PXIe-4143, PXIe-4145:
 DC Voltage
- PXIe-4135, PXIe-4137, PXIe-4139, PXIe-4147, PXIe-4162, PXIe-4163:
 DC Current 
 or
 DC Voltage

Note

Output Enabled

Note

Merged Channels

Note

Output Function

Constant Resistance

Constant Resistance Level

Note

Note

Supported Properties by Device

**Valid Values**
 : Vary by device. Refer to the device specifications for your device for more
 information about supported values.

**Default Value**
 : Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Resistance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Output Resistance |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputshorted.html language=enus -->
## TOPIC 00241: Source:Advanced:Output Shorted

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputshorted.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-outputshorted.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the input of the instrument simulates a short circuit. When this property is set to TRUE, the instrument will simulate a short circuit across the channel/input terminals. The electronic load uses the maximum rated current and range to simulate the short circuit. This property will

### Source:Advanced:Output Shorted

Specifies whether the input of the instrument simulates a short circuit.

When this property is set to TRUE,
 the instrument will simulate a short circuit across the channel/input terminals.
 The electronic load uses the maximum rated current and range to simulate the short circuit.
 This property will only take effect when both [NIDCPOWER_ATTR_OUTPUT_ENABLED](pnidcpower-outputenabled.html) and [NIDCPOWER_ATTR_OUTPUT_CONNECTED](pnidcpower-outputconnected.html) are TRUE.
 When this property is set to FALSE,
 the instrument will resume normal operation based on its existing settings on the specified channel(s).

Note

Supported Properties by Device

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Output Shorted |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-overrangingenabled.html language=enus -->
## TOPIC 00242: Source:Advanced:Overranging Enabled

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-overrangingenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-overrangingenabled.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether NI-DCPower allows setting the voltage level , current level , voltage limit , and current limit outside the device specification limits. TRUE means that overranging is enabled. Default Value :Refer to Supported Properties by Device for the default value by device. To specify a chan

### Source:Advanced:Overranging Enabled

Specifies whether NI-DCPower allows setting the
 [voltage level](/csh?context=nidcpower_nidcpowerviref_nidcpower_configure_voltage_level)
 ,
 [current level](/csh?context=nidcpower_nidcpowerviref_nidcpower_configure_current_level)
 ,
 [voltage limit](/csh?context=nidcpower_nidcpowerviref_nidcpower_configure_voltage_limit)
 , and
 [current limit](/csh?context=nidcpower_nidcpowerviref_nidcpower_configure_current_limit)
 outside the device specification limits. TRUE means that overranging is enabled.

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Overranging Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-ovpenabled.html language=enus -->
## TOPIC 00243: Source:Advanced:OVP Enabled

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-ovpenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-ovpenabled.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables (TRUE) or disables (FALSE) overvoltage protection (OVP). This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices. Defined Values FALSE Overvoltage protection is disabled. TRUE Overvoltage protection is enabled. Default Va

### Source:Advanced:OVP Enabled

Enables (TRUE) or disables (FALSE) overvoltage protection (OVP).

Note

Supported Properties by Device

**Defined Values**

| FALSE | Overvoltage protection is disabled. |
| --- | --- |
| TRUE | Overvoltage protection is enabled. |

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OVP Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-ovplimit.html language=enus -->
## TOPIC 00244: Source:Advanced:OVP Limit

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-ovplimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-ovplimit.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the voltage limit, in volts, beyond which overvoltage protection (OVP) engages. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. For example, setting the OVP Limit to 65 will configure the OVP feature to trigger an OVP error i

### Source:Advanced:OVP Limit

Determines the voltage limit, in volts, beyond which overvoltage protection (OVP) engages. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. For example, setting the OVP Limit to 65 will configure the OVP feature to trigger an OVP error if the output exceeds ±65 V.

Note

Note

Supported Properties by Device

**Valid Values**
 :Vary by device.

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OVP Limit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powerallocationmode.html language=enus -->
## TOPIC 00245: Source:Advanced:Power Allocation Mode

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powerallocationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powerallocationmode.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the device sources the power its source configuration requires or a specific wattage you request; determines whether NI-DCPower proactively checks that this sourcing power is within the maximum per-channel and overall sourcing power of the device. When this property configures NI-

### Source:Advanced:Power Allocation Mode

Determines whether the device sources the power its source configuration requires or a specific wattage you request; determines whether NI-DCPower proactively checks that this sourcing power is within the maximum per-channel and overall sourcing power of the device.

When this property configures NI-DCPower to perform a sourcing power check, a device is not permitted to source power in excess of its maximum per-channel or overall sourcing power. If the check determines a source configuration or power request would require the device to do so, NI-DCPower returns an error.

When this property does not configure NI-DCPower to perform a sourcing power check, a device can attempt to fulfill source configurations that would require it to source power in excess of its maximum per-channel or overall sourcing power and may shut down to prevent damage.

Note

Note

Supported Properties by Device

Disabled

**Default Value**
 : Refer to
 [Supported Properties by Devices](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Power Allocation Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| Disabled | 1058 | The device attempts to source, on each active channel, the power that the present source configuration requires; NI-DCPower does not perform a sourcing power check. If the required power is greater than the maximum sourcing power, the device attempts to source the required amount and may shut down to prevent damage. |
| --- | --- | --- |
| Automatic | 1059 | The device attempts to source, on each active channel, the power that the present source configuration requires; NI-DCPower performs a sourcing power check. If the required power is greater than the maximum sourcing power, the device does not exceed the maximum power, and NI-DCPower returns an error. |
| Manual | 1060 | The device attempts to source, on each active channel, the power you request with the Requested Power Allocation property; NI-DCPower performs a sourcing power check. If the requested power is either less than the required power for the present source configuration or greater than the maximum sourcing power, the device does not exceed the requested or allowed power, respectively, and NI-DCPower returns an error. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powerlinefrequency.html language=enus -->
## TOPIC 00246: Measurement:Power Line Frequency

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powerlinefrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powerlinefrequency.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power line frequency for specified channel(s). NI-DCPower uses this value to select a timebase for setting the Aperture Time property in power line cycles (PLCs). This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devi

### Measurement:Power Line Frequency

Specifies the power line frequency for specified channel(s). NI-DCPower uses this value to select a timebase for setting the
 [Aperture Time](/csh?topicname=pnidcpower-aperturetime.html)
 property in power line cycles (PLCs).

Note

Supported Properties by Device

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Power Line Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Power Line Frequency |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

| 60 Hertz | 60 | Specifies a power line frequency of 60 Hz. |
| --- | --- | --- |
| 50 Hertz | 50 | Specifies a power line frequency of 50 Hz. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powersource.html language=enus -->
## TOPIC 00247: Advanced:Power Source

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powersource.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powersource.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For sessions initialized with deprecated Initialize VIs, this property specifies the power source to use. NI-DCPower switches the power source used by the device to the specified value. This property is not supported in sessions initialized with the niDCPower Initialize With Independent Channels VI.

### Advanced:Power Source

For sessions initialized with deprecated Initialize VIs, this property specifies the power source to use. NI-DCPower switches the power source used by the device to the specified value.

This property is not supported in sessions initialized with the
 [niDCPower Initialize With Independent Channels](/csh?context=nidcpower_nidcpowerviref_nidcpower_initialize_with_channels)
 VI.

Note

Automatic

Committed or Uncommitted

**Default Value**
 :Refer to
 [Supported Properties by Device](/csh?context=nidcpower_nidcpowerviref_supportedproperties)
 for the default value by device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Power Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

| Internal | 1003 | Uses the PXI chassis power source. |
| --- | --- | --- |
| Auxiliary | 1004 | Uses the auxiliary power source connected to the device. |
| Automatic | 1005 | Uses the auxiliary power source if it is available; otherwise, use the PXI chassis power source. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powersourceinuse.html language=enus -->
## TOPIC 00248: Advanced:Power Source In Use

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powersourceinuse.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-powersourceinuse.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the device is using the internal or auxiliary power source to generate power. This property is not supported in sessions initialized with independent channels. Remarks The following table lists the characteristics of this property. Short Name Power Source In Use Data type ci32.png

### Advanced:Power Source In Use

Indicates whether the device is using the internal or auxiliary power source to generate power.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Power Source In Use |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Instrument-based | No |
| Resettable | No |

| Internal | 1003 | Uses the PXI chassis power source. |
| --- | --- | --- |
| Auxiliary | 1004 | Uses the auxiliary power source connected to the device. Only the NI PXI-4110, NI PXIe-4112, NI PXIe-4113, and NI PXI-4130 support this value. This is the only supported value for the NI PXIe-4112 and NI PXIe-4113. |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlevel.html language=enus -->
## TOPIC 00249: Source:Pulse Current:Pulse Bias Current Level

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlevel.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse bias current level, in amps, that the device attempts to generate on the specified channel(s) during the off phase of a pulse. This property is applicable only if the Output Function property is set to Pulse Current . The channel must be enabled for the specified pulse bias curre

### Source:Pulse Current:Pulse Bias Current Level

Specifies the pulse bias current level, in amps, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Current**
 .

Note

Output Enabled

Note

Supported Properties by Device

**Valid Values:**
 The valid values for this property are defined by the values you specify for the
 [Pulse Current Level Range](pnidcpower-pulsecurrentlevelrange.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Bias Current Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Pulse Bias Current Level |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties

<!--NI_TOPIC bundle=ni-dcpower-labview-api-ref path=instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlimit.html language=enus -->
## TOPIC 00250: Source:Pulse Voltage:Pulse Bias Current Limit

- bundle_id: `ni-dcpower-labview-api-ref`
- source_path: `instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-labview-api-ref/raw/resource/enus/instr-lib/nidcpower/nidcpower-rc/nidcpower/pnidcpower-pulsebiascurrentlimit.html
- document_id: `ni-dcpower-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse bias current limit, in amps, that the output cannot exceed when generating the desired pulse bias voltage on the specified channel(s) during the off phase of a pulse. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously. T

### Source:Pulse Voltage:Pulse Bias Current Limit

Specifies the pulse bias current limit, in amps, that the output cannot exceed when generating the desired pulse bias voltage on the specified channel(s) during the off phase of a pulse. Limit is specified as a positive value, but symmetric positive and negative limits are enforced simultaneously.

This property is applicable only if the
 [Output Function](pnidcpower-outputfunction.html)
 property is set to
 **Pulse Voltage**
 and the
 [Compliance Limit Symmetry](pnidcpower-compliancelimitsymmetry.html)
 property is set to
 **Symmetric**
 .

Note

Output Enabled

Note

Note

Supported Properties by Device

**Valid Values:**
 The valid values for this property are defined by the values you specify for the
 [Pulse Current Limit Range](pnidcpower-pulsecurrentlimitrange.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Bias Current Limit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDCPower Configure Pulse Bias Current Limit |
| Channel-based | Yes |
| Instrument-based | No |
| Resettable | No |

Parent topic:

niDCPower Properties
