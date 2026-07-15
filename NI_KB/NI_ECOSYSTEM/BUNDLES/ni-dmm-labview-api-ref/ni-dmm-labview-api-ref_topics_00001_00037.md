# NI DOCUMENT BUNDLE: ni-dmm-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-dmm-labview-api-ref start=1 end=37 -->
<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/calib-mnu.html language=enus -->
## TOPIC 00001: Calibration

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/calib-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/calib-mnu.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DMM Calibration VIs to perform a self-calibration or external calibration on the DMM. icon

### Calibration

Use the NI-DMM Calibration VIs to perform a self-calibration or external calibration on the DMM.

[IMAGE alt='icon' src='calib-mnu.png']

- [niDMM Self Cal VI](../../instr-lib/nidmm/nidmm-llb/nidmm-self-cal-vi.html) Executes the self-calibration routine to maintain measurement accuracy.
- [External Calibration](../../instr-lib/nidmm/extcal-mnu.html) Use the NI-DMM External Calibration VIs to perform an external calibration on the DMM.
- [Calibration Utility](../../instr-lib/nidmm/calutil-mnu.html) Use the NI-DMM Calibration Utility VIs for optional functionality when performing a calibration.

Parent topic:

NI-DMM

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/calutil-mnu.html language=enus -->
## TOPIC 00002: Calibration Utility

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/calutil-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/calutil-mnu.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DMM Calibration Utility VIs for optional functionality when performing a calibration. icon

### Calibration Utility

Use the NI-DMM Calibration Utility VIs for optional functionality when performing a calibration.

[IMAGE alt='icon' src='calutil-mnu.png']

- [niDMM Get Cal Count VI](../../instr-lib/nidmm/nidmm-llb/nidmm-get-cal-count-vi.html) Returns the calibration count for the specified type of calibration.
- [niDMM Get Cal Date and Time VI](../../instr-lib/nidmm/nidmm-llb/nidmm-get-cal-date-and-time-vi.html) Returns the date and time of the last calibration performed.
- [niDMM Get Last Cal Temp VI](../../instr-lib/nidmm/nidmm-llb/nidmm-get-last-cal-temp-vi.html) Returns the temperature during the last calibration procedure.
- [niDMM Get Dev Temp VI](../../instr-lib/nidmm/nidmm-llb/nidmm-get-dev-temp-vi.html) Returns the current temperature of the device.
- [niDMM Get External Cal Recommended Interval VI](../../instr-lib/nidmm/nidmm-llb/nidmm-get-external-cal-recommended-interval-vi.html) Returns the recommended interval between external recalibration in months.
- [niDMM Get Self Cal Supported VI](../../instr-lib/nidmm/nidmm-llb/nidmm-get-self-cal-supported-vi.html) Returns a Boolean value that expresses whether the DMM that you are using can perform self-calibration.
- [niDMM Get Cal User Defined Info Max Size VI](../../instr-lib/nidmm/nidmm-llb/nidmm-get-cal-user-defined-info-max-size-vi.html) Returns the maximum string length that can be stored in the EEPROM.
- [niDMM Get Cal User Defined Info VI](../../instr-lib/nidmm/nidmm-llb/nidmm-get-cal-user-defined-info-vi.html) Returns the user-defined calibration information stored in the EEPROM.
- [niDMM Restore Last External Cal Constants VI](../../instr-lib/nidmm/nidmm-llb/nidmm-restore-last-external-cal-constants-vi.html) Reverts the device to the calibration constants from the last complete external calibration. This VI recovers the hardware if a fatal system error occurs during an external or self-calibration procedure.
- [niDMM Set Cal Password VI](../../instr-lib/nidmm/nidmm-llb/nidmm-set-cal-password-vi.html) Changes the password required to enable external calibration functionality. The maximum password string length is eight characters, excluding the termination character. "NI" is the default password. A password is required for external calibration. Be sure to record the password in a secure location.
- [niDMM Set Cal User Defined Info VI](../../instr-lib/nidmm/nidmm-llb/nidmm-set-cal-user-defined-info-vi.html) Stores the user-defined information in the EEPROM.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/config-mnu.html language=enus -->
## TOPIC 00003: Configuration

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/config-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/config-mnu.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DMM Configuration VIs for hardware-specific configuration and control. icon

### Configuration

Use the NI-DMM Configuration VIs for hardware-specific configuration and control.

[IMAGE alt='icon' src='config-mnu.png']

- [niDMM Config Measurement VI](../../instr-lib/nidmm/nidmm-llb/nidmm-config-measurement-vi.html) Specifies the measurement resolution in digits or in absolute units. This VI is polymorphic. To change the selected instance of this polymorphic VI, right-click the VI and choose Select Type followed by Resolution in Digits or Absolute Resolution.
- [niDMM Configure Multi Point VI](../../instr-lib/nidmm/nidmm-llb/nidmm-configure-multi-point-vi.html) Configures the properties for multipoint measurements.
- [niDMM Configure Waveform Acquisition VI](../../instr-lib/nidmm/nidmm-llb/nidmm-configure-waveform-acquisition-vi.html) Configures the device for waveform acquisitions.
- [Measurement Options](../../instr-lib/nidmm/measopt-mnu.html) Use the NI-DMM Measurement Options VIs for additional configuration functionality.
- [niDMM Import Attribute Configuration (Poly) VI](../../instr-lib/nidmm/nidmm-llb/nidmm-import-attribute-configuration-poly-vi.html) Imports an attribute configuration to the session from either a file or a buffer.
- [niDMM Export Attribute Configuration (Poly) VI](../../instr-lib/nidmm/nidmm-llb/nidmm-export-attribute-configuration-poly-vi.html) Exports the attribute configuration of a session to either a file or a buffer.
- [Trigger](../../instr-lib/nidmm/trigger-mnu.html) Use the NI-DMM Trigger VIs to customize the triggering functionality for your application.
- [Actual Values](../../instr-lib/nidmm/values-mnu.html) Use the NI-DMM Actual Values VIs to return optional values.

Parent topic:

NI-DMM

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/dir-mnu.html language=enus -->
## TOPIC 00004: NI-DMM

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/dir-mnu.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DMM VIs to develop applications for your NI digital multimeter. icon

### NI-DMM

Use the NI-DMM VIs to develop applications for your NI digital multimeter.

[IMAGE alt='icon' src='dir-mnu.png']

- [niDMM Initialize VI](../../instr-lib/nidmm/nidmm-llb/nidmm-initialize-vi.html) This VI completes the following tasks:
- [niDMM Initialize With Options VI](../../instr-lib/nidmm/nidmm-llb/nidmm-initialize-with-options-vi.html) This VI completes the following tasks:
- [niDMM Close VI](../../instr-lib/nidmm/nidmm-llb/nidmm-close-vi.html) Closes the specified session and deallocates resources that it reserved.
- [niDMM Property Node VI](../../instr-lib/nidmm/nidmm-llb/nidmm-property-node-vi.html) The niDMM Property Node is used to set, get, or check properties.
- [Configuration](../../instr-lib/nidmm/config-mnu.html) Use the NI-DMM Configuration VIs for hardware-specific configuration and control.
- [Acquisition](../../instr-lib/nidmm/read-mnu.html) Use the NI-DMM Acquisition VIs to acquire data from a measurement.
- [Calibration](../../instr-lib/nidmm/calib-mnu.html) Use the NI-DMM Calibration VIs to perform a self-calibration or external calibration on the DMM.
- [Utility](../../instr-lib/nidmm/utility-mnu.html) Use the NI-DMM Utility functions for optional functionality in your application.

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/extcal-mnu.html language=enus -->
## TOPIC 00005: External Calibration

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/extcal-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/extcal-mnu.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DMM External Calibration VIs to perform an external calibration on the DMM. icon

### External Calibration

Use the NI-DMM External Calibration VIs to perform an external calibration on the DMM.

[IMAGE alt='icon' src='extcal-mnu.png']

- [niDMM Initialize External Cal VI](../../instr-lib/nidmm/nidmm-llb/nidmm-initialize-external-cal-vi.html) The following operations are performed if the Calibration Password is valid:
- [niDMM Close External Cal VI](../../instr-lib/nidmm/nidmm-llb/nidmm-close-external-cal-vi.html) Performs the specified Action , closes the specified external calibration session obtained from niDMM Initialize External Cal, and deallocates resources that it reserved.
- [niDMM Cal Adjust Gain VI](../../instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-gain-vi.html) Calibrates the gain coefficient for the supplied Function , Range , and Input Resistance .
- [niDMM Cal Adjust Offset VI](../../instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-offset-vi.html) Calibrates the offset and Auto Zero offset for the supplied Function , Range , and Input Resistance .
- [niDMM Cal Adjust AC Filter VI](../../instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-ac-filter-vi.html) Calibrates the filter coefficients used for AC measurements of the supplied Function and Range .
- [niDMM Cal Adjust Linearization VI](../../instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-linearization-vi.html) (NI 4065 only) Compensates for any non-linearities.
- [niDMM Cal Adjust Miscellaneous VI](../../instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-miscellaneous-vi.html) Performs a specialized calibration step depending on the specified Type .
- [niDMM Cal Adjust LC VI](../../instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-lc-vi.html) (NI 4082 and NI 4072 only) Performs a specialized LC calibration step depending on the specified Stage .

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/fetch-mnu.html language=enus -->
## TOPIC 00006: Fetch

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/fetch-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/fetch-mnu.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DMM Fetch VIs to add low-level control to your application. icon

### Fetch

Use the NI-DMM Fetch VIs to add low-level control to your application.

[IMAGE alt='icon' src='fetch-mnu.png']

- [niDMM Initiate VI](../../instr-lib/nidmm/nidmm-llb/nidmm-initiate-vi.html) Initiates an acquisition. After you call this VI, the DMM leaves the Idle state and enters the Wait-For-Trigger state. If trigger is set to Immediate mode, the DMM begins acquiring measurement data.
- [niDMM Fetch VI](../../instr-lib/nidmm/nidmm-llb/nidmm-fetch-vi.html) Returns the value from a previously initiated measurement.
- [niDMM Fetch Multi Point VI](../../instr-lib/nidmm/nidmm-llb/nidmm-fetch-multi-point-vi.html) Returns an array of values from a previously initiated multipoint measurement.
- [niDMM Fetch Waveform VI](../../instr-lib/nidmm/nidmm-llb/nidmm-fetch-waveform-vi.html) Returns an array of values from a previously initiated waveform acquisition. This VI is polymorphic. To change the selected instance of this polymorphic VI, right-click the VI and choose Select Type followed by the waveform data or floating point array version of the VI.
- [niDMM Read Status VI](../../instr-lib/nidmm/nidmm-llb/nidmm-read-status-vi.html) Returns measurement backlog and acquisition status.
- [niDMM Abort VI](../../instr-lib/nidmm/nidmm-llb/nidmm-abort-vi.html) Aborts a previously initiated measurement and returns the DMM to the Idle state.
- [niDMM Control VI](../../instr-lib/nidmm/nidmm-llb/nidmm-control-vi.html) Controls the DMM. Use this VI if you want a parameter change to be immediately reflected in the hardware. Use this VI before calling niDMM Initiate to make the initiate call as quickly as possible. Calling this VI while the DMM is taking measurements results in an error. After the DMM is finished taking measurements, calling this VI will make any unfetched data points unavailable.

Parent topic:

Acquisition

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/iviutil-mnu.html language=enus -->
## TOPIC 00007: IVI Utilities

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/iviutil-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/iviutil-mnu.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DMM IVI Utilities VIs to add IVI-inherent options to your application. icon

### IVI Utilities

Use the NI-DMM IVI Utilities VIs to add IVI-inherent options to your application.

[IMAGE alt='icon' src='iviutil-mnu.png']

- [niDMM Error Message VI](../../instr-lib/nidmm/nidmm-llb/nidmm-error-message-vi.html) Takes the error cluster returned by the NI-DMM VIs, interprets it, and returns it as a user-readable string.
- [niDMM Reset with Defaults VI](../../instr-lib/nidmm/nidmm-llb/nidmm-reset-with-defaults-vi.html) Resets the DMM to a known state and sends initialization commands to the DMM. The initialization commands set the DMM to the state necessary for the operation of NI-DMM. All user-defined default values associated with a logical name are applied after setting the DMM.
- [niDMM Disable VI](../../instr-lib/nidmm/nidmm-llb/nidmm-disable-vi.html) Places the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected. If a measurement is in progress when this VI is called, the measurement is aborted.
- [niDMM Get Next Coercion Record VI](../../instr-lib/nidmm/nidmm-llb/nidmm-get-next-coercion-record-vi.html) Returns the coercion information associated with the IVI session, and it retrieves and clears the oldest instance in which NI-DMM coerced a value you specified to another value.
- [niDMM Get Next Interchange Warning VI](../../instr-lib/nidmm/nidmm-llb/nidmm-get-next-interchange-warning-vi.html) Returns the interchangeability warnings associated with the IVI session. It retrieves and clears the oldest instance in which the class driver recorded an interchangeability warning. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior.
- [niDMM Clear Interchange Warnings VI](../../instr-lib/nidmm/nidmm-llb/nidmm-clear-interchange-warnings-vi.html) Clears the list of current interchange warnings.
- [niDMM Reset Interchange Check VI](../../instr-lib/nidmm/nidmm-llb/nidmm-reset-interchange-check-vi.html) When developing a complex test system that consists of multiple test modules, it is generally a good idea to design the test modules so that they can run in any order. To do so requires ensuring that each test module completely configures the state of each instrument it uses. If a particular test module does not completely configure the state of an instrument, the state of the instrument depends on the configuration from a previously executed test module.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/lcopt-mnu.html language=enus -->
## TOPIC 00008: Capacitance and Inductance

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/lcopt-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/lcopt-mnu.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DMM Capacitance and Inductance VIs for control of the inductance and capacitance capabilities on the NI 4072. icon

### Capacitance and Inductance

Use the NI-DMM Capacitance and Inductance VIs for control of the inductance and capacitance capabilities on the NI 4072.

[IMAGE alt='icon' src='lcopt-mnu.png']

- [niDMM Configure Cable Comp Type VI](../../instr-lib/nidmm/nidmm-llb/nidmm-configure-cable-comp-type-vi.html) (NI 4082 and NI 4072 only) Sets the Cable Compensation Type property for the current capacitance/inductance mode range.
- [niDMM Configure Open Cable Comp Values VI](../../instr-lib/nidmm/nidmm-llb/nidmm-configure-open-cable-comp-values-vi.html) (NI 4082 and NI 4072 only) Configures the Open Cable Comp Conductance and Open Cable Comp Susceptance properties.
- [niDMM Configure Short Cable Comp Values VI](../../instr-lib/nidmm/nidmm-llb/nidmm-configure-short-cable-comp-values-vi.html) (NI 4082 and NI 4072 only) Configures the Cable Comp Resistance and Short Cable Comp Reactance properties.
- [niDMM Perform Open Cable Comp VI](../../instr-lib/nidmm/nidmm-llb/nidmm-perform-open-cable-comp-vi.html) (NI 4082 and NI 4072 only) Performs the open cable compensation measurements for the current capacitance/inductance range, and returns open cable compensation Conductance and Susceptance values.
- [niDMM Perform Short Cable Comp VI](../../instr-lib/nidmm/nidmm-llb/nidmm-perform-short-cable-comp-vi.html) (NI 4082 and NI 4072 only) Performs the short cable compensation measurements for the current capacitance/inductance range and returns short cable compensation Resistance and Reactance values. This VI returns an error if the value of the Function property is not set to CAPACITANCE (1005) or INDUCTANCE (1006).

Parent topic:

Measurement Options

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-gain-vi.html language=enus -->
## TOPIC 00009: niDMM Cal Adjust Gain VI

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-gain-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-gain-vi.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calibrates the gain coefficient for the supplied Function, Range, and Input Resistance. Refer to the 4065 6½ Digit DMM Calibration Procedure, the NI 4070/4072 6½ Digit FlexDMM Calibration Procedure, or the NI 4071 7½–Digit FlexDMM Calibration Procedure before using this VI. icon Inputs/Outputs cdbl.

### niDMM Cal Adjust Gain VI

Calibrates the gain coefficient for the supplied **Function**, **Range**, and **Input Resistance**.

Refer to the *4065 6½ Digit DMM Calibration Procedure*, the *NI 4070/4072 6½ Digit FlexDMM Calibration Procedure*, or the *NI 4071 7½–Digit FlexDMM Calibration Procedure* before using this VI.

[IMAGE alt='icon' src='nidmm-cal-adjust-gain-vi.png']

#### Inputs/Outputs

| Expected Value — Expected Value specifies the expected value of the measurement. instrument handle — instrument handle identifies a particular instrument calibration session. You obtain this session handle from niDMM Initialize External Cal. Function — Function specifies the calibration mode used to acquire the measurement. For valid ranges, refer to the calibration procedure for your device. Range — Range specifies the range to calibrate. For valid ranges, refer to the calibration procedure for your device. Auto-ranging is not supported for calibration operations. error in (no error) — error in (no error) describes error conditions that occur before this VI runs. If an error occurred before this VI runs, the VI passes the error in value to error out. This VI runs normally only if no error occurs before this VI runs. If an error occurs while this VI runs, it continues and sets its own error status in error out. Use niDMM Error Message to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Input Resistance — Input Resistance specifies the input resistance that the device uses. Input Resistance values are coerced up to the closest input resistance. instrument handle out — instrument handle out returns a handle that you use to identify the instrument in all subsequent instrument driver VI calls. error out — error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-lc-vi.html language=enus -->
## TOPIC 00010: niDMM Cal Adjust LC VI

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-lc-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-lc-vi.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (NI 4082 and NI 4072 only) Performs a specialized LC calibration step depending on the specified Stage. Refer to the calibration procedure for your device before using this VI. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument calibration session. Y

### niDMM Cal Adjust LC VI

(NI 4082 and NI 4072 only) Performs a specialized LC calibration step depending on the specified **Stage**.

Refer to the calibration procedure for your device before using this VI.

[IMAGE alt='icon' src='nidmm-cal-adjust-lc-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument calibration session. You obtain this session handle from niDMM Initialize External Cal. Stage — Stage specifies which of the LC calibration steps to perform. L & C Open (default) Calibrates the open compensation. L & C Short Calibrates the short compensation. L & C 25 Ω Calibrates the 25 Ω resistance. L & C 1 kΩ Calibrates the 1 kΩ resistance. L & C 5 kΩ Calibrates the 5 kΩ resistance. L & C 100 kΩ Calibrates the 100 kΩ resistance. error in (no error) — error in (no error) describes error conditions that occur before this VI runs. If an error occurred before this VI runs, the VI passes the error in value to error out. This VI runs normally only if no error occurs before this VI runs. If an error occurs while this VI runs, it continues and sets its own error status in error out. Use niDMM Error Message to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. instrument handle out — instrument handle out returns a handle that you use to identify the instrument in all subsequent instrument driver VI calls. error out — error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| L & C Open (default) | Calibrates the open compensation. |
| L & C Short | Calibrates the short compensation. |
| L & C 25 Ω | Calibrates the 25 Ω resistance. |
| L & C 1 kΩ | Calibrates the 1 kΩ resistance. |
| L & C 5 kΩ | Calibrates the 5 kΩ resistance. |
| L & C 100 kΩ | Calibrates the 100 kΩ resistance. |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-linearization-vi.html language=enus -->
## TOPIC 00011: niDMM Cal Adjust Linearization VI

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-linearization-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-linearization-vi.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (NI 4065 only) Compensates for any non-linearities. icon Inputs/Outputs cdbl.png Expected Value Expected Value specifies the expected value of the measurement. civrn.png instrument handle instrument handle identifies a particular instrument calibration session. You obtain this session handle from ni

### niDMM Cal Adjust Linearization VI

(NI 4065 only) Compensates for any non-linearities.

[IMAGE alt='icon' src='nidmm-cal-adjust-linearization-vi.png']

#### Inputs/Outputs

| Expected Value — Expected Value specifies the expected value of the measurement. instrument handle — instrument handle identifies a particular instrument calibration session. You obtain this session handle from niDMM Initialize External Cal. Function — Function specifies the calibration mode used to acquire the measurement. For valid modes, refer to the NI 4065 6 1/2 Digit DMM Calibration Procedure. Range — Range specifies the range to calibrate. For valid ranges, refer to the calibration procedure for your device. Auto-ranging is not supported for calibration operations. error in (no error) — error in (no error) describes error conditions that occur before this VI runs. If an error occurred before this VI runs, the VI passes the error in value to error out. This VI runs normally only if no error occurs before this VI runs. If an error occurs while this VI runs, it continues and sets its own error status in error out. Use niDMM Error Message to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Input Resistance — Input Resistance specifies the input resistance that the device uses. Input Resistance values are coerced up to the closest input resistance. instrument handle out — instrument handle out returns a handle that you use to identify the instrument in all subsequent instrument driver VI calls. error out — error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-miscellaneous-vi.html language=enus -->
## TOPIC 00012: niDMM Cal Adjust Miscellaneous VI

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-miscellaneous-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-miscellaneous-vi.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a specialized calibration step depending on the specified Type. Refer to the calibration procedure for your device before using this VI. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument calibration session. You obtain this session handle f

### niDMM Cal Adjust Miscellaneous VI

Performs a specialized calibration step depending on the specified **Type**.

Refer to the calibration procedure for your device before using this VI.

[IMAGE alt='icon' src='nidmm-cal-adjust-miscellaneous-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument calibration session. You obtain this session handle from niDMM Initialize External Cal. Type — Type specifies which of the miscellaneous calibration steps to perform. Voltage Reference (default) Calibrates the voltage reference. Resistance Reference Calibrates the resistance reference. Internal Impedance Calibrates the internal impedance. 2-Wire Leakage Calibrates the 2-wire leakage resistance. 4-Wire Leakage Calibrates the 4-wire leakage resistance. Section Updates calibration information and verifies calibration completeness. error in (no error) — error in (no error) describes error conditions that occur before this VI runs. If an error occurred before this VI runs, the VI passes the error in value to error out. This VI runs normally only if no error occurs before this VI runs. If an error occurs while this VI runs, it continues and sets its own error status in error out. Use niDMM Error Message to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. instrument handle out — instrument handle out returns a handle that you use to identify the instrument in all subsequent instrument driver VI calls. error out — error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Voltage Reference (default) | Calibrates the voltage reference. |
| Resistance Reference | Calibrates the resistance reference. |
| Internal Impedance | Calibrates the internal impedance. |
| 2-Wire Leakage | Calibrates the 2-wire leakage resistance. |
| 4-Wire Leakage | Calibrates the 4-wire leakage resistance. |
| Section | Updates calibration information and verifies calibration completeness. |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-offset-vi.html language=enus -->
## TOPIC 00013: niDMM Cal Adjust Offset VI

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-offset-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-llb/nidmm-cal-adjust-offset-vi.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calibrates the offset and Auto Zero offset for the supplied Function, Range, and Input Resistance. Refer to the calibration procedure for your device before using this VI. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument calibration session. You ob

### niDMM Cal Adjust Offset VI

Calibrates the offset and Auto Zero offset for the supplied **Function**, **Range**, and **Input Resistance**.

Refer to the calibration procedure for your device before using this VI.

[IMAGE alt='icon' src='nidmm-cal-adjust-offset-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument calibration session. You obtain this session handle from niDMM Initialize External Cal. Function — Function specifies the calibration mode used to acquire the measurement. For valid modes, refer to the NI 4065 6 1/2 Digit DMM Calibration Procedure, the NI 4070/4072 6 1/2 Digit FlexDMM Calibration Procedure, or the NI 4071 7 1/2 Digit FlexDMM Calibration Procedure. Range — Range specifies the range to calibrate. For valid ranges, refer to the calibration procedure for your device. Auto-ranging is not supported for calibration operations. error in (no error) — error in (no error) describes error conditions that occur before this VI runs. If an error occurred before this VI runs, the VI passes the error in value to error out. This VI runs normally only if no error occurs before this VI runs. If an error occurs while this VI runs, it continues and sets its own error status in error out. Use niDMM Error Message to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Input Resistance — Input Resistance specifies the input resistance that the device uses. Input Resistance values are coerced up to the closest input resistance. instrument handle out — instrument handle out returns a handle that you use to identify the instrument in all subsequent instrument driver VI calls. error out — error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-llb/nidmm-clear-interchange-warnings-vi.html language=enus -->
## TOPIC 00014: niDMM Clear Interchange Warnings VI

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-llb/nidmm-clear-interchange-warnings-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-llb/nidmm-clear-interchange-warnings-vi.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the list of current interchange warnings. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in (no error) error in (no error) describes error conditions that occur before this VI runs. If an error occurred befo

### niDMM Clear Interchange Warnings VI

Clears the list of current interchange warnings.

[IMAGE alt='icon' src='nidmm-clear-interchange-warnings-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in (no error) describes error conditions that occur before this VI runs. If an error occurred before this VI runs, the VI passes the error in value to error out. This VI runs normally only if no error occurs before this VI runs. If an error occurs while this VI runs, it continues and sets its own error status in error out. Use niDMM Error Message to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. instrument handle out — instrument handle out returns a handle that you use to identify the instrument in all subsequent instrument driver VI calls. error out — error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

IVI Utilities

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-llb/nidmm-close-external-cal-vi.html language=enus -->
## TOPIC 00015: niDMM Close External Cal VI

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-llb/nidmm-close-external-cal-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-llb/nidmm-close-external-cal-vi.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the specified Action, closes the specified external calibration session obtained from niDMM Initialize External Cal, and deallocates resources that it reserved. Refer to the calibration procedure for your device before using this VI. icon Inputs/Outputs civrn.png instrument handle instrumen

### niDMM Close External Cal VI

Performs the specified **Action**, closes the specified external calibration session obtained from niDMM Initialize External Cal, and deallocates resources that it reserved.

Refer to the calibration procedure for your device before using this VI.

[IMAGE alt='icon' src='nidmm-close-external-cal-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument calibration session. You obtain this session handle from niDMM Initialize External Cal. Action — Action specifies whether the driver saves the updated calibration constants. Abort (default) Restores the calibration constants to what they were before you started the external calibration procedure. Save Saves the new calibration constants to the device. These calibration constants are used for any subsequent measurements. error in (no error) — error in (no error) describes error conditions that occur before this VI runs. If an error occurred before this VI runs, the VI passes the error in value to error out. This VI runs normally only if no error occurs before this VI runs. If an error occurs while this VI runs, it continues and sets its own error status in error out. Use niDMM Error Message to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. error out — error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Abort (default) | Restores the calibration constants to what they were before you started the external calibration procedure. |
| Save | Saves the new calibration constants to the device. |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-llb/nidmm-close-vi.html language=enus -->
## TOPIC 00016: niDMM Close VI

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-llb/nidmm-close-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-llb/nidmm-close-vi.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the specified session and deallocates resources that it reserved. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in (no error) error in (no error) describes error conditions that occur before this VI runs. I

### niDMM Close VI

Closes the specified session and deallocates resources that it reserved.

[IMAGE alt='icon' src='nidmm-close-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in (no error) describes error conditions that occur before this VI runs. If an error occurred before this VI runs, the VI passes the error in value to error out. This VI runs normally only if no error occurs before this VI runs. If an error occurs while this VI runs, it continues and sets its own error status in error out. Use niDMM Error Message to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. error out — error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-DMM

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-llb/nidmm-revision-query-vi.html language=enus -->
## TOPIC 00017: niDMM Revision Query VI

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-llb/nidmm-revision-query-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-llb/nidmm-revision-query-vi.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision numbers of the instrument driver and instrument firmware. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in (no error) error in (no error) describes error conditions that occur before this VI r

### niDMM Revision Query VI

Returns the revision numbers of the instrument driver and instrument firmware.

[IMAGE alt='icon' src='nidmm-revision-query-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in (no error) describes error conditions that occur before this VI runs. If an error occurred before this VI runs, the VI passes the error in value to error out. This VI runs normally only if no error occurs before this VI runs. If an error occurs while this VI runs, it continues and sets its own error status in error out. Use niDMM Error Message to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Instrument Driver Revision — Instrument Driver Revision returns a string containing the instrument driver software revision numbers. Note The array must contain at least 256 elements ViChar[256]. instrument handle out — instrument handle out returns a handle that you use to identify the instrument in all subsequent instrument driver VI calls. error out — error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. Firmware Revision — Firmware Revision returns a string containing instrument firmware revision numbers. Note The array must contain at least 256 elements ViChar[256]. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-llb/nidmm-self-cal-vi.html language=enus -->
## TOPIC 00018: niDMM Self Cal VI

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-llb/nidmm-self-cal-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-llb/nidmm-self-cal-vi.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes the self-calibration routine to maintain measurement accuracy. This feature is supported on the NI 4080/4081/4082 and the NI 4070/4071/4072. This VI calls niDMM Reset, and any configurations previous to the call will be lost. All properties will be set to their default values after the call

### niDMM Self Cal VI

Executes the self-calibration routine to maintain measurement accuracy.

Note

Note

niDMM Reset

[IMAGE alt='icon' src='nidmm-self-cal-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in (no error) — error in (no error) describes error conditions that occur before this VI runs. If an error occurred before this VI runs, the VI passes the error in value to error out. This VI runs normally only if no error occurs before this VI runs. If an error occurs while this VI runs, it continues and sets its own error status in error out. Use niDMM Error Message to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. instrument handle out — instrument handle out returns a handle that you use to identify the instrument in all subsequent instrument driver VI calls. error out — error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

#### Details

Refer to [Self-Calibration](/csh?context=nidmm_dmm_self-calibration) for more information.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-latency.html language=enus -->
## TOPIC 00019: Multi Point Acquisition:Advanced:Latency

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-latency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-latency.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of measurements transferred at a time from the instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses the transfer size. Remarks The following table lists the characteristics of this property. Short Name Latency Data type ci32.png Permissions Read/Write High-lev

### Multi Point Acquisition:Advanced:Latency

Specifies the number of measurements transferred at a time from the instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses the transfer size.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Latency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-lccalculationmodel.html language=enus -->
## TOPIC 00020: Configuration:Measurement Options:Capacitance and Inductance:Advanced:Calculation Model

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-lccalculationmodel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-lccalculationmodel.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4082 and NI 4072 only, specifies the type of algorithm that the measurement processing uses for capacitance and inductance measurements. Remarks The following table lists the characteristics of this property. Short Name LC Calculation Model Data type ci32.png Permissions Read/Write High-l

### Configuration:Measurement Options:Capacitance and Inductance:Advanced:Calculation Model

For the NI 4082 and NI 4072 only, specifies the type of algorithm that the measurement processing uses for capacitance and inductance measurements.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LC Calculation Model |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| Auto | -1 | NI-DMM chooses the algorithm based on function and range. |
| --- | --- | --- |
| Series | 0 | NI-DMM uses the series impedance model to calculate capacitance and inductance. |
| Parallel | 1 | NI-DMM uses the parallel admittance model to calculate capacitance and inductance. |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-logicalname.html language=enus -->
## TOPIC 00021: Inherent IVI Attributes:Advanced Session Information:Logical Name

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-logicalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-logicalname.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string containing the logical name of the instrument. Remarks The following table lists the characteristics of this property. Short Name Logical Name Data type cstr.png Permissions Read Only High-level VIs N/A Resettable No

### Inherent IVI Attributes:Advanced Session Information:Logical Name

A string containing the logical name of the instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Logical Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-minfrequency.html language=enus -->
## TOPIC 00022: Configuration:Measurement Options:Min Frequency

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-minfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-minfrequency.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum frequency component of the input signal for AC measurements. This property affects the DMM only when you set the Function property to AC measurements. The valid range is 1 Hz-300 kHz for the NI 4080/4081/4082 and NI 4070/4071/4072 and 10 Hz-100 Hz for the NI 4065. Remarks The f

### Configuration:Measurement Options:Min Frequency

Specifies the minimum frequency component of the input signal for AC measurements. This property affects the DMM only when you set the Function property to AC measurements. The valid range is 1 Hz-300 kHz for the NI 4080/4081/4082 and NI 4070/4071/4072 and 10 Hz-100 Hz for the NI 4065.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Min Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure AC Bandwidth |
| Resettable | No |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-numberofaverages.html language=enus -->
## TOPIC 00023: Configuration:Advanced:Number Of Averages

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-numberofaverages.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-numberofaverages.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of averages to perform in a measurement. For the NI 4080/4081/4082 and NI 4070/4071/4072, this property applies only when the aperture time is not set to Auto and Auto Zero is ON. The Number of Averages Property will be ignored otherwise. The default is 4 for 7 1/2 digits; other

### Configuration:Advanced:Number Of Averages

Specifies the number of averages to perform in a measurement. For the NI 4080/4081/4082 and NI 4070/4071/4072, this property applies only when the aperture time is not set to Auto and Auto Zero is ON. The Number of Averages Property will be ignored otherwise. The default is 4 for 7 1/2 digits; otherwise, the default is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number Of Averages |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-numberoflcmeasurementstoaverage.html language=enus -->
## TOPIC 00024: Configuration:Measurement Options:Capacitance and Inductance:Number of LC Measurements To Average

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-numberoflcmeasurementstoaverage.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-numberoflcmeasurementstoaverage.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4082 and NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading. Remarks The following table lists the characteristics of this property. Short Name Number of LC Measurements To Average Data type ci32.png Permissions Read/Write High-level VIs N/A Res

### Configuration:Measurement Options:Capacitance and Inductance:Number of LC Measurements To Average

For the NI 4082 and NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of LC Measurements To Average |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-offsetcompensatedohms.html language=enus -->
## TOPIC 00025: Configuration:Measurement Options:Offset Compensated Ohms

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-offsetcompensatedohms.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-offsetcompensatedohms.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables offset compensated ohms. Remarks The following table lists the characteristics of this property. Short Name Offset Compensated Ohms Data type ci32.png Permissions Read/Write High-level VIs niDMM Configure Offset Comp Ohms Resettabl

### Configuration:Measurement Options:Offset Compensated Ohms

For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables offset compensated ohms.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Offset Compensated Ohms |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Offset Comp Ohms |
| Resettable | No |

| Off | 0 | Disables Offset Compensated Ohms. |
| --- | --- | --- |
| On | 1 | Enables Offset Compensated Ohms. |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-sampledelaymode.html language=enus -->
## TOPIC 00026: Multi Point Acquisition:Sample Delay Mode

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-sampledelaymode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-sampledelaymode.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies when the Sample Interval property is used. Set this property before calling niDMM Configure Multi Point if you configure the properties for multipoint measurements using the niDMM Configure Multi Point VI. The NI 4080/4081/4082 are not supported. 0 IVI compliant The Sample Interval propert

### Multi Point Acquisition:Sample Delay Mode

Specifies when the [Sample Interval](/csh?topicname=pnidmm-sampleinterval.html) property is used. Set this property before calling [niDMM Configure Multi Point](/csh?context=nidmm_dmmviref_nidmm_configure_multi_point) if you configure the properties for multipoint measurements using the [niDMM Configure Multi Point](/csh?context=nidmm_dmmviref_nidmm_configure_multi_point) VI.

Note

| 0 | IVI compliant | The Sample Interval property is only used when the Sample Trigger is set to Interval. |
| --- | --- | --- |
| 1 | Not IVI compliant | The Sample Interval property is used as a delay after any type of Sample Trigger. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample Delay Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-sampleinterval.html language=enus -->
## TOPIC 00027: Multi Point Acquisition:Sample Interval

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-sampleinterval.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-sampleinterval.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of time in seconds the DMM waits between measurement cycles. This property only applies when the Sample Trigger property is set to INTERVAL. The default value (-1) ensures that the DMM settles for a recommended time, which is the same as using an immediate trigger. The NI 4065 a

### Multi Point Acquisition:Sample Interval

Specifies the amount of time in seconds the DMM waits between measurement cycles. This property only applies when the Sample Trigger property is set to INTERVAL. The default value (-1) ensures that the DMM settles for a recommended time, which is the same as using an immediate trigger.

The NI 4065 and NI 4070/4071/4072 use the value specified in this property as additional delay. On these devices, the onboard timing resolution is 34.72 ns and the valid range is 0-149 s.

Only positive values are valid when setting the sample interval.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample Interval |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Multi Point |
| Resettable | No |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-sampletrigger.html language=enus -->
## TOPIC 00028: Multi Point Acquisition:Sample Trigger

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-sampletrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-sampletrigger.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sample trigger source. To determine which values are supported by each device, refer to the LabVIEW Trigger Routing section in the NI Digital Multimeters Help. Remarks The following table lists the characteristics of this property. Short Name Sample Trigger Data type ci32.png Permissio

### Multi Point Acquisition:Sample Trigger

Specifies the sample trigger source.

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) section in the *NI Digital Multimeters Help*.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample Trigger |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Multi Point |
| Resettable | No |

| Immediate | 1 | No trigger specified |
| --- | --- | --- |
| Interval | 10 | Interval trigger |
| External | 2 | Pin 9 on the AUX Connector |
| Software Trig | 3 | Configures the DMM to wait until niDMM Send Software Trigger is called. |
| TTL 0 | 111 | PXI Trigger Line 0 |
| TTL 1 | 112 | PXI Trigger Line 1 |
| TTL 2 | 113 | PXI Trigger Line 2 |
| TTL 3 | 114 | PXI Trigger Line 3 |
| TTL 4 | 115 | PXI Trigger Line 4 |
| TTL 5 | 116 | PXI Trigger Line 5 |
| TTL 6 | 117 | PXI Trigger Line 6 |
| TTL 7 | 118 | PXI Trigger Line 7 |
| PXI Star | 131 | PXI Star trigger line |
| LBR Trig 1 | 1004 | Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis |
| AUX Trig 1 | 1001 | Pin 3 on the AUX connector |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-sampletrigslope.html language=enus -->
## TOPIC 00029: Multi Point Acquisition:Sample Trig Slope

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-sampletrigslope.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-sampletrigslope.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the edge of the signal from the specified sample trigger source on which the DMM is triggered. Remarks The following table lists the characteristics of this property. Short Name Sample Trig Slope Data type ci32.png Permissions Read/Write High-level VIs N/A Resettable No Positive 0 The driv

### Multi Point Acquisition:Sample Trig Slope

Specifies the edge of the signal from the specified sample trigger source on which the DMM is triggered.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample Trig Slope |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| Positive | 0 | The driver triggers on the rising edge of the trigger signal. |
| --- | --- | --- |
| Negative | 1 | The driver triggers on the falling edge of the trigger signal. |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-secondaryerror.html language=enus -->
## TOPIC 00030: Obsolete:Inherent IVI Attributes:Error Info:Secondary Error

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-secondaryerror.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-secondaryerror.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: An optional code that provides additional information concerning the primary error condition. The error and warning values can be status codes defined by IVI, VISA, class drivers, or specific drivers. Zero indicates no additional information. Remarks The following table lists the characteristics of

### Obsolete:Inherent IVI Attributes:Error Info:Secondary Error

An optional code that provides additional information concerning the primary error condition. The error and warning values can be status codes defined by IVI, VISA, class drivers, or specific drivers. Zero indicates no additional information.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Secondary Error |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-settletime.html language=enus -->
## TOPIC 00031: Configuration:Advanced:Settle Time

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-settletime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-settletime.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the settling time in seconds. Use this property to override the default settling time. To return to the default, set this property to Auto (-1). Remarks The following table lists the characteristics of this property. Short Name Settle Time Data type cdbl.png Permissions Read/Write High-lev

### Configuration:Advanced:Settle Time

Specifies the settling time in seconds. Use this property to override the default settling time. To return to the default, set this property to Auto (-1).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Settle Time |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-thermistorc.html language=enus -->
## TOPIC 00032: Configuration:Measurement Options:Temperature:Thermistor:Thermistor C

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-thermistorc.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-thermistorc.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Steinhart-Hart C coefficient for thermistor scaling when the Thermistor Type property is set to Custom. Remarks The following table lists the characteristics of this property. Short Name Thermistor C Data type cdbl.png Permissions Read/Write High-level VIs N/A Resettable No

### Configuration:Measurement Options:Temperature:Thermistor:Thermistor C

Specifies the Steinhart-Hart C coefficient for thermistor scaling when the **Thermistor Type property** is set to Custom.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Thermistor C |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-thermistortype.html language=enus -->
## TOPIC 00033: Configuration:Measurement Options:Temperature:Thermistor:Thermistor Type

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-thermistortype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-thermistortype.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the thermistor type. Remarks The following table lists the characteristics of this property. Short Name Thermistor Type Data type ci32.png Permissions Read/Write High-level VIs N/A Resettable No Custom 0 Performs Steinhart-Hart thermistor scaling with the user-specified A, B, and C coeffic

### Configuration:Measurement Options:Temperature:Thermistor:Thermistor Type

Specifies the thermistor type.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Thermistor Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| Custom | 0 | Performs Steinhart-Hart thermistor scaling with the user-specified A, B, and C coefficients. |
| --- | --- | --- |
| 44004 | 1 | Performs scaling for an Omega Series 44004 thermistor. |
| 44006 | 2 | Performs scaling for an Omega Series 44006 thermistor. |
| 44007 | 3 | Performs scaling for an Omega Series 44007 thermistor. |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-thermocoupletype.html language=enus -->
## TOPIC 00034: Configuration:Measurement Options:Temperature:Thermocouple:Thermocouple Type

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-thermocoupletype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-thermocoupletype.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the thermocouple type. Remarks The following table lists the characteristics of this property. Short Name Thermocouple Type Data type ci32.png Permissions Read/Write High-level VIs N/A Resettable No B 1 Thermocouple type B E 4 Thermocouple type E J 6 Thermocouple type J K 7 Thermocouple ty

### Configuration:Measurement Options:Temperature:Thermocouple:Thermocouple Type

Specifies the thermocouple type.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Thermocouple Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| B | 1 | Thermocouple type B |
| --- | --- | --- |
| E | 4 | Thermocouple type E |
| J | 6 | Thermocouple type J |
| K | 7 | Thermocouple type K |
| N | 8 | Thermocouple type N |
| R | 9 | Thermocouple type R |
| S | 10 | Thermocouple type S |
| T | 11 | Thermocouple type T |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-transducertype.html language=enus -->
## TOPIC 00035: Configuration:Measurement Options:Temperature:Transducer Type

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-transducertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-transducertype.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the transducer type. Remarks The following table lists the characteristics of this property. Short Name Transducer Type Data type ci32.png Permissions Read/Write High-level VIs N/A Resettable No Thermocouple 1 Use for thermocouple measurements. Thermistor 2 Use for thermistor measurements.

### Configuration:Measurement Options:Temperature:Transducer Type

Specifies the transducer type.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Transducer Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| Thermocouple | 1 | Use for thermocouple measurements. |
| --- | --- | --- |
| Thermistor | 2 | Use for thermistor measurements. |
| 2-Wire RTD | 3 | Use for 2-wire RTD measurements. |
| 4-Wire RTD | 4 | Use for 4-wire RTD measurements. |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-triggercount.html language=enus -->
## TOPIC 00036: Multi Point Acquisition:Trigger Count

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-triggercount.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-triggercount.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of triggers the DMM receives before returning to the Idle state. This property can be set to any positive ViInt32 value for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082. Refer to Multiple Point Acquisitions in the NI Digital Multimeters Help for more information. Remark

### Multi Point Acquisition:Trigger Count

Specifies the number of triggers the DMM receives before returning to the Idle state. This property can be set to any positive ViInt32 value for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082.

Refer to [Multiple Point Acquisitions](/csh?context=nidmm_dmm_multi_point) in the *NI Digital Multimeters Help*for more information.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Multi Point |
| Resettable | No |

Parent topic:

niDMM Properties

<!--NI_TOPIC bundle=ni-dmm-labview-api-ref path=instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-triggerdelay.html language=enus -->
## TOPIC 00037: Trigger:Trigger Delay

- bundle_id: `ni-dmm-labview-api-ref`
- source_path: `instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-triggerdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-labview-api-ref/raw/resource/enus/instr-lib/nidmm/nidmm-rc/nidmm/pnidmm-triggerdelay.html
- document_id: `ni-dmm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement. The default value is Auto Delay (-1), which means that the DMM waits an appropriate settling time before taking the measurement. The NI 4080/4081/4082 uses the value specified in this prop

### Trigger:Trigger Delay

Specifies the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement. The default value is Auto Delay (-1), which means that the DMM waits an appropriate settling time before taking the measurement.

The NI 4080/4081/4082 uses the value specified in this property as additional settling time. The valid range for Trigger Delay is Auto Delay (-1) or 0.0 - 150.0 seconds, and the onboard timing resolution is 10.0 ns.

The NI 4065 and NI 4070/4071/4072 use the value specified in this property as additional settling time. For these devices, the valid range for Trigger Delay is Auto Delay (-1) or 0.0 - 149.0 seconds and the onboard timing resolution is 34.72 ns.

Use positive values to set the trigger delay in seconds.

Valid Range: Auto Delay (-1.0), 0.0-149.0 seconds (NI 4065 and NI 4070/4071/4072)

Default Value: Auto Delay

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Trigger |
| Resettable | No |

Parent topic:

niDMM Properties
